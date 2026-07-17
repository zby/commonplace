---
description: "LLM-Wiki-v3 review: Markdown+git wiki with schema validation, provenance-checked ingest, pending review, and hybrid pull retrieval"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-18"
---

# LLM-Wiki-v3

LLM-Wiki-v3, by Vivek, is a Python scaffold for a domain-agnostic Markdown+git knowledge wiki meant for humans and LLM agents. At the reviewed commit it implements schema-backed page validation, source-document ingest into `pending/`, span/provenance checks, human review into `knowledge/`, rebuildable BM25/graph/optional dense indexes, query evaluation, and audit logging. The README still labels the repository "Phase 0", but the code contains later ingest, retrieval, review, and eval paths; no MCP server or context compiler is implemented in the inspected tree ([README.md](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/README.md), [src/wiki/cli/__init__.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/cli/__init__.py)).

**Repository:** https://github.com/vvvvvivekkk/LLM-Wiki-v3

**Reviewed commit:** [267541db838cbca757a112bd0cfa47fa61eb5fb2](https://github.com/vvvvvivekkk/LLM-Wiki-v3/commit/267541db838cbca757a112bd0cfa47fa61eb5fb2)

**Source directory:** `related-systems/vvvvvivekkk--LLM-Wiki-v3`

## Core Ideas

**Markdown and git are the authoritative memory store.** Pages live under namespace directories in `knowledge/`, raw source documents are content-addressed under `raw/<sha256>/`, autonomous proposals land in `pending/`, and derived indexes live under `indexes/`. The README states that vectors, BM25, and the graph are rebuildable from Markdown, and the code follows that shape: `rebuild()` loads current pages and recreates BM25, graph, optional dense vector indexes, and a manifest ([README.md](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/README.md), [src/wiki/retrieve/rebuild.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/retrieve/rebuild.py)).

**The schema is a system-definition artifact.** `schema/namespaces.yaml` maps namespaces to schema files and storage directories; namespace schemas deep-merge `_base.schema.yaml`, which requires ids, version, timestamps, source spans, supersession fields, typed edges, and tags. `wiki validate` checks frontmatter against the effective JSON Schema and checks that every `[^src:N]` body footnote keys into the `sources` array ([schema/namespaces.yaml](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/schema/namespaces.yaml), [schema/v1/_base.schema.yaml](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/schema/v1/_base.schema.yaml), [src/wiki/schema_loader.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/schema_loader.py), [src/wiki/validate.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/validate.py)).

**Ingest is provenance-first acquisition, not hidden memory rewriting.** The extractor must call a structured `propose_pages` tool and return verbatim quotes for each claim. The pipeline stores the raw source, chunks it, asks the extractor, locates quoted text in the source, builds pages with `sources` spans, validates schema and footnotes, runs span overlap checks, deduplicates ids, writes valid pages to `pending/`, and writes a manifest. Escalation to a stronger extractor is attempted only for chunks whose pages fail validation ([src/wiki/extract.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/extract.py), [src/wiki/ingest/pipeline.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/ingest/pipeline.py), [src/wiki/ingest/spancheck.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/ingest/spancheck.py)).

**Human review is the promotion boundary.** `wiki review` lists pending Markdown pages, optionally opens them in `$EDITOR`, then accepts, rejects, skips, or quits. Accepting moves the page into the namespace's `knowledge/` directory and can commit it to git; rejecting deletes the pending page. The diff helper flags same-id patches as possible contradictions but does not auto-resolve them ([src/wiki/review.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/review.py), [src/wiki/ingest/diff.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/ingest/diff.py)).

**Context efficiency is hybrid retrieval over explicit pages, not automatic context assembly.** `wiki query` combines SQLite FTS5 BM25, optional fastembed vectors, graph walks from lexically matched entities and aliases, reciprocal-rank fusion, and optional cross-encoder reranking. It returns page ids, scores, retrieval paths, and source ids; it does not compile prompt context, enforce a token budget, or push memory into a model call ([src/wiki/retrieve/query.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/retrieve/query.py), [src/wiki/retrieve/bm25.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/retrieve/bm25.py), [src/wiki/retrieve/dense.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/retrieve/dense.py), [src/wiki/retrieve/graph.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/retrieve/graph.py), [src/wiki/retrieve/rerank.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/retrieve/rerank.py)).

**The evaluation layer is small but real.** Retrieval eval computes NDCG, MRR, and recall over a JSONL query dataset; ingest eval reuses span checks to score faithfulness against raw sources. This makes retrieval and ingest changes observable, although the repository does not yet implement the README's stronger "no change ships without a delta" gate as an enforced release workflow ([src/wiki/eval/harness.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/eval/harness.py), [src/wiki/eval/ingest_eval.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/eval/ingest_eval.py), [src/wiki/cli/__init__.py](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/cli/__init__.py)).

## Artifact analysis

- **Storage substrate:** `repo` `files` `sqlite` `graph` `vector` — The source of truth is git-versioned Markdown, YAML schemas, raw documents, pending proposals, audit JSONL, and eval datasets; derived BM25 and graph indexes persist in SQLite, and optional dense vectors also persist in SQLite as packed blobs.
- **Representational form:** `prose` `symbolic` `parametric` — Page bodies and source-grounded claims are prose; frontmatter schemas, typed edges, provenance spans, supersession fields, CLI commands, audit records, manifests, eval datasets, graph edges, and retrieval scores are symbolic; optional fastembed embeddings and cross-encoder reranking add parametric retrieval state.
- **Lineage:** `authored` `imported` — Schemas, instructions, code, tests, and accepted curated pages are authored; ingest imports external source documents and LLM-proposed pages into `pending/` with located source spans. The inspected code does not learn durable artifacts from agent session logs, tool traces, trajectories, or runtime action traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` — Accepted pages are knowledge artifacts; `AGENTS.md` instructs the extractor; schemas, validation, span checks, and review acceptance enforce admissibility before promotion; namespaces and typed edges route storage and graph traversal; BM25, graph walks, RRF, vectors, rerankers, and evals rank retrieval candidates.

**Knowledge pages.** The retained memory pages are Markdown records whose frontmatter must include stable ids, namespace type, schema version, source spans, supersession metadata, typed edges, and tags. Their body claims are prose, but each substantive claim is expected to cite a `sources` entry with a `[^src:N]` footnote.

**Raw sources and pending proposals.** Raw documents are content-addressed files, while pending pages and manifests are imported acquisition artifacts. Their authority is deliberately weaker than accepted knowledge: they are evidence and candidates until a reviewer accepts or rejects them.

**Schemas and extractor instructions.** `schema/` and `AGENTS.md` are authored system-definition artifacts. They constrain the shape of memory and the extraction behavior: no numeric confidence, no uncited claims, structured output only, no silent contradiction resolution, and namespace-specific allowed edges.

**Derived retrieval indexes.** `indexes/bm25.sqlite`, `indexes/graph.sqlite`, `indexes/vectors.sqlite`, and `indexes/manifest.json` are rebuildable access structures. They rank and route recall, but they are not sources of truth; `load_pages()` excludes superseded pages by default before indexing or querying.

**Audit and eval artifacts.** `audit/log.jsonl` records ingest and review operations with inputs, model, token, cost, duration, success, and summary fields. Evaluation outputs and baselines are descriptive governance artifacts: they make retrieval and ingest behavior visible but do not, in the inspected code, automatically block merges or promotion.

Promotion path: LLM-Wiki-v3 can move external source text into structured pending Markdown, then into accepted knowledge through human review, then into rebuildable retrieval indexes and eval baselines. It does not promote memories into executable tools, model weights, automatic prompt-injection policies, or enforced runtime agent gates.

## Comparison with Our System

| Dimension | LLM-Wiki-v3 | Commonplace |
|---|---|---|
| Primary purpose | Domain-agnostic Markdown+git wiki substrate with provenance-first ingest and retrieval | Methodology KB for agent-operated knowledge bases |
| Main artifact | Namespace-scoped Markdown pages with schemas, source spans, typed edges, and supersession fields | Typed Markdown notes, reviews, sources, instructions, ADRs, indexes, and validation |
| Write path | LLM extraction from source documents into `pending/`, human review into `knowledge/`, git commit on accept | Agent/human authored artifacts, skills, validation, semantic review, curated indexes |
| Read path | Explicit hybrid pull retrieval through `wiki query` | Explicit pull through `rg`, authored links, indexes, skills, and curated navigation |
| Governance | JSON Schema, footnote/source checks, quote location, span overlap, audit log, eval reports | Collection/type contracts, schemas, link checks, source citations, semantic review gates |

LLM-Wiki-v3 is unusually close to Commonplace's design instincts: source-of-truth files, versioned schemas, provenance over confidence scores, no hidden LLM writes, and promotion through a review boundary. The biggest difference is domain and maturity. LLM-Wiki-v3 is a generic wiki kernel with page namespaces and an ingest/retrieval stack; Commonplace is a working methodology KB whose artifact contracts are themselves content.

The strongest divergence is query-time authority. LLM-Wiki-v3 already has hybrid retrieval and explicit eval metrics, but retrieved pages are returned as ranked ids and provenance, not compiled into an agent invocation. Commonplace has less parametric retrieval machinery but a stronger body of operational instructions and review workflows around when a retained artifact should guide a future agent.

### Borrowable Ideas

**Require quote-location before accepting LLM extraction.** Ready for source-ingest workflows. Commonplace source snapshots and generated notes could reject extracted claims when their supporting quote cannot be located in the source text, before semantic review ever runs.

**Prefer provenance chains over numeric confidence.** Ready as a design principle. LLM-Wiki-v3's refusal to store confidence floats fits Commonplace: trust should come from source identity, spans, extractor identity, review status, and validation history.

**Keep autonomous writes in `pending/`.** Ready for trace or source import tools. Commonplace already uses workshops and review runs; a stricter pending directory for machine-proposed library artifacts would make automated acquisition safer.

**Treat retrieval changes as eval-bearing changes.** Needs concrete datasets first. LLM-Wiki-v3's NDCG/MRR/recall harness is a practical shape for future Commonplace retrieval tools once we have stable query sets for KB navigation.

**Do not borrow roadmap claims as architecture.** The README's MCP/context-compiler direction is sensible, but Commonplace should only copy implemented mechanisms: schema validation, span grounding, pending review, and rebuildable indexes.

## Write side

**Write agency:** `manual` `automatic` — Humans can author or edit Markdown pages and review pending proposals; the ingest pipeline automatically stores raw source documents, extracts proposed pages with an LLM, builds frontmatter/source spans, validates them, writes valid candidates and manifests to `pending/`, rebuilds indexes on command, writes eval baselines, and appends audit log records.

**Curation operations:** `none` — Automatic writes are acquisition, indexing, audit, and evaluation-output generation. The code deduplicates proposed ids within one ingest batch and flags same-id patches for human review, but it does not automatically consolidate, deduplicate, evolve, synthesize, invalidate, decay, or promote memory already accepted in the knowledge directory.

## Read-back

**Read-back:** `pull` — Retained memory re-enters use when an operator or host explicitly runs validation, rebuild, query, review, or eval commands. The code implements no MCP server, no context compiler, and no pre-invocation hook that injects wiki memory into an agent prompt.

`wiki query` is a retrieval API, not a read-back loop. It searches current non-superseded pages through BM25, optional dense vectors, graph traversal from entity/alias matches, RRF fusion, and optional reranking, then prints page ids, scores, contributing retrieval paths, and provenance source ids. A host could turn those results into push context for an agent, but that orchestration is not present in the repository.

Selection is bounded by `k`, component top-k values, graph depth, and the existence of rebuilt indexes. There is no token budget, no progressive disclosure ladder from summary to full page, and no faithfulness test showing whether a future model actually obeys retrieved pages after a host includes them.

## Curiosity Pass

**The README is behind or ahead of the code, depending on the section.** It says Phase 0 only implements schema loading and page validation, but the CLI already exposes ingest, review, rebuild, query, and eval. It also advertises MCP and context compilation as future phases; those were not implemented in the inspected source.

**The provenance model is stronger than the retrieval model.** Ingest can locate quotes, compute spans, reject unsupported claims, and preserve raw documents. Query currently returns page ids and source ids rather than claim-level snippets or spans, so retrieval does not yet surface the strongest available evidence directly.

**"No retention decay" is a policy, but supersession is still mostly manual.** The schema has `superseded_by` and `supersedes`; `load_pages()` excludes superseded pages by default. The code flags possible contradictions on patch proposals, but a reviewer must make the supersession decision.

**Deduplication is intentionally shallow.** Ingest dedupes duplicate proposed ids within a batch. It does not attempt semantic duplicate detection across existing pages, which keeps authority with review but leaves scale pressure for later.

**The optional dense path preserves local-first behavior.** Embeddings and reranking use `fastembed` locally when installed. Without it, retrieval still works through BM25 and graph, so the system degrades to inspectable symbolic indexes.

## What to Watch

- Whether the MCP server and context compiler appear in code. That would likely change read-back from pull-only to both and force a new context-budget analysis.
- Whether eval commands become hard gates for ingest, retrieval changes, or review acceptance. That would upgrade evals from reporting to enforcement.
- Whether query results start returning snippets, source spans, or claim-level evidence. That would better connect retrieval to the system's provenance model.
- Whether supersession gains automated stale-claim detection or contradiction handling. That would introduce an automatic `invalidate` operation.
- Whether dense retrieval becomes mandatory or remains optional. That changes how inspectable and dependency-light the memory substrate stays.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: LLM-Wiki-v3 separates Markdown knowledge, schemas, source spans, indexes, audit logs, and eval artifacts by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - classifies: the implemented system stores and retrieves memory, but does not push it into agent context.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: accepted wiki pages and raw sources serve as evidence, reference, and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: schemas, extractor instructions, validation, span checks, review promotion, and retrieval policy carry binding force.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: graph and lexical retrieval depend on ids, aliases, typed edges, wikilinks, tags, and query terms being available as symbols.
