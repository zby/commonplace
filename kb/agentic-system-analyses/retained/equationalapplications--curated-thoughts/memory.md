---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Curated Thoughts memory: source files, derived facts, human verification, bounded context and unequal recall filters."
run-id: AAS-2026-11-08-curated-thoughts-00ab3a770403-01
source-identity: https://github.com/equationalapplications/curated-thoughts
reviewed-boundary: "433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd"
---

# Curated Thoughts memory report

## Boundary and evidence

The subject is the shipped file-to-knowledge system, including desktop, headless CLI, full MCP, separate tools MCP, and local integration instructions. The frozen boundary is SRC-1 at `433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd`; the source register remains in [boundary](boundary.md#source-register). This report follows both persistent knowledge and the controls determining a later model invocation's input. It does not equate the product's words “wisdom,” “verified” or “trustworthy” with factual correctness.

The supplied runtime was used as a provisional route inventory, not as an inspection limit. Direct reads added implementation evidence for `src-tauri/src/wisdom_match.rs`, `src-tauri/src/two_stage.rs` interfaces, `src-tauri/src/prompt_drop.rs`, `src-tauri/src/db/heal.rs`, `src-tauri/src/db/queue.rs`, `src-tauri/src/db/stated_ledger.rs`, `src-tauri/src/db/wisdom.rs`, `src-tauri/src/entities_api.rs`, `src-tauri/src/okf_api.rs`, `src-tauri/src/wiki_graph.rs`, selected `src-tauri/src/lib.rs` maintenance functions, `src-tauri/src/tool_dispatch.rs` retrieval functions, `src-tauri/src/librarian/synthesis.rs`, `tools/src/queries.rs`, `tools/src/bin/ct.rs`, and `src/components/queue/UnverifiedPromptModal.tsx`. The skill was read directly as doctrine/design; the frozen-vector test was read as evaluator implementation, not as an executed result. Other baseline findings below explicitly cite runtime rather than claiming independent reinspection.

The external wiki engine, CTI integration, remote replica implementation and inference-provider internals are not frozen sources. Their absence prevents conclusions about engine-internal admission, host injection/caching, replica consistency and provider learning. No target code, tests or examples were executed. No user vault or agent execution trace was supplied. All route operation statuses remain uninspected.

### Coverage inventory

| Entry point or operation | SRC-1 source paths and inspection | Covering record or unresolved part and prevented conclusion |
| --- | --- | --- |
| Agent file deposit, vault ingest, desktop watcher, CLI librarian | Supplied runtime: `src-tauri/src/wisdom_deposit.rs`, `src-tauri/src/pipeline/mod.rs`, `tools/src/bin/ct.rs`; direct synthesis reads | [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick), [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [MEM-OBJ-source-material](#mem-obj-source-material). Exact parser/chunker variants not re-audited; no complete transformation-fidelity claim. |
| Model synthesis, admission, review | Direct `src-tauri/src/librarian/synthesis.rs`; supplied commit/review findings | [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), annotations below. |
| Human capture, fact edit/archive, entity summary update | Direct `src-tauri/src/entities_api.rs`, `src-tauri/src/db/wisdom.rs` | [MEM-RTE-human-maintenance](#mem-rte-human-maintenance); capture and editing differ from agent append-only writes. Entity merge/redirect internals and draft promotion are not fully traced, preventing complete identity/rollback conclusions. |
| Confirmation, denial, undo and reconstruction | Direct `src-tauri/src/db/queue.rs`, `src-tauri/src/db/stated_ledger.rs`, `src-tauri/src/queue_api.rs` interface | [MEM-RTE-verification-state](#mem-rte-verification-state). Rebuild's caller frequency is not independently established here. |
| Recall-triggered verification prompts | Direct `src-tauri/src/prompt_drop.rs`, `src/components/queue/UnverifiedPromptModal.tsx`; supplied dispatch wiring | [MEM-RTE-verification-prompt](#mem-rte-verification-prompt). Not a mandatory recall veto. |
| CLI message/activity wisdom match and correction output | Direct `tools/src/bin/ct.rs`, `tools/src/queries.rs`, `src-tauri/src/wisdom_match.rs`; two-stage interface inspection | [MEM-RTE-wisdom-match](#mem-rte-wisdom-match). Stage-1 provenance traversal internals not fully audited; no completeness guarantee. |
| Full MCP and tools MCP contextual recall/code search | Supplied runtime; direct full-dispatch getter | [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), [MEM-RTE-alternate-read](#mem-rte-alternate-read). Server-specific logging is not knowledge curation. |
| Legacy semantic search/context/graph and vault search | Direct dispatch functions and `src-tauri/src/wiki_graph.rs` search/context; supplied bridge dispatch | [MEM-RTE-alternate-read](#mem-rte-alternate-read). Graph vocabulary and node budgets constrain results; complete graph/ontology preservation not established. |
| Deletion healing, scheduled pruning and CLI heal | Direct `src-tauri/src/db/heal.rs`, `src-tauri/src/lib.rs`; supplied scheduler findings | [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). |
| External wiki-engine ingest/model callbacks | Supplied `src/lib/wiki.ts` route | [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). Included adapter, opaque engine transformation/admission. |
| OKF bundle import/export | Direct `src-tauri/src/okf_api.rs` preview/apply; underlying apply algorithm not inspected | Included alternative admission capability, not covered by librarian gate. Import conflict rules, metadata trust and rollback remain unresolved; no universal admission invariant. |
| Outbox, reindex, embedding sweep/scheme migration, reconciliation and repair utilities | Supplied runtime plus direct outbox calls in wisdom/queue/prune; `tools/src/bin/ct.rs` dispatch | Content/vector consistency repair exists at inspected writers. Full replay, replica deletion, migration and reconciliation algorithms uninspected; no end-to-end durability or global invalidation conclusion. |
| Evaluation/calibration | Direct `src-tauri/tests/wisdom_gate_bench.rs` header and freeze-key checks; remaining calibration artifacts uninspected | [MEM-CLM-evaluation-boundary](#mem-clm-evaluation-boundary). No empirical reliability, task-success or benefit estimate. |

## Core ideas

1. The retained unit is not just a log. Ordinary files become indexed chunks, model-generated proposals, and then admitted facts/entities/edges/tasks. Existing summaries and fact bodies feed later librarian requests; selected fact bodies also reach external agents. Those are two different consumers and authority paths. [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [MEM-OBJ-wiki-content](#mem-obj-wiki-content).
2. Content and trust metadata are separate. Human confirmation stamps, evidence references, denial keys and embedding scheme labels have symbolic consumers; they are not themselves an explanation of why a fact is true. Confirmation can propagate by exact content hash, while denial keys also depend on source/chunk identity. [MEM-OBJ-verification-ledgers](#mem-obj-verification-ledgers), [MEM-RTE-verification-state](#mem-rte-verification-state).
3. Retrieval policy is surface-specific. The calibrated CLI gate can abstain, apply temporal eligibility and return replacement corrections; lexical contextual recall, direct getters and legacy semantic search have different predicates. Therefore retention or withdrawal metadata alone does not establish universal exclusion from every agent read. [MEM-RTE-wisdom-match](#mem-rte-wisdom-match), [MEM-RTE-alternate-read](#mem-rte-alternate-read).
4. Librarian context is freshly assembled and prefix-truncated. This limits working input rather than compacting an agent conversation. The preserved knowledge is outside the request and must be selected again; no pointer in the model window guarantees future reachability. See the annotation on [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-material
Label: Vault source files and indexed chunks

Raw natural-language files, including caller-written agent deposits and app-captured human statements, live in the vault filesystem. Indexed document/chunk rows persist separately in SQLite with symbolic IDs, hashes and positions; embeddings are dense numerical derivatives, not readable source text. These are original inputs to extraction, not a complete retained agent transcript. Caller identity does not establish the author's human control or whether text came from experience, another model or copied material. The ordinary deposit path is already established in [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick); this object has no supplied object counterpart and is not a duplicate route. SRC-1, `src-tauri/src/wisdom_deposit.rs`, `src-tauri/src/db/wisdom.rs`, `src-tauri/src/librarian/synthesis.rs`; deposit evidence in the cited runtime record.

Human capture has an explicit file-first chain:

> /// The whole capture: render + write the file, write the attestation row and
> /// its ledger mirror, register the kick, run the kick. Order matters: the
> --- `src-tauri/src/db/wisdom.rs`

Later consumers are ingest/librarian and evidence joins, not just file readers. Current source chunks enter a fresh extraction request; they are not automatically the caller's entire session history. Initial general vault acquisition and every parser's fidelity remain outside this object's inspected detail.

#### MEM-OBJ-wiki-content
Label: Retained wiki and entity text

Natural-language `llm_wiki_entries` title/body and entity summaries are persisted in SQLite. Entity IDs, edges and tasks have symbolic structure; edges do not become textual explanations merely because their labels are readable. Text and numerical embeddings are separate operative parts; see [MEM-OBJ-embedding-blobs](#mem-obj-embedding-blobs). This object has no supplied object counterpart; it is the retained product consumed by [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) and [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), not either route itself.

Lineage includes model proposal acceptance, external engine writes with unresolved internals, human edits, and import capability. Librarian read-back is supported directly: candidate facts include live rows across redirect clusters, ordered by update time with a per-candidate cap. The actual prompt receives body text and IDs, not every stored provenance field. SRC-1, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/entities_api.rs`, `src-tauri/src/okf_api.rs`.

> "SELECT id, body FROM llm_wiki_entries
>                  WHERE entity_id IN ({placeholders}) AND deleted_at IS NULL
>                  ORDER BY updated_at DESC LIMIT {MAX_FACTS_PER_CANDIDATE}"
> --- `src-tauri/src/librarian/synthesis.rs`

Model interpretation gives this material guidance authority in later extraction. External recall delivers task evidence/advice without enforcing agent compliance. Persisted rows can span sessions, but actual retention duration, use and improved capacity are unobserved.

#### MEM-OBJ-embedding-blobs
Label: Stored chunk and fact vectors

Dense numerical representations are retained separately from text in database blobs. They derive from text through the configured embedder, with scheme/profile identity affecting comparison eligibility; original model training and exact provider weights are uninspected. No weight-update mechanism is established by these stored vectors. This is distinct from the inference component [RT-CMP-embed-profile](runtime.md#rt-cmp-embed-profile): the component produces vectors, whereas these mutable derived objects enter ranking and coverage checks.

At the inspected fact-edit writer, body replacement also replaces or clears the vector and stamps the write scheme, so an old vector is not deliberately left describing new text. SRC-1, `src-tauri/src/db/wisdom.rs`:

> SET title = ?1, body = ?2, updated_at = ?3, embedding_blob = ?4,
>                 embed_scheme = ?5, entity_id = ?7
> --- `src-tauri/src/db/wisdom.rs`

Consumers are cosine ranking, candidate selection and scheme/coverage guards. Numerical rank affects delivery, not factual validity. Missing embeddings can hide a fact from semantic paths while lexical/direct paths still read its body.

#### MEM-OBJ-verification-ledgers
Label: Durable verification carriers and derived indexes

Symbolic JSONL under `stated/` carries confirmations, attestations and denials; SQLite contains derived stamps, `stated_attestations` and `queue_denials`. Confirmation keys hash title/body; attestations recheck current file bytes; denial keys combine document path, chunk hash and fact-text hash. These metadata are not the retained fact body and do not prove an authenticated human principal merely because a fixed actor label is written. No supplied object counterpart exists; [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission) concerns a different decision boundary. SRC-1, `src-tauri/src/db/stated_ledger.rs`, `src-tauri/src/db/queue.rs`.

> /// * `stated/.denials.jsonl` → `queue_denials`, repopulated verbatim (the
> ///   ledger pins the suppression keys; the chunk/fact text itself is not
> ///   stored, so there is nothing to re-hash);
> --- `src-tauri/src/db/stated_ledger.rs`

Later consumers reconstruct metadata, filter the confirmation queue and select human-tier activity delivery. Ledger files and database mutations are not one atomic storage resource. Deleting a source, changing text, and removing a ledger line have different consequences; no blanket “verification always follows meaning” guarantee is warranted.

#### MEM-OBJ-unverified-match
Label: Unverified match drop file

`<vault>/.brain/unverified-match.jsonl` is ephemeral symbolic operational state carrying fact ID, query, source reference and display-text snapshots. It is an event trace/queue, not independently admitted knowledge. The actual modal deliberately reloads current content by ID rather than trusting that snapshot. Distinct from [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), which produces a result and may emit this object. SRC-1, `src-tauri/src/prompt_drop.rs`, `src/components/queue/UnverifiedPromptModal.tsx`.

> const row = await getQueueFact(p.fact_id);
>           if (row) rows.push(row);
> --- `src/components/queue/UnverifiedPromptModal.tsx`

The emitter deduplicates unacked IDs best-effort; drain acknowledges a capped batch and removes already acknowledged lines. Prompt history is not a durable explanatory memory. The resulting human decision can separately change [MEM-OBJ-verification-ledgers](#mem-obj-verification-ledgers).

### Routes

#### MEM-RTE-wisdom-match
Label: CLI gated wisdom read-back

CLI dispatch selects message or activity target, truncates query text to 2,000 characters, resolves one read scheme and calibrated floors, embeds only when the selected plan needs vectors, then returns selected fact bodies and correction objects. Rust controls selection; no model judges factual truth here. At most ten ordinary entries are admitted by the shared core. Source support: SRC-1, `tools/src/bin/ct.rs`, `tools/src/queries.rs`, `src-tauri/src/wisdom_match.rs`. This has no supplied route counterpart: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) is a separate lexical-wiki/code tool, not CLI wisdom matching.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI JSON or text wisdom result and gate/audit diagnostics; not a generated answer.
- Later read-back: previously admitted SQLite fact bodies reach a requesting external consumer through command output. CTI is a documented external consumer, not inspected host wiring.
- Delegated visibility: embedder receives truncated target text, optionally scheme-prefixed; external consumer receives selected body text and labels, not the whole store or proposal reasoning.
- Selection predicate: calibrated cosine gate plus excludes, nondeleted/nonexpired/nonsuperseded eligibility and read scheme; two-stage mode restricts facts using source candidates. Healthy activity mode restricts to user_stated/user_confirmed, otherwise the caller reruns the message path with its selected stage flags.
- Invalidation or expiry: temporal eligibility filters ordinary entries; corrections follow supplied excluded IDs to a live replacement head, rejecting deleted/expired heads, cycles and excessive depth. Corrections can still flow when ordinary entries abstain.
- Activation or effect: selection and delivery are wired; no external-agent trace establishes compliance or changed behavior.
- Evidence limits: externally installed hooks, caching and automatic injection are not inspected; activity's human-tier restriction does not apply to every fallback result.

> QueryKind::Message => None,
>         QueryKind::Activity => Some(&["user_stated", "user_confirmed"][..]),
> --- `src-tauri/src/wisdom_match.rs`

> // v1-arm selection (--single-stage, or the kill-switch) ALWAYS falls
>     // back to the message call below: the activity v1 arm does not exist in
>     // this PR.
> --- `tools/src/queries.rs`

The two-stage precheck considers calibrated floor availability and candidate embedding coverage before spending embeddings. An unregistered model/scheme can abstain; degraded coverage can fall back to single-stage where a floor exists. This is a budget/relevance gate, not learned new weights or a quality oracle. Exclude IDs are caller state, not internally retained knowledge of what an agent has already seen.

#### MEM-RTE-alternate-read
Label: Semantic graph and direct entry reads

Caller query/vector or topic/ID → shared dispatch/graph code → selected retained rows → caller. Source: SRC-1, `src-tauri/src/tool_dispatch.rs`, `src-tauri/src/wiki_graph.rs`. Distinct from [RT-RTE-context-recall](runtime.md#rt-rte-context-recall): semantic wiki search and direct getters coexist with that lexical contextual-recall route. Vault/code search supplies indexed source snippets rather than derived fact bodies; its baseline is the supplied runtime.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: search hits, graph context/provenance, or concatenated full_text/chunks from the direct getter.
- Later read-back: requesting agent receives retained facts, source references or graph neighborhood; current store state is selected anew.
- Delegated visibility: query embedding can reach provider; selected results return through tool response, with bridge capability differences retained in runtime.
- Selection predicate: wiki search ranks positive cosine times tier weight with requested entity/tier filters and scheme; limits clamp to 1–25. Wiki context adds deduplicated seed walks with depth/node/fact caps. Direct getter selects nondeleted rows by entity/entry ID or title/body/tags topic substring, without a calibrated semantic gate.
- Invalidation or expiry: inspected search/getter predicates exclude deleted rows; unlike CLI matching they do not apply superseded_by/valid_to eligibility. Scheme filters apply to semantic search; direct text getters need no embedding.
- Activation or effect: delivers data and optional verification prompting; not forced belief or action.
- Evidence limits: no shared universal recall policy; full graph traversal correctness and external usage remain uninspected.

> WHERE {entity_filter}{tier_filter}deleted_at IS NULL AND embedding_blob IS NOT NULL{scheme_filter}"
> --- `src-tauri/src/wiki_graph.rs`

> WHERE deleted_at IS NULL AND (entity_id = ?1 OR id = ?1)
> --- `src-tauri/src/tool_dispatch.rs`

The getter concatenates bodies and `source_ref`, not proposal reasoning. Legacy search returns title/score/provenance labels, so a search hit alone is not proof its whole evidential argument was delivered. The context wrapper separately assembles facts, entities, edges, provenance and truncation status.

#### MEM-RTE-human-maintenance
Label: App capture and content maintenance

App commands → shared capture or direct fact/summary writer → retained files/rows and outbox. Source: SRC-1, `src-tauri/src/entities_api.rs`, `src-tauri/src/db/wisdom.rs`. Distinct from [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick) and [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission): app text capture writes attested stated files; existing body editing and archival can bypass the proposal-review transaction as an admission route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: captured path or write success/error, not necessarily proof the librarian produced a fact.
- Later read-back: edited fact bodies and summaries enter future recall/candidate requests; captured stated files enter ingest and synthesis.
- Delegated visibility: embedding service receives edited body where configured; capture kick calls the librarian, not an isolated autonomous agent frame.
- Selection predicate: caller supplies content and target; capture requires nonempty text and exclusive new file; update validates active entity/cluster and existing nonarchived fact. Capture drops the supplied page entity binding and lets librarian targeting decide placement.
- Invalidation or expiry: fact edits replace/clear embeddings; archive soft-deletes and purges edges; file/attestation/ledger/kick is non-atomic. Failure can leave partial capture state; ledger reconstruction and retries are separate recovery routes.
- Activation or effect: content mutations are wired; factual correctness, human authorship authentication and downstream benefit remain unobserved.
- Evidence limits: a frontend command is an intended human decision surface, not proof of deployed access control; import, draft and external engine paths have separate policies.

Admission is the app caller's content decision plus software shape/existence checks, not model approval of every edit. No reference-answer oracle is established. This is open user-driven work, not a controlled improvement curriculum. App capture requests new knowledge; edits can replace bodies; archive can reject continued availability. The update SQL does not reset all existing confidence/provenance fields when text changes, so metadata persistence cannot by itself validate the new meaning.

> update_wisdom_with_blob(&mut guard.0, &entity_id, &fact_id, &body, embedding_blob)
> --- `src-tauri/src/entities_api.rs`

#### MEM-RTE-verification-state
Label: Confirmation denial and reconstruction

App fact decision → ledger and database effects → later queue/delivery/rebuild consumers. Source: SRC-1, `src-tauri/src/db/queue.rs`, `src-tauri/src/db/stated_ledger.rs`. No supplied equivalent route; [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission) admits proposals, while this route judges an existing fact and can undo a prior denial.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: confirm/deny/undeny success/error; a missing evidence source/chunk prevents forming a denial key and causes refusal.
- Later read-back: confirmation stamps affect human-tier consumers; denied rows are archived, queue suppression keys persist, and rebuild can restore metadata from ledgers. Confirmation-by-hash can stamp same-text live facts beyond the originally clicked ID.
- Delegated visibility: ledger reconstruction compares content hashes and source files without a model call; UI supplies the decision, not a provider oracle.
- Selection predicate: fact ID for click decisions; confirmation matches title/body hash; denial uses source-document path, evidence chunk hash and fact-text hash; undeny restores archived same-text matches.
- Invalidation or expiry: hash mismatch prevents new confirmation matching; attestation rebuild drops missing/changed files; undeny removes durable and derived suppression and clears deleted_at on archived text matches. Rebuild is transactional within SQLite, not jointly with ledger I/O.
- Activation or effect: symbolic state changes alter queue membership and activity-delivery eligibility; correctness of confirmation and actual later delivery are unobserved.
- Evidence limits: a stamped fixed actor label is not human authentication; queue suppression is not proof every generation/import path can never reproduce denied content.

Human supplies the click decision; code hashes, stamps or archives. The decision is an admission/rejection of trust or availability, not a computational answer oracle. Open verification requests, not benchmark trials. Undo is supported; ledger-first failures are retriable, not cross-resource atomic. Proposal text guidance is inapplicable here because no model proposes a replacement theory in these functions.

> if let Some(line) = line_by_hash.get(confirmation_content_hash(&title, &body).as_str()) {
> --- `src-tauri/src/db/stated_ledger.rs`

> crate::db::wisdom::archive_wisdom_in_tx(&tx, &entity_id, fact_id)?;
> --- `src-tauri/src/db/queue.rs`

#### MEM-RTE-verification-prompt
Label: Recall-triggered verification prompting

Non-human-tier recall hit → best-effort drop-file append → capped app drain → current-row reread → human confirm/deny. This automatic selector pushes a request to the desktop operator, not unsolicited knowledge into an agent context. SRC-1, `src-tauri/src/prompt_drop.rs`, `src/components/queue/UnverifiedPromptModal.tsx`; source-side emission is also noted in [RT-RTE-context-recall](runtime.md#rt-rte-context-recall). This route has distinct persistence, consumer and admission behavior from recall itself.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: emitter returns unit and swallows I/O errors so prompting failure does not veto recall.
- Later read-back: modal drain reads queued IDs, fetches live brain rows, and presents verification choices; only a subsequent decision enters durable verification state.
- Delegated visibility: GUI receives current row/evidence from the database, not trusted drop-file text.
- Selection predicate: recalled fact not user_stated/user_confirmed, no unacked duplicate ID; app drain cap is three, skips while open/in flight or snoozed, and rereads each fact independently.
- Invalidation or expiry: drain acknowledges selected lines and prunes acknowledged state; vanished/unreadable rows are skipped after acknowledgement; timer cleanup stops polling.
- Activation or effect: prompting and the separate decision path are wired; no evidence a person reviewed or acted on any supplied event.
- Evidence limits: advisory read-before-append dedupe is not transactional; transient state is not a durable knowledge rationale or reliable mandatory review gate.

> pub const PROMPT_DRAIN_CAP: usize = 3;
> --- `src-tauri/src/prompt_drop.rs`

The trigger query and source-reference snapshot can explain why the prompt was raised, but neither automatically becomes a new fact. Human content judgment belongs to [MEM-RTE-verification-state](#mem-rte-verification-state).

#### MEM-RTE-memory-withdrawal
Label: Source healing and delayed pruning

Deletion-triggered scheduler, GUI heal button or CLI heal → source-reference grounding checks → soft deletion/edge purge; scheduled prune → hard deletion of eligible old rows/evidence and outbox records. SRC-1, `src-tauri/src/db/heal.rs`, `src-tauri/src/lib.rs`; triggering adapter is [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). This record separates local retention policy from that broader external-engine/scheduler route rather than replacing it.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: counts/status/error; breaker refusal can report no deletion without making references newly grounded.
- Later read-back: deleted rows disappear from inspected live-row recall; after pruning their row/evidence is physically removed. Outbox deletion is produced but remote application remains outside inspected evidence.
- Delegated visibility: native maintenance uses database evidence, not a model judge; frontend receives status/counts.
- Selection predicate: live librarian_inferred rows with nonnull source_ref, demonstrably ungrounded according to shared helper; breaker can refuse batch. Prune selects only librarian_inferred rows soft-deleted more than seven days ago.
- Invalidation or expiry: soft deletion precedes delayed hard deletion; unreadable/unparseable grounding metadata is conservatively retained by the helper contract, not treated as proof of invalidity.
- Activation or effect: local availability and graph edges change; not a measured correction in agent behavior or factual truth.
- Evidence limits: GUI button and scheduled/CLI heal use sibling functions; user-confirmed/user-stated rows are not covered by this inferred-only selection. Global invalidation across all paths and remote replicas is unestablished.

No model/human judges content meaning in this pass; software checks backing references and deletion budgets. The CLI can explicitly bypass the bulk breaker for a run; this is not per-content human truth approval. Pruning is deletion, not a retained compacted summary. The pre-prune row can remain archived; hard deletion does not itself promise restoration.

> const SEVEN_DAYS_MS: i64 = 7 * 86_400 * 1000;
> --- `src-tauri/src/lib.rs`

> AND e.source_type = 'librarian_inferred'",
> --- `src-tauri/src/db/heal.rs`

### Claims

#### MEM-CLM-evaluation-boundary
Label: Frozen-vector evaluator scope

The shipped regression evaluator asserts a bounded code-path purpose, not demonstrated model quality or long-horizon benefit. It references frozen vectors and expected files; this report did not execute it, inspect all calibration cells or authenticate recorded outcomes. No supplied claim counterpart exists; [RT-CMP-embed-profile](runtime.md#rt-cmp-embed-profile) establishes inference configuration rather than evaluation validity. SRC-1, `src-tauri/tests/wisdom_gate_bench.rs`:

> //! Recomputes hit@2 / FP through `wisdom_match_with_floor` from the vectors
> //! the calibration runs froze. Guards the CODE PATH, not the model.
> --- `src-tauri/tests/wisdom_gate_bench.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-fact
Label: Retained fact consumer authority

Consumer: external calling agent, and separately the librarian model. Channel: requested tool/CLI result for the agent; assembled candidate section for the librarian. Force: natural-language informational guidance, not a symbolic instruction requiring compliance. Horizon: later invocations, potentially across sessions while rows persist. Selection filters are symbolic authority over what gets delivered, not authority over what the recipient believes. Supporting passages and source evidence are in [MEM-OBJ-wiki-content](#mem-obj-wiki-content), [MEM-RTE-wisdom-match](#mem-rte-wisdom-match), and [RT-BAP-librarian-guidance](runtime.md#rt-bap-librarian-guidance). This path distinguishes retained-content authority from the shipped-prompt authority of that supplied record. SRC-1, `src-tauri/src/librarian/synthesis.rs`, `tools/src/queries.rs`, `src-tauri/src/tool_dispatch.rs`.

## Annotations

#### On [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis)

Read-back is internally triggered by current document processing: code selects existing entity summaries and fact bodies using name hits and mean chunk embeddings, clips summary snippets to 200 characters, limits candidate/fact lists, then places candidates ahead of source text/structural context. It truncates the entire user context at the 4,000-character boundary. This preferentially loses suffix material; validation against full pre-truncation collections cannot establish that each allowed citation was visible to the model. SRC-1, `src-tauri/src/librarian/synthesis.rs`.

> let full_context = if structural.is_empty() {
>         format!("{candidates_section}{context_body}")
>     } else {
>         format!("{candidates_section}{context_body}\n{structural}")
>     };
>     let truncated = truncate_context(&full_context);
> --- `src-tauri/src/librarian/synthesis.rs`

No persistent conversation is compacted by this request. As a working-context lens, selected input resembles a temporary frame whose output escapes as proposals; it is not a delegated agent stack with arbitrary history sharing. Outside material stays in files/SQLite and must be queried again. There is no in-window reference whose mere presence makes external memory live or guarantees a reload. Static prompts are guidance, not use-accumulated memory. The retained raw-to-derived chain is source chunks → proposals/reasoning → admitted text → later candidate/recall delivery, not raw logs alone. Agent-deposit origin may include experience, but the system does not itself establish a complete trace origin from that label.

#### On [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission)

Proposal reasoning is retained as proposal metadata; librarian candidate read-back selects `id, body`, while direct entry read-back selects bodies and source references. Thus retained reasons are not shown to accompany every later fact consumer. Human accept/edit/reject and folder-driven automatic admission remain different controls; starting a deposit workflow is not human approval of the derived propositions. The source-supported lineage survives even where rationale delivery is incomplete. SRC-1, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/tool_dispatch.rs`; proposal persistence evidence is supplied by the cited runtime record.

#### On [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

The requesting agent receives selected fact/code content rather than the complete persistent brain. Lexical wiki ranking and cosine code ranking are two selectors, not a single semantic wisdom gate. Requested pull delivery must not be redescribed as autonomous unsolicited injection simply because an external skill recommends calling it. Read-side audit writes are access metadata, not automatically synthesized reusable task lessons. SRC-1, `src-tauri/src/tool_dispatch.rs`, `tools/src/bin/curated_thoughts_mcp.rs`; baseline passages and policy differences are in the cited record.

## Write side

The ordinary acquisition/authoring path is already [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick): caller supplies file content, software validates lane/shape and creates it, then indexed chunks feed synthesis. File authorship, filesystem I/O and downstream proposal admission are distinct. Folder modes and dirty hash/model watermarks decide whether transformation runs; they do not evaluate the truth of each extracted claim. Model-output parsing filters symbolic consistency, while manual or automatic resolution determines persistence. See [RT-OBJ-folder-rules](runtime.md#rt-obj-folder-rules), [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission).

Human capture adds an explicit attestation carrier; human edits can change a fact body directly. Verification changes trust/availability metadata without replacing the text. Denial archives the row and retains a suppression key; undo can restore same-text archived rows. These paths are detailed in [MEM-RTE-human-maintenance](#mem-rte-human-maintenance) and [MEM-RTE-verification-state](#mem-rte-verification-state). Neither an app route nor a confidence label authenticates actual human deliberation.

Withdrawal is not one mechanism. Proposal rejection prevents admission; archive hides a live row; reference healing removes inferred entries with stale grounding; prune physically deletes eligible archived rows later. The inspected recall predicates honor soft deletion, but temporal supersession is not universal across surfaces. Source-specific preservation of reasons and evidence does not establish that every consumer receives or checks them. See [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) and [MEM-RTE-alternate-read](#mem-rte-alternate-read).

A further distinction is essential for supersession deposits: writing a correction request is not application of that correction. The source explicitly retains pending status while librarian application is deferred. SRC-1, `src-tauri/src/wisdom_deposit.rs`:

> // Kick: supersessions/ is `summarize` — the file ingests and drains with
>     // zero facts (V25 override). Librarian APPLICATION of the supersession is
>     // the follow-up reconcile spec (rule 4 mechanics); until then status
>     // stays pending.
> --- `src-tauri/src/wisdom_deposit.rs`

This does not negate the separate implemented reader for already-populated supersession chains in [MEM-RTE-wisdom-match](#mem-rte-wisdom-match). It prevents inferring an end-to-end automatic correction loop from the existence of both writer and reader interfaces.

The external wiki-engine callback path and OKF import are additional admission surfaces. The former has the explicit opaque-engine limit in [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); the latter parses a selected bundle then calls `apply_import`, without demonstrating equivalent librarian proposal checks in the inspected wrapper. SRC-1, `src-tauri/src/okf_api.rs`. Their unresolved internals prevent a claim that every write is model-proposed, human-reviewed, provenance-complete or reversible by one common protocol.

## Read-back

There are four materially different consumers/channels:

- The librarian receives automatically selected existing summaries and fact bodies in a fresh model request. Current document processing triggers selection; the aggregate prefix budget can omit later source/structural material. This is internal read-back, not a persistent chat summary. The supplied synthesis record and annotation retain the selector details.
- External agents request contextual recall, semantic/graph tools, direct getters or CLI wisdom matching. Selection depends on query, target kind, tier/entity filters, exclude IDs, floors and embedding scheme according to surface. The retained material returned is text/snippets and symbolic labels, not trained weights. See [MEM-RTE-wisdom-match](#mem-rte-wisdom-match), [MEM-RTE-alternate-read](#mem-rte-alternate-read) and [RT-RTE-context-recall](runtime.md#rt-rte-context-recall).
- The desktop operator receives pushed verification prompts selected from recent non-human-tier hits, then reread from the brain. Drop-file snapshots are not trusted displayed fact content. Decisions are separate from prompt generation. See [MEM-RTE-verification-prompt](#mem-rte-verification-prompt).
- Reconstruction/maintenance code consumes ledger keys, hashes and references symbolically. This is later read-back of operational trust/availability state, not a model reading explanations. See [MEM-RTE-verification-state](#mem-rte-verification-state) and [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal).

The local skill claims a before-task recall/after-task deposit protocol, [RT-CLM-agent-workflow](runtime.md#rt-clm-agent-workflow). It affords an experience-to-source-to-derived-memory path when a caller follows it; it does not prove automatic full-trace capture or deployed host injection. Access logs and match events alone do not establish trace-fed learning. A trace-origin claim remains local to the caller-supplied text, with opaque/mixed provenance unresolved. No measured improvement or activation is inferred from persistence and delivery.

## Integration issues

- No correction to a supplied runtime fact is required. The new temporal-filter contrast qualifies any later attempt to generalize CLI gate policy to all recall: [MEM-RTE-wisdom-match](#mem-rte-wisdom-match) and [MEM-RTE-alternate-read](#mem-rte-alternate-read) have different inspected predicates.
- Potential route overlap: [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) supplies native heal/prune retention semantics underneath the scheduled calls in [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). These are a policy subroute and a broader callback/scheduling container, not independent duplicate maintenance systems. [MEM-RTE-verification-prompt](#mem-rte-verification-prompt) similarly expands the side effect mentioned in [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), with a later human consumer not covered by the recall route alone.
- The supersession deposit API is wired to request retention but its source says application remains deferred. Existing-chain correction read-back does not close that write-side gap. This prevents an automatic correction-loop claim for [MEM-RTE-wisdom-match](#mem-rte-wisdom-match); it does not deny alternate writers or already populated chains.
- Confirmation reconstruction applies hashes to matching live rows, but its inspected implementation does not explicitly reset existing orphan confirmation stamps. The comments describe reconstruction semantics more strongly than that visible reset behavior. Combined with body editing that preserves metadata, this prevents treating all stored confirmation metadata as continuously tied to unchanged meaning. [MEM-OBJ-verification-ledgers](#mem-obj-verification-ledgers), [MEM-RTE-verification-state](#mem-rte-verification-state), [MEM-RTE-human-maintenance](#mem-rte-human-maintenance); SRC-1, `src-tauri/src/db/stated_ledger.rs`, `src-tauri/src/db/wisdom.rs`.
- OKF import conflict/admission semantics, external wiki-engine transformation, identity merges/drafts, maintenance replay and remote replica application remain locally named unresolved surfaces in the coverage inventory. Available source paths were not all audited; they are not access failures. They prevent universal provenance, rollback, suppression and durability conclusions, not the supported local mechanisms.
- No distinct supplied object duplicates were found. New objects name the material acted on by runtime routes; new read routes name different selectors. [MEM-BAP-retained-fact](#mem-bap-retained-fact) overlaps the librarian consumer of [RT-BAP-librarian-guidance](runtime.md#rt-bap-librarian-guidance) but distinguishes retained content from shipped prompt instructions.

## Limitations and checks

The checkout HEAD was rechecked against the boundary pin and matched. This invocation's job, member type, collection, worker rules, records contract and supplied members were read completely, recovering continuation ranges. No additional source identity, mutable branch evidence, external prior analysis or target execution was used. Source passages are implementation evidence except the explicitly marked shipped skill and evaluator intent. No claims of universal mechanism enumeration, authenticated review, correct synthesis, successful replication, improved capacity or causal benefit follow from this report.

Validation: the supplied `commonplace-validate` memory-role check passed with no findings after correcting two comment-quotation delimiters. This establishes structural/citation checks, not claim support or job acceptance.
