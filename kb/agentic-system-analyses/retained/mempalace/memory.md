---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MemPalace memory mechanisms: normalized drawers, derived locators, diary checkpoints, temporal facts, media references and later context delivery."
run-id: AAS-2026-10-14-mempalace-ed71875aea5a-01
source-identity: "https://github.com/milla-jovovich/mempalace"
reviewed-boundary: "1392e1810c3ca67776bd7fe3e198788a96dbd6d1"
---

# MemPalace memory report

## Boundary and evidence

This member covers the shipped memory loop at SRC-1, commit 1392e1810c3ca67776bd7fe3e198788a96dbd6d1. The source identity and access root are declared in [boundary](boundary.md#source-register). The checkout HEAD was rechecked against that commit. Evidence is implementation plus explicitly labelled doctrine/design, not an executed palace, host session or benchmark. External providers and hosts remain outside the implementation boundary.

The memory scope includes import and automatic capture, manual tools, alternative extraction and checkpoint forms, organization and withdrawal, structured facts, native media references, coordination retention and model-context delivery. It excludes no shipped memory surface on functional grounds. Some included alternatives remain uninspected as identified below; they cannot inherit guarantees from the Chroma/Hermes route. Source searches covered CLI dispatch, hooks, MCP handler definitions, source adapters, layers, search candidates, graph state, cleanup, repair, WAL and evaluator entry paths. Direct source reads and supplied runtime findings are distinguished in the table. New records use SRC-1, not new source registrations.

| Entry point or operation | Paths in SRC-1 and inspection basis | Coverage and limits |
|---|---|---|
| CLI dispatch, project and conversation mining | Direct: `mempalace/cli/__init__.py`, `mempalace/cli/cmd_mine.py`, `mempalace/miner.py`, `mempalace/convo_miner.py`, `mempalace/normalize.py`, `mempalace/general_extractor.py` | [MEM-RTE-source-filing](#mem-rte-source-filing); exchange/general modes differ; individual export parsers and document-format miner remain incompletely inspected, preventing all-format fidelity conclusions. |
| Hermes completed turns and delegation capture | Supplied runtime: `mempalace/integrations/hermes/__init__.py`; direct filing inspection: `mempalace/convo_miner.py` | [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture); best-effort queue, not durable spool. Child task/result is not a complete child transcript. |
| Hook Stop/end/precompact and diary checkpoint | Direct: `mempalace/hooks_cli.py`, `mempalace/mcp_server/tools_diary.py`; supplied wrapper inventory in boundary | [MEM-RTE-diary-checkpoint](#mem-rte-diary-checkpoint), [RT-RTE-hook-ingest](runtime.md#rt-rte-hook-ingest). Every legacy shell wrapper, Cursor/Antigravity variant and DSH autosave implementation was not independently traced; host-specific completion guarantees remain unestablished. |
| Message-wise sweep | Direct: `mempalace/sweeper.py`, `mempalace/cli/cmd_mine.py` | [MEM-RTE-source-filing](#mem-rte-source-filing); independent timestamp cursor/ID regime can overlap file mining. |
| Add/update/delete/direct GET, bulk GET and checkpoint | Direct: `mempalace/mcp_server/tools_write.py`, `mempalace/mcp_server/tools_diary.py`; supplied full/light dispatch | [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch), [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance). Handler inspection does not establish a human caller or content approval. |
| Source adapter and media import | Direct: `mempalace/cli/cmd_mine.py`, `mempalace/sources/context.py`, `mempalace/media.py` | [MEM-RTE-media-index](#mem-rte-media-index). Adapter facade is constructed by executable CLI despite stale module prose saying otherwise. Third-party adapter internals remain opaque. |
| Closets, optional LLM regeneration | Direct: `mempalace/palace/closets.py`, `mempalace/closet_llm.py` | [MEM-OBJ-closet-lines](#mem-obj-closet-lines), [MEM-RTE-closet-regeneration](#mem-rte-closet-regeneration). These are locators, not a complete transcript or truth check. |
| Setup origin/entity registry | Supplied: `mempalace/cli/cmd_init.py`, `mempalace/entity_detector.py`; direct registry call sites in `mempalace/miner.py` and `mempalace/palace_graph.py` | [RT-RTE-init-detection](runtime.md#rt-rte-init-detection); editable people/projects and automatic topics differ. Original correctness is unresolved; later routing/link consumers are known. |
| Semantic, lexical and closet-assisted read | Direct: `mempalace/searcher/candidates.py`; supplied: `mempalace/searcher/query.py`, `mempalace/mcp_server/tools_read.py` | [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall); supplied ranking/fallback findings retained, not independently reproduced. |
| Startup context and layered recall | Direct: `mempalace/layers.py`, `mempalace/cli/cmd_query.py`; supplied Hermes and DSH consumers | [MEM-RTE-wake-context](#mem-rte-wake-context), [RT-BAP-agent-context](runtime.md#rt-bap-agent-context). Layer2 is an exposed filtered-read capability; no independent deployed caller is asserted. |
| Diary files and recent diary read | Direct: `mempalace/diary_ingest.py`, `mempalace/mcp_server/tools_diary.py`; doctrine: `integrations/shared/recall-protocol.md` | [MEM-RTE-diary-checkpoint](#mem-rte-diary-checkpoint). File summaries have caller-controlled/unknown authorship, unlike deterministic hook snippets. |
| KG add/query/invalidate/supersede | Direct: `mempalace/knowledge_graph.py`, `mempalace/mcp_server/tools_kg.py` | [MEM-RTE-temporal-facts](#mem-rte-temporal-facts). General extraction-to-KG automation and every maintenance rewrite caller are not fully traced; no universal fact extraction claim. |
| Hallways, tunnels and traversal history | Direct: bounded reads/searches of `mempalace/hallways.py`, `mempalace/palace_graph.py`, `mempalace/dynamics.py`, `mempalace/palace_audit.py`, `mempalace/cli/cmd_query.py` | [MEM-OBJ-tunnels](#mem-obj-tunnels), [MEM-RTE-tunnel-traversal](#mem-rte-tunnel-traversal). Hallway rebuild/prune and automatic topic/entity tunnel call sites are present; complete proposal/prune policy is not independently verified. No search-ranking benefit inferred. |
| Content cleanup and audit | Direct: `mempalace/sync.py`, `mempalace/mcp_server/tools_write.py`, `mempalace/cli/cmd_audit.py`; supplied user-approved audit doctrine | [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance). Sync conservatively retains unresolved sources; an audit score is not factual warrant. |
| Backend/native alternatives | Supplied registry/wrapper; bounded direct searches of `mempalace/backends/chroma.py`, `mempalace/backends/sqlite_exact.py`, `mempalace/backends/rust_exact.py`, `mempalace/backends/pgvector.py`, `mempalace/backends/qdrant.py`, `mempalace/backends/milvus.py`; Rust core remains uninspected | [MEM-OBJ-drawer-vectors](#mem-obj-drawer-vectors), [RT-RTE-backend-registration](runtime.md#rt-rte-backend-registration). Adapter names do not prove storage semantics, remote retention, encryption or deletion completeness. |
| Repair, backup, migration, export, replication | Direct bounded searches: `mempalace/repair.py`, `mempalace/backups.py`, `mempalace/replica.py`; direct read: `mempalace/logsync.py`, `mempalace/wal.py`; migration dispatch in `mempalace/cli/cmd_query.py` | [MEM-OBJ-write-log](#mem-obj-write-log). Rebuild/prune/archive capabilities are visible; full backup/restore/export/migration/native and replicated deletion semantics remain uninspected. No global erasure or recovery guarantee. |
| Task/event/artifact persistence and reload | Supplied: `mempalace/logstream.py`, `mempalace/tasks.py`, `mempalace/cli/cmd_coord.py`; direct anti-entropy read in `mempalace/logsync.py` | [RT-OBJ-task-request](runtime.md#rt-obj-task-request), [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact), [RT-RTE-task-launch](runtime.md#rt-rte-task-launch), [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery). Not all event types/artifact kinds or recipient workflows inspected; patch delivery is not installation. |
| Evaluators | Direct raw build/query path: `benchmarks/longmemeval_bench.py`; supplied broader evaluator inventory | Ground-truth session retrieval differs from live-loop recall; other modes, `benchmarks/model_eval/runner.py`, LoCoMo, ConvoMem, MemBench and soak/private-palace harnesses remain uninspected here. No result reproduction or production-loop validation. |

## Core ideas

1. **The stored text, access metadata and vectors do different work.** A drawer carries readable material. Wing/room/source/chunk fields route and reconstruct it. A dense embedding selects candidates. A closet is a separate lossy locator over source material. None of these alone certifies truth. See [MEM-OBJ-drawer-text](#mem-obj-drawer-text), [MEM-OBJ-drawer-metadata](#mem-obj-drawer-metadata), [MEM-OBJ-drawer-vectors](#mem-obj-drawer-vectors) and [MEM-OBJ-closet-lines](#mem-obj-closet-lines).
2. **“Verbatim” is relative to the retained representation.** The recall policy asks for exact stored words, but normalization can spell-correct user text, general extraction can omit segments, hook checkpoints retain short user-message prefixes, and delivery can return snippets. These counterexamples prevent an end-to-end byte-preservation interpretation without denying direct text storage. See [MEM-RTE-source-filing](#mem-rte-source-filing), [MEM-RTE-diary-checkpoint](#mem-rte-diary-checkpoint) and [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol).
3. **Continuity has several independent budgets.** L1 startup selection, recent diary rows, semantic result count, closet hydration and direct logical-drawer GET are different selectors. Small result counts do not impose a model token cap. Host compaction remains host-owned. See [MEM-RTE-wake-context](#mem-rte-wake-context) and the read-back annotations.
4. **Retention is editable, not automatically authoritative knowledge.** Explicit caller writes, automatic capture and generated indexes have different admission controls. Temporal facts preserve validity history; drawer edits/deletes purge source closets. Audit and dedup are structural/navigation controls rather than truth or answer oracles. See [MEM-RTE-temporal-facts](#mem-rte-temporal-facts) and [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance).

## Shared records

### Components

#### MEM-CMP-closet-provider
Label: Closet regeneration provider

Source-native identity: `LLMConfig` endpoint/model used by `_call_llm`. Representational form: external distributed-parametric generator behind symbolic request settings. Storage substrate: opaque provider weights/state and local response transient data; the retained product is closet text, not weights. The inspected client requests generation, not parameter updates. Exact weight revision is not pinned by `cfg.model`; a mutable HTTP endpoint can serve another model under that name. Provider-side parameter change and request retention are uninspected. Distinct from the setup classifier [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider): separate caller/configuration and retained product, even if an installation chooses the same service. SRC-1: `mempalace/closet_llm.py`.

> "model": cfg.model,
> "max_tokens": MAX_OUTPUT_TOKENS,
> "messages": [{"role": "user", "content": prompt}],
> --- `mempalace/closet_llm.py`

### Operative objects

#### MEM-OBJ-drawer-text
Label: Drawer text

Source-native identity: drawer `documents` content. Representational form: natural-language source/transcript/code text at its interpretive consumer; source code can separately have symbolic execution semantics, but retrieval here does not execute it. Storage substrate: configured backend document rows, Chroma in the supplied ordinary route. Lineage includes imported files, normalized conversations, direct caller content and captured user/assistant exchanges; it is not uniformly raw human speech. Text can retain reasons when the source/caller supplied them, but no reason field is required. Later search, full drawer GET, diary and wake-up may read different subsets. Authority is information for a host/agent, not enforced truth. This is the retained object selected by [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall), not a duplicate of that route. Supplied capture evidence also appears in [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture). SRC-1: `mempalace/convo_miner.py`, `mempalace/miner.py`, `mempalace/mcp_server/tools_write.py`.

> documents=batch_docs,
> ids=batch_ids,
> metadatas=batch_metas,
> --- `mempalace/convo_miner.py`

#### MEM-OBJ-drawer-metadata
Label: Drawer metadata

Source-native identity: drawer metadata dictionaries: wing, room, source, chunk index/total, timestamps, extract/normalize version, parent IDs and optional entity/provenance fields. Representational form: symbolic identifiers and control/access metadata, separate from the text they describe. Storage substrate: backend metadata rows/payloads. Lineage: miners and handlers construct fields; adapters can supply fields with core stamps. Actual consumers include source freshness/dedup checks, filters, chunk reconstruction, source cleanup and L1 ordering. These fields have software authority over inclusion and routing, not epistemic authority over the text. Source labels do not prove original authorship. Distinct retained part associated with [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch), whose content-hash/write checks do not establish truth. SRC-1: `mempalace/convo_miner.py`, `mempalace/sources/context.py`, `mempalace/layers.py`.

> "ingest_mode": "convos",
> "extract_mode": extract_mode,
> "normalize_version": NORMALIZE_VERSION,
> "id_recipe": ID_RECIPE,
> "chunk_total": chunk_total,
> --- `mempalace/convo_miner.py`

#### MEM-OBJ-drawer-vectors
Label: Drawer and locator vectors

Source-native identity: stored embeddings for drawer, closet or asset collections. Representational form: distributed-parametric numerical representations derived through inference, not revised model weights. Storage substrate: selected backend vector/index state. MiniLM, EmbeddingGemma, EmbeddingGemma2 and endpoint model identity/fixity limits are separately established by [RT-CMP-minilm](runtime.md#rt-cmp-minilm), [RT-CMP-embeddinggemma](runtime.md#rt-cmp-embeddinggemma), [RT-CMP-embeddinggemma2](runtime.md#rt-cmp-embeddinggemma2) and [RT-CMP-openai-compat](runtime.md#rt-cmp-openai-compat). These are output data, not duplicates of those components. Vectors affect software candidate selection; their readable text is separately hydrated. Actual installed weights, all backend persistence details and equivalence after repair remain unverified. SRC-1: `mempalace/searcher/candidates.py`, `mempalace/media.py`, `mempalace/backends/rust_exact.py`, `mempalace/backends/qdrant.py`.

> documents=[asset.descriptor()],
> metadatas=[metadata],
> embeddings=[vector],
> --- `mempalace/media.py`

#### MEM-OBJ-closet-lines
Label: Closet pointer lines

Source-native identity: closet document lines, conventionally `topic|entities|date-and-lines|→drawer_ids`, with a legacy three-segment form. Representational form: topic/quote/summary words are natural-language locators; drawer references and date/line segments are symbolic access parts. Storage substrate: separate closets collection plus derived embeddings. Regex generation scans the first 5,000 characters, selects limited topics/entities/quotes, and references at most three drawer IDs; LLM regeneration is a separate lineage. This is not a complete source summary or exact quotation guarantee. Search uses closets to enrich/boost candidates and then reads drawer material. Supplied overlap: [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall) establishes the consumer, not this object's identity. SRC-1: `mempalace/palace/closets.py`, `mempalace/closet_llm.py`.

> drawer_ref = ",".join(drawer_ids[:3])
> window = content[:CLOSET_EXTRACT_WINDOW]
> --- `mempalace/palace/closets.py`

#### MEM-OBJ-diary-entry
Label: Diary entry

Source-native identity: diary-room document with agent/topic/date metadata; daily-file ingestion also creates entry/chunk drawers in room `daily`. Representational form: readable natural-language or compact checkpoint text; symbolic agent, topic, timestamp and parent keys provide access. Storage substrate: drawer collection, with original daily files and ingestion-state JSON for file import. This specializes [MEM-OBJ-drawer-text](#mem-obj-drawer-text), not a second independent backend. Distinct from [RT-OBJ-task-request](runtime.md#rt-obj-task-request): continuity account rather than addressed task contract. Lineage varies: foreground agent/human-supplied journal, caller-authored file summary or code-generated user-message prefixes. Initial summary accuracy and reason preservation depend on that lineage. Recent diary tools and ordinary search can return it to later agents. SRC-1: `mempalace/mcp_server/tools_diary.py`, `mempalace/diary_ingest.py`, `mempalace/hooks_cli.py`.

> "hall": "hall_diary",
> "topic": topic,
> "type": "diary_entry",
> "agent": agent_name,
> --- `mempalace/mcp_server/tools_diary.py`

#### MEM-OBJ-identity-text
Label: Identity text

Source-native identity: `identity.txt`, defaulting to `~/.mempalace/identity.txt`. Representational form: natural-language self/person/project guidance. Storage substrate: editable filesystem text plus Layer0 instance cache. Doctrine calls it user-written; source establishes a file read, not who actually authored a particular installation's file. No per-edit approval mechanism is established. The startup consumer can give identity text system-prompt placement, but compliance and legitimacy are not guaranteed. This is a retained input to [RT-BAP-agent-context](runtime.md#rt-bap-agent-context), not a duplicate path. SRC-1: `mempalace/layers.py`; supplied Hermes consumer evidence in runtime.

> with open(self.path, "r") as f:
>     self._text = f.read().strip()
> --- `mempalace/layers.py`

#### MEM-OBJ-kg-triples
Label: Temporal KG triples

Source-native identity: entities and triples in `knowledge_graph.sqlite3`, including subject/predicate/object, validity interval, confidence and optional source closet/file/drawer/adapter provenance. Representational form: symbolic graph structure and temporal controls; entity labels and relation contents remain claims requiring interpretation. Storage substrate: SQLite tables. Writers include explicit tools and the exposed adapter graph surface; a universal automatic fact miner is not established. Consumers are KG tools, timeline and fact-checking/maintenance surfaces, not necessarily the vector searcher. Optional provenance pointers are not retained explanatory reasons or automatic source verification. No supplied runtime object has this referent; [RT-RTE-init-detection](runtime.md#rt-rte-init-detection) concerns origin/entity setup, not these temporal assertion rows. SRC-1: `mempalace/knowledge_graph.py`, `mempalace/mcp_server/tools_kg.py`, `mempalace/fact_checker.py`.

> confidence REAL DEFAULT 1.0,
> source_closet TEXT,
> source_file TEXT,
> source_drawer_id TEXT,
> adapter_name TEXT,
> --- `mempalace/knowledge_graph.py`

#### MEM-OBJ-tunnels
Label: Tunnels and traversal fields

Source-native identity: explicit tunnel dictionaries persisted by `_save_tunnels`, with source/target wing/room and optional drawer IDs, label, strength, stability, last activation and access count. Representational form: symbolic graph links and numerical access statistics, not distributed model weights. Storage substrate: palace-scoped tunnel sidecar loaded/saved by graph code. Lineage includes explicit creation and topic/entity-derived links; traversal updates are trace-fed. Later follow/list and audit consumers expose connectivity/history. Source searches did not establish these fields influencing default semantic ranking. Distinct from [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall): explicit graph navigation, not vector candidate selection. Hallways are a separate entity-co-occurrence sidecar feeding linking/audit; their full lifecycle is not claimed by this tunnel record. SRC-1: `mempalace/palace_graph.py`, `mempalace/hallways.py`, `mempalace/dynamics.py`.

> connection["last_activated"] = now.isoformat()
> connection["access_count"] = int(connection.get("access_count", 0)) + 1
> --- `mempalace/dynamics.py`

#### MEM-OBJ-media-asset
Label: Media asset reference

Source-native identity: `MediaAsset` and fixed assets collection row. Representational form: symbolic path/type/dimension/provenance metadata, natural-language descriptor title, and separately derived dense vector in [MEM-OBJ-drawer-vectors](#mem-obj-drawer-vectors). Storage substrate: index row; original opaque image/audio/video bytes stay in the external local file. A title/descriptor is not a caption, transcript or readable surrogate for all those bytes. Missing files can leave searchable references. The result consumer receives descriptor, path, availability and optional related drawer, not automatically the media payload. Distinct from the supplied embedding component [RT-CMP-embeddinggemma2](runtime.md#rt-cmp-embeddinggemma2). SRC-1: `mempalace/media.py`, `mempalace/searcher/media_search.py`.

> def descriptor(self) -> str:
>     """Return searchable descriptor text without captioning or copying bytes."""
>     return f"{self.media_type.title()} asset: {self.title}"
> --- `mempalace/media.py`

#### MEM-OBJ-write-log
Label: Write audit log

Source-native identity: `wal/write_log.jsonl` intent and outcome records. Representational form: symbolic operation/parameter/result envelopes with redacted content fields; not a full transcript or full restorable content history. Storage substrate: append-only local JSONL. Code writes before selected backend mutations and appends outcomes at participating call sites; log failure is nonfatal. Operational diagnostics/replay tooling is an afforded consumer, not an established automatic model-memory read-back route. No supplied object counterpart after comparison with [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact): this is audit metadata, not an exact stored patch. SRC-1: `mempalace/wal.py`.

> if k in _WAL_REDACT_KEYS:
>     safe_params[k] = f"[REDACTED {len(v)} chars]" if isinstance(v, str) else "[REDACTED]"
> --- `mempalace/wal.py`

### Routes

#### MEM-RTE-source-filing
Label: Source filing alternatives

Endpoints/progression: CLI or hook import → source read/normalization or selective extraction → chunks and metadata → backend drawers, with project closets where configured → subsequent recall. Owner: importer code, with caller-selected source/mode/configuration. Project mining, conversation exchange/general extraction and message sweep use different ID/freshness mechanisms. This expands alternatives beside [RT-RTE-hook-ingest](runtime.md#rt-rte-hook-ingest), not a replacement for its submission route; Hermes callback admission stays [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture). SRC-1: `mempalace/miner.py`, `mempalace/convo_miner.py`, `mempalace/general_extractor.py`, `mempalace/normalize.py`, `mempalace/sweeper.py`, `mempalace/cli/cmd_mine.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: counts/skips/errors from import; hook submission alone is not that result.
- Later read-back: drawers are selected by search, direct GET and startup layers; project closets supply search locators.
- Delegated visibility: daemon/subprocess may receive source path and mode; no model-context isolation is established by this import.
- Selection predicate: caller source/mode plus path/readability/length/chunk limits, freshness and extraction rules; general mode rejects unmarked or low-scoring segments.
- Invalidation or expiry: project and conversation re-mines purge prior scoped source chunks before reinsertion; sweep skips timestamps strictly before its session cursor and idempotently upserts deterministic IDs at/after it.
- Activation or effect: stored text and access structures change; later answer dependence is unobserved.
- Evidence limits: individual format parsers, full format miner and backend atomicity are not audited; sweep and file mining can overlap under incompatible IDs.

Admission: caller chooses a corpus, not each retained claim; software chooses accepted files/segments. Original text may mix user, assistant and tool output. General extraction uses marker scores and a confidence threshold, not an answer oracle. Normalization can spell-correct user messages, so “stored verbatim” cannot mean identical to all raw input. Project upsert errors trigger partial-source cleanup; failed initial purge aborts the file and permits later retry. These are storage recovery rules, not belief criticism or retention of rejected claim rationales.

> if _fix is not None:
>     text = _fix(text)
> lines.append(f"> {text}")
> --- `mempalace/normalize.py`

> if not scores:
>     continue
> --- `mempalace/general_extractor.py`

> if confidence < min_confidence:
>     continue
> --- `mempalace/general_extractor.py`

> The sweeper deduplicates against its own prior writes via
> deterministic drawer IDs + a timestamp cursor. It does NOT currently
> coordinate with the file-level miners (miner.py / convo_miner.py) —
> those produce char-chunked drawers without compatible message
> metadata, so running both miners may store overlapping content under
> different IDs.
> --- `mempalace/cli/cmd_mine.py`

#### MEM-RTE-closet-regeneration
Label: Closet regeneration

Endpoints/progression: operator invokes regeneration → group retained drawers by source → configured LLM proposes topics/quotes/summary → parsed lines replace source closets → later search enrichment. Owner: code for acquisition/write; model for proposed words. Distinct from ordinary [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall), which consumes these locators, and [RT-RTE-init-detection](runtime.md#rt-rte-init-detection), which classifies setup entities. SRC-1: `mempalace/closet_llm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: processed/failed and token-usage counts; dry-run lists sources without generation or writes.
- Later read-back: generated closet vectors/text participate in the search route that hydrates retained drawer text.
- Delegated visibility: configured provider receives source name prefix, wing/room and up to 30,000 content characters; provider retention is uninspected.
- Selection predicate: optional wing and source sample, source-grouped drawers; model output up to 1,500 tokens; conversion keeps up to 15 topics, five quotes and 200 summary characters, referencing up to three drawer IDs.
- Invalidation or expiry: source-scoped lock protects purge plus upsert; normalize version stamps prevent immediate stale-index regeneration by ordinary mining. No time expiry is established here.
- Activation or effect: locators are rewritten, not source drawer content or model weights; changed retrieval or answer quality is unobserved.
- Evidence limits: JSON parsing does not verify quote fidelity, factual accuracy, model identity or retrieval benefit; source content beyond the input cap is omitted.

Admission: operator starts the job and configures a provider; the model authors candidate lines and code admits parsed output without per-source human confirmation. Failure to obtain parsed output skips that source with retries for selected provider failures. Guidance requests distinctive topics, exact quotes, WHO/WHAT/WHY summary and JSON. Persisted material includes generated lines, source metadata and generator label, not a required rationale/criticism history. The search reader uses the locators rather than proving their reasons. This trace-fed derived index can shape future selection; no capacity-improvement inference follows.

> if not parsed:
>     failed += 1
>     print(f"  [{i}/{len(sources)}] [FAIL] {os.path.basename(source)} - LLM failed")
>     continue
> --- `mempalace/closet_llm.py`

> "generated_by": f"llm:{cfg.model}",
> --- `mempalace/closet_llm.py`

#### MEM-RTE-diary-checkpoint
Label: Diary checkpoint alternatives

Endpoints/progression: Stop/end lifecycle or caller save → deterministic transcript prefixes, caller-authored entry or daily-file entries → diary drawers → requested diary continuity read or search. Owner: code in silent checkpoint; foreground caller in explicit diary/checkpoint content. Distinct from transcript mining in [RT-RTE-hook-ingest](runtime.md#rt-rte-hook-ingest), though the same Stop event can trigger both. SRC-1: `mempalace/hooks_cli.py`, `mempalace/mcp_server/tools_diary.py`, `mempalace/diary_ingest.py`, `integrations/shared/recall-protocol.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: diary entry ID/chunk count or failure; hook acknowledgement counts drawers separately from folded messages.
- Later read-back: diary tool filters agent plus diary room, optionally wing, and returns newest rows; recall doctrine assigns later agent-continuity questions to this route. Ordinary text search is another reader.
- Delegated visibility: daemon diary job receives entry/agent/topic/wing; a legacy non-silent Stop hook asks the host agent to author a save instead of constructing identical content.
- Selection predicate: save interval/settings and normalized harness agent identity; deterministic hook extraction selects recent eligible user messages, skips harness-prefixed messages, initially caps each at 200 characters and retains at most ten 80-character prefixes in the checkpoint entry. Diary last_n clamps to 1–100 physical rows, not complete logical sessions.
- Invalidation or expiry: silent Stop advances its save marker only after a filed drawer; legacy prompting advances before confirmation. Daily-file hash changes/force rebuild source drawers and closets; explicit entries accumulate until separate maintenance.
- Activation or effect: compact continuity text persists for later retrieval; no evidence that a later host read it or resumed correctly.
- Evidence limits: deterministic checkpoints omit assistant reasoning/results and most user text; arbitrary caller summaries have unresolved fidelity. A diary page can contain chunks rather than whole entries.

Admission differs by branch. Silent mode automatically writes selected trace fragments, without per-content human veto. Non-silent mode asks an agent to write a session summary; that request is not proof of a completed summary. Direct diary tools sanitize caller content and agent names; generic caller identity does not establish human authorship. Batch checkpoint calls semantic dedup per item and file on dedup errors; it can return mixed successes/duplicates/errors rather than one atomic save. Daily-file import reads preexisting summaries whose original author/control is uninspected; hash-based subsequent rebuild is known. No branch's “summary” label establishes retained explanations. Hook snippets can preserve reasons only incidentally within their prefixes; later readers do not receive discarded turns through the checkpoint itself.

> topics = "|".join(m[:80] for m in messages[-10:])
> entry = (
>     f"CHECKPOINT:{now.strftime('%Y-%m-%d')}|session:{session_id}"
>     f"|msgs:{len(messages)}|recent:{topics}"
> )
> --- `mempalace/hooks_cli.py`

> # Marker advances before confirmed save — best-effort; if Claude
> # fails to save, the checkpoint is lost but won't retry endlessly.
> --- `mempalace/hooks_cli.py`

> dup = tool_check_duplicate(content, threshold=dedup_threshold)
> if dup.get("is_duplicate"):
>     out["duplicates"].append({"room": room, "matches": dup.get("matches", [])})
>     continue
> --- `mempalace/mcp_server/tools_diary.py`

#### MEM-RTE-wake-context
Label: Wake context selection

Part of: [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall)

Endpoints/progression: startup wake request → Layer0 file plus Layer1 selected drawer snippets → CLI text/host cache → later prompt context. Parent route covers search and startup; this part isolates the startup selector, which has different inputs and budget. Owner: deterministic layer code; host owns assembly/consumption. SRC-1: `mempalace/layers.py`, `mempalace/cli/cmd_query.py`; supplied DSH/Hermes consumers in [RT-BAP-agent-context](runtime.md#rt-bap-agent-context).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: identity plus rendered L1 string, not a newly stored generative summary.
- Later read-back: previously retained identity and drawer text reaches startup consumers; session caching makes the rendered selection available across later prompt assemblies.
- Delegated visibility: DSH scopes prompt registrations to its agent; child context/compaction remain host-owned. Hermes delegation returns task/result capture, not an entire isolated window.
- Selection predicate: optional wing; normal backend get_recent takes up to 2,000 recent filings; importance/emotional_weight/weight then filed_at descending; top 15 drawers, each snippet capped at 200 characters, approximately 3,200-character L1 body budget. Layer0 reads the full file without an enforced 100-token cap.
- Invalidation or expiry: Layer0 caches after first render; L1 regenerates when called; host-specific cache refresh/disposal follows the supplied runtime. Fallback paged scan is a bounded backend window and need not contain the globally newest drawers.
- Activation or effect: selected snippets and identity are supplied as context; no observed first-call insertion, compliance or benefit.
- Evidence limits: token figures are estimates; headings/room markers are not all accounted for by the content counter, and identity is not globally bounded. No universal 600–900-token startup guarantee.

Selection is software admission to context, not approval of new content. There is no answer oracle. L1's “essential story” is extractive truncation/grouping, not model synthesis. Default ingest metadata generally lacks evaluative importance, making filing recency the practical order in ordinary data. A high weight only matters within the fetched window. These limits challenge an unlimited “highest importance in the whole palace” reading.

> MAX_DRAWERS = 15  # at most 15 moments in wake-up
> MAX_CHARS = 3200  # hard cap on total L1 text (~800 tokens)
> MAX_SCAN = 2000  # size of the candidate window pulled for L1 generation
> --- `mempalace/layers.py`

> if len(snippet) > 200:
>     snippet = snippet[:197] + "..."
> --- `mempalace/layers.py`

#### MEM-RTE-temporal-facts
Label: Temporal fact revision

Endpoints/progression: client proposes assertion/end/successor → sanitized KG tool → SQLite temporal rows → later entity/as_of/timeline response. Owner: caller chooses meaning; graph code maintains intervals. Different retained store and withdrawal semantics from [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch)'s drawer writes. SRC-1: `mempalace/mcp_server/tools_kg.py`, `mempalace/knowledge_graph.py`, `integrations/shared/recall-protocol.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: fact/triple ID, resolved ended boundary or error.
- Later read-back: entity query returns assertions and separates active/historical/future when as_of is absent; explicit as_of filters intervals. Doctrine directs agents to active facts for current questions and source text for reasons/verification.
- Delegated visibility: inapplicable — these handlers do not launch a worker or define a child window.
- Selection predicate: entity/direction/as_of; writes validate names and temporal syntax, not truth. Supersede closes open old rows at the requested boundary and inserts a successor starting there only when no matching open successor exists. An existing open successor is reused without checking or changing its valid_from. Invalidate ends without replacement.
- Invalidation or expiry: validity boundaries alter current-time eligibility while historical rows remain available; supersession is not physical erasure.
- Activation or effect: temporal access changes; the agent must interpret the returned buckets appropriately. No observed changed answer.
- Evidence limits: successful supersede does not guarantee a successor queryable at the requested boundary: a reused successor can start later. Optional provenance is not an automatic source-read or warrant; unrestricted facts payload includes historical and future claims. Global consistency and every KG producer are not established.

Admission is explicit caller proposal plus structural code validation, without built-in human confirmation or answer oracle. The recall skill guides which operation to choose; it does not prove the chosen successor is true. Supersede performs old-row closure and successor insertion or reuse within one SQLite transaction; it is not autonomous content criticism. The shared-boundary read-back guarantee applies to a newly inserted successor, not unconditionally to a reused row. If the old value is active at the requested instant and an already-open successor starts after it, closure succeeds and the existing successor ID is returned, but an as_of query at that instant excludes both: the old row has ended and the successor has not started. This is an implementation counterexample, not an observed run. Recovery rejects malformed/inverted boundaries; caller can submit further temporal changes, but arbitrary prior-state restoration is not established here. Historical assertions preserve past contents, not necessarily reasons for rejection.

> Closes ``(subject, predicate, old_object)`` and opens
> ``(subject, predicate, new_object)`` at one shared instant, so a
> point-in-time query at the boundary returns only the new value.
> --- `mempalace/mcp_server/tools_kg.py`

That handler passage declares intent; the implementation's reuse branch qualifies it:

> existing = conn.execute(
>     "SELECT id FROM triples "
>     "WHERE subject=? AND predicate=? AND object=? AND valid_to IS NULL",
>     (sub_id, pred, new_id),
> ).fetchone()
> if existing:
>     return existing["id"]
> --- `mempalace/knowledge_graph.py`

The later consumer checks both bounds, rather than treating the returned successor ID as proof of current validity:

> return (
>     f" AND (t.valid_from IS NULL OR {valid_from_expr} <= ?) "
>     f"AND (t.valid_to IS NULL OR {valid_to_expr} > ?)",
>     [as_of_key, as_of_key],
> )
> --- `mempalace/knowledge_graph.py`

#### MEM-RTE-tunnel-traversal
Label: Tunnel traversal recording

Endpoints/progression: caller follows room tunnels → endpoint-matched connections and optional drawer previews → access-history potentiation persisted → later list/follow/audit reads. Owner: code, with caller able to suppress recording. Distinct from ordinary semantic [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall). SRC-1: `mempalace/palace_graph.py`, `mempalace/dynamics.py`, `mempalace/palace_audit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: connected wing/room/label/IDs, with at most 300 characters of preview per referenced drawer when hydration succeeds.
- Later read-back: saved tunnel links remain navigable; counters/history appear to audit consumers, which describe never-traversed share as informational rather than scored.
- Delegated visibility: inapplicable — graph navigation alone launches no agent.
- Selection predicate: endpoint wing/room match, optional collection and record flag; selected traversed IDs are potentiated, increasing capped strength/access count and sometimes stability after a spaced interval.
- Invalidation or expiry: explicit link deletion is separate; effective_strength can compute time decay without modifying stored state. Full maintenance scheduling/consumer use of decay is not established.
- Activation or effect: trace-fed numeric metadata changes durably on successful save; no demonstrated downstream ranking change, learned model weights or improved navigation capacity.
- Evidence limits: recording is best effort and failure does not prevent returning connections. Access is not evidence of usefulness or correctness.

Admission: software records traversal traces, not per-event human-approved content. Initial links have explicit and derived creation paths with different controls; this route does not establish all of them. It retains access summaries, not a reason why a link was useful. There is no expected-answer oracle or criticism loop. An installed pure decay function must not be mistaken for scheduled automatic forgetting or content withdrawal.

> if record and connections:
>     record_tunnel_traversal([c["tunnel_id"] for c in connections], config)
> --- `mempalace/palace_graph.py`

> "followed (not scored; mempalace_follow_tunnels records each crossing).",
> --- `mempalace/palace_audit.py`

#### MEM-RTE-media-index
Label: Media indexing and retrieval

Endpoints/progression: explicit media adapter → file reference/validated native media embedding → assets collection → opt-in shared-space search → descriptor/path/availability result. Owner: code and caller configuration. Distinct alternate within [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall), whose supplied report leaves media untraced. SRC-1: `mempalace/cli/cmd_mine.py`, `mempalace/media.py`, `mempalace/searcher/media_search.py`, `mempalace/cli/cmd_query.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: asset write count or setup/per-asset failure; query returns ranked result envelope or refusal.
- Later read-back: query embeds search/code request and retrieves previously indexed compatible text and optional assets; result supplies references rather than original media bytes.
- Delegated visibility: embedding model receives media; a downstream agent must separately open/use the returned path. No automatic host media attachment is established.
- Selection predicate: explicit media opt-in, EmbeddingGemma2 and cosine collections, symbolic filters and finite distances; n_results 1–100, per-collection candidate pool capped at 500 or 5,000 with date filtering; global sort by distance then ID.
- Invalidation or expiry: re-ingest upserts asset ID and preserves original filed_at; current file existence supplies available flag. Missing files remain searchable references rather than automatically erased rows.
- Activation or effect: content-derived vectors influence selection and descriptors reach caller; actual multimodal model consumption and benefit unobserved.
- Evidence limits: file bytes can change independently of index; source identity/dimension checks do not prove semantic equivalence or file immutability. Backend/provider execution not observed.

Admission: caller starts source import; code checks file presence, provider/modality/vector shape and optional related drawer, then writes without per-asset human confirmation. Bad asset/model setup can reject; individual failures can be skipped, with all-failed import raised. No truth/answer oracle. Descriptor text does not acquire the informational contents of the opaque file merely by being stored beside its vector.

> available=Path(path).is_file(),
> --- `mempalace/searcher/media_search.py`

#### MEM-RTE-memory-maintenance
Label: Memory maintenance and withdrawal

Endpoints/progression: explicit update/delete/source-delete/sync or audit-guided operation → selected logical/physical/source rows → text/metadata/index change or report → later searches/GET/context generation reflect surviving state. Owner: caller for explicit edits; software for source cleanup verdicts. This adds lifecycle detail to [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch), not a second dispatch record. SRC-1: `mempalace/mcp_server/tools_write.py`, `mempalace/sync.py`, `mempalace/cli/cmd_audit.py`, `mempalace/cli/cmd_query.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: changed/deleted chunk/closet counts, dry-run source plan, sync buckets or audit findings/score.
- Later read-back: changed documents are fetched later; source closets are purged after content edits/deletes rather than continuing to quote removed text. Existing host caches are not proven synchronously retracted.
- Delegated visibility: inapplicable — these handlers do not themselves launch isolated model work; audit instructions may guide an external agent.
- Selection predicate: logical handle resolves chunk group, physical ID resolves one row; source-delete and sync scope sources, while sync requires explicit project_dirs or wing on apply and only removes established missing/gitignored cases.
- Invalidation or expiry: drawer content edits purge source closets; stale chunks after rechunking are removed; overview caches invalidated. Metadata-only wing/room edits leave source closets. Sync retains unresolved cases and registry sentinels.
- Activation or effect: data/search eligibility changes; no proof of global erasure, cross-replica withdrawal or forgetting in an already assembled host prompt.
- Evidence limits: operations across drawers/closets are not established as one global transaction; backups/WAL/host caches/KG references/other replicas may retain related information. Full restore and cascading KG/link cleanup are uninspected.

Admission: explicit caller changes need structural validation, not semantic approval. Source deletion defaults dry-run; sync applies only on requested scope. Shipped audit doctrine asks for user decisions before restructuring, whereas the write handlers themselves do not implement that dialogue. Audit CLI emits a report and optional threshold exit code, not automatic content acceptance. Repair scans/prunes/rebuilds and migration/archive dispatch are separate reliability surfaces with incomplete inspection here; they cannot establish semantic correction. WAL redacts content, so it does not establish lossless undo. Recovery from mistaken content deletion may require retained sources or backups, whose completeness is not verified.

> if content is not None and source_file:
>     closets_deleted = _purge_source_closets(source_file, commit=True)
> --- `mempalace/mcp_server/tools_write.py`

> if not dry_run and not wing and not project_dirs:
>     raise ValueError(
>         "sync apply requires explicit wing= or project_dirs= so it cannot "
>         "auto-prune every wing in a multi-project palace; pass --wing or "
>         "a project directory"
>     )
> --- `mempalace/sync.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture)

Memory-specific lineage: the retained exchange mixes host-supplied user and assistant content, normalized to labelled text, not a user-only fact set. Metadata classification and IDs control filing; no per-content approval or truth gate follows from opening the adapter. Raw-ish exchange retention can support future information access but is not itself a derived lesson or an improved policy. Queue drops and non-durable worker state bound completeness. The supplied record supplies the minimum passage; SRC-1: `mempalace/integrations/hermes/__init__.py`, `mempalace/convo_miner.py`.

#### On [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall)

Read-back comprises request, selection and delivery, not one “push” classification. MCP/CLI search is requested; Hermes prefetch is host-requested anticipatory supply; DSH startup selection is independently triggered and cached. Search's closet-assisted hydration selects lexical best chunk plus neighbors and caps expanded content at 10,000 characters. Direct logical GET is a distinct full-content escape route. L2 filtered API retrieves up to n_results records and renders up to 300 characters each; its docstring's token estimate is not a token-enforced budget or evidence of deployed invocation. Natural-language content reaches a host context/tool result; metadata and vectors have software selection authority. SRC-1: `mempalace/searcher/candidates.py`, `mempalace/layers.py`, `mempalace/mcp_server/tools_write.py`; supplied consumer passages remain in runtime.

> _CLOSET_RESULT_POOL_MULTIPLIER = 4
> _MAX_HYDRATION_CHARS = 10000
> --- `mempalace/searcher/candidates.py`

#### On [RT-BAP-agent-context](runtime.md#rt-bap-agent-context)

Identity, drawer text and imperative recall guidance have different trust origins even when delivered together. Startup system-prompt placement does not validate imported user/assistant text or prevent instructions embedded in source content from being interpreted as guidance. No source-execution evidence shows the model obeying an embedded instruction. The inspected layers select/truncate but do not establish a general trust-sanitization boundary. The doctrine requires quoting exact stored words, source lookup for explanation and query-dependent selection rather than retrieval every turn. SRC-1: `integrations/shared/recall-protocol.md`, `mempalace/layers.py`; host channel evidence supplied by runtime.

> Response sizes depend on
> the number of facts and the length of stored text; a small result limit
> does not impose a fixed token budget.
> --- `integrations/shared/recall-protocol.md`

#### On [RT-RTE-init-detection](runtime.md#rt-rte-init-detection)

The origin/entity files and known-entity registry are symbolic classifications plus readable names, not automatically verified facts. People/project human edits and automatically passed topics remain separate admission mechanisms. Subsequent consumers are known: miner entity metadata/hall routing and topic/entity link construction. This retains known transformations without resolving original detection accuracy. Topic tunnels use synthetic topic rooms and can point to a semantic category rather than a material source drawer. SRC-1: `mempalace/miner.py`, `mempalace/palace_graph.py`; setup evidence supplied by runtime.

#### On [RT-OBJ-task-request](runtime.md#rt-obj-task-request)

This is natural-language work guidance inside symbolic event routing, retained across invocations in logstream SQLite. Addressed/correlated task retrieval is not semantic palace recall; supplied launcher doctrine asks the worker to reload the task. Exact contents have procedural authority only if the recipient reads/follows them. Direct anti-entropy inspection shows referenced artifacts fetched before applying remote events, not installation of patch contents. SRC-1: `mempalace/logsync.py`; task and consumer evidence supplied in runtime.

> for artifact_id in event.get("artifact_ids") or []:
>     if ls.has_artifact(artifact_id):
>         continue
> --- `mempalace/logsync.py`

#### On [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact)

Stored patch bytes differ from their event/display summaries. The patch is recoverable exact proposal content for a later artifact reader; a readiness event or preview is neither its full payload nor accepted executable product. Supplied runtime passages establish persistence/delivery, not downstream application, rejection or rollback. SRC-1: `mempalace/logstream.py`, `mempalace/mcp_server/tools_coord.py`.

## Write side

The table and records separate content authority from filesystem writes:

| Mechanism | Who supplies/derives content and who admits it | Retained result and later consumer |
|---|---|---|
| Import/sweep | Caller selects corpus/mode; software selects/normalizes/chunks; no itemwise human approval inferred | Drawers/metadata/optional closets → search, GET, L1; [MEM-RTE-source-filing](#mem-rte-source-filing). |
| Hermes/hook transcript capture | Host supplies trace; code classifies/queues/mines, with readiness/queue/routing rejection | Exchange or normalized transcript drawers → later recall; supplied [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture), [RT-RTE-hook-ingest](runtime.md#rt-rte-hook-ingest). |
| Explicit add/update/diary | Caller authors, identity may be model/human/other code; handler validates shape rather than truth | Text or journal → direct and selected reads; [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch), [MEM-RTE-diary-checkpoint](#mem-rte-diary-checkpoint). |
| Silent checkpoint / prompted checkpoint / daily-file import | Code derives prefixes; alternatively host agent is requested to summarize; imported summaries have unresolved initial control | Distinct derived continuity entries → diary/search; same checkpoint record. Source reasons are not systematically retained in snippets. |
| Regex / LLM closets | Software heuristic or model proposes words; parse/packing rules admit automatically after invocation | Derived index text/pointers/vectors → search selection and drawer hydration; [MEM-RTE-closet-regeneration](#mem-rte-closet-regeneration). |
| KG assertion/end/successor | Caller proposes; code enforces naming/interval structure; host recall policy recommends temporal maintenance | Historical and current assertion rows → KG response; [MEM-RTE-temporal-facts](#mem-rte-temporal-facts). |
| Setup entities / graph derivation | Supplied setup distinguishes human-reviewed entities from automatic topics; software derives links and records accesses | Registry → mining/links; tunnel history → navigation/audit; [RT-RTE-init-detection](runtime.md#rt-rte-init-detection), [MEM-RTE-tunnel-traversal](#mem-rte-tunnel-traversal). |
| Media | Caller selects source; software validates embedding space and file/vector structure | Reference/vector/descriptor → opt-in search; [MEM-RTE-media-index](#mem-rte-media-index). |
| Maintenance | Explicit edit/delete/apply admits change; sync software retains uncertain removals; audit doctrine reserves restructuring decisions for user | Surviving rows/indexes → later reads, not retroactive host-window withdrawal; [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance). |

These are open operations, not an expected-answer-scored improvement curriculum. Semantic dedup can reject near-duplicate saves; extraction can reject weak marker matches; neither is truth adjudication. Automatic trace-fed transformations are specifically retained: transcript → checkpoint prefixes → continuity consumer; retained drawers → generated closets → later search; navigation event → access fields → later audit/navigation display. Their reasons are incidental or absent as a required field, so a durable artifact does not establish an explanatory lesson. No capacity-improvement, reflective theory-builder or self-improvement conclusion is inferred from these chains.

Evaluation has another admission boundary: the raw LongMemEval function builds fresh benchmark collections from user turns/sessions and queries the question. Its expected session IDs score retrieval, not factual acceptance into a live user's palace. The code even appends non-returned corpus indices after actual returned rankings, which must be considered when interpreting metrics/cutoffs. The run did not inspect every evaluator mode or execute it. Results are not an automatic curation/adoption path in the inspected live writers. SRC-1: `benchmarks/longmemeval_bench.py`.

> # One document per session: join all user content
> user_turns = [t["content"] for t in session if t["role"] == "user"]
> --- `benchmarks/longmemeval_bench.py`

> # Fill in any missing indices (ChromaDB may return fewer than corpus size)
> seen = set(ranked_indices)
> for i in range(len(corpus)):
>     if i not in seen:
>         ranked_indices.append(i)
> --- `benchmarks/longmemeval_bench.py`

## Read-back

The actual later-consumer chains are distinct:

- **Query → ranked retained text → MCP/CLI/host result.** Search filters and ranks stored drawers, possibly using derived closets and lexical hydration. The agent can then request a complete logical drawer rather than treating a passage as the entire source. Supplied [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall) and its annotation establish this route and limitations.
- **Startup → recent/weighted snippets plus identity → host prompt channel.** [MEM-RTE-wake-context](#mem-rte-wake-context) supplies selector/budget details. It is not query-targeted retrieval, a learned summary or a total-token guarantee. DSH's once-only assembly wait and agent-local disposal come from the supplied runtime, not a MemPalace host-compaction implementation.
- **Continuity request → recent agent rows → model/human journal context.** [MEM-RTE-diary-checkpoint](#mem-rte-diary-checkpoint) establishes documented later agent use, not merely a storage API. Small last_n may split entries, and topical/older information calls for search.
- **Entity/time request → temporal buckets → agent interpretation.** [MEM-RTE-temporal-facts](#mem-rte-temporal-facts) retains invalidated rows for history; “present in facts” and “currently active” differ. Structured validity is not independent verification.
- **Room navigation → linked endpoints/previews; media query → file references.** [MEM-RTE-tunnel-traversal](#mem-rte-tunnel-traversal) and [MEM-RTE-media-index](#mem-rte-media-index) prevent treating previews/descriptors as full payloads or proven agent consumption.
- **Task handoff → addressed event/artifact read → external worker.** [RT-RTE-task-launch](runtime.md#rt-rte-task-launch), [RT-RTE-patch-delivery](runtime.md#rt-rte-patch-delivery) and the object annotations separate routing metadata, exact payload and display text. Retention and delivery do not install the result.

Working-context control is partly selective inclusion, not only accumulation. L1 and L2 truncate; search controls candidate/result/passage size; host adapters cache and supply selected material. Precompact capture tries to preserve content outside the window before the host removes it. The inspected Python precompact hook schedules transcript ingestion and separately mines project data synchronously; this is not synchronous proof that the transcript was saved. Hermes pre-compress is a no-op per runtime. No inspected MemPalace mechanism specifies the host's retained tail/summary after compaction. DSH agent-local registrations resemble a scoped frame only in their lifecycle: disposal removes registrations, not copies already interpreted elsewhere. Retained drawers are values reloaded through explicit searches/IDs, not live pointers in a model window. SRC-1: `mempalace/hooks_cli.py`, `mempalace/layers.py`; supplied host evidence in [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall).

> # Capture tool output via our normalize path before compaction loses it
> if transcript_path:
>     _ingest_transcript(transcript_path)
> --- `mempalace/hooks_cli.py`

## Integration issues

- **Corrections to supplied facts:** none required. The supplied runtime already limits capture, retrieval, compaction, read-only and patch-installation claims. This member adds unsupported-strength counterexamples without replacing its records.
- **Containment/overlap:** [MEM-RTE-wake-context](#mem-rte-wake-context) is explicitly part of [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall). [MEM-RTE-source-filing](#mem-rte-source-filing) overlaps downstream mining in [RT-RTE-hook-ingest](runtime.md#rt-rte-hook-ingest), but includes independent project/general/sweep entries, so is not wholly a part of it. [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance) crosses CLI sync and MCP handlers, not a duplicate dispatcher. [MEM-RTE-media-index](#mem-rte-media-index) adds a distinct media write/read chain rather than replacing general recall. Diary checkpoint and transcript ingest can share a trigger but retain different content. No other new record is proposed as a replacement for a supplied referent.
- **Source-internal stale documentation:** `mempalace/sources/context.py` says no in-tree caller constructs `PalaceContext`, but `mempalace/cli/cmd_mine.py` does so on the explicit adapter path. [MEM-RTE-source-filing](#mem-rte-source-filing) and [MEM-RTE-media-index](#mem-rte-media-index) use executable dispatch, not that negative prose. This prevents declaring adapter use merely hypothetical.
- **Fidelity and authority:** [MEM-RTE-source-filing](#mem-rte-source-filing), [MEM-RTE-diary-checkpoint](#mem-rte-diary-checkpoint) and [MEM-RTE-wake-context](#mem-rte-wake-context) qualify [RT-CLM-recall-protocol](runtime.md#rt-clm-recall-protocol). Exact quoting of stored text does not recover omitted/spell-corrected input. Actual source truth, trust and answer benefit remain unresolved.
- **Temporal supersession guarantee:** [MEM-RTE-temporal-facts](#mem-rte-temporal-facts) corrects this member's unconditional shared-instant assertion. SRC-1 `mempalace/knowledge_graph.py` reuses an open successor without aligning its start, so successful supersession can leave no eligible row at the replacement instant. Transactional closure/insertion-or-reuse and historical withdrawal remain supported; immediate successor visibility requires its actual interval to include the query instant. This correction concerns this member, not a supplied runtime record.
- **Graph update horizon:** [MEM-RTE-tunnel-traversal](#mem-rte-tunnel-traversal) establishes trace-fed persisted counters and audit consumption, not stronger ranking or learning claims. Full hallway/tunnel proposal/pruning and decay-use callers remain incompletely traced; these prevent a whole-graph adaptation characterization.
- **Retention/withdrawal horizon:** [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance) does not prove deletion from backups, host caches, KG references or remote/native stores. Replicated event/artifact import is known from `mempalace/logsync.py`; complete replicated withdrawal, snapshot replacement and recovery remain uninspected. No system-wide forgetting guarantee follows.
- **Alternative surfaces:** backend variants, individual export/document parsers, legacy host wrappers, full repair/migration/export internals and other evaluators remain named in the coverage table with missing facts. These are available but incompletely inspected, not absent or inaccessible. The report supports bounded positive mechanisms, not full correctness/security/reliability of every included alternative.

## Limitations and checks

The inspected boundary is code-grounded, with no target execution, provider call, test, fixture, evaluator rerun or host observation. Implementation status does not imply deployment activation or benefit. No new source identity or boundary was introduced; source HEAD matches the handed revision. Supplied runtime records remain provisional evidence for the portions labelled supplied. All source-dependent findings use SRC-1 and commit-relative anchors; new consequential mechanisms retain minimum passages.

Correction-round source check: HEAD was rechecked at the handed revision. Direct reads of SRC-1 `mempalace/knowledge_graph.py` covered the as_of filter and invalidate/supersede implementation. They qualify the handler's declared boundary guarantee while preserving transaction and withdrawal findings. The coverage table otherwise retains the previous inspection basis; this round did not repeat unrelated analysis.

Deterministic validation: invocation-specific `commonplace-run validate-output` passed for this corrected output: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Form, citations, identity and quotation occurrence do not establish substantive acceptance.
