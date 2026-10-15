---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Link memory analysis: editable Markdown, proposal provenance, lifecycle-dependent recall, automatic context supply and alternate wiki read paths."
run-id: AAS-2026-10-14-link-595f6f9cba36-01
source-identity: "https://github.com/gowtham0992/link"
reviewed-boundary: cc92f3632121b04063b24eaaf3a8c5429eaf2b57
---

# Link memory report

## Boundary and evidence

Link retains personal/project memories, source-backed wiki knowledge, proposal captures and short-lived handoffs for external agents and human readers. This report uses SRC-1 at the frozen revision in [boundary](boundary.md), whose source register remains authoritative. HEAD was rechecked as `cc92f3632121b04063b24eaaf3a8c5429eaf2b57`. Implementation inspection establishes wiring, not successful installed operation, actual approval, changed answers or benefit. No target code, tests, fixtures, benchmark or model provider was executed.

Memory scope includes the runtime's CLI, MCP, HTTP and LinkBar paths; Markdown/file adoption; automatic hooks; proposal mining and cleanup; explicit lifecycle mutations; wiki ingestion and seeding; derived graph/search/vector caches; usage accounting; synchronization, recovery and publication. External hosts decide whether tool results enter a model window and whether instructions are obeyed. Host compaction, sub-agent isolation, provider weights and the separately reported QA benchmark workspace remain outside the supplied evidence. These exclusions prevent an end-to-end memory effectiveness or host-context-management conclusion, not an account of Link's own packet construction.

The table distinguishes direct reads in this job from supplied runtime findings. All paths are SRC-1 commit-relative anchors. Rows grouping parts do not assert that their admission checks are equivalent.

| Entry point or operation | Source path | Coverage and evidence basis | Limit / conclusion prevented |
|---|---|---|---|
| Remember, update, review, archive, restore, forget, visibility | `mcp_package/link_core/memory.py`; `mcp_package/link_mcp/server.py`; `link.py` | Direct writer, mutation, reload, selector, explanation and MCP dispatch reads; [MEM-OBJ-memory-claim](#mem-obj-memory-claim), [MEM-OBJ-memory-controls](#mem-obj-memory-controls), [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle); annotations on runtime admission/recall | Caller identity is not authenticated per-content human approval. |
| CLI focused/temporal recall; slim/full MCP and admin; full page reads | `link.py`; `mcp_package/link_mcp/server.py`; `mcp_package/link_core/memory.py` | Direct CLI recall and MCP recall/review/admin dispatch; [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), [MEM-RTE-wiki-read](#mem-rte-wiki-read) | No installed-host trace; API parameters differ across branches. |
| Combined query, capsule, lexical wiki search and graph context | `mcp_package/link_core/query.py`; `mcp_package/link_core/wiki.py`; `mcp_package/link_core/search.py` | Direct constructor, compaction, cache and search/context reads; [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-OBJ-wiki-cache](#mem-obj-wiki-cache), [MEM-RTE-wiki-read](#mem-rte-wiki-read) | Wiki reads do not inherit focused-memory lifecycle/project filtering. |
| Embedding cache and optional reranking | `mcp_package/link_core/semantic.py` | Direct embedding text, hash refresh and scoring; supplied loader/reranker findings; [MEM-OBJ-semantic-index](#mem-obj-semantic-index), runtime component annotations | Exact external weights and provider internals uninspected; no vector quality measurement. |
| Automatic session-end, manual session-end/capture, imported memory | `link.py`; `mcp_package/link_core/capture.py`; `mcp_package/link_core/importers.py` | Direct automatic hook and capture persistence/accept/cleanup; supplied import route; [MEM-OBJ-session-capture](#mem-obj-session-capture), [MEM-RTE-capture-cleanup](#mem-rte-capture-cleanup), annotation on [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | User-only origin applies to automatic mining, not all manual/import/legacy captures. Import adapter bodies remain supplied-runtime evidence. |
| Startup, first-response autobrief, prompt guard, handoff | `link.py`; `mcp_package/link_mcp/server.py`; `mcp_package/link_core/guard.py`; `mcp_package/link_core/handoff.py` | Direct brief selector, prompt hook, guard and handoff writer/reader; supplied start/autobrief wiring; [MEM-OBJ-handoff](#mem-obj-handoff), [MEM-RTE-guard-reminder](#mem-rte-guard-reminder), session-delivery annotation | Installed configuration and host scheduling unobserved; first response means server-process state. |
| Agent-authored ingest, query filing, lint, research chat | `LINK.md` | Direct procedures; [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), annotation on [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) | Agent transformation and requested human approvals are doctrine, not observed behavior. |
| Structured export, project seed, Obsidian import | `mcp_package/link_core/structured_ingest.py`; `mcp_package/link_core/project_seed.py`; `mcp_package/link_core/obsidian.py` | Supplied [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest), [RT-RTE-project-seed](runtime.md#rt-rte-project-seed), [RT-RTE-source-import](runtime.md#rt-rte-source-import), memory annotations below | Detailed adapter rendering and every project-file selection branch not independently audited here. |
| Consolidate, digest, profile, audit, wins | `mcp_package/link_core/consolidate.py`; `mcp_package/link_core/memory_wins.py`; `mcp_package/link_core/memory.py`; `link.py` | Direct plan builder, CLI consolidate and wins; [MEM-RTE-consolidation-plan](#mem-rte-consolidation-plan), [MEM-RTE-usage-feedback](#mem-rte-usage-feedback) | Digest body and every audit action branch not inspected; semantic synthesis or evaluated improvement not inferred from those names. |
| Usage events and dismissal history | `mcp_package/link_core/usage.py`; `mcp_package/link_core/capture.py` | Direct writes/readers; [MEM-OBJ-usage-ledger](#mem-obj-usage-ledger), [MEM-OBJ-dismissed-proposals](#mem-obj-dismissed-proposals) | Retrieval events measure software surfacing, not model reading or compliance. |
| Backup, operation journal, restore; Git/team sync | `mcp_package/link_core/backup.py`; `mcp_package/link_core/operations.py`; `mcp_package/link_core/sync.py`; `mcp_package/link_core/team_sync.py` | Supplied [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery), [RT-OBJ-operation-journal](runtime.md#rt-obj-operation-journal), [RT-RTE-workspace-sync](runtime.md#rt-rte-workspace-sync); direct team guidance read | No all-copy erasure, all-path transaction or remote deployment established. |
| Share URL, static HTML, audit export | `mcp_package/link_core/share.py`; `mcp_package/link_core/snapshot.py`; `mcp_package/link_core/audit_export.py` | Direct resolver/export builders; [MEM-RTE-retained-export](#mem-rte-retained-export) | External publication/access and subsequent use unobserved. |
| Viewer writes/reads, LinkBar buttons | `serve.py`; `apps/LinkBar/Sources/LinkBar/LinkStore.swift`; `apps/LinkBar/Sources/LinkBar/LinkCLI.swift` | Supplied boundary/runtime wiring into shared functions and explicit subprocesses | UI/HTTP-specific excerpt rendering and every mutation argument not independently audited. No complete client-parity claim. |
| Recall, hygiene, poisoning and salience evaluation | `scripts/eval_recall_quality.py`; `scripts/eval_memory_hygiene.py`; `scripts/eval_memory_poisoning.py`; `scripts/eval_salience.py` | Supplied recall record, direct hygiene/poisoning drivers and salience symbol inspection; [MEM-RTE-memory-evaluation](#mem-rte-memory-evaluation) | Synthetic conditions only; no evaluator run. Salience outcome remains attributed source commentary, not independently reproduced. |
| Other evaluators / validators / tests | `scripts/eval_locomo.py`; `scripts/eval_staleness.py`; `scripts/eval_token_economics.py`; `mcp_package/link_core/validation.py`; `tests/` | Included available evidence, located by boundary/tree, not inspected in this job; supplied validation callers | Prevents exhaustive metric, shape-check and test coverage assessment. No absence inferred. |
| Installed static instructions and model setup | `LINK.md`; `mcp_package/link_core/agent_instructions.py`; `mcp_package/link_core/agent_hooks.py` | [RT-OBJ-link-instructions](runtime.md#rt-obj-link-instructions), [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install), [RT-BAP-agent-steering](runtime.md#rt-bap-agent-steering) | Static deployment policy is not accumulated experience; host loading/compliance unobserved. |

## Core ideas

1. **The editable files are the durable content, not an opaque generative memory service.** Memory claims and wiki articles reach agents as natural language; frontmatter, lifecycle fields and indexes reach code as selection inputs. Optional dense vectors are derived search state, not rewritten model weights. The distinctions are retained in [MEM-OBJ-memory-claim](#mem-obj-memory-claim), [MEM-OBJ-memory-controls](#mem-obj-memory-controls) and [MEM-OBJ-semantic-index](#mem-obj-semantic-index).
2. **Capture, admission and review are different states.** Automatic transcripts create proposal-only raw notes. Accepting a proposal calls the ordinary writer, which creates active pending-review memory. Reviewing changes a trust label/window; it is not the first point at which memory becomes recallable. Approval remains a protocol in [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission). Raw rejection history can itself shape future proposal admission through [MEM-RTE-capture-cleanup](#mem-rte-capture-cleanup).
3. **Withdrawal is consumer-specific.** Focused memory recall filters archive/stale/expiry and project scope. Generic wiki indexing includes memory pages and its query/graph branch does not apply these filters. Archiving is therefore not all-path nondelivery. Updating a memory appends new body text without recomputing its TLDR; compact non-procedure output can retain the old summary while new text affects matching. [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle) and [MEM-RTE-wiki-read](#mem-rte-wiki-read) preserve both counterexamples.
4. **Context selection mixes requests and independent supply.** Query budgets select excerpts and capsule items; startup hooks and MCP autobrief independently push retained context, while prompt guards push one constraint when code judges overlap. Handoffs carry task substance with expiry, not a live worker or the old session window. [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery), [MEM-RTE-guard-reminder](#mem-rte-guard-reminder) and the recall annotation identify each consumer and limit.
5. **Accounting is not evidence of reliance.** Usage events record returned names, not answers or model behavior. Their known live behavioral consumer is guard cooldown; salience is an optional library ranking input, not wired into the inspected ordinary adapters. Consolidation proposes commands instead of applying a learned semantic rewrite. [MEM-RTE-usage-feedback](#mem-rte-usage-feedback) and [MEM-RTE-consolidation-plan](#mem-rte-consolidation-plan) bound these labels.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-claim
Label: Memory claim text

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Material output part of the admission route, not a second declaration of that route. Source-native identity: body, title, TLDR and optional procedure steps in `wiki/memories/*.md`. Substrate: plain local Markdown. Form: natural-language claim/procedure interpreted by agents and humans; the same text is also input to symbolic lexical checks and numerical embedding. Lineage: caller text or accepted mined proposal, source string, appended updates and optional predecessor/successor links. No actual user corpus is supplied. Consumers: focused recall, brief, explain, wiki search/context and viewer; authority is advice/context or procedure instruction, not a host permission rule. Direct editing is possible; shared writer admits active pending content. Closest supplied records are admission and [RT-BAP-context-packet](runtime.md#rt-bap-context-packet); neither separately declares the text part. SRC-1, `mcp_package/link_core/memory.py`.

> if memory_type == "procedure":
>     use_when = (
>         f"- {clean_trigger}" if clean_trigger
>         else "- An agent starts a task this procedure covers."
>     )
>     use_when += "\n- Follow the steps in order; confirm with the user before deviating."
> --- `mcp_package/link_core/memory.py`

#### MEM-OBJ-memory-controls
Label: Memory control fields

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Source-native identity: scope/project/visibility, review status/dates, status/archive/restore/expiry, applies_when and supersession fields parsed from the same memory pages. Substrate: YAML-like Markdown frontmatter, loaded into Python records. Form: symbolic fields with fixed code comparisons; source/review_note/archive_reason strings supply readable provenance and rationale to explainers. Distinct from [MEM-OBJ-memory-claim](#mem-obj-memory-claim): these fields gate or rank content rather than say what the remembered claim is. Consumers: focused selection, inbox/quality actions, explanation lineage and export policies; these are not filesystem access permissions. Empty project permits broad selection, and no selected project means no project filtering. Visibility chiefly concerns sharing/export, not an ACL around local retrieval. Origin is caller-controlled write/review/edit or imported bytes; no independent human assent is established. SRC-1, `mcp_package/link_core/memory.py`.

> def memory_visible_for_project(record: Mapping[str, object], project: str | None = None) -> bool:
>     project_name = normalize_project(project)
>     if not project_name:
>         return True
>     if str(record.get("scope") or "").lower() != "project":
>         return True
>     record_project = normalize_project(str(record.get("project") or ""))
>     return not record_project or record_project == project_name
> --- `mcp_package/link_core/memory.py`

#### MEM-OBJ-retrieval-context
Label: Retrieval context text

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Source-native identity: the memory page's optional `context` frontmatter, bounded to 600 characters at write time. Substrate: Markdown frontmatter and transient parsed record. Form: natural-language surrounding dialogue/notes used by lexical and numerical selectors, not a claim delivered by slim recall. Lineage may be caller-supplied surroundings or proposal extraction; origin is not automatically a user utterance. Distinct from the claim and lifecycle metadata: this text affects findability while duplicate/conflict/echo comparison uses claim text, and slim output removes it. Code has selection authority over it; the later agent sees the selected claim instead. SRC-1, `mcp_package/link_core/memory.py`, `mcp_package/link_core/semantic.py`. Closest supplied counterpart is admission; this is its separate selector-input part.

> def slim_memory(record: Mapping[str, object]) -> dict[str, object]:
>     return {key: value for key, value in record.items() if key not in {"body", "context"}}
> --- `mcp_package/link_core/memory.py`

#### MEM-OBJ-session-capture
Label: Session capture notes and provenance

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Source-native identity: Markdown under `raw/memory-captures/`, with Source Input, Notes, optional Proposal Source and How Link Read This Session. Substrate: local raw files, one refreshable capture per conversation identity when supplied. Form: natural-language retained notes/mining input/decision trail plus symbolic capture/project/date/source-type metadata. This is retained input and derivation context, not accepted memory or a complete verbatim transcript guarantee. Automatic mining is user-only head/tail text; review notes can include assistant text after extraction filtering. Manual notes, imported instruction text and old captures differ. Consumers: inbox, accept-time re-miner, redaction/delete/dedup and startup review summaries. Proposal Source and decision trail permit later inspection of selection reasons, but acceptance passes the selected claim/context/source path, not the whole decision trail, into the memory page. SRC-1, `mcp_package/link_core/capture.py`, `link.py`.

> mining_text = capture_proposal_source(raw_text) or notes
> # Imported captures mine in curated mode: the source was a deliberate
> # instruction file, so chat-junk heuristics do not apply to it.
> curated = str(meta.get("source_type") or "").strip().lower() == "import"
> --- `mcp_package/link_core/capture.py`

#### MEM-OBJ-dismissed-proposals
Label: Dismissed proposal history

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Source-native identity: `raw/memory-captures/.dismissed-proposals.json`, separate from the notes it survives. Substrate: local JSON. Form: symbolic fingerprint membership/dismissal timestamps plus readable text prefixes of up to 160 characters. Lineage: confirmed capture deletion re-mines proposals and records them; FIFO retains up to 500 entries. Consumers: automatic session-end filtering and dedup coverage. Authority: code suppresses matching future proposals; it does not tell the agent a proposition is true. The human-decline interpretation is the API contract, not authentication of the caller. Distinct control part of capture, not a second raw-note store. SRC-1, `mcp_package/link_core/capture.py`, `link.py`.

> entries[fingerprint] = {"memory": text[:160], "dismissed_at": stamp}
> --- `mcp_package/link_core/capture.py`

#### MEM-OBJ-wiki-pages
Label: Wiki knowledge pages

Source-native identity: source, concept, entity, comparison and exploration pages under `wiki/`; memory pages participate in the same generic index but their claim/control parts are declared separately above. Substrate: Markdown. Form: natural-language claims, mechanisms, reasoning and source citations, with symbolic links/frontmatter for graph/index consumers. Lineage spans agent-authored source synthesis, query filing, research-chat synthesis followed by ingest, deterministic structured rendering and project seeding. Closest supplied records: [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki), [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest), [RT-RTE-project-seed](runtime.md#rt-rte-project-seed); this output spans their routes rather than being part of exactly one. Consumers: later FTS/graph query, full context, direct file readers and viewer/export. Authority at the agent is interpreted factual or procedural context. Source count/maturity and confidence labels are author assertions or structural metadata, not verified truth. SRC-1, `LINK.md`, `mcp_package/link_core/wiki.py`.

> - Every claim must link back to its source page. No orphan claims.
> - Tag confidence on claims: `high` (explicitly stated), `medium` (reasonable inference), `low` (speculative)
> --- `LINK.md`

#### MEM-OBJ-wiki-cache
Label: Wiki indexes and cached text

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Source-native identity: `wiki/index.md`, `wiki/_backlinks.json`, `.link-cache/wiki-cache-v2.json`, `.link-cache/page-fts-v2.sqlite` and in-process maps. Substrate: Markdown, JSON, SQLite and process memory. Form: symbolic graph/search/access state; cached article strings preserve natural-language payload, not an independent claim synthesis. Lineage: page scanning/parsing, tokenization, index/backlink rebuild and signature-based cache reuse. Consumers: code selects matching pages and neighbors; human/agent file fallback uses catalog/backlinks. Authority is selection and delivery. Distinct from durable content: caches can be rebuilt; source page changes invalidate through mtime/signature checks, not a truth check. Persistent cache contains full text, relevant to deletion limits. SRC-1, `mcp_package/link_core/wiki.py`, `mcp_package/link_core/search.py`, `LINK.md`.

> records.append({"path": rel_text, "text": text, "signature": signature})
> --- `mcp_package/link_core/wiki.py`

#### MEM-OBJ-semantic-index
Label: Memory semantic vectors

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Source-native identity: `.link-cache/semantic/memories.json`. Substrate: local JSON. Form: dense distributed numerical vectors with symbolic model key, per-name text hash and schema version. This is a derived representation of retained memories, not a learned provider-parameter update. Lineage: title, TLDR, trigger, tags, first 1,000 body characters and up to 600 context characters are embedded and normalized; refreshed hashes/model key prune or replace vectors. Consumers: later query embedding/cosine/standout scoring, then focused-memory ranking. Model2vec and fastembed components remain separately declared by runtime; no exact weight pin or mutable-cache equivalence to an immutable model version is inferred. Unknown weight provenance stays local to those components. SRC-1, `mcp_package/link_core/semantic.py`.

> items[name] = {
>     "hash": wanted[name],
>     "vec": [round(value, 5) for value in _normalize(vector)],
> }
> --- `mcp_package/link_core/semantic.py`

#### MEM-OBJ-handoff
Label: Session handoff packet

Part of: [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery)

Source-native identity: `raw/handoffs/*.md`. Substrate: local Markdown. Form: natural-language task/note/next steps and symbolic creation/expiry/project/previous-path metadata. Lineage: caller-authored standalone relay, secret-pattern redaction and breadcrumb to newest pending packet. Consumers: pending reader and next start/brief delivery; substance rather than the full prior conversation is surfaced. Default TTL is 48 hours; brief text budget constant is 1,500 characters. Expired files remain history; explicit clear removes a packet. Agent authority is task resumption guidance, not a delegated runtime identity. This part is separate from approved long-term memory and proposal captures. SRC-1, `mcp_package/link_core/handoff.py`; delivery passage is supplied by the parent record.

> def pending_handoffs(
>     root: Path,
>     project: str | None = None,
>     now: str | None = None,
> ) -> list[dict[str, object]]:
>     """Unexpired handoffs, newest first. Expired files are left in place
>     (they are the chain's history) but never surfaced."""
> --- `mcp_package/link_core/handoff.py`

#### MEM-OBJ-usage-ledger
Label: Retrieval usage events

Source-native identity: `.link-usage.json` at workspace root. Substrate: local JSON ring of up to 500 events. Form: symbolic time/kind/count/memory names/project, not the query, answer, transcript or readable rationale. Lineage: adapters record surfacing events; recording is best effort and switchable off. Consumers: usage summary/wins and guard cooldown; optional library salience can compute boosts. Closest supplied overlaps: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) and [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery) mention accounting; this shared object spans both, not one contained route. Returned identity counts are access metadata, not proof of model reading or useful action. SRC-1, `mcp_package/link_core/usage.py`, `mcp_package/link_core/guard.py`.

> json.dumps({"schema": "link-usage-v1", "events": events[-MAX_EVENTS:]}, indent=1) + "\n",
> --- `mcp_package/link_core/usage.py`

### Routes

#### MEM-RTE-memory-lifecycle
Label: Memory lifecycle curation

Distinct from [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission): this route changes, reviews or withdraws existing files. Overlap is shared pages and later consumers, not duplicate initial admission. Endpoints: caller identifier/text/note/reason → core mutation → page/control/index/log changes → later recall/explain. Owner: caller proposes and invokes, code resolves target/checks state/conflict and confirmation; human supplies/approves under the protocol, not an authenticated per-content gate. Mode: open maintenance requests; answer oracle: inapplicable, no reference outcome. Updates append text with time/source and reset review; review marks reviewed and re-arms typed due window when needed. Archive retains bytes/reason; restore changes status; forget requires confirmation, deletes page, updates index/backlinks and redacts title references in logs. Visibility mutation changes sharing classification. Recovery uses journal snapshots as in [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery), not universal all-copy rollback. SRC-1, `mcp_package/link_core/memory.py`.

- Immediate return: changed status/review/update counts, candidate refusal or forget confirmation/result.
- Later read-back: reloaded page/control fields affect focused recall, inbox and explanation; archive reason and review note are exposed by explanation.
- Delegated visibility: workspace readers and connected hosts; remote/archive/cache copies are not automatically erased.
- Selection predicate: resolved identifier; active-state check and conflict candidates for update, caller allow_conflict override; explicit confirm for forget; review is callable without proof of human assent.
- Invalidation or expiry: updated body resets pending review but leaves existing TLDR/snippet source text; archive/stale/expiry affect focused selection, restore does not remove expiry; forget removes current file, not all historical copies.
- Activation or effect: durable byte/metadata mutation wired; changed agent reliance uninspected.
- Evidence limits: update's appended text can affect matching while compact output still uses old TLDR; procedure output separately supplies bounded steps. Temporal selection reconstructs lifecycle eligibility, not arbitrary past body versions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> updated_body = append_memory_update(body, clean_text, timestamp, clean_source)
> updates = {
>     "updated_at": f'"{timestamp}"',
>     "update_count": str(next_update_count),
>     "last_update_source": f'"{frontmatter_string(clean_source)}"',
>     "review_status": "pending",
> }
> --- `mcp_package/link_core/memory.py`

> "review_note": record.get("review_note", ""),
> --- `mcp_package/link_core/memory.py`

#### MEM-RTE-wiki-read
Label: Generic wiki read

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Material branch of combined recall and explicit search/context, distinct from focused-memory selection. Endpoints: query/topic → all-page cache/search → primary and graph neighbors → packet/full context → external agent/human. Owner: software ranks and clips; foreground agent chooses follow-up; state is indexed pages and backlink graph. Generic cache enumerates all non-dot Markdown, including archived/project-scoped memory pages. Search and context do not call memory lifecycle/project gates. Thus combined recall can deliver an archived or another project's memory as a wiki page even when focused-memory results exclude it. Page compaction does not retain the memory-specific review/lifecycle warnings. SRC-1, `mcp_package/link_core/wiki.py`, `mcp_package/link_core/search.py`, `mcp_package/link_core/query.py`.

- Immediate return: ranked search metadata, primary full body or clipped packet body and neighbor summaries/provenance.
- Later read-back: prior authored wiki/memory content reaches later query/context invocations; indexes are reused or rebuilt.
- Delegated visibility: caller's host receives tool JSON; direct catalog/file fallback and local viewer readers can reach the same stored pages.
- Selection predicate: lexical/FTS candidate generation and scores, best matching page, inbound plus forward graph links; item/character budgets for combined query, broader content request separately.
- Invalidation or expiry: page signature/mtime and index rebuilding; generic page branch lacks focused-memory archive/expiry/project predicates.
- Activation or effect: code delivers selected bodies; agent adoption or compliance uninspected.
- Evidence limits: this is an inspectable alternate delivery path, not a reproduced leak; ranking/corpus conditions determine which page actually appears. Source-count fields do not authenticate claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> def _markdown_page_paths(wiki_dir: Path) -> list[Path]:
>     return sorted(path for path in wiki_dir.rglob("*.md") if not path.name.startswith("."))
> --- `mcp_package/link_core/wiki.py`

> raw_search_results = search_pages(q, cache, limit=limits["search_results"] + 1)
> search_has_more = len(raw_search_results) > limits["search_results"]
> search_results = raw_search_results[: limits["search_results"]]
> context = context_for_topic(
>     wiki_dir,
>     q,
>     cache,
>     limit=limits["context_pages"] + 1,
> )
> --- `mcp_package/link_core/query.py`

#### MEM-RTE-capture-cleanup
Label: Capture rejection and cleanup

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Endpoints: explicit redact/delete/dedup request → capture resolver/re-miner/fingerprints → retained edited capture, deletion or dismissal ledger → later inbox and automatic capture filtering. Owner: caller selects/confirms deletion or applies dedup; code proposes removable entries and records dismissals. Mode: open cleanup, no answer oracle. Guidance: distinguish user rejection from redundant-copy cleanup; dry-run dedup proposes no semantic rewrite. Human approval is requested but caller confirmation is the physical gate. Redaction changes detected secret values, not proof of complete sanitization. Recovery of deleted raw bytes is not provided by this helper; optional backups differ. SRC-1, `mcp_package/link_core/capture.py`, `link.py`.

- Immediate return: redaction counts, deletion confirmation/result, or kept/removable/removed capture plan.
- Later read-back: changed captures affect later re-mining; recorded dismissals veto matching automatic proposals/dedup candidates at later invocations.
- Delegated visibility: local review consumers; no automatic memory claim delivery from the ledger.
- Selection predicate: selected capture; confirmed deletion re-mines up to ten proposals; dedup scans newest-first, compares accepted/dismissed/pending fingerprints, and keeps entries with fresh proposals.
- Invalidation or expiry: capture removal; bounded FIFO dismissal history can lose old suppression; dedup deletions deliberately do not add dismissals.
- Activation or effect: software cleanup and future suppression wired; improved user review burden unobserved.
- Evidence limits: deleting a capture does not withdraw an already accepted memory; text prefixes survive in dismissal metadata. No universal sensitive-data erasure.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if record_dismissals:
>     try:
>         text = capture_path.read_text(encoding="utf-8", errors="replace")
>         meta, _ = parse_frontmatter(text)
>         mining_text = capture_proposal_source(text)
> --- `mcp_package/link_core/capture.py`

#### MEM-RTE-guard-reminder
Label: Proactive constraint reminder

Part of: [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery)

Endpoints: host per-prompt hook or MCP query guard wrapper → lexical constraint selector → cooldown check/usage event → reminder text → receiving agent. Owner: code decides; host schedules and interprets. Inputs: current prompt, project, stored claims and recent guard events. Constraint-shaped TLDR/title must strongly overlap; no model load in guard itself. This selects a retained claim without a separate explicit recall request. The reminder asks the agent to identify conflict and confirm with the user, not mechanically block the requested action. SRC-1, `mcp_package/link_core/guard.py`, `link.py`; runtime parent supplies MCP guard wiring.

- Immediate return: one constraint reminder or silence; hook can instead nudge a handoff for switch/stop intent.
- Later read-back: saved constraints and recent guard events are consumed on later prompts; events suppress repeated delivery for 45 minutes.
- Delegated visibility: stdout/host context or MCP payload; host controls further propagation.
- Selection predicate: prompt at least 12 characters, constraint regex, focused lexical top-one recall with score at least 15 and permitted confidence; recent guard suppresses repeat.
- Invalidation or expiry: memory lifecycle and overlap; cooldown reads retained event time; usage off/unwritable can prevent recording and therefore later suppression.
- Activation or effect: software emits guidance; actual conflict identification, confirmation or action blocking uninspected.
- Evidence limits: overlap is not contradiction detection; a label like guard does not establish enforcement or human authorization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "If the request conflicts with it, say so and confirm with the user "
> "before proceeding."
> --- `mcp_package/link_core/guard.py`

#### MEM-RTE-usage-feedback
Label: Retrieval accounting feedback

Distinct from supplied recall/delivery routes: this route transforms their event metadata into later reporting/cooldown decisions. Endpoints: returned memory names → best-effort bounded ledger → usage summary/wins or guard cooldown; optional salience function → caller-provided ranking boost. Owner: code records/summarizes; caller may disable; human can use suggested review/archive actions. Mode: ordinary instrumentation and maintenance, not an expected-answer evaluation. No content successor is automatically admitted by usage summary. SRC-1, `mcp_package/link_core/usage.py`, `mcp_package/link_core/guard.py`, `mcp_package/link_core/memory_wins.py`, `mcp_package/link_core/memory.py`.

- Immediate return: boolean recording result, usage counts/top names/never-retrieved list, wins with honest-note text, or salience mapping.
- Later read-back: later summary/wins and guard consume event history; optional library callers can feed salience into memory ranking, but inspected CLI/MCP/query adapters do not pass it.
- Delegated visibility: local reports/reminders; usage state is not the full conversation or exported long-term knowledge.
- Selection predicate: supported event kind and up to twenty nonempty names; last 500 events; summary window and grace period; guard kind/time/name; salience minimum count and bounded logarithmic boost.
- Invalidation or expiry: event ring and summary window; off switch; missing/corrupt data returns empty; never-retrieved means absent from retained ledger, not never delivered over all history.
- Activation or effect: live guard repetition policy can depend on retained use; popularity ranking remains an optional API capability, not deployed ordinary feedback.
- Evidence limits: event emission records software surfacing, not whether the host read, relied on or benefited from content. Salience source commentary reports a rejected experiment; this job did not reproduce it.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for event in reversed(load_usage(root)):
>     if str(event.get("kind")) != "guard":
>         continue
> --- `mcp_package/link_core/guard.py`

> # MEASURED AND NOT ADOPTED. Ranking is not usage-aware, and this is the
> # function that was tried.
> --- `mcp_package/link_core/usage.py`

#### MEM-RTE-consolidation-plan
Label: Consolidation proposal plan

Distinct from existing admission/capture routes: read-only comparison/planning precedes their mutations. Endpoints: capture inbox/review inbox and optional merge candidates → grouping/command construction → human/agent plan → separately invoked mutation routes. Owner: code proposes; user is asked to approve each action; caller can veto by not invoking commands. Mode: open maintenance, triggered by backlog/request. No answer oracle: similarity and review state are heuristics. CLI supplies merge candidates; inspected slim MCP review-consolidate does not. Plan itself persists no new merged meaning; later approved update/archive/delete operations carry their own recovery. SRC-1, `mcp_package/link_core/consolidate.py`, `link.py`, `mcp_package/link_mcp/server.py`.

- Immediate return: duplicate groups, recurring themes, review commands and optional merge/archive commands.
- Later read-back: inapplicable — this builder writes no retained successor; accepted commands separately mutate pages/captures.
- Delegated visibility: plan returned to caller; host decides any agent delegation.
- Selection predicate: supplied bounded inboxes, duplicate/theme grouping and caller-supplied merge candidates; review plan capped at ten.
- Invalidation or expiry: inapplicable — plan is recomputed and can become stale before commands run; no persisted plan lifecycle in this function.
- Activation or effect: action suggestions wired, not autonomous semantic consolidation or criticism-shaped revision.
- Evidence limits: route name does not establish forgetting, synthesis or improvement; CLI/MCP planning surfaces are not fully equivalent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "Read-only plan. Nothing was merged, deleted, or saved. "
> "Run the listed commands only after the user approves each action."
> --- `mcp_package/link_core/consolidate.py`

#### MEM-RTE-retained-export
Label: Retained content export

Distinct from [RT-RTE-workspace-sync](runtime.md#rt-rte-workspace-sync): local permalink, static HTML and audit JSON delivery rather than Git reconciliation. Endpoints: explicit identifier/export options → cached page resolution or renderer/audit builder → URL, HTML files or JSON → documented local viewer/offline reader/security reviewer. Owner: caller chooses options/output; code filters/pages/scans and can refuse. Mode: open export, no answer oracle; guidance is privacy/sensitivity policy, not factual checking. Snapshot default omits memories; including memories and private memories are separate options. Code refuses secret-looking/unreadable wiki by default, with allow_sensitive override. Audit omits full body/raw content but includes slim TLDR/snippet/provenance. Force can remove nonempty output before later sensitivity refusal; atomic files are not an all-export rollback. SRC-1, `mcp_package/link_core/share.py`, `mcp_package/link_core/snapshot.py`, `mcp_package/link_core/audit_export.py`.

- Immediate return: permalink/serve command, created snapshot manifest, or audit packet/file and counts.
- Later read-back: retained HTML/audit files afford later human/offline consumption; permalink reloads live viewer content. External publication and actual readers unobserved.
- Delegated visibility: caller-selected destinations; raw/operation/live-MCP state excluded from HTML export, not every readable personal detail from audit summaries.
- Selection predicate: identifier exact/search resolution; snapshot skips index/log and memories by default, private memories separately; no archive/expiry filter in snapshot page inclusion; audit bounded records/log/operations.
- Invalidation or expiry: snapshot stays at export-time bytes until regenerated/removed; source withdrawal does not edit prior exports; live permalink follows current page availability.
- Activation or effect: files/URLs produced; later human/agent reliance uninspected.
- Evidence limits: exported memory status need not match focused recall eligibility; body omission is not summary redaction; archive/backups/remote/export copies prevent an all-copy forgetting claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if category == "memories":
>     if not include_memories:
>         return False
>     if _memory_visibility(name, meta_index) == "private" and not include_private_memories:
>         return False
> return True
> --- `mcp_package/link_core/snapshot.py`

#### MEM-RTE-memory-evaluation
Label: Offline memory governance evaluation

Distinct from [RT-RTE-recall-evaluation](runtime.md#rt-rte-recall-evaluation): hygiene and poisoning drivers exercise acquisition/governance, not just target-rank retrieval. Endpoints: maintainer-authored synthetic event/attack corpus → temporary wiki writes/recall or warning checks → labels/metrics/report/exit. Owner: dataset author supplies ground truth; code applies heuristic pipeline and scores; maintainer decides any later product change. Mode: bounded offline experiment; oracle is authored event intent/current memory identities or expected attack outcomes/benign controls. Hygiene driver automatically supersedes first detected conflict as simulation policy, not evidence of actual user review. Poisoning simulates one-click acceptance and counts warning survival/refusal; its review-gate label does not independently measure authenticated approval. Guidance/proposed change: evaluator provides comparisons/regression failures, not a runtime memory-admission update. SRC-1, `scripts/eval_memory_hygiene.py`, `scripts/eval_memory_poisoning.py`.

- Immediate return: junk/exposure/precision/growth/temporal metrics or attack outcome/false-positive rows and regression exit.
- Later read-back: temporary generated memory is reread within evaluator; no production memory/ranker update is installed by these drivers.
- Delegated visibility: inapplicable — these inspected drivers use authored synthetic text and code, not inner model agents.
- Selection predicate: gated versus ungated event processing, heuristic extraction/echo/conflict; attack expected outcomes and benign warning checks.
- Invalidation or expiry: temporary corpus discarded with temporary directory; fresh runs recompute; no admitted deployment checkpoint.
- Activation or effect: evaluation capacity wired; no run performed here and no benefit or subsequent product decision observed.
- Evidence limits: synthetic helper-level admission does not cover alternate wiki/Git/file read/write paths, host behavior or arbitrary attacks. External QA report remains reported operation only.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if result.get("conflict"):
>     # The documented resolution loop: replace, with lineage.
>     candidate = result["conflict_candidates"][0]
>     result = _write(
>         wiki, proposal, event["date"],
>         supersedes=str(candidate.get("name")),
>     )
> --- `scripts/eval_memory_hygiene.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Memory-specific output parts are [MEM-OBJ-memory-claim](#mem-obj-memory-claim), [MEM-OBJ-memory-controls](#mem-obj-memory-controls) and [MEM-OBJ-retrieval-context](#mem-obj-retrieval-context). Shared writer secret checking covers clean_text/title in its inspected gate, not an all-field proof. New content is active/pending; typed default review windows are project 3 months, preference/note/procedure 6, decision/fact 12. Review-due is a warning, unlike expires_at default-recall exclusion. Supersession records a new backward link and archives the predecessor with a forward link/reason; explanation later walks lineage and exposes reasons. A source string is provenance supplied by the caller, not source authentication. SRC-1, `mcp_package/link_core/memory.py`; parent retains passage for active/pending/overrides.

> secret_labels = secret_value_warnings(f"{clean_text}\n{title or ''}")
> password_hint = looks_like_password_note(clean_text)
> --- `mcp_package/link_core/memory.py`

#### On [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Focused read-back selects retained memory by query/project/lifecycle, lexical body/head/trigger/context, optional semantic score, recency/review state and applicability. Steps for procedures carry up to 800 characters; ordinary slim output omits full body and context. CLI temporal/as-of reconstructs eligibility using lifecycle dates; it does not load historical body snapshots. Empty-query startup brief preferentially chooses recent preferences, decisions and project memories, fills with other active records, and omits unmatched conditional memories. Query recall instead demotes unmatched conditions. SRC-1, `mcp_package/link_core/memory.py`, `link.py`.

Working-context control: code keeps most source bodies out of the initial packet. Micro/small/medium/large budgets respectively select 1/3/6/10 memories, 1/3/5/8 context pages and 3/5/7/10 capsule items; primary excerpts are 650/1,200/2,400/5,000 characters, neighbors 220/450/700/1,200. Agent chooses later larger-budget/full-context/file requests. Removed material remains in Markdown; the returned path is a follow-up instruction, not an automatically dereferenceable model-window pointer. Link neither pops a separate agent frame nor evicts old host turns; host isolation/compaction remains external. Capsule first can omit review/applicability/steps fields available in richer packet items; warnings and full context are not guaranteed to survive an agent reading only the capsule. Generic wiki branch [MEM-RTE-wiki-read](#mem-rte-wiki-read) requires narrowing the parent selection predicate to focused memory. SRC-1, `mcp_package/link_core/query.py`.

> def _capsule_item(item: Mapping[str, object], max_chars: int) -> dict[str, object]:
>     content = item.get("summary") or item.get("content") or item.get("snippet") or ""
>     return _drop_empty({
>         "kind": item.get("kind", ""),
>         "name": item.get("name", ""),
>         "title": item.get("title", ""),
>         "summary": _trim_text(content, max_chars),
>         "why_selected": item.get("why_selected", ""),
>         "rank_signals": item.get("rank_signals", []),
>         "hybrid_rank": item.get("hybrid_rank", 0),
>         "provenance": item.get("provenance", {}),
>     })
> --- `mcp_package/link_core/query.py`

#### On [RT-CMP-model2vec](runtime.md#rt-cmp-model2vec)

Derived memory representation and later selector are [MEM-OBJ-semantic-index](#mem-obj-semantic-index). Cached vectors change with bounded memory text/model key while provider parameters do not change in this route. Exact external weight provenance remains uninspected as the parent states. SRC-1, `mcp_package/link_core/semantic.py`.

#### On [RT-CMP-fastembed](runtime.md#rt-cmp-fastembed)

Same derived index consumer as [MEM-OBJ-semantic-index](#mem-obj-semantic-index); dense representations influence ranking, not a directly readable claim or procedure. Context/model hashes invalidate derived state, not weight training. SRC-1, `mcp_package/link_core/semantic.py`.

#### On [RT-CMP-reranker](runtime.md#rt-cmp-reranker)

Reranking is a query/result transformation, not an inspected durable trace-trained checkpoint. Shared query and startup selection differ from explicit memory-only reranking, as parent establishes. No independent provider-weight or deployed benefit evidence added. SRC-1, `mcp_package/link_core/semantic.py`, `mcp_package/link_mcp/server.py`, `link.py`.

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Raw-to-derived-to-later chain: external transcript → bounded extraction/user-turn mining and heuristic proposals → raw notes plus mining provenance/decision trail → later accept-time re-mining → selected memory writer → later focused/wiki retrieval. Automatic hook suppression uses existing-memory echoes, duplicates, pending and dismissed fingerprints; injection-shaped proposals are flagged, not censored solely for that shape. Selected derived memories retain source path and optional surrounding context, not complete hook rationale. Raw capture is not itself a durable approved rule. Manual research-chat in LINK.md is an additional agent-authored synthesis: user approves captured substance into raw, then separately requests ingest, potentially producing source/wiki articles rather than personal memories. SRC-1, `link.py`, `mcp_package/link_core/capture.py`, `LINK.md`.

> # Kept, never censored — but the trail says what shape it has so
> # the reviewer knows to check whether they actually said it.
> --- `link.py`

> 4. The file should synthesize the conversation's substance, not dump raw chat logs. Extract the knowledge, not the back-and-forth.
> 5. Do NOT auto-ingest. Tell the human the file is ready for ingest when they want.
> --- `LINK.md`

#### On [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery)

Retained parts supplied automatically are selected memory summaries, review/capture summaries and [MEM-OBJ-handoff](#mem-obj-handoff). Trigger/selector distinction matters: installed startup hook reads project-aware active memory; first eligible MCP response has server-process state, not a proven shared host-session identity. Pending handoff substance reaches next consumer with priority instruction; expiry suppresses surfacing but leaves file history. Prompt guard is a separate selector part [MEM-RTE-guard-reminder](#mem-rte-guard-reminder), with metadata feedback in [MEM-RTE-usage-feedback](#mem-rte-usage-feedback). Delivery remains interpreted natural language. Handoff is retained task state, not automatically accepted long-term memory or restored hidden reasoning. SRC-1, `mcp_package/link_core/handoff.py`, `mcp_package/link_core/memory.py`, `link.py`, `mcp_package/link_mcp/server.py`; parent supplies push and clipping passages.

#### On [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki)

Write agency: external agent extracts/merges/restructures knowledge, while human selects sources, approves filing/research and chooses lint repairs. Initiating ingest is workflow authorization, not per-claim assent. Source pages/raw attribution and authored reasoning can remain for later readers, but budgeted graph neighbors and primary excerpts may not include those reasons. Contradictions/Open Questions and confidence/maturity are requested material structures, not a factual oracle. Source-relative knowledge authoring can alter later context without provider parameter change; learning benefit and iteration remain unestablished independently. SRC-1, `LINK.md`, `mcp_package/link_core/wiki.py`, `mcp_package/link_core/query.py`; parent's theory account is not expanded into an actual theory from the empty scaffold.

#### On [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest)

Retained knowledge pages and source/output ownership hashes have different consumers: later agents read pages; next adapter apply reads manifest/hash control. Source rendering is software authorship; caller apply/adopt/prune is admission, staged validation a structural veto, not per-claim human review. Obsolete outputs remain unless prune is requested; therefore refreshed raw source does not universally withdraw earlier rendered knowledge. SRC-1, `mcp_package/link_core/structured_ingest.py`; supplied parent supports these mechanics. Detailed adapter semantic preservation uninspected here.

#### On [RT-RTE-project-seed](runtime.md#rt-rte-project-seed)

Retained raw project snapshot provides provenance; generated source page immediately participates in later generic wiki search/graph recall. Software selects bounded project material and renders, caller initiates/overwrites. The source-backed page is not a reviewed preference merely because the calling agent is following steering. Historical Git material can join current documentation; temporal truth must not be inferred from snapshot inclusion. SRC-1, `mcp_package/link_core/project_seed.py`; supplied parent supports production/read-back; complete rendering details uninspected here.

#### On [RT-RTE-source-import](runtime.md#rt-rte-source-import)

Raw vault copies afford later ingest; they are not immediately equivalent to recalled wiki knowledge. Instruction/auto-memory import is instead proposal capture with mixed source provenance. Imported text changes authorship evidence, not authenticated user endorsement. SRC-1, `mcp_package/link_core/obsidian.py`, `mcp_package/link_core/importers.py`; these are supplied-runtime findings, not newly inspected adapter bodies.

#### On [RT-RTE-workspace-sync](runtime.md#rt-rte-workspace-sync)

Transferred Markdown retains content/control strings from remote state; local recall reparses them rather than requiring ordinary writer admission. Team export filters current active/team pages but copying alone does not remove earlier remote files. Read-only team guidance warns that private pages and pending review can be unsafe to push, yet suggested Git staging is not a per-file visibility gate. Actual import/sync mechanics are the parent findings; direct file adoption remains alternate authority. SRC-1, `mcp_package/link_core/sync.py`, `mcp_package/link_core/team_sync.py`.

> "active private memories would be included by git add wiki; do not team-sync until they are archived or marked visibility: project/team intentionally."
> --- `mcp_package/link_core/team_sync.py`

#### On [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery)

Pre-write bytes and backup roots are alternative retained checkpoint forms. Their later consumer is explicit recovery/restore, which can reintroduce earlier memory/wiki/raw state; semantic lifecycle judgments do not themselves make old snapshots disappear. Backup defaults to wiki, raw opt-in; ordinary forget is not complete removal from earlier archives. This is byte recovery, not host conversation compaction or improved semantic policy. SRC-1, `mcp_package/link_core/backup.py`, `mcp_package/link_core/operations.py`; supplied parent establishes mechanics, no crash experiment added.

#### On [RT-OBJ-operation-journal](runtime.md#rt-obj-operation-journal)

Storage/form distinction: symbolic operation status and touched paths govern software recovery; snapshot bytes can contain readable claim/article content. Recovery can give those bytes later behavioral relevance via restored ordinary read routes, without converting journal metadata into agent knowledge. SRC-1, `mcp_package/link_core/operations.py`; supplied parent and recovery route support this checkpoint account.

#### On [RT-BAP-context-packet](runtime.md#rt-bap-context-packet)

Actual consumer force varies by delivered part: memory claim/procedure is advice/instruction, wiki body factual context, handoff priority task guidance, guard conflict-confirmation request. Symbolic selectors determine delivery but do not authenticate source trust or enforce agent obedience. Capsule omits richer warnings/steps fields; generic wiki branch can bypass focused lifecycle labels. These limits follow [MEM-RTE-wiki-read](#mem-rte-wiki-read), [MEM-RTE-guard-reminder](#mem-rte-guard-reminder) and the recall annotation. SRC-1, `mcp_package/link_core/query.py`, `mcp_package/link_core/guard.py`, `mcp_package/link_core/handoff.py`.

## Write side

**Acquisition and authoring.** Explicit text/capture acceptance uses caller-authored or deterministically extracted claims, shared heuristic admission and pending active storage. User approval is a shipped protocol, not a universal verified gate. Wiki synthesis uses an external agent under LINK.md; deterministic structured ingest and project seed are different authorship/admission mechanisms. Obsidian raw copies await ingest; imported instruction text enters curated proposal mining. Git/file/restore can admit existing content without shared new-memory checks. These differences are located in the admission, agent-wiki, structured-ingest, seed, import, sync and recovery annotations, not collapsed into one approval claim.

**Trace-fed transformation.** Automatic session-end extraction preferentially removes Link-injected echoes, bounds mining to user head/tail turns and retains raw review context. Later acceptance re-mines retained source rather than reading a frozen numbered proposal checkpoint; available proposals can change with existing memory/context. Accepted claim/source/context then reaches later recall. Manual session-end and research-chat synthesis are alternatives with different origin/approval. Captures retain decision reasons for reviewer inspection; accepted pages need not repeat those reasons. Handoff preserves caller-authored task state with expiry. Usage retains access events; dismissal preserves rejection evidence as fingerprints. The first changes prompt repetition; the second changes future proposal eligibility. Raw logging alone would not establish either behavior-shaping chain. See [MEM-OBJ-session-capture](#mem-obj-session-capture), [MEM-RTE-capture-cleanup](#mem-rte-capture-cleanup), [MEM-RTE-usage-feedback](#mem-rte-usage-feedback).

**Maintenance, rejection and withdrawal.** Update is append/reset-review rather than summary replacement; review re-arms a window; supersession archives with lineage; archive is retained soft withdrawal from focused memory; forget removes current page but not prior snapshots/exports/dismissed prefixes. Consolidate constructs approved-action suggestions, not an autonomous merge. Redact/dedup/delete captures have distinct effects; deleting accepted source does not remove the memory. Structured prune, sync collision policy and backup replacement can separately retain/remove/reintroduce content. No evaluated claim-truth oracle is established. [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle), [MEM-RTE-consolidation-plan](#mem-rte-consolidation-plan), [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery) and [MEM-RTE-retained-export](#mem-rte-retained-export).

**Derived selection state.** File parsing/indexing and vector refresh transform representations, not authored propositions or trained provider parameters. Retrieval context can improve findability while being omitted from delivered claims. Exact provider initialization provenance remains unresolved locally; known later derivation and cache invalidation are established separately. [MEM-OBJ-retrieval-context](#mem-obj-retrieval-context), [MEM-OBJ-wiki-cache](#mem-obj-wiki-cache), [MEM-OBJ-semantic-index](#mem-obj-semantic-index).

## Read-back

Request paths reload retained memory/wiki through CLI/MCP/HTTP; humans and agents can use full context, explain, catalog/backlinks or direct Markdown. Focused memory, generic wiki, rich packet and capsule expose different content and trust metadata. Plain store APIs alone are not asserted as later agent routes: the supplied adapters establish callers; local HTML/audit exports establish documented reader roles only, not deployed external wiring. [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), [MEM-RTE-wiki-read](#mem-rte-wiki-read), [MEM-RTE-retained-export](#mem-rte-retained-export).

Push paths operate independently: session start and first eligible MCP response select active/project-aware brief content plus review/handoff state; prompt guard selects one strongly overlapping saved constraint and checks cooldown. The host receives text by hook stdout or tool response. Host model context eviction/isolation is not Link's responsibility. Source is retained out of the first packet by code budget and can return through explicit follow-up; no separate agent frame or automatic reference dereference is established. [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery), [MEM-RTE-guard-reminder](#mem-rte-guard-reminder).

Update consumers differ from agent consumers. Manifests, hashes, fingerprints, usage times and journal markers shape adapter replacement, suppression, cooldown and recovery. Agents instead receive selected claims, summaries, instructions and provenance. Receiving a path or a review label does not establish reading source rationale; only explanation/raw inspection offers the fuller retained reasoning. Rich delivery establishes capacity, not reliance or benefit. [MEM-RTE-usage-feedback](#mem-rte-usage-feedback), [MEM-RTE-capture-cleanup](#mem-rte-capture-cleanup), recovery/structured annotations and [RT-BAP-context-packet](runtime.md#rt-bap-context-packet).

## Integration issues

1. **Narrow the baseline's selection/withdrawal scope.** [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) says lifecycle/project filters select retained material, and its ordinary invocation describes a combined packet. [MEM-RTE-wiki-read](#mem-rte-wiki-read) establishes that those filters belong to focused memory, not generic wiki search/graph. Source: SRC-1, `mcp_package/link_core/wiki.py`, `mcp_package/link_core/search.py`, `mcp_package/link_core/query.py`. Consequence: archive/expiry/project filtering is not an all-path delivery guarantee; generic page excerpts can also lack memory-specific warnings. This is a supported scope correction, not a claim of an observed incident.
2. **Changed body is not necessarily changed compact claim.** [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle) appends without TLDR recomputation; [MEM-OBJ-memory-claim](#mem-obj-memory-claim) and recall annotation show slim/compact display. Source: SRC-1, `mcp_package/link_core/memory.py`, `mcp_package/link_core/query.py`. Consequence: later match can depend on new text while an ordinary agent sees old summary; temporal eligibility likewise does not reconstruct pre-update body. No supplied runtime fact says otherwise, but reconciliation must retain this limit.
3. **Selector targeting differs by adapter branch.** Slim MCP recall accepts context_path but passes it only to memory mode; brief and query branches shown in SRC-1, `mcp_package/link_mcp/server.py` do not forward it. Shared query also has no context_path parameter. Concerned records: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), [MEM-RTE-wiki-read](#mem-rte-wiki-read). Consequence: advertising a path fence does not establish matched-context selection on all recall modes. CLI temporal options and MCP focused options are also not identical.
4. **Consolidation parity is incomplete.** CLI supplies merge_candidates; slim MCP review-consolidate does not in the inspected dispatch. [MEM-RTE-consolidation-plan](#mem-rte-consolidation-plan), SRC-1, `link.py`, `mcp_package/link_mcp/server.py`. Consequence: no shared autonomous semantic-merge route or identical plan content should be inferred from the common label.
5. **Evaluation claims need mode-local limits.** [MEM-RTE-memory-evaluation](#mem-rte-memory-evaluation) shows authored synthetic oracle, automatic simulated supersession and warning-based poisoning outcomes. [RT-RTE-recall-evaluation](runtime.md#rt-rte-recall-evaluation) covers a distinct target-rank evaluator. SRC-1, `scripts/eval_memory_hygiene.py`, `scripts/eval_memory_poisoning.py`. Consequence: neither proves actual review-gate compliance, arbitrary attack resistance or end-to-end answer quality; all-path generic wiki withdrawal is outside the tested helper path.
6. **Accounting labels exceed the measured fact.** [MEM-RTE-usage-feedback](#mem-rte-usage-feedback), [MEM-OBJ-usage-ledger](#mem-obj-usage-ledger), SRC-1, `mcp_package/link_core/usage.py`, `mcp_package/link_core/memory_wins.py`. Consequence: retrieved/surfaced is not read/used; bounded history cannot support literal never-use across the whole lifetime. Salience's reported nonadoption is not a reproduced causal finding.
7. **Included uninspected parts remain local limits.** Table names detailed import/structured/seed rendering, HTTP/Swift presentation, digest, other evaluators and validation/test internals. Their exact semantic preservation, presentation parity and measured outcomes remain unresolved; available source is not an access gap. External provider weights, host behavior and external QA judgments are genuine supplied-evidence gaps. Concerned records: runtime import/seed/structured/context/session/evaluation routes and [MEM-RTE-memory-evaluation](#mem-rte-memory-evaluation). Reconciliation must not convert these limits to absence.

Possible duplicates: none proposed after comparison with supplied records. Each contained part carries Part of; new lifecycle, feedback, planning, export and governance-evaluation routes have distinct endpoints/results from their closest supplied routes. No record is redeclared merely under a new prefix. Existing runtime records receive memory annotations. Source-native memory/wikified outputs spanning several routes remain valid shared objects, not proposed replacements for those routes.

## Limitations and checks

Source pin recheck passed. Governing job, supplied member types, boundary/runtime, collection, worker rules and records contract were read completely, including all bounded ranges. Added source reads remain inside SRC-1 at the reviewed commit; implementation versus doctrine versus reported operation is identified above. Searches that named nonexistent auxiliary filenames returned errors; those guesses were replaced with the actual core/scripts inventory, not treated as absence evidence. No prior analyses, target execution or unauthorized writes used.

No actual corpus, transcript, installed integration, provider weights or observed model actions are supplied. Wiring does not establish activation, learning benefit, autonomy, reflection or self-improvement. Existing runtime theory conditions remain independent; no formulated theory was invented from a page template. Source quotes support bounded mechanisms, not exhaustive correctness. Export/recovery/cache persistence prevents a blanket erasure claim; budget estimates prevent an exact host-token-cap claim.

Validation: invocation-specific `commonplace-run validate-output` passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” It checks structure and quotation occurrence, not analytical correctness or job acceptance.
