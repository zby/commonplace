---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Tortoise memory: session traces and derived graph content, bounded pointer delivery, recent-session digests and maintenance limits."
run-id: AAS-2026-10-30-tortoise-0c919b4ca77d-01
source-identity: "https://github.com/daniel-ospina/tortoise"
reviewed-boundary: "54922a800f96858935b58ef250da569a4896df44"
---

# Tortoise memory report

## Boundary and evidence

Tortoise retains session material and derived knowledge outside the consuming agent's context. This report keeps the boundary's **complete artifact, partial loop** qualification. SRC-1 is the repository at `54922a800f96858935b58ef250da569a4896df44`; the supplied checkout's HEAD was rechecked against it. Evidence below is inspected implementation and explicitly attributed instruction/design, not an executed capture, delivery, evaluation or improvement demonstration.

The selected memory scope includes SDK/hosted capture, direct Point admission, checkpoint and diary entry, graph-based volunteering, framework and selected Claude-compatible hook delivery, session-start digest, retraction, dream confidence write-back and the source-session expansion helper with its shipped evaluation caller. It includes raw and derived material separately. The frozen repository remains eligible; available but unread mechanisms are retained below as unresolved included surfaces rather than recast as external hosts. External model, database and harness internals and deployed configuration remain outside the evidence. The enclosing model's own compaction, policy compliance and final action are not established by Tortoise's delivery code.

### Coverage inventory

“Direct” means source read for this member; “supplied” means a runtime finding whose quoted support is retained there. All source anchors use SRC-1.

| Entry point or operation | Paths and inspection | Covering records or unresolved fact / conclusion prevented |
|---|---|---|
| CLI dispatch, stdio/HTTP and SDK capture | Supplied `tortoise/deployment.py`, `tortoise/mcp_server.py`, `tortoise/sdk.py`; direct selected shared turn writer and v2 adapter | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-hosted-capture](runtime.md#rt-rte-hosted-capture), [MEM-OBJ-session-turns](#mem-obj-session-turns), [MEM-OBJ-derived-points](#mem-obj-derived-points). M2 internals and every ingest branch unresolved; cannot generalize v2 transformations to them. |
| Consent-bearing production commit; direct Point admission | Supplied `tortoise/sdk.py`; direct MCP wrapper inventory | [RT-RTE-production-commit](runtime.md#rt-rte-production-commit), [RT-RTE-direct-point](runtime.md#rt-rte-direct-point). Remote commit consumer remains untraced; no global consent or provenance guarantee. |
| Checkpoint and diary tools | Direct `tortoise/sdk.py` checkpoint, semantic dedup, diary read/write; `tortoise/mcp_server.py` wrappers and final registration located | [MEM-OBJ-authored-points](#mem-obj-authored-points), [MEM-RTE-checkpoint-diary](#mem-rte-checkpoint-diary). Generic callers do not resolve human authorship or approval. |
| Canonical reflex and framework consumers | Supplied pipeline/framework findings; direct `tortoise/volunteer.py` constants, synopsis and block construction | [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-BAP-framework-block](runtime.md#rt-bap-framework-block), memory annotations. Exact database ranking/why traversal not independently audited. |
| Per-prompt Claude/Codex/Devin/Cline seam | Direct selected `tortoise/claude-hooks/volunteer-turn.sh`, CLI volunteer dispatch located | [MEM-RTE-hook-volunteer](#mem-rte-hook-volunteer). Installation and actual host acceptance unobserved; unknown-harness plain stdout is not proven model injection. |
| Session-start digest | Direct selected `tortoise/claude-hooks/session-start.sh`, complete `_cmd_context` in `tortoise/__main__.py`, SDK `session_context` | [MEM-RTE-start-digest](#mem-rte-start-digest). Hosted GET handler not independently traced; local branch established separately. |
| Journal / optional record / graph state | Supplied emitter; direct shared turn-writer contract, dream journal call | [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission), annotations and session-turn object. Complete record-backed reads, rebuild and backup paths unresolved; cannot promise restoration parity or all-writes durability. |
| Rejection, retraction and confidence maintenance | Direct `tortoise/sdk.py` retract implementation through CAS; `tortoise/dream.py` batch and window methods; MCP maintenance wrapper inventory | [MEM-RTE-point-retraction](#mem-rte-point-retraction), [MEM-OBJ-belief-state](#mem-obj-belief-state), [MEM-RTE-dream-writeback](#mem-rte-dream-writeback). Full invalidate, supersede, delete, merge and promotion/review workflows unresolved; no universal forgetting claim. |
| Spool recovery | Direct selected `tortoise/capture_spool.py` success/permanent/transient handling; `tortoise/store_sync.py` method inventory and CLI dispatch located | [MEM-OBJ-capture-spool](#mem-obj-capture-spool). Full producers, pruning, cursor recovery and admission settings unresolved; cannot establish exactly-once or lossless capture. |
| Source-session expansion and evaluation alternative | Direct `tortoise/session_reinjection.py` seed/fetch/merge and `tools/longmem_eval/retrieve.py` caller | [MEM-RTE-source-expansion](#mem-rte-source-expansion). Reader completion/judge/results not traced; product helper name does not establish live reflex wiring or measured benefit. |
| Other harnesses and UI/service writers | Boundary identifies `tortoise/pi-hooks/`, `tortoise/codex-hooks/`, `tortoise/cursor-hooks/`, `tortoise/hermes-plugin/`, `tortoise/openclaw-plugin/`, `client/`, `integrations/`, `apps/`, `menu-bar/`, `services/`, `website/apps/dashboard/` | Included frontier, bodies not traced end-to-end here. Missing exact persistence, approval, deletion and delivery semantics prevents cross-harness parity and complete writer/consumer inventory. |
| Packs, source import, indexing and governance operations | Boundary inventory; direct MCP function inventory in `tortoise/mcp_server.py` includes pack install, ingest, session/file indexing, source assessment, decision/human-approval, dedup approval and promotion | Included frontier. Missing implementation/admission and actual later use prevents treating all graph content as session-derived or all curation as automatic. |
| Evaluators and maintenance drivers | Boundary lists `battery/`, `benchmarks/`, `eval/`, `tests/`, `validation/`, `spike/`; direct reinjection evaluation caller and dream methods only | Available but uninspected remainder. No measured retrieval quality, learning or deployment-frequency conclusion. |

## Core ideas

1. **Raw traces and derived propositions coexist.** Capturing turns can succeed without an extraction provider. Extraction subsequently admits model-produced graph material, so “captured” and “knowledge extracted” are not synonyms. The session trace is itself bounded and scrubbed, not an untouched transcript archive. See [MEM-OBJ-session-turns](#mem-obj-session-turns), [MEM-OBJ-derived-points](#mem-obj-derived-points) and [RT-RTE-session-capture](runtime.md#rt-rte-session-capture).
2. **The ordinary injected product is a pointer synopsis, not the stored body or full justification.** Graph confidence and lifecycle information control candidate selection. The returned `why` structure can be richer than what a framework actually injects. The block asks the agent to follow supports; it does not enforce that step. See the annotation on [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).
3. **Read paths have different withdrawal and selection semantics.** Current-view volunteering filters terminal material, but the inspected local recent-session digest queries do not carry the same status predicate. Diary reads are identity/recency scoped rather than query-targeted. Retraction therefore cannot be described as deleting every later representation of a claim. See [MEM-RTE-start-digest](#mem-rte-start-digest), [MEM-RTE-checkpoint-diary](#mem-rte-checkpoint-diary) and [MEM-RTE-point-retraction](#mem-rte-point-retraction).
4. **Maintenance changes numerical eligibility without necessarily rewriting meaning.** Dream propagates graph evidence into retained confidence and freshness state. This can change subsequent volunteering, but it is not model training, a transcript summary, or demonstrated improvement. See [MEM-OBJ-belief-state](#mem-obj-belief-state) and [MEM-RTE-dream-writeback](#mem-rte-dream-writeback).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-session-turns
Label: Session episodic turn stream

Source-native identity: Session and contained turn Points written by `_write_capture_turns` (SRC-1, `tortoise/sdk.py`). This object is distinct from the route [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) and from event envelopes [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission): it is the retained trace those mechanisms write, not their generic operation.

Form and storage: scrubbed, windowed natural-language turn content; symbolic deterministic IDs, indices, role/session membership and redaction count; separately derived numerical turn embeddings. The writer can place turns in the record when available, with graph state participating in the alternative path; full record/cache reader dispatch is not established here. Do not infer graph-only turn persistence from Session/CONTAINS terminology. No opaque provider conversation store is established by these local writes; provider retention remains uninspected.

Lineage: caller conversation → stored turn window → redaction → stored text and matching embeddings. This is raw episodic material relative to later extraction, but transformed relative to original user input. On re-capture, shorter windows remove surplus stored turns; removal does not establish removal of all earlier derived knowledge. Caller initiation is not per-turn human approval. Later consumers include session lookup capabilities and the expansion route [MEM-RTE-source-expansion](#mem-rte-source-expansion), with the record/cache compatibility limit stated there. Confidence/pointer delivery ordinarily selects derived beliefs rather than dumping this stream.

> The stored text is the caller-supplied
> pair (``texts_and_counts``) on the live path;
> --- `tortoise/sdk.py`

> turn_texts, redaction_counts = texts_and_counts
> --- `tortoise/sdk.py:2845-2845`

> A SHORTER re-capture DELETES the turns the previous capture left beyond
> the new window (#1920):
> --- `tortoise/sdk.py`

The first and third passages are the writer's contract; assignment and shared caller wiring support the implemented transformation. Exact caps and all store-failure combinations were not independently audited here.

#### MEM-OBJ-derived-points
Label: Extracted graph knowledge and relationships

Source-native identity: v2 payload entities/events/Points/operators admitted by `_extract_session_v2` (SRC-1, `tortoise/sdk.py`, `tortoise/extractor_v2.py`). Distinct retained product of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), not a duplicate route. Compared with [RT-RTE-direct-point](runtime.md#rt-rte-direct-point), these have an extraction lineage rather than arbitrary direct caller content.

Form: natural-language point content and labels, symbolic kinds/IDs/CONTAINS/aboutObject and IMPL/NAND relationships, with numerical embeddings and confidence handled as separate operative parts. Storage: SDK projection and configured event/record machinery, without an all-writes atomicity guarantee. Lineage is bounded/redacted conversation → model story/mapping/search/gap review → structured payload → code-owned writers. The configured model's mutable alias is covered by [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model); embeddings are not updates to [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model).

Write agency: model proposes; code admits/writes after route gates. No per-proposition human approval is inserted. Source/event attribution can survive alongside content, while gaps/warnings may be nonfatal. The returned extracted list is not the entire stored ontology: it is a compact id/kind/text result. Relationship links can preserve structural support or conflict; neither this nor a source ID proves that the proposition retains the extractor's complete reasoning. The later pointer consumer receives selected synopses and flags, not the entire derivation. This is an automatic trace-fed durable content update capable of shaping later work; improved capacity and actual reliance are unobserved.

> conversation = _capture_turn_window(conversation)
> --- `tortoise/sdk.py:13289-13408`

> payload = out.get("payload") or {}
> --- `tortoise/sdk.py:13289-13408`

Supersession is a distinct best-effort payload channel applied after referenced objects exist; unsuccessful application does not fail the entire capture. This limits any claim that v2 atomically replaces prior memory (writer contract in SRC-1, `tortoise/sdk.py`; also [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)).

#### MEM-OBJ-authored-points
Label: Checkpoint items and diary content

Source-native identity: `checkpoint-item` and `diary` Points (SRC-1, `tortoise/sdk.py`). Distinct caller-authored inputs, not necessarily extracted transcript products [MEM-OBJ-derived-points](#mem-obj-derived-points). Their operative admission/read differences are kept in [MEM-RTE-checkpoint-diary](#mem-rte-checkpoint-diary). Closest supplied mechanism is [RT-RTE-direct-point](runtime.md#rt-rte-direct-point): both methods call create_point rather than introducing a new underlying store.

Natural-language content resides with symbolic wing/room/topic/authoredBy and Point identity properties in the projection, subject to configured emission. A provenance Event for a checkpoint records pointAdded and an agent name; it is access/lineage metadata, not the content's reasons or proof of human authorship. Generic caller provenance is unresolved. Checkpoint dedup can reject a redundant candidate without replacing the earlier proposition. Diary read and the recent-session digest are later consumers; checkpoint items can enter graph query/digest surfaces, but their admission does not guarantee volunteering eligibility.

> return self.create_point("diary", entry, **props)
> --- `tortoise/sdk.py`

> "checkpoint-item", item["content"],
> --- `tortoise/sdk.py:29764-29870`

#### MEM-OBJ-belief-state
Label: Dream confidence and freshness state

Source-native identity: persisted confidence, lastDreamedAt, updatedAt and graph-persisted EP messages used for warm start (SRC-1, `tortoise/dream.py`). Numerical belief/message state is symbolic numerical data consumed by fixed algorithms, not distributed model weights; timestamps and IDs are symbolic access/scheduling metadata. Graph is the substrate; ConfidenceChanged journal records mirror committed belief writes when emission works. The message storage implementation and initialization lineage beyond this warm-start interface remain uninspected.

Distinct from content-bearing [MEM-OBJ-derived-points](#mem-obj-derived-points) and generic emission [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission): these are retained numerical/scheduling fields that the maintenance algorithm owns. Dirty roots, staleness and graph evidence feed the maintenance route [MEM-RTE-dream-writeback](#mem-rte-dream-writeback). Confidence later participates in the gate described by [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). Timestamps select future maintenance, not a proposition's truth. Numerical recomputation is curation of reliance signals; it does not establish new natural-language meaning or calibrated correctness.

> self._sdk._hydrate_evidence()
> --- `tortoise/dream.py`

> "SET n.confidence = p.c, n.lastDreamedAt = $now, "
> --- `tortoise/dream.py`

#### MEM-OBJ-capture-spool
Label: Local capture backlog and filing metadata

Source-native identity: spool turn log plus metadata containing capture_key, filed_key/lane/stamp, attempt/backoff and terminal markers (SRC-1, `tortoise/capture_spool.py`). Natural-language turn content is distinct from symbolic filing/access metadata in local files. This backlog precedes server memory admission; keeping it is not extraction learning. No supplied runtime record describes this local recovery object; it is not identical to the graph/journal envelopes [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission).

The inspected flush calls a supplied `post(payload)`, marks an exact matching successful snapshot filed, and leaves newer content eligible for another attempt. The POST function's identity and complete capture-spool producer path are unresolved here, so this establishes local retry/filing behavior, not a fully wired model read-back route. A permanent refusal quarantines while retaining turns; transient failure writes backoff metadata. Thus “discarded” in a summary need not mean destruction of the only copy. No human approval of content is established by retry. Later consumers established here are flush/health bookkeeping, not the foreground model; a successful server capture joins the separately established capture-to-context chain.

> outcome = post(payload)
> --- `tortoise/capture_spool.py`

> fresh["filed_key"] = fresh.get("capture_key") or capture_key(sid, fresh_turns)
> --- `tortoise/capture_spool.py`

> pending["next_attempt_at_ms"] = now_ms + backoff_delay(pending["attempts"]) * 1000
> --- `tortoise/capture_spool.py`

### Routes

#### MEM-RTE-checkpoint-diary
Label: Caller-authored checkpoint and diary admission

Endpoints/owner: caller → SDK checkpoint or diary_write → create_point → graph; diary_read and session_context expose later content (SRC-1, `tortoise/sdk.py`, `tortoise/mcp_server.py`). This composes the underlying [RT-RTE-direct-point](runtime.md#rt-rte-direct-point), but adds distinct batch dedup and agent/wing recency selectors; it is not a duplicate of the primitive write door.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: checkpoint filed/duplicate counts or diary Point; malformed checkpoint content rejected before projection opening.
- Later read-back: diary_read returns newest matching agent entries, optionally wing-filtered; session_context reads diary and recent Points for the digest. Direct tools afford caller-requested access; only the digest has a separately traced automatic model delivery route here.
- Delegated visibility: inapplicable — these methods do not launch an extraction model or a child agent.
- Selection predicate: checkpoint schema check, content hash/in-batch dedup, then optional semantic threshold (default 0.95); diary read uses authoredBy, optional wing and last_n, not task-query semantic relevance.
- Invalidation or expiry: no TTL or automatic semantic revision in these methods; lifecycle changes use other graph operations. Hash-only fallback can admit items semantic dedup would have removed.
- Activation or effect: accepted content becomes a Point; provenance event failure is logged without failing the checkpoint batch. Actual later host use unobserved.
- Evidence limits: generic callers leave human authorship/approval unresolved; no automatic conversation-to-checkpoint summary or complete reasoning-retention contract established.

Trigger/proposal: caller supplies content. Computational validation/dedup can reject; starting a session is not per-item approval. No answer oracle is used. This is open caller filing, with no guaranteed rollback of an already filed prefix if a subsequent item fails. Dedup rejects near-identical text, not necessarily false claims; it does not rewrite the surviving meaning. Embedding implementation may degrade, so a threshold is not proof of one immutable semantic oracle.

> self._check_checkpoint_items(items)
> --- `tortoise/sdk.py`

> "hash-only fallback"
> --- `tortoise/sdk.py:29764-29870`

> "RETURN properties(n) ORDER BY n.createdAt DESC LIMIT $lim",
> --- `tortoise/sdk.py:29964-29964`

#### MEM-RTE-hook-volunteer
Label: Prompt-triggered hook pointer delivery

Endpoints/owner: compatible harness UserPromptSubmit → volunteer-turn.sh → CLI volunteer → canonical reflex → nonempty block → harness-specific JSON field (SRC-1, `tortoise/claude-hooks/volunteer-turn.sh`, `tortoise/__main__.py`). Distinct entry/delivery seam around [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not a second canonical selector.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON carrying additionalContext for Claude/Codex/Devin or contextModification.context for Cline; empty reflex output returns without injected material.
- Later read-back: this code-triggered prompt callback solicits prior graph memory on behalf of the host turn; canonical selected pointers reach the forthcoming host context if its documented hook contract is honored.
- Delegated visibility: the CLI receives the current prompt, not an isolated worker's full transcript; selected pointer block crosses back.
- Selection predicate: resolved runnable seam plus nonblank block; inner retrieval intent, confidence and budget remain those of the canonical pipeline.
- Invalidation or expiry: per-turn output is ephemeral; graph lifecycle controls inner eligibility. No local memory eviction or host-context removal is performed by this shell seam.
- Activation or effect: emits a context contribution, not a mandatory tool call. Unknown-harness plain stdout cannot be counted as model delivery.
- Evidence limits: installation, successful interpreter resolution, host hook execution and model reliance are unobserved; comments claiming compatibility do not establish cross-host operation.

> BLOCK="$(printf '%s' "$PROMPT" | "$TORTOISE_BIN" volunteer 2>"$REFLEX_ERR" || true)"
> --- `tortoise/claude-hooks/volunteer-turn.sh`

> 'additionalContext': os.environ.get('TORTOISE_VOLUNTEER_BLOCK', '')}}))
> --- `tortoise/claude-hooks/volunteer-turn.sh`

#### MEM-RTE-start-digest
Label: Recent-session digest into session-start context

Endpoints/owner: SessionStart shell → `tortoise context` → local SDK session_context or hosted GET /v1/context → CLI rendering → hook stdout (SRC-1, `tortoise/claude-hooks/session-start.sh`, `tortoise/__main__.py`, `tortoise/sdk.py`). No supplied runtime route has this recency-based selector; it is distinct from task-window volunteering [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed compact digest or empty-source notice; failures are swallowed by the hook's digest function.
- Later read-back: prior diary, recent Point and confidence material reaches a new host session via stdout under the hook contract. This is automatic recency supply, not a model-issued memory query.
- Delegated visibility: rendered limited excerpts only; event rows affect empty-state detection but are not printed by the inspected renderer. No child-agent context delegation.
- Selection predicate: local query limits diary 10, recent Points 20, Events 20, confidence rows 20; noise filtering applies to Points/confidence after query. Renderer takes at most 5 diary, 8 Points and 5 confidence rows, truncating content to 160/160/120 characters respectively.
- Invalidation or expiry: local SDK queries shown here have no terminal-status exclusion; recency/rank-out and noise filters are not deletion. Cannot promise retracted material never appears in this digest.
- Activation or effect: supplies natural-language prior context; shipped Claude instructions request starting from relevant prior decisions, not blindly treating all memory as final truth.
- Evidence limits: local query and renderer traced; hosted response internals not independently verified. Actual host injection, subsequent reliance and a total byte cap for the digest are not established.

The CLI chooses hosted mode from user-global stored configuration, with environment alone not selecting hosted mode. That source-routing control is distinct from selection of memory items. The digest's “previous sessions” label is broader than its demonstrated predicate: recency queries do not select a particular prior session or compare current session ID.

> data = sdk.session_context()
> --- `tortoise/__main__.py`

> for p in points[:8]:
> --- `tortoise/__main__.py`

> "MATCH (n:Point) "
>             "WHERE n.is_operator = false "
>             "RETURN properties(n) ORDER BY n.createdAt DESC LIMIT 20"
> --- `tortoise/sdk.py`

> "$TORTOISE_BIN" context 2>/dev/null || true
> --- `tortoise/claude-hooks/session-start.sh`

#### MEM-RTE-point-retraction
Label: Tombstone retraction and subsequent eligibility

Endpoints/owner: caller / MCP wrapper → SDK retract_point → lifecycle/window validation → event emission → conditional status update (SRC-1, `tortoise/sdk.py`, `tortoise/mcp_server.py`). Distinct maintenance transition, extending the lifecycle frontier in [RT-RTE-direct-point](runtime.md#rt-rte-direct-point).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: result or missing/operator/terminal/inverted-window failure; MCP also exposes a dry-run preview.
- Later read-back: stored Point remains addressable while canonical current-view volunteering excludes terminal statuses. Recent-session digest need not apply that filter; full direct get/history consumers are not audited here.
- Delegated visibility: inapplicable — retraction is a code-owned store transition, not model delegation.
- Selection predicate: caller names Point; lifecycle guard rejects missing/operator/already-terminal state; optional valid_to cannot invert the claim window. CAS repeats terminal eligibility at mutation.
- Invalidation or expiry: terminal status retracted, with optional validTo and recorded update time; not physical erasure, universal cache invalidation or rollback of earlier prompt copies.
- Activation or effect: changes future current-view eligibility; append result is not checked before this CAS, so journal failure does not itself veto the state transition.
- Evidence limits: no target execution; supersede/invalidate/delete and complete neighborhood recomputation/replay paths not traced. Full reconstruction and all-consumer withdrawal remain unresolved.

Caller proposes withdrawal; code guards/vetoes invalid transitions. Human contribution is unresolved for generic callers; no answer oracle is involved. The method records withdrawal, not a newly justified replacement theory. Admission and recovery cannot be equated with cross-store atomicity, as also bounded by [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission).

> self._assert_lifecycle_guard(id, method="retraction")
> --- `tortoise/sdk.py`

> self._emit_event("PointRetracted", {"id": id, **_window},
>                          id=id, recorded_ts=_now, **_window)
> --- `tortoise/sdk.py`

> "SET n.status = 'retracted', n.updatedAt = $now"
> --- `tortoise/sdk.py`

#### MEM-RTE-dream-writeback
Label: Windowed confidence maintenance and later gate input

Endpoints/owner: SDK/Dreamer caller → dream_window → stale/dirty selection → bounded operator traversal → EP run → confidence/freshness write-back → journal; subsequent confidence gate reads graph beliefs (SRC-1, `tortoise/dream.py`; [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)). Distinct from extraction/admission routes: maintenance modifies reliance signals rather than proposing text.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: convergence, batches, operator budget use and affected-claim IDs.
- Later read-back: persisted evidence/messages seed later EP work; graph confidence can affect later pointer eligibility. No direct injection of dream reasoning or maintenance logs into a model is established.
- Delegated visibility: inapplicable — selected operations call the local EP engine, not an extraction model/subagent.
- Selection predicate: stale-first claim ranking union retained dirty roots, bounded distinct operators; all-null graph expands the candidate window, but operator processing still uses the pass budget. Zero budget is a no-op.
- Invalidation or expiry: stale epoch guard skips write-back; failed convergence withholds freshness stamps. Dirty-root clearing is delegated to SDK adapter logic not fully audited here.
- Activation or effect: numerical belief/freshness writes and ConfidenceChanged events; downstream confidence gate is wired, exercised changed selection and benefit unobserved.
- Evidence limits: EP numerical algorithm, all initial evidence provenance, scheduler activation frequency and message persistence/recovery not traced end-to-end. Confidence does not certify truth.

Software selects/updates based on graph inputs. No per-write human review or expected-answer oracle appears in the inspected batch/window methods. No natural-language proposal/rejection or content rewrite occurs in these methods. The trace-fed content path remains extraction; numerical propagation alone is not evidence of learning from the success of prior agent action.

> iterations, converged = ep.run(
>             seed_ids, max_hops=max_hops,
>             evidence=dict(self._sdk._evidence),
>             warm_start=warm_start,
>         )
> --- `tortoise/dream.py`

> stamp_now = stamp and converged
> --- `tortoise/dream.py`

> emit("ConfidenceChanged", id=cid, confidence=by_id[cid],
>                      lastDreamedAt=now)
> --- `tortoise/dream.py`

#### MEM-RTE-source-expansion
Label: Source-session turn expansion in retrieval evaluation

Endpoints/owner: shipped LongMemEval retrieve driver → seeded_sessions → bounded graph fetch → property/speaker annotation → merge/guard/recap → later context candidate pool (SRC-1, `tortoise/session_reinjection.py`, `tools/longmem_eval/retrieve.py`). Distinct alternate consumer of retained session traces; no supplied runtime record establishes this path. It is not automatically part of canonical volunteering merely because helpers live in the product package.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: fetch report and expanded pool with separate fetched/merged counts; no model answer from the helper.
- Later read-back: seeded earlier graph hits select containing sessions, bringing omitted turn material back into a later retrieval/evaluation invocation. End-to-end reader prompt assembly and judge consumption remain uninspected here.
- Delegated visibility: annotation fetches content/properties/speaker for selected IDs; the helper does not launch a model or expose the whole original session to a worker.
- Selection predicate: enabled arm, nonempty pool and non-is_tr branch; seeds count admitted claim-text hits, distinct real sessions, and finite fan-out. Fetch follows Session CONTAINS from seed IDs, excludes existing pool IDs, filters turn shape, then applies per-session and total distinct-item caps.
- Invalidation or expiry: no store mutation or summary replacement; on failure retains original pool. Shared seeds may expand multiple containing sessions; seed budget does not model every eventual reader byte/token-cap admission.
- Activation or effect: merge places additions after a session's last base rank and applies guards/recap. Default TURN items are not raw-chunk recapped; explicit total cap controls expansion volume.
- Evidence limits: graph-only fetch cannot establish completeness for record-only turns; live SDK reflex wiring and final reader use/benefit are not established by this inspected evaluation caller.

Default constants documented in the inspected caller yield a total budget of 10 against possible fan-out 15, with explicit/run/environment overrides. Alternative helper chunk_kind can select evaluation transcript chunks instead of product TURN material; this alternative raw representation must not be silently treated as derived claims or a second extractor. This chain is deterministic request-driven expansion of retained text, not unsolicited supply independent of a retrieval request.

> if reinjection_on and not is_tr and pool:
> --- `tools/longmem_eval/retrieve.py`

> _props = point_props_for_hits(
>                             sdk._get_proj(), _all_ids)
> --- `tools/longmem_eval/retrieve.py`

> pool = _merged
> --- `tools/longmem_eval/retrieve.py:2300-2300`

> "MATCH (s:Session)-[:CONTAINS]->(seed) "
> --- `tortoise/session_reinjection.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-start-digest
Label: Session-start excerpts as model context

Consumer: forthcoming host agent/model session. Channel: hook stdout containing natural-language recent-memory excerpts, through [MEM-RTE-start-digest](#mem-rte-start-digest). Force: advisory context and shipped instruction to use relevant prior decisions; not a deterministic veto or proof of correctness. Horizon: session start and whatever subsequent host context retention preserves, not a demonstrated cross-session host-store update. Distinct from [RT-BAP-framework-block](runtime.md#rt-bap-framework-block): it has a different recency selector and delivery seam.

SRC-1, `tortoise/claude-hooks/CLAUDE.tortoise.md`, distinguishes relevant memory from exclusive authority:

> Memory is a floor, not a ceiling — always answer from the current context too.
> --- `tortoise/claude-hooks/CLAUDE.tortoise.md`

## Annotations

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Memory lineage: storage of bounded/redacted turns precedes creation of derived content, and re-capture can update turns without redoing successful extraction. Thus source trace and derived proposition may have different update horizons. Known subsequent transformations do not resolve initial truth, generic caller agency or human approval. The new retained-part declarations are [MEM-OBJ-session-turns](#mem-obj-session-turns) and [MEM-OBJ-derived-points](#mem-obj-derived-points); neither re-declares the generic runtime route. Provider absence leaves episodic memory possible; no-provider is not an absence of all memory. The supplied route's quotes support provider/dispatch behavior; direct writer/adapter evidence is retained with the new objects.

#### On [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission)

Memory substrate/lineage qualification: envelopes are rebuild/feed/projection material, not necessarily the later model-visible content. Some contain content snapshots or vectors, others only mutation metadata. A graph event feed, optional journal and optional record sink have distinct failure outcomes. No complete replay-to-reader parity follows. The shared turn writer explicitly attempts record-capable turn storage, while graph-only source expansion uses graph traversal; this is a named unresolved compatibility question, not evidence of universally missing turns (SRC-1, `tortoise/sdk.py`; [MEM-OBJ-session-turns](#mem-obj-session-turns), [MEM-RTE-source-expansion](#mem-rte-source-expansion)).

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

The memory selector's input is the bounded current window and prior_context, plus graph search/why confidence. Constants in SRC-1, `tortoise/volunteer.py`, cap input at 1000 turns/15 KiB, default output at three pointers (maximum five), synopses at 160 characters and block at 8 KiB. Frameworks can impose their own smaller input windows. Re-mention suppression spends no slot; it is not persistent erasure. This code-driven push callback performs a request to the memory service, but the foreground model need not explicitly ask for the returned memory.

Actual delivered material differs from stored content and returned metadata. `_synopsis` strips controls/collapses whitespace and truncates text; block construction includes ID, label, synopsis and contested/superseded flags. Structured why entries can include support chains and conflicts, but framework consumers use the block. The injected block retains a request to read supports, not the full supporting case. A “data, not instructions” comment and whitespace sanitation do not establish model resistance to malicious stored prose or truthful content. Exact selection confidence and source provenance do not grant runtime-enforced authority at the model consumer.

> DEFAULT_MAX_POINTERS = 3
> --- `tortoise/volunteer.py`

> BLOCK_MAX_BYTES = 8 * 1024
> --- `tortoise/volunteer.py`

> text = re.sub(r"\s+", " ", text).strip()
> --- `tortoise/volunteer.py`

> "Follow a pointer before treating a detail as settled.",
> --- `tortoise/volunteer.py`

> f"{ptr['synopsis']}"
> --- `tortoise/volunteer.py`

## Write side

Capture has separate acquisition, content transformation and storage steps. Caller conversation is acquired under SDK/hosted policy gates; v2 model/code derives graph content automatically; physical I/O does not imply human endorsement. Source text is stored after windowing/redaction, then the extractor's narrative/mapping/gap-review path yields a structured payload. Both raw trace and derived propositions can affect later work, through different readers. Neither transcript retention nor graph support edges proves that the full reasons for a proposed claim survive to the later model. See [RT-RTE-hosted-capture](runtime.md#rt-rte-hosted-capture), [MEM-OBJ-session-turns](#mem-obj-session-turns) and [MEM-OBJ-derived-points](#mem-obj-derived-points).

Direct create_point, checkpoint and diary are alternative admission doors. Generic caller content may be human, agent or software authored; the exposed API does not settle that distinction. Kind/namespace/schema checks and checkpoint dedup are computational controls, while optional capture/recording/consent settings veto stages rather than certify each retained sentence. A checkpoint is not an automatically generated conversation compaction: its caller supplies content. No checkpoint-summary read-back equivalence with a host's native compaction is established. See [RT-RTE-direct-point](runtime.md#rt-rte-direct-point), [RT-RTE-production-commit](runtime.md#rt-rte-production-commit) and [MEM-RTE-checkpoint-diary](#mem-rte-checkpoint-diary).

Maintenance has several distinct consequences. Checkpoint dedup removes admissions, not meaning from a surviving entry. Dream writes confidence and freshness, not revised prose. Retraction tombstones rather than erases. Shorter turn re-capture sweeps surplus trace rows but need not replace derived Points. Spool permanent refusal keeps a local raw copy; successful filing metadata suppresses redundant posting. Each of these is a different notion of “cleanup.” Complete delete/supersession/review/pack paths remain the named inventory frontier, so none is promoted to an all-system removal policy. See [MEM-RTE-point-retraction](#mem-rte-point-retraction), [MEM-RTE-dream-writeback](#mem-rte-dream-writeback) and [MEM-OBJ-capture-spool](#mem-obj-capture-spool).

The trace-fed extraction chain retains behavior-shaping content; actual improved future capacity is unobserved. The dream chain reuses numerical graph state; its name does not establish reflection over an agent's mistakes. Evaluation selection/reader/judge operation beyond the inspected reinjection caller is not evidence of a production feedback-to-memory update. No provider-weight training or universal absence of such learning is inferred.

## Read-back

Three established delivery shapes must remain separate:

- **Current-turn pointers:** callback or compatible prompt hook → bounded window → canonical graph selection → bounded block → host model context. This is automatic callback delivery, not proof of reliance. Full bodies/supports require further access; a pointer in context is not an automatically dereferenced machine address. See [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-BAP-framework-block](runtime.md#rt-bap-framework-block) and [MEM-RTE-hook-volunteer](#mem-rte-hook-volunteer).
- **Session-start recency:** automatic hook → SDK/HTTP digest → excerpt renderer → stdout context. Selection is timestamp/limit/noise based, not current-task relevance. No terminal filter in the inspected local query means it is not a reliable withdrawal boundary. See [MEM-RTE-start-digest](#mem-rte-start-digest) and [MEM-BAP-start-digest](#mem-bap-start-digest).
- **Explicit retrieval/expansion:** diary_read is an exposed requested read capability; absent a particular caller it is not proof of model delivery. The shipped evaluation reinjection caller does establish a concrete retained-turn-to-expanded-pool chain, but not final reader reliance or live reflex parity. See [MEM-RTE-checkpoint-diary](#mem-rte-checkpoint-diary) and [MEM-RTE-source-expansion](#mem-rte-source-expansion).

Working-context control here is selection, shortening and external read-back, not a traced subagent stack frame. Framework input windows drop older turns for the reflex without evicting them from the enclosing model; injected output adds selected memory. Source expansion brings excluded text into a candidate pool; it does not undo a host's native compaction. No scoped child frame, whole-frame discard or automatic dereference follows from these methods. Opaque host isolation/compaction remains outside inspected Tortoise behavior. Storage pointers keep outside material reachable only through explicit retrieval operations; nothing establishes liveness/reference counting for copied model-window content.

## Integration issues

1. **Record-backed trace versus graph-only expansion:** [MEM-OBJ-session-turns](#mem-obj-session-turns), the annotation on [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission) and [MEM-RTE-source-expansion](#mem-rte-source-expansion) expose different substrates. The shared writer contract says record-capable turns; the expansion query only follows graph Session/CONTAINS. Missing facts are full record-backed turn lookup and whether the evaluation/production callers populate graph turns. Consequence: no complete replay/expansion coverage or graph-only persistence claim. This qualifies runtime's broad graph-retention wording rather than disputing its correctly limited emitter semantics.
2. **Withdrawal is consumer-specific:** [MEM-RTE-point-retraction](#mem-rte-point-retraction) plus [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) support terminal exclusion in current-view selection, while [MEM-RTE-start-digest](#mem-rte-start-digest) has no such predicate in its inspected local queries. Consequence: correct any integrated claim that terminal status prevents every context exposure; no correction to runtime's narrowly stated canonical current-view claim is required.
3. **Rich metadata does not imply rich delivered justification:** the annotation on [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-BAP-framework-block](runtime.md#rt-bap-framework-block) distinguish returned why from injected synopsis. Consequence: neither complete rationale preservation nor mandatory evidence reading follows. Full why/source traversal remains uninspected here.
4. **Reinjection deployment scope:** [MEM-RTE-source-expansion](#mem-rte-source-expansion) is wired in a shipped evaluation driver. Scoped search in product and evaluation Python located its concrete call there, not in SDK volunteering. This does not warrant an all-repository absence. Consequence: keep evaluation pool expansion separate from live reflex claims and from final reader/judge outcomes.
5. **Named unresolved included surfaces:** M2, full commit consumer, source/pack imports, merge/review, replay/backup, UI/service writers, other harness plugins, record readers, pruning/store-sync and complete evaluator drivers remain as listed in the coverage inventory. Consequence: the partial-loop boundary and nonuniversal admission/durability/learning claims must survive reconciliation. These are available evidence not access gaps.

No declaration is a possible replacement for a supplied record after comparison. New objects are retained products or numerical/local parts not separately declared by runtime; new routes add concrete distinct callers, selectors or maintenance operations. The canonical capture/reflex/emitter findings are annotations, not duplicate declarations. No source identity or revision correction is proposed.

## Limitations and checks

Source identity was rechecked by Git HEAD against the supplied frozen revision. Added source reads remain SRC-1 implementation or target-authored doctrine; no target execution, dependencies, model calls, runtime fixtures or live services were used. The supplied invocation and record/member contracts were read completely, including bounded continuation reads. Failed exploratory searches for nonexistent context helper filenames established no absence and support no finding; the actual CLI and SDK digest methods were subsequently inspected.

No observed operation, reliable host compliance, truth guarantee, latency measurement, durable all-store atomicity, whole-system deletion guarantee or improved future capacity is established. Exact store failure/rebuild parity, all initializer/embedding provenance, complete later rationale retrieval and full maintenance/harness/evaluator coverage remain bounded unknowns beside the affected records. Validation establishes form and quote occurrence, not these semantic conclusions.

Validation: the role-scoped commonplace-validate check passed after disambiguating three quotation attributions; no finding was narrowed or withdrawn to obtain a pass.
