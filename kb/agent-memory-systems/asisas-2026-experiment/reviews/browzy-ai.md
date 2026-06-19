---
description: "browzy.ai review: terminal personal KB with Markdown/wiki files, SQLite FTS, LLM compilation, query-time context assembly, and trace-derived digests"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# browzy.ai

browzy.ai, by Vihari Kanukollu, is a TypeScript terminal personal knowledge-base engine. At the reviewed commit, it ingests web/PDF/image/text/Markdown sources into local files, compiles them into interlinked Markdown wiki articles with an LLM, indexes those articles in SQLite FTS5, and answers questions by assembling query-ranked wiki context before calling a model.

**Repository:** https://github.com/VihariKanukollu/browzy.ai

**Reviewed commit:** [56c253042041ee2f483a5e9b824174d746891cf4](https://github.com/VihariKanukollu/browzy.ai/commit/56c253042041ee2f483a5e9b824174d746891cf4)

**Last checked:** 2026-06-04

## Core Ideas

**The canonical knowledge surface is a compiled Markdown wiki.** Raw sources are written under the data directory, article files are Markdown with frontmatter, and `_index.json` summarizes articles and concept/tag groups ([src/core/storage/filesystem.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/storage/filesystem.ts), [src/core/types.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/types.ts), [src/core/compile/compiler.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/compile/compiler.ts)). SQLite is important, but it is an index and metadata store rather than the only knowledge substrate.

**Compilation is the main write-side intelligence.** `WikiCompiler` finds newly ingested sources, pre-indexes raw content, asks the LLM to create or update wiki articles, writes those articles, refreshes the FTS index, regenerates backlinks, and updates the wiki index ([src/core/compile/compiler.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/compile/compiler.ts), [src/core/prompts.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/prompts.ts)). The compiler prompt explicitly prefers merging new material into an existing article over duplicate article creation, but the merge quality is LLM-mediated and not independently verified by code.

**Context efficiency is explicit but lexical.** Query serving computes a model budget, retrieves FTS candidates, ranks articles by keyword density, title match, tag match, recency, and backlink count, then includes relevant sections under per-article and total article budgets ([src/core/query/engine.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/engine.ts), [src/core/retrieval/contextBuilder.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/retrieval/contextBuilder.ts), [src/core/retrieval/relevanceRanker.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/retrieval/relevanceRanker.ts), [src/core/retrieval/tokenCounter.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/retrieval/tokenCounter.ts)). This bounds both volume and complexity: at most a small ranked set of articles enters the prompt, long articles are section-selected, and omitted topics are surfaced as gaps.

**SQLite FTS is the retrieval engine.** The database stores source rows, article rows, and an FTS5 virtual table with Porter stemming; search sanitizes a user query into quoted OR terms and ranks with BM25 weights over title, summary, content, and tags ([src/core/storage/sqlite.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/storage/sqlite.ts), [src/core/storage/migrations.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/storage/migrations.ts)). There is no vector store or graph database in the inspected code; backlinks are symbolic fields in article frontmatter and ranking metadata.

**The user schema is a local prompt-level control surface.** `browzy.schema.md` can customize compilation and query behavior, and the system loads it into compiler/query system prompts when the file contains non-comment content ([src/core/schema.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/schema.ts), [src/core/prompts.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/prompts.ts)). That gives users a simple authored instruction layer, but it is not type-checked beyond file existence and length limits.

**Session-derived memory exists, but it is auxiliary.** The CLI saves session JSON, session metadata, optional session digests, and activity-log entries; it can also draft an insight from a multi-source Q&A exchange into `drafts/` ([src/cli/hooks/useSession.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/hooks/useSession.ts), [src/cli/app.tsx](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/app.tsx), [src/core/query/digest.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/digest.ts), [src/core/query/crystallizer.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/crystallizer.ts), [src/core/activityLog.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/activityLog.ts)). The durable trace loop is real, but it is less central than source-to-wiki compilation.

## Artifact analysis

- **Storage substrate:** `files` — The primary retained store is the local data directory: raw source files, wiki Markdown, `_manifest.json`, `_index.json`, drafts, outputs, session JSON/digests, activity logs, config, keys, profile, history, and schema files; SQLite under the data directory provides secondary indexed state for sources, articles, and FTS search.
- **Representational form:** `prose` `symbolic` — Raw sources, wiki article bodies, schema instructions, session exports, digests, drafts, and activity logs are prose; frontmatter, manifests, indexes, FTS rows, session JSON, config, query-cache keys, lint issues, and prompt/output markers are symbolic control surfaces.
- **Lineage:** `authored` `imported` `trace-extracted` — Users author schema/config and can edit local files; ingested URLs/files/images become raw sources and LLM-compiled wiki articles; saved sessions, activity logs, session digests, and insight drafts are derived from Q&A/session traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Wiki articles and raw sources provide evidence/context; `browzy.schema.md` and system prompts instruct compilation and answers; wiki links, tags, manifests, indexes, and source ids route knowledge; lint checks validate links, fields, contradictions, duplicates, and gaps; FTS/BM25 plus heuristic ranking decide context order; session digests, activity logs, and crystallized drafts feed future maintenance and recall.

**Raw sources and manifest.** Ingested material becomes Markdown/text/image/PDF-derived files plus `_manifest.json` entries with ids, type, title, origin, path, summary, tags, timestamps, and content hash for file sources ([src/core/ingest/index.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/ingest/index.ts), [src/core/storage/filesystem.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/storage/filesystem.ts)). Their authority is evidence; they shape behavior only after compilation or search indexing.

**Compiled wiki articles.** Article frontmatter carries title, tags, source ids, backlinks, timestamps, and summary; article bodies carry the prose that is later served to the model. The promotion path is imported/raw source to LLM-compiled article to search-indexed query context. Existing articles can be overwritten with a merged version when the compiler output uses the same slug.

**SQLite search structures.** `sources`, `articles`, and `articles_fts` rows are derived from files and manifest entries. They have ranking/routing authority for retrieval but are not the best human inspection surface; if FTS state is stale, rebuilding from the file store is the obvious repair path.

**User schema and prompts.** `browzy.schema.md` is authored prose that becomes system-prompt instruction for compiler and query paths. It is stronger than ordinary knowledge because it changes how future articles and answers are produced.

**Session and trace artifacts.** Session JSON, session metadata, digest text files, optional `session-{date}` wiki articles, `log.md`, and `drafts/*.md` insight articles are trace-extracted records from interaction. Raw sessions are knowledge artifacts; digests and drafts can become behavior-shaping wiki content once indexed or loaded by later query/read paths.

## Comparison with Our System

browzy.ai and Commonplace both favor local, inspectable artifacts and generated access structures, but they optimize for different operators. browzy is a terminal research assistant: ingest sources, ask questions, stream answers. Commonplace is a methodology KB: collection contracts, type specs, validation, reviews, and explicit routing rules are the central machinery.

The biggest alignment is file-first canonical knowledge with secondary indexes. browzy's Markdown wiki plus SQLite FTS is close to the operational layer Commonplace could add for high-volume source retrieval. The biggest divergence is governance. Commonplace makes artifact type, collection routing, and validation explicit and repo-visible; browzy relies on LLM prompts, lint suggestions, and a user schema file, with fewer hard gates around whether a compiled article faithfully preserves source material.

browzy is stronger on user-facing read-back ergonomics. It packages retrieval, budget management, streaming, confidence, gap detection, query cache invalidation, and source suggestions into one terminal loop. Commonplace is stronger on reviewable authority: the behavior-shaping contracts are mostly authored Markdown and validators rather than hidden prompt effects.

### Borrowable Ideas

**FTS as a secondary access layer over files.** Commonplace could use SQLite FTS for source and review discovery while keeping Markdown as the canonical store. Ready for high-volume source snapshots and related-system reviews.

**Section-level context assembly.** browzy's article-section selection is a concrete way to bound long notes without moving to embeddings. Ready for source snapshots and long reviews; broader use needs section-quality conventions.

**User schema as a local prompt modifier.** A small project-local file that modifies compile/query behavior could map to Commonplace workshop preferences or project-specific review criteria. Needs a concrete workflow so it does not become an untyped instruction dump.

**Gap suggestions from retrieval misses.** browzy turns weak coverage into suggested additions. Commonplace could emit "missing note/source" suggestions from repeated failed searches or review-bundle gaps. Ready where the signal is deterministic; LLM-generated gap lists need review.

**Crystallized insight drafts instead of silent promotion.** browzy writes candidate insights to `drafts/`, not directly into the wiki. Commonplace should keep that staging discipline for trace-derived notes. Ready now as a workshop pattern.

## Write side

**Write agency:** `manual` `automatic` — Users add sources, edit schema/config, export sessions, and can operate the CLI manually; the system automatically writes raw sources, manifests, SQLite rows, compiled/updated wiki articles, backlinks, indexes, activity logs, session files, session digests, and insight drafts.

**Curation operations:** `consolidate` `evolve` `synthesize` — Session digest generation summarizes a prior session; compilation can update an existing article in light of a new source; compiler and crystallizer paths create new wiki/draft entries from sources or multi-article Q&A traces.

### Trace-derived learning

**Trace source:** `session-logs` — The CLI persists session messages, source-bearing assistant turns, session metadata, activity-log entries, and Q&A exchanges used by the crystallizer.

**Extraction.** Session digest generation reads a saved prior session and writes a short digest text file, then optionally writes the digest as a wiki article. The crystallizer consumes the question, generated answer, source article slugs, and source article contents; an LLM judge outputs either `NONE` or an insight article, which is saved under `drafts/` with derived frontmatter. The oracle is an LLM quality filter constrained by prompts, not a deterministic validator.

**Learning scope:** `per-project` — Sessions, wiki articles, drafts, and digests live under one browzy data directory.

**Learning timing:** `online` `staged` — Sessions and activity logs are written during use; digest generation happens on a later startup, and crystallized insight drafting runs asynchronously after a qualifying answer.

**Distilled form:** `prose` `symbolic` — Digests and draft insights are prose; their filenames, frontmatter, tags, source slugs, session metadata, and activity-log markers are symbolic.

In the trace-derived-learning survey terms, browzy sits in the artifact-learning family: it distills session/Q&A traces into prose artifacts that may later be indexed and read back. It strengthens the claim that useful trace-derived learning often needs a staging layer; the implementation writes digests/drafts rather than silently changing authoritative wiki articles.

## Read-back

**Read-back:** `push` — In the implemented Q&A loop, the user asks a question and browzy assembles retained wiki/schema context before the model call; the receiving model does not choose its own memory lookup.

**Read-back signal:** `coarse` `inferred / lexical` — `browzy.schema.md` is always loaded into compiler/query prompts when present, while article context is selected from FTS and lexical/metadata ranking keyed on the current question.

**Faithfulness tested:** `no` — The code computes confidence and logs which sources were used, but it does not run with/without ablations, perturbation tests, or post-answer audits proving that injected context changed the answer faithfully.

The main injection point is pre-invocation. `QueryEngine.prepare` builds a prompt containing the selected knowledge-base context, confidence note, gap note, question, and format instruction; the CLI then streams an LLM response with that prepared prompt plus recent conversation history ([src/core/query/engine.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/engine.ts), [src/cli/app.tsx](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/app.tsx), [src/core/query/historyManager.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/historyManager.ts)). `usedSlugs` excludes already-used articles for follow-up queries, so repeated "tell me more" turns can diversify retrieved context, but retrieval relevance remains lexical and heuristic. Effective precision, recall, and context dilution are not verified from code.

Other consumers include the human user through `/search`, `/health`, recent activity logs, session digests on startup, and exported sessions. Those surfaces are useful, but the memory read-back classification above is for what reaches the model.

## Curiosity Pass

The README advertises a broad architecture, and most of the named modules are present, but the implementation is still a conventional local KB engine: files plus SQLite FTS, LLM prompts, and an Ink terminal interface. There is no vector store, learned retriever, graph database, or autonomous multi-agent memory loop in the inspected code.

The system's strongest "compiled knowledge" claim is also its main risk. LLM compilation can produce readable wiki articles and merge updates, but the code does not verify source faithfulness beyond prompt instructions and later lint suggestions.

The query cache is operationally useful but not durable memory. It is an in-process LRU with TTL and generation invalidation on ingest, so it avoids repeat calls without changing the long-term knowledge base.

The auto-compaction code summarizes older conversation turns, but the current CLI call discards the compaction result instead of storing it for future turns. Durable session digest generation is the real trace-derived memory path.

## What to Watch

- Whether compiled article faithfulness gets a verifier against raw sources; that would make browzy's automatic write path more trustworthy and more Commonplace-like.
- Whether SQLite becomes more than a derived index, such as a canonical article/source store; that would change the substrate classification and repair story.
- Whether insight drafts gain a review/apply workflow into the wiki; that would turn trace-derived drafts into a clearer promotion path.
- Whether retrieval adds embeddings or LLM relevance judgment; that would change read-back signal from purely lexical/metadata inference to embedding or judgment inference.
- Whether `/health` suggestions gain automatic fixes for duplicates, contradictions, or orphan articles; that would add stronger curation operations beyond advisory validation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes browzy's stored wiki from the query loop that actually injects selected context into a model call.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - supports separating raw sources, compiled wiki articles, SQLite indexes, schema prompts, and trace-derived drafts by substrate, form, lineage, and authority.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - describes the authority of schema files, prompts, ranking code, lint checks, and retrieval budgets.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - describes the evidence role of raw sources, wiki article content, logs, sessions, and digests.
- [Use trace-derived extraction](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames browzy's session digests and insight drafts as trace-derived artifact learning with a staging boundary.
