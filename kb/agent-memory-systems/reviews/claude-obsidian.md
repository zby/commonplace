---
description: "claude-obsidian review: Obsidian vault memory with agent skills, hot cache, wiki ingestion, hybrid retrieval, locking, hooks, and methodology modes"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# claude-obsidian

claude-obsidian, by AgriciDaniel, is a Claude Code plugin and Obsidian vault template for building a persistent "LLM Wiki" from sources, questions, and saved conversations. At the reviewed commit it ships agent skills, command files, vault scaffolding, hooks, Python and shell utilities, Obsidian configuration, and an example wiki; the durable memory is an inspectable Obsidian-flavored Markdown vault rather than a hidden chat-memory database.

**Repository:** https://github.com/AgriciDaniel/claude-obsidian

**Reviewed commit:** [cb93ff6d82f9c35a08bf6010e7fac36dfddc827b](https://github.com/AgriciDaniel/claude-obsidian/commit/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b)

**Last checked:** 2026-06-04

## Core Ideas

**The central memory artifact is a wiki vault, not a chat transcript.** `WIKI.md` defines three layers: immutable `.raw/` source documents, generated `wiki/` knowledge pages, and the instruction/schema file that tells the agent how to operate the vault ([WIKI.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/WIKI.md)). The `wiki` skill repeats the same architecture and makes the agent responsible for scaffolding, updating `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`, and routing work to sub-skills ([skills/wiki/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki/SKILL.md)).

**Agent skills are the real application layer.** The repository has no ordinary package manifest; instead, `.claude-plugin/plugin.json` identifies it as a Claude Code plugin, and `AGENTS.md` explains that `skills/<name>/SKILL.md` files are discoverable by Claude Code, Codex, OpenCode, and other Agent Skills-compatible agents ([.claude-plugin/plugin.json](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/.claude-plugin/plugin.json), [AGENTS.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/AGENTS.md)). The main skills implement setup, ingest, query, lint, save, autoresearch, retrieval, mode routing, canvas, and Obsidian syntax support ([skills](https://github.com/AgriciDaniel/claude-obsidian/tree/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills)).

**Context efficiency starts with progressive disclosure and can upgrade to chunk retrieval.** The base query path reads `wiki/hot.md`, then `wiki/index.md`, then a bounded set of pages; quick mode stops at cache/index, standard mode reads 3-5 pages, and deep mode broadens deliberately ([skills/wiki-query/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-query/SKILL.md)). The optional `wiki-retrieve` stack chunks pages, adds contextual prefixes, builds a BM25 index, reranks candidates with local Ollama embeddings when available, and returns candidate page paths for the calling agent to read and synthesize ([skills/wiki-retrieve/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-retrieve/SKILL.md), [scripts/retrieve.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/retrieve.py), [scripts/bm25-index.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/bm25-index.py), [scripts/rerank.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/rerank.py)).

**Write safety is handled as vault operations, not model judgment.** `wiki-ingest`, `save`, `autoresearch`, and `wiki-fold` require per-file advisory locks before writes, and `scripts/wiki-lock.sh` implements path validation, stale lock reaping, and age-based lock acquisition ([skills/wiki-ingest/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-ingest/SKILL.md), [skills/save/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/save/SKILL.md), [scripts/wiki-lock.sh](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/wiki-lock.sh)). Post-tool hooks defer git auto-commit while locks are held, which treats multi-agent safety as a file-system coordination problem ([hooks/hooks.json](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/hooks/hooks.json)).

**Adoption is native to Obsidian and agent workspaces.** `bin/setup-vault.sh` creates the wiki folders, `.raw/`, templates, Obsidian graph settings, snippets, and plugin configuration; transport detection prefers Obsidian CLI where available and falls back to direct filesystem access ([bin/setup-vault.sh](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/bin/setup-vault.sh), [scripts/detect-transport.sh](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/detect-transport.sh), [docs/compound-vault-guide.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/docs/compound-vault-guide.md)). Methodology modes route new content into generic, LYT, PARA, or Zettelkasten layouts through a small Python router instead of asking each skill to invent paths ([scripts/wiki-mode.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/wiki-mode.py)).

## Artifact analysis

- **Storage substrate:** `files` — The primary retained state persists in the vault file tree: `.raw/` sources and manifest, `wiki/` pages, `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`, templates, Obsidian configuration, skill files, hooks, and `.vault-meta` runtime artifacts. Git, Obsidian, MCP, and Claude Code are secondary transport or presentation surfaces.
- **Representational form:** `prose` `symbolic` `parametric` — Wiki pages and skill instructions are prose; frontmatter, wikilinks, manifests, mode configs, lock files, transport snapshots, chunk JSON, BM25 indexes, plugin manifests, and hooks are symbolic; optional Ollama embeddings in `.vault-meta/embed-cache.json` are distributed-parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` — Humans and agents author wiki pages and skills, external sources are imported into `.raw/` and source summaries, and saved conversations, hot-cache summaries, logs, chunk records, access-derived retrieval artifacts, and research outputs can be derived from session and tool activity.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Wiki pages advise later agents as knowledge; skills, commands, AGENTS/CLAUDE/WIKI files, and hooks instruct agents; lock and path scripts enforce write safety; mode and transport helpers route operations; lint, tests, and frontmatter rules validate structure; BM25/rerank state ranks recall; save/ingest/autoresearch/fold workflows turn interaction and source traces into future memory.

**Wiki pages and raw sources.** Storage substrate: Markdown files under `wiki/` plus immutable source files under `.raw/`. Representational form: prose pages with symbolic YAML frontmatter, wikilinks, callouts, tags, source lists, and optional address fields. Lineage: imported source material is stored in `.raw/`, then agent-authored summaries, entity pages, concept pages, questions, and hot-cache state are derived from those sources and interactions. Behavioral authority: knowledge artifact when read by the agent or human; some pages can become soft project instructions when the agent treats decisions, contradictions, or conventions as constraints, but that effective force is not measured by the repository.

**Skill and command layer.** Storage substrate: `skills/*/SKILL.md`, `commands/*.md`, `AGENTS.md`, `WIKI.md`, and `CLAUDE.md`. Representational form: prose instructions with symbolic frontmatter and trigger descriptions. Lineage: authored plugin content. Behavioral authority: instruction and routing, because these files decide when the agent scaffolds a vault, ingests a source, queries the wiki, saves a conversation, runs autoresearch, or lints.

**Hot cache, index, log, and saved sessions.** Storage substrate: ordinary Markdown files such as `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`, `wiki/questions/*`, and `wiki/sessions/*`. Representational form: prose summaries plus symbolic dates, page lists, frontmatter, and wikilinks. Lineage: trace-extracted and authored from recent sessions, ingests, answers, and operations; invalidation is procedural, because the skills instruct agents to update these files after significant operations rather than a daemon continuously recomputing them. Behavioral authority: `wiki/hot.md` is pushed by session-start hooks and query workflows as recent context, while index/log/session pages serve as knowledge, audit, and navigation surfaces.

**Retrieval artifacts.** Storage substrate: `.vault-meta/chunks/<address>/chunk-NNN.json`, `.vault-meta/bm25/index.json`, and `.vault-meta/embed-cache.json` when `wiki-retrieve` is provisioned. Representational form: symbolic chunk metadata and BM25 postings plus parametric embedding vectors. Lineage: derived from wiki page bodies; chunk records include body hashes and page body hashes, BM25 is rebuilt from chunks, and embeddings are cached by body hash ([scripts/contextual-prefix.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/contextual-prefix.py), [scripts/bm25-index.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/bm25-index.py), [scripts/rerank.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/rerank.py)). Behavioral authority: ranking and routing for query-time recall; the memory service returns candidate pages and snippets rather than final answers.

**Locks, transport snapshots, modes, and address metadata.** Storage substrate: `.vault-meta/locks`, `.vault-meta/transport.json`, `.vault-meta/mode.json`, `.vault-meta/address-counter.txt`, and `.raw/.manifest.json`. Representational form: symbolic coordination and routing records. Lineage: generated or updated by setup, detection, ingestion, routing, and address allocation scripts. Behavioral authority: enforcement for write safety, routing for content placement and transport choice, and validation/audit for ingestion delta tracking.

Promotion path: claude-obsidian has a practical path from raw source or conversation trace to `.raw/` capture, wiki page, hot-cache/index/log visibility, optional chunk/index/embedding retrieval, and lint/lock/test governance. It does not promote memories into hard semantic validators; the strongest automatic constraints are structural, path, lock, routing, and retrieval-index constraints.

## Comparison with Our System

| Dimension | claude-obsidian | Commonplace |
|---|---|---|
| Primary purpose | Agent-operated Obsidian wiki for personal/project knowledge | Git-native methodology KB for agent-operated knowledge-base design |
| Canonical artifact | Obsidian Markdown wiki page plus wikilinks/frontmatter | Typed Markdown artifact governed by collection/type contracts |
| Write path | Agent skills mutate a vault through CLI/MCP/filesystem with locks | Direct file edits, skills, validation, review, and index refresh |
| Read path | Hot cache, index, bounded page reads, optional BM25/rerank chunks | `rg`, indexes, links, collection contracts, skills, review reports |
| Governance | Locking, lint instructions, scripts, tests, hooks, Obsidian conventions | Type validation, collection contracts, semantic review gates, generated indexes |
| Learning model | Source/session traces become wiki pages, logs, hot cache, and retrieval artifacts | Authored notes/reviews plus source snapshots, validation, and review workflows |

claude-obsidian and Commonplace share the view that durable agent memory should be inspectable files with human-readable prose and symbolic structure. The major difference is scope. claude-obsidian optimizes for end-user adoption in Obsidian: setup scripts, visual graph/canvas affordances, skills, hot cache, and optional retrieval infrastructure. Commonplace optimizes for a typed methodology corpus where artifact kind, source grounding, and review status are explicit.

The strongest claude-obsidian idea for Commonplace is not "use Obsidian" in general; it is the layered read path. `hot.md` gives cheap recency, `index.md` gives catalogue-level scan, pages give local substance, and optional chunk retrieval handles passage-level lookup. Commonplace already has analogous pieces, but claude-obsidian makes the progressive-disclosure policy explicit in the query skill.

### Borrowable Ideas

**A session-start hot cache with explicit freshness bounds.** Ready now as a pattern. Commonplace could maintain a small project-local current-work cache for active workshops, but it should be scoped to work directories so it does not become an unreviewed global truth source.

**Feature-detected retrieval upgrades.** Ready as a tooling pattern. `wiki-query` falls back gracefully when chunk/BM25/rerank artifacts are absent; Commonplace retrieval tools should keep that posture instead of making optional indexes mandatory.

**Per-file write locks for high-concurrency agent workflows.** Needs a concrete write-heavy workflow. Commonplace currently relies on git discipline and targeted edits; if parallel agents start writing shared indexes or workshop files, claude-obsidian's lock script is a useful model.

**Mode routing as a tiny symbolic helper.** Useful but not urgent. Commonplace collections already route by directory contracts, but a small route helper could be valuable for workshop templates or consuming-project KBs.

**Do not borrow broad auto-commit hooks for Commonplace library artifacts.** claude-obsidian's PostToolUse auto-commit fits an end-user vault that wants loss prevention. Commonplace's review and validation workflow needs deliberate diffs and atomic commits.

## Write side

**Write agency:** `manual` `automatic` — Users and agents intentionally invoke skills to scaffold, ingest, query-and-file, save, lint, fold, and research; automatic or rule-driven operations include transport snapshot generation, address allocation, lock files, hot-cache/log/index maintenance required by skills, chunk and BM25 index generation, embedding-cache writes, hook-triggered hot-cache reads, stale-lock cleanup, and optional git auto-commit.

**Curation operations:** `consolidate` `synthesize` `promote` — `save` condenses a conversation into a permanent note; `wiki-fold` rolls log entries into extractive fold pages; `autoresearch` synthesizes source findings into concept/entity/source/question pages; `wiki/hot.md` promotes recent context into a short session-start cache. These operations are agent-instruction-driven rather than autonomous daemon behavior.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — The system can save current conversations, append operation logs, update hot-cache state after significant interactions, route autoresearch/search/fetch results into pages, and derive retrieval chunks/indexes from the resulting wiki files.

**Learning scope:** `per-project` `cross-task` — The retained wiki and `.vault-meta` artifacts live in a vault and persist across later sessions; `AGENTS.md` and the `wiki` skill also document cross-project referencing through `wiki/hot.md` and `wiki/index.md`.

**Learning timing:** `online` `staged` — Save, ingest, hot-cache updates, log updates, and hook reads happen during ordinary agent sessions; chunking, BM25 rebuilds, methodology-mode setup, linting, DragonScale folds, and autoresearch are staged workflows.

**Distilled form:** `prose` `symbolic` `parametric` — Conversations and sources become prose Markdown pages with symbolic metadata and links; retrieval setup turns those pages into symbolic chunk/index records and optional embedding vectors.

**Trace source.** claude-obsidian qualifies as trace-learning because session activity can become durable memory. The `save` skill explicitly files the current conversation, answer, or insight into a structured wiki note and updates index, log, and hot cache ([skills/save/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/save/SKILL.md)). The `wiki` and `wiki-query` skills require hot-cache reads and updates, while `autoresearch` turns web-search/fetch loops into filed source, concept, entity, and synthesis pages ([skills/wiki/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki/SKILL.md), [skills/wiki-query/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-query/SKILL.md), [skills/autoresearch/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/autoresearch/SKILL.md)).

**Extraction.** The extraction oracle is usually the agent following skill instructions, not a separate scorer. The code-grounded automatic pieces are structural: route paths, allocate addresses, acquire locks, detect transport, chunk text, build BM25, cache embeddings, and run tests. Meaning-level extraction remains an LLM skill behavior.

**Scope and timing.** The durable learning scope is a single vault, but cross-project instructions make the vault reusable from other workspaces. Online memory is mostly the hot cache, log, and saved/session pages produced during normal use; staged memory is source ingestion, autoresearch, log folding, and retrieval-index provisioning.

## Read-back

**Read-back:** `both` — Most wiki memory is pulled through `wiki-query`, `wiki-retrieve`, index scanning, page reads, Obsidian search/CLI/MCP, and explicit skill invocation, but the hooks also push `wiki/hot.md` at session start and after compaction.

**Read-back signal:** `coarse` — The implemented push path is coarse always-load recent-context recall: `hooks/hooks.json` reads `wiki/hot.md` on session start and prompts the agent to silently reread it after compaction. Instance-specific wiki page selection remains pull.

**Faithfulness tested:** `no` — The repository has hermetic tests for locking, address allocation, BM25, retrieval, mode routing, contextual prefixes, and concurrency, but I did not find a behavioral ablation showing that pushed hot-cache context reliably changes agent decisions.

**Targeting and signal.** The push path is not instance-targeted. `wiki/hot.md` is loaded because the session starts or compacts, not because the current task matches a tag, page id, embedding, or lexical query. Instance-specific recall happens when the agent or user asks a question and `wiki-query` uses hot cache, index, bounded page reads, or optional chunk retrieval.

**Injection point.** Hook-provided hot-cache content is assembled before the model continues the session. Query results enter context before synthesis when the agent invokes the query/retrieve workflow. PostToolUse auto-commit, lock cleanup, chunking, BM25 builds, and hot-cache updates are write-side maintenance for later calls, not a second read-back point.

**Selection, scope, and complexity.** Pull selection has explicit complexity controls: quick mode reads cache/index only; standard mode reads a small number of pages; deep mode is intentionally broader; optional retrieval returns top-k chunk candidates with snippets and page paths. The pushed hot cache is small by convention, about 500 words, but actual quality and context dilution are runtime properties, not proven by tests.

**Authority at consumption.** Retrieved wiki pages and hot-cache summaries are advisory knowledge unless the host treats the skill instructions or page content as binding. The skill files themselves carry stronger instruction authority because they define how agents should read, write, cite, route, and maintain the vault.

**Faithfulness.** Tests check structural behavior, such as retrieval fallback, BM25 scoring, lock correctness, path validation, mode routing, and concurrency. They do not test whether an LLM follows the hot cache, retrieved pages, contradiction callouts, or saved rules after those memories appear in context.

**Other consumers.** Humans consume the same artifacts through Obsidian graph view, pages, canvases, CSS snippets, Dataview dashboards, logs, source folders, and git. This is a real consumer surface, not incidental: the system is designed as a shared human/agent vault.

## Curiosity Pass

**The impressive part is the instruction system, not an autonomous backend.** Most meaning-level memory operations happen because a capable agent follows `SKILL.md` instructions. The scripts make those operations safer and more searchable, but they do not independently understand which claims are true.

**Hot cache is useful precisely because it is small and blunt.** It avoids crawl-everything recency cost, but the hook can only push a coarse recent summary. More precise recall is deliberately left to pull retrieval.

**The optional retrieval path is file-derived and inspectable.** Chunk JSON, BM25 indexes, and embedding caches are ordinary vault metadata. That makes the retrieval substrate easier to debug than a hosted vector service, although embeddings still need probing rather than direct semantic inspection.

**The system mixes two memory layers.** The wiki is long-lived knowledge; `hot.md` is a short-lived context cache. Treating both as "memory" is fine only if the review keeps their authority and invalidation differences visible.

**Auto-commit is a product decision with different tradeoffs than Commonplace.** In an Obsidian vault, avoiding data loss can matter more than curated commit boundaries. In a methodology KB, the same hook would weaken review discipline.

## What to Watch

- Whether query-time retrieval starts auto-injecting top-k wiki pages before every prompt; that would move page memory from pull to instance-targeted push.
- Whether linting grows from structural/report guidance into enforceable semantic gates for contradiction, citation, and stale-claim resolution.
- Whether retrieval index maintenance becomes hook-driven after every write; that would increase recall freshness but could make `.vault-meta` churn harder to reason about.
- Whether methodology modes become a stricter type system rather than only path routing; that would bring claude-obsidian closer to Commonplace-style collection contracts.
- Whether tests add with/without memory ablations for hot-cache or retrieved-page use; that would distinguish context presence from behavioral effect.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: claude-obsidian stores a rich wiki, but most page memory affects agents only after explicit query or page reads.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: wiki pages, skills, hot cache, logs, locks, indexes, hooks, and embeddings have different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages, source summaries, questions, and hot-cache content mostly serve as evidence, reference, context, or advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skills, commands, hooks, routing scripts, lock scripts, and retrieval policies configure future agent behavior.
- [Use trace extraction](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: saved conversations, operation logs, hot-cache summaries, autoresearch outputs, and retrieval indexes are derived from use traces and source-processing loops.
