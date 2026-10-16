---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Atomic's retained atoms, derived retrieval state, conversation replay, wiki and report consumers, and tag consolidation at the frozen source boundary."
run-id: AAS-2026-10-12-atomic-f98683232831-01
source-identity: "https://github.com/kenforthewin/atomic"
reviewed-boundary: "983bea6baf449d060514c94b3b15b5f85f77ba9b"
---

# Atomic memory report

## Boundary and evidence

Atomic retains a corpus and several derived products, not one interchangeable memory store. This account includes capture and mutation, enrichment, tag consolidation, search, conversation replay, saved answers, wiki publication and report findings. It includes the shipped standalone/cloud drivers and clients identified in [boundary](boundary.md#boundary-and-evidence). External MCP clients' enclosing loops, provider weights and live deployments are outside the inspected implementation. Their exclusion prevents conclusions about downstream client reliance and provider learning.

The source is SRC-1 at the exact reviewed commit above; [boundary's Source register](boundary.md#source-register) supplies its identity. Direct reads extend the provisional runtime with context truncation, history conversion, tag compaction, full-content tagging, SQLite finding transactions, article archives, query filters, saved-answer conversion and a longitudinal evaluator. All findings are implementation evidence unless marked as requested model behavior. No target code, benchmark, example or provider was executed. Operation, activation and benefit remain uninspected.

The coverage table separates direct inspection from supplied findings. Available but uninspected surfaces remain included. Rows naming them do not imply a complete audit.

| Entry point or operation | SRC-1 paths | Record coverage and inspection basis | Missing fact and conclusion prevented |
| --- | --- | --- | --- |
| Core/MCP capture and agent edits | `crates/atomic-core/src/lib.rs`, `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-server/src/mcp/server.rs` | Supplied [RT-RTE-capture-write](runtime.md#rt-rte-capture-write), [RT-RTE-atom-mutation](runtime.md#rt-rte-atom-mutation); direct reader/search and delete reads; [MEM-OBJ-atoms](#mem-obj-atoms) | No semantic source-verification guarantee or universal consent invariant. |
| Browser/mobile/Obsidian/Discord capture, direct CLI imports | `extension/background/service-worker.js`, `mobile/ios/App/ShareExtension/ShareViewController.swift`, `plugins/obsidian-plugin/src/sync-engine.ts`, `plugins/discord/src/core/atomic-client.ts`, `scripts/import/shared/index.js` | Boundary inspection supplied; [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) covers core/import alternatives only | Client retries, deduplication, mapping deletion and user review remain uninspected; prevents treating all capture routes as identical admission/enrichment. |
| Enrichment and graph state | `crates/atomic-core/src/embedding.rs`, `crates/atomic-core/src/extraction.rs`, `crates/atomic-core/src/graph_maintenance.rs` | Direct single-atom enrichment/tagging; supplied graph/dispatch [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance); [MEM-RTE-atom-enrichment](#mem-rte-atom-enrichment) | Batch/re-embedding branches and graph numerical details not fully inspected; no global freshness/completeness conclusion. |
| Tag merge API and library alternative | `crates/atomic-core/src/compaction.rs`, `crates/atomic-core/src/lib.rs`, `crates/atomic-core/src/storage/sqlite/tags.rs`, `crates/atomic-server/src/routes/utils.rs` | Direct reads; [MEM-RTE-tag-compaction](#mem-rte-tag-compaction) | PostgreSQL merge application not inspected; prevents extending SQLite error/retention semantics to both adapters. |
| Search and identifier readers | `crates/atomic-core/src/search.rs`, `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-server/src/mcp/server.rs` | Direct options, scope predicate, RRF, chat formatting and MCP search; [MEM-RTE-corpus-retrieval](#mem-rte-corpus-retrieval) | Full backend SQL and UI stores not audited; prevents exhaustive rank, deletion and backend-parity guarantees. |
| Conversation reload and context | `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/agent_runtime/context.rs`, `crates/atomic-core/src/chat.rs` | Direct conversion/truncation; supplied [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn); [MEM-OBJ-chat-history](#mem-obj-chat-history) | No observed use of prior text; no guarantee that retained tool/citation metadata reaches the next model call. |
| Save answer as atom | `src/components/chat/saveAnswerAsAtom.ts` | Direct complete helper read; [MEM-RTE-answer-save](#mem-rte-answer-save) | Save-button caller and editing UI not inspected; human per-save approval remains unresolved rather than inferred from helper name. |
| Wiki generation/proposal/accept/dismiss and archives | `crates/atomic-core/src/wiki/agentic.rs`, `crates/atomic-core/src/wiki/mod.rs`, `crates/atomic-core/src/lib.rs`, `crates/atomic-server/src/routes/wiki.rs` | Direct budget/archive/read formatting; supplied [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission); [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles), [MEM-OBJ-wiki-proposals](#mem-obj-wiki-proposals), [MEM-OBJ-wiki-versions](#mem-obj-wiki-versions) | Centroid/section-operation strategies, PostgreSQL archive and UI version/restore consumers uninspected; no all-strategy captured-only or full rollback invariant. |
| Report admission, research readers and findings | `crates/atomic-core/src/reports/agentic.rs`, `crates/atomic-core/src/reports/runner.rs`, `crates/atomic-core/src/storage/sqlite/reports.rs` | Direct read_atom/filter and transaction; supplied [RT-RTE-report-finding](runtime.md#rt-rte-report-finding); [MEM-OBJ-report-findings](#mem-obj-report-findings) | Source seeding/token packing, schedule configuration and PostgreSQL transaction detail uninspected; prevents complete context-isolation/exactly-once claim. |
| Maintenance scheduling, ledgers and configuration | `crates/atomic-server/src/main.rs`, `crates/atomic-cloud/src/dispatcher.rs`, `crates/atomic-core/src/lib.rs` | Supplied [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) | Claims/leases/GC, capabilities cache, task traces, quotas and dirty-watermark recovery not fully inspected; not treated as model-readable knowledge. |
| Delete/reset/backup/account removal | `crates/atomic-core/src/storage/sqlite/atoms.rs`, `crates/atomic-core/src/lib.rs`, `scripts/reset-chunks.js`, `scripts/reset-tags.js`, `deploy`, `docker` | Direct core/SQLite atom delete; boundary supplied reset inventory | Chunk/vector/citation/archive cleanup across adapters, backup restore and account deletion uninspected; prevents secure erasure and universal withdrawal claims. |
| Evaluators and fixtures | `crates/atomic-bench/src/suites/memory_longitudinal.rs`, `crates/atomic-bench/src/suites/pipeline_smoke.rs`, `bench/README.md`, `bench/datasets` | Direct longitudinal import/search/score/tempdir path; boundary supplied pipeline smoke and evaluator contract | Other suites/fixture details and results uninspected; prevents retrieval-quality, answer-quality or learning conclusions. |

## Core ideas

1. **Content and access state are different retained parts.** Markdown atoms are readable knowledge. Chunks preserve selected text; embeddings and graph aggregates select or organize it. Tags are symbolic associations with model-authored names. Numerical retrieval state is not provider weights, and a tag marked `auto` or `manual` does not authenticate who authored its associated prose. See [MEM-OBJ-atoms](#mem-obj-atoms), [MEM-OBJ-atom-chunks](#mem-obj-atom-chunks), [MEM-OBJ-chunk-embeddings](#mem-obj-chunk-embeddings), [MEM-OBJ-tags](#mem-obj-tags).
2. **Generation boundaries differ from retrieval boundaries.** Agentic wiki research excludes report findings, MCP search excludes them by default, but ordinary chat search admits all kinds. A saved model answer goes through ordinary capture, so a `Captured` filter is not a universal non-generated-content filter. These are selection rules, not truth judgments. See [MEM-RTE-corpus-retrieval](#mem-rte-corpus-retrieval), [MEM-RTE-answer-save](#mem-rte-answer-save) and the report annotation.
3. **Retained history is richer than the replayed prompt.** Storage can hold tool output and citation metadata, while the next chat request reconstructs role/content only. Truncation drops old groups; it does not create a durable summary. Wiki and report prose are separate derived products, not conversation checkpoints. See [MEM-OBJ-chat-history](#mem-obj-chat-history) and the chat annotation.
4. **“Compaction” changes categories, not conversational memory.** The implemented tag operation retags atoms, reparents children and deletes the losing tag. Model reasons are logged in the SQLite merge path rather than retained as a later-readable rationale alongside the changed taxonomy. An explicit caller-supplied merge bypasses model selection while keeping hierarchy guards. See [MEM-RTE-tag-compaction](#mem-rte-tag-compaction).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-atoms
Label: Atoms

Source-native identity: `atoms` rows and `AtomWithTags`. Storage substrate: SQLite or PostgreSQL through StorageBackend, with SQLite behavior inspected here. The operative content is natural-language Markdown; IDs, kind, source URL, timestamps, statuses and associations are symbolic metadata. Titles/snippets are readable display derivatives, not substitutes for full content. Lineage includes external captures, direct imports, model mutations, saved answers and separately stamped report output. Actual later consumers include scoped chat tools, MCP/API readers, wiki research and report research. Text reaches models as evidence/tool content, not an independently enforced instruction channel. The closest supplied records are [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) and [RT-RTE-atom-mutation](runtime.md#rt-rte-atom-mutation); those are write routes, not this retained object. SRC-1: `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-core/src/storage/sqlite/atoms.rs`, `crates/atomic-core/src/storage/sqlite/reports.rs`. Finding content is separately assessed in [MEM-OBJ-report-findings](#mem-obj-report-findings).

The request to fetch full content differs from reading a snippet:

> .get_atom_content_impl(atom_id)
> --- `crates/atomic-core/src/chat_tools.rs`

#### MEM-OBJ-atom-chunks
Label: Atom chunks

Source-native identity: chunk content with atom ID/chunk index, persisted by chunk storage. Form: natural-language slices plus symbolic lineage identifiers. Substrate: database chunk rows and text indexes. In the inspected whole-atom path, derivation deletes old chunks, runs chunk_content and saves new text with embeddings. This is text segmentation, not an inspected semantic summary. Later search returns matching chunk text, while wiki consumes selected chunks. Distinct from the maintenance route [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), which produces this material among other effects. SRC-1: `crates/atomic-core/src/embedding.rs`, `crates/atomic-core/src/search.rs`, `crates/atomic-core/src/chat_tools.rs`.

> // Chunk content
>     let chunks = chunk_content(content);
> --- `crates/atomic-core/src/embedding.rs`

#### MEM-OBJ-chunk-embeddings
Label: Chunk embeddings

Source-native identity: embeddings paired with retained chunk content. Form: dense distributed numerical representations; substrate: database vectors/indexes, not model weights. Lineage: configured provider embeds chunk text; mutable model selection is in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). Later query embeddings and vector search compare against this state; results are delivered as text/IDs/scores, not vectors automatically inserted into model context. Source vector generation and update paths establish curation/access capacity, not semantic verification or improved future action. Initial vectors imported by an uninspected alternative and provider-internal derivation remain unresolved. Distinct from the provider component and from the symbolic/natural-language chunk object. SRC-1: `crates/atomic-core/src/embedding.rs`, `crates/atomic-core/src/search.rs`.

> let chunks_with_embeddings: Vec<(String, Vec<f32>)> = embedded
> --- `crates/atomic-core/src/embedding.rs`

#### MEM-OBJ-tags
Label: Tags

Source-native identity: `tags` hierarchy and `atom_tags` associations. Form: symbolic IDs, parent links and source flags; names and optional descriptions are readable text interpreted by the tagger. Substrate: database tables. Lineage: caller-supplied tags, generated applications and compaction. Later consumers use membership/descendants for corpus scope and show taxonomy to readers or taggers. Thus changed associations can change later eligibility even without changing atom text. Model naming/consolidation does not establish correct categories. Closest supplied record [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) is a broader producer route, not an object counterpart. SRC-1: `crates/atomic-core/src/search.rs`, `crates/atomic-core/src/embedding.rs`, `crates/atomic-core/src/compaction.rs`.

> && self.require.iter().all(|t| roots.contains(t))
> --- `crates/atomic-core/src/search.rs`

#### MEM-OBJ-chat-history
Label: Chat history

Source-native identity: chat messages with stored tool calls/citations. Substrate: database chat tables; form: natural-language message/output text plus symbolic role, ordering, tool inputs and citation identities. Lineage: user turns and generated assistant answers, with current-run tool traces saved separately. The next provider invocation receives message role/content; UI/history retrieval can retain richer context. This raw trace retention is not evidence of an automatic durable method update. Closest supplied [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) is the turn route, not a separate object declaration. SRC-1: `crates/atomic-core/src/chat.rs`, `crates/atomic-core/src/agent.rs`.

> Message {
>                 role,
>                 content: Some(m.message.content),
>                 tool_calls: None,
>                 tool_call_id: None,
>                 name: None,
>             }
> --- `crates/atomic-core/src/agent.rs`

#### MEM-OBJ-wiki-articles
Label: Wiki articles

Source-native identity: live wiki article, citations/links, pending proposal and archived article versions. The container has distinct operative parts: natural-language synthesized article/proposal content; symbolic base IDs/timestamps and citation/link identities; historical prose plus serialized citations in versions. Substrate: database wiki tables. Live articles feed chat/MCP/UI readers. Pending proposals feed caller review/acceptance; they do not inherit live-reader authority until publication. Archives retain prior content/citations for version retrieval, but an exercised restoration or model consumer of archives was not established. Lineage comes from selected retained chunks and configurable generation/update instructions. This object is distinct from [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission); differing part authorities are preserved in that route's annotation and separately assessed in [MEM-OBJ-wiki-proposals](#mem-obj-wiki-proposals) and [MEM-OBJ-wiki-versions](#mem-obj-wiki-versions). SRC-1: `crates/atomic-core/src/wiki/mod.rs`, `crates/atomic-core/src/wiki/agentic.rs`, `crates/atomic-core/src/chat_tools.rs`; proposal identity/gates are supplied by the runtime record.

> archive_existing_article(conn, &article.tag_id)?;
> --- `crates/atomic-core/src/wiki/mod.rs`

> "INSERT INTO wiki_article_versions (id, tag_id, content, citations_json, atom_count, version_number, created_at) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
> --- `crates/atomic-core/src/wiki/mod.rs`

#### MEM-OBJ-wiki-proposals
Label: Wiki proposals

Part of: [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles)

Source-native identity: `WikiProposal` retained in `wiki_proposals`, distinct from the live article and archived versions. Storage substrate: database proposal storage through StorageBackend. Representational form: natural-language merged candidate prose and citation excerpts, plus symbolic section operations, citation identities, base article ID/timestamp, proposal ID and new-atom count. Lineage: selected chunks and configured strategy produce a draft against the current article; software persists its merged content, citations and operations. Initial source authorship inherits the corpus uncertainties rather than establishing human authorship. SRC-1 implementation: `crates/atomic-core/src/lib.rs`; the enclosing admission route is [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission), not an object counterpart.

Actual consumers and authority: get_wiki_proposal retrieves the candidate by tag for caller review; accept_wiki_proposal reads it on a later acceptance invocation. Candidate prose has natural-language review authority at the caller, while base IDs/timestamps have fixed freshness-check authority at acceptance. Acceptance copies candidate content/citations into the live article only when its base still matches. Pending retention alone does not grant the live model readers its content. The API exposes caller acceptance/dismissal; generic caller identity and immediate propose-and-accept leave human per-content approval unresolved. Software/model admission writes the candidate; the caller can veto promotion by dismissal. No answer oracle or semantic-support check is established. Operation and actual reliance remain uninspected.

> content: draft.merged_content,
>             citations: draft.citations,
>             ops: draft.ops,
> --- `crates/atomic-core/src/lib.rs`

> match db.0.get_wiki_proposal(&tag_id).await {
>         Ok(Some(proposal)) => HttpResponse::Ok().json(proposal),
> --- `crates/atomic-server/src/routes/wiki.rs`

Retention/recovery: a new pending proposal supersedes the prior candidate; dismiss deletes without promotion. Successful acceptance saves the live article before deleting the candidate in a separate await. Stale acceptance rejects rather than silently rebasing; regeneration requires a new candidate. These controls differ from archive retrieval and live evidence delivery. The supplied route retains the freshness and immediate-accept passages; no automatic rollback or universal human review follows.

#### MEM-OBJ-wiki-versions
Label: Wiki versions

Part of: [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles)

Source-native identity: `WikiArticleVersion` rows in `wiki_article_versions`, separate from live content and pending candidates. Storage substrate: SQLite archive table in the directly inspected implementation; PostgreSQL archive semantics remain uninspected. Representational form: historical natural-language prose and citation excerpts with symbolic version/tag IDs, version number, atom count, timestamp and serialized citation identities. Lineage: save archives the existing live article and its citations before replacement; this is a retained historical checkpoint, not a new synthesis or performance critique. Citation reconstruction in the archive sets source_url to None, so it is not a complete clone of every source field. SRC-1 implementation: `crates/atomic-core/src/wiki/mod.rs`. Closest supplied [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission) is the enclosing publication route; this object is a distinct material part of the retained container.

Actual consumers and authority: list_wiki_versions selects summaries by tag in descending version order; get_wiki_version selects historical content/citations by version ID. Shipped HTTP handlers return those results to requesting callers. Version number and IDs govern fixed selection; historical text is available for caller interpretation, not automatically selected as live model evidence. A later model consumer, exercised restoration and archive-driven rollback are not established by these readers. Thus the archive supports historical retrieval without inheriting live article behavioral authority. Source wiring is inspected; operation and downstream reliance are uninspected.

> "SELECT id, tag_id, content, citations_json, atom_count, version_number, created_at FROM wiki_article_versions WHERE id = ?1",
> --- `crates/atomic-core/src/wiki/mod.rs`

> ok_or_error(db.0.get_wiki_version(&version_id).await)
> --- `crates/atomic-server/src/routes/wiki.rs`

Admission and recovery: software snapshots the previous published product as part of save; no independent human approval of each snapshot or semantic revision occurs. The subsequent publication may be direct or caller-accepted under the supplied route. Archive write failures can fail the inspected save, but read capability alone is not a recovery action. Archive expiry/deletion, restoration UI and cross-adapter parity remain uninspected, preventing universal withdrawal or rollback guarantees. The container retains the archive insertion passages.

#### MEM-OBJ-report-findings
Label: Report findings

Source-native identity: report-kind atom plus `report_findings` provenance and `report_finding_citations`. Natural-language final prose differs from symbolic report/run identity, output tags and citation positions; excerpts are readable source fragments. SQLite retains them in one transaction. The finding is a specialized part of the atoms corpus, not an independently authenticated evidence class. Later chat/MCP finding readers and kind-enabled search consume it. `tagging_status = 'skipped'` prevents ordinary automatic tagging in this insert; deterministic output tags remain. The final report retains prose and resolved cited references, not an inspected durable research-message/tool-trace checkpoint. Closest supplied [RT-RTE-report-finding](runtime.md#rt-rte-report-finding) is the producer/admission route. SRC-1: `crates/atomic-core/src/storage/sqlite/reports.rs`; supplied runtime record grounds final-pass citation selection.

> let tx = conn.transaction()?;
> --- `crates/atomic-core/src/storage/sqlite/reports.rs`

> VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?6, 'pending', 'skipped', ?7, ?8, 'report')",
> --- `crates/atomic-core/src/storage/sqlite/reports.rs`

> tx.commit()?;
> --- `crates/atomic-core/src/storage/sqlite/reports.rs`

### Routes

#### MEM-RTE-atom-enrichment
Label: Atom enrichment

Part of: [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance)

This is the atom embedding/tagging subroute of the broader dispatch, not a replacement for graph maintenance. Endpoints: queued or direct atom processing → configured provider → chunk/vector replacement and tag linking → later search/scope/wiki consumers. Owner: software schedules and persists; model supplies embeddings and tag applications. Context/state: atom text, settings and eligible tag-tree context. Trigger/proposed change: captured/changed atom or retry requests new access metadata. Admission is software/model, with no per-vector or per-tag human approval in inspected handlers. Caller control of settings or target branches is not authorship of each application. Fixed checks skip disabled/no-key/no-target tagging and ignore empty/`null` names. There is no expected-answer oracle; mode is recurring enrichment under configured prompts. Recovery/rejection: provider/storage errors stop the inspected path; queue retry semantics belong to the supplied runtime route. Deleting chunks precedes embedding success, so no rollback of the previous chunk set is established. SRC-1: `crates/atomic-core/src/embedding.rs`, `crates/atomic-core/src/extraction.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success/error or tagging outcome, plus persisted statuses and derived state.
- Later read-back: chunks/vectors drive subsequent retrieval; tags affect later subtree selection and tagger context.
- Delegated visibility: embedding service receives chunk text; tagger receives prefix-limited atom text and selected tag hierarchy with configured system prompt.
- Selection predicate: atom ID/content, current status, auto_tagging_enabled, provider availability and configured auto-tag target tree; tagging max input derives from context estimate, otherwise 120000 bytes under the inspected len/slice implementation.
- Invalidation or expiry: whole-atom embedding deletes/replaces prior chunks; current complete/skipped tags can avoid rerunning; later retag/re-embed operations have separate admission.
- Activation or effect: implementation installs numerical/text access state and tag associations; actual improved retrieval or changed model behavior remains unobserved.
- Evidence limits: single-atom path inspected; batches and existing-chunk re-embedding are included alternatives, not assumed identical. Tagging prefix can omit later content and does not guarantee complete atom classification.

> if current_status == "skipped" || current_status == "complete" {
> --- `crates/atomic-core/src/embedding.rs`

> .delete_chunks_batch_sync(&[atom_id.to_string()])
> --- `crates/atomic-core/src/embedding.rs`

> &content[..end]
> --- `crates/atomic-core/src/extraction.rs`

#### MEM-RTE-tag-compaction
Label: Tag compaction

Endpoints: utility API/core request → all-tag hierarchy → structured LLM merge suggestions → guarded database merge; alternatively caller supplies explicit pairs to apply_tag_merges. Owner: model proposes pairs/reasons in ordinary mode; caller proposes in explicit mode; software decides identity/hierarchy admissibility and performs writes. No independent human veto per model merge is wired in compact_tags. Authenticated caller identity alone does not establish human authorship of explicit pairs. Context: names/hierarchy, not an inspected judgment of each atom's content. Proposed change: winning tag acquires associations/children; loser is deleted. Stock prompt requests conservative equivalence; hierarchy checks reject missing/same/ancestor/descendant pairs, not all semantic mistakes. Mode: open maintenance request; no answer oracle or measured improvement selection. Recovery: missing/invalid pairs skip; SQLite accumulates merge errors and returns counters; no transaction or automatic taxonomy rollback in this inspected apply path. Distinct mechanism within the broad subject of [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), whose declared scheduled graph/pipeline progression does not name this utility operation. SRC-1: `crates/atomic-core/src/compaction.rs`, `crates/atomic-core/src/lib.rs`, `crates/atomic-core/src/storage/sqlite/tags.rs`, `crates/atomic-server/src/routes/utils.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tags_merged and atoms_retagged counters, or orchestration error; SQLite per-merge errors can instead be logged.
- Later read-back: changed tag tree and memberships affect later scopes, browses and auto-tagger context; no later database reader of merge.reason established in this SQLite path.
- Delegated visibility: provider receives full formatted tag hierarchy in ordinary mode; explicit mode skips the provider proposal step.
- Selection predicate: model-selected winner/loser names or explicit caller pairs, resolved case-insensitively and guarded against hierarchy/self merges.
- Invalidation or expiry: loser tag deleted, children reparented, canvas cache invalidated; no automatic restoration of losing taxonomy established.
- Activation or effect: code changes retained categorization automatically after guards; semantic correctness and downstream improvement unobserved.
- Evidence limits: SQLite application inspected, PostgreSQL not audited. Reasons occur in logging rather than inspected durable rationale storage; not a claim that deployment logs cannot be retained externally.

> None => db.0.compact_tags().await,
> --- `crates/atomic-server/src/routes/utils.rs`

> "INSERT OR IGNORE INTO atom_tags (atom_id, tag_id, source) VALUES (?1, ?2, 'auto')",
> --- `crates/atomic-core/src/compaction.rs`

> "UPDATE tags SET parent_id = ?1 WHERE parent_id = ?2",
> --- `crates/atomic-core/src/compaction.rs`

> reason = %merge.reason,
>         "Merged tags"
> --- `crates/atomic-core/src/compaction.rs`

#### MEM-RTE-corpus-retrieval
Label: Corpus retrieval

Endpoints: query/identifier request → scope/kind/time selection and hybrid ranking or exact reader → text window/matching chunk plus identifiers → chat model, wiki research, frontend or MCP response. Owner: caller/model chooses query or ID, fixed selectors constrain candidates. This is request-driven retrieval, not unsolicited whole-corpus prompt injection. Retention is existing atoms/chunks/products; scores and session citation numbering are current-run metadata. Distinct cross-consumer selection route, overlapping read portions of [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission) and [RT-RTE-report-finding](runtime.md#rt-rte-report-finding), not a replacement for their enclosing invocations. SRC-1: `crates/atomic-core/src/search.rs`, `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-server/src/mcp/server.rs`, `crates/atomic-core/src/wiki/agentic.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked text/IDs/scores or paginated content; chat registers current-run citation identities.
- Later read-back: retained corpus reaches later query/tool invocations; delivered evidence can enter generated answers/articles/findings under their distinct admission routes.
- Delegated visibility: chat search renders full matching chunk content with citation number/atom ID/score; MCP renders a 200-character content preview plus matching chunk; wiki research selects session chunks for a later synthesis pass.
- Selection predicate: query, keyword/vector/RRF mode, limit/threshold, tag include/require/exclude with descendants, since_days and kind filter. Chat search defaults to five results and all kinds; MCP defaults to ten, caps at fifty and captured-only unless include_generated.
- Invalidation or expiry: later writes/enrichment change the corpus/index; run-local citation numbers are not durable identities; selected text need not reflect every retained source.
- Activation or effect: source wires delivery to model consumers and API/UI responses; model reliance, compliance and benefit unobserved.
- Evidence limits: direct ID readers do not automatically inherit a search filter; exact backend scoring/cleanup and all alternate reader guards uninspected. API exposure alone does not establish a deployed external MCP consumer.

> result.similarity_score,
>                     result.matching_chunk_content
> --- `crates/atomic-core/src/chat_tools.rs`

> let kinds = if params.include_generated.unwrap_or(false) {
>             KindFilter::All
>         } else {
>             KindFilter::only(AtomKind::Captured)
>         };
> --- `crates/atomic-server/src/mcp/server.rs:176-180`

#### MEM-RTE-answer-save
Label: Answer save

Endpoints: supplied answer/citations/question → deterministic Markdown construction → Chat Answers tag resolution → ordinary atom creation/enrichment → corpus readers. Owner: caller initiates retention; frontend software converts and writes; original model authored the answer. No semantic critic or answer oracle in this helper; mode is open save, not an improvement experiment. Admission: createAtom's ordinary write, not report-kind admission. Rejection/recovery: helper errors propagate; ordinary later edit/delete can change the atom, but automatic restoration of prior answer metadata is not established. Guidance: supplied question/conversation title determines title, source-native conversion rules determine links. The raw answer is transformed: atom citation markers become [[atom_id]], wiki/finding markers lose inline placement and become display-only Sources entries. Code spans/link syntax are protected. This is a distinct trace-to-corpus conversion before the shared ordinary create path [RT-RTE-capture-write](runtime.md#rt-rte-capture-write), not a duplicate of its storage insert. SRC-1: `src/components/chat/saveAnswerAsAtom.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: created AtomWithTags or error through the atoms store.
- Later read-back: saved answer is ordinary corpus content, chunked/embedded/tagged through the create pipeline; Chat Answers marks provenance for filtering/display, not a distinct kind gate.
- Delegated visibility: later readers see derived Markdown/title/Sources, not an automatic replay of original conversation, complete tool trace or model reasoning.
- Selection predicate: caller supplies the answer and citations; deterministic map by citation_index and source_type selects marker conversions and deduplicated source entries.
- Invalidation or expiry: ordinary atom edit/delete applies; conversion has already discarded non-atom inline citation positions and stable source links from those Sources entries.
- Activation or effect: model-produced prose can become retained evidence for later model invocations; improved capacity and automatic learning from criticism are not established.
- Evidence limits: caller UI not inspected, so no human per-save approval invariant; capture classification does not prove non-model authorship. Function comments are checked against the conversion branches rather than treated as provenance guarantees.

> if (sourceTypeOf(citation) !== 'atom') return '';
>       return `${space}[[${citation.atom_id}]]`;
> --- `src/components/chat/saveAnswerAsAtom.ts`

> return useAtomsStore.getState().createAtom(content, undefined, [tagId]);
> --- `src/components/chat/saveAnswerAsAtom.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-corpus-evidence
Label: Corpus evidence authority

Consumer: chat model and configured wiki/report synthesis models. Channel: requested tool results, selected source text and retained conversation prose. Force: natural-language evidence and model interpretation, distinct from symbolic scope/ranking gates; delivery does not establish belief, instruction compliance or truth. Horizon: later turns/requests while content remains and is selected. A generated product can feed later generation, but report-kind and captured-only controls differ by route. Closest supplied [RT-BAP-chat-prompt](runtime.md#rt-bap-chat-prompt) is system-instruction authority, not this evidence channel. SRC-1: `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/wiki/agentic.rs`; [MEM-RTE-corpus-retrieval](#mem-rte-corpus-retrieval) retains delivery evidence and the supplied report route retains final-pass wiring.

## Annotations

#### On [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn)

Read-back adds only role/content from stored messages; attached historical tool_calls and citations are not reconstructed by chat_messages_to_provider_messages. This resolves the runtime's declared historical conversion uncertainty. The richer stored trace can remain available to UI/storage readers without reaching the next provider prompt. Raw-to-derived chain: user/assistant turn text persists → reconstructed role/content → context selection → next provider call. No durable conversational summary is produced by the inspected truncator. SRC-1: `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/agent_runtime/context.rs`; conversion quote is in [MEM-OBJ-chat-history](#mem-obj-chat-history).

Budget is estimated at 70% of context_length; the first and last groups always remain. It is not a strict total-input ceiling when those groups exceed budget or the model context length is unknown. Dropped groups remain in the database, not deleted by prompt selection.

> Some(ctx_len) => (ctx_len as f64 * 0.7) as usize,
>         None => return messages,
> --- `crates/atomic-core/src/agent_runtime/context.rs`

> let mut budget = max_tokens.saturating_sub(first_tokens + last_tokens);
> --- `crates/atomic-core/src/agent_runtime/context.rs`

#### On [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission)

Research selection is followed by additional omission. trim_to_budget stops before a later chunk that exceeds the allowance but always permits the first chunk, so max_source_tokens is not a strict maximum for an oversized first source. The code's ordered input is what determines survival; do not infer that every selected research source reaches synthesis. Source-only eligibility here means captured kind, not independently authenticated raw/non-generated authorship. SRC-1: `crates/atomic-core/src/wiki/agentic.rs`; supplied runtime quotation grounds the captured-kind filter, and [MEM-RTE-answer-save](#mem-rte-answer-save) grounds the authorship caveat.

> if total_tokens + tokens > max_source_tokens && !trimmed.is_empty() {
>             break;
>         }
> --- `crates/atomic-core/src/wiki/agentic.rs`

Current article replacement first archives prior prose/citations in SQLite; archives and pending proposals have different consumers from the live article. Chat GetWiki strips underlying source citation markers, pages the prose, and assigns a new citation to the wiki as a product. Thus original source provenance is retained in storage but not delivered in that tool's article body. MCP get_wiki instead returns article content and citations together. SRC-1: `crates/atomic-core/src/wiki/mod.rs`, `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-server/src/mcp/server.rs`.

> &strip_citation_markers(&wiki.article.content),
> --- `crates/atomic-core/src/chat_tools.rs`

#### On [RT-RTE-report-finding](runtime.md#rt-rte-report-finding)

SQLite's write_finding_transactionally_sync directly confirms atom/tags/provenance/citations share a transaction; this strengthens only the helper's local durability account, not end-to-end exactly-once operation or PostgreSQL parity. Findings retain final prose and chosen citation references; the supplied final-pass progression does not establish durable research rationale. [MEM-OBJ-report-findings](#mem-obj-report-findings) retains the transaction passages.

The research reader is a material alternate selection path: ReadAtom contains core only and directly invokes get_atom with the supplied ID, with no ContextFilter in that handler. Search results are filtered; identifier reads are not thereby scoped. A guessed or otherwise available ID could therefore return text outside the report's search-context filter in this inspected implementation. CitationAdmission still separately controls resolvable citations; source-only citation policy is not a universal content-visibility boundary. This is a positive path finding, not an allegation of observed exploitation. SRC-1: `crates/atomic-core/src/reports/agentic.rs`.

> struct ReadAtom {
>     core: AtomicCore,
> }
> --- `crates/atomic-core/src/reports/agentic.rs`

> let atom = match self.core.get_atom(atom_id).await {
> --- `crates/atomic-core/src/reports/agentic.rs`

#### On [RT-RTE-settings-change](runtime.md#rt-rte-settings-change)

Retained prompts and symbolic configuration have different authority. Stored custom chat prefix reaches a later system message under [RT-BAP-chat-prompt](runtime.md#rt-bap-chat-prompt); tagging_prompt can replace the stock tagging system prompt, while provider/strategy keys choose executable branches. Authors and human approval are unresolved for generic API callers. Settings replacement/clearing changes future selection; it is not evidence of trace-fed automatic prompt improvement. SRC-1: `crates/atomic-core/src/extraction.rs`; provider override and settings routing remain supplied runtime findings.

> let system = custom_system_prompt
>         .filter(|s| !s.is_empty())
>         .unwrap_or_else(|| default_system_prompt_for_tag_tree(tag_tree_json));
> --- `crates/atomic-core/src/extraction.rs`

## Write side

Admission is route-specific. Capture admits caller content; agent edit admits model-proposed text after structural/concurrency checks; neither gate authenticates truth. Those findings are supplied in [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) and [RT-RTE-atom-mutation](runtime.md#rt-rte-atom-mutation). Browser/plugin/share/import initial control is not resolved to “human” merely because these are user-facing surfaces. Physical database writes are software in both human-authored and computed-content cases.

[MEM-RTE-atom-enrichment](#mem-rte-atom-enrichment) automatically transforms retained text into retrieval state and associations. [MEM-RTE-tag-compaction](#mem-rte-tag-compaction) automatically applies model proposals in ordinary mode, while explicit pairs provide caller-directed curation. These operations retain changed access structure rather than a durable criticism of the method. Embedding raw text is not a trace-of-performance update; generated vectors alone establish no improved capacity.

[MEM-RTE-answer-save](#mem-rte-answer-save) does retain a derivative of an interaction outcome. It converts answer/citation material into ordinary corpus prose with reduced provenance. Later retrieval is wired, but the helper does not automatically diagnose performance, preserve the full reasoning episode or revise operating instructions. The preserved answer can shape later context independently of any weight update. Historical raw tool logs do not establish a separate automatic learning route.

Wiki proposal acceptance/dismissal and direct publication remain different admissions under [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission). A caller can reject a pending proposal; direct generation/update alternatives prevent a universal human review claim. Prior article content/citations are archived in the inspected SQLite save routine. [MEM-OBJ-wiki-proposals](#mem-obj-wiki-proposals) separately assesses retained review candidates and acceptance freshness. [MEM-OBJ-wiki-versions](#mem-obj-wiki-versions) assesses historical snapshots and the shipped version readers. Availability of a version reader is a retrieval capability for requesting callers, not evidence of automatic rollback or later model consumption of that checkpoint.

Report generation automatically admits nonempty final prose and ledger-resolved references under [RT-RTE-report-finding](runtime.md#rt-rte-report-finding). The SQLite helper makes finding insertion locally transactional. Research drafts/tool messages and factual grounds beyond selected citation excerpts are not established as durable artifacts consumed by subsequent reports. No confidence/semantic-support guarantee follows from valid markers.

Withdrawal is narrower than secure erasure. The inspected core delete invokes storage and invalidates canvas; SQLite explicitly removes tag associations/outgoing links, marks incoming links missing, removes atom FTS and deletes the atom row. It does not itself demonstrate removal of every chunk/vector, cited excerpt, archive, backup or provider copy. The related schemas/triggers and account/backup/reset routes remain inspection limits, not evidence of absent cleanup. SRC-1: `crates/atomic-core/src/lib.rs`, `crates/atomic-core/src/storage/sqlite/atoms.rs`.

> mark_incoming_atom_links_missing(&conn, id, &chrono::Utc::now().to_rfc3339())?;
> --- `crates/atomic-core/src/storage/sqlite/atoms.rs`

Evaluation is separate from production admission. The inspected LongMemEval driver renders sessions into atoms, bulk imports and waits for enrichment, performs hybrid search, maps atom IDs back to sessions and compares ranks with answer_session_ids. Its retained JSONL metrics are retrieval evidence if a run exists, not memory supplied to production chat or an inspected optimizer that updates its instructions. It uses temporary per-instance databases; keep_db deliberately suppresses TempDir cleanup. No execution/result is registered. SRC-1: `crates/atomic-bench/src/suites/memory_longitudinal.rs`; other evaluators remain in the coverage inventory.

> let scoring_at_k = score_retrieval(&retrieved_sessions, &evidence, top_k);
> --- `crates/atomic-bench/src/suites/memory_longitudinal.rs`

> std::mem::forget(tempdir);
> --- `crates/atomic-bench/src/suites/memory_longitudinal.rs`

## Read-back

Three operations must not be conflated:

- **Automatic history supply:** the next requested chat turn reloads stored message text and trims it before provider delivery. This is automatic selection within a requested turn, not an independent unsolicited memory push. No opaque provider conversation state is inspected.
- **Requested corpus retrieval:** [MEM-RTE-corpus-retrieval](#mem-rte-corpus-retrieval) uses queries, tag scope, time/kind filters and line windows. A stored ID is not proof of relevance; scope/ranking and actual supplied text establish selection. Chat search delivers matching chunk text, not only citation excerpts; exact readers can supply additional windows.
- **Scheduled synthesis:** supplied [RT-RTE-report-finding](runtime.md#rt-rte-report-finding) and [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) connect automatic triggers to retained state. Report source/window/cap and research context select material; wiki's researcher selects session chunks and another budget stage omits some. Scheduler/ledger markers affect recovery and next-window choice, but that symbolic authority does not make them model-readable knowledge.

Live wiki/finding prose can become model context through registered readers. Wiki and finding chat tools treat products as new citation sources rather than transparently replaying every original evidence reference. MCP exposes richer product citations, but downstream usage remains outside Atomic's inspected enclosing loop. Source trust is therefore a combination of kind eligibility, stored lineage and requested model behavior, not an observed grounding guarantee. Generated saved answers may re-enter captured-only routes, and direct report read_atom can bypass the search context's selection filter.

## Integration issues

The correction retains the valid [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles) container and declares its pending candidate and historical checkpoint parts separately as [MEM-OBJ-wiki-proposals](#mem-obj-wiki-proposals) and [MEM-OBJ-wiki-versions](#mem-obj-wiki-versions). They have different admission/freshness checks, selectors and consumer authority; neither replaces or duplicates [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission). No model consumption or automatic restoration of archived versions is newly asserted. This resolves the refusal's missing-part issue without erasing the existing publication caveats.

1. **Resolve historical replay uncertainty:** the chat annotation establishes role/content-only conversion and omission of historical tool-call/citation metadata from provider Messages. This refines [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), whose later-read-back field explicitly left conversion uninspected. It does not contradict rich storage retention.
2. **Resolve report reader isolation:** the report annotation establishes unguarded identifier fetch in ReadAtom, separate from filtered semantic_search. [RT-RTE-report-finding](runtime.md#rt-rte-report-finding) correctly left reader isolation unresolved; do not promote search filtering or SeededOnly citation eligibility to universal model-visible content isolation.
3. **Refine local finding durability:** the SQLite transaction is directly inspected in [MEM-OBJ-report-findings](#mem-obj-report-findings), filling a supplied storage gap in [RT-RTE-report-finding](runtime.md#rt-rte-report-finding). PostgreSQL, post-write cache/ledger/enrichment and replay after failure remain unresolved; exactly-once is still unsupported.
4. **Qualify budget language:** chat and wiki annotations show mandatory first/latest groups or first chunk can exceed nominal limits. [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) and [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission) should retain selection/omission without treating these budgets as strict input guarantees.
5. **Keep taxonomy and conversation compaction separate:** [MEM-RTE-tag-compaction](#mem-rte-tag-compaction) is a newly inspected utility/library route, not a replacement of scheduled graph/enrichment [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance). No possible duplicate referent was found after comparing supplied records; new objects are retained material, supplied routes are operations. [MEM-RTE-atom-enrichment](#mem-rte-atom-enrichment) explicitly declares containment in the supplied maintenance route.
6. **Keep kind separate from authorship:** [MEM-RTE-answer-save](#mem-rte-answer-save) follows ordinary capture, reducing wiki/finding citation lineage and enabling later corpus consumption. [MEM-RTE-corpus-retrieval](#mem-rte-corpus-retrieval) and [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission) must not equate captured-only with verified human/raw content.
7. **Remaining included uncertainties:** client retry/admission/deletion, alternative batch/re-embedding and wiki strategies, report seed packing, PostgreSQL semantics, ledger/GC/lease internals, full backend withdrawal, backup/account removal and evaluator outcomes are itemized in the coverage table. They prevent universal durability, freshness, isolation, erasure and beneficial-learning conclusions. None requires a boundary change; all are available SRC-1 implementation or unsupplied execution evidence, not access gaps.

## Limitations and checks

The report deliberately bounds direct findings to inspected operations. It does not establish exhaustive behavior of every shipped client, adapter or strategy. Provider-internal weights/state and source authenticity remain opaque; no method of deriving those facts from model identifiers is claimed. Delivery, automatic admission and persisted products do not establish activation, learning, reflection, autonomous criticism or self-improvement. No cross-system comparison or adoption recommendation is made.

Identity check: SRC-1 checkout HEAD equals `983bea6baf449d060514c94b3b15b5f85f77ba9b`; git status returned no modifications. Method/input checks: the invocation, named job, three member types, complete boundary/runtime, collection, worker rules and records contract were read; runtime's final bounded continuation returned no additional text. The worker used only pinned inputs and same-commit sources, with no other analysis exposure, target execution, delegation or evidence-boundary change. New records preserve supplied identity and distinguish objects, parts and overlapping routes. Form/quotation validation is not semantic acceptance or successful operation.

Correction checks: reread SRC-1 `crates/atomic-core/src/lib.rs` proposal production/acceptance/dismissal, `crates/atomic-core/src/wiki/mod.rs` archive/list/version retrieval and `crates/atomic-server/src/routes/wiki.rs` candidate/version HTTP readers against the frozen identity. The supplied previous report is the baseline; unrelated findings and limits are retained. The current invocation, refusal and previous answers/report were read completely, including final empty continuations.

Validation: passed the invocation-specific validate-output command. This checks structure, identity and quotation occurrence, not semantic support or job acceptance.
