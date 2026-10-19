---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LLM-Wiki-v3 memory: source-derived Markdown, curated admission, rebuildable indexes and evaluator read-back, without shipped agent context compilation."
run-id: AAS-2026-10-18-llm-wiki-v3-0c553a3118eb-01
source-identity: "https://github.com/vvvvvivekkk/LLM-Wiki-v3"
reviewed-boundary: "267541db838cbca757a112bd0cfa47fa61eb5fb2"
---

# LLM-Wiki-v3 memory report

## Boundary and evidence

The memory boundary covers the shipped source store, proposed and accepted pages, instruction delivery, retrieval derivatives, review/withdrawal, query generation and evaluation. It follows the whole-system boundary, not an imagined MCP deployment ([boundary](boundary.md#boundary-and-evidence)). All source citations below are SRC-1 at the reviewed commit. Implementation findings are static; doctrine is labelled separately. No target code, tests, providers or examples were executed.

Direct reads covered `src/wiki/cli/__init__.py`, `src/wiki/extract.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/ingest/hashing.py`, `src/wiki/ingest/chunk.py`, `src/wiki/ingest/diff.py`, `src/wiki/review.py`, `src/wiki/validate.py`, `src/wiki/audit.py`, `src/wiki/config.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/query.py`, `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/bm25.py`, `src/wiki/retrieve/dense.py`, `src/wiki/retrieve/graph.py`, `src/wiki/retrieve/rerank.py`, `src/wiki/eval/baseline_retriever.py`, `src/wiki/eval/harness.py`, `scripts/pre-commit`, `AGENTS.md` and the sample `knowledge/entities/ada-lovelace.md`. The seed driver's complete `main` was read; individual page specifications were not audited. Function/call-site searches covered `src/`, the seed driver, `README.md` and `Makefile`. Span-check internals, schema contracts, tracked inventory and saved baseline characterization rely on the supplied boundary/runtime, not new complete reads.

Raw documents and derived index artifacts are not supplied in this tracked snapshot; provider state and downloaded model artifacts are outside the available source implementation. These gaps prevent replay of provenance, inspection of actual stored vectors and claims about provider retention. Uninspected seed specifications and most corpus bodies prevent a corpus-wide content-quality judgment. Human interpretation after browsing and downstream answering-agent prompt construction are excluded responsibilities, not implemented consumers inferred from the retrieval label.

| Entry point / memory operation | Source paths (SRC-1) | Coverage and evidence basis |
| --- | --- | --- |
| Ingest, raw reload, chunk context, escalation | `src/wiki/cli/__init__.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/ingest/hashing.py`, `src/wiki/ingest/chunk.py`, `src/wiki/extract.py` | Direct; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-raw-source](#mem-obj-raw-source), annotations below |
| Root instruction delivery / structured proposal tool | `AGENTS.md`, `src/wiki/extract.py`, `src/wiki/ingest/pipeline.py` | Direct; [RT-BAP-ingest-instructions](runtime.md#rt-bap-ingest-instructions); proposal tool returns data, not arbitrary filesystem operations |
| Quote/schema/span checks, pending manifest, changed-body flag | `src/wiki/ingest/pipeline.py`, `src/wiki/validate.py`, `src/wiki/ingest/diff.py`, `src/wiki/ingest/spancheck.py` | Direct except span-check internals supplied by [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy); [MEM-OBJ-ingest-manifest](#mem-obj-ingest-manifest) |
| Review edit/accept/reject/skip; callable accept/reject | `src/wiki/cli/__init__.py`, `src/wiki/review.py` | Direct; [RT-RTE-page-review](runtime.md#rt-rte-page-review); file move can replace current content |
| Validation commands and optional Git hook | `src/wiki/validate.py`, `scripts/pre-commit`, `src/wiki/cli/__init__.py` | Direct; structural validation, not span rechecking; [RT-RTE-page-review](runtime.md#rt-rte-page-review) |
| Curated seed direct writes and temporary-file cleanup | `scripts/seed_corpus.py` | Direct `main`; [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed); page-spec correctness uninspected |
| Rebuild and exposed component build/search operations | `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/bm25.py`, `src/wiki/retrieve/dense.py`, `src/wiki/retrieve/graph.py` | Direct; [RT-RTE-index-query](runtime.md#rt-rte-index-query); three separately replaceable derivatives below |
| Query, adapters, optional rerank, graph neighbors | `src/wiki/retrieve/query.py`, `src/wiki/retrieve/rerank.py`, `src/wiki/retrieve/graph.py` | Direct; [RT-RTE-index-query](runtime.md#rt-rte-index-query); storage APIs are not proof of an external deployed consumer |
| Retrieval baseline direct corpus loading, component evaluation, ingest evaluation | `src/wiki/eval/baseline_retriever.py`, `src/wiki/eval/harness.py`, `src/wiki/cli/__init__.py` | Direct; [RT-RTE-eval-report](runtime.md#rt-rte-eval-report), including alternative non-index read-back |
| Bootstrap queries, caller-selectable output | `src/wiki/cli/__init__.py` | Direct; [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap); distinct default staging and possible direct active-dataset write |
| Audit and evaluation artifacts | `src/wiki/audit.py`, `src/wiki/eval/harness.py`, `src/wiki/cli/__init__.py` | Direct producers/consumers; [MEM-OBJ-audit-log](#mem-obj-audit-log), [MEM-OBJ-eval-results](#mem-obj-eval-results); no automatic policy revision shown |
| Browsing catalog, source/note namespaces, MCP/compile/maintenance labels | `knowledge/_index.md`, `schema/namespaces.yaml`, `README.md`, `Makefile`, `src/wiki/cli/__init__.py` | Catalog/registry from supplied boundary; CLI direct and source search. Registered directories are loaded generically. No inspected CLI compile/MCP/supersede command; labels alone do not establish autonomous maintenance or stored query-answer reuse |

## Core ideas

1. Source prose becomes localized pages with source-span pointers, not a remembered conversation. The retained page can preserve claims and evidence locations without preserving why a model selected or paraphrased them. Existing-corpus content is not fed into the extraction invocation, although later code compares same-ID bodies ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/wiki/extract.py`, `src/wiki/ingest/diff.py`).
2. Admission is path-specific. Interactive review supplies a human content decision, but callable acceptance and the curated seed driver have different controls. Starting seed or ingest is not per-page approval. Structural checks, lexical evidence checks and human correctness are different warrants ([RT-RTE-page-review](runtime.md#rt-rte-page-review), [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed), [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy)).
3. Content and access derivatives have different lifetimes. Knowledge edits do not rebuild indexes. Current-page filtering is real at load/build, but does not universally remove stale identifiers from query output. The active rerank branch is an important counterexample to a blanket claim that all branches are unfiltered ([RT-RTE-index-query](runtime.md#rt-rte-index-query); SRC-1, `src/wiki/retrieve/query.py`).
4. Retrieval selects identifiers, not a budgeted answering prompt. By contrast, bootstrap explicitly supplies retained page bodies to a later model call. That is an implemented memory-to-model path, but its purpose is candidate evaluation data, not answering the user's question ([RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap); SRC-1, `src/wiki/cli/__init__.py`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw-source
Label: Retained raw source content

Source-native identity: `raw/<sha256>/source<suffix>` (or `source`). Substrate: filesystem bytes, decoded UTF-8 by `load_raw_text`. Document prose is natural-language source material; its hash identity is symbolic, not a confidence score. Lineage: original file bytes copied before extraction; the seed driver supplies authored text through temporary files. Consumers: pipeline quote location and source checking, plus later CLI ingest evaluation. The source text is an evidence reference for lexical checks, not an authoritative truth oracle. Raw retention survives pending rejection. No extraction reasoning is stored here. Distinct from the source-ingest route and its manifest; closest supplied record is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1, `src/wiki/ingest/hashing.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/cli/__init__.py`, `scripts/seed_corpus.py`.

> (raw_dir / stored_name).write_bytes(data)
> --- `src/wiki/ingest/hashing.py`

> return candidates[0].read_text(encoding="utf-8")
> --- `src/wiki/ingest/hashing.py`

#### MEM-OBJ-raw-meta
Label: Raw source access metadata

Source-native identity: `raw/<sha256>/meta.json`. Symbolic JSON on filesystem: source ID, origin, filenames, timestamps and byte count. It is neither the source prose nor a readable summary of it. Software constructs it from bytes and caller origin. Its existence makes later `store_raw` calls return early; the loader instead discovers a `source*` file. Thus a metadata sidecar can suppress re-storage without proving that its body is intact. Actual stored-body integrity was not replayed. No independent human content gate is imposed by `store_raw`. Distinct metadata object associated with [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). SRC-1, `src/wiki/ingest/hashing.py`.

> if (raw_dir / "meta.json").exists():
>     return sha, raw_dir
> --- `src/wiki/ingest/hashing.py`

#### MEM-OBJ-page-body
Label: Proposed and admitted page prose

Source-native identity: Markdown body of `ProposedPage` / `PageRecord`, staged in `pending/<id>.md`, then placed under registry namespace directories in `knowledge/`. Natural-language claims remain natural language when humans or bootstrap interpret them; embedded citation/wikilink markers have separate fixed consumers. Lineage: model paraphrase/extraction, human review edits, or curated seed specifications. Curation chooses content rather than merely copying raw traces. The sample retained `knowledge/entities/ada-lovelace.md` has three prose claims, citation markers and `extractor: human` metadata; this is a source-authored artifact, not evidence that this analysis observed seed execution. Extraction/admission reasons and rejected alternative wording are not fields of the retained page.

Later consumers include `search_text` for indexes/reranking, baseline lexical evaluation, ingest faithfulness and bootstrap's model prompt. Bodies are not returned by `retrieve`. Distinct material object crossing several supplied routes, not a duplicate route: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-page-review](runtime.md#rt-rte-page-review), [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed), [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap). SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/retrieve/store.py`, `src/wiki/cli/__init__.py`, `knowledge/entities/ada-lovelace.md`.

> parts = [self.id.replace("-", " "), self.body]
> --- `src/wiki/retrieve/store.py`

#### MEM-OBJ-page-routing
Label: Page selection and relation metadata

Source-native identity: page filename/ID and frontmatter `type`, `superseded_by`, `supersedes`, `related`, `aliases`, `tags`, `parents`, `definition`. YAML in the same Markdown files; localized symbolic IDs, flags and edge records are separated here from prose content. Alias/tag/definition text also becomes lexical or embedding input, not instruction authority. Namespace/type chooses acceptance destination; the filename stem becomes loader identity; `superseded_by` excludes current pages by default. Typed edges and body wikilinks become graph adjacency. A `supersedes` declaration alone does not automatically set the predecessor's `superseded_by`. The loader does not call schema validation. Same-ID maps and index primary keys do not establish global semantic uniqueness across files.

This object spans review and retrieval rather than being part of exactly one supplied route; closest records are [RT-RTE-page-review](runtime.md#rt-rte-page-review), [RT-RTE-index-query](runtime.md#rt-rte-index-query), [RT-CLM-history-policy](runtime.md#rt-clm-history-policy). SRC-1, `src/wiki/review.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/graph.py`, `src/wiki/retrieve/query.py`.

> if not include_superseded and page.meta.get("superseded_by"):
>     continue
> --- `src/wiki/retrieve/store.py`

#### MEM-OBJ-page-sources
Label: Page provenance pointers

Source-native identity: `sources` array and body `[^src:N]` references. Symbolic YAML/Markdown persisted with the page, recording raw source ID, character span, extraction timestamp and extractor label. Derived by locating model-proposed quotes, or seed-authored quotes, in retained source text. Quote strings and fuzzy alignment scores are not retained in these entries; a source pointer is not the original quote display or an explanation of entailment. Checks consume spans and body markers; query output reduces provenance to source IDs, omitting spans and claim-to-source correspondence. Bootstrap passes the body but not this array. Those are consequential downstream omissions, not evidence that initial pointers did not exist.

Distinct operative part crossing [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-index-query](runtime.md#rt-rte-index-query) and [RT-RTE-eval-report](runtime.md#rt-rte-eval-report), not another copy of their routes. SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/retrieve/query.py`, `src/wiki/cli/__init__.py`; enforcement limits in [RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy).

> {"source_id": source_id, "span": span, "extracted_at": now, "extractor": model}
> --- `src/wiki/ingest/pipeline.py`

> out.append(str(s["source_id"]))
> --- `src/wiki/retrieve/query.py`

#### MEM-OBJ-ingest-manifest
Label: Ingest manifest and rejection diagnostics

Source-native identity: `pending/<source_id>.manifest.json`. Symbolic JSON filesystem artifact with usage, model, chunk count, staged IDs/paths/status/contradiction flags, and rejected IDs/issues. This is derived process evidence, not admitted knowledge. New-versus-patch and changed-body flags are software-produced; they do not adjudicate contradiction. CLI immediately prints it. Later review enumerates only Markdown files, so does not automatically display the manifest's warnings or use rejected diagnostics to revise proposals. Same-source ingestion overwrites the manifest. Distinct artifact of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not a duplicate of that route. SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/ingest/diff.py`, `src/wiki/review.py`, `src/wiki/cli/__init__.py`.

> return sorted((root / "pending").glob("*.md"))
> --- `src/wiki/review.py`

#### MEM-OBJ-bm25
Label: Lexical search derivative

Source-native identity: `indexes/bm25.sqlite`, FTS5 `pages(page_id, text)`. Filesystem SQLite, symbolic index structures over derived search text (ID, body and selected fields), not model parameters. `build` can take caller-supplied `PageRecord` lists or default to current page loading. Rebuild supplies one current-page load. Search applies OR-of-terms FTS matching, yielding IDs and scores; the text affects ranking, not instruction following. Whole database unlink/recreation invalidates this derivative independently of knowledge changes and the other databases. Related supplied route: [RT-RTE-index-query](runtime.md#rt-rte-index-query); this is its lexical object, not a second route. SRC-1, `src/wiki/retrieve/bm25.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/rebuild.py`.

> con.execute("CREATE VIRTUAL TABLE pages USING fts5(page_id UNINDEXED, text)")
> --- `src/wiki/retrieve/bm25.py`

#### MEM-OBJ-graph
Label: Retained graph derivative

Source-native identity: `indexes/graph.sqlite`, `nodes` and `edges`. Symbolic SQLite tables, including serialized frontmatter and paths as node metadata, and typed/frontmatter or body-wikilink edges as adjacency. These are separately readable structured records, not an opaque vector or a natural-language graph summary. Software assigns typed edges weight 1.0 and wikilinks 0.5; traversal actually ranks by hops, not these stored confidence-like weights. Undirected traversal can reach missing targets, because insertion does not enforce target existence. Consumers: node enumeration for query seeds, neighbors/walk for retrieval. Exposed `neighbors` is a storage/query capability; no separate deployed caller is inferred. Rebuild replaces this database independently. Distinct derivative of [RT-RTE-index-query](runtime.md#rt-rte-index-query). SRC-1, `src/wiki/retrieve/graph.py`, `src/wiki/retrieve/query.py`.

> scores[other] = max(scores.get(other, 0.0), 1.0 / (hop + 1))
> --- `src/wiki/retrieve/graph.py`

#### MEM-OBJ-vectors
Label: Retained page embeddings

Source-native identity: `indexes/vectors.sqlite`, `vectors(page_id, dim, vec)`. Distributed numerical representations stored as normalized packed-float BLOBs, with symbolic page IDs/dimensions. Lineage: optional BGE inference over `search_text`, not parameter training or retained source-language rationale. Consumers unpack vectors for cosine/dot-product comparison against a current query embedding. IDs/dimensions and the build manifest's model name are metadata, not a readable semantic summary of a vector. No supplied stored vectors establish actual contents. Model artifact provenance remains unresolved beyond the configured name; component fixity is described by [RT-CMP-dense-embedding](runtime.md#rt-cmp-dense-embedding). Database replacement is independent of BM25/graph and does not automatically follow page edits. Distinct object associated with [RT-RTE-index-query](runtime.md#rt-rte-index-query). SRC-1, `src/wiki/retrieve/dense.py`, `src/wiki/retrieve/rebuild.py`.

> con.execute("CREATE TABLE vectors (page_id TEXT PRIMARY KEY, dim INTEGER, vec BLOB)")
> --- `src/wiki/retrieve/dense.py`

#### MEM-OBJ-audit-log
Label: Operation audit records

Source-native identity: `audit/log.jsonl`. Symbolic append-only-in-this-writer JSONL records: timestamp, operation, actor, hashes, output summary, model, usage, duration and error/success. Summaries are readable displays of operation metadata, not complete source content, model responses or retained model reasoning. Ingest and review produce records; empty tracked audit content supplies no observed episode. Inspection/search of `src/` found writers, not a later decision consumer of this log. Therefore log retention alone supplies no demonstrated trace-fed behavior update. A generic caller of `append` remains a capability, not a shipped learning loop. Distinct artifact associated with [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-page-review](runtime.md#rt-rte-page-review). SRC-1, `src/wiki/audit.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/review.py`; empty artifact basis from [boundary](boundary.md#boundary-and-evidence).

> f.write(json.dumps(rec, ensure_ascii=False) + "\n")
> --- `src/wiki/audit.py`

#### MEM-OBJ-eval-queries
Label: Evaluation queries and expected IDs

Source-native identity: `evals/datasets/queries.jsonl` and default `queries.bootstrap.jsonl`. Filesystem JSONL; natural-language questions with symbolic expected page IDs/type. Active dataset initialization/curator decisions were not established by inspecting its producer history. Subsequent bootstrap transformation is known: software supplies each page body to a model and assigns each nonempty generated line that page stem as its expected ID. Human review/merge is requested, not mechanically required for every output path. Later `load_dataset` feeds expected IDs to metric computation, so labels have software scoring authority without being semantic truth guarantees. Active and candidate files have different default consumers; selected output may alias the active path. Related supplied routes: [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap), [RT-RTE-eval-report](runtime.md#rt-rte-eval-report); distinct object, not duplicate route. SRC-1, `src/wiki/cli/__init__.py`, `src/wiki/eval/harness.py`.

> DATASET_RELPATH = ("evals", "datasets", "queries.jsonl")
> --- `src/wiki/eval/harness.py`

#### MEM-OBJ-eval-results
Label: Evaluation reports and build description

Source-native identities: `evals/baselines/<name>.json`, timestamped Markdown reports, `components.json`, and `indexes/manifest.json`. These are software-produced descriptive outputs, grouped here because their inspected role is reporting rather than content admission. Symbolic counts, ranks, metrics and configuration fields persist as JSON; Markdown renders human-readable results. Evaluation JSON retains per-query retrieved and expected IDs; Markdown displays a subset of retrieved IDs. Build metadata does not contain a corpus digest or enforce query-time freshness. Latest named JSON can be replaced; timestamps can retain separate reports. Human inspection is afforded, not an observed adoption event. No inspected query/evaluation path automatically reads these reports as a policy or promotion gate. Distinct artifacts associated with [RT-RTE-eval-report](runtime.md#rt-rte-eval-report) and [RT-RTE-index-query](runtime.md#rt-rte-index-query). SRC-1, `src/wiki/eval/harness.py`, `src/wiki/retrieve/rebuild.py`, `src/wiki/cli/__init__.py`.

> (out_dir / f"{name}.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
> --- `src/wiki/eval/harness.py`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Memory context: code selects approximately 1,000-token source chunks with approximately 100-token overlap using four-character token estimates. Paragraph/sentence accumulation plus overlap makes this a target, not a strict token-window maximum. Each Anthropic call receives fresh root instructions, source ID/offsets and one chunk; output is capped at 4,096 tokens by default. No prior chunks' proposals, corpus bodies, audit history or rejected-attempt critiques are added to the next call. The host retains whole raw text for span location; only proposals escape the model-call frame into pending pages. This resembles isolated frames with returned values, not heap pointers dereferenceable by the model. There is no extraction reload tool in the proposed-page schema. Raw text can be reloaded by host code in later ingestion/evaluation, not on demand by this model. SRC-1, `src/wiki/ingest/chunk.py`, `src/wiki/config.py`, `src/wiki/extract.py`, `src/wiki/ingest/pipeline.py`.

> messages=[{"role": "user", "content": chunk.text}],
> --- `src/wiki/extract.py`

First all-valid nonempty output wins per chunk; otherwise the final attempt's individually valid pages may still stage. The first ID occurrence wins cross-chunk deduplication even if a later duplicate would have better content. These are software curation rules, not human approval or semantic resolution. Retained issues go to the manifest; failed-attempt reasons are not a durable critique consumed by the escalation model. See [MEM-OBJ-ingest-manifest](#mem-obj-ingest-manifest). SRC-1, `src/wiki/ingest/pipeline.py`; supporting selection passage in the supplied route.

#### On [RT-RTE-page-review](runtime.md#rt-rte-page-review)

The human's default consumption is an 800-character pending-file preview, not full provenance replay. The optional editor can show/change the full file, but `accept_page` does not re-run schema/span checks. A review invocation reads pending Markdown, not the ingest manifest that carries changed-body warnings. Acceptance moves the whole file into knowledge and can overwrite its predecessor; rejection deletes only that pending file. Raw sources, manifests and earlier admitted knowledge are not automatically withdrawn by rejection. Optional Git commit gives a possible history/recovery substrate, not transactional rollback after the move. SRC-1, `src/wiki/cli/__init__.py`, `src/wiki/review.py`, `scripts/pre-commit`; supporting move passage in the supplied route.

> typer.echo(page_path.read_text(encoding="utf-8")[:800])
> --- `src/wiki/cli/__init__.py`

#### On [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)

Source text and page/quote specifications originate with script authors; no model extraction or per-content operator decision is added by `main`. Software validates before each write and stops on failure; prior writes remain. Temporary `_seed_source_*` files are deleted after raw retention, not a withdrawal of raw evidence. Direct writes bypass pending and review, making a universal human-admission claim false. SRC-1, `scripts/seed_corpus.py`; validation/write passage in the supplied route.

> finally:
>     tmp.unlink(missing_ok=True)
> --- `scripts/seed_corpus.py`

#### On [RT-RTE-index-query](runtime.md#rt-rte-index-query)

Read-back is request-led: operator query or evaluator adapter supplies query text; software selects from prior retained derivatives. BM25/dense select up to 50 IDs each, graph seeds derive from query/ID/alias token overlap and two-hop adjacency, then fusion keeps 30, with default final k=10. This is a candidate-count budget, not a downstream prompt-token budget. Optional reranker receives query plus current candidate search text, not source raw bodies. Fresh aliases can affect graph seeds even while graph/index content is stale. Returned source-ID provenance omits stored spans. No query path compiles an answering prompt or returns page body text. SRC-1, `src/wiki/retrieve/query.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/rerank.py`; selection/freshness passages in the supplied route.

Component `build(root, pages=...)` operations also permit supplied page lists; their own default loader filter is not an invariant for arbitrary library callers. Graph neighbor calls and low-level search APIs expose retained state but do not prove an additional deployed external-agent route. Dense/rerank consumer versions and uninspected artifact resolution remain as recorded in [RT-CMP-dense-embedding](runtime.md#rt-cmp-dense-embedding) and [RT-CMP-cross-encoder](runtime.md#rt-cmp-cross-encoder). SRC-1, `src/wiki/retrieve/bm25.py`, `src/wiki/retrieve/dense.py`, `src/wiki/retrieve/graph.py`.

#### On [RT-RTE-eval-report](runtime.md#rt-rte-eval-report)

There are distinct later corpus consumers, not only the index-backed query route. `wiki eval retrieval` constructs `BaselineRetriever`, which loads current namespace files once into in-memory token counters and ranks matching terms with a log-frequency tie bonus. It defaults to excluding superseded pages without needing persisted indexes. `eval components` instead uses query adapters and their index freshness limits. `eval ingest` iterates registered files without the current-page filter, loads raw sources, skips pages lacking sources or available raw text, and prints lexical faithfulness; it does not remove failing pages. No generated answer is judged here. SRC-1, `src/wiki/eval/baseline_retriever.py`, `src/wiki/cli/__init__.py`, `src/wiki/eval/harness.py`.

> self.docs = load_corpus(root)
> self._counts: list[Counter] = [Counter(tokenize(text)) for _, text in self.docs]
> --- `src/wiki/eval/baseline_retriever.py`

Evaluation transforms query/outcome pairs into persisted reports, but the inspected CLI/harness offers no subsequent automatic read of reports to alter the retriever or retained assertions. A report is derived from operation-like results; that does not alone make it durable behavior-shaping trace learning. Expected IDs retain scoring authority at the evaluator, not authority to certify page truth. SRC-1, `src/wiki/eval/harness.py`, `src/wiki/cli/__init__.py`; reporting-only passage in the supplied route.

#### On [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap)

This later model invocation receives retained `page.body` in a user message. Full frontmatter, provenance array, raw evidence, manifest warnings and extractor reasoning are omitted. Every registered Markdown page participates, including superseded ones; per-page input has no explicit body truncation/token budget. Response cap is 256 tokens. Code writes every nonempty line and supplies the expected ID itself; requested `per_page` is guidance, not enforced output count. This body has content-generating influence through model interpretation, not system-instruction force. Actual compliance or benefit is unobserved. SRC-1, `src/wiki/cli/__init__.py`.

> f"answer. Return one query per line, no numbering.\n\nPAGE:\n{page.body}"
> --- `src/wiki/cli/__init__.py`

#### On [RT-BAP-ingest-instructions](runtime.md#rt-bap-ingest-instructions)

Root instruction text is static shipped guidance loaded into each extraction request, not itself read-back of accumulated experience. Its authority is natural-language system guidance; tool schema and validators have separate symbolic force. The inspected route does not automatically revise instructions from audit or evaluation. The root file's initial authorship history and provider-internal retained state are not established. SRC-1, `AGENTS.md`, `src/wiki/ingest/pipeline.py`, `src/wiki/extract.py`; source passages in the supplied authority record.

## Write side

The acquisition/curation chain is raw bytes ([MEM-OBJ-raw-source](#mem-obj-raw-source)) → chunk-isolated model proposal → located quote pointers and software checks → pending page and manifest ([MEM-OBJ-ingest-manifest](#mem-obj-ingest-manifest)) → reviewed move or rejection. Human initiation supplies a document, not approval of each model claim. Software staging admits pages with no accumulated issues; the human interactive review is a later decision. Source trust remains bounded by quote matching and token overlap, not semantic adjudication ([RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy)).

The separate seed chain is authored source/specification → shared builder/checks → direct knowledge write. Callable acceptance merely checks type destination, then moves content; optional hook checks structural validity after movement. These alternative admission surfaces prevent treating the curated CLI protocol as a global write authorization boundary ([RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed), [RT-RTE-page-review](runtime.md#rt-rte-page-review)).

Maintenance has separate effects. Changed-body diff creates a manifest warning, not an adjudicated contradiction or automatic supersession. `superseded_by` changes current-load membership; it does not physically erase old pages. Reject deletes pending text but leaves raw and manifest evidence. Same-name acceptance/seed can replace retained content. Explicit rebuilding replaces indexes independently and does not undo earlier source/page writes. Root doctrine asks to preserve history, but actual replacement is a source-supported falsifier of an invariant reading ([RT-CLM-history-policy](runtime.md#rt-clm-history-policy); SRC-1, `src/wiki/ingest/diff.py`, `src/wiki/review.py`, `src/wiki/retrieve/rebuild.py`).

No compaction/checkpoint mechanism is required to explain the inspected extraction frame: each call is fresh. Source-to-page reduction is content curation, not conversation summarization. Audit and manifests preserve selected process facts/diagnostics; indexes preserve access representations; evaluation reports preserve measurements. None of those artifacts by itself supplies a trace → automatic durable behavioral revision → later policy consumer chain in the inspected writers and consumers. In contrast bootstrap's generated rows can enter a later evaluator, by human merge or an output path naming the active dataset. This is a concrete content-to-evaluation-data transformation, not proof of improved capacity or a critique/revision loop. Reasons for source claims survive only insofar as the authored prose states them and pointers retain evidence; model selection rationale is not reconstructed or later read by these routes (SRC-1, `src/wiki/audit.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/eval/harness.py`, `src/wiki/cli/__init__.py`).

## Read-back

| Retained input → actual later consumer | Trigger / selector / delivery | Authority and limit |
| --- | --- | --- |
| Raw source → later ingest or CLI ingest evaluator | Source ID selects filesystem raw text; whole text reaches host checks | Lexical evidence reference, not model instructions or independent truth oracle; absent raw bodies prevent replay ([MEM-OBJ-raw-source](#mem-obj-raw-source)) |
| Pending Markdown → review human / acceptance primitive | Review invocation enumerates sorted Markdown; preview/editor, then chosen move/delete | Human content decision on interactive path; manifest reasons not automatically read ([RT-RTE-page-review](runtime.md#rt-rte-page-review)) |
| Admitted prose and fields → builders and baseline evaluator | Explicit rebuild loads current pages; baseline constructor separately loads current corpus | Text/metadata shapes ranking and corpus membership; neither is an answering agent ([RT-RTE-index-query](runtime.md#rt-rte-index-query), [RT-RTE-eval-report](runtime.md#rt-rte-eval-report)) |
| Persisted lexical, graph, vector derivatives → query/evaluator adapters | Query-led selection and fusion; rerank optionally sees current search text | Access/ranking authority. Return has IDs/scores/paths/source IDs only; no verified body delivery to a downstream agent ([RT-RTE-index-query](runtime.md#rt-rte-index-query)) |
| Page bodies → bootstrap model → retained candidate rows → later evaluator | Operator invokes all-page iteration; user-message body; default candidates need merge, chosen active output need not | Model-interpreted content influence, then symbolic expected-ID scoring authority; not automatic semantic label verification ([RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap), [MEM-OBJ-eval-queries](#mem-obj-eval-queries)) |
| Audit/manifests/reports → unspecified later operator inspection | Files persist; CLI immediately prints selected fields | Afforded inspection is not evidence of automatic later policy use. Reports and logs do not establish a learned update ([MEM-OBJ-audit-log](#mem-obj-audit-log), [MEM-OBJ-eval-results](#mem-obj-eval-results)) |

No inspected route is an independent unsolicited push of selected retained knowledge into an answering agent. Bootstrap is code-controlled delivery inside an operator-requested generation task, not evidence for the unshipped MCP/context compiler. Static extraction instructions remain working-context control but are excluded from accumulated read-back under the record contract (SRC-1, `src/wiki/cli/__init__.py`, `src/wiki/extract.py`; [boundary](boundary.md#boundary-and-evidence)).

## Integration issues

- Clarification, not correction: [RT-RTE-eval-report](runtime.md#rt-rte-eval-report) encompasses two retrieval consumers. The direct baseline loader is not index-backed and honors current-page exclusion at construction. Component evaluation inherits index-query limitations. Evidence: SRC-1, `src/wiki/eval/baseline_retriever.py`, `src/wiki/cli/__init__.py`; annotation supplies the additional passage. A reconciliation should not merge these into one index-only read-back claim.
- Admission-warning delivery limit: [MEM-OBJ-ingest-manifest](#mem-obj-ingest-manifest) and [RT-RTE-page-review](runtime.md#rt-rte-page-review) establish that warning flags print on ingestion, but review only loads Markdown. The later reviewer is not guaranteed to see the stored changed-body warning. This qualifies any inference from retained diagnostics to later criticism; no supplied fact needs replacement.
- Authority omission: [MEM-OBJ-page-sources](#mem-obj-page-sources), [RT-RTE-index-query](runtime.md#rt-rte-index-query) and [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap) concern different delivery channels. Query reduces pointers to source IDs; bootstrap omits the source array entirely. Retained provenance must not be projected intact into either consumer.
- No new declaration duplicates a supplied referent: runtime has no operative-object declarations. The objects here are material stores/parts, while the closest supplied records are routes, policy claims or model components. Route and instruction-authority findings use annotations rather than replacement declarations. The grouped reporting object is a container for descriptive outputs, not a claim of identical storage or invalidation.
- Unresolved initialization/provenance: active dataset authoring/admission history, individual seed-page correctness, most corpus contents, actual raw-body lineage and external model artifacts remain unestablished. These limit dataset trust, corpus-wide provenance and actual numerical-state judgments, not the known subsequent transformations ([MEM-OBJ-eval-queries](#mem-obj-eval-queries), [MEM-OBJ-page-body](#mem-obj-page-body), [MEM-OBJ-vectors](#mem-obj-vectors)).
- Unresolved deployment/use: downstream answering consumer and provider retention are outside inspected wiring; actual human review, report adoption, component availability and behavior changes are unobserved. No memory benefit, semantic fidelity or exercised trace-learning conclusion follows solely from persistence ([RT-RTE-index-query](runtime.md#rt-rte-index-query), [RT-RTE-query-bootstrap](runtime.md#rt-rte-query-bootstrap), [MEM-OBJ-audit-log](#mem-obj-audit-log)).

## Limitations and checks

Source HEAD was rechecked as `267541db838cbca757a112bd0cfa47fa61eb5fb2`; source status was clean. The report preserves the supplied run ID, source identity and reviewed boundary. Method basis: supplied memory type, job instruction, collection rules, worker rules and complete record contract. Source reads and searches stayed within SRC-1; no new source identity or execution evidence was introduced.

The falsifier checks specifically examined direct seed admission, edited acceptance, baseline direct loading, superseded-page bootstrap, stale fused returns versus active rerank filtering, graph targets and metadata-triggered raw-store idempotency. They support path-specific conclusions rather than uniform trust/admission/currentness claims. Static evidence establishes wiring, not activation or benefit. Corpus/schema/span-check details not directly audited remain attributed to supplied findings or explicitly limited above.

Deterministic validation: `commonplace-run validate-output` passed for this invocation. This checks form, references, identities and quotation occurrence, not semantic adequacy or job acceptance.
