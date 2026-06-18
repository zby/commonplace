---
description: "Synto review: local LLM vault compiler that turns raw notes into reviewed Markdown wiki articles, SQLite identity state, agent packs, and MCP read tools"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-18"
---

# Synto

Synto, from `kytmanov/synto`, is a local Python CLI for compiling raw Markdown/PDF/text sources into an Obsidian-compatible concept wiki. At the reviewed commit it stores raw notes and published articles as files, keeps lifecycle, identity, lineage, source-segment, metric, cache, and rejection state in `.synto/state.db`, exports an agent-readable pack, and serves the published vault through read-only MCP tools. It is best read as a personal knowledge compiler, not as a chat memory SDK: agents consume the generated wiki by file reads, `INDEX.json`, query synthesis, or MCP calls.

**Repository:** https://github.com/kytmanov/synto

**Reviewed commit:** [6b336034b1849443939dcc868feeac1af2fc8c35](https://github.com/kytmanov/synto/commit/6b336034b1849443939dcc868feeac1af2fc8c35)

**Last checked:** 2026-06-18

## Core Ideas

**The source/wiki split is the central memory model.** Synto treats `raw/` notes and imported originals as source material, then derives concept articles under `wiki/`, staged drafts under `wiki/.drafts/`, source summary pages under `wiki/sources/`, saved query answers under `wiki/queries/`, and synthesized answer pages under `wiki/synthesis/` ([README.md](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/README.md), [src/synto/pipeline/ingest.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/ingest.py), [src/synto/pipeline/compile.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/compile.py), [src/synto/pipeline/query.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/query.py)). The retained artifact an agent normally reads is not the raw note but the compiled article, with source lineage retained for audit.

**SQLite is the operational spine behind a file wiki.** `state.py` defines schema versions through v26 and tables for raw note lifecycle, concepts, articles, rejections, blocked concepts, ingest chunks, compile state, compile runs, LLM cache, source documents/segments, FTS, metric events, concept occurrences, entity labels, identity logs, and merge candidates ([src/synto/state.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/state.py)). Files remain inspectable, but identity, deduplication, edit protection, review state, segment attribution, and many repair operations depend on the database.

**Compilation is LLM-driven but review-staged.** Ingest asks the fast model to extract summaries, concepts, aliases, named references, quality, and language; compile asks the heavy model to write one concept article per concept and puts drafts in `.drafts/` rather than directly publishing them ([src/synto/pipeline/ingest.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/ingest.py), [src/synto/pipeline/compile.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/compile.py)). `verify_drafts()` and `publish_drafts()` record explicit status transitions, confidence thresholds can hold drafts back, and `reject_draft()` stores feedback plus the rejected body for later recompiles.

**Concept identity is stronger than filename identity.** Current code has an entity layer with stable entity ids, preferred labels, aliases, occurrence candidates, ambiguity states, identity logs, and curation commands for rename, merge, split, unmerge, and homonym resolution ([src/synto/state.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/state.py), [src/synto/pipeline/maintain.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/maintain.py), [src/synto/cli.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/cli.py)). That gives the system a durable answer to aliases and homonyms that a plain file-per-title wiki lacks.

**Context efficiency is index-routed progressive reading, not vector recall.** `synto query` reads `wiki/index.md`, expands a question through aliases, asks the fast model to select up to five page titles, loads at most `MAX_CHARS_PER_PAGE` from selected pages, and asks the heavy model to answer ([src/synto/pipeline/query.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/query.py)). `INDEX.json` and pack export provide compact concept/source/routes/segments metadata for file-aware agents ([src/synto/indexer.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/indexer.py), [src/synto/pack_export.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pack_export.py)). Volume is bounded by index selection, page caps, and published/draft status filters; complexity is still article-shaped and can include synthesized pages unless callers choose primitive reads.

**The MCP surface is read-only but not trace-free.** `serve.py` exposes article, concept, source, lineage, question-answering, and verbatim source segment tools; default article visibility is published-only, raw source access is license-gated, and optional MCP audit rows record tool calls, arguments, success, latency, result counts, and resolved labels ([src/synto/serve.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/serve.py), [src/synto/state.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/state.py)). Remote Streamable HTTP has DNS-rebinding host checks but no built-in authentication.

## Artifact analysis

- **Storage substrate:** `files` `sqlite` `repo` `service-object` — User-facing memory persists as Markdown/raw files, pack JSON/TOML, and exported directories; operational state lives in SQLite; the package repo holds prompts, schemas, commands, and tests; `synto serve` is a runtime MCP service object over a vault.
- **Representational form:** `prose` `symbolic` — Raw notes, source summaries, concept articles, query answers, synthesis pages, rejection feedback, and MCP descriptions are prose; frontmatter, SQLite rows, schemas, lifecycle statuses, identity ids, aliases, source segments, FTS indexes, config, pack manifests, tool schemas, and route tables are symbolic. The reviewed implementation has an optional placeholder for an injected RAG store during ingest, but Synto's shipped query/read-back path is not vector-backed.
- **Lineage:** `authored` `imported` `trace-extracted` — Human-authored raw notes, Synto prompts, configs, and curation commands coexist with imported PDFs/Markdown/text/web clips; compiled articles, source summaries, concept occurrences, query/synthesis pages, compile runs, metric/audit events, LLM cache rows, and rejection feedback are derived from source material or use traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` `ranking` `learning` — Articles and source passages advise future agents; prompts, generated `AGENTS.md`/`CLAUDE.md`, and MCP tool descriptions instruct consumers; indexes, aliases, entity ids, routes, and selected pages route context; schemas, lint, status filters, confidence thresholds, and source-access policy validate or gate behavior; query routing and lexical/source search rank; rejection feedback, compile state, cache/metrics, and audit/backlog data alter later maintenance or compilation.

**Raw sources and source segments.** Raw files under `raw/` and archived originals under `.synto/sources/` are imported or authored evidence; `source_documents`, `source_segments`, and `source_segments_fts` store source identity, license, structural locators, hashes, text, warnings, and BM25 search state. These artifacts have knowledge authority when an agent asks for verbatim source text and validation/enforcement authority when license policy hides source paragraphs.

**Concept articles and source pages.** Draft and published Markdown pages carry prose explanations plus symbolic frontmatter such as title, sources, aliases, status, confidence, lineage, content hash, kind, question hash, source hashes, and compile-run ids. They are the main knowledge artifacts; their status, confidence, single-source flags, and hashes also route review, publication, and manual-edit protection.

**Identity and routing state.** Concept entities, labels, occurrences, merge candidates, `INDEX.json`, `wiki/index.md`, pack routes, and alias maps are symbolic routing artifacts. Their lineage is partly extracted from notes, partly curated by rename/merge/split/keep commands, and partly regenerated from published state. They decide which source material recompiles which page and which page a query or MCP concept lookup returns.

**Review, rejection, and maintenance state.** Rejections, blocked concepts, stubs, compile-state rows, lint/maintain repairs, identity logs, and source-quality signals are system-definition artifacts. Rejection feedback is especially behavior-shaping: the next concept compile injects recent feedback into the write prompt, while repeated rejections block the concept until an operator unblocks it.

**Query, synthesis, cache, and audit state.** Saved queries and synthesis pages become prose knowledge artifacts with source-page hashes and duplicate detection. LLM cache, compile runs, metric events, MCP audit rows, and daily rollups are symbolic trace artifacts. Most are diagnostic, but audit/backlog and rejection/compile state can guide later maintenance, and synthesis pages can become first-class query sources.

Promotion path: a source can move from imported raw text to extracted concepts, segment-backed occurrences, source summaries, draft concept articles, verified drafts, published wiki pages, `INDEX.json`/pack routes, MCP-readable answers, and optional synthesis pages. The path strengthens routing and review state, but semantic truth remains LLM- and reviewer-mediated rather than independently proven.

## Comparison with Our System

Synto and Commonplace both use files, Markdown, frontmatter, generated indexes, agent-readable instructions, and explicit validation/review surfaces. Synto is more productized as a personal source-to-wiki compiler: it imports PDFs, segments sources, extracts concepts with LLMs, writes drafts, preserves original source passages, exports portable packs, and serves MCP. Commonplace is more methodology-native: it defines collection contracts, type specs, semantic review, link vocabulary, and curated indexes for an agent-operated KB that is itself the durable design record.

The strongest divergence is authority placement. Synto lets the LLM create the conceptual layer and relies on draft review, confidence, rejection feedback, manual-edit protection, and curation commands to keep that layer usable. Commonplace asks authors to write durable artifacts directly under type contracts, then validates and reviews them. Synto is stronger for turning large incoming source sets into a usable wiki; Commonplace is stronger when the artifact's exact wording and link semantics are already the design object.

Synto's database/file split is also different from Commonplace's git-first model. The SQLite state DB gives Synto stable entity ids, segment attribution, incremental compile state, and trace/audit ledgers that would be awkward in plain Markdown. But the README explicitly notes that git revert does not restore `.synto/state.db`, so rollback of curation operations is not purely repository-native ([README.md](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/README.md)). Commonplace's slower, file-first path gives simpler diff, review, and rollback properties.

### Borrowable Ideas

**Stable concept identity below display names.** Commonplace could borrow the entity-id/label distinction for high-churn index or glossary surfaces where aliases and renames should not break links. Needs a concrete rename-heavy collection before adding database-like identity machinery.

**Rejection feedback as a retained compile input.** Ready as a narrow workflow idea. Commonplace review gates could keep concise rejection rationales that are automatically presented during the next rewrite attempt, while still requiring human/agent review before promotion.

**Source-segment MCP primitives beside synthesized answers.** Synto's split between `answer_question` and verbatim source tools is worth borrowing for source-backed reviews: expose exact passages as a separate read path so synthesized context does not replace evidence. Ready when Commonplace has a stable source-segment index.

**Pack export as an agent consumption contract.** Synto's `agent/manifest.json`, concepts, sources, routes, segments, and `AGENTS.md` shape is a useful packaging idea for making a KB portable to agents that cannot run the full local toolchain. Needs a concrete consuming-agent target.

**Do not borrow hidden state for core KB truth without a rollback story.** SQLite is useful for operational state, but Commonplace should keep durable claims, review status, and system-definition artifacts in git-tracked files unless the database can be regenerated or versioned with equivalent confidence.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents write raw notes, run CLI/MCP-adjacent workflows, review/verify/approve/reject drafts, curate identities, repair links, and edit published articles; automatic code paths import and segment sources, extract concepts and items, create source summary pages, compile drafts, update indexes, save queries/syntheses, maintain FTS/cache/metrics/audit rows, create stubs, and apply selected lint/maintenance repairs.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `promote` — Compilation consolidates multiple source notes into one concept article; raw-note hashes, synthesis question hashes, aliases, and merge candidates provide deduplication pressure; re-ingest/recompile, alias normalization, concept occurrence attribution, and link repair evolve stored metadata or pages; query synthesis and concept compilation create new articles from existing retained sources; manual-edit detection, deferred compile states, blocked concepts, source hashes, and rejection records mark stale or unsafe update paths; verify/approve/status transitions, confidence thresholds, and pack/index generation promote drafts into stronger consumption surfaces.

### Trace-derived learning

**Trace source:** `tool-traces` `event-streams` — Synto retains rejection events, compile runs, LLM cache hits, metric events, MCP audit rows, saved query/synthesis events, and source-access/backlog signals; it does not mine full chat transcripts or multi-step agent trajectories in the reviewed implementation.

**Learning scope:** `per-project` `cross-task` — Trace state belongs to a vault and affects later runs against that vault, especially future compiles of the same concepts and maintenance reports consumed across tasks.

**Learning timing:** `online` `staged` — Rejections, compile runs, cache/metrics, and MCP audit rows are written during normal use; their behavior-shaping effect is staged into the next compile, review, doctor/backlog, or maintenance pass.

**Distilled form:** `prose` `symbolic` — Rejection feedback is retained prose and injected into later prompts; block status, compile state, query/synthesis hashes, metrics, cache counters, audit rows, and backlog data are symbolic.

The most important trace-derived loop is rejection feedback. `reject_draft()` deletes the draft, stores feedback and rejected body, resets the concept compile state to pending, and auto-blocks after the rejection cap; `compile_concepts()` later loads recent rejections and passes them into the concept write prompt ([src/synto/pipeline/compile.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/pipeline/compile.py), [src/synto/state.py](https://github.com/kytmanov/synto/blob/6b336034b1849443939dcc868feeac1af2fc8c35/src/synto/state.py)). That is not autonomous semantic learning, but it is durable feedback from a prior generation attempt shaping a later generated artifact.

MCP and metric traces are weaker learning signals. `serve.py` can audit tool usage and result counts, and `state.py` contains backlog/report helpers that map hashed resolved labels back to concepts; those traces guide coverage and maintenance, but I did not find code that automatically rewrites articles or reranks query selection from MCP audit rows alone. Synto therefore fits the survey branch where trace-derived state mostly guides compilation and maintenance, not model weights or always-on policy.

## Read-back

**Read-back:** `both` — Agents and users can pull memory by reading files, exported packs, CLI query results, or MCP tools; command/MCP workflows can also push selected retained wiki context into the answering or working agent by prescribed index reads, page selection, status filters, and generated agent entry points.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / judgment` — Coarse read-back comes from generated `AGENTS.md`/`CLAUDE.md`, pack manifests, and default published-only MCP filters; identifiers include article ids, concept names, entity ids, aliases, tags, source ids, segment ids, statuses, paths, and selected pack routes; lexical inference appears in `search_articles`, source-segment FTS, alias substring matching, and index scanning; judgment inference appears when the fast model selects pages for `synto query` or `answer_question`.

**Faithfulness tested:** `no` — The repo has tests for query routing, MCP handlers, pack export, lint, compile, review, and safety behavior, but I did not find an ablation or post-action audit demonstrating that injected wiki context reliably changes downstream agent behavior as intended.

**Direction edge cases.** `answer_question` is a pull tool call from the client, but it pushes selected wiki pages into Synto's internal heavy-model answer prompt. A file-aware external agent reading `INDEX.json` and articles is pull-only unless a host harness automatically loads the generated entry points or pack routes. Static package docs are not counted as accumulated memory read-back; generated pack metadata and vault articles are.

**Selection, scope, and complexity.** Query selection is bounded by `MAX_PAGES = 5` and `MAX_CHARS_PER_PAGE = 8000`, while MCP search caps article and source-segment limits at 50. Article visibility defaults to published, and callers can explicitly opt into verified or draft material. Source tools expose exact paragraphs under a configurable license policy; legacy vaults with no source licenses relax the default to all and warn at server startup. Actual precision, recall, and context dilution are not verified from static code.

**Authority at consumption.** Published articles, source passages, query answers, and synthesis pages are advisory knowledge unless the receiving agent's prompt treats them as stronger instruction. Generated `AGENTS.md`/`CLAUDE.md` files and MCP tool descriptions carry instruction authority for agents that load them. Status filters, license gates, and manual-edit protection enforce access or overwrite boundaries inside Synto, but Synto does not hard-gate downstream actions based on retrieved wiki content.

**Other consumers.** Humans read and edit the vault in ordinary editors or Obsidian, CLI users run review/maintain/query/doctor commands, file-aware agents consume exported packs, MCP clients consume live read tools, and future Synto runs consume the state DB for incremental compilation and curation.

## Curiosity Pass

**"No vector database" does not mean no database.** Synto avoids embedding stores for retrieval, but its operational memory is heavily SQLite-backed. That is a reasonable split, but the rollback and portability story differs from a pure file vault.

**The review loop is stronger than the generation loop.** The LLM writes drafts, but the durable behavioral innovation is the staged review/rejection/blocked-state machinery around those drafts.

**Source passages are a trust escape hatch.** The MCP verbatim tools let a frontier model bypass Synto's generated article when exact wording matters. That is more valuable than making the article generator sound authoritative.

**Concept identity is carrying ontology work without calling itself an ontology.** Entity ids, preferred labels, aliases, occurrence candidates, ambiguity states, and merge/split logs amount to a lightweight concept graph even though the main read surface remains files and indexes.

**Remote MCP is operationally sharp.** The code adds DNS-rebinding host protections, but the CLI help and changelog state there is no built-in auth for Streamable HTTP. That keeps local usage simple and makes deployment boundaries important.

## What to Watch

- Whether MCP audit/backlog data starts automatically affecting query routing, article prioritization, or compile scheduling; that would strengthen the trace-derived learning claim beyond rejection feedback.
- Whether pack export gains enough source-span provenance for agents to verify synthesized article claims without calling the live MCP server.
- Whether the optional RAG hook in ingest becomes a shipped vector-backed retrieval path; that would change the representational-form and read-back classifications.
- Whether `.synto/state.db` gains a git-trackable export/replay format for identity and curation state; without it, file rollback and database truth remain split.
- Whether remote MCP deployments add authentication or capability-scoped clients; source-segment access makes the trust boundary materially important.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Synto's vault can store many articles, but only query, MCP, pack, or file-read workflows activate them for an agent.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Synto splits raw files, generated articles, SQLite state, indexes, packs, and MCP tools across different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: source passages, concept articles, saved queries, synthesis pages, and pack articles mainly serve as evidence and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: SQLite lifecycle state, identity labels, indexes, tool schemas, status filters, and generated agent instructions shape future behavior.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - compares: Synto turns rejection/tool/use traces into future compile and maintenance signals rather than mining full conversations into policies.
