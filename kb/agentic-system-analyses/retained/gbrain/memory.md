---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "GBrain memory mechanisms: explicit facts, canonical fences, core delivery, compaction harvest, consolidation and rating-driven retrieval at the frozen boundary."
run-id: AAS-2026-10-11-gbrain-9de8e3c225d3-01
source-identity: "https://github.com/garrytan/gbrain"
reviewed-boundary: "da434385572e0dc0d825649179aabed4107d6e60"
---

# GBrain memory report

## Boundary and evidence

GBrain retains knowledge for external agents and for its own retrieval and maintenance consumers. This report preserves the boundary's **complete artifact, partial loop** classification. SRC-1 is the repository at `da434385572e0dc0d825649179aabed4107d6e60`, declared in [boundary](boundary.md). HEAD was rechecked and matched; the checkout was clean. All added findings are implementation evidence, except explicitly identified comments and operation descriptions. No execution or causal experiment was performed.

The selected scope includes explicit fact writes, extracted facts, canonical page fences, core memory, requested recall, context packs and deltas, compaction banking, withdrawal, consolidation, feedback and supplied skill/subagent persistence. External host compaction and model interpretation remain excluded. GBrain's checkpoint producer is included even though the host owns the actual compaction. Available but untraced shipped branches remain included uncertainties, not absences.

The following table distinguishes direct bounded source inspection from supplied runtime evidence. Source paths are commit-relative under SRC-1. Each unresolved row names the conclusion prevented.

| Operation or operative part | Source paths | Coverage and limits |
|---|---|---|
| CLI capture, MCP dispatch, journal/publication | `src/commands/capture.ts`, `src/mcp/dispatch.ts`, `src/core/persistence/coordinator.ts` | Supplied [RT-RTE-capture-write](runtime.md#rt-rte-capture-write), [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch); no independent full transport audit. |
| Frozen operation catalog and memory verbs | `src/core/operations.ts`, `src/core/verbs.ts`, `src/core/ops/facts.ts` | Direct imports/catalog searches and bounded handlers; [MEM-RTE-remember-write](#mem-rte-remember-write), [MEM-RTE-recall-delivery](#mem-rte-recall-delivery), [MEM-RTE-context-pack](#mem-rte-context-pack), [MEM-RTE-delta-delivery](#mem-rte-delta-delivery). Entity and synthesize implementations not fully read; no complete facade conclusion. |
| Explicit write preparation, fact/page representation | `src/core/persistence/memory-prepare.ts`, `src/core/facts/backstop.ts` | Direct; [MEM-OBJ-facts](#mem-obj-facts), [MEM-OBJ-fact-metadata](#mem-obj-fact-metadata), [MEM-OBJ-fact-embedding](#mem-obj-fact-embedding), [MEM-OBJ-facts-fence](#mem-obj-facts-fence). Embedding and index rebuild internals remain untraced. |
| Extraction and alternate DB-only/fence paths | `src/core/facts/extract.ts`, `src/core/facts/backstop.ts` | Direct bounded producer and publication selection; [MEM-RTE-extraction-write](#mem-rte-extraction-write). Managed facts-maintenance internals, connectors, transcript drains and extraction-review admission remain uninspected; no universal publication-control claim. |
| Core designation, editing and delivery | `src/core/core-memory.ts`, `src/core/persistence/core-guard.ts` | Direct bounded implementation; [MEM-RTE-core-delivery](#mem-rte-core-delivery). Compiled instruction-file consumers not traced. |
| SessionStart hook, other hook dispatch | `src/commands/hook.ts` | Direct bounded dispatch searches; session-start IPC/output wiring identified. Stop writeback and PreCompact bodies not fully inspected; no all-host trace-origin or consent conclusion. |
| OpenClaw compaction and manifest | `src/core/context-engine.ts`, `src/core/context/session-state.ts`, `src/core/context/checkpoint-harvest.ts` | Direct bounded reads; [MEM-RTE-checkpoint-harvest](#mem-rte-checkpoint-harvest). Renderer/redactor, corpus writer/GC, manifest merge/GC and harvest receipt publication now have bounded direct reads; [MEM-OBJ-checkpoint-corpus](#mem-obj-checkpoint-corpus) and [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest) separate their lineage and consumers. Full sweep and GC scheduling remain uninspected; no complete retention or cleanup guarantee. |
| Forget and purge | `src/core/facts/withdrawal.ts`, `src/core/ops/purge.ts`, `src/core/facts/purge.ts` | Direct withdrawal and purge-entry reads; [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal). Purge deletion inventory/verifier and semantic withdrawal review not fully traced; no physical-erasure or semantic-paraphrase guarantee. |
| Consolidation and takes read tools | `src/core/cycle/phases/consolidate.ts`, `src/core/ops/takes.ts` | Direct; [MEM-RTE-facts-consolidation](#mem-rte-facts-consolidation). Managed consolidation publication internals remain uninspected. |
| Retrieval ratings and later ranking | `src/core/feedback/rate.ts`, `src/core/feedback/store.ts`, `src/core/search/feedback-boost.ts`, `src/core/search/hybrid/rank.ts` | Direct reads plus rank-stage call-site search; [MEM-RTE-feedback-update](#mem-rte-feedback-update). [MEM-OBJ-retrieval-events](#mem-obj-retrieval-events), [MEM-OBJ-retrieval-feedback](#mem-obj-retrieval-feedback) and [MEM-OBJ-ranking-weights](#mem-obj-ranking-weights) separate attribution, admitted history and derived ranking state. Store prune/reset and migration schema now directly read; relational-edge weighting consumer, implicit-feedback routes and cleanup scheduling remain untraced. |
| Query/image selection, shared skills, durable subagent replay | `src/core/ops/search.ts`, `src/core/shared-skills/publication.ts`, `src/core/minions/handlers/subagent.ts` | Supplied runtime findings, annotated below. No new complete ranking, installed-skill activation or replay-retention finding. |
| Other dream transformations and evaluators | `src/core/cycle/phase-table.ts`, `src/core/cycle.ts`, `src/commands/eval-brainbench.ts` | Direct phase-table searches and supplied [RT-RTE-maintenance-run](runtime.md#rt-rte-maintenance-run). Synthesis, patterns, concepts, atom extraction, conflict review, grade cache, nightly probes and skillopt remain unresolved operative parts; their candidate contents, rejection, retained reasons and later consumers are not established. No measured-quality or complete trace-learning assessment. |
| Administrative UI, bootstrap/compiled context, pinned questions, remaining connectors and libraries | `admin/`, `src/core/questions/service.ts`, `src/core/bootstrap/`, `src/core/context/` | Included available evidence, mostly inventory or imports only. Pack's pinned-answer call is visible, but its writer and admission are not traced. No universal instruction-authority, initialization or withdrawal propagation claim. |

## Core ideas

1. **Knowledge text and control state have different consumers.** Fact claims and page bodies supply evidence through caller/model interpretation. Fact IDs, scope, expiry, trust, source and supersession fields govern eligibility and routing. A provenance string is attribution, not a certified source. [MEM-OBJ-facts](#mem-obj-facts), [MEM-OBJ-fact-metadata](#mem-obj-fact-metadata).
2. **Fact storage is not universally file-backed.** Explicit remember can publish an entity fence and SQL row together, but subjectless/unresolved facts and extraction fallbacks can be DB-only. This is a source-supported countercase to treating Markdown as every fact's canonical representation. [MEM-RTE-remember-write](#mem-rte-remember-write), [MEM-RTE-extraction-write](#mem-rte-extraction-write).
3. **Independent supply differs from requested retrieval.** Recall returns selected rows after eligibility, redaction and budget packing. Core delivery is designation-based, not query-relevance selection. Hooks and OpenClaw can deliver retained material without a model choosing recall first. Checkpoints chiefly deliver pointers, not the original transcript or full derived claims. [MEM-RTE-recall-delivery](#mem-rte-recall-delivery), [MEM-RTE-core-delivery](#mem-rte-core-delivery), [MEM-RTE-checkpoint-harvest](#mem-rte-checkpoint-harvest).
4. **Forgetting retains negative control state.** Withdrawal expires matching facts, records a fingerprint ledger and invalidates affected projections. Core reads consult canonical snapshots rather than blindly injecting stale stored bodies. This establishes bounded suppression, not universal semantic deletion. [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal).
5. **A trace can change later selection without changing knowledge claims.** Rating an attributed retrieval event updates retained ranking weights. Subsequent hybrid ranking reads those weights. The implementation therefore has a trace-fed behavioral update, independently of whether extraction or consolidation improves knowledge. Benefit is unobserved. [MEM-RTE-feedback-update](#mem-rte-feedback-update).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-facts
Label: Fact claim text

Source-native identity: `facts.fact`. Form: natural-language claims; substrate: SQL facts rows through the engine. Lineage may be explicit caller text, page/transcript extraction or compaction harvest. It is derived memory when extracted, not a raw conversation trace. Recall and packs deliver eligible claims; consolidation interprets confidence/embeddings to select claim text. Text supplies knowledge to later agents, not an executable command. Provenance and reasons need not be complete. Distinct from [RT-OBJ-persistence-requests](runtime.md#rt-obj-persistence-requests), which retains write intent and settlement rather than the active knowledge row. SRC-1 `src/core/persistence/memory-prepare.ts`, `src/core/ops/facts.ts`.

> const fact: NewFact = { ...input, source: String(p.provenance).trim(), valid_from: validFrom, valid_until: validUntil,
>     confidence: 1, embedding, embedding_model, source_session: typeof p.session_id === 'string' ? p.session_id : null,
>     ...(context ? { context } : {}) };
> --- `src/core/persistence/memory-prepare.ts`

#### MEM-OBJ-fact-metadata
Label: Fact eligibility and lineage fields

Source-native identity: `facts` ID, entity/source/session, visibility, dates, confidence, supersession, consolidation and trust fields. Form: symbolic control/access metadata plus natural-language provenance/context notes. Substrate: SQL columns. They select, invalidate and attribute claims; they are not the claim's truth warrant. Explicit writes assign confidence 1, which is not an observed probability. Session provenance is not universally durable through fence rebuild: the extract_facts parameter contract explicitly warns that fence reconstruction loses session IDs. No supplied object counterpart; the journal's authority/recovery fields have a different owner and horizon. SRC-1 `src/core/persistence/memory-prepare.ts`, `src/core/ops/facts.ts`.

> session_id: { type: 'string', description: 'Opaque session id (e.g. topic-id from MCP _meta.session_id, or CLI --session). Stored on each fact for the recall --session filter. Not an auth surface. NOTE (#4206): the session survives on the DB row at insert time, but the `## Facts` fence has no session column — a fence rebuild/reconcile re-derives rows session-less. Treat fence-backed facts as session-less across rebuilds.' },
> --- `src/core/ops/facts.ts`

#### MEM-OBJ-fact-embedding
Label: Fact vector representation

Source-native identity: `facts.embedding`, `embedding_model`. Form: dense numerical representation, distinct from natural-language fact text and symbolic model identity; substrate: SQL vector state. Explicit write preparation embeds claim text when available; inferred entity links disable vector-based dedup while retaining the embedding. Consolidation uses cosine clustering. Exact embedding provenance for pre-existing rows and rebuild compatibility is not fully established. This is output state, not the weights of [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). SRC-1 `src/core/persistence/memory-prepare.ts`, `src/core/cycle/phases/consolidate.ts`.

> const { embedding, embedding_model, degraded } = await prepareFactEmbedding(input.fact, signal, await factEmbeddingDisabled(engine, config));
> signal?.throwIfAborted();
> // #5836: an inferred link dedups exact text only, so it never supersedes or drops a similar fact.
> const dedupEmbedding = p.entity_inferred ? null : embedding;
> --- `src/core/persistence/memory-prepare.ts`

#### MEM-OBJ-facts-fence
Label: Entity page facts fence

Source-native identity: parsed/rendered `## Facts` fence in entity `compiled_truth`, with `row_num` and `source_markdown_slug` on indexed facts. Form: mixed natural-language claims and symbolic tabular provenance/status fields; substrate: page DB body and optional canonical Markdown. Explicit remember appends a row and can deactivate the superseded row; the parser/chunker then prepares publication. Later page reads and fact indexing are distinct consumers. A fence is not a complete transcript and does not preserve all SQL metadata. No supplied object counterpart: [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) is a page-producing route, not this retained representation. SRC-1 `src/core/persistence/memory-prepare.ts`.

> const appended = refuseUnparsedRewrite(target.page, row.slug, row.source_id, () => upsertFactRow(target.page.compiled_truth, {
>       claim: input.fact, kind: input.kind, visibility: input.visibility, confidence: 1, notability: 'medium', validFrom: formatFenceDate(validFrom),
>       validUntil: validUntil ? formatFenceDate(validUntil) : undefined, source: fact.source, context }));
> --- `src/core/persistence/memory-prepare.ts`

#### MEM-OBJ-session-checkpoints
Label: Session checkpoint manifest and corpus

Source-native identity: corpus segment `.txt` plus ledger/sidecars, and `session_context_state.checkpoint_manifest`. These are separate operative parts within one checkpoint mechanism: rendered transcript corpus is natural-language trace material on disk; manifest is symbolic segment/order/time/slug metadata with readable title summaries in SQL JSONB. Neither is an opaque provider-native checkpoint. Corpus bytes are renderer output, not proven verbatim host history. The valid container is preserved; its independently assessed parts are [MEM-OBJ-checkpoint-corpus](#mem-obj-checkpoint-corpus) and [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest). Harvest creates facts/fences; verified entity links then enter the manifest. The manifest is consumed by later assemble/pack rendering, not itself by fact extraction. [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) consumes this state but does not own its producer. SRC-1 `src/core/context-engine.ts`, `src/core/context/session-state.ts`.

> const merged = [...fresh, ...existing.filter((l) => !freshSlugs.has(l.slug))].slice(
>       0,
>       CHECKPOINT_MANIFEST_CAP,
>     );
> --- `src/core/context/session-state.ts`

#### MEM-OBJ-checkpoint-corpus
Label: Rendered checkpoint transcript corpus

Part of: [MEM-OBJ-session-checkpoints](#mem-obj-session-checkpoints)

Source-native identity: content-addressed corpus segment `.txt`, accompanied by the session ledger and harvest/progress/ingested sidecars. Representational form: natural-language rendered trace text; symbolic hashes, source stamps and sidecar state control banking and retries. Storage substrate: local corpus files, temporary-file rename and JSON sidecars, not SQL or provider-native opaque checkpoint state. This part is distinct from the supplied context-assembly consumer and from [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest): it preserves extraction input, not a pointer selector. SRC-1 `src/core/context/corpus-segments.ts`, `src/core/context/checkpoint-harvest.ts`.

Lineage: bounded host turn windows are rendered by toCorpusText and scanned/redacted before banking; scanner failure returns null. The stored bytes therefore need not equal original host history. Initial host/provider provenance and the full renderer remain unresolved. Extraction and sweep consume these files under [MEM-RTE-checkpoint-harvest](#mem-rte-checkpoint-harvest), producing claim text and optional fences. The corpus itself is not delivered in later context assembly and has no independently established direct host-model authority. Its authority at the extraction consumer is input material interpreted under extractor guidance; retained raw trace alone does not establish a learned strategy or improved capacity.

Persistence/invalidation: identical content addresses avoid rewriting existing files and preserve sidecar lifecycle. An ingested marker stops repeat extraction. FIFO manifest failure keeps its receipt and leaves the corpus retryable without repeating extraction; inline fallback's different contract remains in the route. File GC uses mtime and a longer ceiling for un-ingested files; companion GC removes old ledgers and orphan sidecars. These are inspected cleanup capabilities, not verified scheduling or universal erasure. They are independent of SQL session-row retention.

> const text = toCorpusText(turns);
>   try {
>     const scan = await import('../secret-scan.ts');
>     const redacted = scan.redactFindings(text);
>     return { text: redacted.text, redactions: redacted.redactions.length };
> --- `src/core/context/corpus-segments.ts`

> const ageLimit = present.has(name + INGESTED_SUFFIX) ? retentionMs : retentionMs * CORPUS_UNINGESTED_RETENTION_FACTOR;
> --- `src/core/context/corpus-segments.ts`

#### MEM-OBJ-checkpoint-manifest
Label: Checkpoint pointer manifest

Part of: [MEM-OBJ-session-checkpoints](#mem-obj-session-checkpoints)

Source-native identity: `session_context_state.checkpoint_manifest`, CheckpointLink entries containing slug, title, at, n and seg. Representational form: symbolic page references, segment hash, ordinal and time, with readable natural-language titles. Storage substrate: SQL JSONB scoped by source/client/normalized session. It is neither the raw corpus nor the extracted facts. No separate supplied object counterpart: [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) reads this part of the preserved checkpoint container. SRC-1 `src/core/context/session-state.ts`, `src/core/context/checkpoint-harvest.ts`, `src/core/context-engine.ts`.

Lineage/admission: harvest receipts retain extracted entity slugs; source-scoped getPage verifies existence and obtains titles before software appends links. No per-link human approval is established. Newest links replace older entries of the same slug and the merge caps at 20; titles collapse whitespace and cap at 300 characters. This is derived access metadata, not a transcript summary or a retained explanation of each fact. A failed manifest read aborts append rather than treating failure as empty state. FIFO receipts support republication without re-extraction; the inline fallback can lose pointers after facts are inserted.

Later consumer/authority: assemble polling uses seg to identify checkpoint completion, and later assemble/pack renders compact pointers. formatCheckpointBlock selects the first ten links and tells the host to re-pull with get_page. Symbolic metadata governs selection; titles and instruction text reach the external model through the system addition, without established compliance or full-page delivery. Rendering treats failed reads as empty. SQL row GC can age out session state (default seven days) or evict old rows above the per-client cap; full GC caller scheduling and page-deletion pointer refresh remain uninspected. Corpus-file existence alone neither ensures this manifest persists nor guarantees a surviving pointer is retrievable later.

> const page = await job.engine.getPage(slug, { sourceId: job.sourceId });
>         if (page) verified.push({ slug, title: page.title || slug });
> --- `src/core/context/checkpoint-harvest.ts`

> if (existing === null) return false;
> --- `src/core/context/session-state.ts`

> for (const l of links.slice(0, 10)) {
> --- `src/core/context-engine.ts`

#### MEM-OBJ-fact-withdrawals
Label: Withdrawal ledger

Source-native identity: `fact_withdrawals`, keyed by source, visibility, subject and fact fingerprint. Form: symbolic negative eligibility state; substrate: SQL. It retains that a matching claim was explicitly withdrawn, not its complete justification. Writers check it; source snapshot overlays and projection invalidation propagate suppression. Purge uses a distinct `fact_purges` tombstone surface whose full lifecycle is uninspected. No supplied counterpart; journal receipts are operation records, not ongoing re-admission vetoes. SRC-1 `src/core/facts/withdrawal.ts`.

> const inserted = await tx.executeRaw(`INSERT INTO fact_withdrawals(source_id,visibility,subject,fact_hash)
>       VALUES ($1,$2,$4,gbrain_fact_fingerprint($3)) ON CONFLICT DO NOTHING RETURNING fact_hash`, [sourceId,row.visibility,row.fact,row.subject]);
> --- `src/core/facts/withdrawal.ts`

#### MEM-OBJ-takes
Label: Consolidated take claims

Source-native identity: `takes`, plus contributing facts' `consolidated_into`. Form: natural-language claim and symbolic holder/kind/weight/source/time/active state; substrate: SQL, with managed publication responsibility delegated. Consolidation selects an existing highest-confidence claim, not a new LLM synthesis. Later takes_list/search retrieve eligible rows; holder visibility can keep `self` takes from particular remote consumers. Input edges and fact IDs retain derivation lineage; concatenated sessions alone are not a reasoning explanation. No supplied object counterpart; [RT-RTE-maintenance-run](runtime.md#rt-rte-maintenance-run) is its enclosing driver. SRC-1 `src/core/cycle/phases/consolidate.ts`, `src/core/ops/takes.ts`.

> const best = cluster.reduce((a, b) => (b.confidence > a.confidence ? b : a));
> const avgWeight = cluster.reduce((s, f) => s + f.confidence, 0) / cluster.length;
> const sources = Array.from(new Set(cluster.map(c => c.source_session ?? c.source).filter(Boolean))).join(',');
> --- `src/core/cycle/phases/consolidate.ts`

#### MEM-OBJ-retrieval-weights
Label: Retrieval feedback and weights

Source-native identity: `retrieval_events`, event pages/links, `retrieval_feedback`, `retrieval_weights`. Raw use-attribution records, explicit ratings and derived weights are different operative parts, now independently declared as [MEM-OBJ-retrieval-events](#mem-obj-retrieval-events), [MEM-OBJ-retrieval-feedback](#mem-obj-retrieval-feedback) and [MEM-OBJ-ranking-weights](#mem-obj-ranking-weights). This record remains their mechanism container, not a uniform object-level authority or retention classification. Form: symbolic event/client/content identities, ordinal ratings and localized numerical weights; substrate: SQL. These weights are not model parameters or dense embeddings. Rating admission binds an event and unchanged page hash; the update produces bounded weights, and later ranking reads them. The stored event/weight history retains rating attribution, not a content-directed criticism explaining why evidence failed. No supplied counterpart to [RT-RTE-query-read](runtime.md#rt-rte-query-read), which returns evidence rather than learning ranking weights. SRC-1 `src/core/feedback/rate.ts`, `src/core/feedback/store.ts`, `src/core/search/feedback-boost.ts`.

> calc AS (
>        SELECT c.*, LEAST(1, GREATEST(0, c.w_eff + $6::real * ((c.rating - 1) / 4.0 - c.w_eff)))::real AS w1
>          FROM cur c
>      ),
> --- `src/core/feedback/store.ts`

#### MEM-OBJ-retrieval-events
Label: Retrieval event attribution state

Part of: [MEM-OBJ-retrieval-weights](#mem-obj-retrieval-weights)

Source-native identity: `retrieval_events`, `retrieval_event_pages`, `retrieval_event_links`. Representational form: symbolic event/client/operation/time identity and page source/slug/hash/rank/cited or link path references. Storage substrate: SQL tables. This is raw use-attribution metadata, not query text, answer prose, rating history or derived weights. It is distinct from [RT-RTE-query-read](runtime.md#rt-rte-query-read), which returns evidence; the supplied route is not a declaration of its retained attribution state. SRC-1 `src/core/feedback/store.ts`, `src/core/feedback/rate.ts`, `src/core/schema-migrations/v207-retrieval-feedback.ts`.

Lineage: insertRetrievalEvents accepts page/link attribution from retrieval producers and inserts event and child rows idempotently. Complete producer enumeration remains uninspected. The later rating consumer reads the event, checks client ownership and compares retained page hashes to current hashes. Its authority is to bound which evidence may be rated, not to rank later queries or certify truth. Admission uses event ownership plus current teaching authority; attribution alone grants no update authority. Missing/pruned events refuse ratings. Prune deletes events older than the configured retention window, cascading to page/link rows and feedback history; derived weights have no event foreign key and can outlive the attribution. Full prune invocation and deployed retention settings remain uninspected.

> if (event.client_id !== clientId) {
> --- `src/core/feedback/rate.ts`

> if (current.get(ref) !== w.page.content_hash) { skipped.push({ kind: 'page', ref, reason: 'stale_revision' }); continue; }
> --- `src/core/feedback/rate.ts`

#### MEM-OBJ-retrieval-feedback
Label: Admitted retrieval feedback history

Part of: [MEM-OBJ-retrieval-weights](#mem-obj-retrieval-weights)

Source-native identity: `retrieval_feedback`, keyed by event, signal, element kind, source and element key. Representational form: symbolic attribution and signal, ordinal 1–5 rating, localized numerical before/after weights and application time. Storage substrate: SQL rows, not model parameters. Lineage: [MEM-RTE-feedback-update](#mem-rte-feedback-update) admits caller ratings under ownership, source teaching, content revision, feature and rate-limit checks. Human versus computational rater remains unresolved. The schema also permits cited signals; their producers and admission remain untraced. No supplied object counterpart; this history is not the evidence rows of [RT-RTE-query-read](runtime.md#rt-rte-query-read). SRC-1 `src/core/feedback/store.ts`, `src/core/feedback/rate.ts`, `src/core/schema-migrations/v207-retrieval-feedback.ts`.

Authority/consumers: newly inserted rows authorize a weight update within the same SQL statement. Conflict/no-new-row does not compound weights. Later retries read history to report already-applied outcomes, and admission counts recent explicit rating calls from it. Ranking reads weights instead of these rows. The rating records an outcome signal, not reasons, expected-answer evidence or content-directed criticism. Event deletion cascades to this history; surviving weights can therefore no longer have their complete attribution reconstructed from retained history. No independent feedback-history lifetime or GC scheduling guarantee is established.

> INSERT INTO retrieval_feedback
>          (event_id, signal, element_kind, source_id, element_key, client_id, rating, weight_before, weight_after)
>        SELECT $7, $8, element_kind, source_id, element_key, $9, rating, w_eff, w1 FROM calc
>        ON CONFLICT DO NOTHING
>        RETURNING element_kind, source_id, element_key, rating
> --- `src/core/feedback/store.ts`

> CREATE TABLE IF NOT EXISTS retrieval_feedback (
>         event_id       TEXT NOT NULL REFERENCES retrieval_events(id) ON DELETE CASCADE,
> --- `src/core/schema-migrations/v207-retrieval-feedback.ts`

#### MEM-OBJ-ranking-weights
Label: Derived retrieval ranking weights

Part of: [MEM-OBJ-retrieval-weights](#mem-obj-retrieval-weights)

Source-native identity: `retrieval_weights`, keyed by source_id, element_kind and element_key, with weight, content_hash, updates and updated_at. Representational form: localized bounded numerical state and symbolic element/revision keys; neither dense embeddings nor chat-model weights. Storage substrate: SQL. Lineage: admitted feedback drives a bounded moving-average update from neutral 0.5, rather than retaining a claim or full criticism. Distinct from [RT-CMP-reranker-model](runtime.md#rt-cmp-reranker-model), an external model whose scores this local stage can reorder. SRC-1 `src/core/feedback/store.ts`, `src/core/search/feedback-boost.ts`, `src/core/schema-migrations/v207-retrieval-feedback.ts`.

Later consumer/authority: hybrid applyFeedbackStage reads page weights and applies a fixed multiplier to the ordering score after reranking, preserving raw score/rerank_score. This is the positive trace-fed behavior-shaping result in [MEM-BAP-ranking-weights](#mem-bap-ranking-weights), not authority belonging to raw events or rating history. Model compliance is unnecessary for this numerical selector, but no actual ranking run or benefit was observed. Link-weight consumer remains untraced. Changed page hashes halve the effective deviation from neutral at read/update rather than deleting the row. Disabled/zero influence bypasses the effect; read failure leaves ranking unchanged.

Retention/recovery: weights are independent of event/history pruning. Source deletion cascades via their source foreign key; prune removes missing page/link targets, and resetRetrievalWeights deletes all or scoped rows. These are source-inspected capabilities; reset authority, cleanup scheduling and deployed horizons remain uninspected. Absence reads as neutral, not restored historical attribution. Reasons do not reach this later ranking consumer.

> LEFT JOIN retrieval_weights w
>          ON w.source_id = p.source_id AND w.element_kind = 'page' AND w.element_key = p.slug
> --- `src/core/search/feedback-boost.ts`

> if (influence <= 0) return results;
> --- `src/core/search/feedback-boost.ts`

### Routes

#### MEM-RTE-remember-write
Label: Explicit fact write

Caller proposes one claim with mandatory provenance, optional entity/TTL/replacement and default world visibility. The verb validates inputs, submits a journaled mutation, and preparation chooses duplicate, insert or supersession. Software checks withdrawal, candidate state, embedding configuration, trust and write gate. Lower-tier supersession becomes a contested insert. Human authorship or review is unresolved; trusted local access is not per-content approval. Operating mode: open knowledge request, no answer oracle. Publication/recovery inherits the supplied coordinator protocol, not a truth test. Distinct from page capture: its proposed state is a fact and optional entity fence. SRC-1 `src/core/verbs.ts`, `src/core/persistence/memory-prepare.ts`; compare [RT-RTE-capture-write](runtime.md#rt-rte-capture-write).

- Immediate return: inserted/duplicate/superseded outcome, IDs and notices, or held/refused/pending receipt.
- Later read-back: SQL fact claims and optional fences reach recall, context packs, page readers and consolidation.
- Delegated visibility: source authority and remote/private constraints apply; default world is not default private extraction.
- Selection predicate: explicit entity/replaces, active candidate dedup and current page identity/revision; inferred linking does exact-text dedup rather than semantic supersession.
- Invalidation or expiry: TTL, supersession, withdrawal and live publication checks can remove eligibility or refuse publication.
- Activation or effect: inserts knowledge state or no-op duplicate; contested/held results do not imply canonical acceptance of the claim.
- Evidence limits: admission, entity resolution and embedding/dedup helpers not fully audited; no truth or exercised-use guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (gate.action === 'reject') throw writeGateRejectedError(gate.assessment);
> if (gate.action === 'hold') return { observedRevision, validate, apply: async tx => heldOutcome(gate.assessment, (await recordWriteGateHold(tx, gate.hold!)).holdId) };
> --- `src/core/persistence/memory-prepare.ts`

#### MEM-RTE-extraction-write
Label: Automatic extraction write

Producer pipeline converts page or turn text to candidate facts using configured chat inference, entity resolution, capture dedup and managed or legacy publication. It bounds and sanitizes input, skips dream-generated input, and selects notability admission. Software/provider outputs decide candidate admission; no mandatory human approval is established. Guidance is the extractor system/variant/operator appendix, not a retained explanation for each inferred fact. Operating mode: extraction request, no reference-answer oracle. Failure/refusal/schema/transport outcomes differ; provider failures can retry rather than silently claim zero success. This is a transformation beyond [RT-RTE-maintenance-run](runtime.md#rt-rte-maintenance-run), not a duplicate of that driver. SRC-1 `src/core/facts/extract.ts`, `src/core/facts/backstop.ts`.

- Immediate return: real counts/IDs and skipped or failure reason, or durable queued work in queue mode.
- Later read-back: derived facts become recall/pack candidates; successfully fenced entity slugs can become checkpoint links.
- Delegated visibility: explicit visibility wins, otherwise extraction resolves operator default fail-closed to private; source/session and derivation trust are carried.
- Selection predicate: capped turn text, anti-dream flag, availability/kill switch, notability, entity resolution and duplicate checks; initial trace origin can mix user, assistant and tool material and is not inferred from hook labels.
- Invalidation or expiry: withdrawal and write gates can suppress/reject; managed replay binds retained extraction; full rollback and retry guarantees remain uninspected.
- Activation or effect: model-authored derived text can become retained knowledge; DB-only fallback exists when no usable fence target is available.
- Evidence limits: no actual extraction observed; complete origin/role filters, managed publication and caller consent policies uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const visibility = ctx.visibility ?? (await resolveDefaultVisibility(ctx.engine));
> // #5888: one exact-duplicate check for the capture lanes, before either writer.
> const { facts, dropped } = await dedupCapturedFacts(ctx, await inferMissingSubjects(ctx, outcome.facts, visibility, input.pageSlug, managed), visibility, resolveEntitySlugWithSource);
> if (!managed) await assertAmbientCaptureAdmissible(ctx.engine, ctx.source);
> if (managed) return withCaptureDrops(dropped, facts.length || !dropped.length ? await publishManagedFacts(ctx.engine, managed, ctx, facts, visibility, input.pageSlug) : null);
> --- `src/core/facts/backstop.ts`

#### MEM-RTE-recall-delivery
Label: Requested fact and page recall

Caller triggers recall; handler selects fact arms and optional page-search arm, applies eligibility/redaction, packs and returns evidence. Distinct from [RT-RTE-query-read](runtime.md#rt-rte-query-read): fact rows and supersession/entity/session/question selection are operative here, although the page-search machinery overlaps. SRC-1 `src/core/ops/facts.ts`.

- Immediate return: fact text, attribution/status/date/trust fields, optional page evidence and budget/degradation metadata.
- Later read-back: previously admitted facts/fences/pages are retrieved; raw audit checkpoint rows are excluded, not treated as user knowledge.
- Delegated visibility: federated granted sources fan out; remote callers receive world-only facts with private-provenance exclusion and eligibility policy.
- Selection predicate: question ranking or supersessions/since/entity/session/recent branches; query optionally adds page search. Default budget packing prices facts first, query_first prices results first.
- Invalidation or expiry: active-only default and trust filters constrain eligibility; include-expired/supersessions intentionally expose history. Cache invalidation internals remain uninspected.
- Activation or effect: delivers evidence to requesting agent/operator; final answer, tool use or model compliance is not established.
- Evidence limits: question ranking and hybrid internals not fully read; token estimate is not exact provider accounting and metadata overhead is not proven fully budgeted.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const view = redactRetrievalOutput([{ facts: rows.map(r => ({ fact: r.fact, context: r.context, source: r.source })), results: searchResults }], {}).results[0];
> searchResults = view.results;
> if (ctx.remote !== false) rows = rows.map((r, i) => ({ ...r, ...view.facts[i] }));
> --- `src/core/ops/facts.ts`

#### MEM-RTE-context-pack
Label: Boundary context pack

Explicit tool call or shipped hook IPC triggers deterministic assembly of core text, entity cards/open threads, facts and optional newer mentions/pinned answers. This is not full-page reading. It is distinct from OpenClaw assemble's returned host prompt addition, though both can call related context machinery. SRC-1 `src/core/ops/facts.ts`, `src/commands/hook.ts`; compare [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly).

- Immediate return: structured cards/facts/threads and injectable text with budget and core metadata.
- Later read-back: persisted entity and hot-fact state reaches a later session-start/post-compaction invocation.
- Delegated visibility: private data requires explicit trusted-local opt-in; proactive eligibility and authorized quarantine request govern delivery.
- Selection predicate: up to eight explicit entity names/slugs, source, since and session; core packs first, then cards/threads, facts and newer mentions.
- Invalidation or expiry: source eligibility, suppression and core withdrawal snapshot handling apply; pinned-answer freshness implementation uninspected.
- Activation or effect: session-start hook can inject pack text without a model-originated retrieval call; explicit calls remain requested delivery.
- Evidence limits: core is reserved before item packing and may itself exceed a smaller caller token budget; no universal exact-budget guarantee. IPC consumer and pinned-answer writer not fully audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const itemBudget = budgetTokens - packHeaderCost() - coreTokens;
> const cardCost = (c: (typeof cards)[number]) =>
>   lineCost(renderCardLine(c)) + threadsOf(c).reduce((n, t) => n + lineCost(renderThreadLine(t)), 0);
> --- `src/core/ops/facts.ts`

#### MEM-RTE-delta-delivery
Label: Incremental delta delivery

Caller supplies a cursor/since or established session; handler selects newer page/fact context and persists delivery position. Cursor state is access metadata, not learned claim text. No supplied exact counterpart: [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) describes a different host callback. SRC-1 `src/core/ops/facts.ts`.

- Immediate return: incremental context plus next_cursor and separate cursor-arm metadata, or typed retry/degradation notice.
- Later read-back: later wake reads retained delivery position and changed knowledge since it; stateless callers must carry returned cursor.
- Delegated visibility: source/client/session namespace separates trusted-local, authenticated remote and shared unauthenticated remote sentinel; private opt-in is local-only.
- Selection predicate: explicit opaque cursor overrides both arms; otherwise explicit since or saved session state; budget caps delivered items.
- Invalidation or expiry: failed session-state read refuses rather than initializing a new cursor; incomplete delivery holds position. Session GC policy not fully read.
- Activation or effect: changes future delivery selection, not fact meaning; exact same-timestamp paging uses fact IDs in opaque cursor.
- Evidence limits: assembler, cursor advancement and GC internals not exhaustively traced; no universal no-loss guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> throw sessionUnavailableError(ctx, bumpLocalDegraded(sourceId, clientId, sessionId, true) >= DELTA_ESCALATE_AFTER, retryArgs);
> --- `src/core/ops/facts.ts`

#### MEM-RTE-core-delivery
Label: Designated core delivery

Owner-designated pages carry always_load/core_priority. Enabled core loads default plus session source inside allowed sources; it selects eligible, unsuppressed pages, applies sensitivity policy and renders title plus compiled truth. This is independently supplied knowledge/instruction text, not query-targeted retrieval. Core marking is owner-plane controlled, but remote content edits may pass under notify policy without prior review. Software rejects disallowed marking/deletion/edit and growth beyond budget; shrinking writes can pass. Open content editing mode, no answer oracle; journal publication supplies recovery. Distinct selector within [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), also used by packs. SRC-1 `src/core/core-memory.ts`, `src/core/persistence/core-guard.ts`.

- Immediate return: core block, rendered-page inventory, omissions, notices and revision; disabled returns no text.
- Later read-back: designated retained page content is loaded on later assembly/pack/session-start delivery.
- Delegated visibility: default/session source intersection with allowed sources; private and quarantine/trust filtering, activation suppression and sensitivity withholding/redaction precede rendering.
- Selection predicate: always_load true, source, positive priority then slug; whole pages fit character budget and page cap. Default enabled is false, default character budget 4000, permitted configuration 500–6000.
- Invalidation or expiry: page deletion, withdrawal-aware canonical snapshot, trust/suppression, sensitivity and disabled setting can remove delivered text; visible changes alter core revision.
- Activation or effect: natural-language knowledge/instructions enter host prompt lanes; downstream compliance is external. Owner-only marking does not mean every delivered edit was human-approved.
- Evidence limits: all compiled-file lanes and unmanaged bypasses not audited; character budget is not enclosing model token budget.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!settings.enabled) {
>     return { text: '', chars_used: 0, chars_limit: settings.maxChars, pages: [], truncated: false, omitted: [], revision: 'disabled', enabled: false };
>   }
> --- `src/core/core-memory.ts`

#### MEM-RTE-checkpoint-harvest
Label: Compaction checkpoint harvest

OpenClaw compact callback triggers bounded transcript-tail rendering and spool-first banking before delegated compaction. Corpus is retained before fact extraction; capability/consent/source/kill-switch gates may leave only banked raw material. Serve FIFO harvesting and direct inline fallback have different link-retry contracts. Automatic model extraction proposes derived knowledge; software verifies entity-page existence before manifest links. No mandatory per-fact human approval or answer oracle; open trace harvest under extractor guidance. It complements rather than duplicates [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), which is the later consumer. SRC-1 `src/core/context-engine.ts`, `src/core/context/checkpoint-harvest.ts`, `src/core/context/session-state.ts`.

- Immediate return: banked/harvested/skipped checkpoint metadata attached to delegate result, not a guaranteed completed extraction.
- Later read-back: corpus can be harvested by sweep; derived facts reach recall; manifest is later rendered into assemble/pack pointers and get_page instructions.
- Delegated visibility: source stamp/incarnation and sanitized session identity bind harvest; direct fallback explicitly invokes pipeline remote false. Full raw capture consent and sensitivity policy remain uninspected.
- Selection predicate: transcript boundary window and configured turn cap, segment hash/claim/ingested state, extraction availability and consent; display selects first ten manifest links.
- Invalidation or expiry: abort/deadline can leave banked retryable material; FIFO receipt replay can repair manifest without re-extraction. Inline fallback marks ingested even after manifest failure, so links are best effort there.
- Activation or effect: trace → rendered corpus → derived facts/fences → verified manifest → pointers in later system addition. Instruction says trust links over compaction summary; this does not demonstrate retrieval or correct recall.
- Evidence limits: original host summary is external and alternative corpus adapters are untraced; no claim of lossless reconstruction, universal receipt retry or complete cleanup.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> lines.push(
>     'Checkpoint saved to the brain at compaction; facts harvested moments later — ' +
>     're-pull with get_page. Trust these links over the compaction summary.',
>   );
> --- `src/core/context-engine.ts`

#### MEM-RTE-fact-withdrawal
Label: Fact withdrawal propagation

Forget reaches a software-controlled source/visibility/subject-specific withdrawal transaction. It expires matching claims, records negative eligibility and invalidates affected page projections/chunks; it can queue semantic review and mirror/git/embedding effects. Caller chooses withdrawal, but human intent is not inferable from agent-facing request. No truth oracle; open withdrawal request. Transaction and mirror/rebuild machinery coordinate persistence; complete rollback/recovery beyond inspected transaction is uninspected. Distinct from [RT-RTE-capture-write](runtime.md#rt-rte-capture-write): this changes negative eligibility, not merely page text. SRC-1 `src/core/facts/withdrawal.ts`, `src/core/core-memory.ts`.

- Immediate return: withdrawn flag and affected page revisions at the transaction helper; facade receipt shape not fully traced.
- Later read-back: writers reject matching withdrawn claims; snapshot overlays and core reads suppress stale fences; explicit supersession/history reads may expose prior state.
- Delegated visibility: source and visibility partition withdrawals; entity-bound claims withdraw that subject, subjectless claims use wildcard subject.
- Selection predicate: normalized fingerprint plus scope/subject, discovered affected pages and locked fact/page state.
- Invalidation or expiry: bumps knowledge_revision, clears text projection/embedding signature and deletes affected chunks; expiry retains history rather than physical deletion.
- Activation or effect: prevents exact-claim re-admission and invalidates derived candidates. New wording is a documented countercase; semantic review completion is not established.
- Evidence limits: discovery/overlay completeness, paraphrase review, previously delivered/downloaded bytes and all projections untraced; no universal erasure claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> export const FACT_WITHDRAWN_SUGGESTION = 'A forgotten claim stays withdrawn, and remembering the same text again is refused; '
>   + 'a claim forgotten without an entity is withdrawn for every entity. If it is still true, remember it in new words. '
>   + 'To link a fact saved without an entity, do not forget it: remember it with entity and replaces set to its fact id.';
> --- `src/core/facts/withdrawal.ts`

#### MEM-RTE-facts-consolidation
Label: Fact cluster consolidation

Part of: [RT-RTE-maintenance-run](runtime.md#rt-rte-maintenance-run)

This phase is a transformation inside the maintenance driver's cycle action. Software scans unconsolidated active entity facts asserted by user or without speaker; default bucket count is three, oldest age 24h, candidate cap 100. It separates external/owner trust groups, checks compatible claims and clusters by cosine. Highest-confidence existing text becomes a self-held take. Managed maintenance publication or attributed legacy transaction decides admission; write gates can hold/reject. No per-cluster human approval, no reference-answer oracle; deterministic promotion under fixed executable rules, not model criticism. Dry-run previews bounded clusters. SRC-1 `src/core/cycle/phases/consolidate.ts`, `src/core/ops/takes.ts`.

- Immediate return: phase counts and preview/failure report.
- Later read-back: take rows reach takes_list/search and other eligible takes consumers; facts retain consolidated_into lineage, and temporal validity changes affect future fact reads.
- Delegated visibility: managed path selects world facts; self holder is not universally remote-readable. Dry-run private text requires trusted-local remote false.
- Selection predicate: bucket/age/active/speaker gates, vector threshold and typed-claim/date/amount compatibility; existing retired take prevents resurrection.
- Invalidation or expiry: contributing facts are marked consolidated, older cluster facts receive valid_until; existing resolved take stays immutable. Abort returns partial committed work rather than all-run rollback.
- Activation or effect: writes derived claims and lineage and updates later eligibility; no new LLM summary or semantic warrant follows from the name consolidation.
- Evidence limits: managed publication and all downstream synthesis consumers not fully traced; no improved-capacity evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (gate && gate.action !== 'insert') { if (gate.action === 'hold') clustersGateHeld++; else clustersGateRejected++; continue; }
> --- `src/core/cycle/phases/consolidate.ts`

#### MEM-RTE-feedback-update
Label: Rating-driven retrieval update

Client proposes a 1–5 rating for a recorded answer or named pages. Software requires enabled learning, event ownership, rate cap, teaching authority, revision identity and idempotent targets. It writes rating attribution and bounded page/link weights. Guidance is the rating scale and fixed update equation; no content criticism or expected-answer oracle is supplied by the rating itself. Human versus computational rater is unresolved; mode is open explicit feedback, not a controlled experiment. No supplied duplicate: [RT-RTE-query-read](runtime.md#rt-rte-query-read) supplies evidence, this route retains outcome-derived ranking state. SRC-1 `src/core/feedback/rate.ts`, `src/core/feedback/store.ts`, `src/core/search/feedback-boost.ts`, `src/core/search/hybrid/rank.ts`.

- Immediate return: applied/skipped targets, before/after weights, multiplier and next-search guidance.
- Later read-back: applyFeedbackStage reads retrieval_weights on later hybrid rank calls; stored event is attribution, weight is derived behavior-shaping memory.
- Delegated visibility: same client owns answer; teaching source requires authority stronger than simply reading evidence; arbitrary out-of-answer page ratings refuse.
- Selection predicate: targeted pages or cited think/synthesize pages, otherwise returned pages, plus used path links for whole-answer ratings; only current matching hashes admit page update.
- Invalidation or expiry: event retention can make rating unavailable; changed content refuses stale rating and halves old weight's deviation from neutral at ranking/update. Full reset/GC scheduling uninspected.
- Activation or effect: fixed multiplier reorders actual ordering scores after reranking; raw scores stay unchanged and failures leave list untouched. Later ranking dependence is wired, not observed benefit.
- Evidence limits: link-weight consumer and implicit signals untraced; no exercised learning, causal quality or content-directed theory revision established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const ordered = await applyFeedbackStage(engine, reranked, { reranked: reranked !== deduped });
> --- `src/core/search/hybrid/rank.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-ranking-weights
Label: Retained ranking weight authority

Consumer: hybrid retrieval ranking stage. Channel: SQL-derived per-page weight through fixed multiplier on ordering key. Force: symbolic/numerical reranking, not language-model obedience or a modification of stored knowledge text. Horizon: later retrieval calls while weight and feature remain enabled. Distinct from [RT-BAP-context-addition](runtime.md#rt-bap-context-addition), which supplies text to a model. Implementation is wired; operation and benefit uninspected. SRC-1 `src/core/search/feedback-boost.ts`.

> const m = feedbackMultiplier(weight, influence);
> r.feedback_boost = Math.round(m * 10_000) / 10_000;
> boosted++;
> return { r, index, key: base >= 0 ? base * m : base / m, scored: true };
> --- `src/core/search/feedback-boost.ts`

## Annotations

#### On [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly)

Memory-specific read-back: core is optional and disabled by default, delivers compiled truth rather than timeline, and applies withdrawal/sensitivity/trust filters. Checkpoint supply is a manifest of verified entity pointers; it is not the raw segment or full harvest. Added producer lineage is [MEM-RTE-checkpoint-harvest](#mem-rte-checkpoint-harvest). SRC-1 `src/core/core-memory.ts`, `src/core/context-engine.ts`; supporting passages retained in those records. Budget is separate core characters and compact link cap, not established enclosing token accounting. Authority remains natural-language system addition interpreted by the external host model.

#### On [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop)

Supplied evidence establishes raw assistant/tool replay state retained in SQL and consumed on later job resumes. This is recovery/context memory, not evidence of extraction into improved strategies. Opaque provider internal state remains uninspected; readable replay blocks are not proof of provider-native state persistence. No new source inspection or broader retention conclusion. SRC-1 `src/core/minions/handlers/subagent.ts`, `src/core/ai/gateway.ts`; passage and durability limits are in the supplied record.

#### On [RT-OBJ-shared-skill-heads](runtime.md#rt-obj-shared-skill-heads)

Catalog heads are symbolic selection state; linked instruction bodies and assets have separate interpretive/execution consumers. Editing/publishing authority is not downstream activation. The supplied record establishes revision storage, while host installation/follow behavior, trace-fed optimization and retained optimization reasons remain uninspected. SRC-1 `src/core/shared-skills/publication.ts`, `src/core/ops/skills-catalog.ts`; use supplied passage, not a new activation assertion.

#### On [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model)

Extraction calls the gateway with independently selected facts.extraction_model/per-call override and operator prompt appendix; chat availability is checked against that selected model. Input is capped at 8000 characters and dream-generated flag skips extraction. This is inference transforming retained input; no operational parameter update or exact weight identity is established. SRC-1 `src/core/facts/extract.ts`.

> if (input.isDreamGenerated) return { ok: true, facts: [] };
> if (!input.turnText) return { ok: true, facts: [] };
> --- `src/core/facts/extract.ts`

## Write side

Acquisition is caller-supplied text for explicit capture/remember, or rendered retained page/conversation material for extraction. [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) establishes durable intent admission and publication; [MEM-RTE-remember-write](#mem-rte-remember-write) adds semantic fact decision and optional fence. The software authority checks decide whether a caller can publish, not whether a claim is true. Initial human control over existing corpora is unresolved. Subsequent executable transformations remain established despite that unknown.

Automatic extraction's raw-to-derived chain is [MEM-RTE-extraction-write](#mem-rte-extraction-write). It may retain attribution, confidence and entity-inference notes, but no full model reasoning or guaranteed reasons for every candidate. Compaction additionally retains rendered corpus and manifests with separate recovery contracts; a banked result does not imply extracted facts, and derived DB-only facts do not necessarily yield manifest links. [MEM-RTE-checkpoint-harvest](#mem-rte-checkpoint-harvest).

Maintenance is not one uniform curation policy. Consolidation performs deterministic existing-claim selection and temporal writes, with gates and retired-claim handling, not generated synthesis. Other synthesis/pattern/concept/skillopt paths stay separately unresolved in the coverage inventory. The phase table distinguishes grade_takes cached verdicts from opt-in resolutions and skillopt files/proposals from DB writes. Those labels do not establish their meaning or approval. SRC-1 `src/core/cycle/phase-table.ts`; [MEM-RTE-facts-consolidation](#mem-rte-facts-consolidation).

Rejection can retain control evidence without admitting knowledge: remember hold records, contested facts, expiry, and withdrawal ledgers have different consequences. Forget is not purge. Purge's local handler rejects remote callers, plans targets, provides dry-run receipt/token and requires matching confirmation; this proves software confirmation, not that a human reviewed it. Its deletion inventory and physical residuals remain uninspected. SRC-1 `src/core/ops/purge.ts`, `src/core/facts/purge.ts`.

> if (ctx.remote !== false) throw purgeHostOnly(params.id);
> assertPersistenceAccepting(ctx.engine);
> await initializeLocalPersistence(ctx);
> --- `src/core/facts/purge.ts`

Feedback is a second raw-to-derived path: attributed event plus admitted rating → feedback history and weights → later ranking. Reasons are not part of the numeric rating input, and no later criticism reader is established. This is a trace-fed ranking update, not merely raw logging and not proof of better retrieval. [MEM-RTE-feedback-update](#mem-rte-feedback-update), [MEM-BAP-ranking-weights](#mem-bap-ranking-weights).

## Read-back

Requested routes include query/image evidence from the supplied runtime, recall facts/pages, explicit context_pack and delta, takes_list/search, and get_skill/assets. They have different selectors and authority: recall is evidence supply, delta state shapes future delivery, and ranking weights directly change ordering. A storage API alone is not asserted to activate a host. [RT-RTE-query-read](runtime.md#rt-rte-query-read), [MEM-RTE-recall-delivery](#mem-rte-recall-delivery), [MEM-RTE-delta-delivery](#mem-rte-delta-delivery), [RT-RTE-skill-publication](runtime.md#rt-rte-skill-publication).

Independent push supply is shipped SessionStart IPC/output composition and OpenClaw assemble. Source search in `src/commands/hook.ts` identifies requestContextPack, acceptance of returned text and composeSessionStartOutput. Full hook deadline/fallback behavior remains uninspected. Core is designation-based; entity cards are bounded summaries; checkpoint lines instruct re-pull. None proves complete-page delivery or compliant host retrieval. SRC-1 `src/commands/hook.ts`, `src/core/context-engine.ts`, `src/core/ops/facts.ts`; [MEM-RTE-context-pack](#mem-rte-context-pack), [RT-BAP-context-addition](runtime.md#rt-bap-context-addition).

Source trust is both filtering and labeling. Recall resolves eligibility before source fan-out, and output includes trust/provenance/date fields after redaction. Core suppresses activation-flagged pages and sensitivity hits. These are consumer-time controls, not proof of truth, semantic completeness or reliable injection resistance. For withdrawal, core consults snapshot when ledger indicates affected subject/source, so an old stored compiled_truth is not blindly treated as eligible. SRC-1 `src/core/core-memory.ts`, `src/core/ops/facts.ts`.

> if (r.withdrawn) {
>       const snap = await exec.readPageSnapshot(r.slug, { sourceId: r.source_id, ...(opts.excludePrivate ? { excludePrivate: true } : {}) });
>       if (!snap) continue;
>       compiled = snap.page.compiled_truth ?? '';
>     }
> --- `src/core/core-memory.ts`

## Integration issues

- The checkpoint and feedback containers previously named operative parts without declaring them independently. This correction preserves both containers and all supported route findings, and adds containment declarations for [MEM-OBJ-checkpoint-corpus](#mem-obj-checkpoint-corpus), [MEM-OBJ-checkpoint-manifest](#mem-obj-checkpoint-manifest), [MEM-OBJ-retrieval-events](#mem-obj-retrieval-events), [MEM-OBJ-retrieval-feedback](#mem-obj-retrieval-feedback) and [MEM-OBJ-ranking-weights](#mem-obj-ranking-weights). Corpus and manifest have different stores, recovery and consumers. Events and history can expire while derived weights survive; only weights have the established later ranking authority. Reconciliation can resolve the named missing-part conflicts without discarding the positive harvest/ranking findings. The parts are contained in exactly one local object each, not replacements or possible duplicates of supplied runtime records.
- No supplied fact was found requiring reversal. Runtime's uninspected checkpoint/core/consolidation fields are now partly resolved, not silently treated as erroneous. Integrate [MEM-RTE-checkpoint-harvest](#mem-rte-checkpoint-harvest), [MEM-RTE-core-delivery](#mem-rte-core-delivery) with [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly); producer/selector and host callback are distinct.
- Recall's page-search arm overlaps [RT-RTE-query-read](runtime.md#rt-rte-query-read), but [MEM-RTE-recall-delivery](#mem-rte-recall-delivery) additionally owns fact-arm selection. No identical-route duplicate is asserted. Packs and deltas are separate operations, not aliases for context assembly.
- Remember shares coordinator admission with [RT-RTE-capture-write](runtime.md#rt-rte-capture-write), but targets fact decisions/fences rather than capture pages. [MEM-RTE-facts-consolidation](#mem-rte-facts-consolidation) is explicitly a material phase part of the maintenance route, not a replacement for it.
- Core owner designation is not prior human approval of every content edit: notify allows software publication followed by review notice. Default disabled and omission/filtering qualify “always loaded.” SRC-1 `src/core/core-memory.ts`, `src/core/persistence/core-guard.ts`; [MEM-RTE-core-delivery](#mem-rte-core-delivery).
- Checkpoint FIFO receipt retry and direct fallback's best-effort manifest differ. Inline marks ingested even after manifest failure. Prevent universal claim that every retained fact yields a reliable future checkpoint pointer. SRC-1 `src/core/context-engine.ts`, `src/core/context/checkpoint-harvest.ts`; [MEM-RTE-checkpoint-harvest](#mem-rte-checkpoint-harvest).
- Session metadata loses fidelity through fence rebuild according to the operation contract; complete cross-rebuild session recall is unsupported. SRC-1 `src/core/ops/facts.ts`; [MEM-OBJ-fact-metadata](#mem-obj-fact-metadata).
- Withdrawal is fingerprint-scoped; differently worded claims and semantic review remain unresolved. Purge controls are inspected but its sweep and residual verifier are not. Prevent semantic-erasure and all-consumer suppression claims. SRC-1 `src/core/facts/withdrawal.ts`, `src/core/facts/purge.ts`; [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal).
- Rating history and ranking weights have a positive later consumer witness; do not classify the system's trace updates solely from raw subagent logs. Link weighting, implicit signals, probes, optimization and resulting benefit remain unresolved. SRC-1 `src/core/search/hybrid/rank.ts`, `src/core/feedback/store.ts`; [MEM-RTE-feedback-update](#mem-rte-feedback-update), [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop).
- Remaining included mechanisms are the unresolved rows of the coverage table: pinned answers, synthesis/pattern/concept production, skillopt, evaluators, compiled instruction files, connector/drain initialization and full purge/GC propagation. Their available source was not exhausted; missing evidence prevents complete lifecycle, theory/learning and universal authority assessment, not the bounded positive findings above.

## Limitations and checks

The analysis used direct bounded reads/searches of SRC-1 plus the supplied boundary/runtime members and explicitly supplied previous memory output/refusal. Correction reads added bounded `src/core/context/corpus-segments.ts` renderer/write/GC, `src/core/context/session-state.ts` manifest/GC, `src/core/context/checkpoint-harvest.ts` receipt-publication, `src/core/context-engine.ts` pointer rendering, `src/core/feedback/store.ts` insertion/update/read/prune/reset, `src/core/feedback/rate.ts` and `src/core/search/feedback-boost.ts`, plus `src/core/schema-migrations/v207-retrieval-feedback.ts` schema. These are implementation evidence, not execution. The source identity and clean tree were rechecked at the same commit. A correction search used a nonexistent migrations glob and returned exit 2 while identifying the existing migration; the migration was then read directly. No finding relies on the failed glob. Identity and clean-tree checks matched the frozen boundary. One scoped search referenced nonexistent `src/core/ops/knowledge.ts` and returned exit 2; no finding relies on that nonexistent path, and required searches were rerun against existing paths. No target commands, tests, examples, providers or services were executed.

No observed-run or causal evidence supports host compliance, semantic quality, successful learning, deployment-level safety or improvement. Untraced available files stay explicit uncertainties. Quotations establish source occurrence, not semantic correctness or complete coverage. Deterministic validation: this correction's required role-memory command passed with “Member content check passes; invocation residue not checked.” Validation establishes form and quotation occurrence only, not claim support or job acceptance.
