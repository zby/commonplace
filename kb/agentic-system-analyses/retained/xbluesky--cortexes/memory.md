---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Cortexes memory: filtered Raw, human-admitted pages, derived retrieval indexes and ephemeral continuation batons."
run-id: AAS-2026-11-08-cortexes-af94078f2405-01
source-identity: https://github.com/xbluesky/cortexes
reviewed-boundary: "2b8e79f0099203e0453147b708346349952bb963"
---

# Cortexes memory report

## Boundary and evidence

The memory boundary includes the whole shipped vault loop: session capture, direct saves, distillation, broadcast, index maintenance, query, Raw navigation/queue/reclaim, evaluation and takeoff. It excludes host/provider internals, live private vaults and later revisions, as fixed in [boundary](boundary.md#boundary-and-evidence). No target program, test, example or provider call was executed. Implementation findings concern wired operations; procedures specify requested model/human behavior. Neither establishes actual activation or benefit.

The supplied runtime provides capture, foreground routing and maintenance progression. Direct SRC-1 reads added here cover `hooks/hooks.json`, `cortex-vec/src/cortex_vec/cli.py` dispatch, `store.py` initialization, summary generation, rebuild/upsert/delete and display conversion, `parser.py`, `config.py`, `bm25.py`, `graph.py`, `reclaim.py`, `eval/run.py`, `distill_queue.py`, `raw_view.py`, plan creation/identity/budget portions of `distill_plan.py`, map-card portions of `raw_map.py`, evolve/query/takeoff skills and distill's note/marker/index/log steps. These are implementation and doctrine/design layers under the existing SRC-1 registration, not new sources. Remaining capture filters, deck callbacks and span/seal details below rely on the supplied runtime's inspected findings and quotations rather than a second complete source audit.

| Entry point or memory operation | Source path (SRC-1) | Coverage and limit |
|---|---|---|
| SessionEnd and classifier | `hooks/hooks.json`, `hooks/scripts/session-end-record.sh`, `hooks/scripts/filter-transcript.py` | Manifest directly read; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [MEM-OBJ-raw](#mem-obj-raw). Individual command/TOML filter semantics not re-audited; prevents a complete preservation/privacy claim. |
| SessionStart and deck | `hooks/scripts/session-start-inject.sh`, `hooks/deck.tsx` | Supplied [RT-RTE-session-start](runtime.md#rt-rte-session-start); previews and topic metadata are not full memory bodies. Host compaction/permission internals unavailable. |
| Genesis/evolve and upsert/rebuild | `commands/genesis.md`, `skills/cortex-evolve/SKILL.md`, `cortex-vec/src/cortex_vec/store.py` | Genesis supplied; evolve/store directly read. [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), page and index objects below. Caller-selected upsert is an alternative to rebuild's directory scan. |
| Distill and broadcast | `skills/cortex-distill/SKILL.md`, `skills/cortex-broadcast/SKILL.md` | Distill output steps directly read; other progression supplied in [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit). No actual approved page supplied. |
| Map/span/plan, queue/raw-state | `cortex-vec/src/cortex_vec/raw_map.py`, `cortex-vec/src/cortex_vec/raw_span.py`, `cortex-vec/src/cortex_vec/distill_plan.py`, `cortex-vec/src/cortex_vec/distill_queue.py` | Mixed direct/supplied coverage; [MEM-OBJ-distill-plan](#mem-obj-distill-plan), [MEM-OBJ-distilled-marker](#mem-obj-distilled-marker). Ledger proves emission/accounting, not understanding. |
| Alternative raw-view API | `cortex-vec/src/cortex_vec/raw_view.py`, `cortex-vec/src/cortex_vec/cli.py` | Direct; [MEM-RTE-raw-view](#mem-rte-raw-view). Exposed operation, not the prescribed map-first consumer route. |
| Reclaim | `cortex-vec/src/cortex_vec/reclaim.py` | Direct; [MEM-RTE-reclaim-raw](#mem-rte-reclaim-raw). Filesystem deletion is real capacity, not semantic curation. |
| Hybrid, lexical, graph and full-file reads | `skills/cortex-query/SKILL.md`, `cortex-vec/src/cortex_vec/store.py`, `cortex-vec/src/cortex_vec/bm25.py`, `cortex-vec/src/cortex_vec/graph.py` | Direct plus supplied fusion/rerank trace in [RT-RTE-vault-search](runtime.md#rt-rte-vault-search). Synonym expansion internals not separately inspected; query token-expansion provenance remains bounded to shipped configuration, not learned synonyms. |
| Index withdrawal | `cortex-vec/src/cortex_vec/store.py` | Direct; [MEM-RTE-index-delete](#mem-rte-index-delete). Index deletion does not remove the page or Git history. |
| Takeoff create/resume/done | `skills/cortex-takeoff/SKILL.md`, `hooks/scripts/takeoff.sh` | Skill direct, helper supplied; [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff), [MEM-OBJ-takeoff](#mem-obj-takeoff). |
| Eval run/propose | `cortex-vec/src/cortex_vec/eval/run.py` | Direct; [MEM-RTE-retrieval-eval](#mem-rte-retrieval-eval). Adapter/metric internals not independently audited; no measured retrieval quality inferred. |

## Core ideas

1. Raw is already a lossy, filtered derivative of a host transcript, not the original trace. Durable knowledge is a second transformation: the foreground model proposes pages or edits and a human is prescribed to decide distill/broadcast content. Direct evolve is a separate admission path with no final draft-approval requirement. The difference matters more than the shared Markdown substrate ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), [RT-RTE-direct-save](runtime.md#rt-rte-direct-save)).
2. Indexes change access, not the canonical page. Chroma holds body and generated-summary entries plus numerical embeddings; BM25 holds tokens and display metadata, not a raw body copy; graph topology is rebuilt from current wikilinks and cached in process. Display `summary` is a short extraction from the winning stored text, not necessarily the generated bilingual summary. See [MEM-OBJ-vectorstore](#mem-obj-vectorstore), [MEM-OBJ-bm25](#mem-obj-bm25), [MEM-OBJ-wikilink-graph](#mem-obj-wikilink-graph).
3. Context control mostly avoids loading material rather than evicting it. Map/span exposes bounded source fragments; query returns candidates before full-page reading; takeoff replaces the next session's input with a curated baton. None of these removes earlier foreground turns. Separate classifier/summary/rerank calls keep most foreground context out and return only verdicts or derived outputs; provider internals and host compaction remain outside inspection ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff)).
4. Retained metadata can have stricter operational authority than prose. A position-anchored marker controls future queues; a plan hash can reject loading. By contrast, a retrieved note influences answers through model interpretation, not an executable truth rule. No admission or retrieval score establishes that retained claims are correct ([MEM-OBJ-distilled-marker](#mem-obj-distilled-marker), [MEM-OBJ-distill-plan](#mem-obj-distill-plan), [MEM-BAP-page-context](#mem-bap-page-context)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Filtered Raw session record

SRC-1, `hooks/scripts/session-end-record.sh`, `hooks/scripts/filter-transcript.py`. No object counterpart is declared by runtime; this is the retained output of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), whose quotations support the transformation and fallbacks. Storage: dated Markdown files in the vault's Raw tree, optionally Git/remote copies. Natural-language conversation/tool output is derived from host JSONL; frontmatter/audit/processed markers are symbolic metadata with different consumers. Source origin includes user/model turns and tool results; Task output bypasses generic filtering, while other selected residue can be sampled/deduplicated after classifier judgment. Thus neither pristine trace nor pure human knowledge describes Raw. A terminal failure stub may retain only a pointer/diagnostic instead of content. The source transcript is a separate host artifact, not guaranteed indefinitely available through the vault.

Later consumers are foreground distill/broadcast, explicit archive grep and reclaim. Capture admission is automatic code/model selection, with no per-record human approval. The classifier verdict controls retention, not truth. Raw can carry decision rationale when preserved, but source filtering can remove material; no universal rationale-preservation guarantee follows. Raw alone is retained trace, not demonstrated future capacity improvement.

#### MEM-OBJ-notes-projects
Label: Canonical Notes and Projects pages

SRC-1, `skills/cortex-evolve/SKILL.md`, `skills/cortex-distill/SKILL.md`. Distinct retained product of [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), [RT-RTE-distill-review](runtime.md#rt-rte-distill-review) and [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit); no runtime object counterpart. Storage: vault Markdown, Git history and optional remote copies. Natural-language content, wikilinks and frontmatter coexist: readers interpret prose, parsers consume tags/repos/title, graph code resolves links. Initialization of particular private pages is unknown; supported subsequent transformations include new authored saves, Raw-derived drafts and exact-section edits/contradiction flags. Evolve uses `source: cortex`; the distill writing steps inspected here do not require a structured source-range/reason record on every page. Raw markers/log targets supply partial lineage in the other direction. Do not infer a universal bidirectional provenance graph.

> source: cortex
> --- `skills/cortex-evolve/SKILL.md`

> 4. Present draft to user for confirmation
> 5. Write to vault using Obsidian Flavored Markdown (wikilinks, frontmatter, callouts)
> --- `skills/cortex-distill/SKILL.md`

Admission differs by route: evolve is user-initiated model authorship without mandatory final draft confirmation; distill prescribes verdict and draft confirmation; broadcast prescribes target/change decisions. Physical host Write/Edit is not proof of approval. Later readers include query's foreground host, maintenance proposals, indexers and evaluation. Knowledge content is interpretive guidance to the host, not privileged executable instruction or verified fact.

#### MEM-OBJ-vectorstore
Label: Chroma body summary and embedding entries

SRC-1, `cortex-vec/src/cortex_vec/store.py`, `cortex-vec/src/cortex_vec/config.py`. No runtime object counterpart; derived index in [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), consumed by [RT-RTE-vault-search](runtime.md#rt-rte-vault-search). Persistent Chroma collection `cortex` under `~/.cortex/vectorstore`. Separate operative parts: natural-language title/body and generated summary documents; symbolic IDs, source paths and repo/type/category metadata; numerical embeddings used by cosine retrieval. Numerical representations are not locally trained model weights. Embedding provenance and model fixity are bounded by [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model); provider parameter storage stays opaque.

Rebuild reads Notes/Projects except `_archive`; upsert takes a caller path and has only an existence check here, so the rebuild scan is not a universal type restriction. Each repo membership produces body and summary entries. Summary generation sees title/tags and only 3000 body characters, requests at most 400 completion tokens, and falls back to title/tags; software admits the returned text without a content-approval gate. Model authorship is distinct from caller identity. No summary rationale, criticism record or validation of fidelity is retained by this operation.

> "content": _SUMMARY_PROMPT.format(title=title, tags=tags, body=body[:3000]),
> --- `cortex-vec/src/cortex_vec/store.py`

> summary_id = f"{doc_id}::summary"
> summary_metadata = {**metadata, "entry_type": "summary"}
> --- `cortex-vec/src/cortex_vec/store.py:355-356`

Read-back returns a deduplicated page candidate using the best body/summary cosine, with a display extraction from that matched document. Full page content is delivered only by the later file read. IDs/metadata control routing/rank; generated summary prose supports relevance judgment, not an answer oracle. Upsert deletes stale variants before rebuilding and BM25 follows later; recovery is explicit rebuild/upsert, not an atomic canonical/index transaction.

#### MEM-OBJ-bm25
Label: Persistent lexical token records

SRC-1, `cortex-vec/src/cortex_vec/bm25.py`, `cortex-vec/src/cortex_vec/store.py`, `cortex-vec/src/cortex_vec/parser.py`. Distinct index part from Chroma; overlaps [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) as its lexical input, not a duplicate route. Storage: `~/.cortex/bm25/index.pkl`. Symbolic token lists and metadata derive from parsed title/body; a natural-language display summary is the first nonempty nonheading line, stripped of callout prefix and capped at 120 characters. The bilingual model summary is not its input. Raw body is not stored in the pickle record. BM25Okapi is reconstructed on load, rather than retained as a model trained by session feedback.

> rec = {f: doc.get(f) for f in _META_FIELDS}
> rec["repos"] = list(doc.get("repos") or [])
> rec["tokens"] = tokenize(text)
> --- `cortex-vec/src/cortex_vec/bm25.py`

> with open(self._file, "wb") as f:
>             pickle.dump(self.docs, f)
> --- `cortex-vec/src/cortex_vec/bm25.py`

Admission is automatic deterministic parsing/tokenization on rebuild/upsert, including BM25-only rebuild without embedding calls. Later search ranks token overlap and applies repo/type/category predicates before returning display fields. Full text remains reloadable from canonical pages. No human approves each token or summary extraction; edits require refresh. Tokenizer/synonym details are not separately inspected, limiting claims about exact multilingual/token expansion behavior, not the demonstrated storage/consumer chain.

#### MEM-OBJ-wikilink-graph
Label: Cached wikilink adjacency and display metadata

SRC-1, `cortex-vec/src/cortex_vec/graph.py`. Distinct selector object within [RT-RTE-vault-search](runtime.md#rt-rte-vault-search). Symbolic adjacency sets/title lookup and display metadata live in a process-local `_cache` keyed by vault path; no graph persistence file is written by this module. Retained source is canonical page wikilinks, which may be model-authored or human-edited: the source's phrase “human-curated graph” does not establish human-only link authorship. Scan uses Notes/Projects excluding `_archive`; title and stem resolve links, unresolved targets are skipped, and resolved edges are bidirectional. Duplicate titles use the first mapping encountered. Graph display summaries use the same first-line extraction, not generated summary text.

> if dest and dest != rel:
>                 adjacency[rel].add(dest)
>                 adjacency.setdefault(dest, set()).add(rel)  # links are bidirectional
> --- `cortex-vec/src/cortex_vec/graph.py`

Consumer: optional graph retrieval stream expands top-hit seeds by configured hops, applies returned-node filtering, orders equal-distance neighbors by stable digest and caps count. The filter constrains returned nodes, not intermediate traversal at multiple hops. Topology controls candidate discovery, not claim warrant. Cache returns on repeat vault-key access without freshness comparison in this module; no live cache-invalidation guarantee follows. This is a read-derived access structure, not a trace-fed semantic rewrite.

#### MEM-OBJ-distilled-marker
Label: Processed markers and maintenance log

SRC-1, `cortex-vec/src/cortex_vec/distill_queue.py`, `skills/cortex-distill/SKILL.md`, `skills/cortex-evolve/SKILL.md`. No runtime object counterpart; control/output state of [RT-RTE-distill-review](runtime.md#rt-rte-distill-review) and [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit). Distinguish two retained parts. Symbolic `<!-- distilled: ... -->` lines in Raw govern eligibility. Markdown `log.md` records outcome, target, repo and optional dedup top hit, but is not the queue parser's input. It does not itself contain the mandatory full reasoning or source evidence ranges for every decision. Storage is vault files with prescribed Git commits.

Queue code accepts the first pre-conversation whole-line marker, else a final nonempty marker; quoted markers inside conversation do not count. Unknown but present marker is still distilled. `new` and `pending-merge` without resolution remain broadcast-eligible; skips and no-insight leave Raw retained but remove it from distill admission. Admission is model-written following prescribed human decisions, except the automatic meta-session skip in [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). Markers are operational claims about completion, not proof of review or truth.

> def is_distilled(state: RawState) -> bool:
>     return state.outcome != "undistilled"
> --- `cortex-vec/src/cortex_vec/distill_queue.py`

> return state.outcome in ("new", "pending-merge") and not state.broadcast_resolved
> --- `cortex-vec/src/cortex_vec/distill_queue.py`

#### MEM-OBJ-distill-plan
Label: Source-bound navigation ledger

SRC-1, `cortex-vec/src/cortex_vec/distill_plan.py`, `cortex-vec/src/cortex_vec/config.py`, `cortex-vec/src/cortex_vec/raw_map.py`. Distinct state object used by [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), not a duplicate route. Symbolic JSON under `$XDG_CACHE_HOME/cortex/distill-plans/` or `~/.cache/cortex/distill-plans/`, source-hash file plus active pointer. It records file/source/parser identities, semantic/ambiguous/reviewed intervals, evidence labels/ranges, map cursor, budgets and expected outcome. Source text stays in Raw; the ledger is access/coverage metadata, not an independently authored knowledge summary. Automatic API accounting admits entries; callers supply evidence labels, with reviewed-range checks supplied in runtime. Human approval is not attested by the JSON.

> "session_used_chars": 0,
>         "map_next_index": 0,
>         "span_count": len(spans),
>         "semantic": semantic,
>         "ambiguous": ambiguous,
>         "reviewed": [],
>         "evidence": [],
> --- `cortex-vec/src/cortex_vec/distill_plan.py`

Default map budgets are 12000 page and 100000 session characters; output accounting reserves control space. Map previews are 160 characters, lexical anchors at most eight; span selection reloads original text. Source drift rejects loading; seal blocks pages; complete removes state, so retained evidence ranges are not guaranteed as durable page lineage after completion. A reset claims a new session through a flag, not host attestation. Persistence supports partial review across sessions but does not preserve a full model/human reasoning history. The helper does not evict pages already delivered to the host.

#### MEM-OBJ-takeoff
Label: Topic continuation baton

SRC-1, `skills/cortex-takeoff/SKILL.md`. No runtime object counterpart; the retained product of [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff), with authority already declared by [RT-BAP-baton-context](runtime.md#rt-bap-baton-context). Natural-language free-form curation plus symbolic repo/topic/workdir/time/summary frontmatter lives in `<vault>/.takeoff/<repo-slug>/<topic>.md`. The foreground model chooses useful current-session goal/progress/next-step/gotcha material; original input is a mixed user/model/tool working trace. User requests handoff or accepts reminder, but no separate content approval is prescribed. This is trace-fed derived memory, not merely retained raw logs or parameter learning.

> Content is free-form — write
>    whatever genuinely lets a fresh session continue without re-deriving
>    context.
> --- `skills/cortex-takeoff/SKILL.md`

The next session first receives only a summary/path menu, then chosen full-body adoption. Reasons may be included as gotchas/open questions but no fixed schema requires their retention or verification. One active baton per topic is overwritten; resume retains it; explicit done trashes it, with 30-day pruning. The policy excludes indexing, distillation, commits and log entries. The ignored-path preflight is not universal Write enforcement, as runtime notes. This creates a short-lived continuation channel separate from the durable knowledge index.

### Routes

#### MEM-RTE-raw-view
Label: Alternative deterministic Raw projection

SRC-1, `cortex-vec/src/cortex_vec/raw_view.py`, `cortex-vec/src/cortex_vec/cli.py`. Distinct exposed API from the map/span procedure in [RT-RTE-distill-review](runtime.md#rt-rte-distill-review). Caller passes file and optional budget/level. Code chooses L0 verbatim if small; L1 preserves prose and selected Agent/Task outputs, elides other tool bodies to line anchors; L2 removes those tool bodies too; L3 keeps prose heads/special insight/table lines and collapses long tool runs; L3* hard-clips with a recovery pointer. Default view budget is 150000 characters. An explicit level bypasses automatic budget choice. No model semantic judgment or per-output human approval occurs. Raw on disk is unchanged; printed projection is not a durable summary checkpoint.

- Immediate return: Printed projected text or size statistics.
- Later read-back: Afforded reading of accumulated Raw through the exposed CLI; no particular later foreground use of this alternative API is established beyond its intended distill-consumption role.
- Delegated visibility: inapplicable — local projection runs no model or worker.
- Selection predicate: Caller file/level/budget and deterministic block kind, tool-name keep set, prose-head and special-line rules.
- Invalidation or expiry: Projection is recomputed on each call; line anchors depend on the underlying file remaining unchanged.
- Activation or effect: Controls emitted working context only; source remains reachable for exact span reload.
- Evidence limits: No execution or automatic host-window eviction; this API does not provide plan ledger enforcement merely by sharing Raw input.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> if lvl:
>         out = text if lvl == "L0" else render(parse_blocks(text), lvl, cfg)
>     else:
>         _, out = choose_level(text, cfg)
> --- `cortex-vec/src/cortex_vec/raw_view.py`

#### MEM-RTE-reclaim-raw
Label: Superseded Raw removal

SRC-1, `cortex-vec/src/cortex_vec/reclaim.py`. Material cleanup part of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), also directly exposed by CLI. Unlike capture it selects/deletes existing Raw rather than producing a new record.
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Code scans the undistilled queue; compares nonempty conversation-body lines from first turn onward; admits removal only for a prefix with matching repo. A `keep` survivor limits the scan; otherwise later path breaks equal-body ties. Divergent filter output fails prefix matching and is kept. Apply prefers `git rm`, falling back to unlink; no per-file human content approval is required inside apply. Decisions are symbolic redundancy checks, not an answer oracle or model criticism. Rejection includes cross-repo prefix pairs and empty bodies; Git history affords recovery only for tracked content.

- Immediate return: Candidate or removed path list; cross-repo refusals on stderr.
- Later read-back: Remaining Raw supplies distill/archive; removed candidates no longer consume queue/context budget. Tracked deletions may be recoverable through Git, not a dedicated reload command here.
- Delegated visibility: inapplicable — no model is called.
- Selection predicate: Undistilled candidate, nonempty body prefix, matching repo, survivor/tie rule.
- Invalidation or expiry: Apply removes selected files; nonmatching candidates remain. No independent age TTL.
- Activation or effect: Changes durable archive/queue membership, not semantic claims in surviving pages.
- Evidence limits: No removal run supplied; failed unlink stays; preservation proof is restricted to compared body lines, not all file metadata.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if cand_repo != keep_repo:
>                 result.refused.append(
>                     CrossRepoPair(p, keep_path, cand_repo, keep_repo)
>                 )
>                 continue
>             result.superseded.append(p)
> --- `cortex-vec/src/cortex_vec/reclaim.py`

#### MEM-RTE-index-delete
Label: Explicit derived-index withdrawal

SRC-1, `cortex-vec/src/cortex_vec/store.py`. Distinct from upsert/rebuild in [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), and from expiration described by [RT-RTE-vault-search](runtime.md#rt-rte-vault-search). Caller selects path; software deletes all matching Chroma variants, then lexical record if reached. No per-content human review, semantic criticism or expected-answer oracle. It changes access machinery, not canonical content. A relevant alternative branch prevents a universal synchronized-deletion claim: if no stale Chroma IDs exist, it returns before BM25 deletion. A BM25-only or divergent lexical record can therefore remain searchable.

- Immediate return: Deleted vector-entry count or idempotent no-vector-entry result.
- Later read-back: Future vector search loses deleted entries; BM25 search loses the path only when execution reaches its deletion; grep/full-file reads remain possible.
- Delegated visibility: inapplicable — no delegated consumer is created.
- Selection predicate: Caller path equality or `path::` prefix for Chroma; exact base path for BM25.
- Invalidation or expiry: Explicit deletion; later upsert/rebuild can recreate entries from the still-present file.
- Activation or effect: Derived selector membership changes; neither page withdrawal nor Git erasure follows.
- Evidence limits: Source branch, not observed stale-result incident; caller identity and actual human control unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not stale:
>         # Idempotent: the goal state (not indexed) already holds.
>         print(f"cortex-vec: {rel_path} not indexed; nothing to delete",
>               file=sys.stderr)
>         _emit(args, [], {"deleted": 0, "path": rel_path})
>         return
> --- `cortex-vec/src/cortex_vec/store.py`

#### MEM-RTE-retrieval-eval
Label: Offline retrieval evaluation and query proposals

SRC-1, `cortex-vec/src/cortex_vec/eval/run.py`. No supplied route counterpart: [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) answers foreground searches; this route evaluates adapters and writes a scorecard/query-set artifact. Caller starts run or propose. Code loads Notes/Projects excluding `_archive`, parses them to lexical document shape and initializes named adapters. Run compares ranked document IDs to query-set `gold`, records timing and scores, aggregates and optionally writes Markdown. Gold paths are a reference-answer oracle for retrieval membership, not note factual correctness; missing paths warn. Propose uses the summary-role model to draft queries from title/display summary, pre-fills the source page as gold and writes JSONL marked for user review. Human confirmation is requested by documentation; no interactive approval gate precedes file output. Operating mode: bounded supplied query set, not autonomous online improvement. No automatic admission of scorecard results into retrieval configuration is established by this runner.

- Immediate return: Per-query rows and scorecard, or proposed query JSONL with review warning.
- Later read-back: Runner loads saved query/gold files on a later evaluation invocation; scorecard is an external inspection artifact, not a wired foreground memory input here.
- Delegated visibility: Proposal provider receives each page title/display summary, not full sessions; adapters receive corpus documents through their interfaces.
- Selection predicate: Supplied query file, adapter names and k; proposer scans canonical corpus and skips failed model calls.
- Invalidation or expiry: Output path can be overwritten; missing gold warns rather than rewriting it. No automatic freshness validation established here.
- Activation or effect: Produces evaluation evidence/proposals, not automatic page or parameter revision.
- Evidence limits: Adapter/metric internals and actual results not inspected; no benchmark quality, causal gain or exercised learning inferred.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> sc = score.score_query(ranked, set(q["gold"]), k)
> --- `cortex-vec/src/cortex_vec/eval/run.py`

> "note": "AUTO-PROPOSED — review query + gold before use",
> --- `cortex-vec/src/cortex_vec/eval/run.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-page-context
Label: Retained page to foreground reasoning

SRC-1, `skills/cortex-query/SKILL.md`. Distinct from [RT-BAP-plugin-guidance](runtime.md#rt-bap-plugin-guidance): that path supplies static method text; this path supplies accumulated vault content. Consumer is the later foreground Claude Code model. Channel: query hit metadata/display summaries, lexical excerpts and selected full-page Read. Force: natural-language information used through model interpretation; symbolic metadata determines discovery but does not certify truth. Horizon: later sessions until page/index replacement or removal, subject to stale indexes. Human choice governs which full page to load when multiple matches, not every candidate's appearance. [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) establishes wiring and the absence of supplied activation evidence.

> - If multiple matches, list them and ask which one to read
> - If user wants details → read the full file
> --- `skills/cortex-query/SKILL.md`

## Annotations

#### On [RT-RTE-session-start](runtime.md#rt-rte-session-start)

Memory delivery is metadata-first: top-level topic names and baton previews, not an automatic full-vault injection. The automatic selector is repo/topic availability at lifecycle start, not a query-conditioned page selector. This push can route a later search or baton adoption, but alone does not establish full retained-content read-back. The deck substitutes a menu for part of hook context; it does not summarize or evict the ongoing conversation.

#### On [RT-RTE-distill-review](runtime.md#rt-rte-distill-review)

The trace-to-derived chain is [MEM-OBJ-raw](#mem-obj-raw) → selected map/span text → human-confirmed draft → [MEM-OBJ-notes-projects](#mem-obj-notes-projects) → deterministic/model-generated indexes → later query. This affords trace-fed knowledge curation, not demonstrated improvement. Specific decision rationales are candidate signals in the supplied route, but [MEM-OBJ-distilled-marker](#mem-obj-distilled-marker) and the inspected page template do not guarantee retaining the reasons for every admission/rejection. [MEM-OBJ-distill-plan](#mem-obj-distill-plan) keeps evidence coordinates during review; completion removes that ledger. Later query reads note content, not a required criticism/admission-rationale record. Pending-merge is deliberately not a new derived page; skips retain Raw and control metadata only.

#### On [RT-RTE-direct-save](runtime.md#rt-rte-direct-save)

The direct save path prevents equating all vault knowledge with distilled traces. A user can supply content; the model selects placement and authors it; the CLI automatically generates access structures. These are three different agency/admission roles. `_index.md` is a separately maintained natural-language/page-link directory; `log.md` is operational history; neither is Chroma or BM25's primary body input. Summary generation affects future candidate selection even without model-weight changes. Its input is a page prefix, not a whole original trace. If the page is trace-derived, the index is a second-order trace derivative, not new evidence of truth.

#### On [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff)

The baton is the alternative checkpoint form to durable Notes/Projects. It is curated from current work for a next session, not merely the last turns verbatim; all foreground context not selected by the author stays out of the next session's initial baton. Loading supplies the whole selected note, while topic summaries only select it. No numeric body budget is prescribed. This resembles passing a compact return value to a fresh frame, but no Cortexes-owned pop/eviction of the old context occurs. Host-level context retention/compaction remains opaque.

## Write side

Acquisition has separate gates. Capture automatically accepts eligible host transcripts and filters/classifies them, with fail-preserving branches; humans do not approve each Raw. Evolve is explicitly initiated by a user but has model-selected content/placement and no final-draft gate. Distill prescribes separate human verdict and new-draft confirmation. Broadcast prescribes page/change approval; earlier committed pages survive abort. These software versus human controls are policies or code checks at their actual enforcement point, not interchangeable evidence of curated truth ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit)).

Automatic subsequent transformations are distinct from unknown initial content authorship. Chroma generation, BM25 tokenization and graph construction accept canonical page contents without semantic review. Bilingual summary generation drops everything after the input prefix and does not retain its reasoning. The display extraction can further narrow that output. Batons use foreground curation and carry continuation instructions; their free-form schema can retain rationale, but does not ensure it. No retained-parametric update is established: the provider models are separately described by runtime, while retained numerical embeddings are document representations ([MEM-OBJ-vectorstore](#mem-obj-vectorstore), [MEM-OBJ-bm25](#mem-obj-bm25), [MEM-OBJ-wikilink-graph](#mem-obj-wikilink-graph), [MEM-OBJ-takeoff](#mem-obj-takeoff)).

Rejection and withdrawal have different retained effects. A no-insight/skip marker suppresses future review without deleting Raw; pending-merge delays page creation but remains broadcast-eligible; reclaim removes redundant undistilled bodies; index delete only changes derived access and can miss BM25 in its early-return branch. File deletion, index deletion, Git recovery and baton trashing are not one universal forgetting operation. Rebuild can recreate withdrawn index entries from extant pages. Nothing inspected establishes erasure from provider logs, host transcripts or all Git history ([MEM-OBJ-distilled-marker](#mem-obj-distilled-marker), [MEM-RTE-reclaim-raw](#mem-rte-reclaim-raw), [MEM-RTE-index-delete](#mem-rte-index-delete), [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff)).

## Read-back

The ordinary retained-content route is a foreground request or prior-context signal → query-conditioned search → ranked metadata → user-selected full page. Repo filters scope Projects but retain cross-repo Notes; they do not establish trust or tenant isolation. Raw is a separately requested archive/read-for-maintenance surface, not in rebuild's normal semantic corpus. Explicit upsert has a broader caller-selected path surface, so normal rebuild coverage is not a universal admission restriction ([RT-RTE-vault-search](runtime.md#rt-rte-vault-search), [MEM-OBJ-vectorstore](#mem-obj-vectorstore)).

Map/span pulls source ranges according to foreground selection, with page/session character budgets and source identity checks. It keeps bulk Raw out, but emitted fragments accumulate in the current host window. Alternative raw-view is a deterministic projection with reload pointers, not a guaranteed durable model summary. Query similarly avoids loading full bodies until selection. A store capability with an arbitrary caller is not alone an exercised later-consumer route; raw-view's status is therefore afforded rather than observed ([RT-RTE-distill-review](runtime.md#rt-rte-distill-review), [MEM-RTE-raw-view](#mem-rte-raw-view)).

Automatic SessionStart supply selects topic metadata/baton previews on lifecycle and repo state, without a semantic request or page-body budget. Actual baton content arrives through explicit resume, and ordinary notes through query/Read. Nested capture classification excludes almost all foreground conversation, supplying at most a residue prefix and receiving only a verdict. Summary calls see bounded page content; rerank sees query and candidate title/summary, not the full page or foreground trace. These separate calls approximate isolated frames whose outputs escape, but provider contexts are opaque and no host-window reference/liveness semantics follow. A new foreground session plus baton is a prescribed continuation boundary, not an automatic Cortexes compaction mechanism ([RT-RTE-session-start](runtime.md#rt-rte-session-start), [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-vault-search](runtime.md#rt-rte-vault-search), [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff)).

## Integration issues

- Supplemental withdrawal finding: [MEM-RTE-index-delete](#mem-rte-index-delete) qualifies any reading of [RT-RTE-vault-search](runtime.md#rt-rte-vault-search)'s “index changes through ... delete” as synchronized vector/lexical removal. SRC-1 `cortex-vec/src/cortex_vec/store.py` returns before BM25 deletion when no vector IDs exist. This is a branch-specific consistency limit, not an observed incident or correction to the literal claim that delete changes indexes.
- Supplemental path-scope limit: [MEM-OBJ-vectorstore](#mem-obj-vectorstore) distinguishes rebuild's Notes/Projects scan from caller-path upsert. SRC-1 `cortex-vec/src/cortex_vec/store.py` does not impose the same scan restriction on upsert. Do not turn the usual corpus boundary into a universal prevention guarantee.
- [MEM-RTE-reclaim-raw](#mem-rte-reclaim-raw) is a material cleanup part of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), not a competing capture definition. The explicit CLI route shares that implementation. Other new objects have no supplied object counterparts; new authority path differs from static plugin guidance; raw-view and evaluation have no supplied route counterparts. No record requiring supersession or possible duplicate remains after this comparison.
- Unknown/private page provenance, actual retained rationale, human adherence and activation remain uninspected in [MEM-OBJ-notes-projects](#mem-obj-notes-projects), [MEM-OBJ-takeoff](#mem-obj-takeoff) and [MEM-BAP-page-context](#mem-bap-page-context). Available templates establish possibilities and requirements, not private content or successful later dependence. Reconciliation must not infer improvement, factual warrant or theory revision from generic page editing.
- No actual benchmark results or reviewed query set were supplied for [MEM-RTE-retrieval-eval](#mem-rte-retrieval-eval); proposed gold is page-derived and requires review. This prevents retrieval-quality and causal-learning claims. No other correction to supplied facts is proposed.

## Limitations and checks

HEAD was checked directly and equals `2b8e79f0099203e0453147b708346349952bb963`; identity is the registered SRC-1 repository. Analysis followed the supplied memory job, member type and record contract, not a prior analysis or authoring skill. Source reads and searches were bounded; an initial search for `raw_reclaim.py` failed because the actual module is `reclaim.py`, which was subsequently read. No missing module was inferred from that search failure.

This is source-grounded mechanism analysis, not an execution audit. Capture subfilter completeness, tokenizer/synonym internals, evaluation metric/adapter details, real concurrency and host/provider behavior were not independently established. Explicit limits above prevent universal preservation, freshness, privacy, context-eviction, human-admission, performance or benefit claims. The positive source-supported counterexamples retained here include lossy Raw, summary-prefix input, alternate file reads, upsert's broader path interface, graph cache reuse, explicit-level projection bypass, and the index-delete early return.

Validation: passed the assigned role-aware commonplace-validate content check; this checks structure, references and quotation occurrence, not semantic acceptance or successful operation.
