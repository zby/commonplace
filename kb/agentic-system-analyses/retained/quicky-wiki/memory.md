---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Quicky Wiki memory: derived claims, confidence, summaries, provenance, review traces and uneven withdrawal across SQLite and file views."
run-id: AAS-2026-10-15-quicky-wiki-628f7d7cc628-01
source-identity: https://github.com/anzal1/quicky-wiki
reviewed-boundary: cfeecbffce5b6d0f16533b258a1e88edd86f731e
---

# Quicky Wiki memory report

## Boundary and evidence

The memory boundary includes source-file admission, SQLite content and access structures, persisted configuration, optional answer-derived sources, maintenance, direct edits, file views and later model/client reads. It follows the whole-system boundary, not just the primary question-answer route. SRC-1 is the frozen repository at cfeecbffce5b6d0f16533b258a1e88edd86f731e, registered in [boundary](boundary.md#source-register). All findings below are implementation or attributed prompt/design findings. No supplied run establishes actual memory contents, activation, calibration, recovery or benefit.

Direct inspection extended the supplied runtime with store schema, source/page/claim/event writes, row mappers, search and deletion implementations; complete ingestion, comparison, resolution, query, watch, save-answer, lint, Markdown and temporal/cascade implementations; library exports; MCP tool handlers; dashboard server routes; compilation and consensus context construction. Scoped searches checked CLI command dispatch, registered MCP tools, maintenance/discovery consumers, alternative renderers, event readers and dependency writers. These are additional reads within SRC-1, not new sources. The table distinguishes direct inspection from supplied findings.

| Entry point / operation | SRC-1 paths | Coverage and records / limit |
|---|---|---|
| Setup and retained instruction selection | `src/cli/create.ts`, `src/cli/context.ts`, `src/compiler/ingest.ts` | Setup/load behavior supplied by [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup); extraction's entity-prompt consumption directly read. No installed configuration supplied. |
| File, directory and URL ingestion | `src/cli.ts`, `src/cli/ingest.ts`, `src/cli/fetch-url.ts`, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts` | CLI dispatch searched; driver/fetch behavior supplied by [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); all compiler transformations directly read. Claims, control fields and summaries split below. |
| Watched admission / deletion | `src/cli/watch.ts` | Complete direct read; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) annotation. No deletion propagation; startup scan only admits unregistered paths. |
| Schema, indexing and exposed mutations | `src/graph/store.ts`, `src/lib.ts` | Direct schema, constructor, API inventory, mutation, retrieval and row-mapper reads; [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store) and its six parts below. Prepared-statement details not exhaustively audited. Direct library admission principals remain caller-dependent. |
| Ordinary answer / save | `src/graph/query.ts`, `src/cli/query.ts`, `src/cli/save-answer.ts` | Query and save helper directly read; CLI branch behavior supplied by [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-answer-save](runtime.md#rt-rte-answer-save). No authenticated original evidence or hidden reasoning restored. |
| Consensus | `src/compiler/consensus.ts` | Context construction directly read; responder/fallback behavior supplied by [RT-RTE-consensus-answer](runtime.md#rt-rte-consensus-answer). No persisted consensus result established. |
| MCP reads / writes | `src/mcp/server.ts` | Tool inventory searched; query, list/search/get, health, ingest and metadata handlers directly read; [RT-RTE-client-access](runtime.md#rt-rte-client-access). Enclosing agent selection/use is outside captured evidence. |
| Dashboard reads, cache, bookmark, edits, prune | `src/cli/serve.ts` | Server routing directly read; UI request/confirmation sites searched. [RT-RTE-client-access](runtime.md#rt-rte-client-access); file-view and withdrawal qualifications below. No deployed authentication or grants captured. |
| Decay, cascade, lint and review | `src/graph/temporal.ts`, `src/graph/cascade.ts`, `src/cli/lint.ts`, `src/cli/metabolism.ts`, `src/metabolism/redteam.ts`, `src/metabolism/resurface.ts`, `src/metabolism/health.ts`, `src/discovery/discover.ts` | First three directly read; remaining consumers searched and supplied by [RT-RTE-health-review](runtime.md#rt-rte-health-review). Review suggestions are not a retained accepted revision. Dependency initialization by embedding callers is unresolved. |
| Compilation / exports / timeline | `src/cli/compile.ts`, `src/render/markdown.ts`, `src/render/timeline.ts`, `src/render/obsidian.ts`, `src/render/anki.ts`, `src/render/marp.ts` | Compile/Markdown/timeline directly read; other selectors searched. [MEM-OBJ-rendered-views](#mem-obj-rendered-views). Alternative templates not fully inspected; no downstream application behavior established. |
| Model/provider state | `src/llm/adapter.ts` | Supplied [RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter). Distributed parameters and provider retention are opaque, not absent. No inference about endpoint training or internal conversation memory. |
| Release artifacts | `package.json`, `.github/workflows/publish.yml` | Supplied [RT-RTE-package-release](runtime.md#rt-rte-package-release); excluded from the retained-knowledge mechanism account, not from the system boundary. No installation or runtime code improvement established. |

User corpora, generated databases/views, model calls, external client policies and dependency internals were not supplied. Available but uninspected UI/export details are inspection limits, not access gaps. No external retrieval research, target execution or provider invocation was performed.

## Core ideas

1. **The reusable memory is an extracted graph, not a transcript.** Source files become claim statements, confidence/control fields, provenance links, summaries and events. Later calls reconstruct selected messages from these parts. Extraction/comparison calls do not preserve their complete conversations or hidden reasoning in the inspected graph schema (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/graph/store.ts`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).
2. **A contradiction normally changes reliance without replacing the statement.** The comparison marks an existing claim challenged, lowers its confidence and retains a reason in an event. That branch does not also retain the new contradictory statement as a new claim. The next ordinary answer sees old statement plus lower confidence, not the event reason or the new source body. This is narrower than a complete retained debate ([MEM-OBJ-claims](#mem-obj-claims), [MEM-OBJ-epistemic-events](#mem-obj-epistemic-events)).
3. **Summaries have two different consumer roles.** Their text reaches people/client page listings and search; search hits can indirectly select page claims for answering. Ordinary answer construction does not insert the summary itself. Summary refresh is coupled to ingestion, not every claim/score mutation. “Compaction” would therefore be misleading if taken to mean conversation replacement or a uniform maintenance guarantee ([MEM-OBJ-page-summaries](#mem-obj-page-summaries)).
4. **Trust labels and bounded context do not mean verified evidence.** Source quality is inferred from caller options/frontmatter and used in scoring. Ordinary retrieval has count limits but no aggregate token budget; comparison and consensus can receive all claims. Models interpret rounded scores as text; code uses the same scores for sorting, staleness and decay. None of this establishes calibrated confidence ([MEM-OBJ-claim-controls](#mem-obj-claim-controls), [RT-CLM-confidence-citations](runtime.md#rt-clm-confidence-citations)).
5. **Withdrawal is substrate-specific.** Database deletion removes claims and their local event/provenance relations; it does not remove original sources, saved answers or already-rendered files. A changed file does not retract its earlier claims automatically. Later consumers can therefore disagree about what remains ([MEM-OBJ-rendered-views](#mem-obj-rendered-views), [RT-RTE-client-access](runtime.md#rt-rte-client-access)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-claims
Label: Claim statement content

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity: `claims.statement`, UUID-addressed and page-associated. SQLite stores natural-language assertions; model/human interpretation gives them semantic force. This is the content part of the supplied store, not a replacement store. Confidence and provenance have separate consumers and are declared separately below. Extracted source text is transformed into these statements; direct store/dashboard edits provide another lineage. The initial contents of any embedding-created database are uninspected (SRC-1, `src/graph/store.ts`, `src/compiler/ingest.ts`, `src/compiler/resolve.ts`, `src/cli/serve.ts`).

Later consumers include diff comparison, page summary generation, ordinary/consensus answering, discovery, reviews and exports. Delivery is wired evidence/context, not executable instruction or verified truth. The compiler admits without per-claim human approval; direct dashboard PATCH accepts a supplied string. A human can author an edit, but generic HTTP/library callers do not establish human approval. Statement edits replace current content without storing the previous wording in that method (SRC-1, `src/graph/store.ts`, `src/cli/serve.ts`).

> "UPDATE claims SET statement = ? WHERE id = ?"
> --- `src/graph/store.ts`

Challenge retains the existing statement and a reduced score rather than automatically installing its challenger. The `challenges` branch in comparison populates `diff.challenged`; the resolver calls `challengeClaim` and cascade. This is distinct from the `new` branch that produces `diff.newClaims`. Omitted/invalid matches can drop a proposed statement; parse failure instead falls back to all-new admission. These countercases preclude a complete source-to-claim preservation guarantee (SRC-1, `src/compiler/diff.ts`, `src/compiler/resolve.ts`; [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

> store.challengeClaim(c.claimId, source.id, c.confidenceAfter, c.reason);
> --- `src/compiler/resolve.ts`

#### MEM-OBJ-claim-controls
Label: Claim confidence and access controls

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity: claim ID/page ID, `confidence`, `first_stated`, `last_reinforced`, `decay_rate` and `tags_json`. These are symbolic identifiers, scalar controls and serialized labels in SQLite, distinct from assertion text. Confidence is not a learned embedding or distributed parameter. Code consumes these fields for filtering, ordering, time decay and candidate selection; answer/summary/review models receive some as natural-language percentages. They persist across commands until overwritten/deleted (SRC-1, `src/graph/store.ts`, `src/graph/temporal.ts`, `src/graph/query.ts`; [RT-RTE-health-review](runtime.md#rt-rte-health-review)).

Lineage includes model initial confidence weighted by source quality, fixed reinforcement/challenge rules, elapsed-time decay, edge-based cascade and direct caller edits. The quality multipliers range from 1.0 for peer-reviewed to 0.35 for social, with blog at 0.6 and unknown at 0.45. These labels alter scores without authenticating source quality. Reinforcement uses a source-count-dependent weighted merge, not a guaranteed confidence increase (SRC-1, `src/compiler/confidence.ts`). Admission is software/model controlled in the compiler/decay routes and supplied-content acceptance on direct edits. Authorship, transport access and per-content approval are different. The public store does not impose the compiler's clamp on every direct numeric write. Generic confidence updates also reset the reinforcement timestamp; they do not add an event. Thus a decay/cascade/edit changes later staleness selection as well as the number, without the same history as reinforcement (SRC-1, `src/graph/store.ts`, `src/graph/temporal.ts`, `src/graph/cascade.ts`).

> updateClaimConfidence(id: string, confidence: number): void {
>     this.db
>       .prepare(
>         "UPDATE claims SET confidence = ?, last_reinforced = ? WHERE id = ?",
>       )
>       .run(confidence, new Date().toISOString(), id);
>   }
> --- `src/graph/store.ts`

> const weight = 1 / (1 + sourceCount * 0.1);
>   const merged = existing * (1 - weight) + newEvidence * weight;
> --- `src/compiler/confidence.ts`

The timestamp is behavioral metadata, not evidence that a source actually reinforced a claim. Confidence-driven reuse establishes a retained control effect in code, not empirical accuracy or learning benefit.

#### MEM-OBJ-page-summaries
Label: Page summary text

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity: `pages.summary`. Natural-language model output persists in a SQLite text column. `generatePageSummaries` supplies the page title and all its claim statements with rounded confidence; a prompt requests one sentence of at most 30 words. Code accepts trimmed output longer than five characters, without enforcing a word limit or human approval. Reasons/source excerpts are not separately retained with the summary (SRC-1, `src/compiler/resolve.ts`, `src/graph/store.ts`).

> if (summary && summary.length > 5) {
>           store.updatePageSummary(pageId, summary);
>         }
> --- `src/compiler/resolve.ts`

This is derived content, not a raw trace or provider checkpoint. Touched/missing-summary pages refresh during resolution; failures leave previous/empty summaries. Direct claim statement edits, deletions and decay do not invoke this helper in their inspected callers. Consequently a stale summary can remain indexed even after its underlying claims change. Later `store.search` considers summaries, and ordinary query expands a matched page to up to ten claims if it has no direct claim-hit group. The summary influences selection there, while only claims enter the answer text. MCP page/list/entity reads and Markdown rendering expose summary text directly (SRC-1, `src/compiler/resolve.ts`, `src/graph/query.ts`, `src/graph/store.ts`, `src/mcp/server.ts`, `src/render/markdown.ts`).

> full.claims.slice(0, 10).map((c: any) => ({
> --- `src/graph/query.ts`

#### MEM-OBJ-source-register
Label: Source and entity access metadata

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity: `sources` rows, `claim_sources`, and page kind/metadata columns. These symbolic paths, hashes, quality/type labels, JSON metadata and provenance identities are not copies of original source bodies. Source files remain separate filesystem inputs. Metadata may contain prose, but equality filters, kind selection and metadata merge use fixed field rules, not model interpretation. Source rows link claims to recorded sources; reinforcement adds a link, while challenge records its source in the event rather than adding a reinforcing provenance link (SRC-1, `src/graph/store.ts`).

> .prepare(
>           "INSERT OR IGNORE INTO claim_sources (claim_id, source_id) VALUES (?, ?)",
>         )
>         .run(claimId, sourceId);
> --- `src/graph/store.ts`

Lineage: caller-selected files/frontmatter/overrides, compiler-generated hashes/UUIDs, and caller metadata merges. Authorship of input files is not authenticated. A changed source updates hash/time but reuses its previous source object, including stored quality/type; identical bytes skip claim extraction while still merging page metadata/kind. Thus changing extraction configuration or quality options does not itself invalidate the content-hash skip. Page metadata merges preserve unspecified keys, not exact replacement of all old metadata. The `syncPrimaryPageEntity` comment's “frontmatter authoritative” wording must be read against that merge implementation (SRC-1, `src/compiler/ingest.ts`, `src/graph/store.ts`).

> const next = { ...current, ...patch };
> --- `src/graph/store.ts`

Consumers: hash/time checks determine later ingestion; source qualities shape extraction confidence; source links/counts appear in review/page/export views; kind/metadata support MCP entity selection. Ordinary QA does not receive source identity or metadata. The graph is provenance-indexed, not a source snapshot or authenticated evidence archive (SRC-1, `src/compiler/ingest.ts`, `src/graph/query.ts`, `src/mcp/server.ts`, `src/render/markdown.ts`).

#### MEM-OBJ-epistemic-events
Label: Epistemic event history

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity: `epistemic_events`, read into `Claim.timeline`. SQLite retains symbolic IDs/type/time/source and before/after confidence plus natural-language `note`. Creation and reinforcement notes are generic; challenged events retain the model reason or fallback. These are reduced mutation traces, not full extraction/diff responses or independent raw observations. The public `addEvent` API also allows externally supplied history; its original provenance is caller-dependent (SRC-1, `src/graph/store.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`).

> INSERT INTO epistemic_events (id, claim_id, date, type, trigger_source_id, confidence_before, confidence_after, note)
>         VALUES (?, ?, ?, 'challenged', ?, ?, ?, ?)
> --- `src/graph/store.ts`

`rowToClaim` attaches timeline data, but attachment to an object is not delivery to every model. Ordinary query, comparison, summaries and consensus select statements/scores rather than event notes. Dashboard events expose trace fields; timeline rendering selects event type/date/score transition and current statement, not the full historical assertion/reason. The record therefore preserves a challenge reason for inspection without establishing that the next reasoning call consults it (SRC-1, `src/graph/store.ts`, `src/graph/query.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/compiler/consensus.ts`, `src/render/timeline.ts`, `src/cli/serve.ts`).

> const timeline = this.getClaimTimeline(id);
> --- `src/graph/store.ts`

Direct statement/confidence edits lack matching history writes; deletion destroys associated events. This is not a complete audit/version/rollback substrate (SRC-1, `src/graph/store.ts`).

#### MEM-OBJ-graph-relations
Label: Dependency, contradiction and page links

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity: `claim_dependencies`, `claim_contradictions`, `page_links`. These symbolic ID pairs reside in SQLite. The first controls cascade/dependent selection; contradiction edges control contested flags/review/lint; page links support navigation/rendering. Their lineage differs: ingestion creates concept/co-citation page links, but extraction's dependency strings do not survive diff/resolution as claim-edge writes. Store APIs permit caller-supplied claim edges; source search found their declarations but no shipped calls to either edge-adder. This agrees with, rather than duplicates, the ingestion-route finding (SRC-1, `src/graph/store.ts`, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

> store.addPageLink(uniquePageIds[i], uniquePageIds[j]);
>       store.addPageLink(uniquePageIds[j], uniquePageIds[i]);
> --- `src/compiler/resolve.ts`

Admission of page links is software controlled. Initialization/admission of any externally populated claim edges remains unknown; this prevents claiming automatic dependency discovery or exercised cascade. Given such edges, cascade updates dependent confidence with damping, depth and small-delta stops. Ordinary QA does not traverse those edges; their numerical consequences may arrive through confidence. Deletion removes touching edges rather than retaining a withdrawn relation record (SRC-1, `src/graph/cascade.ts`, `src/graph/store.ts`, `src/graph/query.ts`).

#### MEM-OBJ-rendered-views
Label: Rendered file views

Distinct identity: filesystem outputs of render/compile/export, not the SQLite substrate or transient [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff). Closest supplied records are [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store) and [RT-RTE-client-access](runtime.md#rt-rte-client-access); those refer to the authoritative store and client route, not these separately persisted files. No supplied object declares the output files themselves.

Source-native identity: `wiki/` Markdown pages and compile/export outputs. They combine natural-language summaries/statements with symbolic frontmatter, links, scores and display markers. Markdown rendering reads current graph content and overwrites each nonempty page file. Other compile targets include model-generated slides, Anki text, graph HTML and timeline Markdown; Obsidian export creates additional page/source/index/dashboard files. These are derived views with different selectors, not source backups (SRC-1, `src/render/markdown.ts`, `src/cli/compile.ts`, `src/render/obsidian.ts`, `src/render/anki.ts`, `src/render/marp.ts`, `src/render/timeline.ts`).

> if (claims.length === 0) continue;
>     const p = await renderWikiPage(store, page, wikiDir);
> --- `src/render/markdown.ts`

Automatic render admission follows driver completion; explicit compile/export is user-triggered without per-output approval. There is no cleanup of obsolete files in `renderAllPages`, and lint prune deletes database rows only. Readers can therefore retain withdrawn claims in old files. Standard query reads the store, not these files; however dashboard `/api/page` explicitly reads an existing file under the literal working-directory `wiki` path and includes it as `markdown`. This display consumer is a concrete read-back exception to treating all rendered bytes as terminal-only output. External Obsidian/Anki/slide use is afforded by the exports, not observed here (SRC-1, `src/render/markdown.ts`, `src/cli/lint.ts`, `src/cli/serve.ts`).

> const wikiPath = join(process.cwd(), "wiki", full.page.path);
>           if (existsSync(wikiPath)) {
>             markdown = await readFile(wikiPath, "utf-8");
>           }
> --- `src/cli/serve.ts`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Storage/form split: the six declared parts distinguish semantic content, access/control data, derived summaries, provenance, reduced traces and relations. FTS tables are derived symbolic text indexes over claim statements and page titles/summaries, maintained by SQLite triggers. They are not embeddings. Constructor migration/rebuild code repairs schema/index structures; it does not validate source truth. Payloads in this store are readable text/JSON, not opaque provider checkpoints (SRC-1, `src/graph/store.ts`).

> CREATE VIRTUAL TABLE IF NOT EXISTS pages_fts USING fts5(
>   title,
>   summary,
>   content=pages,
>   content_rowid=rowid
> );
> --- `src/graph/store.ts`

#### On [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup)

Memory-specific authority: persisted configuration selects provider/model, paths, entity kinds and extraction guidance. The entity-specific text is appended to the extraction system message, unlike graph assertions supplied as user-message evidence. Static shipped defaults are not accumulated memory; edited project configuration is retained operator/caller input. Servers/watch retain their loaded configuration. Human control is evidenced for explicit setup options, not for every possible external config writer. No automatic critique-to-prompt rewrite is established (SRC-1, `src/compiler/ingest.ts`; setup/load passages supplied in this record).

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Raw-to-derived lineage: caller file bytes → body/chunks → extracted claim arrays → comparison diff → graph parts → future model/client contexts. File path/hash metadata is persisted before this chain completes; it is not a successful-compilation checkpoint. Reasons partly survive only as challenge notes; complete prompts/responses and discarded statements do not survive in the inspected schema. Summary text is derived from claims, not a retained conversation compaction (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/graph/store.ts`).

Working context: code opens independent system/user message calls. Bodies above 12,000 characters use 8,000-character slices with 500 overlap; statement prefixes normalized to 80 characters deduplicate returned claims. Only extracted arrays escape each call. Comparison sees all stored/new statements; page assignment sees all titles in batches of eight claims; summary calls see one page's claims with concurrency three. None provides a uniform token budget or reloads hidden reasoning. The disposable-call/frame analogy fits isolated inputs/returns, but there are no model-visible pointers or source-level sub-agent frames to restore. Later retrieval reconstructs text by value (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`).

> const chunkSize = 8000;
>   const overlap = 500;
> --- `src/compiler/ingest.ts`

Watcher processing is automatic supply to the compiler after a filesystem event, not unsolicited supply to the answer model. The user need not approve each extracted claim. Startup admits unregistered files; deletion is ignored. Updating a source does not first withdraw all prior source-associated statements, and an unchanged failed source may skip on retry. Accordingly file lifetime, admission completion and graph lifetime are distinct (SRC-1, `src/cli/watch.ts`, `src/compiler/ingest.ts`, `src/compiler/resolve.ts`; hash/recovery passages supplied in the record).

> // File was deleted, ignore
> --- `src/cli/watch.ts`

#### On [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)

Read-back direction is request-driven: question → code search → selected retained statements/scores → answer model. It is not independent background injection. Search strips non-ASCII-alphanumeric characters, removes stop/short words, performs prefix-OR FTS with LIKE fallback and limits pages/claims independently to 50. Page-only matches expand to at most ten claims. Result counts bound selection, not total tokens. The answer gets page headings and rounded score/statement lines, not source documents, source identities, graph edges, metadata, claim IDs or event reasons. Claims can be low-confidence and still be retrieved; scores are guidance rather than a hard truth gate (SRC-1, `src/graph/store.ts`, `src/graph/query.ts`; model-visible line passage supplied in this record).

Each invocation rebuilds context. Plain answers are not persisted; model activation and benefit remain unobserved. A source path retained elsewhere does not mean this consumer can automatically dereference it.

#### On [RT-RTE-consensus-answer](runtime.md#rt-rte-consensus-answer)

Read-back selector differs materially from ordinary query: code groups all page-associated claims/confidences rather than question-filtering the graph. Each independent responder gets that same context and question; comparison consumes successful response content including reasoning. These are current-invocation arrays, not retained prior debate. The supplied route's single-response and fallback qualifications remain. No aggregate token budget or later saved consensus artifact is established (SRC-1, `src/compiler/consensus.ts`).

> const allClaims = store.listClaims();
> --- `src/compiler/consensus.ts`

#### On [RT-RTE-answer-save](runtime.md#rt-rte-answer-save)

Retained result: natural-language answer and resolved cited statements plus symbolic question/time/confidence frontmatter in `synthesis-<question-slug>.md`. This is derived model output re-presented as a source, not independent confirming evidence. The human save flag authorizes file retention, not factual validation. The helper uses `quality: blog`; the ordinary compiler later re-extracts this document, with explicit ingest or a watcher required. A question-derived filename can overwrite an earlier answer. It preserves neither original model messages nor authenticated source excerpts (SRC-1, `src/cli/save-answer.ts`, `src/cli/watch.ts`).

> `quality: blog`,
> --- `src/cli/save-answer.ts`

This is the concrete answer-trace-fed update path: graph context → generated answer → saved document → re-extraction → graph → later question. It can shape future capacity through retained content, but the source provides no exercised loop, independent corroboration, retained error evaluation or improvement attribution. Save/reingest does not change model weights.

#### On [RT-RTE-client-access](runtime.md#rt-rte-client-access)

Read-back targeting: MCP `get_page` requests title; `search_wiki` requests lexical text with limit 20; `list_entities` requests kind and exact top-level metadata equality; `list_claims` selects confidence range and slices a caller/default limit. Page views expose summary/claims/counts/tags, not complete original evidence. Tool delivery is wired; an enclosing agent's use or obedience is unknown. Direct library store access is a capability, not a deployed external consumer route (SRC-1, `src/mcp/server.ts`, `src/lib.ts`).

Withdrawal/editing: dashboard PATCH replaces statement/confidence after basic type checks, without independent approval or a retained previous version. Database claim deletion removes its events/source links and touching dependency/contradiction edges, but leaves source rows/files and page summaries. Empty-page prune removes page links/rows; it is not low-confidence claim pruning. Page deletion exists as a store capability but its dashboard branch is shadowed as the runtime states. SQLite FTS triggers track database changes; rendered files and saved answers do not receive the same invalidation. Dashboard cache invalidation is process-local with TTL fallback, not a cross-client coherence protocol (SRC-1, `src/graph/store.ts`, `src/cli/serve.ts`, `src/cli/lint.ts`, `src/render/markdown.ts`).

> this.db.prepare("DELETE FROM claims WHERE id = ?").run(id);
> --- `src/graph/store.ts`

No tombstone prevents later re-extraction, no source withdrawal API is shown in the inventoried store, and unchanged source/hash skip can leave a manually deleted claim absent until some different admission path runs. These are bounded findings about the inspected API/compiler, not a claim about operator backups or arbitrary embedding code (SRC-1, `src/graph/store.ts`, `src/compiler/ingest.ts`).

#### On [RT-RTE-health-review](runtime.md#rt-rte-health-review)

Curation differs by operation. Decay deterministically changes durable confidence/time controls; red-team, resurfacing and discovery produce invocation-local suggestions. Lint reports structural issues, low scores, self-dependency and unresolved contradiction edges; it neither checks every factual assertion nor automatically accepts a repair. Its prune option deletes empty pages only. User initiation is not per-update approval; review output needs a separate edit/ingest decision to become retained content (SRC-1, `src/graph/temporal.ts`, `src/cli/lint.ts`; review selection/output passages supplied in this record, corroborated by searches of `src/cli/metabolism.ts`, `src/metabolism/redteam.ts`, `src/metabolism/resurface.ts`, `src/discovery/discover.ts`).

> const pruned = store.deleteEmptyPages();
> --- `src/cli/lint.ts`

Later ordinary answers consume decayed scores without the update's reason. Review suggestions are not thereby learned methods or retained criticism iterations. A human could transfer a suggestion through another admission surface, but that is an afforded possibility, not a wired acceptance route in these callers.

#### On [RT-BAP-retained-context](runtime.md#rt-bap-retained-context)

Authority differs at actual consumers: code treats IDs/hashes/metadata/numbers by fixed rules; model calls interpret selected claims/scores as evidence-like user-message text; configured entity guidance reaches a system-message channel; browser/MCP readers receive display/API content. Source trust and admission do not become instruction authority merely because a statement is persisted. Reasons stored in event notes do not follow the claims into the ordinary answer model. These distinctions qualify a system-wide claim of uniform memory authority (SRC-1, `src/graph/store.ts`, `src/compiler/ingest.ts`, `src/graph/query.ts`, `src/mcp/server.ts`, `src/cli/serve.ts`).

## Write side

Acquisition is file/URL/watch/client-driven. Compiler calls automatically derive and admit content; source authorship is separate from per-claim admission. Model extraction/comparison plus fixed score rules decide normal graph updates. Parse/index/DB failures are technical rejection, not a truth oracle; comparison fallback can admit all proposals. Public store calls and dashboard edits provide alternate software-admitted writes whose ultimate human control depends on the caller. Metadata merge is another admission mechanism, not a semantic claim review (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/cli/serve.ts`, `src/lib.ts`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-client-access](runtime.md#rt-rte-client-access)).

Maintenance changes current scores, derived summaries or graph structure on different schedules. Claims and challenge events retain only selected reasons; ordinary consumers do not reconstruct an evidence debate from them. Red-team critique and discovery remain proposals. Deletion destroys local history rather than installing a retained rejection. Source replacement is incremental admission, not source-wide retraction; raw deletion is ignored by watch. These effects follow the separate parts and annotations above, not an assumed universal “living knowledge” guarantee (SRC-1, `src/graph/store.ts`, `src/compiler/resolve.ts`, `src/cli/watch.ts`; [MEM-OBJ-epistemic-events](#mem-obj-epistemic-events), [MEM-OBJ-rendered-views](#mem-obj-rendered-views)).

The only traced answer-derived retention is opt-in save then later ingest/watch. Event rows are reduced traces, not automatically transformed into new method guidance. No inspected schema/caller establishes a host-compaction checkpoint or restored conversation tail; inaccessible provider state remains unresolved rather than classified as absent (SRC-1, `src/cli/save-answer.ts`, `src/graph/store.ts`; [RT-RTE-answer-save](runtime.md#rt-rte-answer-save), [RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter)).

## Read-back

The ordinary model route is pull: requester question → lexical selector → current claims/confidences → fresh answer. Consensus reads the full graph's page-associated claims. Ingestion comparison and page assignment reread retained claims/titles as part of new admission; summaries read one page's claims. Review requests select high-confidence, stale or low-confidence subsets; scores and timing affect those selections. None of these consumers is established merely from storage methods: the cited shipped callers construct their messages explicitly (SRC-1, `src/graph/query.ts`, `src/compiler/consensus.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`; [RT-RTE-health-review](runtime.md#rt-rte-health-review)).

MCP/dashboard/CLI page, search, claim, event and timeline reads deliver retained parts to clients or humans. Their authority is informational; downstream adoption is outside captured evidence. Dashboard file read-back can expose a stale Markdown view alongside current graph data. Exports afford later readers without proving deployment. Watch is a push into the admission pipeline, not a push into a model's ongoing conversation. No inspected route implements one shared context window with global compaction/eviction/reload rules (SRC-1, `src/mcp/server.ts`, `src/cli/serve.ts`, `src/cli/watch.ts`, `src/render/timeline.ts`; [MEM-OBJ-rendered-views](#mem-obj-rendered-views)).

## Integration issues

- **No supplied fact needs replacement.** Qualify the runtime's “Markdown is a derived view, not query input” as applying to standard model queries. Dashboard page reads do load existing Markdown for display. This does not contradict the ordinary QA route, but prevents treating generated files as having no shipped later consumer. Evidence: SRC-1, `src/cli/serve.ts`; [MEM-OBJ-rendered-views](#mem-obj-rendered-views), [RT-RTE-client-access](runtime.md#rt-rte-client-access).
- **Containment, not duplicate identity:** the six SQLite-part records are explicitly parts of [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store), separated because their forms, admission, invalidation and consumers differ. The rendered-view object is a distinct derived filesystem artifact. No new record is intended to replace a supplied record.
- **Dependency initialization remains unresolved:** the store permits claim edges, but shipped extraction drops their proposed strings. Unknown embedding-created edges prevent asserting automatic dependency construction or exercised propagation; populated edges still support a conditional cascade capability. Evidence: SRC-1, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/graph/store.ts`; [MEM-OBJ-graph-relations](#mem-obj-graph-relations), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).
- **Reasons versus later reliance:** challenge notes survive but the next answer receives only statement/score. A retained criticism should not be inferred to be a later model input. Evidence: SRC-1, `src/graph/store.ts`, `src/graph/query.ts`; [MEM-OBJ-epistemic-events](#mem-obj-epistemic-events), [RT-BAP-retained-context](runtime.md#rt-bap-retained-context). This is a consumer limit, not denial of the retained note.
- **Independent withdrawal and freshness:** edited/deleted/decayed claims can coexist with stale summaries, file views or saved syntheses. No supplied artifacts establish which version any actual deployment displayed. Evidence: SRC-1, `src/graph/store.ts`, `src/compiler/resolve.ts`, `src/render/markdown.ts`, `src/cli/save-answer.ts`; [MEM-OBJ-page-summaries](#mem-obj-page-summaries), [MEM-OBJ-rendered-views](#mem-obj-rendered-views), [RT-RTE-answer-save](runtime.md#rt-rte-answer-save).
- **Opaque alternatives and caller lineage:** provider state, embedding admission policies, installed configs and actual external client behavior remain uninspected. This prevents complete provenance, exercised trace-learning or benefit claims, not the statically established retained graph/read-back account. Evidence: SRC-1, `src/lib.ts`; [RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter), [RT-RTE-client-access](runtime.md#rt-rte-client-access).

## Limitations and checks

Source HEAD was rechecked as cfeecbffce5b6d0f16533b258a1e88edd86f731e and the checkout status was clean. Source identity and run/boundary fields match the supplied invocation/boundary. This member follows the supplied memory type and shared-record contract; it adds no sources, delegates no work and does not execute target code. Searches challenged universal dependency, source-withdrawal, durable-critique, summary-freshness and rendered-output assumptions against alternate paths. Missing observed runs prevents activation, calibration, effectiveness and recovery conclusions; no absence record is inferred from missing traces. Alternative export/UI details and opaque external state retain the limits named in the coverage table.

Deterministic validation: the supplied `commonplace-run validate-output` command passed the member content check (exit 0); its result states that invocation residue is not checked. Form/quotation validation does not establish semantic correctness, claim support or job acceptance.
