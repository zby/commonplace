---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "llm-wiki memory: trace-derived pages, host and MCP read-back, graph metadata, optional review and maintenance"
run-id: AAS-2026-10-16-llm-wiki-6786c5985cdc-01
source-identity: "https://github.com/Pratiyush/llm-wiki"
reviewed-boundary: b1088890ee0743810a92577aecad946c6b3eb2d2
---

# llm-wiki memory report

## Boundary and evidence

The subject is the file-based knowledge loop fixed by [boundary](boundary.md), at SRC-1 commit b1088890ee0743810a92577aecad946c6b3eb2d2. Memory scope includes converted traces, derived wiki content, access metadata, pending synthesis, candidate archives, diagnostic read-back, instruction revision and publication. External agent windows, provider weights, private stores and deployed editor/vault state are not supplied. Their exclusion prevents conclusions about actual context loading, semantic correctness, durability in use or benefit. Available but unread variants are not access gaps.

Direct inspection added SRC-1 `llmwiki/confidence.py`, `llmwiki/lifecycle.py`, `llmwiki/ingest_queue.py`, `llmwiki/context_md.py`, `llmwiki/candidates.py`, `llmwiki/lint/__init__.py`, selected lint rules, MCP query/search and metadata endpoints in `llmwiki/mcp/server.py`, graph extraction/query in `llmwiki/graphify_bridge.py`, log archival in `llmwiki/synth/pipeline.py`, CLI lint dispatch, `CLAUDE.md`, `AGENTS.md`, `.claude/commands/wiki-{sync,update,reflect}.md`, `.claude/skills/self-learn/SKILL.md` and `.claude-plugin/plugin.json`. These supply implementation and doctrine/design evidence only. Conversion, backend variants, publication, editor wiring and provider details not reread here use the supplied runtime/boundary evidence, identified below. HEAD was rechecked against the pin; Git status was clean. No target code, tests, examples or providers were executed.

| Entry point / operation | Source path (SRC-1) | Coverage and limit |
|---|---|---|
| CLI sync, adapter acquisition, raw/state writes, quarantine | `llmwiki/cli.py`, `llmwiki/convert.py`, `llmwiki/adapters/` | Supplied [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion); raw trace and selector distinctions below. Individual native-store normalization not audited; full trace fidelity prevented. |
| Direct host ingest and query; save answer | `CLAUDE.md`, `AGENTS.md` | Direct read; [MEM-OBJ-wiki](#mem-obj-wiki), annotations on host route. |
| Backend synthesis, dummy/Ollama/agent variants, prompt override | `llmwiki/synth/pipeline.py`, `llmwiki/synth/agent_delegate.py`, `llmwiki/synth/ollama.py` | Supplied [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion); direct log-helper read. No completed generation observed. |
| Pending prompt read/cleanup | `.claude/commands/wiki-sync.md`, `llmwiki/synth/agent_delegate.py` | Direct procedure plus supplied implementation; [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts). UUID, not content-quality, gate. |
| Candidate promote/merge/discard/stale list | `llmwiki/candidates.py` | Direct; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [MEM-OBJ-candidate-archive](#mem-obj-candidate-archive). Initialization remains unresolved; direct ingest bypasses it. |
| Update, reflection and optional saved report | `.claude/commands/wiki-update.md`, `.claude/commands/wiki-reflect.md` | Direct; [MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance). Instruction compliance unobserved. |
| Trace-to-method revision | `.claude/skills/self-learn/SKILL.md` | Direct; [MEM-RTE-self-learn](#mem-rte-self-learn). External personal framework copy not frozen. |
| MCP query/search/read/source listing/export | `llmwiki/mcp/server.py` | Query/search direct; other endpoints supplied [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access). [MEM-CLM-archive-visibility](#mem-clm-archive-visibility) challenges universal withdrawal. |
| MCP confidence/lifecycle/dashboard/entity/category | `llmwiki/mcp/server.py`, `llmwiki/lint/__init__.py` | Direct; [MEM-RTE-quality-inspection](#mem-rte-quality-inspection). Stored metadata read-back, not automatic recalculation. |
| Confidence/decay and lifecycle library operations | `llmwiki/confidence.py`, `llmwiki/lifecycle.py` | Direct bodies and bounded caller search; [MEM-OBJ-quality-metadata](#mem-obj-quality-metadata). Durable update caller not established. |
| CLI graph build/query | `llmwiki/graphify_bridge.py`, `llmwiki/cli.py` | Direct extraction/query plus persistence search; [MEM-RTE-graph-query](#mem-rte-graph-query). External Graphify internals excluded; built-in graph engine not independently audited. |
| Folder context, scaffold hot/memory/identity files | `llmwiki/context_md.py`, `llmwiki/cli.py`, `AGENTS.md` | Direct; [MEM-OBJ-navigation](#mem-obj-navigation). Scaffold labels do not prove automatic consolidation or push injection. |
| Queue and SessionStart registration | `llmwiki/ingest_queue.py`, `.claude-plugin/plugin.json` | Direct; [MEM-OBJ-ingest-queue](#mem-obj-ingest-queue). Hook implementation absent per boundary; producer/consumer wiring unresolved. |
| Static reader, exports and optional metadata-only Claude overview | `llmwiki/build.py`, `llmwiki/exporters.py` | Supplied [RT-RTE-reader-build](runtime.md#rt-rte-reader-build). Publication is a separate retained representation, not proof that semantic wiki pages drive all exports. |
| Vault/editor overlays; tests, CI and repairs | `llmwiki/vault.py`, `integrations/`, `tests/`, `.github/workflows/`, `scripts/` | Supplied boundary inventory, runtime vault notes and scoped searches only. Exact overlay/library overwrite policies, all repair transformations and evaluator assertions remain uninspected here; no universal admission or test-success conclusion. |

## Core ideas

1. **Retention is not one store with one admission gate.** Raw Markdown preserves rendered session evidence; source/entity/concept pages summarize it; JSON mtimes select future work; pending UUIDs coordinate deferred work. Direct host edits, backend writes and optional candidate transitions have different admission controls. [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion), [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission).
2. **Read-back selects different information by route.** Host instructions request semantic navigation through index/overview/folder descriptions to full pages. MCP query ranks text and returns snippets. CLI graph query returns node labels and paths, not page claims. The latter cannot stand in for a full-content answer. [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest), [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), [MEM-RTE-graph-query](#mem-rte-graph-query).
3. **Quality names exceed their enforcement.** Confidence/lifecycle helpers expose calculations and transitions; inspected MCP tools read stored fields, and lint emits reports. Candidate archival preserves reasons but does not remove archived Markdown from every later query. [MEM-OBJ-quality-metadata](#mem-obj-quality-metadata), [MEM-RTE-quality-inspection](#mem-rte-quality-inspection), [MEM-CLM-archive-visibility](#mem-clm-archive-visibility).
4. **Context budgets mostly filter inputs, rather than compacting a host conversation.** The supplied runtime establishes 8,000-character synthesis prefixes, bounded build metadata and MCP snippets. Folder descriptions afford model-directed omission before full reads. The full files remain separately reachable. No inspected mechanism establishes target-controlled host-window eviction or a popped subagent frame; provider-internal contexts remain opaque. [MEM-OBJ-navigation](#mem-obj-navigation), [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), [RT-RTE-reader-build](runtime.md#rt-rte-reader-build).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-wiki
Label: Derived wiki content

SRC-1: `CLAUDE.md`, `AGENTS.md`. UTF-8 Markdown on the local filesystem. Natural-language summaries, facts, quotes and contradictions have model/human interpretation as their downstream consumer; symbolic frontmatter, filenames and links support discovery and tooling. This is the retained endpoint of [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest) and [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), not another route or the static prompt [RT-OBJ-source-page](runtime.md#rt-obj-source-page). No object counterpart is declared in runtime.

Lineage: raw rendered session material → per-source summary → entity/concept/overview integration; optional query answer → saved synthesis. Raw provenance can include user statements, assistant output, tool previews and imported non-session sources; adapter identity alone does not make every claim user-authored. Host doctrine requests reasons and source references, but enforced completeness of those reasons is not established. Backend views can omit the raw tail and existing wiki context. Later consumers include foreground ingest/query and MCP text selection; delivery supplies knowledge/context, not binding truth or demonstrated compliance.

> 9. **Flag contradictions** — if a new source contradicts existing wiki content, add a `## Contradictions` section to the affected page and leave BOTH claims visible. Do not silently overwrite.
> --- `CLAUDE.md`

#### MEM-OBJ-navigation
Label: Navigation and scaffold memory surfaces

SRC-1: `CLAUDE.md`, `AGENTS.md`, `llmwiki/context_md.py`, `llmwiki/cli.py`. Index/overview and folder `_context.md` are local Markdown. Folder prose is natural-language selection guidance for the host, while the exact `_context.md` filename is symbolic discovery/exclusion metadata. `load_folder_context` parses simple key/value metadata and returns body text; `folder_context_summary` extracts the first non-heading paragraph, default 240 characters. That display summary is not the whole retained context. Authorship/initialization of later customized folder descriptions is unresolved; CLI init supplies some static scaffolds.

Distinct from [RT-OBJ-source-page](runtime.md#rt-obj-source-page): these select existing knowledge rather than instruct raw-to-page synthesis. They supply the navigation part of [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest), but are stored objects, not a duplicate route.

> The context file is a one- or two-paragraph description of what lives in that folder — use it to decide whether the folder is worth walking into for the current query, and which of its pages to read in full versus skip.
> --- `CLAUDE.md`

`AGENTS.md` additionally labels `hot.md`, per-project hot caches, `MEMORY.md`, `hints.md`, `SOUL.md` and `CRITICAL_FACTS.md`. CLI init creates placeholders with hot-cache, 200-line cap and Auto Dream claims. A bounded search in `llmwiki/`, `.claude/` and `.claude-plugin/` found scaffold strings, not the claimed hot refresh or Auto Dream consolidation implementation. Their accumulated lineage, automatic selector, cap enforcement and push channel remain unresolved. The agent schema's query steps explicitly read index/overview, not an automatic injection of every special file. This prevents counting those labels as established trace-fed consolidation or unsolicited context delivery; it does not negate ordinary file readability.

#### MEM-OBJ-quality-metadata
Label: Confidence and lifecycle metadata

SRC-1: `llmwiki/confidence.py`, `llmwiki/lifecycle.py`, `AGENTS.md`, `llmwiki/mcp/server.py`. Symbolic numbers, dates and categorical strings in page frontmatter, distinct from the natural-language claims they describe. Confidence functions combine source count/quality, age and inbound-link count; decay is a separate caller-applied multiplier. Lifecycle functions return permitted states or stale suggestions, not filesystem writes. Exact initial values and the authority that later changes each deployed page's fields are unresolved. MCP metadata consumers filter/display stored values; query scoring inspected here does not use these fields to veto a page.

> score = f1 * 0.3 + f2 * 0.3 + f3 * 0.2 + f4 * 0.2
>     return round(score, 2)
> --- `llmwiki/confidence.py`

> if confidence < 0.5:
>         return LifecycleState.STALE
> --- `llmwiki/lifecycle.py`

No counterpart in runtime; related [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) rewrites `status`, whereas lifecycle endpoints read `lifecycle`. Those keys must not be equated. Bounded caller search in `llmwiki/`, `.claude/`, `.claude-plugin/` and `AGENTS.md` found definitions of computation/stale helpers, not a production caller persisting their return values. This supports an unresolved update route, not a repository-wide absence of quality control.

#### MEM-OBJ-candidate-archive
Label: Archived candidates and reasons

SRC-1: `llmwiki/candidates.py`. Local Markdown under `wiki/archive/candidates/<timestamp>/` and optional adjacent `.reason.txt`. Archived page prose retains the candidate body; reason prose records caller-supplied rejection or merge explanation, timestamp and former path. The transition functions do not establish how the candidate was originally proposed or substantively reviewed. Distinct retained product of [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), not a duplicate transition route. Merge additionally puts the candidate body and former path into the target page. Discard does not retract already copied claims from other pages.

> if reason:
>         reason_file = dest.with_suffix(".reason.txt")
> --- `llmwiki/candidates.py`

Later generic Markdown scans can consume archived page content, but the inspected query/search scan does not read `.reason.txt`; thus rejection rationale does not necessarily accompany rejected claims. No dedicated later reason-reader or automatic rollback is established. Promotion can overwrite a target without archiving its old body; the candidate archive is not a universal undo store.

#### MEM-OBJ-ingest-queue
Label: Pending ingest queue

SRC-1: `llmwiki/ingest_queue.py`, `.claude-plugin/plugin.json`. Symbolic JSON path array in `.llmwiki-queue.json`; set-union/deduplication on enqueue, sorted persistence, full clear on dequeue. This is access/work metadata, not derived knowledge. No runtime record counterpart after comparison with [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts): the queue contains paths, not rendered prompts or UUID sentinels.

> items = _load(queue_file)
>     qf = queue_file or DEFAULT_QUEUE_FILE
>     if qf.is_file():
>         qf.write_text("[]", encoding="utf-8")
>     return items
> --- `llmwiki/ingest_queue.py`

The docstring attributes population to SessionStart and consumption to `/wiki-sync`, but the directly read slash procedure uses conversion counts/new files and pending-prompt scanning. Plugin registration points at the missing hook noted by boundary. Thus library retention/read/clear capabilities are implemented; an actual later queue consumer and successful-ingest acknowledgment protocol are not established. Clearing before caller processing would not itself guarantee ingestion. No complete memory read-back route is inferred from the API alone.

### Routes

#### MEM-RTE-wiki-maintenance
Label: Wiki update and reflection

SRC-1: `.claude/commands/wiki-update.md`, `.claude/commands/wiki-reflect.md`. Distinct maintenance triggers not declared by [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest): user-selected page/reason → foreground Read of page/index/sources → targeted edit/date/log; or optional focus → corpus/sample read → reflection/proposals → user approval before saving or editing. These are open requests without expected-answer oracle. Model proposes content; update instructions admit the requested local edit without per-sentence approval, while reflection explicitly reserves changes to the user. Host permissions enforce neither rule within this source boundary. Recovery is manual re-edit/source reconstruction; no transaction. Contradiction-preservation guidance and logs persist, but guaranteed correction of every copy is not established.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Requested update summary or 3–5 paragraph reflection and proposed actions.
- Later read-back: Updated page reaches normal queries; approved saved reflection enters `wiki/syntheses/`; operation log records the event.
- Delegated visibility: Foreground agent reads target and listed sources, or source/entity/concept corpus with representative sampling permitted above 50 pages.
- Selection predicate: Caller path/reason or focus hint; model chooses representative sample and substantive changes.
- Invalidation or expiry: Content/date changed in place; old conflicting claims should remain; reflection alone makes no page obsolete.
- Activation or effect: Instructions afford revision and later delivery, not observed uptake or improvement.
- Evidence limits: No host execution, sample-selection algorithm, actual edit or complete downstream retraction trace.

> **Don't edit pages during reflection.** Reflection is read-only. Any changes are proposed to the user, who approves before you touch the wiki.
> --- `.claude/commands/wiki-reflect.md`

#### MEM-RTE-self-learn
Label: Session lessons to method guidance

SRC-1: `.claude/skills/self-learn/SKILL.md`. Distinct from [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest): method-doc/steering/skill revision rather than ordinary wiki-page compilation. User completion/learning request or substantial-session trigger → foreground agent reads transcript, progress/tasks/framework/changelog → proposes lessons scored by generality and occurrence count → shows diff → human approval → applies documentation/steering/skill changes and logs/version bump. Guidance asks for failure explanations and repeated evidence. No expected-answer oracle or measured comparison is specified; occurrence count is a heuristic, not causal attribution. Humans can reject; no automatic rollback is specified, beyond editable retained text. Code changes are explicitly excluded by this skill.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Candidate lesson table, diff and approval request; after approval a changed-file report.
- Later read-back: Future self-learn is instructed to reread framework/changelog; new skills and steering afford later host guidance when loaded, whose deployment-specific loading is uninspected.
- Delegated visibility: Current foreground agent sees selected recent transcript and method artifacts, not a separate worker context.
- Selection predicate: Recency plus failed attempts, repeated loops, decisions and user hints; model scores generality/count; user admits proposed diff.
- Invalidation or expiry: Method text replaced/extended with version/changelog/progress record; low-confidence single occurrence should remain draft; no automatic expiry.
- Activation or effect: A trace-to-behavior-guidance path is requested and human-gated; exercised change, later dependence and capacity benefit remain unobserved.
- Evidence limits: Historical example outcomes are attributed source claims, not supplied traces; external personal framework copy is outside the frozen evidence.

> 5. **Show the diff to the user before applying anything.**
> --- `.claude/skills/self-learn/SKILL.md`

> 6. **Dogfood itself.** Self-learn should produce a session transcript that future self-learn passes can read.
> --- `.claude/skills/self-learn/SKILL.md`

This is trace-fed guidance revision as an affordance, not automatic trace learning. Reasons can survive in proposed rules and changelog, but the skill does not require a complete linked criticism record with blame and test outcomes. No exercised theory-builder or self-improvement claim is made.

#### MEM-RTE-quality-inspection
Label: Quality metadata and lint read-back

SRC-1: `llmwiki/mcp/server.py`, `llmwiki/lint/__init__.py`, `llmwiki/cli.py`, `llmwiki/lint/rules/content_freshness.py`, `llmwiki/lint/rules/summary_accuracy.py`, `llmwiki/lint/rules/contradiction_detection.py`. This grouped metadata/diagnostic route overlaps the MCP endpoints of [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), but also includes independent CLI lint dispatch. It therefore is not wholly part of that supplied record and is not identical to its question-query/read/sync surface. Both endpoint families reload stored pages and return reports without admitting content changes.

Caller requests health/state/range/entity/tag views; code reloads pages, filters stored fields and returns display summaries. CLI lint independently reloads pages and runs selected registry rules, returning issues, not revised pages. No content proposer, admission decision, expected-answer oracle or automatic correction is established by these read/report operations. Human/model downstream choices are outside their return path. Freshness warning does not persist a `stale` state. Rule names are not semantic validation evidence: summary accuracy checks emptiness; contradiction detection checks explicit sections if a callback is supplied. CLI does not pass a callback to `run_all`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP metadata lists/dashboard or CLI issue summary/JSON and optional error exit.
- Later read-back: These calls reload prior page fields/body; reports are not persisted by these handlers. Host lint doctrine separately offers saving a report with user permission.
- Delegated visibility: Host gets filtered field summaries or issues, not necessarily the page claim and all its evidence; CLI includes no model callback.
- Selection predicate: Requested numeric range/state/name/type/tag, registry/rule flags, dates and structural checks; most metadata lists cap displayed rows at 50, tag enumeration at 100.
- Invalidation or expiry: Files reread on request; no metadata mutation, expiry or query exclusion follows automatically from these diagnostics.
- Activation or effect: Diagnostic delivery wired; repair or changed reliance unobserved.
- Evidence limits: Not a correctness oracle or complete semantic audit; tests and actual human review not executed/observed.

> # Structural proxy: check summary field is non-empty when present.
> --- `llmwiki/lint/rules/summary_accuracy.py`

#### MEM-RTE-graph-query
Label: Retained graph metadata query

SRC-1: `llmwiki/graphify_bridge.py`, `llmwiki/cli.py`. No supplied counterpart after comparison with [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access) and [RT-RTE-reader-build](runtime.md#rt-rte-reader-build): this is CLI retrieval of a previously built graph, not full-page MCP retrieval or raw reader publication. Extractor derives symbolic nodes/links/project/date-proximity edges from wiki Markdown, including inferred edges; Graphify build exports `graphify-out/graph.json` and copies graph artifacts to `graph/`. The query reloads the former JSON with NetworkX, scores keyword label/ID matches plus degree/type bonuses, takes five seeds, traverses by requested depth, sorts by degree and returns at most 20 labels/path summaries. Consumer is the invoking person/agent; inference labels and graph connectivity are not validated page claims. External graph construction internals remain opaque, not source-admitted model or embedding state.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed metadata list, or missing-graph/no-matches message; no generated answer or source body.
- Later read-back: Retained graph JSON is reloaded on a later CLI query; no query-result persistence implemented here.
- Delegated visibility: Caller receives node labels, types, connection counts and optional file paths, not full Markdown, quotes or rejection reasons.
- Selection predicate: Question keywords in labels/IDs, connectivity/type bonuses, five seeds, depth-limited neighbors, 20-node cap; final `token_budget` slices characters, not tokens.
- Invalidation or expiry: Explicit rebuild refreshes graph; no query-time source freshness check is established.
- Activation or effect: Retained graph affects implemented selection; host behavior and answer benefit remain unobserved.
- Evidence limits: Graphify package implementation and deployed graph absent; built-in engine not audited here. Inferred proximity is not semantic entailment.

> return text[:token_budget] if len(text) > token_budget else text
> --- `llmwiki/graphify_bridge.py`

### Claims

#### MEM-CLM-archive-visibility
Label: Archive inactivity versus retrieval visibility

SRC-1: `llmwiki/lifecycle.py`, `llmwiki/candidates.py`, `llmwiki/mcp/server.py`, `llmwiki/lint/__init__.py`, `llmwiki/graphify_bridge.py`. Lifecycle documentation calls archived pages inactive; candidate doctrine presents discard as removal from the trusted area. This is not a universal exclusion at actual read consumers. Query/search recursively scan wiki Markdown without a candidate/archive/lifecycle predicate; lint loading skips README but does not implement its comment's archive skip; graph extraction also recursively scans Markdown. Thus rejected/archived text can remain retrievable. Reasons in adjacent text files need not accompany it. This qualifies downstream withdrawal, not the file-move behavior of [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission).

> archived  — Kept for history, inactive (manual transition only).
> --- `llmwiki/lifecycle.py`

> for page in wiki.rglob("*.md"):
> --- `llmwiki/mcp/server.py`

> # Skip README and archive
>         if p.name == "README.md":
>             continue
> --- `llmwiki/lint/__init__.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion)

Memory distinction: raw Markdown is a redacted/truncated rendering, not byte-identical native history; JSON mtime state is symbolic access metadata selecting future work, while quarantine records failures. Native session origins remain mixed user/assistant/tool material, not guaranteed factual truth. Raw retention by itself is not derived behavior-guidance learning. Synthesis and host ingestion supply the later transformation. SRC-1 `llmwiki/convert.py`, supported by the route's normalization passage. Exact adapter loss and all non-session provenance remain uninspected here.

#### On [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis)

Raw trace → selected prefix plus metadata/template → backend body → persisted source page → host/MCP later read is the implemented trace-derived memory chain. Backend text admission does not certify correct extraction or preserved reasoning; dummy/placeholder outputs challenge any inference from a synthesized counter. The 8,000-character cap is an input prefix selector; full raw files remain reachable separately. Mtime state can suppress rerender after only prompt/model changes. SRC-1 `llmwiki/synth/pipeline.py`, `llmwiki/synth/ollama.py`; runtime's write and backend-selection passages supply evidence.

#### On [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts)

The durable natural-language prompt is task/context retention for a later foreground invocation, not host-window compaction. Header/sentinel are symbolic coordination parts consumed by equality checks, distinct from prompt meaning. Cleanup after completion removes the prompt best effort; the source page remains the later knowledge consumer's input. Runtime's UUID passage supports association only. SRC-1 `llmwiki/synth/agent_delegate.py`, `.claude/commands/wiki-sync.md`. No target-launched subagent or isolated context frame is established.

#### On [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest)

Natural-language wiki pages feed both later knowledge writing and question answering. Query selection is agent judgment after index/overview, with folder-context prefilter specifically in Claude doctrine; the directly read agent-agnostic schema omits that folder step despite claiming identical workflows. No numerical token budget is enforced. Saved substantial answers have explicit user admission; routine ingest writes do not. SRC-1 `CLAUDE.md`, `AGENTS.md`. Runtime's save-answer passage supports the permission distinction. [MEM-OBJ-navigation](#mem-obj-navigation) describes the retained selection inputs.

#### On [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access)

SRC-1 `llmwiki/mcp/server.py`. Query is caller-pulled read-back: text scoring selects up to `max_pages` (default five), about 400-character snippets and 1,000-character overview prefix, with 1,500-character index fallback. Search optionally adds raw sessions and returns at most 200 matching lines, each sliced to 200 characters. Scan inputs use 4 MiB per file and 50 MiB aggregate, skipping oversize/unreadable files; this is not semantic rejection. Index/overview reads precede the capped corpus scan, so the scan budgets are not a bound on every read. Query has no archive/lifecycle exclusion, and its computed skipped-oversize count is not surfaced in query output; search does surface it. No result persistence or autonomous push is implemented by these handlers.

> _MCP_SCAN_PER_FILE_BYTES = 4 * 1024 * 1024   # 4 MiB / file
> _MCP_SCAN_AGGREGATE_BYTES = 50 * 1024 * 1024  # 50 MiB / call
> --- `llmwiki/mcp/server.py`

#### On [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)

SRC-1 `llmwiki/candidates.py`, `CLAUDE.md`, `AGENTS.md`. Candidate module prose claims ingest creates candidates first; the inspected host schemas directly create entity/concept pages. Therefore initial candidate routing is unresolved, not a universal gate. Caller action is separate from authorship and human review: CLI availability cannot authenticate the reviewer. Archived reason retention is optional for discard; merge supplies its own reason. Ordinary Markdown consumers need not see that reason. [MEM-OBJ-candidate-archive](#mem-obj-candidate-archive) records the retained products, while [MEM-CLM-archive-visibility](#mem-clm-archive-visibility) limits downstream inactivity.

## Write side

Acquisition is code-selected conversion, not per-record human approval; raw guard/force/quarantine behavior remains scoped as runtime states. Semantic host ingest is a separate model-authoring/admission path, backend synthesis accepts returned bodies, and pending completion checks identity rather than truth. User initiation does not imply approval of each claim. The prompt override is manually replaceable behavior guidance, not itself accumulated experience. Relevant records: [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion), [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest), [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis), [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion), [RT-OBJ-source-page](runtime.md#rt-obj-source-page).

Maintenance has three different admissions: targeted update affords direct foreground edits; reflection requires approval before changes/saving; self-learn requires showing a diff and approval before method edits. None is a code-enforced universal gate. Candidate promotion/merge/discard is another explicit caller-selected path, not mediation of all writes. Confidence helpers and quality tools must not be promoted from calculations/readouts to proven automatic metadata persistence. [MEM-RTE-wiki-maintenance](#mem-rte-wiki-maintenance), [MEM-RTE-self-learn](#mem-rte-self-learn), [MEM-OBJ-quality-metadata](#mem-obj-quality-metadata).

Source pages request source links, quotes, decisions and contradictions; these can retain reasons for a later agent that reads the relevant sections. MCP snippets and graph summaries can omit those reasons. Optional candidate rejection reasons are stored separately and not in the generic Markdown read chain. Backend force can replace prior bodies; pending completion does not preserve appended text despite its docstring; no universal rollback or cross-page retraction follows. [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-candidate-archive](#mem-obj-candidate-archive), [RT-CLM-append-preservation](runtime.md#rt-clm-append-preservation).

Log archival is a separate deterministic retention transformation, not learned prose consolidation. SRC-1 `llmwiki/synth/pipeline.py` checks a 50×1024-byte threshold before appending, keeps the first five lines, appends the rest to a yearly Markdown archive, then resets the active log. Recursive MCP scans can later select either file; no dedicated active-log-only relevance policy is established. This does not validate the unrelated Auto Dream scaffold claim.

> # Reset log to header only
>     log_path.write_text(header + "\n\n---\n", encoding="utf-8")
> --- `llmwiki/synth/pipeline.py`

## Read-back

Pull routes dominate inspected delivery: a user/agent asks a question, chooses a page, requests a quality view, invokes graph query or starts synthesis/ingest. Code or foreground judgment then selects retained content and returns it through Read, MCP text or stdout. Requests and selection must not be conflated: the question targets topics, graph matching targets labels/IDs, exact page reads target caller paths, and quality tools target metadata ranges/states. [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) identifies the actual foreground answer consumer and contextual force; delivery alone proves no activation.

For deferred synthesis, a later slash invocation explicitly scans pending prompts, so durable task instructions reach the foreground without a target-launched worker. A scheduled or SessionStart push route cannot be established from the missing hook plus queue docstring. Hot-cache/critical-fact names likewise establish no automatic injection. [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts), [MEM-OBJ-ingest-queue](#mem-obj-ingest-queue), [MEM-OBJ-navigation](#mem-obj-navigation).

Publication consumes rendered/raw material into regenerated HTML/search/export forms with optional metadata-only model prose. Supplied [RT-RTE-reader-build](runtime.md#rt-rte-reader-build) supports retention and later reader/export consumers, not proof of semantic reuse of every curated wiki page. MCP export is caller-directed text delivery of generated artifacts, not proof of their deployment or downstream agent use. External provider weights/opaque host windows remain separate from filesystem memory; no numerical parameter update is established by the supplied model adapters.

## Integration issues

- **Additional CLI read-back route:** [MEM-RTE-graph-query](#mem-rte-graph-query) extends runtime coverage beyond host/MCP/publication. Its misleading token-budget name means a character slice; labels/paths do not deliver page evidence. This is an addition, not a duplicate MCP route.
- **Archive withdrawal is endpoint-specific:** [MEM-CLM-archive-visibility](#mem-clm-archive-visibility) qualifies any inference from [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) that rejected knowledge cannot return. Archived text can be selected without its reason file. No source evidence establishes corpus-wide retraction.
- **Quality and candidate status differ:** [MEM-OBJ-quality-metadata](#mem-obj-quality-metadata) distinguishes `status` rewritten on promotion from `lifecycle` read by tools. Production persistence of confidence/auto-stale helper results is unresolved. This prevents assigning a universal automatic lifecycle gate.
- **Candidate initialization conflict remains:** module prose says candidates first; host ingest schemas write trusted directories directly. [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) already leaves proposer identity unresolved. The added inspection supports optionality, not a correction to its implemented transitions.
- **Unresolved automatic surfaces:** hot refresh, Auto Dream consolidation, queue hookup and SessionStart delivery lack established implementations in the inspected/search boundary. [MEM-OBJ-navigation](#mem-obj-navigation), [MEM-OBJ-ingest-queue](#mem-obj-ingest-queue). Do not infer those routes from scaffold prose; do not erase known direct file transformations because these routes are unresolved.
- **Schema divergence:** agent-agnostic query omits folder pre-read despite its identity claim. Annotation on [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest) scopes the runtime's folder-context statement to the Claude procedure rather than every host schema.
- **Possible overlap:** [MEM-RTE-quality-inspection](#mem-rte-quality-inspection) groups MCP metadata inspection, overlapping [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), with independent CLI lint under the same report-only control. It is not wholly contained by that supplied route. Other new objects are route products/inputs, not duplicate supplied objects. No further possible duplicate identified after comparison. Self-learn and maintenance extend the provisional baseline without establishing exercised learning or autonomous improvement.
- **Uninspected included variants:** native adapter losses, all repair scripts, built-in graph, vault write helpers/editor variants and full evaluator assertions remain bounded limits in the coverage table. Their available source is not absent. No private corpus or execution trace is supplied to resolve actual uptake, recovery, answer quality or benefit.

## Limitations and checks

Frozen identity was rechecked with Git; the checkout matched the boundary commit and was clean. Direct new evidence stays within SRC-1; no prior analyses or external sources were used. The runtime baseline remains provisional: this member adds graph and method-maintenance paths and qualifies schema-wide folder navigation. Strong labels were checked against counterexamples: direct ingest versus candidates-first doctrine, archive inactivity versus recursive retrieval, summary-accuracy naming versus structural proxy, token budget versus character slicing, and scaffolds versus automatic consolidation wiring.

Implementation/doctrine evidence supports these capacities and limits, not observed execution, semantic correctness, actual retained reasons at every delivery, capacity improvement or causal benefit. No target test results were inferred from test presence. Deterministic validation: `commonplace-run validate-output` passed the member content check. Invocation residue was not checked. This checks structure and quotation occurrence, not analytical correctness or job acceptance.
