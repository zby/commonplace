---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Cludebot memory: retained content, retrieval-state feedback, three distinct dream implementations, prompt consumers and withdrawal limits."
run-id: AAS-2026-10-15-cludebot-cb70d11d215b-01
source-identity: "https://github.com/sebbsssss/cludebot"
reviewed-boundary: "cecf234f10397b1e21dec2ff65ded864982f3564"
---

# Cludebot memory report

## Boundary and evidence

This report covers Clude's retained content and selection state at SRC-1, commit cecf234f10397b1e21dec2ff65ded864982f3564. It includes the shipped consumers, not just the SDK. The supplied [boundary](boundary.md#boundary-and-evidence) fixes a whole-system boundary; the supplied [runtime account](runtime.md#runtime-account) is provisional evidence of wiring, not an exhaustive memory inventory. Direct reads below extend that inspection at the same commit. HEAD was rechecked and the source working tree was clean. Only implementation and doctrine/design evidence is used. No target execution, tests, provider calls, deployment state or independent benchmark reproduction was inspected.

Memory scope includes database rows, local JSON and SQLite stores, generated semantic/procedural/self-model/introspective content, embeddings and graph/access state, conversation history, and persistent export/instruction surfaces. Transient prompt strings and task frames are included as working-context controls, not mislabeled persistent memory. External model weights, host prompt-loading behavior and actual service/chain state are opaque dependencies. Static shipped instructions are policy rather than accumulated experience. Promotional assets and workstation metadata remain excluded as in the boundary. Available but unread included paths remain explicit limits, not absences.

### Coverage inventory

“Direct” means source text or named symbol/control ranges read in this job. “Supplied” means the cited runtime record supplies the trace and passage. The rows retain unresolved alternatives rather than assuming parity from names.

| Entry point / memory operation | Source path and inspection | Coverage / prevented conclusion |
|---|---|---|
| Authenticated chat, guest counterpath, history fitting and asynchronous exchange storage | Supplied `apps/server/src/routes/chat.routes.ts`; direct `apps/server/src/lib/memory-prompt.ts` | [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-guest-chat](runtime.md#rt-rte-guest-chat), annotation below. No observed activation or strict tokenizer/latest-turn guarantee. |
| SDK/MCP store, recall, summary/hydrate, tool update/delete | Supplied SDK; direct dispatch ranges in `packages/brain/src/mcp/server.ts`, `packages/brain/src/memory/memory.ts` | [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), [MEM-RTE-recall-selection](#mem-rte-recall-selection), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal). SDK caller identity does not establish human approval. |
| JSON local mode | Direct store/recall/clinamen/delete ranges in `packages/brain/src/mcp/local-store.ts` | [MEM-OBJ-local-store](#mem-obj-local-store); no PostgreSQL decay/encryption parity. Remaining update details not audited. |
| SQLite mode and CLI dream | Direct `packages/brain/src/storage/sqlite-store.ts` store/recall/queue ranges; full `packages/brain/src/storage/dream-engine.ts`, `packages/brain/src/cli/dream.ts` | [MEM-OBJ-sqlite-store](#mem-obj-sqlite-store), [MEM-RTE-local-dream](#mem-rte-local-dream). Queue results are not shown adopted as recallable memory. |
| Main dreams: consolidation, compaction, reflection, contradiction, procedural extraction | Supplied consolidation/orchestration; direct bounded phase bodies in `packages/brain/src/memory/dream/cycle.ts` | [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle), [MEM-RTE-dream-compaction](#mem-rte-dream-compaction), [MEM-RTE-belief-revision](#mem-rte-belief-revision). Emergence publication details remain supplied/partial, not a complete consumer audit. |
| Hosted dreams | Direct agent processing body in `packages/brain/src/memory/hosted-dreams.ts` | [MEM-RTE-hosted-dream](#mem-rte-hosted-dream); owner-scoped semantic/procedural generation, not main-cycle parity. Scheduler details are supplied/search coverage. |
| Action/outcome strategies | Direct refinement/generation/reinforcement body and symbol inventory in `packages/brain/src/memory/action-learning.ts` | [MEM-RTE-strategy-refinement](#mem-rte-strategy-refinement). Original action/outcome instrumentation and social metric acquisition were not fully traced, so causal attribution to a recalled strategy is unestablished. |
| Active reflection and divergence retrieval | Direct seed and journal production ranges in `packages/brain/src/memory/active-reflection.ts`; JSON clinamen body; PostgreSQL clinamen API inventoried | [MEM-RTE-journal-continuity](#mem-rte-journal-continuity). Full PostgreSQL divergence selector and publication implementation uninspected; no universal random/anomaly-selection claim. |
| JEPA deep connections | Direct main phase in `packages/brain/src/memory/dream/deep-connection.ts` and client request in `packages/brain/src/memory/dream/jepa.ts` | [MEM-RTE-deep-connection](#mem-rte-deep-connection), [MEM-CMP-jepa-service](#mem-cmp-jepa-service). Service architecture/training/version inaccessible in this source boundary. |
| Shared response/bot consumer, enhanced selection | Direct full `packages/brain/src/services/response.service.ts`, `packages/brain/src/experimental/enhanced-recall.ts`, formatter in `packages/brain/src/memory/memory.ts`; shared client symbol ranges | [MEM-RTE-response-memory](#mem-rte-response-memory). Reranker internals, confidence scoring and all social feature callers not fully audited. IRCoT requires an extra caller-supplied function, absent in this service invocation. |
| Write enrichment, category assignment, outbox, shadow reconciliation | Direct store body and shadow implementation; outbox worker inventoried | [MEM-OBJ-retrieval-state](#mem-obj-retrieval-state), [MEM-RTE-shadow-reconcile](#mem-rte-shadow-reconcile), supplied entry route. Full fragment extraction, entity pipeline, categorizer, RPC and retry semantics not audited; no complete enrichment receipt inferred. |
| Instruction installation, CLI dispatch, sync/export/import/snapshot/verify | Direct CLI dispatcher and full sync/dream; supplied setup; other command bodies inventoried | [RT-RTE-host-setup](runtime.md#rt-rte-host-setup), [MEM-RTE-prompt-sync](#mem-rte-prompt-sync). No execution-hook registration was established by the bounded setup/instruction searches; no system-wide hook-absence claim. Export/import/snapshot format fidelity and verifier internals remain uninspected. |
| Upload extraction | Direct `packages/brain/src/services/upload-processor.ts` extraction/admission ranges; upload route control search | [MEM-RTE-upload-extraction](#mem-rte-upload-extraction). Source fidelity of generated `original_text` is requested, not checked by the inspected schema. File extraction and full drain/retry loop not audited. |
| JSON pack import alternatives | Supplied `apps/server/src/routes/memory-packs.routes.ts`; direct `/packs/import` in `apps/server/src/routes/cortex.routes.ts`; CortexV2 export declarations | [RT-RTE-pack-import](runtime.md#rt-rte-pack-import), annotation below. Distinct owner-scope and count behavior; cannot generalize one handler's control to another. Smart exports/V2 import bodies uninspected. |
| Revocation/redelegation and ordinary mutation | Direct `packages/brain/src/memory/memory-revoke.ts`, `memory-decryption.ts`, migration 024 and memory update/delete bodies; encryption HTTP route search | [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal). Latest migration overlays, all recall lanes and derivative withdrawal remain incompletely audited; no end-to-end erasure claim. |
| Evidence tracing/explanation | Direct trace root/ancestry and explanation ranges in `packages/brain/src/memory/trace.ts` | [MEM-RTE-provenance-explanation](#mem-rte-provenance-explanation). API exposes a concrete model consumer, not proof that external callers use it or that inferred reasons are authentic. |
| Dashboard tasks and feature/worker producers | Supplied executor/tools/worker registry | [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task). Tools can store findings/recall; full social, sentiment, compound, campaign and Telegram retention loops remain included but uninspected. Prevents enumeration of every trace origin and decision consumer. |
| Marketplace, PMP artifact/pack/unlock/title, device/binding, legal/PII, wiki-pack installation | Direct endpoint/symbol inventories in `apps/server/src/routes/pack-marketplace.routes.ts`, `pmp-artifacts.routes.ts`, `pmp-packs.routes.ts`, `compliance.routes.ts`, `wiki-packs.routes.ts`; boundary inventory of remaining clients/services | Unresolved included operations. Missing payload serialization, transfer/installation admission, client read-back, scan disposition and delist/detach consequences prevent equating legal/cryptographic approval or pack purchase with semantic trust, memory adoption, or withdrawal. Wiki installation invalidates category cache; full rule interpretation not inspected. |
| Chain commitments and portable payloads | Direct store launch; boundary inventory of `packages/memorypack/src/`, `packages/pmp-sdk/src/`, `packages/tokenization/src/`, `programs/memory-registry/src/`, `contracts/base/` | Hash/proof/title payloads not substantively decoded. No claim that a commitment retains readable memory, guarantees truth, or retracts copies. Native cryptographic objects and consumer checks remain unresolved, not subsumed into plaintext rows. |
| Evaluation and cleanup | Direct LongMemEval judging/result-return range and targeted searches in `misc/scripts/longmemeval-benchmark.ts`; supplied reproduction entry | [MEM-OBJ-evaluation-results](#mem-obj-evaluation-results). Reference-answer scoring produces result artifacts; full seed/reload/cleanup code and all other evaluators, experimental local-memory implementation and shipped data artifacts uninspected. Prevents score reproduction, clean-state guarantees and causal benefit claims. |
| Frontends, mobile, infrastructure and native logs | Boundary inventories of `apps/chat/`, `apps/dashboard/`, `apps/mobile/`, `infra/`, native logs/results | Available but not directly traced here. UI persistence, live configuration, observed operation and deployment parity are not established. |

## Core ideas

1. **Content and retrieval state are different retained products.** Exchanges and generated prose live in memory rows. Vectors, links, timestamps, decay and importance affect selection by code. PostgreSQL recall normally reinforces access/links without boosting importance; JSON local recall explicitly boosts importance. One store's behavior does not characterize the others ([MEM-OBJ-retrieval-state](#mem-obj-retrieval-state), [MEM-OBJ-local-store](#mem-obj-local-store)).
2. **Trace transformation is wired, but admission is mostly automatic.** Main dreams create semantic summaries, procedural rules and self-model text. Hosted dreams have weaker lineage retention and a smaller phase set. SQLite dreams retain a queue result, not the same adopted memory product. Starting a scheduler is not approving each output ([MEM-RTE-dream-compaction](#mem-rte-dream-compaction), [MEM-RTE-belief-revision](#mem-rte-belief-revision), [MEM-RTE-hosted-dream](#mem-rte-hosted-dream), [MEM-RTE-local-dream](#mem-rte-local-dream)).
3. **Behavioral authority is consumer-specific.** MCP returns tool-result JSON to an external host; chat renders bounded memory into a system message; the shared response formatter explicitly orders the model to follow procedural strategies. Neither storage type nor a `source` label establishes reliability, obedience or causal benefit ([RT-BAP-chat-grounding](runtime.md#rt-bap-chat-grounding), [MEM-BAP-procedural-guidance](#mem-bap-procedural-guidance)).
4. **Withdrawal is not one operation.** Delete removes a row; revocation seals access to an encrypted row; contradiction handling adds a resolution and lowers a source's decay; compaction marks originals without deleting them; reconciliation shadow proposals do not apply revisions. None establishes that prior prompts, exports or derived statements are forgotten ([MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), [MEM-RTE-shadow-reconcile](#mem-rte-shadow-reconcile)).

## Shared records

### Components

#### MEM-CMP-jepa-service
Label: JEPA prediction service

No counterpart after comparison with runtime's embedding and generation components: this is the separate latent-relation prediction endpoint, not the query embedding provider. SRC-1, `packages/brain/src/memory/dream/jepa.ts`, sends an embedding, importance/decay/age/type and concept hashes to a configured URL and receives predicted embeddings/confidences. Client-side payloads are numerical dense representations plus symbolic metadata. Service weights, substrate, training lineage and whether parameters change during operation are uninspected: the remote service implementation is not supplied. Exact version is not pinned in this request; the mutable URL can resolve to another implementation. This does not establish online training.

> const response = await fetch(`${this.opts.url}/predict`, {
> --- `packages/brain/src/memory/dream/jepa.ts`

### Operative objects

#### MEM-OBJ-memories
Label: memories

Distinct from [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context): this is retained row content, not its transient rendering. SRC-1, `packages/brain/src/memory/memory.ts`, stores natural-language `content` and `summary` in Supabase/PostgreSQL, with symbolic type, source, owner, tags, evidence IDs and arbitrary metadata. Those columns do not all share a consumer or trust level. Content can be raw exchange, imported material, document extraction or model-derived text; initial caller authorship is not generally known. Caller-supplied `source` and citations are provenance assertions, not authentication or a truth gate. Summary is separately supplied/truncated, not guaranteed a faithful or sufficient rendering of content. Optional encryption changes physical encoding, not the natural-language form after authorized decryption. Failed DEK-wrap persistence can revert content to plaintext, as the supplied [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry) establishes.

> evidence_ids: opts.evidenceIds || [],
>         compacted: false,
> --- `packages/brain/src/memory/memory.ts`

Evidence IDs permit tracing but do not guarantee retained reasons: derived text may omit its argument, input summaries may already omit details, and normal prompt rendering does not automatically traverse ancestry. Later consumers include ordinary recall, dream selectors, response formatting, hydration and trace/explain. No rows or model outputs from actual operation were inspected.

#### MEM-OBJ-retrieval-state
Label: Retrieval state

Distinct from [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context) and the model components: persistent selection machinery comprises dense summary/fragment embeddings, symbolic lexical indexes, entity/link tables, and row importance/decay/access/timestamp fields. These live in database rows/indexes, not provider weights. Source text is transformed by configured embedding/extraction providers; complete extraction lineage and RPC implementations remain partly uninspected. Dense vectors have distributed numerical form; IDs, bond types and weights have fixed symbolic consumers. They affect future candidate generation and ranking without needing a model to interpret their reasons. SRC-1, `packages/brain/src/memory/memory.ts`:

> const { error } = await db.rpc('batch_boost_memory_access', {
>     memory_ids: ids,
>   });
> --- `packages/brain/src/memory/memory.ts`

The surrounding implementation calls this after selection when access tracking is enabled, and separately reinforces co-retrieved links. Bench mode disables that feedback. This is use-fed selection-state change, not evidence of better future capacity. The normal PostgreSQL path does not increase importance on read; [MEM-OBJ-local-store](#mem-obj-local-store) is a counterexample to extending that statement system-wide.

#### MEM-OBJ-local-store
Label: LocalMemory JSON store

Material storage alternative within [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), not the same referent as rendered context. SRC-1, `packages/brain/src/mcp/local-store.ts`, persists a JSON array under the user's `.clude/memories.json`, with numeric IDs, natural-language content/summary and symbolic metadata. Caller-provided text is pushed unchanged by `localStore`; temporary-file rename provides file replacement, not a multi-writer transaction or content-approval gate. Recall scores substring matches, importance, decay and creation recency, filters options and takes a bounded slice. Returning results also persists access time/count and increases importance. Corrupt-file handling backs up text and starts a fresh store; that is not demonstrated recovery of its semantic contents.

> mem.importance = Math.min(1, mem.importance + 0.01);
> --- `packages/brain/src/mcp/local-store.ts`

Later MCP calls reload the JSON file. `localClinamen` selects high-importance low-overlap content on request rather than unsolicited supply. There is no embedding/model-weight product in the inspected JSON path. Periodic decay parity, host adoption and remaining update semantics are not established.

#### MEM-OBJ-sqlite-store
Label: SqliteStore memories and dream queue

Distinct local substrate under [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), separate from JSON and PostgreSQL semantics. SRC-1, `packages/brain/src/storage/sqlite-store.ts`, stores text rows with `clude-` string IDs and JSON-encoded metadata, plus optional numerical vectors from the local embedder. Recall uses optional owner/type/importance/decay filters and vector candidates or an importance/recency-limited keyword fallback, then composite scoring. Full scoring/access tail and schema/extension behavior were not audited. The separate `dream_queue` holds operation, IDs, status and JSON-serialized generated result; a queue result is not automatically a memory row.

> ).run(JSON.stringify(result), now, id);
> --- `packages/brain/src/storage/sqlite-store.ts`

This attribution is the completion write, not a claim that the output is subsequently consumed by recall. The local embedding model's pinning/mutability limits are supplied in [RT-CMP-local-embedder](runtime.md#rt-cmp-local-embedder). Queue admission and later external use remain separately bounded in [MEM-RTE-local-dream](#mem-rte-local-dream).

#### MEM-OBJ-evaluation-results
Label: LongMemEval result records

No counterpart in supplied runtime records. SRC-1, `misc/scripts/longmemeval-benchmark.ts`, constructs symbolic result records containing question/reference/generated answer text, model-judged correctness, token F1, latency, returned-memory counts and evidence-session coverage. Storage is the benchmark's result JSON artifacts; searches locate the result writer and rejudge mode, not an observed run. The answer/reference prose is natural language; scores and IDs have code-defined consumers. A dataset reference answer is an answer oracle for this bounded evaluator, not a production memory truth oracle.

> const goldAnswer = String(q.answer || '');
>         const correct = await judgeAnswer(generated, goldAnswer, q.question, q.question_type);
>         const f1 = tokenF1(generated, goldAnswer);
> --- `misc/scripts/longmemeval-benchmark.ts`

Per-category readers and optional multistage answer processing differ from ordinary chat. Bench mode is set to suppress read feedback. Rejudge searches show failure-only rescoring and saving a new result file; this changes evaluation records, not demonstrated production-memory organization. Full seed provenance/cleanup and evaluator variants remain uninspected. No independent accuracy or causal memory benefit follows from the retained result format.

### Routes

#### MEM-RTE-recall-selection
Label: Recall selection
Part of: [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry)

This is the PostgreSQL selector/read subroute, not a replacement for SDK/MCP mode dispatch. SRC-1, `packages/brain/src/memory/memory.ts`, moves from caller query/options to optional query expansion, query embeddings, memory/fragment similarity, metadata candidates and flag-gated BM25, then scoring, entity/co-occurrence expansion, bond traversal, diversity and a final owner guard. Producer is the caller; code selects retained rows. Results are decrypted where possible. Metadata, seeds, entity and graph lanes have differing predicates; no universal filter guarantee is inferred from one lane.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected memory rows or an empty array on caught failure.
- Later read-back: prior writes and derived content reach later SDK/MCP/chat/service invocations through these selected rows; the selector itself does not guarantee model consumption.
- Delegated visibility: expansion/embedding providers see queries; downstream hosts receive selected row data. Database vectors/indexes are not themselves explanatory prose delivered to the chat model.
- Selection predicate: query, scope, types/tags/user/wallet and configured thresholds/flags; default limit five and minimum decay 0.1; importance-ranked pool, knowledge-seed candidates, optional lexical/vector/fragment lanes and graph/entity additions.
- Invalidation or expiry: decay and metadata changes alter future ranking; owner guard strips foreign results when scope is set; errors degrade or return empty; different lanes do not establish one uniform revocation/type/decay check.
- Activation or effect: row selection and asynchronous access/link reinforcement are wired; no answer-level dependence or benefit observed.
- Evidence limits: RPC/schema overlays, entity helper internals and every admission/filter lane not audited. Results are count-bounded by stages, not a universal tokenizer budget.

> const limit = opts.limit || 5;
>   const minDecay = opts.minDecay ?? 0.1;
> --- `packages/brain/src/memory/memory.ts`

Summary recall is a distinct alternative within the same entry container: it selects lightweight columns ordered by importance/date and applies metadata filters, but its inspected body does not use `opts.query` for semantic/text matching. Hydration requests explicit IDs and owner scope and returns available decrypted rows; this affords requested retrieval, not an independently wired two-stage host policy. Neither method proves later model activation. Their source bodies were read directly in SRC-1, `packages/brain/src/memory/memory.ts`.

#### MEM-RTE-dream-compaction
Label: Dream compaction
Part of: [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

The main cycle's compaction phase selects old faded low-importance episodic summaries, groups them by first concept, generates takeaways, stores semantic output with evidence IDs, marks originals and adds `elaborates` links. This is archival content transformation, not truncation of an already-running chat window. SRC-1, `packages/brain/src/memory/dream/cycle.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: phase completion and dream-log write; no user-facing checkpoint restore operation.
- Later read-back: semantic output is an ordinary recall candidate and can reach chat/shared response consumers; originals remain rows and can still be accessed.
- Delegated visibility: generator receives numbered source summaries, not full episodic bodies; later consumers receive selected rendering, not automatically the evidence chain.
- Selection predicate: episodic, uncompacted, over seven days old, decay below 0.3, importance below 0.5, oldest-first limit 30; at least five candidates overall and three per concept group; 150 output-token request.
- Invalidation or expiry: successful output precedes marking; partial writes/links are not rolled back; originals are marked rather than deleted. Main recall does not generally exclude `compacted` rows in the inspected body.
- Activation or effect: source-to-derived persistence is wired; later reliance and storage/context savings not observed.
- Evidence limits: no generated artifact or run trace; a locally generated `hashId` is assigned to `compacted_into` but is not passed into `storeMemory`, which generates its own hash. Pointer validity is therefore not established by this code; evidence IDs and numeric link endpoints are independent lineage paths.

Admission is model proposal plus automatic software storage. The prompt asks for essential meaning, not a reference-answer test. No per-summary human approval or semantic rejection gate is shown here beyond underlying storage checks; a failed phase can leave earlier admissions intact. Guidance persists in source; output and lineage persist in memory/logs. The model receives summaries, so retained reasons are limited to what that transformation preserves.

> .update({ compacted: true, compacted_into: hashId })
> --- `packages/brain/src/memory/dream/cycle.ts`

#### MEM-RTE-belief-revision
Label: Belief revision
Part of: [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

This part is the main contradiction-resolution phase, not all dream generation. SRC-1, `packages/brain/src/memory/dream/cycle.ts`, obtains at most three unresolved contradiction pairs, fetches their rows, asks the model for a current/synthesized understanding, parses citations and stores a semantic resolution. Code then creates `resolves` links and reduces the weaker source's decay. Importantly, the weaker source is selected by importance, with age as tie-breaker, not by interpreting which source the generated resolution says is wrong.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: phase completion and dream-log output; unavailable contradiction RPC skips this phase.
- Later read-back: resolution enters ordinary recall; altered decay affects future ranking, while both originals remain available. Log retention alone does not show a later log-reading critic.
- Delegated visibility: model receives both contents plus type/age/importance/concepts; normal later consumers receive selected resolution/source snippets, not automatically complete criticism and ancestry.
- Selection predicate: unresolved-pair RPC, max three, conditional owner filter and available source IDs; non-cop-out response plus underlying storage checks.
- Invalidation or expiry: reduces weaker decay by 20 percent with floor 0.05 after successful storage; asynchronous links and database updates can fail separately; no transactional rollback or universal source suppression.
- Activation or effect: new content and changed selection state are wired; correct resolution and subsequent behavioral dependence remain unobserved.
- Evidence limits: no instantiated theory or criticism output; pair detection/RPC and full encrypted-content path not audited. Prompted truth judgment is not demonstrated truth correction.

> const newDecay = Math.max(0.05, weaker.decay_factor * 0.8);
> --- `packages/brain/src/memory/dream/cycle.ts`

Admission is automatic model proposal/code rejection of cop-out responses; no per-resolution human decision or expected-answer oracle. Mode is open maintenance. Stored evidence IDs/links retain provenance, not necessarily a content-directed argument with blame assignment. For this theory-like belief route, guidance asks for the more accurate or nuanced belief and persists in shipped prompts; resolved prose and logs persist across invocations. **theory-builder conditions 1–4:** 1: afforded — a whole resolved belief can be formulated in text; actual content not observed. 2: uninspected — delivery and rank changes do not establish decisions depend on what the belief says. 3: afforded — prompt requests identifying outdated/wrong content, but no retained response demonstrates claim/result/blame/revision. 4: uninspected — repeated maintenance and stored outputs do not show criticism shaping a next round. Addressability is row-level whole-text replacement plus IDs, not a demonstrated assumption/part structure. Persistence is cross-invocation storage eligibility. Learning is uninspected: no improved-capacity or attribution evidence. Reflection is afforded as a proposed self-belief operation; both causal directions in exercised behavior are uninspected. Reflective/autonomous theory-builder status is uninspected; neither follows from scheduling/model authorship.

#### MEM-RTE-hosted-dream
Label: Hosted dream

Distinct owner-scoped alternate implementation, not a part of the main orchestrator's referent; overlaps [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle) only in its comparative account of hosted dreams. SRC-1, `packages/brain/src/memory/hosted-dreams.ts`, obtains episodic summaries, requests JSON factual insights and rules, then stores semantic/procedural rows within `withOwnerWallet`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: counts of stored semantic/procedural outputs.
- Later read-back: owner-scoped generated rows become ordinary recall/export candidates and may enter chat/service prompts.
- Delegated visibility: provider sees up to 30 dated episodic summaries from at most 50 recent episodes; consumer receives generated text, not automatically its sources.
- Selection predicate: at least 20 episodic memories and five recent episodes within seven days; OpenRouter enabled; parse JSON array; keep up to five insights and three rules, each length greater than 10 and less than 500.
- Invalidation or expiry: parse/provider failures are caught by phase; no cross-phase transaction or per-rule rollback. Subsequent ordinary memory management applies.
- Activation or effect: automatic generation/admission is wired; richer recall and improved behavior not observed.
- Evidence limits: declared array type is not a deep semantic validator; no output truth comparison, evidence-ID mapping or reasons retention is shown in these store calls.

> source: 'hosted-dream',
>                 importance: 0.65,
> --- `packages/brain/src/memory/hosted-dreams.ts`

Model proposes, software parses/filters/adopts; users do not approve individual products in this path. Guidance asks facts rather than events and rules of things to do/avoid; no expected-answer oracle. The file's broad header mentions compaction/reflection/self-model, but the inspected function explicitly skips compaction, contradiction resolution and emergence and stores only semantic/procedural outputs. This prevents inferring full main-cycle parity from its label. No theory assessment is inferred solely from generated-rule labels.

#### MEM-RTE-local-dream
Label: Local dream

Distinct alternative to [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle), reached by the CLI `dream` dispatch, not the SDK's main cycle. SRC-1, `packages/brain/src/cli/dream.ts`, `packages/brain/src/storage/dream-engine.ts`, `packages/brain/src/storage/sqlite-store.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI output/queue processing completion; successful model output is JSON-serialized into the queue result, or failure metadata marks the queue entry failed.
- Later read-back: decay changes later SQLite recall eligibility/scoring. Generated queue results have no adoption into memory rows or ordinary recall consumer in the inspected execute/complete bodies; external result-reading consumers are uninspected.
- Delegated visibility: selected Ollama model receives summaries of memory IDs named by each queue entry; original content is fetched but not included by the prompt builder.
- Selection predicate: CLI requires local `brain.db`; applies decay; queue processing needs at least five pending entries, loads up to 50 and uses the first detected Ollama model or fallback name. Standalone scheduler and every-tenth-store hook exist as class methods; their call-site search found no non-test brain call except CLI construction, so automatic MCP activation is not established.
- Invalidation or expiry: local requests have abort timeouts; queue failures are recorded; decay floors at 0.01. A failed result does not roll back prior decay.
- Activation or effect: local decay and queue completion are wired. Semantic/procedural memory adoption from dreams is not established by a completed queue status.
- Evidence limits: full repository-wide external callers and actual queue initialization remain unknown; exported methods afford caller use. The detected model version/weights are not pinned, and no parameter update is shown in this client. Ollama's mutable localhost endpoint and model name can resolve to changed weights; provider-held parameter changes and exact storage of those weights are uninspected.

> this.store.completeDream(entry.id, { success: true, result });
> --- `packages/brain/src/storage/dream-engine.ts`

Queue APIs admit requested operations/IDs through caller code; whether a human chooses them is unresolved. Model produces text; completion marks success without truth testing or per-result approval, including empty response fallback. No answer oracle is supplied. Operation names select shipped prompts, not proof of corresponding curation. This alternative cannot supply the missing later consumer for a trace-to-derived-memory learning claim.

#### MEM-RTE-strategy-refinement
Label: Strategy refinement
Part of: [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

Main learning phase calls action/outcome tracking and refinement. The inspected refinement in SRC-1, `packages/brain/src/memory/action-learning.ts`, groups retained action rows by feature and outcome tag, generates caution/reinforcement rules and stores procedural text with aggregate rates. It also increases importance of existing same-feature strategy rows after positive actions. The latter matches feature tags, not a checked provenance record proving that the strategy was recalled and caused that action.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated lesson strings, with caught failures returning accumulated results.
- Later read-back: procedural rows and changed importance can enter ordinary recall; [MEM-RTE-response-memory](#mem-rte-response-memory) independently selects procedural guidance and renders rates.
- Delegated visibility: generator sees counts and up to three truncated action-content examples per feature; later response model receives strategy rendering and aggregate metadata, not full measured outcome records.
- Selection predicate: up to 50 action-tagged rows from seven days, at least three with outcome tags overall, at least two per feature; negative rate over 0.6 or positive rate over 0.7 triggers generation; reinforcement finds up to 20 strategy-tagged procedural rows.
- Invalidation or expiry: generation failures return null; old rules remain rather than a demonstrated supersession; importance reinforcement capped at one. New write failure does not necessarily prevent lesson text appearing in the returned list.
- Activation or effect: trace-fed rule and ranking updates are wired; successful downstream behavior and improved capacity remain unobserved.
- Evidence limits: full original action/outcome instrumentation and metric reliability were not audited; aggregate success rates are not causal effect estimates or a reference-answer oracle.

> featureInstruction: 'You are a strategy analyzer. Output ONLY the procedural rule, nothing else. No quotes, no explanation.',
> --- `packages/brain/src/memory/action-learning.ts`

Computation proposes and admits the rule without per-content human approval. Mode is open ongoing maintenance, with rates serving trigger/selection rather than expected correct answers. Guidance asks avoidance or continuation; source persists and result text plus feature/count/rate metadata persist. Reasons are deliberately compressed out of the requested output; examples are not copied into the stored strategy metadata. Later rendering reads rates, not necessarily a justification. This is an improvement-directed behavioral guidance path, not sufficient evidence for learning, formulated criticism, or exercised self-improvement.

#### MEM-RTE-journal-continuity
Label: Journal continuity

Distinct from [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle): active reflection is a separate SDK/scheduled operation. SRC-1, `packages/brain/src/memory/active-reflection.ts`, selects recent/important and divergent seeds, generates a theme and journal, titles/stores it as introspective memory, and links seeds/previous entries.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: journal structure with text/title/seed IDs/memory ID, or null for trivial output/failure; callback/publication handling is a separate surface not fully audited.
- Later read-back: a later reflection explicitly loads up to three introspective memories from 72 hours and supplies their summaries; ordinary recall may also deliver journals to response/chat consumers.
- Delegated visibility: generator sees up to 15 seed summaries, up to three self-model summaries, previous-journal summaries and memory statistics; not full original exchanges or all prior journal reasoning.
- Selection predicate: recent six-hour episodic plus high-importance 48-hour candidates and up to two clinamen seeds; random older fallback only on caught clinamen error; deduplicate/limit, then model theme and up to 1500 journal tokens.
- Invalidation or expiry: outputs shorter than 50 trimmed characters rejected; source/previous rows persist; linked writes can fail separately. Summary truncation limits future continuity.
- Activation or effect: previous retained self-generated text is wired into a later model invocation, not merely offered by an API; actual influence or improvement unobserved.
- Evidence limits: no generated journal; its label does not prove criticism, novel knowledge or accurate introspection. Divergence selector internals and posting consumer remain partial inspection.

> const previousReflections = await getRecentMemories(72, ['introspective' as any], 3);
> --- `packages/brain/src/memory/active-reflection.ts`

Admission is automatic model generation plus length/storage checks; no independent truth oracle or per-entry human approval. Shipped guidance invites questioning beliefs and continuity, but these are requested operations, not evidence they occurred. Journal prose may retain reasons; the later reflection path reads the shortened summary, not automatically the whole argument.

#### MEM-RTE-deep-connection
Label: Deep connection
Part of: [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

SRC-1, `packages/brain/src/memory/dream/deep-connection.ts`, samples memory vectors/metadata, invokes [MEM-CMP-jepa-service](#mem-cmp-jepa-service), matches predicted embeddings to retained memories, rejects already-findable/self/existing targets and writes symbolic graph links. This result differs from semantic text generation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: link count, skip flag and up to three top-link summaries; dream log is also written.
- Later read-back: stored links can affect bond traversal in [MEM-RTE-recall-selection](#mem-rte-recall-selection); provider predictions are not directly chat instructions.
- Delegated visibility: JEPA service sees source embedding and metadata; selector compares predicted vectors to the database; later consumers see linked memories selected by code.
- Selection predicate: `JEPA_ENABLED` flag, up to 15 recent plus five random high-importance candidates, 24-hour already-queried exclusion, usable embedding; predicted matches excluding normal fast recall top ten and existing links, rank confidence times similarity, top two per source.
- Invalidation or expiry: unavailable service marks queried and defers retry; graph write is separate; no correctness rollback/independent validation is established.
- Activation or effect: numerical prediction to symbolic link to later selection is wired; semantic validity, deployed activation and benefit remain unobserved.
- Evidence limits: service training and exact parameters unknown; successful novelty relative to one recall call is not proof of a true causal/support relation.

> .map(c => ({ ...c, score: c.confidence * c.similarity }))
> --- `packages/brain/src/memory/dream/deep-connection.ts`

Software selects/admits links automatically; no human per-link approval or expected-answer oracle. Guidance is a fixed requested relation set. Stored strength is 0.5, not the computed rank score; relation/IDs persist while the proposed semantic rationale is absent from this admitted link. No theory-builder claim is inferred from relation labels.

#### MEM-RTE-response-memory
Label: Response memory

Distinct shared-response consumer route, not a part of the authenticated chat handler or dashboard executor. It overlaps the supplied [RT-CMP-generate-response](runtime.md#rt-cmp-generate-response) as consumer computation rather than duplicate component. SRC-1, `packages/brain/src/services/response.service.ts`, `packages/brain/src/experimental/enhanced-recall.ts`, `packages/brain/src/memory/memory.ts`, `packages/shared/src/core/claude-client.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated response/thread through the shared generation client.
- Later read-back: when caller supplies memory options, prior content and procedural rules enter later response generations as system-message memory context.
- Delegated visibility: provider receives dated summary/content snippets grouped by type, with success-rate annotations for qualifying procedural metadata and grounding instructions; not the entire database or complete provenance trace.
- Selection predicate: main enhanced recall plus independent procedural recall limit three and minimum importance 0.5, ID deduplication; optional provider reranking/confidence filtering; IRCoT additionally needs `llmCallFn`, not passed by this service.
- Invalidation or expiry: selection rebuilt each call; absent memory options skips recall; failures/flags change available context, not a guaranteed rejection of generation. Underlying stored rows remain reachable.
- Activation or effect: system prompt delivery and explicit behavioral direction are wired; compliance and successful behavior change unobserved.
- Evidence limits: renderer truncation limits visibility; no strict whole-request token budget shown here; enhanced selector names do not prove every experiment activates. Reranker and gate internals remain uninspected.

> IMPORTANT: You MUST follow the Learned Strategies above. They are behavioral rules you derived from analyzing your own past successes and failures. Apply them to this response.
> --- `packages/brain/src/memory/memory.ts`

The passage above is the text inside a source string, not an instruction to this analyst. This route is requested delivery: caller opts into memory; code then supplies additional procedural selections without requiring each strategy's own query. It is not an independently unsolicited background push. Strategy authority is natural-language model instruction, not code execution or a verified warrant for the advertised provenance.

#### MEM-RTE-upload-extraction
Label: Upload extraction

No counterpart after comparison with [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry) and [RT-RTE-pack-import](runtime.md#rt-rte-pack-import): this is a file-chunk model transformation/admission path. SRC-1, `packages/brain/src/services/upload-processor.ts`, starts from pending `llm_outputs` chunk rows and model-extracts memory nodes, then owner-scopes parallel episodic writes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: background chunk processing; HTTP upload acceptance is not proof that every node was stored. Node/parser results and raw provider output are tracked by the processor.
- Later read-back: stored episodic extracted nodes become ordinary recall/dream inputs; chunk/output records alone do not establish a production prompt consumer.
- Delegated visibility: provider sees document chunk and extraction instructions; later memory consumers can see title, generated summary, entities and alleged original text, bounded by underlying store/renderer truncation.
- Selection predicate: pending chunk claim, regex-extracted JSON array and schema requiring title/content/entities/original_text types; accepted nodes passed to storage with batch/chunk/node metadata.
- Invalidation or expiry: parse failure yields no nodes; independent writes can partially succeed; full retry/cleanup loop not audited.
- Activation or effect: document-to-derived-memory admission is wired, not verified fidelity or later behavioral dependence.
- Evidence limits: uploaded file authorship and human versus agent caller unresolved; original-text equality is requested, not checked by this schema. Extraction/queue safety and all file formats not audited.

> original_text: z.string(),
> --- `packages/brain/src/services/upload-processor.ts`

User/agent initiates upload; model authors extracted nodes; software schema/storage admits without per-node human approval or reference oracle. Guidance requests faithful summaries and verbatim passages. These are retained with source IDs and metadata, but a claimed source passage remains model-produced until compared with the raw chunk. This gives derived text an acquisition path, not authenticated authorship.

#### MEM-RTE-prompt-sync
Label: Prompt sync

Distinct from [RT-RTE-host-setup](runtime.md#rt-rte-host-setup): setup writes static tool-use policy; sync writes a changing content snapshot for later host loading. SRC-1, `packages/brain/src/cli/sync.ts`, called by the inspected CLI dispatcher, exports hosted memories or loads local database recent memories and writes a prompt file periodically or once.

- implementation conclusion status: wired
- consumption conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: a UTF-8 prompt file and CLI update message.
- Later read-back: documented symlinking into a project affords later host consumption; no inspected host loader guarantees the file is used or reloaded.
- Delegated visibility: selected summary-or-content bullets grouped as facts/behaviors/history, not IDs, complete evidence chains or all memory types.
- Selection predicate: fetch/export limit 10000; direct path looks back 8760 hours; at most 40 semantic and 30 procedural by importance and 20 episodic by recency; no tokenizer budget.
- Invalidation or expiry: full file overwritten on refresh; default 300-second interval or `--once`; caught errors report refresh failure. Old external copies are not withdrawn.
- Activation or effect: persistent rendered content is wired; future host loading/compliance only afforded.
- Evidence limits: target host, grants, runtime tokenizer and actual symlink configuration uninspected. Self-model/introspective types are not rendered by this function.

> Symlink ${output} into your project for live memory access.
> --- `packages/brain/src/cli/sync.ts`

Operator/caller chooses format/path/interval; code automatically selects and replaces content. This is not per-memory approval. Guidance labels retained material as prior memory and learned behaviors; selection text persists on disk, and removal is file edit/deletion or next overwrite, not a system-wide semantic veto.

#### MEM-RTE-memory-withdrawal
Label: Memory withdrawal

Distinct mutation/control subroute within the broad capabilities of [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), with extra encrypted HTTP operations not established by that record. SRC-1, `packages/brain/src/memory/memory.ts`, `packages/brain/src/memory/memory-revoke.ts`, `packages/brain/src/memory/memory-decryption.ts`, `packages/database/migrations/024_revoke_columns.sql`; MCP numeric-ID schemas and encryption endpoint ownership were also inspected by ranges/search.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: update/delete boolean or structured revoke/redelegate outcome; prerequisite/key/decrypt/RPC failures reject access-state changes.
- Later read-back: row deletion or edited fields change subsequent retrieval; revocation clears plaintext summary/vector/tokens and provider wrap in the inspected RPC; normal recall/summary/graph paths contain exclusion guards. Explicit hydration is owner-scoped but has no delegated-state predicate in its inspected body and can return undecryptable ciphertext.
- Delegated visibility: revoke uses provider key to seal remaining summary/vector before dropping provider access; redelegation takes an owner-client supplied provider wrap and validates by decrypting stored content. External already-delivered plaintext is outside this operation.
- Selection predicate: row ID and scope/HTTP owner admission; revocation requires encrypted delegated row and usable provider wrap/key; redelegation requires encrypted row and an authenticating key unwrap/decrypt.
- Invalidation or expiry: caller edits/deletes or revokes; owner rewrap can restore provider access. Database/update failures report failure; no global derivative/export/cache rollback is established.
- Activation or effect: access-state mutation and scoped row mutation are wired; end-to-end erasure across lanes, migrations and derived copies unobserved and not established.
- Evidence limits: migration 024 is an inspected base, not a claim all later overlays preserve exactly it; entity/seed/fragment paths and external copies require separate audit. Local mode identifiers and mutation schemas do not have proven parity.

> DELETE FROM memory_dek_wraps WHERE memory_id = p_memory_id AND recipient = 'provider';
> --- `packages/database/migrations/024_revoke_columns.sql`

Caller-authorized deletion/edit/revocation is content/access replacement, not evidence the caller is human or that a model cannot invoke an exposed management tool. Software validates keys/shape and scopes requests; there is no semantic truth oracle. Plain `updateMemory` truncates/patches content and summary but does not call enrichment or lexical refresh in the inspected body, so refreshed embeddings/indexes cannot be assumed. It also does not show an encryption rewrite protocol. This is a stale-index/encryption-coherence audit question, not a deployed failure observation.

SQLite store IDs are `clude-` strings while MCP update/delete schemas require positive numbers and stringify those numbers for SQLite. The inspected store/recall return string IDs. This source mismatch prevents assuming the advertised management tools can address returned SQLite memories, despite the methods existing. JSON numeric IDs do not have this particular mismatch (SRC-1, `packages/brain/src/storage/sqlite-store.ts`, `packages/brain/src/mcp/server.ts`).

#### MEM-RTE-shadow-reconcile
Label: Shadow reconcile

Distinct write-time instrumentation alternative, not main dream contradiction resolution. It extends [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry) but does not replace stored content. SRC-1, `packages/brain/src/memory/memory.ts`, `packages/brain/src/memory/reconcile-shadow.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: detached completion after optional embedding; missing table/provider/budget degrades without undoing the original write.
- Later read-back: proposed operations/reasons persist in `memory_reconciliation_log` for analysis; no production recall/adoption consumer is established by this shadow implementation. Reporting tools are inventoried, not fully traced.
- Delegated visibility: candidate screening sees embeddings; optional router receives same-owner summaries and dates. Normal memory consumers do not receive a superseded row merely because a proposal says update/noop.
- Selection predicate: enabled configuration, not bench mode, stored embedding, resolved owner scope, top six temporal-similarity candidates, valid/non-invalidated owner-fenced rows, configured floor/LO/HI, optional router budget.
- Invalidation or expiry: unavailable schema skips instrumentation; router off/over budget produces `needs_router`; original memory remains admitted. No rollback needed for an unapplied proposal.
- Activation or effect: retained measurement/advice is wired, not operative content replacement or downstream behavior change.
- Evidence limits: full router validation, enforce alternatives and reporting-tool consumers not audited. File header's LLM-free description is incomplete for the optional router branch.

> proposed_op: decision.op,
> --- `packages/brain/src/memory/reconcile-shadow.ts`

The quoted field belongs to a log insertion, not an applied update. Proposer is screening code/optional model; software admits a log record, not a changed belief. Human review is contemplated by the source's measurement rationale but not a per-write approval gate. No answer oracle or semantic success is supplied by cosine. Persisted reason/gate version helps later analysis but does not close a production revision loop.

#### MEM-RTE-provenance-explanation
Label: Provenance explanation

Distinct model-consuming library operation, not generic hydration under [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry). SRC-1, `packages/brain/src/memory/trace.ts`, fetches owner-scoped root/evidence rows and graph/entity relations, then `explainMemory` explicitly supplies a derived trace context to `generateResponse`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: trace/explanation, ranked key memories and chronology, or null when root/response unavailable.
- Later read-back: invocation on a retained memory supplies root content, ancestry/related summaries and selected snippets to a model; this is a concrete internal consumer rather than merely a hypothetical caller of storage.
- Delegated visibility: root content and provenance context, ancestor content snippets up to 300 characters, descendant/related summaries, entity and timeline information; not necessarily original model reasoning or complete source inputs.
- Selection predicate: requested memory ID, default trace depth three, visited-node deduplication and bounded relation/entity selection; explanation asks why this memory exists and requests a reasoning chain.
- Invalidation or expiry: deleted/inaccessible sources limit trace; a new explanation is generated from current retained state; prior generated reasons are not established as stored/adopted guidance.
- Activation or effect: trace-to-model delivery is wired; historical authenticity and behavioral reliance on the explanation unobserved.
- Evidence limits: helper traversal/decryption and external endpoint usage not fully audited. Generated explanation reconstructs reasons; it does not authenticate an original reasoning episode.

> const trace = await traceMemory(memoryId, 3);
> --- `packages/brain/src/memory/trace.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-procedural-guidance
Label: Procedural guidance

Distinct from [RT-BAP-chat-grounding](runtime.md#rt-bap-chat-grounding): consumer is the shared response model, not chat's separate renderer/provider invocation. Channel is system-message memory context built by the response service and shared formatter. Force is natural-language behavioral instruction, with rates attached for suitable procedural metadata; horizon is current generation and future generations that reselect the stored rule. Code also grants procedural memories an independent selection route even when they were not returned by the main query. SRC-1, `packages/brain/src/services/response.service.ts`, `packages/brain/src/memory/memory.ts`, `packages/shared/src/core/claude-client.ts`; [MEM-RTE-response-memory](#mem-rte-response-memory) supplies the minimum passage. The formatter calls them rules derived from past successes/failures, but caller-authored/imported procedural content can receive the same treatment: type alone does not authenticate that derivation. Delivery is wired; compliance, reliability and improved capacity are unobserved.

## Annotations

#### On [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn)

Conversation rows retain raw exchange text; separate episodic memory wraps user/assistant text. Later history and recalled memory are separate read-back paths. The supplied route establishes history prefix limit and heuristic trimming, so evicted window text remains in storage rather than being replaced by a generated checkpoint. This resembles bounded by-value reconstruction, not a traversable pointer heap: IDs alone do not restore omitted contents. Direct inspection of SRC-1, `apps/server/src/lib/memory-prompt.ts`, clarifies that introspective memories are deliberately included with episodic memories in `<recent>`, not omitted as an unsupported type.

> const episodic = memories.filter(m => m.memory_type === 'episodic' || m.memory_type === 'introspective').sort(byMemoryDateAsc);
> --- `apps/server/src/lib/memory-prompt.ts`

#### On [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

Main consolidation, reflection and procedural extraction produce different retained parts of the common memory store. Direct reflection reads existing self-model plus up to ten 48-hour semantic memories and statistics; parses evidence citations; rejects cop-outs; stores a self-model row, temporal/support links and dream log. Later reflection explicitly reloads self-model through `getSelfModel`; ordinary response renderers also expose selected self-model text. Procedural extraction uses recent episodic summaries with importance/valence, asks for one/two behavioral rules, rejects short/cop-out responses and stores up to two procedural rows with evidence IDs. These are automatic transformation/admission rather than human approvals. SRC-1, `packages/brain/src/memory/dream/cycle.ts`:

> content: `Self-reflection: ${text}`,
> --- `packages/brain/src/memory/dream/cycle.ts`

> content: `Behavioral pattern: ${text}`,
> --- `packages/brain/src/memory/dream/cycle.ts`

These texts and evidence references retain derived claims and lineage, not necessarily their reasons. A dream-log record may retain the fuller response, but the ordinary model prompt does not automatically reload that log. Name-based assertions of reflection/learning are therefore not upgraded to observed criticism or capacity improvement. Main cycle parts declared above have their own controls/status; hosted and SQLite alternatives remain distinct.

#### On [RT-RTE-pack-import](runtime.md#rt-rte-pack-import)

The supplied `/api/memory-packs/import` owner-scope uncertainty remains. A separate Cortex `/packs/import` explicitly wraps writes in the authenticated owner's scope, maps imported data to content/summary/type/tags/source, and increments imported count after awaiting storage without testing a returned ID. Thus one handler's count can overstate successful row admissions, while the supplied handler increments only for a returned ID. SRC-1, `apps/server/src/routes/cortex.routes.ts`:

> await withOwnerWallet(cortexReq.ownerWallet!, async () => {
>         for (const mem of pack.memories) {
> --- `apps/server/src/routes/cortex.routes.ts`

Imported source content is caller-selected; a source/tag label does not prove its original author, human review or truth. Both paths feed normal rows rather than a separate higher-trust knowledge substrate. Bulk sequential writes lack an established cross-item rollback. This is an alternative admission path, not evidence that the supplied route's scope concern is repaired.

## Write side

The entry route admits caller-authored content after shape/length/duplicate checks, owner/context resolution and optional auto-metadata. Content I/O is code-owned; whether the caller is human, agent or integration is not determined by API presence. Exchange capture is automatic after generation; imported packs and uploads have different admission rules. Keep those separate from a human editing agent configuration or installing host instructions ([RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task), [MEM-RTE-upload-extraction](#mem-rte-upload-extraction)).

The raw-to-derived chains are concrete but unequal:

- Exchange/episode summaries → main semantic consolidation or procedural rules → ordinary rows/evidence IDs/links → later recall and prompt rendering. Main reflection additionally consumes previous self-model. Some reasons may remain in prose/logs, but normal renderers supply bounded snippets rather than a complete evidence reconstruction ([RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle), [MEM-RTE-response-memory](#mem-rte-response-memory)).
- Old episodic summaries → compact semantic takeaway → marked originals plus lineage → later recall. This is neither a current-window checkpoint nor deletion; `compacted_into` requires identity repair/audit ([MEM-RTE-dream-compaction](#mem-rte-dream-compaction)).
- Contradiction contents → resolution plus importance/age-based decay change → subsequent selection. Generated semantic judgment and source downweighting do not necessarily identify the same rejected claim ([MEM-RTE-belief-revision](#mem-rte-belief-revision)).
- Action/outcome-tagged traces → aggregated features/examples → rule plus rates → independent procedural selection and instruction. Stored rates provide an access/credibility cue, not retained causal justification ([MEM-RTE-strategy-refinement](#mem-rte-strategy-refinement), [MEM-BAP-procedural-guidance](#mem-bap-procedural-guidance)).
- Owner-scoped episodes → hosted facts/rules → rows without explicit evidence-ID mapping in those store calls → later recall. SQLite's summaries → generated queue result has a different terminal product; no recall adoption was established ([MEM-RTE-hosted-dream](#mem-rte-hosted-dream), [MEM-RTE-local-dream](#mem-rte-local-dream)).
- Prior journals/seeds/self-model summaries → new journal → introspective row/summary → explicitly later journal-summary consumption. Reasons can be lost in that summary even when full journal content remains stored ([MEM-RTE-journal-continuity](#mem-rte-journal-continuity)).
- Retained vectors/metadata → predicted neighbors → graph links → later graph expansion. This is selection-state transformation, not a newly formulated explanatory theory ([MEM-RTE-deep-connection](#mem-rte-deep-connection)).

Read feedback also changes later selection state; JSON local mode's importance bump differs from PostgreSQL. Automatic enrichment and shadow proposals are separate from admission of the initial row; neither completion nor truth follows from receiving an ID. Evaluation writes results and rescored artifacts; the inspected evaluator does not establish automatic adoption of those scores into live memory. Benchmark seeding/cleanup and all alternate evaluators remain explicitly uninspected ([MEM-OBJ-evaluation-results](#mem-obj-evaluation-results)).

Rejection is mechanism-specific: empty storage content, cop-out dream responses, parse/length failures, trivial journals, invalid key wraps, and optional confidence filtering reject different things. They are not one semantic veto. Deletion/revocation/update can remove or alter future accessibility, but derivative memories, exports and delivered prompts need their own withdrawal chain. Shadow `update`/`noop` decisions remain unapplied; label-based contradiction “resolution” need not erase or even fully suppress originals ([MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), [MEM-RTE-shadow-reconcile](#mem-rte-shadow-reconcile)).

## Read-back

The system has requested pull paths and automatic selection within requested generation, not one universal push policy. SDK/MCP recall returns records; explicit hydration selects IDs. MCP results require an external host to interpret them. Host setup requests recall/store behavior but does not enforce it. Prompt sync affords file-based host supply; the file write is wired, host loading is not ([RT-RTE-host-setup](runtime.md#rt-rte-host-setup), [MEM-RTE-prompt-sync](#mem-rte-prompt-sync)).

Authenticated chat supplies selected content as typed system sections after heuristic context fitting; independent history reload can preserve raw text that the memory summary omits. Guest chat does not run this persistence loop. Shared response generation instead opts in through memory options, performs enhanced recall and a separate procedural query, then supplies system text with an explicit follow-strategies instruction. Its selector can add general high-importance strategies without a query; that is automatic supplementation within the caller's requested response, not proof of background unsolicited delivery ([RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-guest-chat](runtime.md#rt-rte-guest-chat), [MEM-RTE-response-memory](#mem-rte-response-memory)).

Working-context controls differ. Chat's code trims fitted history/memory while storage remains reachable. Dashboard tasks isolate each prompt/tool transcript from foreground chat and persist task results, but the supplied executor does not reload prior task logs; tool calls can separately recall/store findings. Dream/journal frames expose summaries or selected source contents, not the foreground window. Popping these frames does not itself retain memory; the explicit write/return paths do. Summary/hydration APIs and provenance explanation can bring selected retained material into later contexts, but only explanation has an inspected internal model invocation after trace reconstruction ([RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task), [MEM-RTE-provenance-explanation](#mem-rte-provenance-explanation)).

Count limits, output-token requests and character-snippet bounds are different budgets. They do not imply a common tokenizer-bounded context, complete evidence delivery or faithful reconstruction. Selection state has algorithmic authority at ranking; prose has interpretation-dependent authority at models; tool JSON availability has only host-affordance authority until a caller actually delivers/uses it. No source-only trace establishes activation or benefit.

## Integration issues

1. **Clarification, not a contradiction of the broad runtime warning:** chat explicitly maps introspective memories into `<recent>`. “Unsupported types are not rendered” must not be read as excluding the source-native introspective type. Direct renderer evidence is in the [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) annotation. Also the shared formatter includes all five source-native types; its procedural force differs from chat's grounding policy ([MEM-RTE-response-memory](#mem-rte-response-memory), [MEM-BAP-procedural-guidance](#mem-bap-procedural-guidance)).
2. **Storage-mode maintenance parity is unresolved and locally contradicted:** hosted processing is only semantic/procedural in the inspected function, and SQLite completion writes queue result, not adopted memory. Keep these distinct from the main orchestrator ([RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle), [MEM-RTE-hosted-dream](#mem-rte-hosted-dream), [MEM-RTE-local-dream](#mem-rte-local-dream)). Whether an uninspected caller adopts local queue results remains open.
3. **Compaction identity and semantics:** the phase creates a local hash for originals' `compacted_into`, while storage generates its own hash. Evidence IDs/numeric links remain separate positive lineage. A usable hash pointer or actual archival exclusion is not established; do not equate compaction with dropping originals/current-window replacement ([MEM-RTE-dream-compaction](#mem-rte-dream-compaction), [MEM-OBJ-memories](#mem-obj-memories)).
4. **Pack admission alternatives:** the scoped Cortex handler does not resolve the supplied generic pack handler's scope uncertainty; their imported-count rules also differ. Full PMP/marketplace unpack/install/read-back/withdrawal remains an included unresolved loop, with missing facts and prevented conclusions in the coverage table ([RT-RTE-pack-import](runtime.md#rt-rte-pack-import)).
5. **Withdrawal and editing coherence:** latest RPC overlays, all entity/seed/fragment lanes, derivative content, indexes/encryption after ordinary patches and already exported copies need further audit before a universal suppression/erasure claim. SQLite string IDs conflict with numeric MCP management schemas. No deployed exploit/failure is claimed ([MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry)).
6. **Reason retention and outcome attribution:** strategy refinement retains aggregate rates but explicitly asks only a rule. Same-feature reinforcement does not verify prior strategy use. Journal continuity reads shortened summaries; provenance explanation reconstructs rather than authenticates reasons. These positives coexist with unestablished content-directed criticism, causation and capacity improvement ([MEM-RTE-strategy-refinement](#mem-rte-strategy-refinement), [MEM-RTE-journal-continuity](#mem-rte-journal-continuity), [MEM-RTE-provenance-explanation](#mem-rte-provenance-explanation)).
7. **Misleading labels:** reconciliation header describes an LLM-free slice, but a gated model-router branch exists and still only inserts proposals. Hosted header overstates the function's implemented phase set. “Learned strategy,” “resolution,” “success rate” and JEPA relation names do not establish source trust or epistemic success ([MEM-RTE-shadow-reconcile](#mem-rte-shadow-reconcile), [MEM-RTE-hosted-dream](#mem-rte-hosted-dream), [MEM-RTE-deep-connection](#mem-rte-deep-connection)).
8. **Record identity reconciliation:** declared main compaction, belief revision, strategy and deep-connection routes are explicit parts of the supplied main-cycle container, not proposed replacements. Recall is a part of the entry container. New stores, retrieval state and evaluation result objects have no supplied object counterpart; rendered context remains separate. Shared response/procedural authority and trace explanation have distinct consumers/operations. Hosted/local dream records overlap the runtime's comparative discussion, not its main-orchestrator referent; if reconciliation treats that referent as a broader container, preserve these parts and their different statuses rather than merging mechanisms. No known exact duplicate is intentionally redeclared.
9. **Coverage limits:** complete evaluator seed/cleanup, other evaluators, social/compound workers, client retention, portable cryptographic payloads, marketplace/compliance disposition, external model state and deployment remain unresolved as itemized above. This prevents an exhaustive whole-system guarantee, not the supported chains established here. No extra source identity or scope expansion is requested.

## Limitations and checks

All conclusions are bounded to inspected source at the frozen commit. No observed run, genuine generated theory/journal, model weight artifact, deployed tenant database or independent intervention/comparison was available. Positive delivery/selection/admission wiring does not establish reliable interpretation, truthful content, exercised reflection, causal learning or successful self-improvement. Unread shipped paths are inventory limits, not evidence of absence or external exclusions.

Method inputs were read completely, including bounded runtime and record-contract ranges. Source identity was rechecked against supplied boundary and HEAD. Report identity fields match the supplied run/boundary. Only assigned report, answers, worker identity and any validation-repair scratch are writable. Deterministic validation: the required `commonplace-run validate-output` command passed with “Member content check passes; invocation residue not checked.” This checks structure/quotation occurrence rather than acceptance or substantive support.
