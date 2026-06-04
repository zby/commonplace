---
description: "Quicky Wiki review: SQLite claim graph with LLM source extraction, confidence events, generated wiki outputs, health loops, dashboard, and MCP pull tools"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-03"
---

# Quicky Wiki

> Replaced 2026-06-04. See [Quicky Wiki](./quicky-wiki.md) for the current review.

Quicky Wiki, from `anzal1/quicky-wiki`, is a TypeScript CLI/library for compiling user-supplied documents into a confidence-scored local knowledge graph. At this commit it initializes a project with `raw/`, `wiki/`, and `.quicky/`, extracts atomic claims from Markdown/text/URL sources with an LLM, stores sources/pages/claims/events in SQLite with FTS search, renders wiki pages and other outputs, serves a dashboard, and exposes MCP tools for agent access.

**Repository:** https://github.com/anzal1/quicky-wiki

**Reviewed commit:** [65ef29b9dcc76237aa797a0d16c50bc8fd89baf7](https://github.com/anzal1/quicky-wiki/commit/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7)

**Last checked:** 2026-06-03

## Core Ideas

**The canonical memory is a SQLite claim graph.** A Quicky project stores configuration under `.quicky/config.yaml`, the graph under `.quicky/graph.sqlite`, source documents under `raw/`, and rendered pages under `wiki/` ([README.md](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/README.md), [src/cli/context.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/context.ts), [src/cli/create.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/create.ts)). The database is not a cache over Markdown; it is the source of truth for sources, pages, claims, dependencies, contradictions, links, and epistemic events ([src/graph/store.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/store.ts)).

**LLM extraction turns documents into atomic claims with metadata.** `ingestSource()` reads a local source or fetched URL markdown, parses frontmatter, hashes content, infers source type/quality/page kind, then prompts the configured LLM to emit JSON claims with statement, confidence, tags, related concepts, and dependency hints. Long content is chunked at 8000 characters with 500-character overlap, then de-duplicated by normalized statement prefix ([src/compiler/ingest.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/ingest.ts), [src/cli/fetch-url.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/fetch-url.ts)).

**Confidence is first-class but heuristic.** Initial confidence is scaled by source quality tier; new evidence merges with an existing claim by a Bayesian-inspired diminishing-return formula; challenged claims are reduced to 60% of prior confidence and dependent claims receive a damped cascade update ([src/compiler/confidence.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/confidence.ts), [src/compiler/diff.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/diff.ts), [src/compiler/resolve.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/resolve.ts), [src/graph/cascade.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/cascade.ts)). The code stores and propagates confidence; it does not make the confidence oracle strong.

**Temporal maintenance is exposed as metabolism.** Each created, reinforced, or challenged claim gets an epistemic event, and `metabolism` commands report stale/contested/cascade-risk claims, apply exponential decay, ask an LLM to resurface low-confidence or stale claims, and red-team high-confidence claims ([src/graph/store.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/store.ts), [src/graph/temporal.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/temporal.ts), [src/metabolism/health.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/health.ts), [src/metabolism/resurface.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/resurface.ts), [src/metabolism/redteam.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/metabolism/redteam.ts), [src/cli/metabolism.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/metabolism.ts)).

**Context efficiency is retrieval before answering, not whole-graph loading.** `queryKnowledge()` searches SQLite FTS for up to 50 relevant pages/claims, groups claims by page, and sends only those confidence-marked claim lines to the answering LLM ([src/graph/query.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/query.ts)). MCP tools similarly expose `search_wiki`, `get_page`, `list_claims`, `list_pages`, `health_report`, and `query_wiki`, so an agent can pull bounded slices rather than loading `.quicky/graph.sqlite` or the whole `wiki/` tree ([src/mcp/server.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/mcp/server.ts)). Multi-model consensus is the exception: it builds context from all pages and all claims, so that path is less context-efficient on large graphs ([src/compiler/consensus.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/compiler/consensus.ts)).

**Generated wiki files are projections, not the maintained source.** `compile markdown` and ingest flows render Markdown pages with frontmatter, confidence badges, claim anchors, related pages, and source lists; exports can also produce Obsidian vaults, slides, Anki decks, graph HTML, and timelines ([src/render/markdown.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/render/markdown.ts), [src/render/obsidian.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/render/obsidian.ts), [src/cli/compile.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/compile.ts)). These files improve adoption and human browsing, but edits to them are not the primary update path for the graph.

## Artifact analysis

- **Storage substrate:** `sqlite` - The central retained state persists in `.quicky/graph.sqlite`, opened through `KnowledgeStore`, with `sources`, `pages`, `claims`, relationship tables, event tables, and FTS virtual tables ([src/cli/context.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/context.ts), [src/graph/store.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/graph/store.ts))
- **Representational form:** `prose` `symbolic` - Symbolic relational tables, FTS indexes, IDs, confidence numbers, timestamps, event types, JSON metadata, and links carry prose claim statements, source titles, summaries, tags, and LLM-generated answers
- **Lineage:** `authored` `imported` - Raw files and web pages are authored or imported source material, while source records, claims, pages, events, confidence state, FTS indexes, generated wiki files, and config derive from ingestion, LLM extraction, deterministic scoring, and CLI options.
- **Behavioral authority:** `knowledge` `routing` `ranking` `validation` — Sources, claims, generated pages, exports, and events advise users and agents, while graph ranking, confidence lifecycle, query context, kind rules, dashboard/MCP tools, and config route, rank, or audit future answers and edits.

**Raw source files.** Storage substrate: project files under `raw/`, plus fetched URL markdown created by `fetchUrlToMarkdown()` and any local source path passed to `qw ingest`. Representational form: prose Markdown/text with optional YAML-style frontmatter, or HTML converted to Markdown. Lineage: authored/imported user documents or fetched web pages; `contentHash` detects changed source content. Behavioral authority: source knowledge artifacts and extraction inputs; they do not reach future answers unless ingested into the graph or read independently.

**Source records.** Storage substrate: SQLite `sources` rows with path, title, type, quality tier, content hash, ingestion timestamp, and metadata JSON. Representational form: symbolic row plus prose title/metadata. Lineage: derived from the raw source path, frontmatter, inferred source type/quality, and content hash. Behavioral authority: provenance and confidence input; quality tier scales extracted claim confidence, and source links support later citation-like reporting.

**Claim graph.** Storage substrate: SQLite `claims`, `claim_sources`, `claim_dependencies`, `claim_contradictions`, `pages`, and `page_links` tables. Representational form: mixed symbolic graph/relational structure plus prose claim statements and page summaries. Lineage: LLM extraction, LLM diffing against existing claims, LLM page assignment, deterministic confidence scoring, and deterministic co-citation links. Behavioral authority: central knowledge artifact for users and agents; also a system-definition artifact for answer assembly because its FTS/ranking/filtering path determines which claims can enter the prompt.

**Epistemic events and confidence lifecycle.** Storage substrate: SQLite `epistemic_events` rows and mutable claim confidence fields. Representational form: symbolic event type, before/after confidence, timestamps, trigger source ids, and prose notes. Lineage: generated by claim creation, reinforcement, challenge handling, manual confidence edits, decay, and cascade propagation. Behavioral authority: evaluation/audit knowledge artifact in timelines and health reports; system-definition artifact where decay, challenge, and cascade updates alter future retrieval order, displayed trust, and answer context.

**FTS search indexes and query context.** Storage substrate: SQLite FTS5 virtual tables plus transient grouped context strings. Representational form: symbolic lexical index and prose claim snippets. Lineage: triggers keep FTS tables aligned with `claims` and `pages`; `queryKnowledge()` derives bounded prompt context from search results. Behavioral authority: ranking and routing authority over read-back. Effective precision/recall is not verifiable from static code.

**Generated wiki/export files.** Storage substrate: project `wiki/` files and export directories. Representational form: Markdown, Obsidian-compatible Markdown, Marp slides, Anki text, graph HTML, and timeline Markdown. Lineage: compiled from SQLite pages, claims, links, sources, and events. Behavioral authority: knowledge artifact for browsing and external reuse; weak system-definition only when a host agent or human treats an exported file as instruction.

**Project configuration and kind rules.** Storage substrate: `.quicky/config.yaml` written as JSON by the implementation. Representational form: symbolic config with LLM provider/model/base URL, paths, metabolism thresholds, quality weights, kind rules, and entity prompts. Lineage: initialized from defaults, API-key/provider detection, and user CLI options. Behavioral authority: system-definition artifact over extraction provider, output paths, claim decay settings, confidence weighting, entity kind inference, and prompt specialization.

**Dashboard and MCP surfaces.** Storage substrate: authored TypeScript code plus live HTTP/stdio process state and short-lived dashboard cache. Representational form: symbolic APIs/tool schemas plus JSON responses and HTML. Lineage: authored implementation over the graph store. Behavioral authority: read/write interface authority: MCP can query, search, list, ingest, and update entity metadata; the dashboard can browse, query, edit/delete claims, delete pages, ingest bookmarks, and prune empty pages ([src/cli/serve.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/serve.ts), [src/mcp/server.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/mcp/server.ts)).

Promotion path: Quicky Wiki promotes raw sources into LLM-extracted claims, claims into page summaries and linked graph state, graph state into rendered wiki/export artifacts, and optional query answers into new source Markdown through `--save`. It does not promote graph claims into reviewed notes, validators, or prompt rules; confidence and metabolism alter graph authority but do not create a stronger reviewed artifact class.

## Comparison with Our System

| Dimension | Quicky Wiki | Commonplace |
|---|---|---|
| Primary purpose | Compile arbitrary source documents into a confidence-scored personal wiki/graph | Maintain a typed methodology KB for agents and maintainers |
| Canonical substrate | SQLite graph plus generated wiki files | Git-tracked Markdown collections, type specs, indexes, sources, reports, and validation |
| Unit of knowledge | Atomic extracted claim attached to a page and sources | Typed artifact with prose argument, frontmatter, links, status, and collection contract |
| Trust model | Source quality multipliers, confidence scores, reinforcement/challenge events, health reports | Source grounding, authoring contracts, validation, semantic review, git history, curated links |
| Read-back | FTS/search/query/MCP/dashboard pull into bounded context | `rg`, indexes, links, skills, reports, validation/review commands, mostly explicit pull |
| Lifecycle | Decay, stale/contested reports, red-team/resurface suggestions, manual edits | Status fields, replacement archives, validation, review gates, workshop-to-library promotion |

Quicky Wiki is closest to Commonplace at the "source material becomes maintained knowledge" level, but it chooses the opposite canonical granularity. Commonplace keeps whole typed artifacts readable and reviewable; Quicky Wiki decomposes sources into individual claims and lets the database coordinate confidence, provenance, search, and outputs. That makes Quicky better suited to broad ingestion and dashboard exploration, while Commonplace is stronger for durable methodology claims whose argument, caveats, and review state must stay inspectable as prose.

The trust tradeoff is sharp. Quicky Wiki has more first-class machinery for confidence, temporal events, stale claims, contested claims, and graph visualization than Commonplace's ordinary notes. But its confidence pipeline depends heavily on LLM extraction/diffing plus heuristics; it does not retain exact source spans per claim, extraction prompts/model versions per claim, reviewer acceptance states, or a distinction between candidate and validated claims. Commonplace is slower, but its artifacts carry stronger human/agent review affordances.

## Read-back

**Read-back:** `pull` - Retained memory reaches agents and users through explicit CLI commands, dashboard routes, MCP tools, generated wiki pages, and FTS-backed query calls. I did not find an implemented host hook that automatically matches the current task and injects Quicky Wiki memory before an agent acts.

### Borrowable Ideas

**Confidence lifecycle as a visible field, not a hidden rank.** Commonplace could expose claim confidence, reinforcement, challenge, and staleness in review reports or candidate artifacts. Ready for derived/review artifacts, but not as an automatic trust oracle for library notes.

**Epistemic event logs for graph-like claims.** Quicky's `created`/`reinforced`/`challenged` event stream is a useful pattern for future structured-claim work. A Commonplace analogue would track when a claim's confidence/status changed and which source or review triggered it. Needs a concrete structured-claim workflow first.

**Health reports that produce action candidates.** Stale, contested, cascade-risk, resurface, and red-team views are useful operational queues. Commonplace already has validation and semantic review; borrowing this would mean generating focused maintenance queues rather than adding another broad sweep.

**Multi-surface exports from one canonical store.** Quicky compiles one graph into Markdown, Obsidian, slides, Anki, graph, and timeline outputs. Commonplace should borrow only the lineage discipline: if we generate alternate views, the source-of-truth and refresh path must remain explicit.

**Do not borrow document-to-claim extraction without review gates.** Automatic extraction is useful for exploration and workshop intake, but Commonplace methodology notes should not become durable library claims just because an LLM extracted them with a confidence number.

**MCP as a narrow pull interface.** Quicky's MCP tools are a practical agent integration surface: list, search, get page, query, health, ingest. A Commonplace MCP layer should similarly expose bounded operations rather than whole-repo dumps. Needs a maintained tool contract before implementation.

## Write side

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The config file is named YAML but written as JSON.** `CONFIG_FILE` is `config.yaml`, while `loadConfig()` parses it with `JSON.parse()` and `saveConfig()` writes `JSON.stringify()` ([src/cli/context.ts](https://github.com/anzal1/quicky-wiki/blob/65ef29b9dcc76237aa797a0d16c50bc8fd89baf7/src/cli/context.ts)). Valid JSON is valid YAML, but the implementation is JSON-configured despite the filename.

**"Living wiki" is implemented more as mutable graph state than as editable wiki prose.** The dashboard can patch/delete claims and pages, and ingestion re-renders `wiki/`; the rendered Markdown files are outputs. That is a reasonable product choice, but it means the human-editable wiki metaphor is weaker than in file-first systems.

**The strongest maintenance actions are advisory.** Red-team and resurface produce critiques/questions/suggestions; decay and manual dashboard edits can change confidence/state. There is no code path that automatically applies red-team confidence adjustments or resolves contradictions from critiques.

**Contradiction storage appears underused by the ingestion path.** The schema and graph renderer support contradiction edges, and health/lint can surface contested claims. The inspected diff/resolve path lowers confidence for challenged claims but does not visibly add `claim_contradictions` rows for the challenging evidence. Parent QA may want to check whether another path populates them.

**The `--save` query path is a compounding loop with weak lineage.** A generated answer can be saved as a new Markdown source and later ingested, but the resulting source is `quality: blog` with cited claim text, not a formally reviewed synthesis. That is useful for personal workflows and risky for KBs that require high-fidelity provenance.

**This is not trace-derived learning under the survey rule.** Quicky Wiki derives durable artifacts from user-supplied documents and explicit saved answers, not from agent session logs, tool/action traces, event streams, repeated trajectories, or rollouts. It therefore does not get the `trace-derived` tag.

## What to Watch

- Whether claim-level provenance gains exact source spans, extraction prompt/model metadata, and per-claim review status. That would make the confidence graph more auditable and closer to Commonplace's source-grounding bar.
- Whether contradiction handling begins writing explicit `claim_contradictions` relationships during ingestion/diff resolution. That would make dashboard graph edges and contested-claim reports structurally stronger.
- Whether MCP adds push-style context activation or remains explicit pull. A task-aware hook would change the read-back placement and raise context-dilution questions.
- Whether generated wiki files become editable inputs with reconciliation back into SQLite. That would change the canonical-source model and introduce bidirectional sync problems.
- Whether metabolism/red-team outputs can mutate confidence or create review queues with acceptance states. That would turn advisory maintenance into governed lifecycle machinery.
- Whether multi-model consensus switches from all-claim context assembly to the same FTS-bounded retrieval path as `queryKnowledge()`. That would matter for context efficiency at scale.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Quicky Wiki stores and searches memory well, but agent effect depends on explicit query/search/MCP/dashboard pull.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Quicky Wiki's raw sources, SQLite graph, events, FTS path, generated wiki, config, dashboard, and MCP tools need separate substrate/form/lineage/authority treatment.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, rendered pages, graph views, health reports, and query results mostly serve as evidence, context, or advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: config, quality weights, extraction prompts, confidence formulas, FTS ranking, decay, cascade propagation, and tool schemas shape later behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Quicky Wiki's main agent-facing mechanism is routing and loading selected claims into bounded LLM calls.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - echoes: Quicky Wiki answers by FTS-selecting a bounded claim context rather than loading the whole graph.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts: Quicky Wiki uses LLM extraction, but from documents rather than operational traces, so it falls outside the trace-derived placement rule.
- [Evaluate memory by effects, not by existence](../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) - motivates: Quicky Wiki's confidence, health, red-team, and query surfaces are partial effect-oriented checks, though behavioral uptake is not tested.
