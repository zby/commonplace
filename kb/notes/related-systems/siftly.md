---
description: Next.js + SQLite bookmark ingestion system whose deterministic-first, resumable enrichment pipeline offers concrete patterns for scaling KB source loading with explicit progress state
type: note
status: current
tags: [related-systems]
last-checked: 2026-03-07
---

# Siftly

Siftly is a self-hosted system for importing X/Twitter bookmarks into a searchable local knowledge store. It is built as a high-throughput ingestion pipeline: parse many input variants, deduplicate, enrich incrementally, classify, then expose hybrid search and visual exploration over the processed set. Next.js 16 + Prisma 7 + SQLite, with Anthropic SDK for LLM calls.

**Repository:** https://github.com/viperrcrypto/Siftly
**Local instance reviewed:** `../Siftly/`

## Core Ideas

**Normalize inputs before any intelligence work.** `lib/parser.ts` converts multiple export formats (native Twitter API v1/v2, console script bookmarklet, flat CSV-like JSON, twitter-web-exporter) into one canonical bookmark shape, which makes downstream stages deterministic and simpler.

**Store raw payloads and derived views separately.** `rawJson` is preserved in DB while extracted entities, semantic tags, categories, and media analysis are stored as derived fields. This enables reprocessing without re-import.

**Run deterministic extraction before paid/slow model calls.** The pipeline backfills hashtags, URLs, mentions, tool domains (matching against 100+ known tool domains), and tweet type via `lib/rawjson-extractor.ts` before vision/enrichment/categorization. Zero API cost for this stage.

**Design the pipeline as resumable and idempotent.** Stage markers (`entities`, `semanticTags`, `enrichedAt`, `imageTags`) plus sentinels (`{}` for failed image analysis) avoid infinite retries and let runs continue from partial state. Pipeline progress streamed to UI via SSE.

**Bound concurrency and batch expensive stages.** Specific limits per stage: 12 concurrent vision workers, 20 bookmark pipeline workers, 2 enrichment workers. Enrichment batches 5 bookmarks per API call; categorization batches 20. Retry with exponential backoff (1.5s → 4s → 10s) distinguishes client errors (400/401/403/422, no retry) from transient errors (5xx/timeouts, retry).

**Use hybrid retrieval: cheap candidate generation, expensive semantic ranking.** FTS5 with Porter stemming and unicode61 tokenization produces keyword candidates; regex-based intent detection maps queries to category slugs for narrowing; Claude reranks the top 150 candidates with 0.3–1.0 relevance scores and short reasons. Results cached in a 100-entry LRU with 5-minute TTL. Falls back to LIKE queries if FTS5 table is unavailable.

**Structured vision analysis as a first-class enrichment stage.** `lib/vision-analyzer.ts` sends images/GIFs/video thumbnails to Claude and receives structured JSON: people descriptions, OCR'd text, objects/brands/logos, scene, action, mood, style classification (photo/screenshot/meme/chart/code/diagram), meme template identification, and 30–40 searchable tags. Same-URL images are analyzed once and results reused across bookmarks. 3.5MB raw size limit per image.

**Enrichment metadata goes beyond tags.** The semantic enrichment stage (`enrichAllBookmarks`) produces not just 25–35 searchable tags per bookmark but also structured metadata: sentiment, named people, and company names, stored in a separate `enrichmentMeta` field. Batched at 5 bookmarks per API call with 2 concurrent workers.

**12 predefined categories with AI-readable descriptions.** Categories like "AI & Machine Learning", "Crypto & Web3", "Dev Tools & Engineering" each carry a `description` field that acts as an instruction to the categorization LLM. Confidence scores (0.5–1.0) are stored per assignment. The categorization prompt explicitly weights signals: image analysis > tool domain detection > semantic tags > raw text. Custom categories supported; `isAiGenerated` flag tracks origin.

**Multi-tier auth with Claude CLI OAuth.** `lib/claude-cli-auth.ts` resolves API credentials in priority order: Claude Code CLI OAuth via macOS keychain, DB-saved API key, environment variable, local proxy. The keychain integration reads tokens with expiry checking — zero-config on macOS when Claude Code is installed. Settings UI shows green badge when CLI auth detected.

**Model selection in UI.** Settings allow choosing between Haiku, Sonnet, and Opus (defaults to Opus 4.6). OpenAI is listed as an alternative provider option.

**Export to CSV, JSON, or ZIP with media.** The export system (`lib/exporter.ts`) supports three formats: CSV (flat), JSON (structured with categories and media), and ZIP (per-category manifest plus downloaded media files).

**Force-directed mindmap visualization.** `components/mindmap-canvas.tsx` renders a root → categories → bookmarks graph using @xyflow. Category nodes are positioned equidistant on a circle scaled by bookmark count. Categories are collapsible, and uncategorized bookmarks offer an inline "AI Categorize" button. Cmd+K command palette provides global search.

## Comparison with Our System

| Dimension | Siftly | Commonplace |
|-----------|--------|-------------|
| Storage substrate | SQLite + Prisma models | Markdown files + git |
| Ingestion unit | Bookmark rows with media/category joins | Source snapshot + `.ingest.md` analysis |
| State tracking | Explicit per-stage fields + `ImportJob` records + pipeline counters | Mostly implicit in files/workshop artifacts; limited stage-level state |
| Deterministic pre-pass | Strong (entity extraction, parser normalization, FTS indexing) | Light; ingest is mostly reasoning-heavy and manual/skill-driven |
| Throughput target | High-volume homogeneous stream | Lower-volume heterogeneous sources |
| Retrieval strategy | FTS candidate filtering + LLM rerank | Search + traversal over curated links and note descriptions |
| Media handling | Structured vision analysis with OCR, scene, mood, meme detection | No media analysis; sources are text snapshots |
| Auth model | Multi-tier (CLI OAuth → DB key → env var → proxy) | Agent inherits environment credentials |
| Visualization | Force-directed mindmap (category → bookmark graph) | None; knowledge structure is implicit in links |

Siftly optimizes for operational throughput and resumability on a narrow artifact type. We optimize for reasoning quality and compositional linking across mixed artifact types. The opportunity is not to copy the storage model, but to borrow the pipeline discipline.

## Borrowable Ideas

### Ready to borrow now

- **Ingestion stage state as first-class artifact.** Add a small state file in each ingest workshop (`queued`, `snapshotted`, `connected`, `analyzed`, `distilled`) so retries and audits are explicit instead of inferred.
- **Deterministic pre-pass before `/ingest` analysis.** Extract cheap signals (domains, link counts, source kind hints, author handles) before LLM summarization, then pass them into analysis prompts.
- **Failure sentinels for retry policy.** Record "attempted but failed" markers for brittle steps so repeated runs do not spin forever and can distinguish retryable vs terminal failure.
- **Canonical adapter layer for source formats.** Define one internal "snapshot facts" shape that URL snapshots, local files, and future importers all map into.
- **Candidate-then-rerank retrieval pattern for heavy search.** For deep-search style tasks, prefilter with deterministic criteria first, then use LLM scoring on a bounded candidate set.
- **AI-readable category descriptions as classification instructions.** Each Siftly category carries a `description` field that tells the LLM what belongs there — not a human summary, but a machine instruction. Analogous to how our area index entries could carry classification guidance for `/ingest` auto-tagging.

### Needs a clear use case first

- **High-concurrency worker pipeline for bulk ingestion.** Useful only when source volume is high enough that sequential `/ingest` becomes the bottleneck.
- **Materialized FTS index over derived source facets.** Valuable if KB source count grows to where grep/qmd latency dominates interactive use.
- **Schema-heavy ingestion metadata.** Siftly's DB fields are powerful, but a full relational model is probably premature for our current scale and file-first design.
- **Structured vision analysis for image-bearing sources.** When ingesting sources with screenshots, diagrams, or charts, a structured prompt returning OCR text, scene type, and searchable tags could enrich snapshots. Only useful if commonplace starts handling visual sources.
- **Same-URL deduplication for expensive operations.** Siftly tracks which image URLs have already been analyzed and reuses results. Pattern applies to any expensive per-source operation (LLM summarization, embedding generation) where the same URL may appear in multiple contexts.

## What to Watch

- Does Siftly generalize its pipeline beyond X/Twitter, or remain domain-specific?
- Does its in-memory pipeline state (`globalThis`) hold up under multi-process deployment modes, or will it need persistent job state?
- Do its deterministic extraction stages continue to reduce LLM cost as data formats drift?
- Does the hybrid search stack (FTS + rerank) keep precision as category taxonomy grows?
- The Claude CLI OAuth integration is macOS-only via keychain. Will cross-platform auth follow?

---

Relevant Notes:

- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — enables: Siftly's import jobs and stage counters are concrete workshop artifacts for ingestion state
- [automating-kb-learning-is-an-open-problem](../automating-kb-learning-is-an-open-problem.md) — extends: Siftly is a concrete narrow-scope automation pipeline we can compare against our open questions
- [deterministic-validation-should-be-a-script](../deterministic-validation-should-be-a-script.md) — foundation: deterministic preprocessing before LLM calls follows the same hard-oracle trajectory
- [instructions-are-typed-callables](../instructions-are-typed-callables.md) — extends: Siftly's stages behave like typed callables composed into a pipeline
- [ClawVault](./clawvault.md) — extends: comparative evidence for staged pipelines, with a different optimization target (workshop memory)
- [Thalo](./thalo.md) — extends: comparative evidence for formalization choices (DSL structure vs runtime ingestion pipeline)
- [sift-kg](./sift-kg.md) — contrasts: both ingest documents into knowledge structures, but sift-kg extracts entity-relation graphs via LLM while Siftly enriches and classifies fixed-schema bookmark records
