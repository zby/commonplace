---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Engraph memory: vault bodies, lossy retrieval indexes, identity extraction and move-fed placement state at the frozen revision."
run-id: AAS-2026-10-14-engraph-0cd4f00695b0-01
source-identity: "https://github.com/devwhodevs/engraph"
reviewed-boundary: f9a95bc96accc792c02ee384d9e6bf768a88c8c8
---

# Engraph memory report

## Boundary and evidence

This report covers Engraph's retained vault content, derived SQLite search structures, placement feedback, identity context, configuration/profile, migration state, diagnostics and requested read-back. The source and whole-system scope are those of [boundary](boundary.md#source-register). All source findings use SRC-1 at f9a95bc96accc792c02ee384d9e6bf768a88c8c8. HEAD was rechecked. Implementation establishes wiring, not successful operation. No target, tests, models or examples were executed.

External conversations, actual user vaults, model bytes and client instruction handling are excluded as in boundary. This prevents identifying the original author of arbitrary incoming text, actual session retention, agent obedience or improved answers. There is no repository access gap. Uninspected implementation details below remain available, not absent.

Direct reads added selected implementation ranges in `src/store.rs`, `src/profile.rs`, `src/placement.rs`, `src/watcher.rs`, `src/indexer.rs`, `src/identity.rs`, `src/context.rs`, `src/health.rs`, `src/writer.rs`, `src/search.rs`, `src/tags.rs`, `src/chunker.rs`, `src/serve.rs` and `src/main.rs`; the complete `skills/engraph/SKILL.md` supplies doctrine/design. Searches checked CLI dispatch, MCP tool declarations, HTTP routes and library functions. Supplied runtime findings support the remaining adapter/setup/migration details; they are not represented as independent direct reads.

| Entry point / retained operation | Paths (SRC-1) | Coverage and remaining limit |
| --- | --- | --- |
| External Markdown admission; CLI index, startup, watcher, explicit reindex | `src/indexer.rs`, `src/watcher.rs`; supplied `src/http.rs` | [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), [MEM-OBJ-chunk-record](#mem-obj-chunk-record), [MEM-OBJ-file-record](#mem-obj-file-record). Direct per-file/batch reads; notification delivery unobserved. |
| CLI/MCP/HTTP create, append, metadata, section edit, rewrite, frontmatter, move | `src/writer.rs`, `src/serve.rs`, `src/main.rs`; supplied `src/http.rs` | [RT-RTE-note-admission](runtime.md#rt-rte-note-admission). Direct create plus supplied other edit findings. Exact metadata edit merge/conflict behavior not independently audited; no uniform edit freshness or rollback conclusion. |
| Placement, create/add/delete adjustments, detected move correction | `src/placement.rs`, `src/watcher.rs`, `src/store.rs`, `src/indexer.rs`, `src/writer.rs` | [MEM-OBJ-folder-centroids](#mem-obj-folder-centroids), [MEM-OBJ-placement-corrections](#mem-obj-placement-corrections), [MEM-RTE-placement-feedback](#mem-rte-placement-feedback). Direct reads; quality and consistent aggregate semantics unestablished. |
| Search, query cache, topic context | `src/search.rs`, `src/store.rs`, `src/context.rs` | [RT-RTE-query-search](runtime.md#rt-rte-query-search), [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache), [RT-RTE-topic-context](runtime.md#rt-rte-topic-context). Direct orchestration branch/context; detailed score internals rely on runtime. |
| Read, read_section, who, project, list, vault_map, graph | `src/context.rs`, `src/serve.rs`; supplied `src/main.rs` | [MEM-RTE-vault-readback](#mem-rte-vault-readback). Direct context/read adapter; standalone graph formatting not independently inspected, so no complete graph-output assessment. |
| Setup, identity CLI refresh and identity tools | `src/identity.rs`, `src/indexer.rs`; supplied `src/onboarding.rs`, `src/main.rs`, `src/http.rs` | [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply), [MEM-OBJ-identity-fact](#mem-obj-identity-fact), [MEM-RTE-identity-context](#mem-rte-identity-context). Direct extraction/format; setup caller details supplied. |
| Profile/config loading and placement/context role maps | `src/profile.rs`; supplied `src/config.rs`, `src/serve.rs` | [MEM-OBJ-vault-profile](#mem-obj-vault-profile), setup annotation. Profile schema read; full detector heuristics not audited, preventing correctness claims for inferred roles. |
| Archive/unarchive, soft/hard delete, cleanup and CLI clear | `src/writer.rs`, `src/indexer.rs`, `src/main.rs` | [MEM-RTE-note-withdrawal](#mem-rte-note-withdrawal). Direct reads; no crash-safety or permanent exclusion guarantee. |
| PARA preview/apply/undo | supplied `src/migrate.rs`, `src/main.rs`, `src/serve.rs`, `src/http.rs` | [RT-RTE-para-migration](runtime.md#rt-rte-para-migration), annotated below. Saved proposals/history are distinct from feedback-trained placement. No independent classification audit. |
| Health and telemetry storage | `src/health.rs`, `src/store.rs`; MCP/HTTP searches | [MEM-OBJ-health-report](#mem-obj-health-report), [MEM-OBJ-cli-event](#mem-obj-cli-event). Health routines directly read; telemetry producer/consumer call sites not fully traced, preventing a trace-learning claim for CLI logs. |
| Agent skill, client setup, product/model replacement | `skills/engraph/SKILL.md`; supplied README/setup/release/inference findings | [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill), [RT-RTE-product-release](runtime.md#rt-rte-product-release), runtime model components. Static instructions and weight cache are not use-derived vault memory. Client activation/model internals unobserved. |

## Core ideas

Engraph separates editable source text from derived retrieval state. Markdown bodies remain on disk, while SQLite stores short snippets, identifiers, graph relationships and dense vectors. Search sees a lossy display of content; a later full read can recover the current disk body. Selection and display can therefore have different freshness. See [MEM-OBJ-vault-notes](#mem-obj-vault-notes), [MEM-OBJ-chunk-record](#mem-obj-chunk-record) and [MEM-RTE-vault-readback](#mem-rte-vault-readback).

Persistent state also shapes future writes. A detected move can update folder centroids, which later semantic placement consumes. This is a concrete trace-fed update, not merely retention of a correction log. It applies only to recognized provenance labels and surviving suggestion metadata, and type rules or explicit folders can bypass it. It establishes a behavior-shaping pathway, not measured improvement or faithful human feedback ([MEM-RTE-placement-feedback](#mem-rte-placement-feedback)).

Identity is another derived view: code selects projects, linked people and recent daily-note snippets, saves extracted facts, then formats them with configured identity for later requests. Labels such as “current” and “fact” do not establish truth, expiry or recent refresh after every watcher event ([MEM-RTE-identity-context](#mem-rte-identity-context)).

Context budgeting happens before tool delivery. Topic context selects and trims disk bodies, leaving omitted material reloadable. It neither compacts the external agent's prior turns nor controls its total context window. The source-grounded details and non-strict byte accounting are in [RT-RTE-topic-context](runtime.md#rt-rte-topic-context).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-vault-notes
Label: Vault notes

Source-native Markdown notes are natural-language content plus symbolic frontmatter on the filesystem. Initial content is supplied by users, external tools or callers with unresolved human control; create can transform tags, links, folder and frontmatter before writing. Files are distinct from [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache) and the transient [RT-OBJ-search-config](runtime.md#rt-obj-search-config); they are retained inputs to [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), not that route's identity. Disk bodies reach read/context clients as knowledge, not Rust-executed instructions. Downstream model interpretation may confer additional authority, but is outside captured evidence (SRC-1, `src/writer.rs`, `src/context.rs`).

> let full_content = format!("{}{}", frontmatter, body);
> --- `src/writer.rs`

#### MEM-OBJ-file-record
Label: FileRecord

Source-native `FileRecord` is symbolic access/selection metadata in SQLite `files`: path, content hash, mtime, tags, indexing timestamp, docid, created_by and note_date. It is derived from paths, frontmatter and I/O, not retained prose reasoning. It supports resolution, filters, freshness checks, dates and extraction. Adapter labels are not authenticated authors; docids aid lookup but are regenerated from paths on indexed rename. Distinct from raw bodies, vectors and supplied [RT-OBJ-search-config](runtime.md#rt-obj-search-config); no supplied object counterpart (SRC-1, `src/store.rs`, `src/indexer.rs`).

> let new_docid = generate_docid(new_rel);
> store.update_file_path(old_rel, new_rel, &new_docid)?;
> --- `src/indexer.rs`

#### MEM-OBJ-chunk-record
Label: ChunkRecord

Source-native `ChunkRecord` has separately operative parts. Natural-language heading/snippet resides in SQLite `chunks` and the FTS lane; symbolic file/vector IDs and token counts join it to access metadata; distributed-parametric dense vectors reside as BLOBs and sqlite-vec entries. Full chunk text is embedded but the saved display snippet is not full text. Chunks use token-count splitting at 512 with 50 overlap on per-file indexing. Initial embedding provenance is the runtime embedder, whose actual weights remain uninspected. No inference-time weight update follows from replacing vectors. The text part supplies search display, reranker candidates and identity extraction; numerical state supplies similarity and centroid updates. Deletion/reindex can remove these derived parts independently of the source body (SRC-1, `src/indexer.rs`, `src/store.rs`, `src/chunker.rs`; [RT-CMP-llama-embed](runtime.md#rt-cmp-llama-embed), [RT-CMP-llama-rerank](runtime.md#rt-cmp-llama-rerank)). No supplied object counterpart; overlaps search route only as its retained input.

> let truncated: String = text.chars().take(200).collect();
> format!("{truncated}...")
> --- `src/chunker.rs`

> store.insert_fts_chunk(file_id, chunk_seq as i64, snippet)?;
> --- `src/indexer.rs`

#### MEM-OBJ-folder-centroids
Label: folder_centroids

Source-native `folder_centroids` stores folder-keyed dense numerical vectors as little-endian f32 BLOBs, with symbolic count/time metadata in SQLite. This is derived behavior-shaping memory, separate from model weights and the correction log. Indexing averages chunk vectors of newly indexed paths grouped by first path component; create/watcher adjustments use a note's mean vector and an actual parent-folder key. `adjust_folder_centroid` treats the stored count as the number of file vectors. Thus paths and units differ across writers: there is no warranted single full-vault, file-weighted centroid invariant. Ordinary changed-file watcher indexing adjusts centroids only if the file is new; the batch indexer's centroid loop uses `indexed_rel_paths`, not every stored file (SRC-1, `src/indexer.rs`, `src/watcher.rs`, `src/writer.rs`, `src/store.rs`). Distinct retained input to [RT-RTE-note-admission](runtime.md#rt-rte-note-admission); no supplied object counterpart.

> for rel_path in &indexed_rel_paths {
>     let folder = rel_path.split('/').next().unwrap_or("(root)").to_string();
> --- `src/indexer.rs`

> store.upsert_folder_centroid(folder, &centroid, vectors.len())?;
> --- `src/indexer.rs`

> .map(|(o, v)| (o * nf + v) / new_n as f32)
> --- `src/store.rs`

#### MEM-OBJ-placement-corrections
Label: PlacementCorrection

Source-native `PlacementCorrection` is symbolic SQLite trace data: file path, suggested and actual folders and timestamp. It records a detected metadata/path mismatch, not a human's explanation or authenticated correction. The write is separate from centroid adjustment; logging can fail after adjustment and vice versa. A getter affords inspection, but no later placement consumer of log rows was established by the inspected paths; later placement consumes centroids instead. Distinct from [MEM-OBJ-folder-centroids](#mem-obj-folder-centroids) and from the preview/history of [RT-RTE-para-migration](runtime.md#rt-rte-para-migration) (SRC-1, `src/store.rs`, `src/watcher.rs`, `src/placement.rs`).

> FROM placement_corrections ORDER BY id DESC LIMIT ?1",
> --- `src/store.rs`

#### MEM-OBJ-vault-profile
Label: VaultProfile

Source-native `VaultProfile` is symbolic TOML persisted to `vault.toml`, containing vault path/type, structure method, detected folder-role map and aggregate statistics. It is a derived configuration representation, not a prose explanation of the detector's reasoning. Setup admits detected values; loaded profiles shape placement, archive exclusion and identity/context folder selection. Updating the file does not itself replace a server's already loaded profile. This is a distinct retained result of [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply), not a duplicate of the route. Full detection accuracy is uninspected (SRC-1, `src/profile.rs`, `src/placement.rs`, `src/indexer.rs`, `src/identity.rs`; supplied setup record).

> /// Complete vault profile, persisted to `vault.toml`.
> --- `src/profile.rs`

#### MEM-OBJ-identity-fact
Label: IdentityFact

Source-native `IdentityFact` separates symbolic tier/key/time/source fields from natural-language value text in SQLite `identity_facts`. Tier-1 facts are extracted from indexed file metadata, graph counts and saved snippets. Projects and people retain file-path sources; focus, blocking and OOO writes pass `None`, so this read-back loses direct source attribution. Reasons and source bodies are not retained in the fact row. The formatter returns grouped values and latest update timestamp, not source pointers. Distinct output of [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply) and [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), with no supplied object counterpart (SRC-1, `src/identity.rs`, `src/store.rs`).

> store.upsert_identity_fact(1, "current_focus", &item, None)?;
> --- `src/identity.rs`

#### MEM-OBJ-health-report
Label: HealthReport

Source-native `HealthReport` is current-request symbolic diagnostic output assembled from retained file/edge/unresolved-link state. It is not itself a saved evaluation or an automatic veto of content. Orphans exclude configured daily/inbox prefixes; pending inbox lists indexed paths; tag issues use fixed work-path/tag rules. Stale-note detection is a stub returning empty output, so an empty stale list does not establish fresh notes. Material diagnostic input `unresolved_links` is retained symbolic source/target data from indexing; detailed cleanup of that table across every delete variant is uninspected, preventing guaranteed diagnostic freshness. No supplied counterpart beyond maintenance routes (SRC-1, `src/health.rs`, `src/store.rs`).

> pub fn find_stale_notes(_store: &Store, _days: u32) -> Result<Vec<String>> {
>     Ok(Vec::new())
> }
> --- `src/health.rs`

#### MEM-OBJ-cli-event
Label: CliEvent

Source-native `CliEvent` is symbolic SQLite raw telemetry with timestamp, operation, outcome and optional detail. Store exposes append, date-filtered query and age-based pruning. These storage methods establish capability, not a deployed logger or a later behavior-shaping consumer. Full producer/consumer call-site inspection is unresolved; this prevents classifying CLI telemetry as trace-fed learning. It is distinct from placement correction and query cache, with no supplied object counterpart (SRC-1, `src/store.rs`).

> "DELETE FROM cli_events WHERE julianday('now') - julianday(timestamp) > ?1",
> --- `src/store.rs`

### Routes

#### MEM-RTE-placement-feedback
Label: Placement feedback

Detected filesystem move → indexed rename → suggestion/provenance comparison → centroid add/subtract and correction log → suggestion-field stripping → later automatic semantic placement. Watcher code owns detection and admission; the mover may be a human or another process. The detector accepts `claude-code`, `cli`, `mcp-server`; `http-api` is not in that list. Metadata is a proxy, not an authenticated feedback principal. Create writes suggestion metadata specifically for an inbox fallback with a positive but below-threshold semantic candidate, so this pathway must not be generalized to every automatic placement (SRC-1, `src/writer.rs`, `src/placement.rs`, `src/watcher.rs`, `src/store.rs`). Distinct submechanism within the supplied maintenance route:

Part of: [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Watcher logs adjustment/errors; no synchronous tool feedback acknowledgment is required.
- Later read-back: Later `place_note` reads saved centroids, embeds new content and chooses a folder; the log row is not the placement input in inspected code.
- Delegated visibility: Writer callers receive placement/result metadata; centroid values and correction reasons are not automatically delivered to an external agent.
- Selection predicate: Move event, successful rename, recognized created_by, suggested_folder differing from actual parent; nonempty retained chunk vectors permit centroid adjustment. Later semantic placement is reached only after type rules fail and no explicit folder overrides it, accepting best cosine similarity above 0.65.
- Invalidation or expiry: Add/subtract replaces numerical state; indexing can overwrite touched centroid rows; stripping suggestion/confidence changes future detectability. No per-correction rollback or expiry in inspected route.
- Activation or effect: Numerical updates are wired to later placement selection, not observed improvement. No transcript or model parameter training is implied.
- Evidence limits: Move delivery, authenticity, positive placement outcomes and coherent aggregate units are unobserved; adjustment errors warn rather than enforce all-or-nothing feedback.

Proposer: mover supplies changed path and prior note metadata. Decider: code, without a separate approval step. Veto/rejection: missing/nonmatching metadata, equal folders, failed rename or absent vectors prevent relevant steps; callers can avoid the move or override later placement. Operating mode: open event processing. Answer oracle: none; actual folder is treated as a preference signal, not known correct placement. Guidance is fixed detection and cosine/mean rules. Durable results are altered numerical centroids, raw correction rows and edited frontmatter, not revised explanatory theory. Recovery is best effort via later indexing/manual state changes; no built-in inverse of a correction is established.

> const ENGRAPH_AGENTS: &[&str] = &["claude-code", "cli", "mcp-server"];
> --- `src/placement.rs`

> // Adjust centroids: boost actual, decay suggested
> --- `src/watcher.rs`

#### MEM-RTE-vault-readback
Label: Vault readback

Client read/list/who/project/vault-map/section request → Rust resolver/filter/graph/FTS selection → current disk read or saved snippets/metadata → serialized client result. These are distinct alternatives to ranked query search and budgeted topic context, not duplicate declarations of [RT-RTE-query-search](runtime.md#rt-rte-query-search) or [RT-RTE-topic-context](runtime.md#rt-rte-topic-context). Direct library functions are storage/context capabilities; MCP `read`, `list`, `who`, `project`, `vault_map`, `read_section` supply concrete shipped callers (SRC-1, `src/context.rs`, `src/serve.rs`; HTTP/CLI routes supplied in runtime).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Full note plus metadata/edges, section body, person/project bundle, filtered note list or overview.
- Later read-back: Previously written files, indexed relationships and snippets reach a later client request; full/section reads reread disk.
- Delegated visibility: Person output includes full person note, mention snippets and link paths; project output includes main note, child-note metadata, tasks, team paths and daily mention snippets, not full child bodies.
- Selection predicate: Identifier/name resolution for explicit reads; folder/tag/created_by/limit for lists; graph relationships and person lookup for who; same-folder list capped at 50 plus incoming links for project, with FTS daily mentions capped at five. An identifier is a lookup key, not evidence of semantic targeting.
- Invalidation or expiry: Disk changes affect body reads; index changes affect resolution, snippets, metadata and edges. No saved bundle expiry: outputs are current-call objects.
- Activation or effect: Code changes selected returned material. External model interpretation and compliance are unobserved.
- Evidence limits: Full-note and who/project delivery have no inspected common topic-style budget. File-record selection can be stale while disk body is current; missing disk full reads return explanatory placeholder data.

The route is requested pull, not independent push. It adds external material on demand without managing old turns. Raw body remains reachable through read/section tools, subject to indexed resolution; client references do not themselves behave as dereferenceable context-window pointers.

> let full_path = params.vault_path.join(&record.path);
> let (content, body, frontmatter) = match std::fs::read_to_string(&full_path) {
> --- `src/context.rs`

#### MEM-RTE-identity-context
Label: Identity context

Full indexing/setup or explicit CLI identity refresh → clear/extract tier-1 facts → SQLite retention → later CLI/MCP/HTTP identity request → formatted L0/L1 text. Code selects projects by tag excluding archive/template path components; people by incoming edge count (five); latest dated daily note for focus; last seven daily notes for OOO; last three for blocking. These are counts of notes, not elapsed-day expiry. The formatter consumes configured L0 identity and saved L1 values. Routine changed/moved/deleted watcher branches do not call extraction; full rescan does through shared indexing (SRC-1, `src/identity.rs`, `src/indexer.rs`, `src/watcher.rs`; adapter triggers supplied in [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply)). This is a distinct extraction/read-back chain, not a duplicate setup route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Extractor returns category counts; identity callers get grouped natural-language text with latest update time.
- Later read-back: Persisted tier-1 facts reach later identity requests across invocations; L0 comes from config rather than a tier-0 database read in the formatter.
- Delegated visibility: Caller gets values, category labels and update time, not fact-row source fields or extraction rationale.
- Selection predicate: Caller requests identity; fixed tag/folder/date/regex/edge rules select extraction inputs. Formatter groups by recognized keys, without a token-budget truncation routine.
- Invalidation or expiry: Extraction clears tier 1 before populating; subsequent re-extraction replaces it. No time-based expiry or mandatory per-event refresh is present in inspected extraction/formatting.
- Activation or effect: Extracted text is wired to client context delivery; the MCP description recommends session-start use but cannot ensure it.
- Evidence limits: Saved snippets can omit relevant text; extraction failure after clearing can leave partial facts. No correctness, immediate freshness or client-session use demonstrated.

Admission: software extraction from admitted index, with setup/refresh caller choice but no per-fact review. Human control over arbitrary source text is unresolved. Veto/recovery: caller can refrain or edit source/config and rerun; errors limit extraction; no automatic previous-fact rollback. Operating mode: open refresh/request. Answer oracle: none. Fixed heuristics guide derived content and are not revised by it. The path is content extraction, not established conversation-trace learning.

> store.clear_identity_facts(1)?;
> --- `src/identity.rs`

#### MEM-RTE-note-withdrawal
Label: Note withdrawal

Caller archive/unarchive/delete/clear or synchronization of deleted files → filesystem and/or index mutation → changed later read/search reachability. This splits lifecycle consequences from the general supplied [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), rather than replacing that route. Archive writes preserved body with new archive frontmatter, deletes vectors/FTS/edges/file row and removes original file. Unarchive reads direct disk path, uses archived_from, rebuilds tags/frontmatter and chunks and removes archive copy. Hard delete removes disk then purges Store. Soft delete instead renames disk and replaces only file row; it is not identical to archive (SRC-1, `src/writer.rs`, `src/indexer.rs`, `src/main.rs`).

Part of: [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lifecycle result/error or CLI clear message; index removal reports counts through its caller.
- Later read-back: Archive normally removes indexed resolution/search; direct-path unarchive restores indexed content. Hard delete removes the source. Soft delete leaves a new file record, so it cannot inherit archive's full indexed invisibility.
- Delegated visibility: Caller receives path/status, not proof that every auxiliary derivative or already delivered client copy was erased.
- Selection predicate: Caller file/mode, configured archive folder or default 04-Archive; unarchive follows disk frontmatter original path and refuses existing restore destination. Integrity cleanup selects indexed files absent on disk.
- Invalidation or expiry: Removes selected retrieval structures; CLI clear deletes engraph.db (or all data directory with --all), not vault Markdown. Archive exclusion depends on profile/config traversal; direct reindex is a separate admission route.
- Activation or effect: Alters future selection/resolution. Does not retract already returned context or necessarily refresh retained identity facts/centroids/cache.
- Evidence limits: Multi-step operations are not a cross-resource transaction. Soft-delete body, vector and FTS cleanup differs from hard delete/archive. Complete withdrawal of all derivatives is not established.

Admission: caller selects lifecycle change; server note guards/HTTP authorization as supplied in runtime, no semantic approval oracle. Index integrity cleanup is automatic software admission of deletion. Operating mode: open requests/maintenance. Rejection: resolution, already-archived and restore collision checks plus I/O errors. Recovery: unarchive is an explicit restore affordance, but archive replaces prior frontmatter instead of preserving every field; hard delete has no inspected built-in restoration. Fixed archive/tag/path rules guide mutation; body, archive metadata and possibly residual derived state persist. Archive status is not a proof that explicit alternative admission cannot reindex the file.

> let (_old_fm, body) = split_frontmatter(&content);
> --- `src/writer.rs`

> // Delete only index files: engraph.db.
> --- `src/main.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache)

Memory lineage: accepted orchestration result serialized into SQLite; symbolic intent/dates plus expansion text influence later search. Query hash selects it only when an orchestrator is present. Cache read bypasses regeneration on valid JSON; malformed JSON invokes orchestration/heuristic fallback but this hit branch does not write a replacement. It retains result fields, not reasoning or correctness evidence. Clear's database deletion removes this state; routine note deletion does not implement cache revocation in the inspected paths. Model and timestamp metadata are not lookup invalidators (SRC-1, `src/search.rs`, `src/main.rs`, `src/store.rs`; runtime quote supports getter).

> serde_json::from_str(&cached_json).unwrap_or_else(|_| {
> --- `src/search.rs`

#### On [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh)

Retained lineage separates natural-language snippets, symbolic access/edge/tag metadata and dense vectors from source disk bodies. Per-file indexing embeds full chunks but saves FTS snippets, bounding keyword and identity visibility. Indexing also registers tags; the registry's exact/fuzzy/prefix rules later alter writer tags, so it is persistent software-admitted naming state, not merely a counter. Physical write provenance is unresolved for external files, while transformation/admission are code-controlled. Graph relationships are symbolic derived wikilink/mention state; later query/context uses them for selection, not as independent truth checks (SRC-1, `src/indexer.rs`, `src/tags.rs`, `src/context.rs`).

> if dist > 0 && dist <= 2 && (best.is_none() || dist < best.as_ref().unwrap().1) {
> --- `src/tags.rs`

#### On [RT-RTE-topic-context](runtime.md#rt-rte-topic-context)

Working-context control: client-requested topic/budget triggers code selection, disk reread, frontmatter omission and UTF-8-safe body truncation. Direct results take priority; graph expansions receive budget/8 caps. Default 32000 and overhead 100 are byte-based calculations despite character names; markers added after trimming can exceed the nominal cap. Direct markers include docid reload hints, and section entries retain paths/docids. Omitted body remains on disk; tool-level selection is not old-turn eviction or isolated-agent execution. No context frame is popped and no external conversation total is controlled (SRC-1, `src/context.rs`).

> const DEFAULT_BUDGET: usize = 32000;
> const SECTION_OVERHEAD: usize = 100;
> --- `src/context.rs`

#### On [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply)

Retained L0 identity consists of configured name, role and vault purpose text interpreted by external clients after formatting; profile is symbolic machine-consumed state; tier-1 extraction is separately recorded above. Generic apply identity does not establish human per-field approval. Saved values and loaded server snapshots have different lifetimes (SRC-1, `src/identity.rs`, `src/profile.rs`; supplied setup findings).

#### On [RT-RTE-para-migration](runtime.md#rt-rte-para-migration)

Memory parts: JSON preview destinations/classifications are symbolic guidance to later apply; Markdown preview is a human-readable display, not the apply input; SQLite migration entries support reverse moves. These persist proposed/output locations and history, not revised classifier rules. Unlike move-fed centroids, saved preview retention alone does not establish experience-fed future classification. Undo is best effort and deletes its log even after partial errors, limiting repeat recovery (SRC-1, `src/migrate.rs`; supplied runtime passage and route).

## Write side

Acquisition has two controls: external editors supply files, which traversal/watch/index code admits without semantic approval; tool/CLI callers supply proposed text, which writer code transforms and admits under operational guards. Authorship, software transformation and actual I/O are separate. Create's exact/alias and high-confidence fuzzy linking can add relationships without another approval, while auto_link=false returns suggestions; explicit folders bypass placement. Registry tag matching can rename proposed tags. The runtime captures rejection, conflict and consistency limits in [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) and [RT-CLM-write-consistency](runtime.md#rt-clm-write-consistency).

Maintenance replaces derived chunks/vectors/edges and retains timestamps/hash/labels, not criticism of source claims. Identity derives shorter text from those already lossy snippets. Its reasons are not returned by the formatter, and some fact sources are absent from rows ([MEM-OBJ-identity-fact](#mem-obj-identity-fact)). Neither process is transcript compaction. No compaction/checkpoint claim is inferred from ordinary chunking.

The qualifying trace-fed update is [MEM-RTE-placement-feedback](#mem-rte-placement-feedback): move plus metadata → old chunk vectors → adjusted durable centroids → later semantic placement. The correction row records the observation but is not the later selector input. Reasons need not survive: stripping removes suggested_folder/confidence, while numerical state keeps no articulated why. This supports source-level feedback wiring, not improved capacity. Alternative numerical updates during create/index/delete must remain separate from the feedback route's provenance ([MEM-OBJ-folder-centroids](#mem-obj-folder-centroids)).

Diagnostics return issues but do not automatically reject or repair content in inspected health routines. Withdrawal has several distinct meanings: source erasure, moving source out of indexed traversal, replacing retrieval rows, removing the entire database, and best-effort reverse migration. None proves retraction of previously delivered text or all derived facts. See [MEM-OBJ-health-report](#mem-obj-health-report), [MEM-RTE-note-withdrawal](#mem-rte-note-withdrawal) and the migration annotation.

## Read-back

Search and topic context are caller-triggered pulls; indexing/watchers push changes into retained stores, not unsolicited note bundles into a model window. Query cache selects by query hash; similarity/FTS/graph/date lanes select indexed content; full reads select a resolved identifier. Identity selects derived facts by keys and projects them as text. Placement consumes dense retained centroids internally. These consumers have different authority: selector code mechanically changes result/placement; external agents merely receive text under an unobserved client policy (SRC-1, `src/search.rs`, `src/context.rs`, `src/placement.rs`, `src/identity.rs`; linked records above).

Only topic context has the inspected shared budget mechanism. Search counts results; who/project/full reads are not thereby bounded to the same context budget. Project children are pointers/metadata and tasks rather than all their bodies. Saved snippets are readable summaries of chunks, not the full vector's input; reranker/extractor decisions cannot be assumed to inspect omitted text. Reload is afforded and wired through read/read_section, but caller use is unobserved ([MEM-RTE-vault-readback](#mem-rte-vault-readback), [RT-RTE-topic-context](runtime.md#rt-rte-topic-context)).

## Integration issues

1. **Centroid aggregation cannot be treated as one coherent full-vault mean.** [MEM-OBJ-folder-centroids](#mem-obj-folder-centroids) retains the batch indexer's first-component/chunk-count grouping versus create/watch parent-folder/file-mean updates. SRC-1 `src/indexer.rs`, `src/watcher.rs`, `src/store.rs` supply contrary witnesses. This qualifies any stronger placement-learning/accounting inference; the supplied runtime did not itself assert that invariant.
2. **Identity refresh is not every-event refresh.** [MEM-RTE-identity-context](#mem-rte-identity-context) finds extraction in full indexing, not routine watcher branches. SRC-1 `src/identity.rs`, `src/indexer.rs`, `src/watcher.rs`. Saved facts may outlast source edits/withdrawal; no immediate current-state guarantee follows from [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh).
3. **Lifecycle operations require the split above.** [MEM-RTE-note-withdrawal](#mem-rte-note-withdrawal) is explicitly part of [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), not a competing replacement. Soft delete, archive and hard delete differ in retained row/content cleanup (SRC-1 `src/writer.rs`). Archive loses original frontmatter fields, and unarchive is restoration of body/tags/location rather than every original metadata field. Exact residual vec/FTS behavior of soft delete and all auxiliary cleanup remains unresolved; this prevents a complete-erasure conclusion.
4. **Feedback is a material subroute, not duplicate index refresh.** [MEM-RTE-placement-feedback](#mem-rte-placement-feedback) is part of [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh). Recognition excludes http-api and requires suggestion metadata. Numerical results and raw correction logs have different later consumers. No strong all-moves or human-correction reading is supported (SRC-1 `src/placement.rs`, `src/writer.rs`, `src/watcher.rs`).
5. **Health label overstates stale detection.** [MEM-OBJ-health-report](#mem-obj-health-report) retains the implementation stub despite the advertised stale-note diagnostic (SRC-1 `src/health.rs`, `src/serve.rs`, `skills/engraph/SKILL.md`). An empty report must not serve as a freshness evaluation or approval gate.
6. **Opaque/untraced parts remain local limits.** [MEM-OBJ-cli-event](#mem-obj-cli-event) has storage/prune APIs but unresolved producer/consumer wiring; full profile detection, all unresolved-link cleanup, standalone graph output and external agent handling are not fully inspected. These prevent telemetry-learning, exhaustive diagnostic freshness, detection-correctness and client-activation conclusions, not the positive routes established here.
7. **No duplicate declarations intended.** Existing cache/search/context/setup/migration referents are annotated, not re-declared. New objects are retained inputs or results, distinct from those supplied routes. [MEM-RTE-vault-readback](#mem-rte-vault-readback) covers non-search read alternatives and [MEM-RTE-identity-context](#mem-rte-identity-context) the extraction-to-format chain. Their overlap with supplied setup/index/query routes is causal linkage, not identical endpoints/progression.

## Limitations and checks

Only SRC-1 implementation and doctrine/design were used. Source HEAD and exact run/source identities were rechecked; no new source register entry, outside commit or live content was added. Authoring used the supplied contracts, not prior analyses or KB adoption theory. No observed-run or causal-experiment evidence supports operation, quality, human approval, learning benefit or downstream behavior.

The report does not claim exhaustive code auditing. Coverage retains available-but-uninspected details beside their prevented conclusions. Countercases inspected include lossy FTS versus full body, semantic bypass by type/explicit folder, centroid writer mismatch, HTTP author-label exclusion, ordinary watcher versus full-rescan identity refresh, soft delete versus archive, and the stale-detection stub. These constrain source labels without erasing wired positives.

Validation: required validate-output check passed: “Member content check passes; invocation residue not checked.” This is not job acceptance, claim support or successful target operation.
