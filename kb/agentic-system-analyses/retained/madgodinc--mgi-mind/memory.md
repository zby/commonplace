---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MGI-Mind memory: separate note, fact, playbook and session stores; selective recall, outcome-derived ranking and bounded maintenance."
run-id: AAS-2026-11-08-mgi-mind-e0f02081480f-01
source-identity: https://github.com/madgodinc/mgi-mind
reviewed-boundary: a8defc36f7d0bcd5108714763a12625a0eda0868
---

# MGI-Mind memory report

## Boundary and evidence

This report covers the memory loop of MGI-Mind at SRC-1, commit `a8defc36f7d0bcd5108714763a12625a0eda0868`, using the source register in [boundary](boundary.md#source-register). Included are all shipped memory entry surfaces: CLI, MCP, HTTP, Python integrations, session/transcript handling, note/fact/procedure/skill stores, pinned blocks, quarantine, outcome signals, context selection, exports and maintenance. External host context managers, provider internals and installed model bytes remain outside the inspected source. No target execution, tests, service calls or causal experiment was performed. Implementation and doctrine are distinguished below; neither establishes actual assistant compliance or improvement.

Direct source inspection extended the runtime baseline into `src/procedure.rs`, `src/skill.rs`, `src/outcome.rs`, `src/session_ingest.rs`, fact admission/read/withdrawal in `src/knowledge.rs`, `src/doubt.rs`, `src/activity.rs`, `src/access.rs`, `src/provenance.rs`, `src/vault.rs`, export/rendering and context assembly in `src/cli.rs`, and their storage consumers in `src/storage.rs`. Dispatch and registered-tool searches in `src/mcp.rs`, CLI dispatch in `src/cli.rs`, viewer handler searches in `src/viewer.rs` and relocation searches in `src/relibrary.rs` checked alternate routes. The four Python integration drivers were read directly. HTTP scope, extractor internals, embedding/reranking components and Markdown application are supplied runtime findings rather than independent full reinspection here. All newly inspected paths are within SRC-1, not new sources.

| Entry point / memory operation | Source paths, SRC-1 | Coverage and limits |
|---|---|---|
| Direct CLI/MCP/HTTP add; Python remember/search | `src/cli.rs`, `src/mcp.rs`, `src/storage.rs`, `docs/integrations/openai_agents.py`, `docs/integrations/langgraph.py`, `docs/integrations/pydantic_ai.py`, `docs/integrations/hermes.py` | Direct storage/driver reads plus supplied [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), [RT-RTE-scoped-http](runtime.md#rt-rte-scoped-http); [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-memory-vectors](#mem-obj-memory-vectors). Hermes host registration remains explicitly illustrative. |
| Candidate/raw ingest; recoverable rejection | `src/ingest.rs`, `src/storage.rs` | Direct branch and promotion/expiry reads; [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [MEM-OBJ-quarantine](#mem-obj-quarantine). Near-duplicate rejection and cheap-gate rejection are not interchangeable. |
| Post-session transcript harvest | `src/session_ingest.rs`, `src/cli.rs` | Direct parser and CLI dispatch; [MEM-RTE-transcript-harvest](#mem-rte-transcript-harvest). Both human and model text, not tool evidence, survive. |
| Optional automatic fact extraction | `src/ingest.rs`, `src/extractor.rs` | Enqueue directly read; worker supplied by [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction). Enabled installation and output quality unobserved. |
| Fact add/query/history/as-of/invalidate/restore; cardinality | `src/knowledge.rs`, `src/duel.rs` | Direct admission/default-read/withdrawal inspection; [MEM-OBJ-fact](#mem-obj-fact), [MEM-OBJ-fact-state](#mem-obj-fact-state), [MEM-RTE-fact-lifecycle](#mem-rte-fact-lifecycle). History/as-of implementations not fully traced: complete world-time semantics not established. |
| Doubt-window retrieval/background maintenance | `src/doubt.rs`, `src/activity.rs`, `src/knowledge.rs`, `src/storage.rs` | Direct drift, retest and worker reads; [MEM-OBJ-origin-context](#mem-obj-origin-context), [MEM-RTE-fact-retest](#mem-rte-fact-retest). Typed signal collection mismatch limits the purported fact-feedback chain. |
| Learn/recall; skill set/match/show/list/remove/outcome | `src/procedure.rs`, `src/skill.rs`, `src/storage.rs`, `src/mcp.rs` | Direct read; [MEM-OBJ-procedure](#mem-obj-procedure), [MEM-OBJ-skill](#mem-obj-skill), [MEM-OBJ-procstats](#mem-obj-procstats), [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking); supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). |
| Session start/last/end; context | `src/session.rs`, `src/cli.rs` | End/last/render/build directly read; start/recovery supplied runtime plus function inventory. [MEM-OBJ-session](#mem-obj-session), [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing). Zombie-recovery details not fully inspected; no reliable automatic summary-generation conclusion. |
| Pinned block set/get/list/remove | `src/storage.rs`, `src/mcp.rs` | Direct file/write/read branches; [MEM-OBJ-blocks](#mem-obj-blocks), [MEM-RTE-pinned-blocks](#mem-rte-pinned-blocks). |
| Unified recall, browse/history/by-author, should-search advice | `src/mcp.rs`, `src/storage.rs`, `src/retrieval_policy.rs` | Unified dispatcher directly read; storage/default filter directly read; advice call directly read. [MEM-RTE-unified-recall](#mem-rte-unified-recall). Metadata listings and policy heuristic internals not exhaustively audited; no exhaustive selection-equivalence claim. |
| External snippets; web save | `src/provenance.rs`, `src/cli.rs` | Direct validators/formatter and `run_web`; [MEM-OBJ-memory](#mem-obj-memory). External origin is caller-supplied; web save calls ordinary storage, not ingest. |
| Markdown reconciliation; edit/delete; viewer UI | `src/md_reconcile.rs`, `src/storage.rs`, `src/viewer.rs` | Supplied [RT-RTE-markdown-reconcile](runtime.md#rt-rte-markdown-reconcile), directly read edit, viewer route/handler search. Viewer maps edit/delete/promote to shared storage and offers consolidation preview. UI authentication/rendering not deeply inspected; no universal safe-edit guarantee. |
| Consolidation/archive/restore; access tracking | `src/consolidate.rs`, `src/access.rs`, `src/storage.rs` | Direct policy/access reads plus supplied [RT-RTE-store-consolidation](runtime.md#rt-rte-store-consolidation); [MEM-OBJ-access](#mem-obj-access). |
| Export profile/instructions/JSON/Markdown; backup/restore | `src/cli.rs`, `src/storage.rs` | Direct profile/instruction rendering, verified-procedure selector and archive writer; [MEM-RTE-portable-export](#mem-rte-portable-export). Full JSON/Markdown reassembly and restore failure handling not audited; no complete round-trip equivalence claim. |
| Relibrary, reindex, migration, calibration | `src/relibrary.rs`, `src/storage.rs`, `src/migrate_v14.rs`, `src/calibration.rs` | Relibrary search establishes preserved payload/vector move and access rekey, apply gating; other bodies remain available but uninspected here. Initialization/backfill lineage and changed embedding-space compatibility are not fully established; supplied runtime component findings remain bounded. |
| Audit, outcome logs, evaluator retention | `src/audit.rs`, `src/outcome.rs`, `src/bench_procedural.rs`, `src/bench.rs`, `src/bench_policy.rs`, `src/bench_stale.rs` | Audit API search, direct outcomes and procedural benchmark loop; [MEM-OBJ-audit](#mem-obj-audit), [MEM-OBJ-external-signals](#mem-obj-external-signals), [MEM-CLM-benchmark-isolation](#mem-clm-benchmark-isolation). Other evaluators supplied by boundary, raw result files uninspected. No benchmark score, live feedback-to-production route or efficacy established. |
| Secret vault | `src/vault.rs`, `src/mcp.rs`, `AI_INSTRUCTIONS.md` | Direct terminal store/retrieve and instruction-only MCP branch; [MEM-OBJ-vault](#mem-obj-vault). Cryptographic implementation not audited. |
| Host prompt protocol, install/deployment wrappers | `AI_INSTRUCTIONS.md`, `docs/integrations/`, `src/mcp.rs` | Direct selected protocol and drivers; boundary supplies installation/manual loading limit. No inspected host compactor, token-window hook or isolated assistant subtask frame. This is a limit of the inspected server/drivers, not evidence that external hosts lack them. |

## Core ideas

MGI-Mind retains several different things, not one interchangeable vector memory. Notes retain prose plus dense and sparse indexes; facts use vectorless triples and lifecycle fields; procedures retain error/context/fix text; skills retain named trigger/body playbooks; session summaries and pinned blocks live in files. Procedure/skill outcomes live separately from their content. The embedding is a selection representation, not a readable substitute for the stored note. See [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-fact](#mem-obj-fact), [MEM-OBJ-procstats](#mem-obj-procstats) and the other object records.

Admission is path-specific. Direct add, web save and Markdown replacement do not pass the ingest novelty policy. Ingest can preserve a rejected candidate in quarantine; fact conflict handling can preserve a challenger outside default visibility; playbook outcomes change ranking without rewriting the playbook. Human authorship, approval and physical persistence must not be collapsed: most MCP writes admit caller-supplied content without per-item human approval. The host can be the author, while deterministic server code remains the admission owner ([RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [MEM-RTE-fact-lifecycle](#mem-rte-fact-lifecycle), [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking)).

Read-back is predominantly requested. Calling context returns a selected briefing; calling search returns ranked fragments; calling match retrieves bodies omitted from the catalogue. The automatic selectors run *inside* those requests, not as independent unsolicited host injection. The manual requests the habit; the server cannot establish obedience. A notable secondary path exports verified fixes as instruction text for later host-file consumption, but installed use remains an affordance, not a demonstrated deployment ([RT-BAP-host-recall](runtime.md#rt-bap-host-recall), [MEM-RTE-portable-export](#mem-rte-portable-export)).

Outcome-derived ranking is a wired trace-fed update: reported reuse produces durable counters used on subsequent recall. It is not evidence of semantic criticism, justified truth or improved capacity. Typed labels such as `test_passed` are supplied by callers; no test runner is authenticated by this API. The fact retest path has an additional collection-addressing discontinuity; see [MEM-RTE-fact-retest](#mem-rte-fact-retest).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory
Label: Memory content

Source-native `type=memory` content is natural-language text in Qdrant's `memories` payload. Library/source/author/hash/timestamps and chunk position are symbolic metadata, not the note's warrant. A direct add chunks and embeds caller text, uses content/library-derived IDs and retains original creation time on exact re-upsert. This is the retained endpoint of [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), not a duplicate route; runtime declared no object counterpart. Original material may be human/model-authored notes, external snippets, web Markdown, disk imports or transcript blocks. A source label does not authenticate the original evidence. Later search consumers receive selected text, source and author, not a proof or full original document. SRC-1, `src/storage.rs`, `src/provenance.rs`, `src/cli.rs`.

> let (chunks, overlaps) = stored_chunks(content);
> --- `src/storage.rs`

> let ids: Vec<String> = chunks
>         .iter()
>         .map(|c| deterministic_id(library, c))
>         .collect();
> --- `src/storage.rs`

Provenance admission adds URL/locator/search-tool formatting checks; it does not fetch or independently verify the snippet. Web save executes `crw`, then ordinary storage. Direct edit writes new content and deletes the old point; it carries author but supplies no source to the replacement. No universal old-note rollback follows from that route.

> add_memory_authored(config, &library, new_content, None, author.as_deref()).await?;
> --- `src/storage.rs`

#### MEM-OBJ-memory-vectors
Label: Memory retrieval vectors

Dense vectors derived by [RT-CMP-embedder](runtime.md#rt-cmp-embedder) are distributed-parametric numerical representations stored alongside note payloads in Qdrant. Sparse hashed lexical vectors are symbolic selection indexes. These are separate operative encodings from [MEM-OBJ-memory](#mem-obj-memory): the search code consumes numbers for ranking, while a host interprets returned prose. They are generated on writes, not trained model weights. Configured/installed embedding provenance remains as bounded in the runtime component; no external-provider state is inferred. Closest supplied route is [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), with no object counterpart. SRC-1, `src/storage.rs`.

> let vectors = NamedVectors::default()
>             .add_vector(DENSE_VEC, Vector::new_dense(embedding))
>             .add_vector(SPARSE_VEC, Vector::new_sparse(s_idx, s_val));
> --- `src/storage.rs:1420-1546`

#### MEM-OBJ-quarantine
Label: Quarantined memory

One unchunked Qdrant candidate retains its original text and vectors plus symbolic `quarantined` and `quarantine_reason` fields. It is not a model summary and is not fact-conflict quarantine. Source/author handling differs from ordinary authored add: `add_quarantined` supplies no author. This is the rejected-content endpoint of [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), with no supplied object counterpart. Ordinary search excludes it; quarantine APIs show content/reason. Promotion flips visibility and retains the historical reason. Expiry deletes only if still quarantined and audits a bounded content snapshot; a log entry is not automatic restoration. SRC-1, `src/storage.rs`, `src/ingest.rs`.

> new_payload.insert("quarantined".into(), false.into());
> --- `src/storage.rs`

> // Leave `quarantine_reason` in place as historical trail; the audit entry
> // below records the promotion explicitly.
> --- `src/storage.rs`

#### MEM-OBJ-fact
Label: Fact triple

Source-native subject/predicate/object strings in vectorless Qdrant `_kg_facts` points. Triple slots are symbolic for matching and conflict-axis selection; their values are natural-language assertions for the host. Direct callers and optional extraction can author them. There is no general retained argument explaining why the assertion is correct. Exact triples have deterministic IDs. This is distinct from the optional producer [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) and its transient extraction request; no supplied object counterpart. Later default query, history/as-of, graph and context consumers have different filters. SRC-1, `src/knowledge.rs`.

> let point = PointStruct::new(id.clone(), NamedVectors::default(), payload);
> --- `src/knowledge.rs`

#### MEM-OBJ-fact-state
Label: Fact lifecycle and cardinality state

Symbolic Qdrant payload state controls fact visibility, confirmation counts, author, validity bounds, origin-context ID and optional cached confidence. Predicate cardinality is separately registered in `_kg_predicates`; admission consults it to determine whether conflicting objects compete. These fields are not natural-language criticism. They control the storage/read algorithms, while returned triples have only contextual force on the host. No supplied object counterpart; closest producer is [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction), and closest consumer is [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing). SRC-1, `src/knowledge.rs`, `src/doubt.rs`.

> payload.insert("status".into(), status.as_str().into());
> --- `src/knowledge.rs`

> EntryStatus::Active | EntryStatus::Contested | EntryStatus::Unknown
> --- `src/knowledge.rs`

Default visibility is not synonymous with uncontested truth: contested values can remain visible. Explicit invalidation differs from stale/superseded status; it requires explicit restoration and ordinary reassertion is refused. Reassertion builds a fresh payload from selected old fields; it is not shown preserving every previously attached derived field.

#### MEM-OBJ-procedure
Label: Error fix procedure

Natural-language error/context/fix and optional provenance are stored in `memories`, type `procedure`, library `_procedures`; dense context vectors and sparse normalized-error vectors support selection. This is not a generic note: ordinary note search excludes it. The error normalizer removes volatile path/address/number detail. Identity combines normalized error and fix, so the same lesson can upsert rather than always insert a new independent item. This is distinct from supplied skill admission [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission); no object counterpart. A later procedure recall renders fix, error, context, provenance and trust counters. It does not necessarily retain an explanatory rationale or the originating execution transcript. SRC-1, `src/procedure.rs`, `src/storage.rs`.

> let id = procedure_id(norm_error, fix);
> --- `src/storage.rs`

> payload.insert("library".into(), PROCEDURE_LIBRARY.into());
> --- `src/storage.rs`

#### MEM-OBJ-skill
Label: Named skill playbook

Natural-language `when` trigger and `body`, with symbolic name/ID/timestamps, stored in Qdrant `memories`, type `skill`, `_skills`. Trigger/name vectors select a body; the body itself is not what `add_skill` embeds. Caller-supplied replacement keeps name identity and original creation time. No initial skill corpus or actual field contents were supplied, so body-level rationale, provenance and theoretical content remain unresolved. This object is the endpoint, not a re-declaration of [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Catalogue consumers see names and first nonempty trigger lines; match/show consumers receive bodies. SRC-1, `src/storage.rs`, `src/skill.rs`.

> let embedding = embedder::embed_passage(config, when).await?;
> --- `src/storage.rs`

> payload.insert("body".into(), body.into());
> --- `src/storage.rs`

#### MEM-OBJ-procstats
Label: Procedure and skill outcome statistics

Symbolic counts, latched verified flag and last-used timestamp live in vectorless Qdrant `_mod_procstats`, keyed by procedure or skill ID. They are derived state separate from [MEM-OBJ-procedure](#mem-obj-procedure) and [MEM-OBJ-skill](#mem-obj-skill). Legacy core payload fields can seed reads when side rows are missing. Later recall/match ranks with these values; exports select verified procedures. No supplied object counterpart; this extends the outcome-history limit of [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). SRC-1, `src/storage.rs`, `src/procedure.rs`, `src/skill.rs`.

> let verified = cur.verified || (worked && verify);
> --- `src/storage.rs`

Failures demote ranking but do not clear a previously true verified latch. A verified export is therefore not an independent current correctness certificate.

#### MEM-OBJ-external-signals
Label: Typed external signal log

Structured symbolic `ExternalSignal` records contain signal type, success, source and timestamp. Serialized JSON is written to `external_signals_v15` on `MEMORIES_COLLECTION`, not directly to `_kg_facts`. Caller-provided labels are reported evidence, not captured test execution. Dedup keeps latest per type/source. Later procedure bridging uses novelty of a pair, while fact retest attempts a same-ID signal lookup through the memories helper. Those are distinct consumers with different consequences. No supplied object counterpart; closest route is supplied skill admission's outcome-history reference [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). SRC-1, `src/outcome.rs`, `src/storage.rs`, `src/mcp.rs`.

> set_memory_payload_field(config, memory_id, "external_signals_v15", serialised).await
> --- `src/storage.rs`

#### MEM-OBJ-session
Label: Session file and summary

Local timestamped Markdown session files retain symbolic lifecycle header/footer plus caller-authored natural-language summary. This is a derived continuity artifact, not an automatically retained whole conversation. `session::last(agent)` returns a selected full file; context instead takes global newest and renders first ten header lines plus the entire end footer when present. The manual's roughly 200-word summary is advice, not a code truncation limit. This object is the write/read endpoint of [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing), not a duplicate route. SRC-1, `src/session.rs`, `src/cli.rs`, `AI_INSTRUCTIONS.md`.

> let footer = format!(
>         "\n---\n\n[end]\nended = {}\nsummary = {summary}\n",
>         now.to_rfc3339()
>     );
> --- `src/session.rs`

#### MEM-OBJ-blocks
Label: Pinned blocks

Natural-language content keyed by normalized symbolic names in local `blocks.json`. Set overwrites a map entry, bounded to 4096 bytes per block and 32 blocks; remove deletes it. `load_blocks` treats missing/corrupt JSON as empty. Context includes every loaded block without query ranking. This is distinct from the aggregate consumer [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing); no object counterpart. Content authorship is whoever calls set, not necessarily a human, and the source's “always-true” label is no truth guarantee. SRC-1, `src/storage.rs`, `src/cli.rs`.

> crate::config::mind_home().join("blocks.json")
> --- `src/storage.rs`

#### MEM-OBJ-origin-context
Label: Query activity and origin contexts

The recent query-vector buffer is process-local numerical activity state, not a transcript. Facts can retain an `origin_context_id` referring to numerical centroid vectors in `data_dir/doubt_contexts.json`. Entries have symbolic creation timestamps, content-addressed IDs and oldest-entry eviction under a cap. These numerical representations derive from actual search-query embeddings in this process, not necessarily the entire assistant task. Drift comparisons consume them; the host receives neither their raw content nor an explanation reconstructed from them. Corpus-mean and drift-journal helpers also retain derived numerical activity data; their exact initialization/cache invalidation was not fully traced. No supplied object counterpart; closest supplied read route is [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory). SRC-1, `src/activity.rs`, `src/storage.rs`, `src/knowledge.rs`.

> crate::activity::record_query(&embedding);
> --- `src/storage.rs`

> config.data_dir.join("doubt_contexts.json")
> --- `src/activity.rs`

A missing or evicted origin vector prevents a drift judgment, not evidence that the fact remains true.

#### MEM-OBJ-access
Label: Access journal

Symbolic ID/count/last-access map is accumulated when search surfaces results and periodically persisted as a JSON journal. It is usage metadata, not note content, execution success or user endorsement. Flush merges maximum counts/latest timestamps across disk/process state, so it is not an exact cross-process event ledger. Consolidation reads this derived trace to calculate coldness and later change retrieval membership when apply is requested. No supplied object counterpart; closest supplied route is [RT-RTE-store-consolidation](runtime.md#rt-rte-store-consolidation). SRC-1, `src/access.rs`, `src/consolidate.rs`.

> e.count = e.count.max(stat.count);
> --- `src/access.rs:109-109`

#### MEM-OBJ-audit
Label: Audit event log

Append-only newline JSON local `audit.log` stores symbolic operation/actor/target plus optional natural-language before/after/note snapshots. This is raw mutation history and bounded display content, not a semantic summary or automatically adopted instruction. Search uses separate access counters. The inspected API offers load, target and recent readers and chain verification; source search does not establish automated reconstruction or full undo. Logging is configurable and best effort. No object counterpart; this spans the mutations of [RT-RTE-markdown-reconcile](runtime.md#rt-rte-markdown-reconcile) and [RT-RTE-store-consolidation](runtime.md#rt-rte-store-consolidation), rather than being contained in one. SRC-1, `src/audit.rs`, `src/storage.rs`.

> tracing::warn!("audit: failed to record event: {e:#}");
> --- `src/audit.rs`

#### MEM-OBJ-vault
Label: Secret vault

`VaultData` is a structured key-to-entry map serialized and encrypted to a local vault file under mind home, with separate salt. Secret values are opaque payload strings; key/category/description are readable metadata after decryption, not semantic embeddings. Source storage uses no Qdrant vector search here. Terminal store requires a password; terminal retrieve requires password and, unless `skip_confirm`, explicit y confirmation. MCP returns terminal instructions rather than values. The operator/terminal caller is the established later consumer, not an assistant prompt route. No supplied object counterpart; distinct from [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory). SRC-1, `src/vault.rs`, `src/mcp.rs`, `AI_INSTRUCTIONS.md`.

> let vault: VaultData = serde_json::from_slice(&decrypted)?;
> --- `src/vault.rs`

> if !skip_confirm {
> --- `src/vault.rs`

Encryption changes storage encoding, not the intrinsic representational form of the arbitrary original value. Cryptographic security and any downstream application use remain uninspected.

### Routes

#### MEM-RTE-transcript-harvest
Label: Transcript text harvest

CLI `IngestSession` supplies a local Claude Code JSONL path/library to `ingest_transcript`. Parser code, not a summarizing model, selects user/assistant text blocks, prepends role tags, and sends Memory candidates through ordinary ingest. Human choice initiates the file-level workflow; there is no wired human approval for each retained block. Cheap relevance/novelty/dedup software decides admission. No answer oracle. It is open transcript harvesting, not a controlled improvement experiment. Closest supplied route [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) begins downstream; this route's distinct referent is the transcript-to-candidates transformation. SRC-1, `src/session_ingest.rs`, `src/cli.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rows scanned, blocks extracted, aggregate ingest counters and session ID when parsed.
- Later read-back: Admitted role-tagged text reaches ordinary search; quarantine remains accessible only through its separate review/promotion routes until live.
- Delegated visibility: inapplicable — parser does not create an isolated model frame; tool/thinking blocks are omitted from retained candidates.
- Selection predicate: Only user/assistant rows and text content; malformed rows are skipped, whitespace-only blocks ignored. Tool use/results and thinking are excluded.
- Invalidation or expiry: Downstream quarantine/deletion/archive governs results; source transcript is not deleted by this parser.
- Activation or effect: Durable excerpts can shape later host tool results; no behavioral change or benefit observed.
- Evidence limits: Role tags preserve human/model distinction but not proof of truth. Session-specific source tagging is computed but discarded; candidates supply source None, so retained source defaults to ingest.

> if blk.block_type != "text" {
>                         continue;
>                     }
> --- `src/session_ingest.rs`

> let _ = source_tag; // reserved for a future per-candidate source plumbing.
> --- `src/session_ingest.rs`

This is trace-fed retention of mostly verbatim excerpts, not automatic semantic consolidation. It can still feed optional extraction downstream, where model-produced triples are a further transformation. Normal gate rejection and explicit promotion/expiry supply recovery, not an all-file transaction.

#### MEM-RTE-fact-lifecycle
Label: Fact admission and withdrawal

Caller supplies a triple (or the optional extractor produces one). Knowledge code serializes the fact axis and cross-process writes, reads prior state/cardinality, chooses active/contested/quarantine-candidate, upserts the new payload and retires a losing old object. There is no per-triple human approval requirement. A caller can explicitly invalidate or restore; deterministic duel policy, not an authenticated answer oracle, decides conflicts. This is open-input knowledge change, not a benchmark. Confirmation history and scoring guide reliance, not formulated content-directed criticism. No supplied route counterpart: [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) is one producer; [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) is one consumer. SRC-1, `src/knowledge.rs`, `src/duel.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ID and, on verdict-aware callers, recorded/won/contested/quarantined/invalidated result. The optional worker does not forward these verdicts to the original assistant.
- Later read-back: Default lexical subject/predicate/object queries exclude invalid/hidden statuses; context renders selected visible triples; history and contested APIs expose alternative states explicitly.
- Delegated visibility: No model frame; extractor sees the input content as specified in the supplied producer route, not the assistant's full window.
- Selection predicate: Identical-triple history, predicate cardinality and conflicting objects feed admission. Default read visibility admits active, contested and unknown, not stale/superseded/quarantine-candidate.
- Invalidation or expiry: Explicit valid=false blocks exact and case/whitespace-variant reassertion until explicit restore. Duel retirement keeps traces; restore preserves lifecycle status rather than automatically making a stale item active.
- Activation or effect: Server selection/visibility changes are wired; host belief/action changes and correctness are unobserved.
- Evidence limits: No reference truth verifier or successful conflict episode supplied. Upsert-then-retire avoids retiring before writing the successor but is not an atomic multi-point database transaction.

> if existing_valid.as_deref() == Some("false") {
> --- `src/knowledge.rs`

> crate::duel::DuelOutcome::Quarantine => (EntryStatus::QuarantineCandidate, None),
> --- `src/knowledge.rs`

> apply_doubt_window(config, &mut facts).await;
> --- `src/knowledge.rs`

The retained triple and status do not reconstruct the original reasoning. Audit can retain a verdict and retired object, but the default triple rendering omits those reasons. “Contested” is not synonymous with rejected: a contested value can reach a default consumer.

#### MEM-RTE-fact-retest
Label: Drift and fact retest

Retrieval checks query-derived origin/current centroids when configured; shadow mode measures without changed ordering, enforce mode can update doubt counters and reorder facts. MCP's supplied startup wiring starts an automatic background loop that selects at most 50 candidates per tick, yields to MCP activity and recomputes confidence from payload signals. It writes cached confidence/doubt state, not revised triple content. Code owns promotion/recovery under configured rules; no human approval or answer oracle is part of each tick. This extends [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing)'s inherited-context state, not a duplicate briefing or automatic extraction route. SRC-1, `src/doubt.rs`, `src/knowledge.rs`, `src/activity.rs`, `src/storage.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Query returns facts with in-doubt ordering when enforce conditions are met; background work logs transitions rather than returning a guaranteed result to the triggering caller.
- Later read-back: Stored doubt counters/confidence enter later retest decisions; drift retrieval reads retained origin vectors and counters to set in_doubt. This establishes derived-state reuse, not that every exported/briefing view displays doubt.
- Delegated visibility: No isolated assistant frame; code reads scalar payloads and stored vectors, not a reasoning transcript.
- Selection predicate: Retrieval requires drift mode, origin vector, current query centroid and corpus mean. Background candidate selection is bounded; successful retests clear flags, errors reflag for retry. Exact candidate prioritization remains only partially inspected.
- Invalidation or expiry: Oldest context-vector eviction makes some drift comparisons unavailable; process-local inherited/flag registries reset on restart, and session end clears inheritance. Retest promotes/recovers doubt without deleting the triple.
- Activation or effect: Numeric state and conditional order changes are implemented; semantic falsification and improved answers are not established.
- Evidence limits: HTTP must not inherit MCP lifecycle assumptions. Typed outcome reads target memories while scalar fact inputs target _kg_facts; a complete ordinary fact-signal-to-fact-retest chain is not established.

> let typed_signals = crate::storage::read_external_signals(config, fact_id)
>         .await
>         .unwrap_or_default();
> --- `src/doubt.rs`

> let Some(raw) = existing_payload_string(
>         &client,
>         MEMORIES_COLLECTION,
>         memory_id,
>         "external_signals_v15",
>     )
> --- `src/storage.rs`

> facts.sort_by_key(|f| f.in_doubt);
> --- `src/knowledge.rs`

The collection mismatch is material: a fact ID used by retest is looked up in the memory collection by the typed-signal helper, not the fact collection used for scalar confidence inputs. An incidental same-ID memory would not establish ordinary fact provenance. This does not invalidate the independently wired procedure bridge or scalar fact retest.

#### MEM-RTE-outcome-ranking
Label: Outcome to playbook ranking

Caller reports worked/failed or typed signal/source/success. Code stores counters in `_mod_procstats`; skill outcome reuses the same stats function. `mind_outcome` stores deduplicated typed signals and bridges a *new* test_passed/code_compiled pair on a procedure to counters and verification. Open-input feedback is computationally admitted without mandatory per-content human review; even user_confirmed is an API label, not evidence a human acted. No authenticated test runner or expected-answer oracle is wired here. This route is distinct from supplied body admission [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission): it changes derived reliance, not body content. SRC-1, `src/mcp.rs`, `src/outcome.rs`, `src/storage.rs`, `src/procedure.rs`, `src/skill.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Confirmation of recorded signal/counters; typed procedure bridge can append the procedure update confirmation.
- Later read-back: Recall/match fetch stats, normalize retrieval scores and rank by relevance plus verified boost and outcome ratio; verified-procedure exports consume the same state.
- Delegated visibility: Returned playbooks show content and counts; full original tests, execution logs and causal diagnoses are not supplied by counters.
- Selection predicate: Procedure error/context hybrid retrieval or skill task/trigger hybrid retrieval supplies up to twice the requested candidate count; later ranking/rendering takes the requested limit. Verified adds 0.25; outcome ratio contributes up to magnitude 0.20 as evidence count grows.
- Invalidation or expiry: Body deletion/relearning and separate stats maintenance affect history; verified latches true. Typed same-key repost updates the log but does not rebump counters; manual procedure outcomes are not idempotent.
- Activation or effect: Trace-fed durable stats change subsequent code ranking/selection; changed assistant execution and improved capacity remain unobserved.
- Evidence limits: Reported success is not independently checked. A later same-key success/failure reversal can change the typed log without correcting the earlier counter bump because the bridge tests novelty.

> if signal_was_new
>                 && is_proc_signal
>                 && crate::storage::is_procedure(cfg, memory_id).await?
> --- `src/mcp.rs`

> s += 0.25; // a deterministic-signal-verified fix is trustworthy
> --- `src/procedure.rs`

This is automatic transformation of reported reuse traces into durable behavioral selection state. Origins can be human reports, model/tool callers or external harness reports; the API does not prove which. It retains counts and optional typed source/timestamp, not the causal reason a fix succeeded. Failures reduce rank but do not rewrite claims. No content-directed criticism, reliable learning or exercised self-improvement is inferred from the update alone.

#### MEM-RTE-pinned-blocks
Label: Pinned block admission

MCP/CLI caller supplies name/content; storage validates name, size and total count, atomically writes the JSON map and emits before/after audit. Remove deletes a named entry. Caller can propose replacement/removal and code rejects invalid inputs; initiating a tool call is not human per-block approval. No model transformation, expected-answer oracle or experiment is involved. Distinct from the consuming aggregate [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing). SRC-1, `src/storage.rs`, `src/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Set/remove confirmation or requested block/map text.
- Later read-back: Subsequent context requests load all blocks and render them near the top; profile export renders only each block's first line.
- Delegated visibility: No isolated worker frame; host receives block text when the response is used.
- Selection predicate: Normalized name for get/set/remove; all loaded entries for context, without semantic ranking.
- Invalidation or expiry: Explicit overwrite/remove; missing/corrupt file reads as empty; audit history is not automatic rollback.
- Activation or effect: Future briefing content changes; prompt priority/compliance are not enforced by local placement alone.
- Evidence limits: No deployed blocks or host invocation supplied. Per-block caps are not a global token budget for the host window.

> let prior = blocks.insert(name.clone(), content.to_string());
>     save_blocks(&blocks)?;
> --- `src/storage.rs`

#### MEM-RTE-unified-recall
Label: Requested multi-store recall

Caller invokes `mind_recall_all`; dispatcher queries facts, searches notes and recalls procedures by task context, then concatenates sections. No skill branch appears in this dispatcher; skills use match separately. Code owns selection inside the requested operation, while the caller owns whether to ask and the host owns interpretation. This is distinct from the note-only driver [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory). HTTP structured/scoped alternatives remain as bounded in [RT-RTE-scoped-http](runtime.md#rt-rte-scoped-http). SRC-1, `src/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Facts/current triples, ranked memory snippets and procedure text in separate sections, or nothing-found message.
- Later read-back: Each request can retrieve accumulated content from the three stores; static operating guidance is not itself newly learned memory.
- Delegated visibility: Host gets selected rendered content, not raw indexes, all rejected candidates or complete rationale.
- Selection predicate: Same query feeds lexical facts, note search and context-only procedure recall. Per-silo limit defaults to five; notes use tier two display truncation. There is no one joint score or overall token cap in this dispatcher.
- Invalidation or expiry: Each store's default filters and deletion/withdrawal policies apply before rendering.
- Activation or effect: Multi-store delivery is wired; truthful synthesis or host obedience is unobserved.
- Evidence limits: Each silo is handled with if-let-Ok, so an omitted section may mean an error rather than no relevant knowledge. Tool labels do not establish exhaustive recall.

> if let Ok(mems) = crate::storage::search(cfg, query, None, limit, 2).await
>                 && !mems.is_empty()
> --- `src/mcp.rs`

#### MEM-RTE-portable-export
Label: Learned instruction and profile export

Caller requests export format. Instructions selects verified procedures, sorted by success count, and renders error/fix/provenance/counts as Markdown. Profile renders first-line pinned blocks, up to 40 facts, 15 verified fixes and 24 skill catalogue entries. Code transforms retained state deterministically, without a model summary or per-item human approval. Caller controls whether output is saved; no test oracle validates it. No supplied export route counterpart; it consumes content from [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) only as a catalogue and from the independently declared procedure store as fixes. SRC-1, `src/cli.rs`, `src/storage.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Markdown or file-write confirmation.
- Later read-back: A caller can install generated text in a host instruction file; that external consumer role is afforded by prompt-ready export, not wired automatic deployment in the inspected exporter.
- Delegated visibility: Instruction output includes fixes and counts/provenance; profile omits full skill bodies and all but first lines of blocks.
- Selection predicate: Verified-procedure selector reads core plus side stats, filters verified, sorts success count; profile has fixed item caps, not a joint relevance selector.
- Invalidation or expiry: Later exports recompute from current state; already saved copies are not automatically revoked when underlying memory is deleted or contradicted.
- Activation or effect: File/response generation is wired; authoritative host loading and changed behavior are afforded, not observed.
- Evidence limits: Verified latching is caller-signal based. Export labels do not prove current correctness, semantic compression fidelity or installed instruction precedence.

> all.retain(|h| h.verified);
>     all.sort_by_key(|h| std::cmp::Reverse(h.success_count));
> --- `src/storage.rs`

> "{} verified error→fix procedure(s), most-proven first. Prefer these before \
>          re-deriving a fix.\n\n",
> --- `src/cli.rs`

### Claims

#### MEM-CLM-benchmark-isolation
Label: Claimed procedural benchmark isolation

Source-native evaluator claims a throwaway library and cleans that library before/after, but calls `procedure::learn` with BENCH_LIB only as provenance. The actual procedure storage selects `_procedures`. Thus the inspected evaluator cannot establish the isolation its comment advertises. This is distinct from supplied runtime routes; it limits interpreting procedural recall results as uncontaminated rather than identifying an ordinary assistant consumer. SRC-1, `src/bench_procedural.rs`, `src/storage.rs`.

> // Isolated, throwaway library. Drop first in case a prior aborted run
>     // left it half-populated.
> --- `src/bench_procedural.rs`

> Some(BENCH_LIB),
>             false,
>             Some("bench"),
> --- `src/bench_procedural.rs`

The source evaluator compares recalled `fix.trim()` to dataset gold fix strings and can save per-item JSON. That oracle measures retrieval of provided fixes, not actual fix execution or improved assistant capacity. No retained result files were inspected and no score is asserted.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-store-selection
Label: Retained state controls selection

Consumer: Rust admission, recall/match, context and maintenance code. Channel: lifecycle flags, side-collection outcome counts, access metadata and retained vectors. Force: symbolic filtering/ranking rules and numerical comparisons determine membership/order within those operations; they do not enforce downstream beliefs. Horizon: later requests and maintenance ticks across sessions when durable state is preserved. Unlike [RT-BAP-host-recall](runtime.md#rt-bap-host-recall), this authority acts inside the server before model interpretation. [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking), [MEM-RTE-fact-lifecycle](#mem-rte-fact-lifecycle) and [RT-RTE-store-consolidation](runtime.md#rt-rte-store-consolidation) retain the supporting source passages. SRC-1, `src/storage.rs`, `src/procedure.rs`, `src/skill.rs`, `src/consolidate.rs`.

#### MEM-BAP-playbook-guidance
Label: Retrieved playbook guidance

Consumer: requesting assistant or operator. Channel: recall/match/show tool text, context catalogue then selected body, or portable Markdown export. Force: natural-language advice/instructions whose compliance depends on the host; no local execution of a fix or skill body is established. Horizon: subsequent task invocations, and potentially sessions when exported text is installed. Distinct from note recall [RT-BAP-host-recall](runtime.md#rt-bap-host-recall) by instruction-content and export consumers. [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking), [MEM-RTE-portable-export](#mem-rte-portable-export) and [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) supply evidence. SRC-1, `src/procedure.rs`, `src/skill.rs`, `src/cli.rs`.

## Annotations

#### On [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Retained results are live note chunks, single-point quarantine or independent fact/procedure writes, not one uniformly curated memory. Promotion on repeated cheap/novelty rejection occurs before a new quarantine write; the near-duplicate branch preserves a distinct candidate in quarantine but does not itself call promotion. An explicit promote remains available. Reason survives promotion even though an adjacent comment says it clears. Content was retained, not necessarily improved. SRC-1, `src/ingest.rs`, `src/storage.rs`; [MEM-OBJ-quarantine](#mem-obj-quarantine) retains the passage.

#### On [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing)

Read-back is requested briefing with automatic selection *inside* the request. Session rendering keeps the first ten header lines and the complete end footer; it is not blindly the first ten lines of a completed session. Skills remain reachable through match/show despite omission of bodies. Pinned block count/byte limits, 20 fact candidates and 24 catalogue entries constrain individual surfaces, but do not establish one token budget. After selecting at most 20 facts, context checks `valid_until` with a missing lower bound rather than the stored `valid_from`. Thus “temporally valid” needs qualification. SRC-1, `src/cli.rs`.

> if crate::knowledge::fact_valid_at(None, valid_until.as_deref(), &now) {
> --- `src/cli.rs`

The session summary is caller-authored; the server does not run a raw conversation-to-summary model here. The material is durable across later invocations, but host trimming, compaction and actual model-visible context remain outside this route's control.

#### On [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Outcome counts/verification are in separate `_mod_procstats`, shared with procedures. Replacing a body does not independently verify the new body; its stable identity can retain trust history. Trigger-based vectors retrieve the body; catalogue renders first nonempty trigger line. Actual body content and original reason histories remain unavailable in this source-only analysis. SRC-1, `src/storage.rs`, `src/skill.rs`; [MEM-OBJ-skill](#mem-obj-skill), [MEM-OBJ-procstats](#mem-obj-procstats), [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking) supply passages.

#### On [RT-RTE-store-consolidation](runtime.md#rt-rte-store-consolidation)

Curation here selects survivors, not a model-generated merged semantic summary. Near-duplicate policy keeps longer content, with older creation time as tie breaker; access-derived coldness can change later membership. Archive versus prune changes reversibility. SRC-1, `src/consolidate.rs`.

> if la != lb {
>         // Drop the shorter one.
>         return if la < lb { &a.id } else { &b.id };
>     }
> --- `src/consolidate.rs`

This is another automatic trace-fed transformation only when maintenance applies it: search-surfacing counts affect coldness, apply changes retrieval membership. It does not retain reasons why an assistant found the memory useful.

## Write side

**Acquisition and authoring.** Assistant candidate extraction is requested by `AI_INSTRUCTIONS.md`, whereas raw ingest uses a heuristic and post-session ingest uses a text-block parser. Their origins differ: user text, assistant text and external snippets can all enter retained content. [MEM-RTE-transcript-harvest](#mem-rte-transcript-harvest) preserves those distinctions and its session-source loss. The four integration examples use direct add rather than gated ingest. Provenance formatting improves locatability without checking truth. These alternatives make “all memory is automatically extracted” and “every write passes relevance gating” false within the inspected boundary ([MEM-OBJ-memory](#mem-obj-memory), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)).

**Admission and rejection.** Direct storage checks library/secret content; ingest adds relevance/novelty/near-duplicate policies with recoverable quarantine. Fact admission consults cardinality and retained assertions; named skill/block updates replace caller content under structural caps. Starting a file import, transcript harvest or maintenance pass is not proof of human per-content approval. The manual separately asks the assistant to ask before appending a permanent rule to the host rules file; that is doctrine for an external editing surface, not a universal server gate (SRC-1, `AI_INSTRUCTIONS.md`; [MEM-RTE-pinned-blocks](#mem-rte-pinned-blocks), [MEM-RTE-fact-lifecycle](#mem-rte-fact-lifecycle), [RT-RTE-markdown-reconcile](runtime.md#rt-rte-markdown-reconcile)).

> append only, and ask first.
> --- `AI_INSTRUCTIONS.md`

**Transformation and maintenance.** Chunking/indexing preserves prose fragments; transcript parsing omits tool/thinking content; optional extraction derives triples; session end stores a caller-supplied continuity summary; counters derive ranking from reports; consolidation removes selected material rather than rewriting its meaning. Unknown initial installed memories, skill content and migration/backfill state do not erase these known subsequent transformations. Neither the summarizer's reasons nor a full raw execution trace is guaranteed to accompany derived instructions. Source reasons may remain in provenance/audit fields, but ordinary context triples and profile summaries omit much of that material ([MEM-OBJ-session](#mem-obj-session), [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking), [MEM-RTE-portable-export](#mem-rte-portable-export)).

**Withdrawal and recovery.** Quarantine can be explicitly promoted or expired; archived notes can be restored; fact invalidation requires explicit restore; duel retirement retains historical rows; deletion and Markdown replacement have different recovery properties. In-place same-name playbook overwrite is not a versioned-body rollback. Backup retains Qdrant snapshots when possible and otherwise warns that direct storage copying needs quiescence; this is a distinct checkpoint form, not a compacted semantic memory. Its later consumer is the restore operation, which uploads snapshots/extracts files, not a model interpreting archive bytes. Exact failure/round-trip behavior remains uninspected (SRC-1, `src/storage.rs`; [RT-RTE-markdown-reconcile](runtime.md#rt-rte-markdown-reconcile), [RT-RTE-store-consolidation](runtime.md#rt-rte-store-consolidation)).

> That copy is only consistent if nothing was writing to it; \
>              stop Qdrant first if this store is live."
> --- `src/storage.rs`

**Evaluation.** Procedural benchmarking supplies a fixed gold-fix retrieval oracle and optionally saves raw ranked results, not a test-execution outcome oracle. Its claimed isolation needs qualification. Other benchmark branches and retained scores remain uninspected or supplied-boundary-only here. No inspected automatic path feeds benchmark scores into installed memory policy or model weights; this is an inspection limit, not a system-wide evidenced absence ([MEM-CLM-benchmark-isolation](#mem-clm-benchmark-isolation)).

## Read-back

The strongest wired host path is the shipped tool wrapper: host chooses recall, Python calls search tier two, server ranks full content then truncates display to 500 characters, and returned text becomes a host tool result. It is request-directed retrieval. The dense/sparse filters exclude skills/procedures/quarantine and normally archive; search has library, author, source and date targeting. A file or ID lookup elsewhere is a different selector, not semantic relevance ([RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), [MEM-OBJ-memory-vectors](#mem-obj-memory-vectors)).

Unified recall separately combines fact, note and procedure results without a global token budget. Skill match defaults to three outputs and searches trigger/name rather than full body; the caller can reload a body omitted from the context catalogue. Browse/history/quarantine APIs offer deliberate inventory/review paths, not unsolicited model context. Typed signals and access counts primarily reach server selection/maintenance consumers, rather than being equivalent to stored prose delivered to the assistant ([MEM-RTE-unified-recall](#mem-rte-unified-recall), [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking), [MEM-BAP-store-selection](#mem-bap-store-selection)).

Context assembly preferentially keeps bodies out and leaves an index plus reload operation. Session rendering removes most header/body lines but keeps the end summary. This resembles selecting a compact checkpoint, not an isolated sub-agent frame: no pushed child assistant context or whole-frame pop/return was found in the inspected server/drivers. The window receives text by value; a catalogue name is only a pointer in the operational sense that the assistant may call match/show, not an automatically followed memory reference. The host still owns accumulation, eviction and any actual compaction. Per-object bounds do not prove a global bounded window ([RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing), its annotation above).

Portable instruction/profile export supplies a separate afforded consumption channel. Subsequent host-file loading can have stronger authority than one advisory recall result, but installation, priority and revocation are not wired by export itself. Vault read-back is terminal/operator access only on the inspected surface. Backup restoration changes storage for later reads; it is not itself a natural-language memory delivery ([MEM-RTE-portable-export](#mem-rte-portable-export), [MEM-OBJ-vault](#mem-obj-vault)).

## Integration issues

1. **Temporal qualification of briefing.** Correct the broad “temporally valid facts” description in [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing): direct `build_context` inspection shows `fact_valid_at(None, valid_until, now)`, so the stored lower bound is not checked there. Status/valid filtering remains wired. This prevents claiming complete world-time filtering for that consumer; see its annotation and [MEM-OBJ-fact-state](#mem-obj-fact-state).
2. **Fact typed-signal continuity unresolved.** [MEM-RTE-fact-retest](#mem-rte-fact-retest) reads fact scalars from `_kg_facts` but typed signals through a helper targeting `memories`. [MEM-OBJ-external-signals](#mem-obj-external-signals) writes that memory collection. A fact-wide external-evidence correction claim requires another supported bridge; do not transfer the working procedure bridge's status to this path. This is source-level discontinuity, not lack of execution evidence alone.
3. **Caller labels versus measured success.** [MEM-RTE-outcome-ranking](#mem-rte-outcome-ranking) can verify from caller-supplied signal labels, and its novelty bridge does not revise counters on same-key reversal. [MEM-OBJ-procstats](#mem-obj-procstats) latches verification. Reconciliation must not call this authenticated testing, semantic criticism or demonstrated capacity improvement.
4. **Evaluator contamination possibility.** [MEM-CLM-benchmark-isolation](#mem-clm-benchmark-isolation) distinguishes temporary-library cleanup from actual `_procedures` writes. No benchmark results were adopted. This prevents treating that evaluator's comments as proof of independent clean-room recall or post-test restoration.
5. **Lineage loss in transcript harvest.** [MEM-RTE-transcript-harvest](#mem-rte-transcript-harvest) retains role tags but discards session-specific source tagging. This limits session-targeted provenance claims even though parser input and returned report know the ID.
6. **Quarantine mechanisms differ.** [MEM-OBJ-quarantine](#mem-obj-quarantine) is ordinary memory with a flag/reason; [MEM-OBJ-fact-state](#mem-obj-fact-state) has fact quarantine-candidate status. The ingest promotion branch does not imply automatic promotion for every near-duplicate or fact. Historical reason survives flag promotion despite contrary nearby comment.
7. **Object/route overlaps, not duplicates.** Every new object records the retained endpoint or operative part of supplied routes; runtime declares no objects. New transcript parsing is upstream of supplied ingest; fact lifecycle is downstream of supplied extraction; pinned writes are upstream of supplied briefing; playbook outcomes are distinct from supplied skill body admission. [MEM-BAP-playbook-guidance](#mem-bap-playbook-guidance) overlaps host textual interpretation in [RT-BAP-host-recall](runtime.md#rt-bap-host-recall), but adds procedure/skill and exported-instruction consumers. No replaceable duplicate record identified.
8. **Included unresolved surfaces.** Coverage table retains migration/calibration/backfill initialization, complete export/reassembly/restore behavior, detailed history/as-of semantics, candidate prioritization in background retest, viewer authorization, external host scheduling and raw benchmark results as uninspected. These prevent global completeness, safety, exact temporal equivalence and efficacy claims; they do not negate traced retention, requested recall or derived ranking.

## Limitations and checks

Checkout HEAD was rechecked as `a8defc36f7d0bcd5108714763a12625a0eda0868`, matching boundary. Only registered SRC-1 files and handed contracts/members were used; no prior analyses or other revisions were consulted. Source inspection was read-only. No target command or tests were run. Governing method is the supplied memory job, member type and shared record contract; no authoring skill or delegation was used.

The supplied runtime is provisional evidence and its passages support the cited routes, not observed execution. Direct inspection challenged universal admission, truth/verification, temporal-filtering, quarantine-reason and benchmark-isolation interpretations. Local contradictions/uncertainties are retained above rather than erased. Parameter components remain as separately assessed in runtime; state-derived adaptation does not imply weight training. No reliable host compliance, improved capacity, causal benefit or exercised self-improvement is established.

Validation: completed with the invocation-specific commonplace-validate command; the final successful result establishes structural/quotation checks only, not semantic acceptance.
