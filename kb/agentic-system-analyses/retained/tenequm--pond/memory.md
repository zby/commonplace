---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Pond archival memory: canonical traces, selective recall, embeddings, checkpoint carriers and fidelity-limited restoration."
run-id: AAS-2026-10-14-pond-7a589a889ca1-01
source-identity: "https://github.com/tenequm/pond"
reviewed-boundary: "0c440e130faf44052d0d896a585e572090079f1f"
---

# Pond memory report

## Boundary and evidence

Pond retains agent-session evidence and reloads it into later work. This report covers the whole-system boundary's memory surfaces: adapter and HTTP admission, canonical tables, derived search text and embeddings, local access metadata, maintenance, copy/archive import, projected recall tools, SQL, and restored-session consumers. It does not treat Pond as the host's reasoning or compaction runtime. External model/harness internals, remote storage internals and deployed access controls remain outside the frozen source. They prevent conclusions about original summary generation, host interpretation, exact external model artifacts and operational reliability.

The source is SRC-1 at `0c440e130faf44052d0d896a585e572090079f1f`, as registered in [boundary](boundary.md). HEAD was rechecked and the source checkout was clean. Direct reads add implementation coverage of `packages/pond/src/wire.rs`, `packages/pond/src/sessions.rs` search-text, view, blob, embedding, archive, copy and cleanup ranges; `packages/pond/src/rowmap.rs` layout; `packages/pond/src/syncstate.rs` cursor/last-sync persistence; `packages/pond/src/main.rs` cursor, reconciliation and embedding stages; Pi codec replay/carrier/reconstruction; OpenClaw checkpoint/carrier/reconciliation paths; search planning and restore lineage in `packages/pond/src/handlers.rs`; and Pi schema budgets. Direct doctrine/design and reported-operation reads cover `packages/pond/SKILL.md`, `docs/benchmarks/recall-context-cost.md` and its measuring script. Supplied runtime records, not new direct inspections, establish transport registration, host tool wiring and most CLI dispatch. No executable, target test, model or benchmark was run.

### Coverage inventory

“Supplied” identifies runtime evidence, not independent reinspection. All paths below are SRC-1 implementation unless otherwise marked. Available but uninspected paths are not access gaps.

| Entry point or memory operation | Source paths and inspection basis | Records or local limit |
|---|---|---|
| CLI/server/scheduled sync and HTTP canonical ingest; adapter configuration | Supplied `packages/pond/src/main.rs`, `packages/pond/src/schedule.rs`, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`; direct canonical schema and cursor reads | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-adapter-config](runtime.md#rt-rte-adapter-config), [MEM-OBJ-sync-cursor](#mem-obj-sync-cursor). Software admission is not per-content human approval. |
| Canonical session/message/part and opaque provider payload retention | Direct `packages/pond/src/wire.rs`, `packages/pond/src/sessions.rs` | [MEM-OBJ-session](#mem-obj-session), [MEM-OBJ-message](#mem-obj-message), [MEM-OBJ-part](#mem-obj-part), [MEM-OBJ-raw-record](#mem-obj-raw-record). Codec completeness remains local to each adapter. |
| Pi source compaction/checkpoint carriers and native/foreign reconstruction | Direct `packages/pond/src/adapter/pi_coding_agent.rs` | [MEM-OBJ-checkpoint-carriers](#mem-obj-checkpoint-carriers), annotation on [RT-RTE-session-restore](runtime.md#rt-rte-session-restore). Original model generation is opaque; reconstruction can omit carriers. |
| OpenClaw summary carriers, successor/checkpoint metadata and deletion classification | Direct selected ranges of `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/main.rs` | [MEM-OBJ-checkpoint-carriers](#mem-obj-checkpoint-carriers), [MEM-RTE-deletion-detection](#mem-rte-deletion-detection). File/DB recovery completeness is not audited. |
| Other registered codecs | Supplied seam in `packages/pond/src/adapter/mod.rs`; available `agy.rs`, `claude_ai_export.rs`, `claude_code.rs`, `claude_desktop_app.rs`, `codex_cli.rs`, `devin.rs`, `grok_build.rs`, `hermes.rs`, `letta_code.rs`, `nanoclaw.rs`, `oh_my_pi.rs`, `opencode.rs` under that directory not individually inspected | Shared admission/consumer facts apply; raw-record coverage, injected/conversational mapping, opaque state, summary alternatives and round-trip completeness remain uninspected per codec. No universal losslessness or exhaustive checkpoint claim follows. |
| FTS/vector search and get-session/get-message projections | Direct `packages/pond/src/sessions.rs`, `packages/pond/src/handlers.rs`; supplied renderer/MCP wiring | [MEM-OBJ-search-text](#mem-obj-search-text), [MEM-OBJ-message-vector](#mem-obj-message-vector), annotation on [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall). Search scope differs from retained scope. |
| Pi/OpenClaw/Hermes registration, prompts and scope policy | Direct Pi schema and recall skill; supplied `packages/pi-pond/src/tools.ts`, `packages/openclaw-pond/src/tools.ts`, `packages/hermes-pond/tools.py` and service paths | [RT-BAP-recall-guidance](runtime.md#rt-bap-recall-guidance), [RT-RTE-openclaw-tools](runtime.md#rt-rte-openclaw-tools), [MEM-BAP-recalled-history](#mem-bap-recalled-history). No Pond-owned automatic context push is established by these requested tools. |
| SQL and export files | Supplied `packages/pond/src/sql.rs`, `packages/pond/src/transport.rs`, CLI SQL | [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql). Export storage exists; later consumption of export files is uninspected. |
| Inline embedding, backlog/force embedding and index maintenance | Direct `packages/pond/src/embed.rs`, `packages/pond/src/main.rs`, `packages/pond/src/sessions.rs`; supplied loader | [MEM-RTE-message-embedding](#mem-rte-message-embedding), [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder). Model ID is not immutable weight identity. |
| Row-meta cache, cursor fallback, storage compaction/cleanup | Direct `packages/pond/src/rowmap.rs`, `packages/pond/src/syncstate.rs`, `packages/pond/src/main.rs`, `packages/pond/src/sessions.rs` | [MEM-OBJ-row-meta](#mem-obj-row-meta), [MEM-RTE-sync-watermarks](#mem-rte-sync-watermarks). These control lookup/capture, not host summarization. |
| Store copy, clean archive export/import, public library writes | Direct `packages/pond/src/sessions.rs`; supplied library/CLI surface | [MEM-RTE-archive-transfer](#mem-rte-archive-transfer). Library upserts and import do not universally inherit wire validation; caller-specific human control is unresolved. |
| Restore and Pi session switch | Direct Pi codec and shared lineage; supplied writer/bridge | [RT-RTE-session-restore](runtime.md#rt-rte-session-restore), [RT-BAP-session-switch](runtime.md#rt-bap-session-switch). Host parse/continuation is unobserved. |
| Retrieval evaluation | Direct `docs/benchmarks/recall-context-cost.md`, `docs/benchmarks/recall-context-cost.sh` | [MEM-CLM-context-cost](#mem-clm-context-cost). Remaining package tests, benches, `ops/search-benchmarks/` and `ops/e2e/` not inspected here; no broad recall-quality or task-success conclusion. |
| Fleet producer/sidecar and adapter-development procedure | Supplied boundary/runtime `ops/examples/pi-fleet/worker.sh`, compose and `skills/pond-add-adapter/SKILL.md` | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-adapter-development](runtime.md#rt-rte-adapter-development). No observed deployment or autonomous capability revision. |

`packages/pond/src/memory.rs` was read to challenge its name: it trims allocator pages, not model-visible context. It does not establish a second agent-memory store. Supporting publication/build files stay within the boundary without supplying a separate memory loop.

## Core ideas

1. **Retention is wider than recall.** Canonical parts preserve tool bodies, reasoning, files and injected material; `search_text` admits only a narrower conversational projection. Summary-only retrieval omits file bytes, while message-target, export and restore readers load full parts. A search miss cannot establish archive absence. See [MEM-OBJ-part](#mem-obj-part) and [MEM-OBJ-search-text](#mem-obj-search-text).
2. **Derived numerical memory changes selection, not the embedder's parameters.** Message vectors persist and affect later semantic search. They derive from filtered, token-limited text, not the whole episode. Backlog/force embedding is a separate maintenance admission path. See [MEM-RTE-message-embedding](#mem-rte-message-embedding) and [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder).
3. **Historical roles are not present authority.** Tool-result recall presents prior statements as evidence for the host model to interpret. Restoration instead serializes history into a host session file; source format and fidelity determine what survives. Neither route establishes factual correctness or reliable behavioral adoption. See [MEM-BAP-recalled-history](#mem-bap-recalled-history) and [RT-BAP-session-switch](runtime.md#rt-bap-session-switch).
4. **Archiving a summary is not performing compaction.** Pi/OpenClaw summaries and checkpoint metadata are source-fed history. Native Pi replay can carry them into a host loader; foreign reconstruction drops System carriers. This counterexample prevents an inference from stored checkpoint to every later consumer receiving it. See [MEM-OBJ-checkpoint-carriers](#mem-obj-checkpoint-carriers).
5. **Withdrawal and cleanup have different targets.** Deletion reconciliation reports candidates without removing canonical content. Old-version cleanup reclaims superseded physical storage, not a semantic retraction. Retained early conclusions also remain searchable; the shipped recall skill asks the model to read the end rather than rewriting those claims. See [MEM-RTE-deletion-detection](#mem-rte-deletion-detection) and [RT-OBJ-prompt-guidelines](runtime.md#rt-obj-prompt-guidelines).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-session
Label: Session

Source-native `Session` is symbolic identity/lineage and access metadata: ID, parent session/message pointers, source agent, timestamp, project and provider options. Storage: canonical Lance sessions table. Lineage comes from codecs or canonical callers; unresolved parents are not repaired into an invented history. Consumers include search filters/grouping, gets, copy and restore lineage. This metadata controls deterministic selection and reconstruction, not the truth of transcript content. Distinct from [RT-OBJ-adapter-config](runtime.md#rt-obj-adapter-config): stored-session metadata versus future capture configuration. SRC-1, `packages/pond/src/wire.rs`, `packages/pond/src/handlers.rs`.

> pub parent_message_id: Option<String>,
>     pub source_agent: String,
>     pub created_at: DateTime<Utc>,
>     pub project: Extracted<String>,
> --- `packages/pond/src/wire.rs`

#### MEM-OBJ-message
Label: Message

Source-native `Message` records symbolic role, ID, session, timestamp and options; System carriers additionally carry optional source text. Storage: Lance messages table. Text content is natural-language material interpreted by later humans/models, while schema fields are consumed by fixed rules. Original authorship can mix users, models, harness code and tools; a role/source-agent label alone does not resolve that mixture. Consumers: get, SQL, restoration and derived search projection. This is the retained result of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), not that route's identity. No supplied object counterpart after comparison. SRC-1, `packages/pond/src/wire.rs`; admission evidence is in the supplied capture record.

> pub enum Message {
>     System {
> --- `packages/pond/src/wire.rs`

#### MEM-OBJ-part
Label: Part

Source-native `Part` stores ordered message content and explicit conversational/injected provenance in Lance parts. Symbolic tags/links and JSON tool arguments/results coexist with natural-language text/reasoning. File data may be bytes, string or URL; its readable name/MIME summary is not its opaque payload. Original content is source-fed, not a Pond-authored factual digest. Consumers differ: summary-only search/session views inspect metadata; message targets, export and restore inspect complete parts, including file blobs. Storage admission does not warrant a tool result or reasoning statement as correct. Distinct from [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall): stored part versus read-back operation. No supplied object counterpart. SRC-1, `packages/pond/src/wire.rs`, `packages/pond/src/sessions.rs`.

> /// Every part of these messages, full fidelity (file blobs included). The
>     /// canonical read primitive - restore/export, verbatim mode, and the
>     /// message-mode target all need the complete set.
> --- `packages/pond/src/sessions.rs`

> // Summary reads (search hits, conversational view) need only the part
>         // metadata in `variant_data` to build a `PartSummary` - never the file
>         // blob - so they skip the `_rowaddr` + `take_blobs` round trip. Only
>         // full-fidelity callers (restore/export/message-mode) read the blobs.
> --- `packages/pond/src/sessions.rs`

#### MEM-OBJ-raw-record
Label: Source raw record

Source-native `options.source.raw_record` retains a symbolic JSON source row in canonical session/message options for the inspected Pi codec. Its payload may include natural-language content or opaque harness state. It is source evidence distinct from the readable extracted carrier summary, and not a guarantee that every codec retains every upstream state. Pi's native replay reader uses source order and complete raw rows; absence of any required raw row disables that replay. SQL can expose options; ordinary conversational views do not imply delivery of this payload. Distinct from [RT-RTE-session-restore](runtime.md#rt-rte-session-restore): a retained input part, not the restoration route. No supplied object counterpart. SRC-1, `packages/pond/src/adapter/pi_coding_agent.rs`.

> let mut records = vec![raw_record(&session.session.options)?];
> --- `packages/pond/src/adapter/pi_coding_agent.rs`

> records.push(raw_record(message.message.options())?);
> --- `packages/pond/src/adapter/pi_coding_agent.rs`

#### MEM-OBJ-checkpoint-carriers
Label: Compaction and branch-summary carriers

Pi v3 compaction and OpenClaw compaction/branch-summary rows become System carriers with source `summary` text; raw options preserve the surrounding record. Representational form: natural-language summary plus symbolic checkpoint/lineage fields; storage: canonical messages/options. These are already-derived upstream traces, not fresh Pond summarization. Original generation, retained reasons and exact host compaction policy remain uninspected. Pi native v3 replay can deliver the original record to the host; Pi reconstruction omits System carriers. OpenClaw checkpoint metadata supplies cut-point lookup, with conflicting parent mappings removed rather than guessed. This does not imply the summary is indexed: System roles are excluded from `search_text`. Distinct from [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) and [RT-RTE-session-restore](runtime.md#rt-rte-session-restore): specific retained alternatives shared by those routes; no supplied object counterpart. SRC-1, `packages/pond/src/adapter/pi_coding_agent.rs`, `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/sessions.rs`.

> Some("compaction") | Some("branch_summary") => vec![carrier(
>             session_id,
>             &id,
>             seq,
>             timestamp,
>             value,
>             extract_str(value, "summary"),
>         )],
> --- `packages/pond/src/adapter/openclaw.rs`

> for parent_id in ambiguous {
>         found.remove(&parent_id);
>     }
> --- `packages/pond/src/adapter/openclaw.rs`

#### MEM-OBJ-search-text
Label: SearchText

Source-native `search_text`/`SearchText` is a natural-language and file-label projection stored on Lance message rows and cached in the row-meta map. Deterministic derivation joins non-empty conversational User/Assistant text and file name/MIME/URL fields. It excludes injected scaffolding, tool/system bodies, reasoning and file bytes. FTS reads this text; embedding transforms the same projection. Gets of conversational sessions also select rows with this projection. This is derived recall material, not extracted beliefs or revised instructions. Distinct from [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall): its retained selector input; no supplied object counterpart. SRC-1, `packages/pond/src/sessions.rs`.

> // spec.md#search: only conversational parts contribute to the indexed
>         // text; harness-injected scaffolding is excluded from search.
>         if part.provenance != Provenance::Conversational {
>             continue;
>         }
> --- `packages/pond/src/sessions.rs`

> let text = chunks
>         .into_iter()
>         .filter(|chunk| !chunk.trim().is_empty())
>         .collect::<Vec<_>>()
>         .join("\n");
> --- `packages/pond/src/sessions.rs`

#### MEM-OBJ-message-vector
Label: Message vector and embedding model

Dense message vectors are distributed-parametric representations stored with symbolic `embedding_model` metadata in Lance messages, separate from [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder)'s weights. They derive from `search_text` through passage formatting and bounded inference. Later vector search consumes them to rank retained messages; no direct instruction authority attaches to a vector. The model-ID label supports stale-model checks but cannot detect changed weights behind the same mutable ID. Source text remains separately reloadable. No supplied object counterpart; numerical outputs are explicitly distinguished from weights by the supplied component. SRC-1, `packages/pond/src/embed.rs`, `packages/pond/src/sessions.rs`.

> /// Fills `messages.vector` / `messages.embedding_model` for the backlog of
> /// un-embedded messages. Reads `messages.search_text` directly, batches it
> /// through the backend one vector each, and writes each batch back to
> /// `messages` by primary key.
> --- `packages/pond/src/embed.rs`

#### MEM-OBJ-row-meta
Label: RowMetaMap

Source-native row-meta map stores symbolic row/session/message IDs, role/project/source/timestamps/counts/watermarks and compressed natural-language `search_text`. Substrate: local version-keyed mmap files, dictionary encoding and zstd blocks, resident read-only snapshots and delta chains. It derives from canonical rows; it is a lookup/access cache rather than another curated account of a session. Consumers resolve FTS/vector hits, hydrate metadata and provide sync watermarks. Version/probe validation and miss fallback constrain stale cache use; segment compaction rebuilds this cache, not host context. Distinct from [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall): local read substrate; no supplied counterpart. SRC-1, `packages/pond/src/rowmap.rs`, `packages/pond/src/sessions.rs`.

> //! Memory-mapped, process-shareable per-message meta map keyed by stable
> //! `row_id`. Resolves FTS/vector `_rowid`s to `(session_id, message_id)` and
> //! hydrates hit meta (`role`, `project`, `source_agent`, `timestamp`,
> //! `search_text`) in memory, with a `take_rows` miss-fallback for rows appended
> //! since the build. Also carries a `session_id -> message count` aggregate.
> --- `packages/pond/src/rowmap.rs`

#### MEM-OBJ-sync-cursor
Label: SyncCursor and last-sync record

Source-native `SyncCursor` is symbolic store lineage plus per-session watermarks in local JSON state keyed by store. Last-sync JSON separately records completion time, duration, counts, outcome and optional error for status readers; it is not transcript content. Cursor lineage derives from a store-validated row-meta snapshot and store probe. A later restarted sync can use it as a `SkipOracle` when the map is unavailable; a mismatched store causes discard. Temp/rename writes avoid partial JSON delivery. These retained metadata change capture decisions, not the host model's instructions. Distinct from [RT-OBJ-adapter-config](runtime.md#rt-obj-adapter-config): observed storage progress versus configured source eligibility. SRC-1, `packages/pond/src/syncstate.rs`, `packages/pond/src/main.rs`.

> pub(crate) struct SyncCursor {
>     pub messages_version: u64,
>     pub row_count: usize,
>     pub oldest_messages: Vec<(u64, String)>,
>     pub watermarks: BTreeMap<String, i64>,
> }
> --- `packages/pond/src/syncstate.rs`

### Routes

#### MEM-RTE-message-embedding
Label: Canonical message embedding

Configured inline ingest or maintenance backlog → `search_text` → `passage:` formatting → fixed loaded embedder inference → key-addressed vector/model merge or initial append → later vector-search selector. Rust chooses eligible rows and owns writes; human configuration/force flags are not content-by-content vector approval. This is a material transformation within the supplied capture and maintenance account, not a replacement for [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). SRC-1, `packages/pond/src/embed.rs`, `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`; component fixity/512-token bound are in [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Embedded append/update batches and progress summary; provider/shape/store errors can stop the stage.
- Later read-back: Later query embeddings are compared with retained message vectors to select transcript hits.
- Delegated visibility: inapplicable — no worker dispatch; selected readable text returns through requested recall.
- Selection predicate: Non-null search text with missing embedding model; force maintenance also selects rows whose model ID differs from current configuration.
- Invalidation or expiry: Force/model-swap path drops the vector index and re-embeds stale-ID rows; same-ID upstream artifact drift is not identified by this predicate.
- Activation or effect: Numerical rows and subsequent ranking capacity change; downstream task improvement is unobserved.
- Evidence limits: Weight revision is not pinned; token truncation and pre-embedding projection omit source content; inference and benefit were not executed.

Admission: software checks backend result count/vector width and store keys; user can choose configuration/force or cancel a maintenance stage. Model inference produces values but does not judge admission. Rejection leaves a later backlog/retry opportunity; completed batches remain durable. No task-answer oracle; open maintenance, not a theory revision experiment. Guidance is configured model/passage format; vectors and model labels persist, not an explanation of their semantics. Raw traces → filtered text → vectors → later selector is an automatic trace-fed update affecting retrieval, but it does not establish improved capacity, parameter training or a revised operational method.

> if vectors.len() != chunk.len() {
>             return Err(anyhow!(
>                 "backend returned {} vectors for {} messages",
>                 vectors.len(),
>                 chunk.len(),
>             ));
>         }
> --- `packages/pond/src/embed.rs`

#### MEM-RTE-sync-watermarks
Label: Sync watermark persistence and reuse

Store-validated row-meta snapshot → persisted cursor → restarted sync's fallback oracle → configured adapter freshness decisions. Rust owns derivation, lineage checks and discarding invalid metadata. This extends [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)'s selection detail; distinct identity is the cross-invocation access-metadata route, not canonical content admission. SRC-1, `packages/pond/src/main.rs`, `packages/pond/src/syncstate.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Best-effort local cursor write or warning; sync continues without inventing a snapshot when none is validated.
- Later read-back: A restarted sync can read timestamps to skip fresh source sessions without rebuilding the row map first.
- Delegated visibility: inapplicable — local capture planner, not a reasoning-worker boundary.
- Selection predicate: Prefer the rowmap oracle; fallback requires cursor version/count not ahead of store and matching oldest-message lineage.
- Invalidation or expiry: Failed lineage comparison removes the cursor; stale but validated trailing progress costs rereads rather than admitting a guessed newer watermark.
- Activation or effect: Software capture planning depends on retained progress; model behavior is not a consumer of the cursor.
- Evidence limits: Every codec's freshness implementation and actual cross-process operation remain uninspected.

Admission is software snapshot/probe validation, with no per-watermark human decision or answer oracle. Open sync is the operating mode. Recovery uses a usable map or rereads when metadata is absent/invalid; this is not semantic curation.

> if cursor.messages_version <= current_version
>         && cursor.row_count <= probe.row_count
>         && cursor.oldest_messages == probe.oldest_messages
>     {
>         return Some(cursor);
>     }
> --- `packages/pond/src/main.rs`

#### MEM-RTE-archive-transfer
Label: Store copy and clean archive transfer

Operator/library caller → source store delta plan or clean Lance archive → schema/key admission and per-table writes → destination canonical rows → later recall/restore. Rust owns table I/O; caller decides source/destination, with human control unresolved for unspecified library callers. Distinct from [RT-RTE-session-capture](runtime.md#rt-rte-session-capture): bulk table transfer rather than adapter/wire-event validation. SRC-1, `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-table row/insert counts or an error; clean export creates self-contained staged datasets and source-version metadata.
- Later read-back: Destination stores expose imported content to search/get/SQL/restore; standalone export consumers beyond import are uninspected.
- Delegated visibility: inapplicable — data transfer, not reasoning delegation.
- Selection predicate: Delta plan distinguishes absent/grown sessions; clean import validates all table schemas before starting table writes.
- Invalidation or expiry: Separate table commits admit partial progress on later failure; old-version cleanup is distinct from withdrawing canonical rows.
- Activation or effect: Durable corpus availability changes; transfer itself does not demonstrate improved answers.
- Evidence limits: Cross-table snapshot atomicity, every compatibility/backfill case and external store concurrency are not independently verified.

Admission is schema/plan/store software checks, not per-content human fact review. Caller can refuse the operation; no task-answer oracle. Open backup/maintenance mode. Recovery is later retry/completion, not universal rollback. Copy/archive paths share optional embedding maintenance but do not imply every row passed `IngestValidator`.

> // Validate every table's schema before importing any: a
>         // mixed-compatibility archive must fail whole, not half-restore.
> --- `packages/pond/src/sessions.rs`

> // The three tables are independent Lance datasets with separate write
>         // locks, so copy them concurrently - mirrors the ingest path's
>         // three-table `try_join!` (see `upsert_session_batch`).
> --- `packages/pond/src/sessions.rs`

#### MEM-RTE-deletion-detection
Label: OpenClaw deletion detection without withdrawal

Configured sync → deleted-archive enumeration + stored session/project + live-entry probe → erase/preserve report → sync summary. Software classifies suspected upstream intent; Pond does not enact that intent in this path. Distinct from [RT-RTE-session-capture](runtime.md#rt-rte-session-capture): post-capture diagnostic output rather than content deletion. SRC-1, `packages/pond/src/adapter/openclaw.rs`, `packages/pond/src/main.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Erase candidates and preserve reasons in human/JSON sync output.
- Later read-back: Canonical rows remain available to later recall and restore because detection does not purge them; later consumption of the report itself is uninspected.
- Delegated visibility: inapplicable — diagnostic report, not worker delivery.
- Selection predicate: Configured reconciliation and discoverable deleted files; main-session key with absent live entry can become an erase candidate; machine-generated sessions and ambiguous/unreadable cases preserve.
- Invalidation or expiry: No canonical expiry is enacted; multiple configured roots downgrade erase candidates to preservation due to cross-root ambiguity.
- Activation or effect: Summary/report changes, not removal or denial of read-back.
- Evidence limits: Missing derived deletion files prevent enumeration; original deletion intent is inferred by rules, not authenticated human approval.

Decision/oracle: deterministic classification uses live-entry presence as a reference outcome, not expected task answers. Upstream human deletion is distinguishable from automatic retention only to the extent source markers and probes permit it. Operating mode is open sync diagnosis. Rejection/withdrawal of retained content is not implemented by this route; its safety fallback is preservation. The report's label `erase` is a proposal, not effect.

> // a non-openclaw sync pays nothing. Detection-only - it names the erase
>     // set and preserves for the summary; the byte-purge waits on `pond erase`.
> --- `packages/pond/src/main.rs`

> /// names every action for the sync summary and returns the erase set; the
>     /// actual byte-purge + denylist is the caller's `pond erase` step
>     /// (spec.md#session-append-only-exception), never performed here and never
>     /// over MCP.
> --- `packages/pond/src/adapter/openclaw.rs`

### Claims

#### MEM-CLM-context-cost
Label: Reported first-read context cost

SRC-1 reports a smaller first useful Pond response than a median matching transcript for five author-selected queries on one corpus/machine. Evidence layer: reported operation, not observed execution at this pin or causal downstream benefit. The measuring script runs search/grep and byte counts into temporary files and prints a table; no feedback from those measurements into archive admission, embedding revision or prompt revision is established. Distinct from [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall): evaluation claim rather than consumer wiring. SRC-1, `docs/benchmarks/recall-context-cost.md`, `docs/benchmarks/recall-context-cost.sh`.

> - One corpus, one machine, five queries, chosen by the author. This measures
>   the shape of the problem, not a universal constant.
> - Tokens are approximated as bytes/4, not tokenizer-counted.
> --- `docs/benchmarks/recall-context-cost.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-recalled-history
Label: Retrieved history as host evidence

Consumer: requesting host model/human. Channel: rendered search/session/message/SQL tool result containing selected historical content. Force: evidence interpreted by the consumer, not a Pond-certified instruction or enforced answer; stored System/User/Assistant tags do not by themselves confer present system-prompt authority. Horizon: later requests/turns across archived sessions. This is distinct from [RT-BAP-recall-guidance](runtime.md#rt-bap-recall-guidance)'s static recall policy and [RT-BAP-session-switch](runtime.md#rt-bap-session-switch)'s executable session handoff. Supplied [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall) provides delivery/clipping passages. SRC-1, `packages/pond/src/handlers.rs`, `packages/pi-pond/src/tools.ts`, `packages/pond/SKILL.md`. Actual adoption, correctness and changed behavior remain unobserved.

## Annotations

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Retained results are [MEM-OBJ-session](#mem-obj-session), [MEM-OBJ-message](#mem-obj-message), [MEM-OBJ-part](#mem-obj-part) and optional source rows/carriers. Natural-language bodies, symbolic metadata and numerical vector outputs have different consumers. Authorship occurs upstream; admitted content can mix humans, models, harnesses and tools. Physical writes and schema/key software admission do not establish human approval of statements. Later search uses [MEM-OBJ-search-text](#mem-obj-search-text), not all retained parts. Supplied recovery passage supports additive persistence, not universal codec completeness. SRC-1, `packages/pond/src/wire.rs`, `packages/pond/src/sessions.rs`.

#### On [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall)

Read-back is requested, not an independent unsolicited push: model/user selects query/ID, code selects retained rows and projection, renderer/plugin delivers copied text. Search candidate over-fetch, grouping, relevance/recency and subagent exclusion affect which retained parts survive. Direct planning caps requested limits and widens the candidate pool; Pi defaults to 10 and clamps to 25, then clips relayed body bytes at 32 KiB before adding its truncation notice. These are byte/result bounds, not tokenizer guarantees. Session views page the conversational subset by anchor/start/end and byte budget; message target readers can include full parts with bounded conversational neighbors. Returned IDs are explicit reload handles; they are not live window references with automatic dereferencing or liveness counting. Dropped context remains reachable through another request, not through Pond-managed host compaction. SRC-1, `packages/pond/src/handlers.rs`, `packages/pond/src/sessions.rs`, `packages/pi-pond/src/schemas.ts`; clipping passage is supplied by the runtime record.

> export const SEARCH_DEFAULT_LIMIT = 10;
> export const SEARCH_MAX_LIMIT = 25;
> --- `packages/pi-pond/src/schemas.ts`

> export const RESPONSE_MAX_BYTES = 32 * 1024;
> --- `packages/pi-pond/src/schemas.ts`

#### On [RT-RTE-session-restore](runtime.md#rt-rte-session-restore)

Full canonical parts and raw options feed codec serialization; readable search summaries are not the restore input. Direct Pi inspection narrows any generic same-origin/native expectation: only v3-origin plus Native request plus complete raw rows and captured path takes native replay. V4/SQLite origins reconstruct v3 with Foreign fidelity, and reconstruction drops System carriers while keeping them in canonical storage. Thus retained compaction summaries do not necessarily reach the switched host context. Original reasons and opaque state can survive raw records but are not guaranteed delivered after this transformation. Successful file write/session switch is still not evidence of host parsing or continuation. SRC-1, `packages/pond/src/adapter/pi_coding_agent.rs`, `packages/pond/src/sessions.rs`.

> let native_replayable =
>         session_format(&session.session) == V3_FORMAT && fidelity == RestoreFidelity::Native;
> --- `packages/pond/src/adapter/pi_coding_agent.rs`

> // A System carrier (a model/compaction record, or any harness-v2
>         // orchestration mutation) has no idiomatic home in a v3 transcript -
>         // drop it; the content stays in canonical
> --- `packages/pond/src/adapter/pi_coding_agent.rs`

## Write side

Acquisition and canonical admission are supplied by [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). Enabled paths and freshness state govern eligibility; validator schema/order and key checks govern admission. Human content authorship, operator enabling capture, software bootstrap and physical Rust writes are separate contributions. Conflicting labels can be rejected while new rows persist. Disabling an adapter changes future capture rather than withdrawing old rows. Direct library upserts and [MEM-RTE-archive-transfer](#mem-rte-archive-transfer) are alternative admission surfaces; they prevent extending wire-validation guarantees to every write.

Curation in the inspected code is extraction, normalization, searchable projection, embedding, metadata caching and native/foreign reconstruction. It is not automatically fact verification or a revised method. [MEM-RTE-message-embedding](#mem-rte-message-embedding) supplies a genuine automatic raw-to-derived-to-later-selector chain, whereas raw archival accumulation alone supplies no evidence of improved capacity. There is no rationale attached to a dense vector, although its input remains separately retained. A transcript may contain reasons or criticism, but Pond does not establish their correctness or demonstrate that a later model reads and adopts them.

Upstream summaries are an independent trace alternative. Pi/OpenClaw summary carriers and OpenClaw checkpoint cut-point metadata persist in [MEM-OBJ-checkpoint-carriers](#mem-obj-checkpoint-carriers). Unknown source-generation control does not suppress known subsequent extraction, replay and omission. Native replay can retain upstream context-state records; reconstructed Pi v3 omits System carriers. Other codecs' compaction/checkpoint alternatives are available but uninspected, preventing a universal raw-to-summary account.

Maintenance separates data/index-file compaction, index rebuild, optional backlog/re-embedding, rowmap delta compaction and superseded-version cleanup. Cleanup loops over tables with an age floor; its source comment protects live pinned readers. It does not semantically erase canonical content or retract earlier conclusions. SRC-1, `packages/pond/src/sessions.rs`:

> /// Reclaim superseded data/index files across every indexed table (Lance
>     /// `cleanup_old_versions`), without compaction. `pond optimize --rebuild`
>     /// runs this after the rebuild so the index segments it just replaced are
>     /// dropped immediately. The retention floor still protects versions a live
>     /// reader may have pinned (spec.md#concurrency).
> --- `packages/pond/src/sessions.rs`

[MEM-RTE-deletion-detection](#mem-rte-deletion-detection) rejects the stronger interpretation that detecting upstream deletion removes retained evidence. Its erase/preserve report is surfaced but bytes remain. Evaluation in [MEM-CLM-context-cost](#mem-clm-context-cost) measures output size rather than admitting/rejecting session claims; no measurement-driven artifact revision consumer was established. Adapter capability source changes follow the supplied development doctrine, not a traced automatic revision loop: [RT-RTE-adapter-development](runtime.md#rt-rte-adapter-development).

## Read-back

The ordinary host/model request uses [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall). FTS and vector modes select from the same narrower conversational projection, not all retained tool/system/reasoning/file content. Search supplies ranked/grouped snippets and IDs; get-session reads bounded conversational pages; get-message expands the selected target's parts and neighbors. The `PartSummary` rendering is a lossy display projection, not a newly retained model summary. Exact tool bodies and broader retained state remain available through message/SQL/full canonical readers. [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql) is an alternate selector, with optional export writes; a generic export-read method establishes storage ability, not a documented deployed consumer.

The source skill's “one call, full readable transcript” must be bounded by pagination, conversational selection and plugin clipping. Its “losslessly” claim cannot establish every codec/consumer's preservation. The source itself warns about temporal supersession: relevance can find a confident statement later overturned, and the model should request the end or recency sorting. There is no automatic semantic withdrawal of the early statement in the inspected path. SRC-1, `packages/pond/SKILL.md`:

> - Long sessions supersede their own early conclusions. For "what did we
>   decide / latest state", read the end (`pond_get_session(id, from="end")`)
>   or `pond_search` with `sort_by=recency` - relevance rank favors the early,
>   confident, possibly overturned phrasing.
> --- `packages/pond/SKILL.md`

Trust at recall is interpretive: archived role/provenance describes history, not source reliability or authenticated present authority. OpenClaw search scoping and subagent tool withholding are local host policy; targeted gets and direct entry points do not become universally scoped by that policy. Pi's whole-archive recall and Hermes's search filter preserve the supplied limits in [RT-RTE-openclaw-tools](runtime.md#rt-rte-openclaw-tools) and [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall). Static guidelines can request recall first, but they are not retained through use and do not themselves constitute a memory read-back route.

Restoration has a different consumer/channel: [RT-RTE-session-restore](runtime.md#rt-rte-session-restore) delivers files and [RT-BAP-session-switch](runtime.md#rt-bap-session-switch) passes the local file to Pi's loader. The source-supported omission above limits what that consumer receives. Copy/import preserves a destination corpus for subsequent recall, while [MEM-RTE-sync-watermarks](#mem-rte-sync-watermarks) reads retained access metadata into a capture planner. These later consumers are not all model consumers and do not share behavioral authority.

Working-context control consists of requested reload, projection, result/ranking limits, byte clipping, pagination and host-specific tool availability. The trigger is foreground request; deterministic code chooses the admitted response material. Pond does not own host trimming or subagent frames. Archive content is copied by value into tool results; omitted bodies stay on disk and require explicit re-request. This resembles external retained storage with requested loads, not a host stack frame whose return value alone escapes. Actual host frame isolation/compaction and whether native checkpoint replay changes the host window remain uninspected.

## Integration issues

- **Restore-fidelity refinement:** the supplied [RT-RTE-session-restore](runtime.md#rt-rte-session-restore) already says actual adapter output determines fidelity. Direct Pi evidence adds a consequential same-origin counterexample: v4/SQLite-origin restoration is reconstructed as v3/Foreign and omits System carriers. Keep the annotation when integrating; do not collapse archived summaries into universally delivered checkpoint state. Concerns [MEM-OBJ-raw-record](#mem-obj-raw-record), [MEM-OBJ-checkpoint-carriers](#mem-obj-checkpoint-carriers). SRC-1, `packages/pond/src/adapter/pi_coding_agent.rs`.
- **Capture/maintenance subroute overlaps:** [MEM-RTE-message-embedding](#mem-rte-message-embedding) and [MEM-RTE-sync-watermarks](#mem-rte-sync-watermarks) overlap [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)'s account but name distinct transformation/read-back chains. [MEM-RTE-archive-transfer](#mem-rte-archive-transfer) separates an alternate table admission mechanism; [MEM-RTE-deletion-detection](#mem-rte-deletion-detection) separates post-capture classification. They are not replacement candidates for the broader supplied capture referent. No object or authority-path duplicate was identified after comparison.
- **Codec coverage unknowns:** per-codec raw payload, injected/scaffold mapping, source summary/checkpoint alternatives and restore completeness remain uninspected outside the named Pi/OpenClaw ranges. The inventory preserves these included parts; do not infer exhaustive losslessness from [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) or [MEM-OBJ-part](#mem-obj-part). SRC-1, `packages/pond/src/adapter/mod.rs` and the available adapter paths listed above.
- **Source-origin/control uncertainty:** summary authorship, original compaction rationale and opaque harness payload semantics are not resolved by capture. Known storage/replay/omission facts survive this limit. Concerns [MEM-OBJ-checkpoint-carriers](#mem-obj-checkpoint-carriers), [MEM-OBJ-raw-record](#mem-obj-raw-record); host internals are outside SRC-1.
- **Mutable embedding identity:** model-ID stale checks cannot distinguish changed upstream weights behind the same ID. This qualifies numerical lineage in [MEM-OBJ-message-vector](#mem-obj-message-vector), not the supported fixed-loaded-inference account in [RT-CMP-candle-embedder](runtime.md#rt-cmp-candle-embedder). Exact external artifact revision remains uninspected.
- **Source marketing versus selected delivery:** full-readable/lossless skill labels do not override projection/page/byte/fidelity restrictions. Source recency instructions address contradictory historical conclusions but do not withdraw them. Concerns [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall), [MEM-BAP-recalled-history](#mem-bap-recalled-history). SRC-1, `packages/pond/SKILL.md`, `packages/pond/src/sessions.rs`, `packages/pi-pond/src/schemas.ts`.
- **No withdrawn-byte conclusion:** source restoration comments mention erased/denylisted sessions, but executable deletion reconciliation is detection-only and CLI output says erase is not yet implemented. Do not treat those comments as evidence of a live purge/denylist consumer. Concerns [MEM-RTE-deletion-detection](#mem-rte-deletion-detection), [RT-RTE-session-restore](runtime.md#rt-rte-session-restore). SRC-1, `packages/pond/src/handlers.rs`, `packages/pond/src/main.rs`, `packages/pond/src/adapter/openclaw.rs`.

## Limitations and checks

The whole-system boundary is unchanged, but this member is not an exhaustive codec, index or deployment audit. No required source was inaccessible; uninspected evidence and excluded dependency internals are named beside their prevented conclusions. Program/test/model execution was prohibited and not performed. Presence, wired delivery, behavioral adoption and task benefit remain separate. The cost report is attributed measurement with corpus/query/machine/method limits, not verification at this revision. No learning, autonomy or self-improvement claim follows from storing traces or deriving vectors alone.

Identity checks: the supplied run/source fields are repeated exactly; checkout HEAD equals the frozen revision and status is clean. Method identity is the supplied job, member types, collection contract, worker rules and records contract, read completely. Source text, not filenames or supplied route labels alone, was used to challenge full-transcript, same-origin-native, compaction, deletion and model-pinning interpretations.

Validation: completed with the invocation's deterministic validator; this establishes structure, citation resolution and quotation occurrence, not semantic acceptance or observed target behavior.
