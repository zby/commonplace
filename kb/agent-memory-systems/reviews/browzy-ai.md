---
description: "Terminal TypeScript personal KB that compiles raw sources into a markdown wiki, serves Q&A through SQLite FTS and section retrieval, and writes thin session-derived digests and insight drafts"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# browzy.ai

browzy.ai is a TypeScript terminal personal knowledge base by Vihari Kanukollu. It ingests URLs, PDFs, images, Markdown, and text files into a local data directory, compiles them into an interlinked markdown wiki, indexes the wiki in SQLite FTS5, and answers questions by retrieving relevant article sections into an LLM prompt. Its distinctive memory design is a compiled middle layer: raw sources are evidence, wiki articles are the durable knowledge artifacts, SQLite is a rebuildable retrieval index, `browzy.schema.md` is an operator-editable system-definition artifact, and session digests plus crystallized insight drafts are lightweight trace-derived artifacts rather than a full learning loop.

**Repository:** https://github.com/VihariKanukollu/browzy.ai

**Reviewed revision:** [56c253042041ee2f483a5e9b824174d746891cf4](https://github.com/VihariKanukollu/browzy.ai/commit/56c253042041ee2f483a5e9b824174d746891cf4)

## Core Ideas

**The source-of-truth layer is readable files, not the database.** The default data directory is `~/.browzy/default`, with `raw/`, `wiki/`, `output/`, and `.browzy/` created by config setup; the README also documents `drafts/` and `sessions/` as user data surfaces ([README.md](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/README.md), [config.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/config.ts)). `FilesystemStorage` writes raw captures, wiki articles, `_index.json`, and exported outputs as local files with path-safety checks ([filesystem.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/storage/filesystem.ts)). In artifact terms, raw files are retained evidence artifacts; compiled articles are the user-facing knowledge artifacts; the database is an operational derivative.

**Compilation is ahead-of-time LLM distillation from raw sources into wiki articles.** Ingest normalizes web, PDF, image, Markdown, and text inputs into `RawSource` records and a `raw/_manifest.json` list, then `WikiCompiler.compile()` finds sources not yet represented in article frontmatter and compiles them in batches ([ingest/index.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/ingest/index.ts), [compiler.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/compile/compiler.ts)). Small sources become template articles without an LLM call; larger sources go through the compiler prompt and are parsed from `===ARTICLE===` blocks into Markdown files with `title`, `tags`, `sources`, `backlinks`, `created`, `updated`, and `summary`. The compiler also refreshes backlinks from `[[slug]]` links and writes `_index.json`, so the wiki has a generated navigation surface separate from the articles.

**SQLite FTS5 is a derived retrieval/runtime tool.** `SQLiteStorage` stores source metadata and article rows, then maintains an `articles_fts` virtual table with Porter stemming and BM25 weighting over title, summary, content, and tags ([sqlite.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/storage/sqlite.ts), [migrations.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/storage/migrations.ts)). The index has ranking influence over answers, but not source authority: markdown article files remain the canonical knowledge artifacts, and FTS entries are rebuilt or invalidated as compilation and ingest proceed.

**Question answering retrieves sections, not whole documents.** `QueryEngine.prepare()` reads the optional schema, computes a model-aware budget, asks `ContextBuilder` for relevant context, and returns a prompt plus coverage metadata without necessarily making the LLM call ([engine.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/engine.ts)). `ContextBuilder` searches SQLite, backfills from `_index.json` when FTS is sparse, ranks candidates, extracts matching article sections, caps per-article and total article tokens, and emits confidence plus gap terms ([contextBuilder.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/retrieval/contextBuilder.ts), [relevanceRanker.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/retrieval/relevanceRanker.ts)). This makes retrieval a symbolic ranking and clipping pipeline rather than a vector-memory store.

**`browzy.schema.md` is a prompt-level control plane.** `ensureSchema()` creates a template file, `readSchema()` ignores comment-only templates and caps user content at 4000 characters, and both compiler and query prompts prepend the schema when present ([schema.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/schema.ts), [prompts.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/prompts.ts)). This is a system-definition artifact with instruction force over compilation and answering, but its representational form is prose and its enforcement is model compliance, not validation.

**Sessions, digests, and drafts are distinct retained surfaces.** `useSession()` writes full conversation sessions as JSON under `~/.browzy/sessions/`, keeps `last-session-meta.json`, prunes old sessions past 50 files, and can export a redacted session as Markdown ([useSession.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/hooks/useSession.ts)). On later startup, the Ink app can summarize the last session into a digest text file and optionally write a `session-YYYY-MM-DD` wiki article; during live Q&A, it can ask the crystallizer to save at most one novel multi-source insight into `drafts/` ([app.tsx](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/app.tsx), [digest.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/digest.ts), [crystallizer.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/crystallizer.ts)). These are trace-derived, but thin: there is no scoring, review state, deduplication, or implemented promotion path from `drafts/` into `wiki/`.

## Comparison with Our System

| Dimension | browzy.ai | Commonplace |
|---|---|---|
| Primary substrate | Local user data tree plus derived SQLite FTS5 | Git repository of typed markdown artifacts plus validation scripts |
| Main memory unit | Compiled wiki article | Typed note, reference doc, instruction, review, or workshop artifact |
| Raw evidence | `raw/*.md`, images, manifest, source IDs | Sources, snapshots, cited files, and source-linked notes |
| Retrieval | FTS5 + heuristic ranking + section extraction | Agent navigation over files, indexes, links, and review reports |
| Control surface | `browzy.schema.md` prepended to compiler/query prompts | Collection conventions, type specs, instructions, skills, validation, review gates |
| Session traces | JSON sessions, digest text/wiki article, crystallized drafts | Workshop/log artifacts when intentionally retained; not default chat-history memory |
| Governance | Deterministic link/orphan/missing-field checks plus LLM consistency lint | Deterministic validation plus semantic review workflows and explicit artifact contracts |

browzy.ai is stronger as a consumer application: it gives a user a terminal interface, model/provider selection, direct ingestion, automatic compilation, query streaming, and a concrete local retrieval pipeline. Commonplace is stronger as a methodology substrate: it distinguishes artifact types, authority, lineage, review state, and lifecycle much more explicitly. The sharpest divergence is promotion. In browzy, raw source -> wiki article is automated and valuable, but wiki article -> stronger rule, validator, instruction, or reviewed library claim is not a separate lifecycle. In commonplace, promotion and authority changes are slower, but they are first-class design concerns.

The closest commonplace analogue to browzy's compiled wiki is a workshop layer that has been made queryable: raw intake, compiled intermediate articles, generated indexes, and outputs all live together. That is useful for personal research, but it can blur the line between accumulated library knowledge and derived work-in-flight material unless lifecycle boundaries are made explicit.

**Read-back:** push — app-side FTS ranking and section extraction inject retrieved wiki context into answer prompts.

## Borrowable Ideas

**Use a derived FTS index while keeping files canonical.** Ready to borrow when the KB needs faster or section-aware retrieval. browzy is a good example of a database as an operational accelerator, not a rival source of truth.

**Compile raw intake into reusable intermediate articles before Q&A.** Ready as a workshop pattern. The ahead-of-time compile step amortizes LLM cost and creates inspectable artifacts that future queries can reuse, but commonplace would need review status and source-lineage rules before promoting those articles into the library.

**Expose an operator-editable schema prompt.** Needs a specific use case. A bounded `browzy.schema.md` is a simple way to let a user steer domain tone and emphasis without editing code. In commonplace, the equivalent would probably be workshop-local guidance, because collection-level conventions already carry stronger authority.

**Retrieve relevant sections under an explicit token budget.** Ready to borrow for any future retrieval layer. `ContextBuilder` combines FTS candidates, rank signals, section extraction, per-article caps, and confidence/gap metadata in one understandable pipeline.

**Keep crystallized insights in drafts, not directly in the wiki.** Ready as a cautionary pattern. browzy's `drafts/` directory is a sensible low-authority landing zone for trace-derived synthesis; commonplace would add review and promotion mechanics before such drafts could affect always-loaded or validated behavior.

## Trace-derived learning placement

browzy.ai qualifies as trace-derived because it consumes conversation traces and writes durable symbolic artifacts. This is separate from the raw-source compiler: URLs, PDFs, images, and text files are source evidence, while sessions are assistant/user interaction traces.

**Trace source.** The raw trace is the per-session message list persisted by `useSession()` as JSON, plus the current answer, question, and `sourcesUsed` list available during live Q&A ([useSession.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/hooks/useSession.ts), [app.tsx](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/app.tsx)).

**Extraction.** There are two extraction paths. `generateSessionDigest()` turns prior user and assistant messages into a 2-3 sentence digest under `SESSION_DIGEST_PROMPT` ([digest.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/digest.ts), [prompts.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/prompts.ts)). `crystallize()` asks an LLM whether a multi-source answer contains a genuinely novel connection; it saves `NONE` or a parsed article-like draft ([crystallizer.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/query/crystallizer.ts)). The oracle is the LLM prompt itself, not downstream task reward or human approval.

**Storage substrate.** Raw sessions live as JSON files in `~/.browzy/sessions/`. Digests live as text files and may also be written as wiki articles. Crystallized insights live as Markdown files under `drafts/` with `derived: true` frontmatter. None of these become model weights.

**Representational form.** The retained outputs are prose symbolic artifacts. The digest is prose summary; the crystallized draft is article-shaped Markdown with frontmatter; the session JSON is structured trace evidence.

**Lineage.** Session files preserve message traces, digests point indirectly through `last-session-meta.json`, and crystallized drafts include `sources` plus the triggering question. Lineage is present but shallow: there is no stable derivation graph, invalidation rule when source articles change, deduplication across drafts, or review status.

**Behavioral authority.** Sessions and digests are knowledge artifacts when shown as context or read by the user. A digest written into `wiki/` can influence future answers after indexing, giving it advisory/ranking authority through retrieval. `drafts/` are low-authority candidate knowledge artifacts until a user promotes them manually. `browzy.schema.md` is the separate system-definition artifact: it instructs compiler and query prompts, but it is not derived from traces.

**Scope and timing.** The scope is per-user and per-session. Digest generation happens on the next startup when the previous session has enough user turns and an LLM is available. Crystallization runs online during answering, gated to one saved crystallized insight per session unless failed attempts reset the gate. On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), browzy sits in the symbolic artifact-learning branch: session traces can yield prose artifacts, but there is no stronger promotion ladder into rules, tests, validators, or learned parameters.

## Curiosity Pass

**The "compiled knowledge" story is real, but its authority is mixed.** Raw-source compilation produces reusable wiki articles and a link graph, which is stronger than retrieval over a raw document pile. But the compiler's contradiction policy, source merging, and article quality are prompt obligations; deterministic checks catch broken links and missing fields, not semantic drift.

**The SQLite index is well-scoped.** It affects ranking and retrieval but does not become the canonical memory. That makes the design simpler to inspect than database-first memory systems, while still giving better search ergonomics than plain file traversal.

**The schema file is powerful precisely because it is small.** A 4000-character prose schema can shape both compilation and answering. The failure mode is that operators may treat it as enforceable configuration, when it is really a prompt prefix with no parser or validator.

**The session-memory claims are thinner than the product language suggests.** Full sessions are saved, digests can be generated, and one crystallized draft can be created from a multi-source answer. That is enough to count as trace-derived artifact learning, but not enough to count as a robust self-improving memory system.

**Conversation compaction appears under-integrated.** `compactConversation()` can summarize older turns into a retained-looking summary, but the Ink app calls it without storing the returned compacted messages for future prompts ([compactor.ts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/retrieval/compactor.ts), [app.tsx](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/app.tsx)). As reviewed, compaction is more implemented helper than effective retained artifact.

## What to Watch

- Whether `drafts/` gains an explicit promotion workflow into reviewed wiki articles.
- Whether digest articles are indexed consistently and given normal wiki frontmatter, or remain an optional side effect.
- Whether contradiction handling moves from prompt policy into a checked merge/review workflow.
- Whether `browzy.schema.md` grows structured fields or validation, which would make it a stronger system-definition artifact.
- Whether retrieval shifts from FTS and heuristic ranking toward embeddings or hybrid retrieval, and whether canonical markdown remains the source of truth.
- Whether linter output becomes actionable maintenance state rather than one-off terminal feedback.

---

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — aligns: browzy keeps markdown articles canonical and uses SQLite as a derived index.
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — compares: browzy's raw/wiki/drafts/output data tree behaves like a queryable research workshop.
- [Distillation is transformation not selection](../../notes/distillation-is-transformation-not-selection.md) — exemplifies: raw sources are transformed into new compiled wiki articles before retrieval.
- [Stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) — warns: browzy's FTS and `_index.json` surfaces are only trustworthy when kept synchronized with canonical markdown.
- [Memory design adds operational axes to artifact analysis](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) — applies: browzy is clearest when raw sources, wiki articles, FTS index, schema, sessions, digests, and drafts are classified by substrate, form, lineage, and authority.
- [LLM Wiki](./llm-wiki.md) — compares: both compile raw material into markdown wiki articles, but browzy implements a TypeScript runtime and SQLite retrieval layer.
