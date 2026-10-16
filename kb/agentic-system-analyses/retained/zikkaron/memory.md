---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Zikkaron memory: heterogeneous SQLite retention, trace-derived transformations, independent context consumers and incomplete withdrawal."
run-id: AAS-2026-10-15-zikkaron-0102ec63c6e5-01
source-identity: https://github.com/amanhij/zikkaron
reviewed-boundary: dda34a5d903d04ecb5517af214d437873c833302
---

# Zikkaron memory report

## Boundary and evidence

This report covers retained content and context selection in Zikkaron's whole-system boundary. SRC-1 is the repository and revision registered in [boundary](boundary.md#source-register). Direct inspection extends the supplied runtime account into curation, reconsolidation, compression, dual-store abstraction, sleep processing, profiles, prospective triggers, narratives, domain consolidation, sensory episodes, CRDT synchronization and hierarchical retrieval. These are implementation findings; comments and docstrings supply separately identified design claims. No target code, tests, models or hooks were run. HEAD matched the registered commit and tracked status was clean at inspection.

Excluded external implementations remain those in the boundary: the host window and event processing, model/dependency internals, project files, datasets and provider responses. Therefore delivery wiring is assessable, but successful delivery, truth, exercised learning and benefit are not established. The following inventory distinguishes direct inspection from inherited runtime findings. Included but unresolved operations remain visible rather than being counted as absent.

| Entry point or operation | SRC-1 paths and inspection | Covering records or unresolved limit |
|---|---|---|
| MCP remember and recall | `zikkaron/server.py`, `zikkaron/curation.py`, `zikkaron/reconsolidation.py` directly read; gate/ranking also supplied runtime | [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [MEM-RTE-curation-write](#mem-rte-curation-write), [MEM-RTE-recall-revision](#mem-rte-recall-revision) |
| CLI, HTTP and PostToolUse capture | Dispatch/hook passages supplied runtime; `zikkaron/sensory_buffer.py`, `zikkaron/consolidation.py` directly read | [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation), [MEM-OBJ-episodes](#mem-obj-episodes), [MEM-RTE-maintenance-cycle](#mem-rte-maintenance-cycle) |
| Idle/forced consolidation and extended-idle sleep | `zikkaron/consolidation.py`, `zikkaron/curation.py`, `zikkaron/cls_store.py`, `zikkaron/astrocyte_pool.py`, `zikkaron/sleep_compute.py` directly read | [MEM-RTE-maintenance-cycle](#mem-rte-maintenance-cycle); graph causal discovery and community partition correctness not fully inspected, preventing validation of causal/cluster semantics |
| Compression and alternative checkpoint forms | `zikkaron/compression.py`, `zikkaron/sleep_compute.py`, `zikkaron/restoration.py` directly read | [MEM-RTE-compression-write](#mem-rte-compression-write), [RT-RTE-replay-context](runtime.md#rt-rte-replay-context); compression archive access is a library capability, not a demonstrated host reload route |
| Hook push context and restoration | Hooks and CLI supplied runtime; service/project and replay portions directly read | [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [RT-RTE-replay-context](runtime.md#rt-rte-replay-context); selectors differ, host injection unobserved |
| Project context, hot/stale resources | `zikkaron/server.py` project-context passage directly read; resources inventoried by decorators/search | [MEM-RTE-project-context](#mem-rte-project-context); exact resource formatting uninspected, preventing an equivalent-budget claim |
| Seed and evaluator ingestion/QA | `zikkaron/seed.py`, benchmark paths supplied runtime; insertion implementation directly read | [RT-RTE-seed-admission](runtime.md#rt-rte-seed-admission), [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode), [MEM-OBJ-index-enrichment](#mem-obj-index-enrichment) |
| Profile extraction and belief operations | `zikkaron/storage.py`, `zikkaron/profiles.py`, `zikkaron/retrieval.py` directly read and callers searched | [MEM-OBJ-user-profiles](#mem-obj-user-profiles), [MEM-OBJ-derived-beliefs](#mem-obj-derived-beliefs); ordinary production belief-writer wiring not found in bounded search, not a system-wide absence |
| Trigger creation and firing; narrative story/resource | `zikkaron/prospective.py`, `zikkaron/narrative.py`, `zikkaron/server.py` directly read | [MEM-RTE-trigger-delivery](#mem-rte-trigger-delivery), [MEM-RTE-narrative-story](#mem-rte-narrative-story) |
| Hierarchy and navigation | `zikkaron/fractal.py`, service wrappers directly read; cognitive-map navigation supplied runtime | [MEM-RTE-hierarchy-read](#mem-rte-hierarchy-read), [RT-CMP-cognitive-map](runtime.md#rt-cmp-cognitive-map); full causal-chain and gap-assessment algorithms uninspected, preventing completeness/correctness conclusions |
| Rules, installation and fixed model inference | Supplied runtime; service surfaces cross-checked by search | [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [RT-RTE-install-integration](runtime.md#rt-rte-install-integration); installed prose is static policy, not use-derived memory |
| CRDT library sync/conflict resolution | `zikkaron/crdt_sync.py` merge/sync directly read, callers searched | [MEM-RTE-sync-import](#mem-rte-sync-import); transport, deployed peers and full resolution branch uninspected |
| Forget, prune, staleness, ratings | `zikkaron/storage.py`, `zikkaron/server.py`, `zikkaron/curation.py` directly read; `zikkaron/staleness.py`, `zikkaron/thermodynamics.py` mutation sites searched | [MEM-RTE-withdrawal-path](#mem-rte-withdrawal-path); watcher/hash and rating formulas not fully inspected, preventing comprehensive invalidation guarantees |

## Core ideas

1. **The database holds distinct operative parts, not one undifferentiated memory.** Human/model-readable text, dense embeddings and symbolic access/provenance/control fields have different consumers. Raw tool actions and sensory episodes differ from automatic activity summaries, recurring-pattern text and generated connections. Their existence does not establish reliable knowledge. See [MEM-OBJ-memories](#mem-obj-memories), [MEM-OBJ-selection-state](#mem-obj-selection-state) and [MEM-OBJ-episodes](#mem-obj-episodes).
2. **Read-back also writes.** Service recall records access and transition state and can append the query to retained content or create a new query-memory. Background processing turns retained traces into graph state and synthetic text. These are durable behavior-shaping pathways, but not evidence of improved capacity. See [MEM-RTE-recall-revision](#mem-rte-recall-revision) and [MEM-RTE-maintenance-cycle](#mem-rte-maintenance-cycle).
3. **Context selection is plural.** Service ranking/rules/packing, prompt SQL/vector retrieval, session SQL, replay, project-context lookup, hierarchy and story output are distinct selectors. Rules and budgets at one consumer do not constrain all others. Text crosses to the external host by value; Zikkaron does not own window eviction. See [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) and [MEM-RTE-project-context](#mem-rte-project-context).
4. **Retention and recoverability depend on the transformation.** Rate-distortion compression keeps archives; sleep compression overwrites without doing that locally. A micro-checkpoint retains only a shortened task label; drain can retain merely a placeholder/epoch. Forget deletes the primary row and selected dependents, not every separately derived artifact. See [MEM-RTE-compression-write](#mem-rte-compression-write), [MEM-RTE-withdrawal-path](#mem-rte-withdrawal-path) and [RT-RTE-replay-context](runtime.md#rt-rte-replay-context).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memories
Label: memories content

Natural-language `memories.content` in SQLite, with tags and directory labels stored separately. Inputs include caller-written facts, seeds, action summaries and automatically derived text; authorship is not determined by the storage API. Dense embeddings are a distinct part described by [RT-CMP-embedding-engine](runtime.md#rt-cmp-embedding-engine), not prose or an inspectable rationale. The closest supplied route is [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall), which describes operations, not this persistent text object. SRC-1, `zikkaron/storage.py`, `zikkaron/curation.py`, `zikkaron/cls_store.py`.

> "INSERT INTO memories(content, embedding, tags, source_episode_id, "
> "directory_context, created_at, last_accessed, heat, is_stale, file_hash, "
> "embedding_model) "
> --- `zikkaron/storage.py`

Later service/hook/replay consumers interpret or deliver current content. Content may already be merged, compressed or synthetically generated. IDs provide addressability of rows, not fine-grained source warrants. Its downstream model authority is informational, not enforced belief, as [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) establishes.

#### MEM-OBJ-selection-state
Label: Memory selection metadata

Symbolic, fixed-consumer SQLite fields and tables: heat, confidence, importance, usefulness/access counts, staleness, protection, store type, graph IDs/weights, temporal slot membership, transitions, vector clocks and checkpoints' active/epoch fields. Floating-point scores with named fixed rules are symbolic metadata here; dense HDC/SR/pattern matrices have the separate distributed encodings recorded in [RT-CMP-hdc-encoder](runtime.md#rt-cmp-hdc-encoder), [RT-CMP-cognitive-map](runtime.md#rt-cmp-cognitive-map) and [RT-CMP-hopfield-memory](runtime.md#rt-cmp-hopfield-memory). Unlike [RT-OBJ-memory-rules](runtime.md#rt-obj-memory-rules), these are retained observations/control state, not caller-authored condition/action policies. SRC-1, `zikkaron/engram.py`, `zikkaron/curation.py`, `zikkaron/storage.py`.

> "UPDATE memories SET excitability = ?, last_excitability_update = ? WHERE id = ?",
> --- `zikkaron/engram.py`

Engram allocation selects a highest-decayed-excitability slot, boosts it and inhibits neighbors; same-slot memory IDs subsequently enrich retrieval. Access metadata also feeds memify strengthening and decay. Neither confidence nor protection verifies source truth. Actual consumers impose selection authority inside code, distinct from host-model interpretation of returned text.

#### MEM-OBJ-episodes
Label: episodes and action traces

SQLite episodes retain sensory-buffer text, timestamps, session/directory and overlap positions. The RAM buffer and 200-entry deque precede persistence; rotation retains a suffix overlap and shutdown flushes remaining text. Action-stream entries become formatted sensory text, whereas host/HTTP/CLI action-log rows form another trace path. These are selected/truncated traces, not a complete conversation transcript. Part of the broader trace-processing route, not another declaration of its progression:

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

Containment is object-in-route: this record isolates the raw input artifact. SRC-1, `zikkaron/sensory_buffer.py`, `zikkaron/consolidation.py`.

> action_text = f"[ACTION:{tool}] {result_type}: {summary[:150]}"
> self.capture(action_text, directory)
> --- `zikkaron/sensory_buffer.py`

Consolidation reads episodes into entities and relationships; action logs additionally produce activity-summary memories and can be read raw by session-start, per the parent route. Those are different later consumers. Directory/session fields are lineage labels rather than authenticated principals.

#### MEM-OBJ-memory-archives
Label: memory_archives

Natural-language old content and dense prior embeddings plus symbolic original-memory ID, reason, timestamp and mismatch score, stored in SQLite. Compression archives full content/gist; reconsolidation's archive branch stores old content. Unlike a checkpoint in [RT-RTE-replay-context](runtime.md#rt-rte-replay-context), this is version history of one row, not selected working state. SRC-1, `zikkaron/compression.py`, `zikkaron/reconsolidation.py`, `zikkaron/storage.py`.

> earliest = archives[-1]
> return earliest["content"]
> --- `zikkaron/compression.py`

`decompress` can return the earliest archive, with `original_content` fallback. Bounded caller search in `zikkaron/` and `benchmarks/` found test calls but no shipped service/hook invocation of this method. This establishes recoverable storage capability, not an automatic host reader of archived reasons. Forget deletes these archives with the primary memory.

#### MEM-OBJ-index-enrichment
Label: Index enrichment payloads

SQLite fields retain concept lists, COMET inferences, synthetic queries, logic expansions, enriched content and model-version labels. Natural-language inferred text and symbolic lists/version metadata are distinguished from the derived dense embedding. Closest supplied records [RT-CMP-comet-inferencer](runtime.md#rt-cmp-comet-inferencer) and [RT-CMP-doc2-query](runtime.md#rt-cmp-doc2-query) are producers, not these persisted products. SRC-1, `zikkaron/storage.py`.

> "enrichment_comet": json.dumps(result.comet_inferences) if result.comet_inferences else None,
> "enrichment_queries": json.dumps(result.queries) if result.queries else None,
> --- `zikkaron/storage.py`

Insertion conditionally enables this transformation only with settings, suitable content and embedding engine/vector. Software admits outputs without per-item human approval. Enriched content can generate a replacement embedding, while FTS keeps original-content indexing apart from identifier splitting. A consequential limitation: final `insert_vector(memory_id, embedding)` uses the original local variable, while the row embedding may have been replaced by enriched encoding. Thus identical row/vector-index representations cannot be assumed. No ordinary host reader of the complete enrichment rationale is established; model labels are not immutable weight provenance.

#### MEM-OBJ-user-profiles
Label: user_profiles

SQLite symbolic entity/attribute keys, confidence and evidence-memory-ID lists accompany natural-language attribute values. Regex extraction from inserted content writes profiles only when caller-supplied settings enable it. SRC-1, `zikkaron/profiles.py`, `zikkaron/storage.py`, `zikkaron/retrieval.py`. These are material output parts of [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), not duplicates of its selector:

Part of: [RT-RTE-context-selection](runtime.md#rt-rte-context-selection)

> "content": f"{p['entity_name']}: {p['attribute_type']} = {p['attribute_value']}",
> "_source": "profile",
> --- `zikkaron/retrieval.py`

The retrieval display omits evidence IDs, confidence and attribute key while giving a synthetic negative ID. Thus retained lineage is not necessarily supplied to the host. The search helper accepts directory but does not pass it into profile FTS. Knowledge availability is conditional on extraction flag and caller wiring, not universal to all insertions.

#### MEM-OBJ-derived-beliefs
Label: derived_beliefs

SQLite natural-language beliefs with symbolic subject/type, confidence, directory and evidence IDs. Library methods derive preferences/traits from text or accumulated profiles. Retrieval can deliver belief text with confidence-based scores and negative-offset IDs. Distinct from profiles because derivation, confidence weighting and read-out differ; part of the supplied retrieval container:

Part of: [RT-RTE-context-selection](runtime.md#rt-rte-context-selection)

SRC-1, `zikkaron/profiles.py`, `zikkaron/storage.py`, `zikkaron/retrieval.py`.

> belief_content = f"enjoys {label} (evidence: {', '.join(activities)})"
> --- `zikkaron/profiles.py`

Some text contains an evidence summary, but selection omits the stored evidence-ID list and subject field from its content. Bounded caller search across `zikkaron/` and `benchmarks/` found definitions/tests, not a production caller of `derive_from_memory` or `derive_from_profiles`; therefore automatic ordinary-service belief acquisition is unestablished. Existing externally/library-populated beliefs can still be searched when enabled. This is an unresolved writer integration, not opaque model reasoning or evidence that beliefs cannot exist.

### Routes

#### MEM-RTE-curation-write
Label: Curation merge or link

Part of: [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall)

After gate admission, caller content reaches the curator. Code proposes and decides merge/link/create using vector similarity and textual overlap; the caller's human/model identity is unresolved. No expected-answer oracle or per-content human approval occurs in the inspected algorithm. This is open-request knowledge editing guided by configured similarity and fixed thresholds, not an experiment. SRC-1, `zikkaron/curation.py`.

> return jaccard > 0.5
> --- `zikkaron/curation.py`

> merged_content = existing["content"] + "\n" + new_content
> --- `zikkaron/curation.py`

- Immediate return: action and existing/new memory ID to remember.
- Later read-back: merged current content and re-encoded vectors feed later memory consumers; moderate matches retain a separate row and derived_from relation.
- Delegated visibility: inapplicable — local code owns curation, with no delegated model context.
- Selection predicate: top ten vector candidates, similarity thresholds, and Jaccard word overlap for merge.
- Invalidation or expiry: later edits, decay, compression or forget change availability; no prior-version rollback is saved by this merge body.
- Activation or effect: text, tags, heat, access time and vectors are mutated; host adoption is unobserved.
- Evidence limits: similarity/overlap do not establish factual equivalence; candidate search is not directory-scoped in this helper.
- implementation conclusion status: wired
- operation conclusion status: uninspected

No distinct pre-merge substantive veto is wired after these criteria. Failure handling can suppress vector-update errors rather than restore the whole mutation. The link is an association inferred from similarity, not necessarily a factual derivation with reasons. Contradiction detection separately reduces confidence for negation/action mismatches; its availability does not prove every insert or merge undergoes that check.

#### MEM-RTE-recall-revision
Label: Retrieval-triggered reconsolidation

Part of: [RT-RTE-context-selection](runtime.md#rt-rte-context-selection)

Service recall calls reconsolidation with selected memory ID, query and an empty directory. Code computes embedding/directory/time/tag mismatch, consults protection/stability/plasticity and decides none/update/archive. It treats query text as update material without a truth oracle or per-update human approval. Mode is automatic mutation during an open recall request. SRC-1, `zikkaron/server.py`, `zikkaron/reconsolidation.py`.

> _reconsolidation.reconsolidate(m["id"], query, "")
> --- `zikkaron/server.py`

> merged = f"{old_content}\n--- Updated context ---\n{new_context}"
> --- `zikkaron/reconsolidation.py`

- Immediate return: action/mismatch/new-content dictionary to the wrapper, which does not replace the already selected result with this dictionary.
- Later read-back: updated row content, plasticity/stability and newly inserted query-memories can affect subsequent selection.
- Delegated visibility: inapplicable — no separate generation call or agent frame performs this transformation.
- Selection predicate: protection rejects content change; weighted mismatch and stability-adjusted thresholds choose update versus archive branch.
- Invalidation or expiry: future curation/forget/maintenance changes results; update can retain only first/last 500 old characters plus query when long.
- Activation or effect: durable SQL/content/vector changes are wired; returned current recall and later DB state need not have identical text.
- Evidence limits: query is not evidence of correction; no supplied execution demonstrates useful revision or consistency across all representations.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The archive branch archives old content and inserts the query as a new memory; it does not delete or zero the old memory in this body. Therefore the action name `archive` is not proof of withdrawal. The update branch does not first call `_archive_memory`. Recovery is branch-dependent storage history, not universal version rollback. This countercase is material to claims that reconsolidation replaces obsolete knowledge.

#### MEM-RTE-maintenance-cycle
Label: Automatic retained-state consolidation

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

This isolates the parent's maintenance stage beyond action-summary production. Idle/force code owns admission and transformations; extended idle schedules sleep, subject to a six-hour interval after successful sleep. No per-derived-item human approval or answer oracle is present. Guidance is configured decay, similarity, graph/word heuristics and source-native consistency checks, not learned criticism of the method. SRC-1, `zikkaron/consolidation.py`, `zikkaron/curation.py`, `zikkaron/cls_store.py`, `zikkaron/sleep_compute.py`, `zikkaron/astrocyte_pool.py`.

> if not consistency["consistent"]:
>     stats["skipped_inconsistent"] += 1
>     continue
> --- `zikkaron/cls_store.py`

> schema = f"Recurring pattern across {n_memories} observations: {key_phrase}"
> --- `zikkaron/cls_store.py`

> content = f"Dream connection: {summary_a} may relate to {summary_b}"
> --- `zikkaron/sleep_compute.py`

- Immediate return: maintenance counters/log rows; daemon catches failures and continues later.
- Later read-back: episodes become graph entities/edges; usage counts strengthen importance and reweight relations; co-occurrence can become synthetic fact text; recurring episodes become semantic rows; sleep connections/cluster summaries and narratives feed later queries.
- Delegated visibility: inapplicable — daemon code is not a separately prompted agent; only later selected products cross to the host.
- Selection predicate: cycle-specific decay/usage thresholds; memify pair weight at least ten; CLS recurring patterns with negation-consistency and semantic-similarity duplicate veto; sleep sampled unconnected pairs with similarity thresholds.
- Invalidation or expiry: prune deletes low-heat/low-confidence never-accessed memories; duplicate handling, decay and subsequent transformations alter results; CLS preserves source episodes.
- Activation or effect: persistence and downstream retrieval wiring exist; quality improvement and actual exercise remain unobserved.
- Evidence limits: complete causal-discovery/community algorithms and all duplicate semantics uninspected; graph relation names do not validate causal truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software, including rejection of CLS clusters on negation mismatch; this heuristic is not a semantic contradiction proof. CLS abstracts common words (up to fifteen) or uses a shortest-memory fallback, inserts semantic content and derived_from links without deleting episodes. The actual retained rationale is uneven: links preserve IDs; synthetic co-modification statements and dream text retain limited summaries, not a complete argument. The dream text truncates each source to 100 characters. Memify pruning and content insertion are not undone as a whole if a later stage fails. Domain consolidation changes heat and extracts typed entities for assigned memory IDs; its name does not establish a separate generative learner. Successful capacity gain is not inferred from the source's `self-improvement` label.

#### MEM-RTE-compression-write
Label: Alternative memory compression

This route has no identical supplied counterpart: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) is its scheduler container, while [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) packs current output rather than rewriting storage. Age/heat scheduling and sleep choose text to compress. Code proposes and admits extractive representations without per-item human approval or answer oracle; mode is automatic maintenance. SRC-1, `zikkaron/compression.py`, `zikkaron/sleep_compute.py`, `zikkaron/storage.py`.

> if mem.get("is_protected", False):
>     stats["protected_skipped"] += 1
>     continue
> --- `zikkaron/compression.py`

> "UPDATE memories SET content = ?, compressed = 1 WHERE id = ?",
> --- `zikkaron/sleep_compute.py`

- Immediate return: gist/tag string or compression counts to maintenance/library caller.
- Later read-back: current row content and replacement embeddings reach recall, hooks and replay; archived originals require a separate library read.
- Delegated visibility: inapplicable — extractive code executes locally, without a summary-model frame.
- Selection predicate: rate-distortion schedule excludes protected and semantic rows; separate sleep SQL selects old, verbose, not-yet-compressed rows and retains entity-bearing sentences or first/last fallback.
- Invalidation or expiry: rewriting replaces current searchable text; rate-distortion keeps archive/original fallback, whereas sleep compression has no archive write in this method.
- Activation or effect: retained representations change; actual loss or benefit in a session unobserved.
- Evidence limits: local archive preservation is not an exercised host reload route; protection from one compressor does not establish protection from the other.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The rate-distortion route first archives original text, then gist, and advances compression level. The independent sleep route neither tests protection/store_type nor stores original text in its inspected body. Rollback thus cannot be generalized across both. Reasons omitted from the extracted current content may survive an archive only on the first route, and ordinary selectors do not automatically substitute that archive. This differs from host compaction, whose discarded window is outside Zikkaron's control.

#### MEM-RTE-project-context
Label: Direct project context

Distinct from the query-ranked [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) and event-driven [RT-RTE-hook-context](runtime.md#rt-rte-hook-context). An MCP caller requests a directory; code reads its hot rows without semantic query/rule packing. SRC-1, `zikkaron/server.py`, `zikkaron/storage.py`.

> memories = storage.get_memories_for_directory(directory, min_heat=settings.PROJECT_CONTEXT_MIN_HEAT)
> --- `zikkaron/server.py`

- Immediate return: dictionary of memories plus possible hook-install hint, with binary embedding/HDC fields removed.
- Later read-back: retained current text for the exact directory becomes task context when caller asks, as shipped instructions request.
- Delegated visibility: inapplicable — ordinary tool result to the requesting host, not child-agent execution.
- Selection predicate: directory equality and configured heat floor, ordered by heat descending.
- Invalidation or expiry: each call reselects changed rows; existing delivered text expires only under external host-window control.
- Activation or effect: response construction is wired; caller compliance with instruction to request/use it remains unobserved.
- Evidence limits: no explicit result-count or text budget in this inspected lookup; no explicit is_stale exclusion in that SQL.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-trigger-delivery
Label: Prospective trigger read-back

Distinct from general recall: retained trigger conditions are fixed-code selectors, and triggering occurs while `remember` supplies current content/directory/tags/time. Caller `create_trigger` or regex-based auto-creation proposes content; code validates trigger type and stores it. No answer oracle or per-generated-trigger human review; open requests and automatic content scanning coexist. SRC-1, `zikkaron/prospective.py`, `zikkaron/server.py`.

> triggered_memories = _prospective.check_triggers(trigger_context)
> --- `zikkaron/server.py`

- Immediate return: create ID or matching retained trigger texts attached to remember response.
- Later read-back: independently stored prospective text is supplied on a later matching remember invocation, not only when foreground model asks for recall.
- Delegated visibility: inapplicable — local matching supplies text to the same host response channel.
- Selection predicate: active trigger, trigger-type condition, target context and current time; count exceeding MAX_TRIGGER_COUNT deactivates the trigger.
- Invalidation or expiry: active-state/count changes stop future matching; deletion of an originating memory is not itself a trigger deletion in the inspected forget path.
- Activation or effect: trigger count/active state and response delivery are wired; subsequent host action unobserved.
- Evidence limits: trigger initialization is caller- or regex-derived, not proven scheduling reliability; full matching grammar not independently verified here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Persisted trigger content is natural language; condition/type/count/target-directory are symbolic policy in SQLite. Auto-creation extracts future-oriented phrases and keywords rather than storing a justification. Rejection is invalid type, no phrase/keywords or later inactive state; recovery requires caller/library edits, not a recorded approval protocol.

#### MEM-RTE-narrative-story
Label: Sleep narrative retention and story

Sleep code summarizes a directory's recent memories, decisions, events, entities and heat topics into `narrative_entries`; MCP story/resource requests later join summaries. No matching supplied declaration exists: [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) is a different consumer. Automatic software admits template-generated natural-language summaries and symbolic periods/decision/event lists in SQLite, without per-entry human approval or answer oracle. SRC-1, `zikkaron/narrative.py`, `zikkaron/sleep_compute.py`, `zikkaron/server.py`.

> return "\n\n".join(parts)
> --- `zikkaron/narrative.py`

- Immediate return: generated entry/counters to sleep; chronological story string to requesting host.
- Later read-back: at most ten selected retained entry summaries by default are combined for later project-story invocation.
- Delegated visibility: inapplicable — no independent model/agent authors the narrative in this path.
- Selection predicate: active directories and narrative interval for writes; directory and entry limit for reads, sorted chronologically after selection.
- Invalidation or expiry: later summaries accumulate; edits/forget of source memories do not automatically rewrite narrative text in these methods.
- Activation or effect: durable derived prose reaches tool/resource results; model adoption unobserved.
- Evidence limits: generated synopsis is not a full activity history or an independently checked explanation of decisions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposal guidance is the fixed summary template with capped lists. Recent narrative existence vetoes a new entry until the interval passes. No snapshot/whole-cycle undo is wired in these methods; partial failure is logged by auto_narrate.

#### MEM-RTE-hierarchy-read
Label: Hierarchical retained context

Code stores and reads cluster summaries separately from member memories. Sleep summary updates use entity/keyword counts and mean normalized embeddings; fractal retrieval selects level by caller argument or query length. MCP exposes hierarchical recall and drill_down. These are alternative consumers beyond [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), not another name for ordinary recall. SRC-1, `zikkaron/fractal.py`, `zikkaron/sleep_compute.py`, `zikkaron/server.py`.

> "summary": cl["summary"],
> "score": sim * weight,
> "member_count": cl["member_count"],
> --- `zikkaron/fractal.py`

- Immediate return: ranked memory/cluster dictionaries or requested cluster members.
- Later read-back: retained SQLite cluster natural-language summaries, symbolic membership/hierarchy and distributed centroid BLOBs guide later queries/drill-down.
- Delegated visibility: inapplicable — selected dictionaries return to the host, no separate context frame.
- Selection predicate: explicit level or query-length weighting, query/centroid similarity, bounded per-level retrieval; cluster ID targets drill-down.
- Invalidation or expiry: rebuilds/sleep updates and memory changes can alter membership/content; no universal live-summary freshness guarantee established.
- Activation or effect: code-selected summary/member delivery wired; downstream behavior unobserved.
- Evidence limits: full tree/community construction and every ordinary-retrieval fractal signal branch not verified; centroid-free clusters are skipped by inspected similarity selector.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Centroids change by recomputation from retained embeddings; there is no weight-training or mutable remote endpoint for this derived numerical object. Algorithm is revision-pinned, exact values are not: they depend on DB state and externally resolved embedding model. Summary generation admits heuristic updates automatically; underlying member access is a separate affordance, not proof that each requesting host drills down to verify them.

#### MEM-RTE-sync-import
Label: Library CRDT import

Library caller supplies remote memory dictionaries; fixed code decides insertion or clock merge. Closest supplied [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall) stamps provenance but does not establish a sync transport. SRC-1, `zikkaron/crdt_sync.py`.

> local_match = local_by_content.get(remote_content)
> --- `zikkaron/crdt_sync.py`

- Immediate return: new/merged/conflicted/unchanged counters to library caller.
- Later read-back: imported or merged current rows can be read by ordinary consumers if a caller populates them; no deployed sync caller established.
- Delegated visibility: uninspected — no remote-peer transport or deployed caller traced.
- Selection predicate: exact content matching in sync, then vector-clock relation; merge helper can combine concurrent differing text and union tags.
- Invalidation or expiry: later ordinary maintenance/forget applies; no network withdrawal or authenticated provenance contract established.
- Activation or effect: callable storage mutation capability, not evidenced production synchronization.
- Evidence limits: bounded caller search found tests rather than production sync use; content-difference merge capacity is not itself proof that exact-content sync reaches that case.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission is code after arbitrary library-caller input, without remember gate or per-item human approval; source authenticity is unresolved. The docstring's similarity language is weaker evidence than the exact-content dictionary lookup. Vector clocks and agent labels are symbolic provenance, not source trust verification. Guidance is fixed CRDT policy; recovery/rollback beyond separate conflict-resolution/library operations is uninspected, and no answer oracle or improvement objective is wired.

#### MEM-RTE-withdrawal-path
Label: Forget and retained derivative limits

Caller forget and automatic memify prune remove primary memories via storage; staleness/decay instead mark or reduce heat. These are distinct from admission rejection in [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall). SRC-1, `zikkaron/storage.py`, `zikkaron/server.py`, `zikkaron/curation.py`.

> "DELETE FROM memory_archives WHERE original_memory_id = ?",
> --- `zikkaron/storage.py`

> self._conn.execute("DELETE FROM memories WHERE id = ?", (memory_id,))
> --- `zikkaron/storage.py`

- Immediate return: deleted/not_found result for forget; prune counts for maintenance.
- Later read-back: removed primary rows cannot be selected as such, but separately retained summaries/profiles/beliefs/triggers/narratives are not all withdrawn by this function.
- Delegated visibility: inapplicable — local deletion, no delegated consumer recall cancellation.
- Selection predicate: caller ID for forget; prune requires heat below .01, confidence below .3 and zero accesses.
- Invalidation or expiry: archives/transitions/vector rows are explicitly removed; delivered host text and independently derived rows are outside this method's deletion list.
- Activation or effect: deletion is wired; system-wide erasure and already-injected context revocation are not established.
- Evidence limits: all schema cascades and downstream derivative repair not comprehensively audited; bounded conclusion is that this function supplies no explicit semantic withdrawal propagation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller controls an explicit deletion request, but per-content human involvement remains caller-dependent. Automatic pruning is a software veto of continued retention. There is no archive-backed undo after forget here because it deletes the archives too. Staleness and zero heat are not physical deletion, and selectors with different heat/stale rules can disagree. Ratings change later reliability/stability metadata rather than evaluating a gold answer. No oracle or guaranteed improvement follows.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-hook-context](runtime.md#rt-rte-hook-context)

Memory read-back is unsolicited relative to foreground tool selection: UserPromptSubmit/SessionStart events supply context even without a recall call. The supplied record retains verbatim trigger/budget/delivery evidence under SRC-1, `zikkaron/hooks/prompt-recall.py` and `zikkaron/hooks/session-start-context.py`. Selection inputs are prompt/cwd/current DB state; selected parts are formatted current memory text or checkpoint/actions/anchors, not an archive reconstruction. Top-five and content-character caps in the prompt route do not bound all session/replay output. DB-path divergence and host injection limits remain beside the parent findings.

#### On [RT-RTE-replay-context](runtime.md#rt-rte-replay-context)

Checkpoint storage mixes natural-language task, working memory, pending decisions and symbolic session/directory/epoch/active fields. Manual structured snapshots, event-derived micro-checkpoints and auto-drain placeholders are different retained products. Direct SRC-1 inspection of `zikkaron/restoration.py` shows micro-checkpoint content is only a 150-character, newline-flattened label inserted as current_task; it does not reconstruct the full source episode:

> summary = content[:150].replace("\n", " ")
> --- `zikkaron/restoration.py`

The supplied record establishes global checkpoint selection and bounded anchors/recent/hot/predicted delivery. Thus raw-to-derived-to-consumer chains include remember text → micro task label → restore, and compaction event → epoch/placeholder → restore. Drain does not acquire unrecorded conversation content. Retained reasons can survive caller-written snapshot fields, but their completeness depends on the caller; placeholder and truncated micro forms do not ensure them. Host compaction removes window material under an opaque external policy; selected DB text returns by value, not a pointer keeping the discarded frame live.

#### On [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode)

The supplied record distinguishes dataset ingestion, selected dated memory context, generation, gold-answer judging and saved reports. Its SRC-1 evidence anchors are `benchmarks/run_locomo_jscore.py`, `benchmarks/test_e_locomo.py` and `benchmarks/run_longmemeval.py`. Evaluation answers/judgments are retained results only if saved by the driver; no later production-memory or policy consumer is established. This limits the claim to an evaluation capability, not trace-fed production improvement. Alternative storage callers can enable the enrichment/profile parts described here, so benchmark DB contents cannot be assumed identical to ordinary service inserts.

## Write side

Admission mechanisms differ. Remember's predictive gate can reject before curation; curator then merges/links/inserts using code-owned criteria. Anchors, seeds, action summaries, reconsolidation inserts and optional library imports do not inherit this same gate. User tool invocation is not approval of every derived item. Explicit caller authorship remains human/model-unresolved; subsequent regex, similarity, extraction and summary transformations are computational admission. [RT-RTE-seed-admission](runtime.md#rt-rte-seed-admission) retains replacement/dry-run/recovery evidence; [MEM-RTE-curation-write](#mem-rte-curation-write) and [MEM-RTE-sync-import](#mem-rte-sync-import) isolate additional controls.

Trace-fed routes retain more than logs. Host tool actions → action_log → grouped activity memories → recall/session context is established by [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation). Service remember/recall traces → sensory episode → entities/co-occurrence → graph selection or memify-derived text is covered by [MEM-OBJ-episodes](#mem-obj-episodes) and [MEM-RTE-maintenance-cycle](#mem-rte-maintenance-cycle). Retrieval query → reconsolidated content/query-memory → subsequent selection is [MEM-RTE-recall-revision](#mem-rte-recall-revision). Access counts/heat → importance/relation updates → later ranking form another durable trace-feedback path. These chains establish automatic trace-fed update capacity, not successful learning.

Reasons survive unevenly. Explicit prose may contain reasons; raw actions often retain only truncated summaries. CLS retains source links but abstracts common words, dreams retain truncated paired text, profiles/beliefs retain evidence IDs but omit them from display, and micro-checkpoints retain short labels. Archives can preserve discarded text on one compression path without providing a host read-back route. None of these mechanisms alone supplies truth warrant. Evaluation gold answers do not automatically become production curation controls. See [MEM-RTE-compression-write](#mem-rte-compression-write), [MEM-OBJ-user-profiles](#mem-obj-user-profiles) and [MEM-OBJ-derived-beliefs](#mem-obj-derived-beliefs).

Maintenance and withdrawal have different horizons: heat/staleness modifies eligibility, pruning/forget deletes primary rows, and separate derivatives can survive. Protection is consumer-specific: reconsolidation and rate-distortion compression inspect it, whereas the independent sleep compression SQL does not. This prevents an invariant that protected content is never edited. [MEM-RTE-withdrawal-path](#mem-rte-withdrawal-path) records the explicit deletion boundary.

## Read-back

Requested delivery includes recall, project context, hierarchy/drill-down, navigation, restore and project story. Automatic supply includes host prompt/session events, prospective matches inside remember, and related-memory reinjection after remember. Selectors receive different inputs: semantic query, exact directory, explicit cluster ID, active global checkpoint, prompt terms, trigger context or recent period. Their distinct outputs and delivery channels are recorded in [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [RT-RTE-replay-context](runtime.md#rt-rte-replay-context) and this member's routes. Direct SRC-1 `zikkaron/server.py` reinjection inspection confirms a query from the first 300 content characters, heat floor .3, exclusion of the newly stored ID, configured count and per-related-content truncation to 300 characters. It returns related text to the same caller, not a separate agent.

Service packing controls current result size/content, not the host's accumulated window. Hook character budgets, replay section caps and exact-directory lookup are separate policies. No single bound applies to every channel. Rule-mediated service selection is code authority over candidate delivery; hook SQL and replay are not all governed by those rules. Model interpretation of returned natural language is weaker authority than deterministic selection. [RT-BAP-retrieval-rules](runtime.md#rt-bap-retrieval-rules) and [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) retain this distinction.

Archive decompression, belief derivation, dual-store `query_dual` and CRDT synchronization expose library capabilities whose ordinary production callers were not established by bounded search. A callable storage method does not establish a later requesting agent. Conversely, belief/profile search and hierarchical/story consumers are concrete readers when populated/enabled; an unresolved writer does not erase those readers. Static installed instructions and hooks configuration shape behavior but are not use-derived read-back.

## Integration issues

- **Refinement, not a duplicate:** [MEM-RTE-curation-write](#mem-rte-curation-write), [MEM-RTE-recall-revision](#mem-rte-recall-revision) and [MEM-RTE-maintenance-cycle](#mem-rte-maintenance-cycle) are narrower parts of supplied routes. Object-in-route containment for episodes/profiles/beliefs isolates retained artifacts rather than replacing the route. No whole supplied referent is redeclared.
- **Archive is not withdrawal:** [MEM-RTE-recall-revision](#mem-rte-recall-revision) qualifies the runtime's unresolved detailed revision semantics: the archive branch preserves old row eligibility while inserting query text; the update branch does not locally archive first. SRC-1, `zikkaron/reconsolidation.py`. Any reconciliation treating archive action as replacement must preserve this countercase.
- **Protection is path-specific:** [MEM-RTE-compression-write](#mem-rte-compression-write) shows separate sleep SQL lacks the rate-distortion protector/semantic checks. SRC-1, `zikkaron/sleep_compute.py`, `zikkaron/compression.py`. Do not generalize protected-decay/replay policy to all transformations.
- **Index representation disagreement:** [MEM-OBJ-index-enrichment](#mem-obj-index-enrichment) identifies enriched row embedding versus final original-vector insertion in SRC-1, `zikkaron/storage.py`. Correctness and actual incidence require execution evidence absent here; a uniform-vector claim is prevented statically.
- **Unresolved acquisition:** [MEM-OBJ-derived-beliefs](#mem-obj-derived-beliefs) and [MEM-RTE-sync-import](#mem-rte-sync-import) have callable producers and possible later readers, but bounded caller searches did not establish ordinary deployment wiring. Full conflict-resolution and all alternative external callers remain uninspected. These limits prevent automatic multi-agent sync or service-belief-production claims.
- **Unresolved semantic guarantees:** graph causal discovery, community/tree construction, complete staleness/rating algorithms and hot/stale resource formatting remain partly inspected, as the coverage inventory states. Their wiring does not verify causal truth, complete freshness, equivalent budgets or comprehensive withdrawal. [MEM-RTE-maintenance-cycle](#mem-rte-maintenance-cycle), [MEM-RTE-hierarchy-read](#mem-rte-hierarchy-read) and [MEM-RTE-withdrawal-path](#mem-rte-withdrawal-path) retain the affected findings.
- **Evaluation has no established production admission:** [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode) remains separate from these update routes; no supplied run or inspected production consumer closes a judgment-to-policy feedback chain.

## Limitations and checks

The analysis used frozen source text and the supplied members, not prior characterizations or target execution. Git HEAD and clean tracked status were rechecked at inspection. Added coverage is implementation evidence under SRC-1; source comments do not become observed operation. Every route's operation status remains uninspected. No benefit, successful restoration, complete erasure, project isolation, verified provenance or capacity gain is inferred.

Deterministic validation: completed with the supplied validate-output command; its passing result checks format, citation/quotation conditions and invocation identity, not semantic correctness or operational success.
