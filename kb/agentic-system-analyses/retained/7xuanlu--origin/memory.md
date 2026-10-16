---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Origin memory: daemon-owned captures, derived retrieval channels, page review and Space Brief handoff at the frozen Wenlan revision."
run-id: AAS-2026-10-15-origin-805d03bc599f-01
source-identity: https://github.com/7xuanlu/origin
reviewed-boundary: "61b462ea6adf019b3e27d3f58ac5a0fe055f76b1"
---

# Origin memory report

## Boundary and evidence

Origin is branded Wenlan in SRC-1. The [boundary](boundary.md) fixes the whole-system scope and frozen commit. This member includes capture, imported conversations and documents, database representations, automatic enrichment, pages and their Markdown projections, revision/refinement review, Space Briefs, queued writes, retrieval projections, cleanup and evaluation context. It excludes the enclosing agent's private transcript, host compaction, provider-internal memory and deployed credentials from positive conclusions: those implementations and live states are not supplied.

The runtime is a supplied implementation account, not execution evidence. Direct reads added SRC-1 implementation coverage of `crates/wenlan-core/src/db.rs` schema, retrieval, episode/fact co-writes, summaries, revisions, deletion, decay and eviction; `crates/wenlan-core/src/db/brief.rs`; `crates/wenlan-server/src/brief_routes.rs`, `source_routes.rs`, `outbox.rs`; `crates/wenlan-core/src/ingest.rs`, `post_ingest.rs`, `chat_import/mod.rs`, `chat_import/bulk_ingest.rs`, `synthesis/recaps.rs`, `synthesis/decision_logs.rs`, `synthesis/refinement_queue.rs`, `post_write/page_revision.rs`, `refinery/summary.rs`, `refinery/mod.rs`, `retrieval/compress.rs`, `eval/runner.rs`, `eval/answer_quality.rs`; MCP projections and CLI command inventory. Direct doctrine/design reads added `plugin/skills/handoff/SKILL.md`, `plugin/skills/brief/SKILL.md`, `plugin/skills/curate/SKILL.md`; direct hook reads covered `plugin/hooks/hooks.json` and `plugin/hooks/check-daemon.sh`. None establishes observed operation or benefit.

### Coverage inventory

“Supplied” means reliance on the named runtime record, including its evidence passages. “Direct” means source read here; unresolved entries remain included, not silently excluded.

| Entry point / retained part | Source path(s), SRC-1 | Coverage and remaining limit |
| --- | --- | --- |
| MCP capture; batch and synchronous admission | `crates/wenlan-mcp/src/tools.rs`; `crates/wenlan-server/src/memory_routes.rs` | Supplied [RT-RTE-capture-store](runtime.md#rt-rte-capture-store); direct projection check. [MEM-OBJ-memories](#mem-obj-memories) separates content from control metadata. |
| CLI capture, recall, Brief, pages, sources, curate, outbox | `crates/wenlan-cli/src/main.rs` | Direct command inventory; dispatch details supplied by runtime for recall. Pages/editor and entity commands are available but not fully traced; no universal CLI admission claim. |
| SessionStart hook; handoff and resume skills | `plugin/hooks/hooks.json`; `plugin/hooks/check-daemon.sh`; `plugin/skills/handoff/SKILL.md`; `plugin/skills/brief/SKILL.md` | Direct: health/version/outbox notices are not automatic knowledge injection. [MEM-RTE-brief-handoff](#mem-rte-brief-handoff) is the separate instructed session route. Generated Codex skill parity is uninspected. |
| Conversation import | `crates/wenlan-core/src/chat_import/mod.rs`; `crates/wenlan-core/src/chat_import/bulk_ingest.rs` | Direct [MEM-RTE-import-inputs](#mem-rte-import-inputs): paired mixed-role content, dedup and whole-conversation flush. Individual vendor parser fidelity and all subsequent import distillation stages uninspected. |
| Directory/OKF and Obsidian sync | `crates/wenlan-server/src/source_routes.rs`; `crates/wenlan-core/src/sources/directory.rs` | Direct sync handler and directory producer search; [MEM-RTE-import-inputs](#mem-rte-import-inputs). Directory queue preparation, DOCX/PDF extraction, OKF semantics and deletion propagation not fully traced. Cannot claim complete source fidelity or uniform store gate. |
| Classification, extraction, title and page growth | `crates/wenlan-core/src/ingest.rs`; `crates/wenlan-core/src/post_ingest.rs` | Direct [MEM-RTE-enrichment-slices](#mem-rte-enrichment-slices); supplied [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work). Entity extraction/linking and all page-growth internals remain partial. |
| Recaps and decision logs | `crates/wenlan-core/src/synthesis/recaps.rs`; `crates/wenlan-core/src/synthesis/decision_logs.rs` | Direct [MEM-RTE-burst-recaps](#mem-rte-burst-recaps). Raw-context bodies and generated summaries differ; not all summaries reach standard MCP. |
| Summary rollup and root | `crates/wenlan-core/src/refinery/summary.rs`; `crates/wenlan-core/src/db.rs` | Direct [MEM-RTE-summary-rollup](#mem-rte-summary-rollup); opt-in deep retrieval prelude, not default universal retrieval. |
| Episodes and fact-child vectors | `crates/wenlan-core/src/db.rs` | Direct [MEM-OBJ-episode-rows](#mem-obj-episode-rows), [MEM-OBJ-fact-children](#mem-obj-fact-children); opt-in co-writes and cross-rerank consumers. Full child ranking and backfill implementation not audited. |
| Pages, source lineage, edits, refresh and prompt overrides | `crates/wenlan-core/src/synthesis/distill.rs`; `crates/wenlan-core/src/post_write/page_update.rs`; `crates/wenlan-core/src/sources/page_watcher.rs`; `crates/wenlan-core/src/prompts/mod.rs` | Supplied [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh), [RT-RTE-filesystem-edit](runtime.md#rt-rte-filesystem-edit), [RT-RTE-prompt-override](runtime.md#rt-rte-prompt-override); direct snippet-cap and revision-card checks. All page creation/merge writers not audited. |
| Memory/page revisions; refinement queue | `crates/wenlan-core/src/post_write/page_revision.rs`; `crates/wenlan-core/src/synthesis/refinement_queue.rs`; `crates/wenlan-core/src/db.rs` | Direct [MEM-RTE-review-decisions](#mem-rte-review-decisions). Lint-repair-specific proposals, vocabulary promotion and cross-space action internals remain unresolved; explicit review instructions do not establish API-enforced human approval. |
| Recall, Brief related context, direct page/source access | `crates/wenlan-server/src/memory_routes.rs`; `crates/wenlan-server/src/brief_routes.rs`; `crates/wenlan-mcp/src/tools.rs` | Direct projections/Brief; supplied [RT-RTE-recall-search](runtime.md#rt-rte-recall-search). MCP exposes page sources and revision reads; full UI/detail/query-only projections and truth-grant internals uninspected. Cannot infer every client receives identical provenance. |
| Access history, decay, rejection pruning, soft eviction and forget | `crates/wenlan-core/src/db.rs`; `crates/wenlan-core/src/refinery/mod.rs` | Direct [MEM-OBJ-access-state](#mem-obj-access-state), [MEM-RTE-withdrawal-cleanup](#mem-rte-withdrawal-cleanup). No production caller found for access-count flushing in bounded search; read history alone is not learning. |
| Lint diagnostics, agent work packets, repair prepare/apply/verify | `crates/wenlan-mcp/src/tools.rs` | Direct bounded agent-work pagination and local-only repair entry gates. Manifest transaction, retained repair reasons and later repair consumers remain uninspected; prevents generalizing canonical page-update guarantees to repair. |
| Evaluation and read-time compression | `crates/wenlan-core/src/eval/runner.rs`; `crates/wenlan-core/src/eval/answer_quality.rs`; `crates/wenlan-core/src/retrieval/compress.rs` | Direct [MEM-RTE-eval-compression](#mem-rte-eval-compression). Other evaluator modes and private caches uninspected/unavailable respectively. No inference of production adaptation from benchmark reports. |
| Graph/entities, communities, detection, reweave, emergence, overview, page maps and KG rethink | `crates/wenlan-core/src/refinery/phase.rs`; `crates/wenlan-core/src/refinery/mod.rs`; `crates/wenlan-core/src/db.rs` | Direct phase inventory and selected DB dependency cleanup. Detailed graph transformations, ontology/vocabulary payloads and all retrieval contributions remain uninspected. They are included operative alternatives, not evidence of absent mechanisms. |
| Remote MCP/relay; native/frontend consumers; provider state | `crates/wenlan-mcp/src/tools.rs`; `relay/src/worker.ts`; `app/src/api.rs`; `src/lib/tauri.ts`; `crates/wenlan-core/src/llm_provider.rs` | Supplied [RT-RTE-remote-query](runtime.md#rt-rte-remote-query) and provider component records. Live grants, host interpretation, hidden provider state and complete UI mutation wiring remain unknown. |

## Core ideas

1. **The store retains multiple representations, not one authoritative summary.** Text and structured fields coexist with original-source text, dense vectors and symbolic lineage. Episodes preserve a redacted input alternative; child vectors retrieve the parent rather than become independent user facts. Recaps keep burst context in their bodies. A display label such as “memory” or “recap” does not establish what a later model actually receives ([MEM-OBJ-memories](#mem-obj-memories), [MEM-OBJ-episode-rows](#mem-obj-episode-rows), [MEM-RTE-burst-recaps](#mem-rte-burst-recaps)).
2. **Current project state has a separate authority path.** A typed database Brief, not its Markdown receipt or chronological session log, is the shipped handoff/resume authority. The external agent authors deltas from session evidence; software admits exact-ID/version operations. This is an instructed trace-to-retained-state route without per-item user approval, not demonstrated learning ([MEM-RTE-brief-handoff](#mem-rte-brief-handoff)).
3. **Admission and withdrawal are representation-specific.** Pending memory revisions, manufactured page revision cards, refinement proposals and soft-evicted rows have different terminal effects. Dismissing a memory revision preserves a newly independent capture; dismissing a page card deletes it. Rejecting a refinement can terminate its workflow without removing the underlying content ([MEM-RTE-review-decisions](#mem-rte-review-decisions), [MEM-RTE-withdrawal-cleanup](#mem-rte-withdrawal-cleanup)).
4. **Context control occurs before and after retrieval.** Queries and scopes select retained candidates; deep retrieval can add summaries/episodes/children; MCP drops some fields; synthesis caps source snippets before inference. The compression helper has an evaluator consumer, but the bounded call-site search does not establish a production recall consumer. None of these is evidence of host transcript compaction ([RT-RTE-recall-search](runtime.md#rt-rte-recall-search), [MEM-RTE-eval-compression](#mem-rte-eval-compression)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memories
Label: memories

SRC-1, `crates/wenlan-core/src/db.rs`: libSQL rows retain natural-language content/title/summary/source text, symbolic type/space/version/confirmation/supersession/provenance fields, JSON structured fields and distributed dense embeddings. The parts have different consumers: prose supplies knowledge context; symbolic fields govern eligibility and mutation; vectors supply similarity. Structured values can be rendered into prose or split into fact children; their authority is consumer-relative. Initial content can be human, agent or imported mixed-role text; source-agent labels do not independently authenticate origin. Subsequent model enrichment is separately known even where initial authorship is unknown.

Closest supplied records are [RT-RTE-capture-store](runtime.md#rt-rte-capture-store) and [RT-RTE-recall-search](runtime.md#rt-rte-recall-search), routes rather than declarations of this stored object. This object spans both and is not a part of exactly one. It is distinct from [RT-OBJ-prompt-registry](runtime.md#rt-obj-prompt-registry): knowledge content is not the task-instruction registry.

>     structured_fields TEXT,
>     retrieval_cue TEXT,
>     source_text TEXT,
> --- `crates/wenlan-core/src/db.rs:4194-4196`

The standard MCP `RecallHit` delivers content, title, score, identity, version, confirmation and selected lineage/delta fields, but not `source_text`, `structured_fields` or the separate `summary` field (SRC-1, `crates/wenlan-mcp/src/tools.rs`). Thus retained original material is not necessarily the readable tool result. Dense embeddings are derived from text using [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding); exact deployed model bytes and all historical embedding provenance are unresolved, not inferred from vector presence.

#### MEM-OBJ-episode-rows
Label: episode rows

SRC-1, `crates/wenlan-core/src/db.rs`: optional `source='episode'` rows carry PII-redacted `source_text`, falling back to content, subject to a word gate. They share the parent logical source ID, have a deterministic physical ID and `episode_of`, inherit parent metadata and carry separately embedded text. Natural-language near-verbatim content and symbolic parent linkage are separate operative parts. This is an input-preserving retrieval alternative, not a synthesized summary or an unrestricted raw transcript archive. For imports/seed paths without source text, “verbatim” refers to the available content, not necessarily the original export.

Distinct from [RT-RTE-capture-store](runtime.md#rt-rte-capture-store): co-write is in core upsert, also usable by eval/library callers, and bypasses the server quality gate by construction. Write and read are opt-in. Base retrieval explicitly excludes episode rows; the cross-rerank path adds an episode stream. Co-write replaces stale episodes for the source on re-upsert. Full edge-case invalidation/backfill coverage remains uninspected.

>     let verbatim = redact_pii(source_text.unwrap_or(content));
> --- `crates/wenlan-core/src/db.rs`

>         filter_conditions.push("c.source != 'episode'".to_string());
> --- `crates/wenlan-core/src/db.rs`

#### MEM-OBJ-fact-children
Label: fact children

SRC-1, `crates/wenlan-core/src/db.rs`: opt-in upsert creates a narrative child and coercible structured-field children, with deterministic IDs, natural-language child text, symbolic parent/field identity and numerical embeddings. The children are retained retrieval indexes in libSQL; they are not independent admissions of new user knowledge. Cross-rerank fact-channel hits rehydrate the parent. Old child rows are replaced within the parent write transaction. Their lexical field rendering is derived from content/structured values; provenance behind caller-supplied values remains as uncertain as the parent.

Closest supplied record [RT-RTE-recall-search](runtime.md#rt-rte-recall-search) describes the outer consumer route, not this core child representation. It is distinct from the raw episode alternative and from [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding), which supplies the embedding mechanism rather than these stored outputs. Full ranking/field coercion and backfill paths remain uninspected.

>         // child per coercible structured field ("key: value"). Each child
>         // rehydrates to its PARENT memory (parent_id = doc.source_id,
>         // parent_kind = 'memory') so retrieval credit flows through the parent's
>         // own source_id (metric-honest). Child id = sha256(parent_id + field)[..16]
> --- `crates/wenlan-core/src/db.rs`

#### MEM-OBJ-space-brief
Label: Space Brief

SRC-1, `crates/wenlan-core/src/db/brief.rs`: durable libSQL `briefs`, `brief_items` and operation receipts retain last-session summary, active/backlog item prose, stable IDs, versions, states, gates and update receipts. Prose is natural language interpreted by humans/agents; symbolic identities and expected versions control updates. Session evidence is summarized by the external agent, not necessarily by the daemon model. A Markdown projection is a derived human receipt, not the reload authority; a chronological session log is another artifact. No supplied runtime object declares this referent; [RT-RTE-recall-search](runtime.md#rt-rte-recall-search) is a different query route.

> The daemon Brief is current-work authority. Its
> `~/.wenlan/sessions/_status/<space>.md` projection is a one-way human receipt.
> Never read, edit, or overwrite that receipt as authority.
> --- `plugin/skills/handoff/SKILL.md`

Read-back and mutation: [MEM-RTE-brief-handoff](#mem-rte-brief-handoff). Static instructions request authority at the external agent; they do not prove compliance or establish semantic correctness of the snapshot.

#### MEM-OBJ-summary-nodes
Label: summary nodes

SRC-1, `crates/wenlan-core/src/refinery/summary.rs`, `crates/wenlan-core/src/db.rs`: natural-language bucket and root bodies, titles, dense embeddings and symbolic source associations persist as `summary_nodes` and `summary_node_sources`. Buckets derive from retained memory groups; root provenance is the union of bucket source IDs, while its textual input is bucket titles. Stored associations preserve derivation pointers, not complete reasons for every generated statement. Code can fall back to deterministic templates. Later opt-in cross-rerank retrieval selects a prelude; source deletion removes dependent nodes. Distinct from pages in [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh): different tables, admission and deep-read placement. Route: [MEM-RTE-summary-rollup](#mem-rte-summary-rollup).

>     // Root rollup over the bucket titles.
>     let root_sources = union_sources(bucket_source_sets.iter().map(|v| v.as_slice()));
>     let (root_title, root_body) = summarize_root(llm, &bucket_titles).await;
> --- `crates/wenlan-core/src/refinery/summary.rs`

#### MEM-OBJ-revision-cards
Label: page revision cards

SRC-1, `crates/wenlan-core/src/post_write/page_revision.rs`: manufactured page-update proposals are stored in the memory substrate, but a page card is not an ordinary newly captured fact. Natural-language proposed prose has symbolic page identity/control payload; a review display is not the complete machine payload. The dispatcher resolves cards before ordinary memory revision logic. Consumers are page acceptance/dismissal and review surfaces, not unconditional page replacement. Detailed card serialization, stale-card acceptance fences and all display projections are uninspected here.

Part of: [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh)

The parent is a route; this object is its durable staged-result part, with distinct terminal treatment from an accepted page. [MEM-RTE-review-decisions](#mem-rte-review-decisions) covers the shared review dispatcher.

>     if let Some(card) = resolve_page_revision_card(db, id).await? {
>         db.delete_by_source_id("memory", &card.revision_id).await?;
> --- `crates/wenlan-core/src/post_write/page_revision.rs`

#### MEM-OBJ-access-state
Label: access and maintenance state

SRC-1, `crates/wenlan-server/src/memory_routes.rs`, `crates/wenlan-core/src/db.rs`: the recall handler stores selected memory IDs in `access_log` and query/activity history; page rows are excluded from those memory IDs. This is raw symbolic usage metadata with optional natural-language query, not derived knowledge. Separate `access_count`, `last_accessed`, confidence and stability fields feed decay; effective confidence feeds optional eviction. They are not interchangeable with access-log entries. `log_accesses` inserts log rows; `flush_access_counts` separately updates count/time. A repository search under `crates` and `app/src` found only definition/test callers of the latter, preventing a claim that ordinary production recall increments these fields through that function. This bounded finding is not a system-wide absence assertion.

Closest supplied route [RT-RTE-recall-search](runtime.md#rt-rte-recall-search) establishes log persistence; this object spans logging and maintenance, not exactly one route. No retained content revision is inferred from logging. [MEM-RTE-withdrawal-cleanup](#mem-rte-withdrawal-cleanup) traces the known maintenance consumer and its gap.

>                     "UPDATE memories SET access_count = COALESCE(access_count, 0) + 1, last_accessed = datetime('now') WHERE source_id = ?1",
> --- `crates/wenlan-core/src/db.rs`

### Routes

#### MEM-RTE-brief-handoff
Label: Handoff deltas and later Brief read

Owner: the host agent following handoff/brief instructions proposes session-derived summary and typed changes; the daemon validates and commits them. Open session-close/resume workflow, no answer oracle. The user initiates handoff but the skill explicitly says not to seek approval for ordinary Brief changes/captures. This is not per-content human approval. Software can reject invalid requests, detect changed-operation-ID reuse, and return version conflicts. Same-ID matching retries return the retained receipt. Existing-item deltas use exact IDs; the DB can commit nonconflicting changes while recording conflicts. Recovery is reread/reconcile or typed replacement, not transcript rollback. SRC-1, `plugin/skills/handoff/SKILL.md`, `plugin/skills/brief/SKILL.md`, `crates/wenlan-core/src/db/brief.rs`, `crates/wenlan-server/src/brief_routes.rs`, `crates/wenlan-server/src/outbox.rs`.

No supplied counterpart after comparison with [RT-RTE-recall-search](runtime.md#rt-rte-recall-search): Brief read uses a Space-owned snapshot, adding separate topic context only when requested. The queued-write leg is an alternative admission path, not another knowledge authority.

- Immediate return: typed receipt with applied/conflicted changes, version, projection path/warnings; CLI offline result can instead mean queued, not committed.
- Later read-back: a later Brief request reloads the database summary and complete active/backlog state for the resolved Space; handoff also reads it before authoring existing-item changes.
- Delegated visibility: external agent receives snapshot text and item IDs/versions; optional user topic invokes same-Space memory search as separately labelled related context. Session log and Markdown receipt are not substituted as authority by the instructions.
- Selection predicate: explicit/configuration/repository Space resolver; no topic means no related search. Topic search uses server limit and truth-grant filtering of page rows. Update predicates use caller/operation identity and expected versions, not fuzzy text matching.
- Invalidation or expiry: later deltas supersede snapshot fields; complete removes an item. Offline outbox replay can reconcile summary expected_version to the current Brief, a deliberately weaker stale-summary boundary than an online snapshot CAS. No fixed Brief expiry is established.
- Activation or effect: DB snapshot and receipt projection writes are wired; later agent priority/continuation authority is instructed, not observed.
- Evidence limits: session interpretation is external; log creation and user-visible skill behavior are doctrine, not observed executions. Full outbox filesystem lifecycle and deployed replay are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>     let mut receipt = db.apply_brief_update(&request).await?;
> --- `crates/wenlan-server/src/brief_routes.rs`

>                     summary.expected_version = current_version;
> --- `crates/wenlan-server/src/outbox.rs`

The handoff skill asks for bounded Git/conversation evidence, a chronological session log before Brief update, then atomic durable captures. The retained behavioral result is the Brief and captures, not proof that the session log itself has an automatic later reader. The narrative log preserves reasons only to the extent the agent writes them; the normal Brief consumer receives the summary/items, not the entire log.

#### MEM-RTE-import-inputs
Label: Conversation and source input admission

Owner: importing caller supplies exports or configured file sources; core/server code selects and stores input. These are acquisition routes distinct from [RT-RTE-capture-store](runtime.md#rt-rte-capture-store), not proved to share its gate. Chat pairing combines adjacent user/assistant messages and skips unmatched messages. Bulk ingest deduplicates conversations and flushes whole conversations as units. Vault sync uses mtime/hash skipping, document conversion, content-quality checks and upsert; fully filtered files are not marked synced, permitting later retry. Directory/OKF sync instead queues work and requests import priority. SRC-1, `crates/wenlan-core/src/chat_import/mod.rs`, `crates/wenlan-core/src/chat_import/bulk_ingest.rs`, `crates/wenlan-server/src/source_routes.rs`.

Admission is software parsing/dedup/filtering, not demonstrated item-by-item human review. Human source authorship and import initiation do not mean approval of every retained pair. No answer oracle; open import/synchronization mode. Failure returns counts/errors or leaves input retryable; full vendor parser and directory queue recovery remain uninspected.

- Immediate return: import counts/progress or sync counts, skips, errors and queued work; not a promise that every input has been distilled.
- Later read-back: durable raw-import entries/documents become available to later processing and retrieval; full import-to-distilled-memory selector chain remains uninspected.
- Delegated visibility: initial bulk ingestion writes supplied text without doing classification/extraction/distillation itself; later model visibility depends on a later stage, not the import label.
- Selection predicate: supported parsed conversations and unseen vendor/source IDs; paired messages; configured source scope, changed mtime/hash, conversion and content quality for the inspected vault branch.
- Invalidation or expiry: repeat conversation IDs are skipped; changed source files can re-enter sync. Directory disappearance/deletion propagation and edits to already imported conversations are not fully traced.
- Activation or effect: input retention and queue admission are wired; eventual organization and useful recall unobserved.
- Evidence limits: full parser fidelity, roles across all vendor exports, all source formats and downstream import enrichment are uninspected; “raw” is relative to the parser output.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>                 content: format!("User: {}\nAssistant: {}", user.content, asst.content),
> --- `crates/wenlan-core/src/chat_import/mod.rs`

>         memories_stored += db.store_raw_import_memories_batch(&entries).await?;
> --- `crates/wenlan-core/src/chat_import/bulk_ingest.rs:195-195`

#### MEM-RTE-enrichment-slices
Label: Durable enrichment slices

Part of: [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work)

This is the stage-specific transformation part of the scheduler route, not a second scheduler. SRC-1, `crates/wenlan-core/src/ingest.rs`, `crates/wenlan-core/src/post_ingest.rs`. Code selects durable candidates; a model proposes classification, structured extraction or title text under registry instructions; version-aware commit code admits derived fields. Explicit caller fields constrain what classification may replace. Initial author control can be unknown while these later software/model transformations are known. No per-item human veto or answer oracle appears in the inspected slice; operating mode is automatic organization. Failure receipts record retry/abandon against input version, with shared maximum of three attempts. Title generation can reject output before commit. Page-growth matching/writing is a further stage, only partially read here; supplied page refresh remains the authority for its traced gate, not for every enrichment write.

- Immediate return: selected/committed/call counts or failure/retry report to scheduler, not immediate generated content to the capture caller.
- Later read-back: derived type, space, importance, quality, tags, structured fields/cue/dates and title persist on memory state and can influence later retrieval/maintenance; full field-by-field ranking effects remain uninspected.
- Delegated visibility: classification sees the first 1000 content characters and task prompt; structured extraction is a separate selected frame, not the whole host conversation. Omitted text remains in the store.
- Selection predicate: durable stage candidate and attempt bound; explicit type protected; derived space only when absent, not previously rejected, and registered. Commit checks input generation; title checks its snapshot.
- Invalidation or expiry: concurrent content generation can defeat commit; versioned receipts constrain retry. Later writes may create new eligible generations. No general TTL.
- Activation or effect: derived state and stage receipts are wired; model judgments are not semantic truth guarantees, and future answer effects are unobserved.
- Evidence limits: parser/commit internals, complete page-growth, entity extraction and imported-raw transformations are not exhaustively traced. This is a trace-fed write when its selected input originates in captured conversation, not proof of improved capacity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         user_prompt: input.content.chars().take(1000).collect(),
> --- `crates/wenlan-core/src/ingest.rs`

> pub(crate) const ENRICHMENT_MAX_ATTEMPTS: u32 = 3;
> --- `crates/wenlan-core/src/post_ingest.rs`

#### MEM-RTE-burst-recaps
Label: Burst recaps and decision logs

Part of: [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work)

SRC-1, `crates/wenlan-core/src/synthesis/recaps.rs`, `crates/wenlan-core/src/synthesis/decision_logs.rs`: automatic recent-memory selectors group activity bursts, skip insufficient/already covered bursts, and generate summary text or deterministic fallbacks. Model guidance is `detect_pattern`/`summarize_decisions`, not a supplied expected answer. Code admits nonempty/non-null response with think-tag stripping or fallback; it upserts a recap fact/decision without item-level human approval. Recap title generation is another call in this implementation; scheduler budgeting may limit which calls succeed. This is retained aggregation, not necessarily new explanatory knowledge.

- Immediate return: generated count/phase result to maintenance caller.
- Later read-back: recap rows enter the memory substrate and later memory retrieval subject to ordinary eligibility/scoring; retained body is burst context, not merely the generated summary. Recaps also store source IDs for detail display; decision-log constructor shown does not add that same structured source-ID field.
- Delegated visibility: model receives selected burst contents, with space labels; standard MCP later returns content/title but omits the separate summary field. It therefore need not deliver the generated recap summary verbatim.
- Selection predicate: configured lookback and minimum burst size, recent cap 100 for recaps and 50 for decision inputs, temporal grouping and recap-range coverage check.
- Invalidation or expiry: covered ranges suppress repeat generation; complete dependent-recap invalidation after source edits/deletion is uninspected, so no guarantee that all old recap prose is withdrawn with an original.
- Activation or effect: raw-to-derived summary plus retained raw-context body is wired; later agent reliance/benefit unobserved.
- Evidence limits: inputs can mix human/model/agent-derived content; source-agent `refinery` identifies the transformer, not original experiential provenance. No semantic summary gate beyond the inspected acceptance/fallback checks is established here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>                     (cleaned.trim().to_string(), raw_context)
> --- `crates/wenlan-core/src/synthesis/recaps.rs`

>         // Track source memory IDs so the detail view can show exact sources
>         let source_ids: Vec<&str> = burst.iter().map(|(id, _, _, _)| id.as_str()).collect();
> --- `crates/wenlan-core/src/synthesis/recaps.rs`

#### MEM-RTE-summary-rollup
Label: Summary rollup and prelude reuse

Part of: [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work)

SRC-1, `crates/wenlan-core/src/refinery/summary.rs`, `crates/wenlan-core/src/refinery/mod.rs`, `crates/wenlan-core/src/db.rs`: opt-in SummaryRollup builds bucket/root nodes, preferring model summaries and falling back to deterministic templates. Code, not a human approval step, admits sanitized output meeting lexical overlap floor. No expected-answer oracle; open corpus rollup. This is distinct from the page gate in [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh). Prior nodes are cleared then rebuilt; transaction-wide atomic replacement is not established by this orchestration.

- Immediate return: count of written nodes, or error, to refinery caller.
- Later read-back: opted-in `search_memory_cross_rerank` selects summary nodes and prepends their SearchResult projections outside the reranked memory limit, before memory rows and appended pages.
- Delegated visibility: bucket model sees member titles (content fallback), requests 200 output tokens and has a 15-second timeout; root sees bucket titles. Later caller receives summary body, not a reconstruction of all contributing member contents/reasons.
- Selection predicate: qualifying buckets, minimum membership, provider availability and sanitize/overlap checks; later query/scope retrieval selects root/bucket nodes, configured bucket K defaults to three; active source filters add provenance overlap checks.
- Invalidation or expiry: rebuild clears nodes; source deletion deletes associated summary nodes; source revision acceptance also invalidates summaries. Full stale-read guards and every mutation path remain uninspected.
- Activation or effect: retained rollup-to-prelude chain is wired behind feature/read-path gates; not universal default recall behavior or demonstrated orientation benefit.
- Evidence limits: lexical overlap is not entailment; provider failure falls back to template. Full graph-to-bucket lineage and source visibility correctness are not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>             Some(body) if body_meets_overlap_floor(&body, &member_source) => (tmpl_title, body),
> --- `crates/wenlan-core/src/refinery/summary.rs`

>         out.extend(prelude_rows);
>         out.extend(results);
> --- `crates/wenlan-core/src/db.rs`

#### MEM-RTE-review-decisions
Label: Revision and refinement decisions

Owner: local caller requests accept/dismiss/reject; post-write dispatcher and DB apply typed actions. Shipped curate instructions require unambiguous user choices, but callable APIs do not prove those choices occurred. Open correction/review mode, no reference-answer oracle. SRC-1, `plugin/skills/curate/SKILL.md`, `crates/wenlan-core/src/post_write/page_revision.rs`, `crates/wenlan-core/src/db.rs`, `crates/wenlan-core/src/synthesis/refinement_queue.rs`. Distinct from proposal creation in [RT-RTE-capture-store](runtime.md#rt-rte-capture-store) and [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh); spans both proposal families and refinement actions rather than being a part of one.

- Immediate return: target/revision IDs and wrote outcome, or refinement action receipt/error. A successful contradiction acknowledgement need not rewrite either fact.
- Later read-back: accepted memory revision is activated/confirmed and original suppressed according to supersession rules; dismissed memory revision becomes an independent row. Page-card dismissal deletes the manufactured card; refinement rejection retains terminal proposal status for later queue checks without deleting underlying knowledge.
- Delegated visibility: reviewer can receive proposed/current content and bounded diff; stable revision IDs disambiguate siblings. A bounded display is not proof that all payload fields were inspected by a human.
- Selection predicate: revision identity (exact source ID or legacy target lookup), page-card recognition before ordinary revision handling, pending state and action-specific validation; terminal refinement proposals reject repeat application.
- Invalidation or expiry: memory acceptance invalidates derived dependencies in a DB transaction and rolls back on error; dismissal clears false supersession. Page acceptance/repair and all refinement action rollback contracts remain partial; no universal undo claim.
- Activation or effect: live eligibility/ownership/workflow state changes are wired; review choices and downstream factual improvement unobserved.
- Evidence limits: user-consent rules are instructions, not authenticated API consent. Page card serialization/fence internals and many refinement actions remain uninspected. Generic `detect_contradiction` acceptance acknowledges/resolves, not an automatic truth adjudication.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>              SET pending_revision = 0, supersedes = NULL,
> --- `crates/wenlan-core/src/db.rs`

>         "detect_contradiction" => {
>             // Validate the proposal shape, then acknowledge-and-resolve below —
>             // do NOT mutate either memory. A pure contradiction keeps both facts;
> --- `crates/wenlan-core/src/synthesis/refinement_queue.rs`

#### MEM-RTE-withdrawal-cleanup
Label: Withdrawal and maintenance cleanup

Owner: explicit forget caller initiates deletion; daemon maintenance initiates decay, optional eviction and rejection pruning. SRC-1, `crates/wenlan-core/src/db.rs`, `crates/wenlan-core/src/refinery/mod.rs`. Distinct from capture/review because these change retained eligibility/dependencies rather than admit new capture prose. Software applies deletion/eligibility predicates; pin/confirmation fields can protect against eviction, not explicit forget. No answer oracle or required per-content human approval in automatic maintenance; explicit caller identity alone does not resolve human control. Recovery differs: transactional rollback on failure, clearing soft-eviction state for archive recovery, no demonstrated recovery of successfully deleted content.

- Immediate return: deletion success/error; maintenance counts/phase reports, including archived count with no physical delete in the inspected eviction stage.
- Later read-back: default search excludes `evicted` rows and eligible hide-mode superseded rows; page dependencies are marked source-removed/stale and cite edges retired on deletion; dependent summary nodes, observations, queues, access records and evaluation references are removed. Existing page prose is not shown to be synchronously erased.
- Delegated visibility: maintenance reads symbolic confidence/access/state and dependency identifiers, not a new host transcript. Query clients subsequently receive only eligible current projections; old client copies cannot be retracted by DB cleanup.
- Selection predicate: explicit source kind/ID for forget; eviction flag plus maintenance trigger, confidence/age/cap policy and confirmed/pinned/protected exclusions; rejection log prune uses 30 days.
- Invalidation or expiry: deletion cleans dependencies transactionally; soft eviction retains content while changing `supersede_mode`; rejection receipts expire separately. Full file deletion propagation and every derived recap/graph invalidation are not established.
- Activation or effect: source deletion, eligibility changes and retention policies are wired. Decay consumes count/time fields to store effective confidence, then eviction consumes that value; production recall-to-count flushing linkage is not established by the inspected callers.
- Evidence limits: access-log retention is not evidence of learned knowledge; effective confidence is not a measured truth score. Cleanup does not prove semantic retraction from every derived artifact or external consumer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>                         "UPDATE memories SET supersede_mode = 'evicted' \
>                          WHERE source_id = ?1 AND source = 'memory'",
> --- `crates/wenlan-core/src/db.rs`

>                      SET source_memory_ids = ?1, stale_reason = 'source_removed', refresh_blocked_reason = NULL
> --- `crates/wenlan-core/src/db.rs`

#### MEM-RTE-eval-compression
Label: Evaluator bundle compression

SRC-1, `crates/wenlan-core/src/retrieval/compress.rs`, `crates/wenlan-core/src/eval/answer_quality.rs`: an environment-gated evaluation variant passes assembled retrieval context and question to the compression helper, then supplies returned text to an answer request. Code/model select a representation change, not a different initial search pool. This is distinct from [RT-RTE-recall-search](runtime.md#rt-rte-recall-search) and the source-snippet cap in [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh). In the bounded `crates/wenlan-core/src` search for `compress_context(`, the non-test consumer found was answer-quality evaluation; production use is not established despite module comments referring to a production path.

- Immediate return: compressed trimmed nonempty string, or unchanged input on disabled/no-provider/too-short/error/timeout/empty output paths.
- Later read-back: inapplicable — the inspected compressed string feeds the next answer request in this evaluation; no durable checkpoint and later invocation reload of that string is established.
- Delegated visibility: compressor receives query plus assembled bundle and compression prompt; answering model receives the substituted bundle, not both original and compressed versions.
- Selection predicate: master env gate at evaluation branch; helper tuning enable, minimum characters, provider availability, configured output-token cap and timeout, nonempty output.
- Invalidation or expiry: local per-case string; discarded with evaluation context. Original bundle remains available to fallback code, not necessarily in the answer model's window.
- Activation or effect: request construction is wired; no source-supplied trace inspected here establishes semantic faithfulness, answer change or benefit.
- Evidence limits: no runtime faithfulness/coverage gate in the inspected helper; nonempty truncation or invention may pass. This is working-context control, not demonstrated retained-memory compaction or host-session eviction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>                     user_prompt: format!("Context:\n{}\n\nQuestion: {}", compressed, qa.question),
> --- `crates/wenlan-core/src/eval/answer_quality.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-recall-search](runtime.md#rt-rte-recall-search)

Memory-specific projection: SRC-1, `crates/wenlan-mcp/src/tools.rs`, standard `RecallHit` exposes content and selected metadata, omitting separate summary, structured fields and source text. Thus original reasons retained only in omitted source text are not delivered automatically. Recap raw-context bodies can still carry reasons; provenance/delta fields can remain visible. Query-only projection is separately selected, not assumed identical. Source-dependent semantics remain natural-language knowledge at the external agent, not an enforceable instruction priority. Supplemental page warning explicitly distinguishes unconfirmed AI-written prose; score is relevance, not correctness. Supplied [RT-BAP-recall-skill](runtime.md#rt-bap-recall-skill) requests relevance judgment but supplies no compliance evidence.

>             return query_success(query_output::project_recall(&resp));
> --- `crates/wenlan-mcp/src/tools.rs`

#### On [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh)

Memory lineage: SRC-1, `crates/wenlan-core/src/synthesis/distill.rs`, candidate source snippets are capped to 800 characters before model input. Omitted material remains retrievable by other routes rather than occupying the compilation frame. Accepted page prose and provenance outlive the inference; staged card and page have different consumers. Citation overlap plus source pointers preserves a route to evidence, not all rationale or semantic entailment. [MEM-OBJ-revision-cards](#mem-obj-revision-cards) isolates the staged-result part; [MEM-RTE-review-decisions](#mem-rte-review-decisions) distinguishes dismissal from ordinary capture dismissal.

#### On [RT-OBJ-prompt-registry](runtime.md#rt-obj-prompt-registry)

Memory boundary: defaults are static guidance, not material accumulated through use. File overrides are durable changeable guidance with a loader consumer, but the supplied [RT-RTE-prompt-override](runtime.md#rt-rte-prompt-override) establishes no feedback-driven author of those files. Neither override persistence nor schema field `compress_context` proves operational compaction or an improvement loop. Task guidance is interpreted by providers; symbolic write gates remain separate.

## Write side

Acquisition starts with different principals and gates, not one universal “memory write”: capture uses server validation/trust/quality admission; imports use parser/dedup/sync branches; filesystem page edits are an alternate direct content replacement; core upsert can create derived index channels without rerunning server quality admission. Starting an import or handoff is not per-item approval. See [RT-RTE-capture-store](runtime.md#rt-rte-capture-store), [RT-RTE-filesystem-edit](runtime.md#rt-rte-filesystem-edit), [MEM-RTE-import-inputs](#mem-rte-import-inputs), [MEM-OBJ-episode-rows](#mem-obj-episode-rows), [MEM-OBJ-fact-children](#mem-obj-fact-children).

Automatic organization is known even when input authorship is unresolved. Selected retained content becomes classification/extraction/title, recap summary, rollup or page candidate; code then commits, stages or rejects under the relevant gate. A natural-language summary and a numerical index are different retained consequences of the same input. [MEM-RTE-enrichment-slices](#mem-rte-enrichment-slices), [MEM-RTE-burst-recaps](#mem-rte-burst-recaps), [MEM-RTE-summary-rollup](#mem-rte-summary-rollup) and [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh) cover these differences. Unknown phase internals are listed in the inventory rather than generalized from one successful path.

Trace-derived chains include conversation pairs to stored input to later organization; session conversation/Git evidence to handoff summary/items to later Brief; recent memories to recap summary plus raw-context body to retrieval; grouped memories to summary nodes to optional prelude. These establish implemented/instructed transformations, not measured improved capacity. Original input can mix human decisions, assistant answers and prior derived text. Keeping a `refinery` label does not resolve that mixture. Reasons survive when present in retained source/body/log; a later MCP projection may omit separate source/summary fields. No inspected route automatically feeds the chronological session log itself into the next Brief.

Maintenance/rejection has durable consequences: retry/abandon receipts govern subsequent slices; pending states gate default reads; acceptance changes eligibility; dismissal has object-specific semantics; deletion retires dependencies; soft eviction retains recoverable text; rejection history has a separate 30-day retention. These are not equivalent to deleting all criticized content ([MEM-RTE-review-decisions](#mem-rte-review-decisions), [MEM-RTE-withdrawal-cleanup](#mem-rte-withdrawal-cleanup)). Evaluation seeds isolated per-case databases and evaluates outputs; it is not evidence that production content or task prompts are automatically rewritten from scores (SRC-1, `crates/wenlan-core/src/eval/runner.rs`, `crates/wenlan-core/src/eval/answer_quality.rs`).

## Read-back

The ordinary request route is query/filter/rank/projection/tool delivery to an external agent or human, not an automatic injection of all retained state. Deep cross-rerank may additionally select episode and fact-child channels, prepend rollup summaries and append pages; default base retrieval excludes episodes and evicted/pending rows. Feature presence must not be conflated with default enablement. Standard MCP and CLI summaries are different delivery channels. Direct page/source/revision operations offer additional requested read surfaces; their complete projection contracts remain limited as noted in coverage ([RT-RTE-recall-search](runtime.md#rt-rte-recall-search), [MEM-OBJ-episode-rows](#mem-obj-episode-rows), [MEM-OBJ-fact-children](#mem-obj-fact-children), [MEM-RTE-summary-rollup](#mem-rte-summary-rollup)).

Brief read selects an entire current Space snapshot, not query-ranked fragments; an explicit topic adds a separate search. Handoff rereads the snapshot to target exact items. This provides a specific later consumer, unlike a storage API with no caller. Offline outbox replay is a deferred write consumer, not a substitute read authority ([MEM-RTE-brief-handoff](#mem-rte-brief-handoff)).

Automatic maintenance is a push into stored state, not necessarily unsolicited push into a foreground conversation. The SessionStart hook inspected here emits health/version/outbox notices, not retained knowledge. The shipped Brief skill explicitly says it is not a mandatory every-session boot step (SRC-1, `plugin/hooks/hooks.json`, `plugin/hooks/check-daemon.sh`, `plugin/skills/brief/SKILL.md`). Background selectors, capped compilation snippets and evaluator compression are working-context controls. They isolate per-request task frames: selected input crosses in and a result crosses out, while the complete host transcript never becomes Origin's model frame by default. The stack-frame analogy fits request-local selection/return, but not reference-based liveness: stored omitted text is outside the model window and needs a new retrieval, not a dereference of an in-window pointer. Host compaction policies and sub-agent frames remain external/uninspected.

## Integration issues

1. **Additional route, not a correction to runtime recall:** [MEM-RTE-brief-handoff](#mem-rte-brief-handoff) and [MEM-OBJ-space-brief](#mem-obj-space-brief) add the explicit current-work snapshot path. Runtime's brief mention does not capture typed deltas, one-way receipt authority or offline summary-version reconciliation. These materially qualify any general “all reuse is search” account. Evidence: SRC-1, `crates/wenlan-server/src/brief_routes.rs`, `crates/wenlan-server/src/outbox.rs`, `plugin/skills/handoff/SKILL.md`.
2. **Counterexample to generic rejection semantics:** [MEM-RTE-review-decisions](#mem-rte-review-decisions) distinguishes memory unstage-and-keep, page-card delete and refinement terminal-status-only changes. It complements [RT-RTE-capture-store](runtime.md#rt-rte-capture-store) and [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh), not a duplicate declaration of them. Any synthesis calling all dismissal “discard the memory” needs correction. Evidence: SRC-1, `crates/wenlan-core/src/post_write/page_revision.rs`, `crates/wenlan-core/src/db.rs`.
3. **Compression integration unresolved:** [MEM-RTE-eval-compression](#mem-rte-eval-compression) is the directly located evaluator route; module comments claim shared production use but bounded call-site inspection did not find it. Do not promote [RT-OBJ-prompt-registry](runtime.md#rt-obj-prompt-registry)'s compression field to production activation. Evidence: SRC-1, `crates/wenlan-core/src/retrieval/compress.rs`, `crates/wenlan-core/src/eval/answer_quality.rs`.
4. **Access trace feedback gap:** [MEM-OBJ-access-state](#mem-obj-access-state) and [MEM-RTE-withdrawal-cleanup](#mem-rte-withdrawal-cleanup) establish logging, decay and an eviction consumer, but not production recall-to-count flushing. Comments mention a timer; callers found in bounded `crates`/`app/src` search were tests. This blocks attributing adaptive retention to ordinary recall access alone, without denying known maintenance operations. No correction to [RT-RTE-recall-search](runtime.md#rt-rte-recall-search)'s narrower logging finding.
5. **Parts, not possible duplicates:** enrichment, burst recap and rollup routes are explicit parts of [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work); page cards are the staged-result part of [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh). Other new declarations compare their nearest supplied records in their bodies. No new record is asserted to duplicate a supplied referent.
6. **Included unresolved operations:** full graph/community/vocabulary changes, import distillation and formats, all page/repair writers, stale revision-card acceptance, detailed refinement actions, complete UI/query-only/detail projections, generated Codex parity, dependent recap invalidation and provider-internal state remain as itemized in coverage. They prevent universal admission, lineage, recall-provenance, semantic-withdrawal and client-parity conclusions. Named evidence is available except private/deployed/provider state; absence of inspection is not absence of mechanisms.

No supplied runtime finding requires withdrawal on the inspected evidence. The additions narrow potential extrapolations rather than contradicting its explicitly bounded claims.

## Limitations and checks

The frozen checkout HEAD was rechecked as `61b462ea6adf019b3e27d3f58ac5a0fe055f76b1`, with clean status at initial inspection. Only SRC-1 was used; no prior analyses, external websites, target execution, tests, models or services were consulted. Supplied inputs and governing types/contracts were read completely with bounded ranges; source reads were scoped ranges, not claims of full-file audits. The method is this invocation's pinned worker/record/type procedure, not repository authoring skills. Source findings are implementation or attributed doctrine, not observed operation or causal effectiveness.

Provider states and weights remain external or version-unresolved as recorded in runtime components. Local persistence wiring does not establish crash durability in deployed processes. Content delivery does not establish host obedience; lexical overlap does not establish truth; retained experience transformations do not establish learning, autonomous theory building or exercised self-improvement. The inventory preserves the known unresolved parts beside the conclusions they prevent.

Validation: the invocation's `commonplace-run validate-output` command passed after repairing two ambiguous quote attributions and one incorrectly split comment quotation. Result: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” No finding was narrowed or withdrawn to pass the check.
