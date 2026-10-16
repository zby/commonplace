---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Spacebot memory: typed claims, temporal summaries, transcript recovery, procedures and instance wiki at the frozen runtime boundary."
run-id: AAS-2026-10-14-spacebot-6a954b400f95-01
source-identity: https://github.com/spacedriveapp/spacebot
reviewed-boundary: "5c2ee47b397e09c956dc15000ea576ecd28e92bb"
---

# Spacebot memory report

## Boundary and evidence

Spacebot retains several different kinds of material, not one undifferentiated memory. This account includes typed agent memories, numerical retrieval indexes, human anchors, working-memory events and summaries, durable conversation and worker traces, session chronicles, skills, identity instructions, wiki pages, and the task/goal/project/wake state supplied to later decisions. The functional boundary and source identity are those of [boundary](boundary.md#boundary-and-evidence), SRC-1 at `5c2ee47b397e09c956dc15000ea576ecd28e92bb`.

Direct reads below are implementation evidence unless identified as prompt doctrine or evaluator definition. They supplement, rather than merely repeat, [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn), [RT-RTE-context-control](runtime.md#rt-rte-context-control) and [RT-RTE-skill-change](runtime.md#rt-rte-skill-change). Source reading included bounded bodies/searches, not an exhaustive audit. No target execution, provider call, dependency installation or test run was performed. No deployment/database/trace was supplied. External providers, OpenCode internals and remote MCP implementations remain outside the frozen source; their opaque retention and embedding/model provenance cannot be reconstructed from this repository.

### Coverage inventory

“Direct” means this analyst read the named source, not an observed execution. A supplied route's evidence remains attributed to that member. Available but uninspected detail is not an access gap or evidence of absence.

| Entry point / operative part | Source paths and inspection | Covering records, or missing fact and prevented conclusion |
|---|---|---|
| Startup stores and human seeding | Direct search of `src/main.rs`; direct `src/memory/types.rs`, `src/memory/store.rs`; supplied `src/db.rs` coverage | [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-memory-metadata](#mem-obj-memory-metadata), [MEM-OBJ-human-anchor](#mem-obj-human-anchor). Configured human seed body not traced fully; cannot establish overwrite policy for every org edit. |
| Periodic conversation extraction; branch tools and completion hook | Direct `src/agent/channel.rs`, `src/agent/channel_dispatch.rs`, `src/tools.rs`, `src/tools/memory_save.rs`, `src/tools/memory_persistence_complete.rs`; hook search `src/hooks/spacebot.rs`; prompt doctrine `prompts/en/memory_persistence.md.j2` | [MEM-RTE-memory-admission](#mem-rte-memory-admission). Standard channel isolation is not universal: direct/autonomy/cortex-chat and full-memory workers have alternate save grants. |
| File ingestion and API upload/history removal | Direct `src/agent/ingestion.rs`, `src/api/ingest.rs` | [MEM-RTE-file-ingestion](#mem-rte-file-ingestion). Initial source authorship and semantic trust unresolved; upload is not approval of each extracted claim. |
| Public store APIs and memory tool mutations | Direct `src/memory/store.rs`, `src/tools/memory_save.rs`, `src/tools/memory_delete.rs`, `src/tools/memory_consolidate.rs`, `src/memory/consolidation.rs` | [MEM-RTE-memory-admission](#mem-rte-memory-admission), [MEM-RTE-memory-curation](#mem-rte-memory-curation). Bare store save/update can omit indexing/contract state; API capability alone is not another later-consumer route. |
| Embedding, FTS, graph and metadata recall | Direct `src/memory/embedding.rs`, `src/memory/search.rs`, `src/tools/memory_recall.rs`; store query bodies/search | [MEM-CMP-embedding-model](#mem-cmp-embedding-model), [MEM-OBJ-retrieval-index](#mem-obj-retrieval-index), [MEM-RTE-memory-recall](#mem-rte-memory-recall). Lance table implementation not independently audited; no recall-quality result. |
| Automatic store/participant context | Direct `src/memory/render.rs`, `src/memory/working.rs`, `src/agent/channel.rs` | [MEM-RTE-context-supply](#mem-rte-context-supply). First-line displays are not full content. |
| Cortex synthesis and association passes; janitor | Direct selected `src/agent/cortex.rs`, `src/agent/maintenance.rs`, `src/memory/maintenance.rs` | [MEM-RTE-temporal-synthesis](#mem-rte-temporal-synthesis), [MEM-RTE-memory-curation](#mem-rte-memory-curation). Tick activity and janitor configuration are not known for a deployment. |
| Durable conversation, rolling history and private frames | Direct hydration in `src/agent/channel.rs`; supplied compactor/worker/branch account | [MEM-OBJ-conversation-log](#mem-obj-conversation-log); annotations on [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history), [RT-RTE-context-control](runtime.md#rt-rte-context-control), [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work). Full private tool history is not the durable conversation log. |
| Chronicle cuts, fallback markers, rollup, view, expansion | Direct selected `src/agent/chronicle.rs`, `src/tools/chronicle.rs`; registration in `src/tools.rs` | [MEM-OBJ-chronicle-checkpoint](#mem-obj-chronicle-checkpoint), [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention). Exact database conflict/fence interleavings and all rollup failure forms not audited. |
| Cross-channel and attachment recall | Direct search of `src/tools/channel_recall.rs` and branch registration; attachment route inventoried only | Channel recall is included in [MEM-RTE-memory-recall](#mem-rte-memory-recall). Attachment recall and binary/saved attachment transformations remain uninspected; cannot claim complete recoverability of attachments from text history. |
| Skills, support files and provenance | Supplied `src/skills.rs`, `src/tools/skill_manage.rs`, `src/tools/read_skill.rs`, installer coverage; direct reflection prompt | Annotated [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set) and [RT-RTE-skill-change](runtime.md#rt-rte-skill-change). Generic file/shell and external installation differ from reflection admission. |
| Identity and generated agent profile | Direct `src/identity/files.rs`, channel identity render; direct profile generator in `src/agent/cortex.rs`; supplied factory/config admission | [MEM-OBJ-identity](#mem-obj-identity). Profile-card SQLite write known, later behavioral consumer unestablished; no profile-to-agent instruction loop inferred. All human-org mutation propagation remains unresolved. |
| Wiki tools, API and CLI | Direct `src/wiki/store.rs`, `src/tools/wiki_read.rs`, `src/cli/wiki.rs`, selected `src/api/wiki.rs`; tool registration | [MEM-OBJ-wiki-page](#mem-obj-wiki-page), [MEM-RTE-wiki-editing](#mem-rte-wiki-editing). Every API handler and UI caching rule not audited. |
| Memory CLI / administrative read surface | Direct `src/cli/mod.rs`, `src/cli/memory.rs`, search of `src/api/memories.rs` | [MEM-RTE-memory-recall](#mem-rte-memory-recall). CLI List/Search are inspection, not an independent authoring command. |
| Tasks, goals, projects, durable wakes and autonomy runs | Supplied runtime; direct task inclusion in `src/memory/render.rs` | [RT-RTE-autonomy-epoch](runtime.md#rt-rte-autonomy-epoch), [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work). Task status has symbolic execution consequences as well as a natural-language display. Full task/goal/project revision stores and wake retry semantics uninspected; cannot equate these state machines with validated knowledge. |
| Worker/OpenCode transcripts and outcomes | Supplied runtime; direct search of restore path in `src/agent/channel_dispatch.rs`; direct reflection prompt | [RT-RTE-opencode-work](runtime.md#rt-rte-opencode-work), [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work), [RT-RTE-skill-change](runtime.md#rt-rte-skill-change). Driver snapshots are not proof of external OpenCode's full internal context. |
| Captured prompts, audit/usage and evaluation | Direct prompt sweeper in `src/agent/maintenance.rs`; hook and `tests/behavioral_fixtures.rs` searches; source-local maintenance/chronicle tests encountered | Captures are expiring debug evidence, not a traced automatic learning input. Evaluator definitions check routing/contracts; no test outcome or semantic memory benefit supplied. |

Static presets, built-in skills and shipped prompts are included as initialization/guidance, not read-back merely because they are loaded. Generic filesystem work products may later be read explicitly, but their unrestricted contents and unknown future callers do not establish a more specific memory consumer. External provider state, remote service state and OpenCode's internal memory remain excluded implementations, not absent memory.

## Core ideas

1. **Automatic context is shallow; recall is another operation.** The global renderer selects a fixed type order and emits first lines with dates, not whole claims or their sources. Human anchors are separately scoped to present participants. A branch can retrieve more and return a conclusion. Automatic delivery does not establish that the foreground model used the selected material ([MEM-RTE-context-supply](#mem-rte-context-supply), [MEM-RTE-memory-recall](#mem-rte-memory-recall)).
2. **Traces have several derived destinations.** Conversation text can become typed memories or procedural skills; working events become intraday/daily narratives; old conversation spans become chronicles. These have different retention, loss and recovery behavior. A checkpoint pointer is not a live reference to the removed model window ([MEM-RTE-temporal-synthesis](#mem-rte-temporal-synthesis), [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention), [RT-RTE-skill-change](runtime.md#rt-rte-skill-change)).
3. **Semantic judgment and admission checks are different.** A model chooses what to save and how to merge it. Code validates types, size, identifiers and a terminal accounting contract. That contract proves neither truth nor useful extraction. Similarity-generated `Updates` edges need not encode an actual revision relation ([MEM-RTE-memory-admission](#mem-rte-memory-admission), [MEM-RTE-memory-curation](#mem-rte-memory-curation)).
4. **Withdrawal is route-local.** Forgetting removes a memory from ordinary recall/render, but does not erase prior prompt copies, logs, skills, wiki pages or summaries derived from it. Index upkeep and semantic withdrawal are separate. Archived wiki discovery and explicit slug reads also differ ([MEM-RTE-memory-curation](#mem-rte-memory-curation), [MEM-RTE-wiki-editing](#mem-rte-wiki-editing)).

## Shared records

### Components

#### MEM-CMP-embedding-model
Label: EmbeddingModel text encoder

Source-native identity: `EmbeddingModel`, distinct from provider inference in [RT-CMP-spacebot-model](runtime.md#rt-cmp-spacebot-model). It wraps `fastembed::TextEmbedding` in an Arc; local model files live in a configured cache. Parameters and output vectors are distributed-parametric representations; their cache and LanceDB are substrates, not forms. SRC-1, `src/memory/embedding.rs` implements text embedding through default fastembed options and blocking inference tasks. Exact model version pinned: not established by this wrapper; it supplies default options without an explicit model/revision. Parameters change during operation: no parameter-update call in the inspected wrapper; downloaded-weight provenance and dependency internals remain uninspected. Mutable endpoint can resolve to another model: this is a local loaded encoder, not the runtime LLM routing endpoint; selection/download resolution behind default initialization is uninspected. Do not infer training from new stored vectors.

> let options = fastembed::InitOptions::default()
>     .with_cache_dir(cache_dir.to_path_buf())
>     .with_show_download_progress(true);
> --- `src/memory/embedding.rs`

### Operative objects

#### MEM-OBJ-memory
Label: Memory claim content

Source-native identity: the `content` part of `Memory`, persisted per agent in SQLite `memories`; natural-language claims interpreted by later models. Distinct from the live message container [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history) and procedural files [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set); neither supplied object denotes this store. Text originates from model tool arguments, extracted conversations/files, and configured human-anchor seeds. Initial deployed contents are unknown. Updates and consolidation can replace text; human saves append observations to an existing anchor. A source string or checkpoint link is optional provenance, not a truth guarantee. Consumers receive full content through recall or a first-line display through automatic render (SRC-1, `src/memory/types.rs`, `src/tools/memory_save.rs`, `src/memory/render.rs`, `src/tools/memory_recall.rs`).

> pub struct Memory {
>     pub id: String,
>     pub content: String,
>     pub memory_type: MemoryType,
> --- `src/memory/types.rs`

#### MEM-OBJ-memory-metadata
Label: Memory selectors and association graph

Source-native identity: `Memory` type/importance/timestamps/access counters/source/channel/forgotten/provenance fields and `Association` rows. SQLite stores symbolic metadata; fixed code rules use type, importance and forgetting to select content, and weighted typed graph edges to rank neighbors. A source label's prose may be interpreted by readers but is not authenticated lineage. These are separate operative parts from [MEM-OBJ-memory](#mem-obj-memory), not another declaration of a supplied runtime object. Model saves propose association types; automatic similarity passes also create them. `Contradicts` reduces a graph score; it is not an enforced contradiction-resolution procedure (SRC-1, `src/memory/types.rs`, `src/memory/store.rs`, `src/memory/search.rs`, `src/agent/cortex.rs`).

> RelationType::Updates => 1.5,
> RelationType::CausedBy | RelationType::ResultOf => 1.3,
> RelationType::RelatedTo => 1.0,
> RelationType::Contradicts => 0.5,
> RelationType::PartOf => 0.8,
> --- `src/memory/search.rs`

#### MEM-OBJ-retrieval-index
Label: EmbeddingTable and chronicle index

Source-native identity: `EmbeddingTable` and optional `ChronicleEmbeddingTable`, persisted in LanceDB. Memory/checkpoint IDs and text are symbolic/textual stored fields; dense embeddings are distributed-parametric retrieval representations derived from content. They select candidates; SQLite resolves authoritative current memory text and forgotten state. Embeddings are not another readable summary and do not themselves give the model instructions. Checkpoint hit output can be just title/channel/sequence/similarity, not full checkpoint content. No counterpart after comparison with [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history); this index does not contain the live window. SRC-1, `src/memory/search.rs`, `src/tools/memory_save.rs`, `src/tools/memory_recall.rs`. Underlying Lance schema/index implementation and complete startup repair coverage remain uninspected.

> if let Some(memory) = self.store.load(&memory_id).await?
>     && !memory.forgotten
> --- `src/memory/search.rs:332-341`

#### MEM-OBJ-human-anchor
Label: Per-human anchor mapping and cache

Source-native identity: human-anchor mapping resolved by `get_human_anchor`, and `ChannelState.human_anchor_cache`. SQLite maps an exact platform-scoped human key to a human-typed Memory; session memory caches the resulting text or a miss. Mapping is symbolic, anchor text natural-language, cache a copy rather than a live reference. Distinct from supplied channel history: it is separately queried and rendered. SRC-1, `src/memory/store.rs`, `src/tools/memory_save.rs`, `src/memory/working.rs`, `src/agent/channel.rs`. Model-provided observations and startup org seeds can populate anchors; complete seed replacement/provenance control is unresolved. Later participant context receives only a first line, after participant and budget filtering. A session-cached miss or old value can persist; immediate refresh after every write is not established.

> if let Some(cached) = cache.lock().await.get(human_id) {
>     return Ok(cached.clone());
> }
> --- `src/memory/working.rs`

#### MEM-OBJ-working-events
Label: WorkingMemoryEvent rows

Source-native identity: `WorkingMemoryEvent` in per-agent SQLite `working_memory_events`. Event type/time/channel/user/importance are symbolic selectors; summary/detail are text. Runtime event emitters and model-selected persistence events supply mixed lineage: these are not all raw human utterances. Event summaries are not complete process payloads or tool traces. Store `record` spawns a write and logs failure rather than blocking its caller. Consumers include Cortex synthesis and working-memory/activity/participant context. Distinct from [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history): this is an agent-wide temporal event store (SRC-1, `src/memory/working.rs`, `src/tools/memory_persistence_complete.rs`, `src/tools/memory_save.rs`).

> /// Fire-and-forget event recording. Spawns a task, never blocks the caller.
> --- `src/memory/working.rs`

#### MEM-OBJ-temporal-summaries
Label: IntradaySynthesis and DailySummary

Source-native identity: `IntradaySynthesis` and `DailySummary`, SQLite derived narratives with dates/ranges/counts. Natural-language summaries are separate from symbolic coverage/time metadata and from event inputs in [MEM-OBJ-working-events](#mem-obj-working-events). They are not the chronological channel window [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history). Model-produced intraday text summarizes event summaries, not every raw payload; daily synthesis uses intraday text plus an unsynthesized raw-event tail. Later channel preambles receive budgeted summaries. No required field retains a content-directed criticism or a derivation argument; reasons present in prose can survive only if the summarizer includes them (SRC-1, `src/memory/working.rs`, `src/agent/cortex.rs`).

> // Build input from intra-day synthesis paragraphs + any unsynthesized tail.
> --- `src/agent/cortex.rs`

#### MEM-OBJ-conversation-log
Label: Durable conversation messages

Source-native identity: conversation rows read through `ConversationLogger`/`ChronicleStore`; per-agent SQLite. Natural-language message content with symbolic role, sender, sequence and time. Distinct from, not a contained part of, [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history): live history and durable text are different containers with different contents and lifetimes. Hydration reconstructs text messages, not original private tool-call objects. Channels, chronicle summarizers and channel-recall branches consume these rows (SRC-1, `src/agent/channel.rs`, `src/agent/chronicle.rs`, `src/tools/channel_recall.rs`).

> // Tool calls and tool results are never persisted to the conversation log,
> // so a tool-heavy turn would otherwise be dropped from live context with
> // nothing recorded about it anywhere.
> --- `src/agent/chronicle.rs`

This comment concerns the conversation log, not all tracing: worker transcripts and debug prompt capture are different stores. It prevents treating transcript expansion as exact recovery of every former model-visible value.

#### MEM-OBJ-chronicle-checkpoint
Label: ChronicleCheckpoint summaries and coverage

Source-native identity: durable SQLite `ChronicleCheckpoint` records, not live rolling summaries. Text titles/summaries are natural-language; sequence/kind/level/range/rollup relations are symbolic navigation and coverage state. This object supplements [RT-RTE-context-control](runtime.md#rt-rte-context-control), not [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history)'s in-memory referent. Ordinary cuts summarize a durable span with prior narrative context and available discarded live tool traffic. Bootstrap covers an oldest readable backlog slice; summarization failure can retain only an unsummarized notice. Emergency truncation records discarded coverage without a semantic summary. Higher-level rollups derive from prior checkpoint summaries. Consumers include later prompt views, tool open/expand, and optional embedded checkpoint search (SRC-1, `src/agent/chronicle.rs`, `src/tools/chronicle.rs`, `src/memory/search.rs`).

> tracing::warn!(%error, "chronicle summarization failed, recording an unsummarized span");
> (fallback_title, unsummarized_notice(messages.len()), None)
> --- `src/agent/chronicle.rs`

#### MEM-OBJ-wiki-page
Label: WikiPage content and versions

Source-native identity: `WikiPage`, `WikiPageVersion`, instance-wide SQLite page/version tables and FTS. Natural-language content and optional edit summaries; symbolic slug/type/version/author/related/archive fields control discovery and history. This shared store is distinct from agent-local typed memories and the filesystem [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set); no supplied counterpart. Explicit tools/API/CLI create or revise content and later readers retrieve it. Versions retain prior content, not necessarily the reasons for its claims. `wiki_read` resolves inline linked titles one hop without linked bodies (SRC-1, `src/wiki/store.rs`, `src/tools/wiki_read.rs`, `src/cli/wiki.rs`).

> /// Inline wiki: links resolved to their current titles (one hop, no content).
> --- `src/tools/wiki_read.rs`

#### MEM-OBJ-identity
Label: Identity files and rendered identity

Source-native identity: `Identity` soul/identity/role fields loaded from agent-root `SOUL.md`, `IDENTITY.md`, `ROLE.md`. Filesystem text, then live runtime snapshots; natural-language instruction content delivered verbatim into later system prompts. Missing files can be scaffolded from shipped presets; existing content is left intact. Initial custom authoring and each deployed mutation are unknown. Supplied [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) covers configuration admission, but these instruction bodies are a distinct object from routing settings and [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set). Factory/API changes and generic filesystem paths require separate authority analysis; the file's comment about sandbox protection is not an unconditional guarantee under disabled containment (SRC-1, `src/identity/files.rs`, `src/agent/channel.rs`; [RT-CLM-role-grants](runtime.md#rt-clm-role-grants)).

> /// Files render verbatim — an identity file carries its own headings,
> /// so the renderer adds none — and blank files render nothing.
> --- `src/identity/files.rs`

### Routes

#### MEM-RTE-memory-admission
Label: Memory extraction and tool admission

Endpoints/progression: runtime turn/time/event-density trigger → silent persistence branch with copied current history → model recall/save/consolidation decisions → SQLite/index writes and terminal accounting → later recall/render. Distinct knowledge-write route from instruction revision [RT-RTE-skill-change](runtime.md#rt-rte-skill-change), although the same branch may perform both. Runtime chooses when and which grants; model proposes/decides semantic content; code can veto malformed type/size/importance/human-key requests and embedding failures. User initiation of a conversation is not per-content human approval. Operating mode is open retrospective extraction; no expected-answer oracle. Prompt asks selective retention, recall first, stale-memory verification and abstention. Direct channels, autonomy/cortex-chat and full-memory workers can save without this automatic branch trigger (SRC-1, `src/tools.rs`, `src/agent/channel.rs`, `src/agent/channel_dispatch.rs`, `src/tools/memory_save.rs`, `prompts/en/memory_persistence.md.j2`).

- Immediate return: save success/refusal, saved ID and optional consolidation advice; branch completion stays out of ordinary channel history.
- Later read-back: saved text reaches later automatic render or explicit recall; validated extracted events enter temporal storage and subsequent synthesis.
- Delegated visibility: branch gets current channel history, not a fresh full historical database export; reflection grants worker inspection separately.
- Selection predicate: enabled memory/persistence settings and turn/time/event triggers; model selects durable facts and event summaries under prompt guidance; direct save callers select their own content.
- Invalidation or expiry: forget/consolidation/pruning can change later availability; embedding failure invokes compensation for new or merged anchor state; partial association/FTS failures can be warnings.
- Activation or effect: durable writes and later supply are wired; factual correctness and behavior depending on these claims are unobserved.
- Evidence limits: deployed initial content and model adherence unknown; successful writes are not transactionally undone merely because a later branch or completion check fails.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The completion tool rejects fabricated/mismatched save-ID sets and requires a reason for no-save. Events are emitted only after that validation. This is an accounting gate, not semantic evaluation (SRC-1, `src/tools/memory_persistence_complete.rs`, `src/hooks/spacebot.rs`).

> if provided_set != recorded_set {
>     return Err(MemoryPersistenceCompleteError(format!(
>         "saved_memory_ids mismatch: expected {:?}, got {:?}",
>         recorded_ids, provided_ids
>     )));
> }
> --- `src/tools/memory_persistence_complete.rs`

#### MEM-RTE-file-ingestion
Label: File ingestion to memories

Endpoints/progression: file dropped/uploaded to agent ingest directory → periodic scan/read/hash/chunk → fresh branch-profile model per chunk → memory tools/terminal contract → progress rows → later memory consumers. No counterpart in supplied runtime; shares admission tools with [MEM-RTE-memory-admission](#mem-rte-memory-admission) but has external file input and destructive source cleanup. API caller supplies a file; model decides extracted content; software checks completion, not semantic source trust. Initial authorship/human approval of extracted claims unresolved. Open bulk import, no answer oracle or per-claim human veto. Failed chunks remain retryable; prior successful saves are not an all-file atomic transaction (SRC-1, `src/agent/ingestion.rs`, `src/api/ingest.rs`).

- Immediate return: API upload acknowledgement and ingestion status/progress; each chunk must report a terminal outcome.
- Later read-back: extracted typed memories/indexes reach recall/render; progress rows skip completed chunks after restart.
- Delegated visibility: each chunk gets fresh empty history with shared retained-memory tools; no chunk-to-chunk live transcript propagation.
- Selection predicate: scan of ingest directory, line-boundary chunking at configured size, SHA-256 content hash and completed-chunk indices; model chooses what to keep.
- Invalidation or expiry: successful file completion deletes progress and original file; failed chunks keep the source; deleting API ingestion history only removes the history row, not derived memories.
- Activation or effect: writes and cleanup are wired; downstream information quality and exact replay behavior under every crash ordering are unobserved.
- Evidence limits: deleting the file/history is not lineage-based withdrawal of its derived claims; no supplied run establishes source fidelity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Full success: clean up progress rows and remove the source file.
> --- `src/agent/ingestion.rs`

> sqlx::query("DELETE FROM ingestion_files WHERE content_hash = ?")
> --- `src/api/ingest.rs`

#### MEM-RTE-memory-curation
Label: Memory revision and maintenance

Endpoints/progression: save advice/model request, periodic Cortex maintenance, association loop or enabled instance janitor → revise selectors/text/graph or withdraw rows → later selection/render/recall. Different mechanisms are explicitly separated below. No supplied route denotes this combined maintenance family; [RT-RTE-context-control](runtime.md#rt-rte-context-control) manages invocation windows, not this store. Open maintenance, no semantic answer oracle or required human approval. Model merges propose text; code thresholds propose similarity edges/maintenance merges. Structural checks can refuse requests; these do not certify knowledge (SRC-1, `src/memory/consolidation.rs`, `src/memory/maintenance.rs`, `src/memory/store.rs`, `src/agent/cortex.rs`, `src/agent/maintenance.rs`, `src/tools/memory_delete.rs`).

- Immediate return: advisory debt/near-duplicate previews, consolidation counts, forget result, maintenance report or warnings.
- Later read-back: survivor content and rank/graph changes shape later search/render; forgotten rows remain provenance but not ordinary recalled content.
- Delegated visibility: branches compose explicit consolidation batches; janitor and maintenance are programmatic, not delegated semantic critics.
- Selection predicate: type partitions/near-duplicate thresholds, age/access/importance, configured merge thresholds, incremental association update times or full backfill.
- Invalidation or expiry: tool forgetting sets a flag; pruning physically deletes old low-importance non-identity rows; merge preserves an absorbed forgotten row and Updates edge; index updates have their own failure paths.
- Activation or effect: selectors/content can change future delivery; actual beneficial selection and correction of false claims are unobserved.
- Evidence limits: not a globally atomic SQLite-plus-Lance transaction; no complete derivative invalidation or erasure guarantee; concurrent/failure deployment behavior unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/curation mechanisms:

- **Save association:** model supplies relation/weight; target existence is checked; invalid relation falls back to RelatedTo. An `updates` edge alone does not forget the older row or adjudicate which claim is true (`src/tools/memory_save.rs`).
- **Write-time consolidation:** save lands before advice. Branch supplies survivor/absorbed IDs and merged content; code validates partitions and nonempty text, serializes per partition and commits all SQL merges together. It rewires graph edges, marks absorbed rows forgotten, retains an Updates edge and optional covering-checkpoint provenance. Survivor re-embedding and absorbed-vector deletion happen after commit and can warn/fail. SQL rollback does not imply a cross-store atomic rollback (`src/memory/consolidation.rs`, `src/memory/store.rs`).
- **Periodic merge:** code chooses higher-importance survivor (ID tie-break), concatenates noncontained text with a byte cap, then re-embeds; this is not semantic synthesis. Decay uses age/access, skips identity and changes importance; pruning hard-deletes old below-threshold non-identity rows. A janitor can run the same routines even for dormant agents, but is opt-in (`src/memory/maintenance.rs`, `src/agent/maintenance.rs`).
- **Association pass:** similarity threshold chooses RelatedTo versus Updates and a weight; semantic entailment, temporal succession and contradiction are not tested (`src/agent/cortex.rs`).
- **Forget:** model/tool caller supplies ID/reason; store sets forgotten. Reason appears in result/tracing, not a required persistent argument attached to every descendant. Ordinary search joins filter the flag. Already-delivered copies and separately derived artifacts are not recalled retroactively (`src/tools/memory_delete.rs`, `src/memory/search.rs`).

> // Write-time consolidation check. Advisory: the save has already
> // landed; the advice tells the branch about near-duplicates and
> // per-partition over-cap debt so it can run one atomic batch.
> --- `src/tools/memory_save.rs`

> let relation_type = if similarity >= updates_threshold {
>     RelationType::Updates
> } else {
>     RelationType::RelatedTo
> };
> --- `src/agent/cortex.rs`

#### MEM-RTE-memory-recall
Label: Explicit memory and transcript recall

Endpoints/progression: model/tool request → hybrid or metadata selector → current SQLite content/labels → bounded tool result → requesting branch/worker/direct model; ordinary branch conclusion may later reach channel. Alternate API/CLI request → list/search → operator display. Distinct from [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work): this specifies its memory selection, not work execution. Runtime grants and request parameters choose scope; no claim-admission oracle. SRC-1, `src/tools/memory_recall.rs`, `src/memory/search.rs`, `src/tools/channel_recall.rs`, `src/tools.rs`, `src/cli/memory.rs`, `src/api/memories.rs`.

- Immediate return: memories with content/type/importance/score/date and optional provenance labels; checkpoint hits carry title/sequence/channel; cross-channel tool returns a formatted text transcript or channel list.
- Later read-back: accumulated store/log data enters a later requesting invocation; requested delivery is not unsolicited push. Returned IDs/labels require another explicit tool to recover more.
- Delegated visibility: standard channel delegates raw memory search to a branch; direct/autonomy/cortex-chat and configured workers may recall themselves. Cross-channel transcript remains branch-mediated where registered.
- Selection predicate: hybrid query embeds text, retrieves Lance FTS/vector candidates and keyword-matched high-importance graph seeds, fuses ranks and applies type/min-score/caps; metadata modes select recent/important/typed rows without query embedding. Channel recall resolves channel name and clamps transcript count.
- Invalidation or expiry: SQL resolution rejects missing/forgotten memories; tool result budgets can omit material; access recording updates future access-dependent selection/decay; content/index revisions change later matches.
- Activation or effect: content is supplied as tool output, not enforced truth or required instruction; no exercised dependence or recall quality observed.
- Evidence limits: tool schema advertises human filtering but parser lacks a human match arm; checkpoint search does not itself expand content; stale survivor vectors may alter candidate selection even when SQL supplies current text.
- implementation conclusion status: wired
- operation conclusion status: uninspected

FTS failure can fall back to other sources; failure to embed the query still propagates before vector/graph completion, so this is not an unconditional embedding-free hybrid fallback. The final curation is ranked truncation, not a second LLM critic. API/CLI human-readable tables shorten text; JSON can preserve more. Storage getters alone are not additional exercised read-back routes.

> let query_embedding = self.embedding_model.embed_one(query).await?;
> --- `src/memory/search.rs`

#### MEM-RTE-context-supply
Label: Automatic memory context supply

Endpoints/progression: later channel prompt build → code reads store/tasks/working state/participants → fixed renderers and budgets → preamble → channel model. This is the memory supply inside [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn), not a replacement execution route. SRC-1, `src/agent/channel.rs`, `src/memory/render.rs`, `src/memory/working.rs`.

- Immediate return: rendered knowledge, temporal/activity and participant blocks; memory Off returns no such layers.
- Later read-back: previously stored claims/summaries/events/anchors enter subsequent model invocations without a foreground recall request.
- Delegated visibility: branch forks can inherit current history while their own preamble/grants differ; automatic foreground rendering is not proof every worker receives all layers.
- Selection predicate: fixed Fact/Decision/Preference/Goal/Observation section order, scaled per-type entry caps, importance/updated-time order, first nonempty content line and word budget; task statuses are appended separately. Working renderer allocates today/yesterday/week shares; participant renderer resolves present human keys and token budget.
- Invalidation or expiry: writes/forget/prune change subsequent store queries; summaries age out of rendered windows; session anchor cache can delay both positive and negative refresh; memory-Off and render errors suppress layers.
- Activation or effect: natural-language evidence/context in a system-prompt channel, not a fixed behavioral rule; task status is separately consumed by symbolic execution gates.
- Evidence limits: memory word budget does not cap task block or whole request; first-line text omits multiline reasons and provenance; no proof of model reliance or adequate context fit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> /// `max_words` caps the memory sections; the Active Tasks section always
> /// renders regardless — task-awareness is a standing signal, and an empty
> /// board is itself information. Shown-of-total counts report what was
> --- `src/memory/render.rs`

#### MEM-RTE-temporal-synthesis
Label: Event synthesis to later temporal context

Endpoints/progression: runtime/model events → working-memory SQL rows → Cortex count/time-triggered intraday summarizer → stored narratives → yesterday synthesis plus uncovered event tail → later budgeted channel context. Distinct from [RT-RTE-context-control](runtime.md#rt-rte-context-control): these are agent-wide situational narratives, not live history replacement. Runtime selects spans and triggers; model writes prose; successful output is saved without semantic comparison or per-summary human approval. Open ongoing maintenance; no answer oracle (SRC-1, `src/agent/cortex.rs`, `src/memory/working.rs`).

- Immediate return: saved synthesis/count logs or failure/backoff; empty yesterday can become “No activity.”
- Later read-back: later channel prompts render today's intraday summaries and event tail, yesterday summary and earlier daily summaries; synthesis also feeds subsequent daily synthesis.
- Delegated visibility: a short summarizer call receives event summaries with types/time/channel, not complete raw tool payloads; no tools are offered for fact-checking in this synthesis call.
- Selection predicate: unsynthesized events after latest synthesis range; count OR elapsed-time trigger; yesterday daily-existence check; rendering uses 60/20/20 percent token shares and importance-limited tail.
- Invalidation or expiry: old raw events are pruned by configured retention; a daily summary is not regenerated once present by this routine; render windows omit older material without deleting summaries.
- Activation or effect: trace-fed derived text reaches later invocation context; useful retention, accurate reasons and improved future capacity remain unobserved.
- Evidence limits: event recording is asynchronous; retained summaries are lossy derived text, not proof that every event or argument survived; active Cortex scheduling is configuration-dependent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Use a short one-shot LLM call — no tools, no hooks.
> --- `src/agent/cortex.rs`

The comment is a local description: the builder in this body does attach `CortexHook`; it has no tool server and is not the persistence hook's save-ID contract. This is not evidence that synthesis is entirely hook-free.

#### MEM-RTE-chronicle-retention
Label: Chronicle retention and recovery

Part of: [RT-RTE-context-control](runtime.md#rt-rte-context-control)

Endpoints/progression: interval/pressure or bootstrap/emergency condition → code selects durable span and available live tool traffic → model summary or fallback notice → durable checkpoint/optional embedding → fenced live-prefix trim and rollup → later bounded view/open/expand. This is the durable chronicle part of the supplied context-control route; rolling compactor remains separate. Code owns cuts and fences; model owns prose; no human approval or semantic answer oracle. Failed summarization can still admit an explicitly unsummarized span. Recovery is explicit access to durable messages, not automatic reconstruction of original model context (SRC-1, `src/agent/chronicle.rs`, `src/tools/chronicle.rs`, `src/agent/channel.rs`).

- Immediate return: committed checkpoint and reduced live context, or declined stale cut/failure; emergency truncation can drop unsummarized live content.
- Later read-back: every-turn chronicle view renders selected summaries or collapsed titles/ranges; tools list/open; eligible branches expand paginated durable messages; optional recall exposes checkpoint hits. Restart hydration loads text after latest level-zero boundary in chronicle mode, newest limited text in rolling mode.
- Delegated visibility: channel gets metadata/open summaries; branch constructor adds Expand capability scoped to its channel; branch can curate recovered raw text into a conclusion rather than force raw rows into channel context.
- Selection predicate: configured thresholds/request estimate, durable ranges/turn boundaries, mode-generation fence, latest checkpoint boundary, render recent/older caps and word-derived token estimator; expansion selects explicit sequence/cursor with configured limit.
- Invalidation or expiry: mode/head changes can reject stale trims; rollups mark constituent lineage; oldest view entries collapse then drop; raw durable log remains separately queryable but never contained original tool-call structures.
- Activation or effect: replacement context and future supply are wired; semantic preservation and use of recovered evidence unobserved.
- Evidence limits: no exact full-window recovery guarantee; rolling summaries need not persist; minimum view floor can exceed a tiny configured budget; no observed restart/failure trial.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "chronicle view floor exceeds its budget; rendering the header and one entry"
> --- `src/agent/chronicle.rs`

This source-supported floor prevents elevating the renderer's “upper bound” comments to an unconditional hard-budget guarantee.

#### MEM-RTE-wiki-editing
Label: Wiki editing and later retrieval

Endpoints/progression: granted model wiki tool or API/CLI caller → page create/edit → SQLite page and version history → later list/search/read/history → model/operator. No supplied counterpart after comparison with filesystem [RT-RTE-skill-change](runtime.md#rt-rte-skill-change). Model or administrative caller proposes content; store performs structural/type/slug/replacement checks, not truth validation. API caller identity does not establish human content approval. Open knowledge authoring; no expected-answer oracle. SRC-1, `src/wiki/store.rs`, `src/tools/wiki_read.rs`, `src/tools.rs`, `src/api/wiki.rs`, `src/cli/wiki.rs`.

- Immediate return: page/current version, mutation error or read/search/history result.
- Later read-back: registered branch/eligible worker wiki tools retrieve persisted content; CLI/API expose it to operators; no automatic whole-wiki injection was established.
- Delegated visibility: tool registration depends on wiki store/profile/worker wiki-write configuration; read resolves linked titles but not linked page bodies.
- Selection predicate: explicit slug/version read, type-filtered list, FTS title/content query and history limit; a page ID alone is not semantic targeting.
- Invalidation or expiry: archive removes discovery from list/search; explicit slug read does not check archived in the inspected store; restore copies historical content into a new version rather than undoing version history.
- Activation or effect: supplied prose can inform model decisions; neither adherence nor correctness/improvement observed.
- Evidence limits: create uses a transaction for page plus first version; edit updates page then inserts history separately, so failure need not imply complete rollback. No inferred derivative retraction in memories/skills/summaries.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> /// List all pages, optionally filtered by type. Excludes archived pages.
> --- `src/wiki/store.rs`

> self.load_by_slug(slug).await
> --- `src/wiki/store.rs:558-558`

### Claims

#### MEM-CLM-retention-contract
Label: Retention contracts do not establish truth

Claimed operation: persistence instructions ask recall-first, selective saves and correction of stale material, while code checks valid writes and terminal accounting. An Updates association or successful terminal signal does not itself establish semantic supersession or improved memory. The prompt's claim of “full conversation history” is limited by the actual current-history clone: compaction, hydration and isolation have already selected what is live. This qualifies doctrine without correcting a false runtime fact. SRC-1, `prompts/en/memory_persistence.md.j2`, `src/agent/channel_dispatch.rs`, `src/agent/channel.rs`; [RT-RTE-context-control](runtime.md#rt-rte-context-control), [MEM-RTE-memory-admission](#mem-rte-memory-admission).

> You are a memory persistence process. You have the channel's full conversation history. Your job is to extract and preserve important information as memories.
> --- `prompts/en/memory_persistence.md.j2`

> Verify stale memory before relying on it. If a recalled memory conflicts with
> the newer conversation context, treat the older item as stale, avoid propagating
> it as truth, and capture the latest truth via `updates` or `contradicts`.
> --- `prompts/en/memory_persistence.md.j2`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-context
Label: Retained knowledge to model context

Consumer: later channel/branch/worker models with relevant grants. Channel: automatic system-prompt rendering and requested tool output, sometimes transformed once more into a branch conclusion. Force: natural-language evidence and contextual guidance interpreted by the model, not a truth-enforcing code rule. Horizon: later invocations within a session and, for SQL/filesystem state, later sessions while discoverable. Distinct from [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction): this concerns claims/temporal evidence/wiki rather than task procedures. Update consumers (extractor, summarizer, merger) and downstream work consumers are separate; preserving a claim or source label does not prove actual use (SRC-1, `src/agent/channel.rs`, `src/memory/render.rs`, `src/memory/working.rs`, `src/tools/memory_recall.rs`, `src/tools/wiki_read.rs`).

> content: result.memory.content.clone(),
> --- `src/tools/memory_recall.rs`

#### MEM-BAP-memory-selectors
Label: Retained selectors to context selection

Consumer: Rust query/render/maintenance routines. Channel: SQL metadata, typed graph and numerical index lookup. Force: fixed sorting/filtering/scoring rules determine later candidates and displays; memory contents are subsequently interpreted by a model. Horizon: later reads and maintenance passes while metadata/index rows remain. No supplied counterpart: [RT-BAP-runtime-config](runtime.md#rt-bap-runtime-config) controls machinery settings, not use-derived claim access counts/importance/forget state. SRC-1, `src/memory/search.rs`, `src/memory/store.rs`, `src/memory/maintenance.rs`, `src/memory/render.rs`.

> WHERE importance >= ? AND forgotten = 0
> --- `src/memory/store.rs`

## Annotations

#### On [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history)

The durable conversation log is not a serialized copy of this live container: hydration reconstructs assistant/user text from rows; tool calls/results in a former live window are not recovered by that path. Rolling summaries can shape later invocations in the same process without being checkpoint-persistent across restart. Chronicle summaries have their own durable store. SRC-1, `src/agent/channel.rs`, `src/agent/chronicle.rs`; passages in [MEM-OBJ-conversation-log](#mem-obj-conversation-log), [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention) and supplied [RT-RTE-context-control](runtime.md#rt-rte-context-control).

#### On [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set)

Procedure body and support files are durable authored instructions; index descriptions, read-before-edit state, usage and provenance are access/admission metadata rather than the same knowledge. The trace-fed reflection route can turn channel/worker records into later procedures. Retained rationale is content-dependent: there is no demonstrated generated skill or criticism here. Full required bodies and bounded requested reads differ from merely listing skill names. External installation and generic file/shell operations prevent interpreting agent-origin protection as universal curation. Evidence and passages: [RT-RTE-skill-change](runtime.md#rt-rte-skill-change), [RT-CLM-required-skills](runtime.md#rt-clm-required-skills), [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction); direct doctrine SRC-1, `prompts/en/memory_persistence.md.j2`.

#### On [RT-RTE-skill-change](runtime.md#rt-rte-skill-change)

Trace origin is mixed: user conversation and corrections, agent actions and worker transcripts/outcomes. The reflection prompt explicitly distinguishes successful recovery evidence from unresolved/transient failures, asks no-write abstention, and prioritizes patching an existing task-class procedure. This is a requested semantic filter, not a behavioral oracle. Retrospective transcripts influence a writer; retained procedure bodies later guide different work consumers. Source passages already retained in this supplied record support that chain; direct prompt inspection at SRC-1, `prompts/en/memory_persistence.md.j2` confirms it. No additional theory-builder or successful-learning claim is made.

#### On [RT-RTE-context-control](runtime.md#rt-rte-context-control)

Memory-specific separation: rolling summary in live history, durable chronicle summaries, unsummarized checkpoint notices and emergency discarded-span markers are different retained forms. Branch/worker isolation keeps private tool traffic out of the parent; only conclusions/results escape. Clean and precompacted forked workers are different selection paths. Removed raw text may remain reachable through explicit durable-log tools, but pointers do not carry original tool payloads back into the window. This fits the private-frame analogy; it does not create followable heap references. Supplied passages support rolling/isolation behavior; direct SRC-1, `src/agent/chronicle.rs`, `src/tools/chronicle.rs`, `src/agent/channel.rs` refine durable recovery in [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention).

#### On [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work)

Worker outcomes/transcripts are retained raw operational records, not automatically curated lessons. Restoration can use prior serialized transcript; later reflection explicitly requests worker inspection to derive procedures. Completion summaries and transcript bodies are not equivalent evidence. Supplied runtime establishes the storage/resume path; direct reflection doctrine at SRC-1, `prompts/en/memory_persistence.md.j2` requests transcript inspection. Actual extraction/reuse remains unobserved.

## Write side

The principal write chains and their distinct gates are [MEM-RTE-memory-admission](#mem-rte-memory-admission), [MEM-RTE-file-ingestion](#mem-rte-file-ingestion), [MEM-RTE-memory-curation](#mem-rte-memory-curation), [MEM-RTE-temporal-synthesis](#mem-rte-temporal-synthesis), [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention), [MEM-RTE-wiki-editing](#mem-rte-wiki-editing) and [RT-RTE-skill-change](runtime.md#rt-rte-skill-change). They must not inherit one another's guarantees.

| Mechanism | Semantic proposer / human decision | Software admission and what persists |
|---|---|---|
| Periodic extraction | Model reads selected conversation; no required human approval per memory | Tool validation and embedding compensation; successful-save accounting; claim text, metadata, optional graph links/events. Completion does not certify truth. |
| Direct/worker save | Granted caller/model selects bytes; caller role is not exact-content human approval | Same save handler where used, but event/contract/context wiring varies by constructor. |
| Uploaded/file import | File supplier's authorship unknown; model extracts | Chunk completion and shared persistence tools; successful-file source deletion. No all-file semantic acceptance. |
| Human anchor write | Model observations append; startup config supplies another lineage | Human key requirement/anchor lock/size and embedding pipeline; mapping/cache differs from content. Full org-edit propagation unresolved. |
| Consolidation/forget | Model composes replacement or selects ID; no semantic veto oracle | Partition/SQL checks and flag changes; absorbed row/provenance edge can survive; post-commit index maintenance may fail. |
| Periodic merge/decay/prune/association | Code thresholds, not human or model content criticism | Importance changes, concatenated text, forgotten/deleted rows or similarity relations. Counts and labels are not epistemic warrants. |
| Temporal synthesis | Model summarizes events and prior summaries | Saves successful output; scheduling/backoff and daily-existence checks; no required reason-preservation field. |
| Chronicle cuts/rollup | Model summary or code fallback; code controls ranges and trims | Durable coverage/checkpoint records and optional vectors; notices/markers may replace semantic text; recovery limited by raw-log contents. |
| Procedure reflection/install/edit | Supplied runtime distinguishes model reflection, User origin, external sources and API/file/shell | Procedure files reload; origin/pin/read rails are local. No per-procedure correctness test. |
| Wiki write/restore/archive | Model or caller edits; human content control unresolved for generic API identity | Versions and optional edit summaries; replacement/type checks, not semantic review. Restore is a new version; archive is discovery-local. |
| Identity/configuration | Preset seeding, administrative/factory edits; deployed author unknown | Identity text reload/render and separate symbolic config controls; no trace-responsive beneficial identity update established. |

The table describes computational authorship separately from physical I/O: Rust writing SQLite or files does not by itself make content software-selected or human-approved. Initial content remains locally unknown even where later transformations are inspectable.

Reasons can survive in a claim, summary, skill body or wiki edit summary, but automatic first-line rendering can remove them before the next consumer. Checkpoint/Updates lineage identifies a source span or predecessor, not necessarily the argument for a revision. Nothing in the inspected generic memory type requires a retained, separately addressed criticism. This prevents treating all trace-fed updates as formulated theoretical learning. The procedure-specific conditional assessment remains the supplied [RT-RTE-skill-change](runtime.md#rt-rte-skill-change), not a system-wide inference from retention.

## Read-back

Two directions coexist. Automatic channel prompt construction selects store/temporal/participant state independently of a foreground query ([MEM-RTE-context-supply](#mem-rte-context-supply)). Explicit `memory_recall`, `channel_recall`, `chronicle` and wiki reads are requested access, with code-selected content inside the requested scope ([MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention), [MEM-RTE-wiki-editing](#mem-rte-wiki-editing)). Required skill bodies are a further instruction-supply path, unlike optional index hints ([RT-CLM-required-skills](runtime.md#rt-clm-required-skills)).

The global block excludes Identity/Event/Todo/Human types; this does not mean those rows cannot be stored or recalled. Identity instructions have their own file channel, events have a temporal spine, tasks have a board, and human anchors have participant scoping. The first-line store display and first-line cached human anchor are neither whole-body knowledge nor numerical retrieval payloads. Model use of either is unobserved (SRC-1, `src/memory/render.rs`, `src/memory/working.rs`).

Working-context control also includes reconstruction and loss. Rolling compaction retains a live summary and tail; chronicles persist summaries/coverage and trim a covered prefix; failures may leave only an explicit notice. Branches and clean/forked workers isolate context, then return selective results. Chronicle and cross-channel tools can bring durable text back, but copies and summaries are values, not references followed automatically. Removing a frame removes its private context even if external rows remain. These distinctions are established in [RT-RTE-context-control](runtime.md#rt-rte-context-control), refined by [MEM-OBJ-conversation-log](#mem-obj-conversation-log) and [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention).

## Integration issues

1. **Container and part, not duplicate:** [MEM-RTE-chronicle-retention](#mem-rte-chronicle-retention) is the durable chronicle part of [RT-RTE-context-control](runtime.md#rt-rte-context-control). Live rolling summaries remain outside that part. Other new memory objects/routes have distinct identities as stated in their declarations; none is proposed to replace a supplied referent. [MEM-RTE-context-supply](#mem-rte-context-supply) describes memory supply inside [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn), not a duplicate turn loop.
2. **Doctrine qualifications, no supplied fact correction required:** “full conversation history” in persistence doctrine means the copied current window, not all durable history ([MEM-CLM-retention-contract](#mem-clm-retention-contract)). Renderer comments about deterministic memory-only change and hard budgets have exceptions: tasks/configuration affect output and chronicle rendering has a minimum floor. The inspected source paths are `src/memory/render.rs`, `src/agent/chronicle.rs`, `src/agent/channel_dispatch.rs`. Do not inflate supplied runtime's already bounded context guarantees.
3. **Index consistency remains local:** [MEM-RTE-memory-curation](#mem-rte-memory-curation) commits SQL before re-embedding. `src/memory/consolidation.rs` says stale/orphaned embeddings are invisible, but `src/memory/search.rs` can select a surviving ID using stale vector/text indexing, then read current SQL content. Forgotten/missing payload filtering is supported; perfect current-content retrieval is not. No runtime correction is needed, but any reconciliation claim of cross-store atomicity or immediate index consistency must be rejected.
4. **Human filtering/cache:** [MEM-RTE-memory-recall](#mem-rte-memory-recall) has schema/parser disagreement at `src/tools/memory_recall.rs`: `human` appears through ALL in the advertised enum but not the parser match. Unfiltered recall/anchor-specific rendering can still work; this is not absence of human memory. Cache invalidation after writes/org edits remains unresolved at `src/memory/working.rs`, `src/agent/channel.rs`; prevents guaranteed immediate participant refresh ([MEM-OBJ-human-anchor](#mem-obj-human-anchor)).
5. **Withdrawal propagation:** [MEM-RTE-file-ingestion](#mem-rte-file-ingestion) history removal, memory forgetting, wiki archiving and skill archiving are different operations. No complete dependency-based retraction is established across summaries/skills/wiki/memory or already-copied context. Explicit wiki reads differ from archive-filtered discovery ([MEM-RTE-wiki-editing](#mem-rte-wiki-editing)). Do not translate local withdrawal to total erasure.
6. **Remaining operative detail:** attachment recall payload reconstruction; every goal/project/task revision and autonomous-wake retry path; complete org human initialization/edit propagation; debug/usage downstream consumers; all restored worker variants and external provider retention remain locally uninspected as inventoried above. These prevent complete enumeration/recovery/security guarantees, not the positive routes already traced. Generated agent profile cards have a known SQLite producer but no established later behavioral consumer in this inspection; do not classify them as an instruction feedback loop (`src/agent/cortex.rs`).
7. **Evidence quality:** no actual generated claim/procedure/criticism or downstream dependent behavior is supplied. [RT-RTE-skill-change](runtime.md#rt-rte-skill-change)'s conditional theory/self-improvement limits remain unchanged; [MEM-BAP-memory-context](#mem-bap-memory-context) and [MEM-BAP-memory-selectors](#mem-bap-memory-selectors) establish reachable authority paths, not exercised learning or beneficial self-improvement.

## Limitations and checks

The checkout HEAD and clean working-tree status were checked against the boundary revision before source analysis. Registered source identity and supplied run/frontmatter identity were kept unchanged. The report follows the supplied memory type, worker rules and record contract; no prior analyses or other worker state were consulted. The source files named above are additional coverage of SRC-1, not additional sources.

This is source-grounded architecture, with prompt doctrine and evaluator definitions kept separate. No execution evidence supports extraction fidelity, successful retention under crashes, recall precision, semantic conflict resolution, model obedience, reliable withdrawal propagation or improved task performance. “Uninspected” in the inventory means available detail or excluded dependency internals were not established, not that a feature is absent. Source definitions and validation cannot establish activation or benefit.

The required `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The check does not establish semantic acceptance or runtime behavior.
