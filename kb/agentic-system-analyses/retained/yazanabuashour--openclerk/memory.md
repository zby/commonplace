---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OpenClerk memory: canonical Markdown, derived projections, explicit session intake, synthesis repair, semantic caches and regression read-back."
run-id: AAS-2026-10-16-openclerk-ec0e00c2bb0a-01
source-identity: "https://github.com/yazanabuashour/openclerk"
reviewed-boundary: "092fb98d243c2d9d95867ad04618ebce88983552"
---

# OpenClerk memory report

## Boundary and evidence

This member traces retained content and its later consumers within the whole-system [boundary](boundary.md). SRC-1 implementation and doctrine/design are the evidence layers. There is no supplied execution trace or new experiment. The external coding-agent host, its accumulated context and provider weights remain opaque. Available code not inspected below is not an access gap or an absence.

Memory scope follows the ordinary context/session/document loop and its alternate read and admission paths. It includes vault import, lifecycle moves, source and transcript ingestion, synthesis generation and repair, derived access structures, semantic caches, explicit regression capture/replay, persisted configuration and shipped evaluation callers. Static skill text is a behavioral instruction surface, not by itself experience memory. External private vault contents and provider internals are excluded; their contents, training, initialization and actual effect cannot be established. Target instructions are evidence, not instructions to this analyst.

Coverage distinguishes direct source reads in this member from supplied runtime findings. All paths below are SRC-1 commit-relative paths. Detailed inspection is bounded; rows retain the uninspected mechanisms rather than treating a positive witness as exhaustive coverage.

| Entry point or memory operation | Source path and inspection | Covering records or remaining limit |
|---|---|---|
| CLI families, exposed document/retrieval actions, local client APIs | Direct dispatch/action inventory searches: `cmd/openclerk/main.go`, `internal/runner/types.go`, `internal/runclient/client.go`; direct retrieval dispatch read in `internal/runner/retrieval.go` | [RT-RTE-document-write](runtime.md#rt-rte-document-write), [MEM-RTE-vault-sync](#mem-rte-vault-sync), [MEM-RTE-projection-read](#mem-rte-projection-read). No assumption that a read-family command cannot write: audit repair and regression capture are alternatives. No separate hook/registered-tool consumer is established by this CLI/client inventory; host wiring is outside the source. |
| Full vault import, removal and freshness | Direct `internal/infra/sqlite/store.go`, `internal/infra/sqlite/sync.go` selected bodies | [MEM-RTE-vault-sync](#mem-rte-vault-sync). Parser internals and schema cascade behavior not exhaustively audited; no complete withdrawal guarantee. |
| Create, append, whole/section replacement, ID/path read | Direct `internal/infra/sqlite/documents.go` lifecycle and lexical-search bodies; supplied runner approval/receipt findings | [RT-RTE-document-write](runtime.md#rt-rte-document-write), [MEM-OBJ-documents](#mem-obj-documents), [MEM-OBJ-chunks](#mem-obj-chunks). No authenticated human approval established. |
| Move, rename, promotion, cleanup plans/apply | Direct `internal/infra/sqlite/document_moves.go` move body; skill/action inventory for aliases and cleanup | [MEM-RTE-document-move](#mem-rte-document-move). Cleanup proposal algorithm/apply selection and alias-specific normalization not inspected; no claim that cleanup is globally safe or that promotion validates truth. |
| Context pack, explicit session/inbox planning | Supplied runtime plus direct `internal/runner/artifact_candidate_plan.go` intake/planning body | [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), [RT-RTE-session-plan](runtime.md#rt-rte-session-plan). OCR module/process internals and candidate confidence heuristics remain partly uninspected; derived preview is not parser truth. |
| URL/PDF/web ingestion and refresh | Direct creation and dependent-impact bodies in `internal/infra/sqlite/ingest_source.go` | [MEM-OBJ-source-assets](#mem-obj-source-assets); part of [RT-RTE-document-write](runtime.md#rt-rte-document-write). Update extraction/restore/network-validation internals not fully inspected; no comprehensive acquisition-integrity or rollback claim. |
| Video transcript intake | Direct create body in `internal/infra/sqlite/ingest_video.go`; skill doctrine | Same source object; caller supplies transcript/provenance, code renders note and optional metadata asset. Update internals uninspected; no automatic media/transcript acquisition established. |
| Synthesis create/update and disposable validation variant | Direct `internal/runner/compile_synthesis.go` generation/adoption and source-role conversion bodies | [MEM-RTE-synthesis-compile](#mem-rte-synthesis-compile). Disposable variant calls the compiler; runtime-binding validator internals not inspected, preventing a universal isolation claim. |
| Freshness, supersession, source audit repair, maintenance posture | Direct `internal/infra/sqlite/synthesis.go`, `internal/runner/audit_contradictions.go`, `internal/runner/maintenance_report.go` relevant bodies | [MEM-OBJ-projection-states](#mem-obj-projection-states), [MEM-RTE-synthesis-repair](#mem-rte-synthesis-repair). Conflict detection and wrapper-specific report conversion partly uninspected; no general contradiction resolution claim. |
| Lexical search, graph, records, services, decisions, provenance and report consumers | Direct search/dispatch, extraction witnesses in `internal/infra/sqlite/records.go`, `internal/infra/sqlite/services.go`, decision lookup in `internal/infra/sqlite/decisions.go`; rebuild dispatch in `internal/infra/sqlite/sync.go` | [MEM-RTE-projection-read](#mem-rte-projection-read) and separate objects below. Graph/record/service/decision merge, duplicate resolution and every report conversion not exhaustively inspected; no losslessness or authority-ranking claim. |
| Memory-router policy recall | Direct full `internal/runner/memory_router_recall.go` | [MEM-RTE-policy-recall](#mem-rte-policy-recall): hard-coded policy evidence, not a general memory router. |
| Explicit semantic retrieval, cache and module configuration | Supplied runner/provider findings plus direct cache functions in `modules/semantic-retrieval-adapter/main.go` | [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search), [RT-RTE-module-install](runtime.md#rt-rte-module-install), [MEM-OBJ-semantic-cache](#mem-obj-semantic-cache). Provider internals inaccessible; cache is not model training. |
| Regression capture/replay | Direct capture and replay bodies in `internal/runner/retrieval_eval.go` | [MEM-RTE-regression-replay](#mem-rte-regression-replay). File confinement/reader internals and sanitizer strength not audited; no privacy guarantee inferred from the label “sanitized.” |
| Configuration profiles, ignores and enabled modules | Supplied runtime; direct store ignore-loading and action inventory | [RT-RTE-module-install](runtime.md#rt-rte-module-install), [RT-RTE-document-write](runtime.md#rt-rte-document-write), [MEM-RTE-vault-sync](#mem-rte-vault-sync). Full config serialization/initial human control uninspected; configuration is symbolic access/admission state, not knowledge content. |
| Demo and evaluation producer/consumer, checkpoints | Supplied [boundary](boundary.md) and evaluation route; direct demo call-site search and skill policy | [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn). Demo reset/seed/answer bodies, Git checkpoint executor, evaluation telemetry and result bundles not independently inspected here; no observed score, automatic successor admission or complete checkpoint replay claim. |

## Core ideas

1. **Canonical files and executable consumers differ.** The product calls Markdown authoritative, but ordinary search and ID reads consume synchronized SQLite material. A raw disk edit does not thereby update a later read-only result. This follows from [MEM-RTE-vault-sync](#mem-rte-vault-sync), the direct `GetDocument` database read, and [RT-RTE-context-pack](runtime.md#rt-rte-context-pack). Authority is a contract about which evidence to trust, not a universal freshness gate.
2. **Retained content and retained access metadata have separate jobs.** Chunks and vectors select text; projection states and provenance describe derivation/currentness; neither is a preserved reasoning transcript. A synthesis note persists caller claims and some source-role facts. Its freshness is computed separately from timestamps and declared links, not established by its `freshness: fresh` frontmatter or an independent truth test ([MEM-RTE-synthesis-compile](#mem-rte-synthesis-compile), [MEM-OBJ-projection-states](#mem-obj-projection-states)).
3. **Session intake stops before durable adoption.** Explicit files can become candidate previews. Another request must admit the text into the document lifecycle. Automatic end-to-end transcript learning is not established by the session planner; the known transformation still exists even though initial human-versus-agent authorship and later acceptance are unknown ([RT-RTE-session-plan](runtime.md#rt-rte-session-plan)).
4. **“Recall” labels hide different selectors.** Ordinary task context uses lexical retrieval; explicit semantic retrieval uses a reusable vector cache; memory-router recall reads specific policy paths and emits largely code-authored summaries. None establishes that the external model obeyed returned evidence ([RT-RTE-context-pack](runtime.md#rt-rte-context-pack), [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search), [MEM-RTE-policy-recall](#mem-rte-policy-recall)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-documents
Label: Canonical documents

Source-native identity: vault Markdown and its SQLite `documents` mirror. Natural-language bodies and symbolic frontmatter are distinct operative parts: bodies reach humans/models as evidence; keys such as `status`, IDs and `source_refs` also drive fixed code rules. Storage substrate: vault files plus SQLite body/metadata/headings/timestamps. Lineage: user/agent text, imported existing files, extracted source text, or compiler/repair output. Initial author/human control is unspecified for imported files. Not a duplicate of [RT-OBJ-agent-contract](runtime.md#rt-obj-agent-contract), which identifies shipped instructions rather than evolving vault content; documents are state acted on by [RT-RTE-document-write](runtime.md#rt-rte-document-write), not the route itself.

The actual ID consumer reads the database, while mutation refreshes and synchronizes disk state. Canonical content has no TTL in these methods. The skill asks the external agent to prefer active canonical evidence, but content's actual influence is interpretive and unobserved. SRC-1, `internal/infra/sqlite/documents.go`, `skills/openclerk/SKILL.md`.

> SELECT doc_id, path, title, body, headings_json, metadata_json, created_at, updated_at
> FROM documents
> WHERE doc_id = ?
> --- `internal/infra/sqlite/documents.go`

#### MEM-OBJ-chunks
Label: Chunks and lexical index

Source-native identity: SQLite `chunks` and `chunk_fts`. Text sections remain natural language; IDs, line ranges, headings, FTS rows and lexical scores have symbolic access functions. These are derived from current parsed Markdown, not new experiential conclusions. Chunk content is distinct from its citation/access metadata. Search consumes these parts to select snippets, then callers can request full documents. Unlike [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), this is the underlying retained representation, not the selection route. SRC-1, `internal/infra/sqlite/sync.go`, `internal/infra/sqlite/documents.go`.

> INSERT INTO chunks (chunk_id, doc_id, path, heading, content, line_start, line_end)
> VALUES (?, ?, ?, ?, ?, ?, ?)
> --- `internal/infra/sqlite/sync.go`

#### MEM-OBJ-source-assets
Label: Source assets and extracted notes

Source-native identity: ingested PDF assets, web/PDF source notes, video transcript notes and optional video metadata assets. Storage substrate: vault files; source notes enter [MEM-OBJ-documents](#mem-obj-documents). PDF bytes are source payload, not their readable extracted display. Web ingestion creates extracted notes without a separate asset path; optional video assets are metadata, not downloaded media. Notes contain natural-language extraction/transcript plus symbolic URL/hash/capture/provenance fields. No newly trained model is involved in the inspected render/write bodies.

These are material outputs of the ingestion branches of [RT-RTE-document-write](runtime.md#rt-rte-document-write), with different raw provenance from arbitrary authored notes. Caller chooses URL/path or supplies transcript; code performs extraction/rendering and file I/O. Human per-content approval is not established merely because a caller initiated acquisition. Source refresh's known dependent-impact code explicitly leaves synthesis unrepaired. Consumers retrieve the note/citations; no automatic ordinary context-pack delivery of original PDF bytes or metadata asset is established. SRC-1, `internal/infra/sqlite/ingest_source.go`, `internal/infra/sqlite/ingest_video.go`.

> result.SynthesisRepaired = false
> --- `internal/infra/sqlite/ingest_source.go`

#### MEM-OBJ-record-entities
Label: Record entities

Source-native identity: record entities and facts derived from Markdown frontmatter and the `Facts` section. Storage substrate: SQLite projection tables; symbolic key/value organization carries natural-language values. Admission to this projection is a parser predicate, not separate human approval of every generated fact. Later consumers are records lookup/entity and report assembly in [MEM-RTE-projection-read](#mem-rte-projection-read); canonical document citations supply lineage. Distinct from [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), whose selected outputs are not the entity store. Full merge/conflict policy remains uninspected. SRC-1, `internal/infra/sqlite/records.go`, `internal/runner/retrieval.go`.

> if frontmatter["entity_type"] == "" && frontmatter["entity_name"] == "" {
>     return nil, nil, false, nil
> }
> return frontmatter, extractRecordFacts(lines, contentStart), true, nil
> --- `internal/infra/sqlite/records.go`

#### MEM-OBJ-service-records
Label: Service records

Source-native identity: service records/facts. Storage substrate: derived SQLite tables. Symbolic fields include ID, owner, interface and status; facts/summary text retain natural-language values. Lineage: service-specific frontmatter or `entity_type: service` fallback plus `Facts` extraction from Markdown. Code requires ID and name before projection; this is not evidence of content truth. Services lookup/detail are later consumers, separate from records even where inputs overlap; merge and conflict handling remain uninspected. No supplied object counterpart; [RT-RTE-context-pack](runtime.md#rt-rte-context-pack) is not this store. SRC-1, `internal/infra/sqlite/services.go`, `internal/runner/retrieval.go`.

> if projected.ServiceID == "" || projected.Name == "" {
>     return serviceProjection{}, false, nil
> }
> --- `internal/infra/sqlite/services.go`

#### MEM-OBJ-decision-records
Label: Decision records

Source-native identity: `decision_records`, derived by the decision rebuilder. Storage substrate: SQLite; symbolic status/scope/owner/date/supersession/source references accompany natural-language title/summary. Later consumers include decisions lookup/detail and [RT-RTE-context-pack](runtime.md#rt-rte-context-pack). Extraction/merging was not independently traced in full; source grounding here establishes retained fields and query filters, not faithful preservation of all decision rationale. Distinct state behind that supplied route, not a re-declaration of it. SRC-1, `internal/infra/sqlite/decisions.go`, `internal/infra/sqlite/sync.go`.

> SELECT decision_id, title, status, scope, owner, decision_date, summary, supersedes, superseded_by, source_refs, updated_at
> FROM decision_records
> --- `internal/infra/sqlite/decisions.go:57-58`

#### MEM-OBJ-graph
Label: Graph projection

Source-native identity: graph projection rebuilt from documents, exposed through document-link and neighborhood operations. Storage substrate: SQLite derived graph state; representational form: symbolic node/edge relationships and citation metadata rather than model weights. Supplied content may inform navigation, not an independent truth authority under the skill. No supplied object counterpart; [RT-RTE-context-pack](runtime.md#rt-rte-context-pack) is another consumer route, not the graph. Known rebuild and exposure are positive wiring witnesses; extraction limits, edge completeness and every report conversion remain uninspected. SRC-1, `internal/infra/sqlite/sync.go`, `internal/runner/retrieval.go`, `skills/openclerk/SKILL.md`.

> {name: "graph", supported: supportsGraph(s.backend), rebuild: s.rebuildGraph},
> --- `internal/infra/sqlite/sync.go`

#### MEM-OBJ-projection-states
Label: Projection states and provenance

Source-native identity: `projection_states` and provenance events. Storage substrate: SQLite. Both are symbolic metadata, not raw sessions, original full document versions or complete author reasoning. They are separated operationally: states describe the current derived view; events record transitions such as source updates and projection invalidation. `sync.go`'s generic document event retains path, not the whole preimage. Their actual consumers include audit/repair, maintenance, policy recall and explicit state/event requests. No supplied object counterpart; they are inputs to [RT-RTE-context-pack](runtime.md#rt-rte-context-pack)'s broader storage environment, not that route's identity.

For synthesis, `buildSynthesisProjectionState` requires a synthesis path/type, follows declared `source_refs`, detects missing/newer/superseded sources and hashes version inputs. It retains reasons, source-role lists and freshness. Those reasons are consumed by source-sensitive audits and policy recall; correctness beyond those predicates is not checked. Metadata state can change without rewriting synthesis prose. SRC-1, `internal/infra/sqlite/synthesis.go`, `internal/infra/sqlite/sync.go`, `internal/runner/audit_contradictions.go`, `internal/runner/maintenance_report.go`, `internal/runner/memory_router_recall.go`.

> if source.UpdatedAt.After(input.Document.UpdatedAt) {
>     staleRefs = appendUnique(staleRefs, ref)
>     reasons = appendUnique(reasons, "source newer than synthesis")
> }
> --- `internal/infra/sqlite/synthesis.go`

#### MEM-OBJ-semantic-cache
Label: Semantic retrieval cache

Source-native identity: `semantic_retrieval_adapter_cache.v1` JSON under the database directory's `cache/semantic-retrieval-adapter`. Vector parts are dense numerical representations, distributed-parametric in encoding but not provider model weights; schema/provider/model/hash/chunk identities are symbolic metadata. Lineage: selected corpus chunks embedded by [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider). The readable hit/snippet is not the vector payload. This distinct object is retained by [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search); it is not a second declaration of that route or provider.

Cache key includes provider, model, dimensions, filters and corpus hash. Reader checks schema/provider/model/corpus/count, per-chunk hash and nonempty vector, then copies cached vectors onto current chunks. This improves reuse capacity only in the ordinary caching sense; no retrieval-quality improvement or weight update is established. Exact provider weight version remains unpinned, so a cache hit does not settle semantic comparability across a mutable endpoint. Rebuild writes can fail without failing search, as supplied runtime records. SRC-1, `modules/semantic-retrieval-adapter/main.go`.

> rehydrated[idx].Vector = append([]float64(nil), cached.Chunks[idx].Vector...)
> --- `modules/semantic-retrieval-adapter/main.go`

#### MEM-OBJ-retrieval-cases
Label: Retrieval evaluation cases

Source-native identity: `openclerk-retrieval-eval.v1` JSONL cases. Storage substrate: local capture file resolved from runtime paths. Symbolic query/action/filter/result-reference/provider/latency/timestamp records; query text is natural language used as a later selector. This is a reduced retrieval trace, not raw conversation, document body or learned ranking policy. Later replay consumes cases as regression baselines, not truth labels. Distinct from [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn)'s Codex host traces and scenario oracle. SRC-1, `internal/runner/retrieval_eval.go`.

> retrievalEvalSchemaVersion        = "openclerk-retrieval-eval.v1"
> --- `internal/runner/retrieval_eval.go`

### Routes

#### MEM-RTE-vault-sync
Label: Vault synchronization

Endpoints/progression: explicit synced store open → scan configured vault → skip ignores/symlinks/non-Markdown → prune missing document rows → parse/import in batches → FTS and projection rebuild → later database readers. Owner: deterministic store code; caller chooses opening mode/configuration. Context: existing files and stored mirror. No counterpart to this whole route in supplied records: [RT-RTE-document-write](runtime.md#rt-rte-document-write) overlaps per-document synchronization but not whole-vault admission/removal. SRC-1, `internal/infra/sqlite/store.go`, `internal/infra/sqlite/sync.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: initialized store or error; sync diagnostics record progress.
- Later read-back: changed documents, chunks and projections feed later search/get/report calls; missing/ignored paths leave the imported document set after pruning.
- Delegated visibility: filesystem text reaches local parsers/database, not a separately isolated model frame.
- Selection predicate: configured root/ignore rules, `.md` extension, nonsymlink file; sorted paths, batches of 200, size/count limits and parse validation.
- Invalidation or expiry: content comparison skips unchanged imports; changed material marks rebuild pending; removal marks FTS/projection rebuild pending; no time-based expiry established.
- Activation or effect: derives executable access state and can withdraw indexed document rows; agent behavior and full deletion cascades are unobserved/uninspected respectively.
- Evidence limits: batched/database commits are not a whole-vault transaction; initialized read-only opens do not run full synchronization.

Admission: existing files are supplied by outside authors/editors whose per-content human control is unresolved. Import code admits parseable selected files, rejects errors, and mechanically derives chunks/indexes without separate semantic approval. This automatic transformation is known despite unknown initial authorship. No answer oracle or improvement criterion is used. Recovery is subsequent synchronization/rebuild; diagnostics and pending markers help distinguish partial progress. Read-only initialization is an important counterexample to a universal no-physical-write claim: an uninitialized database falls back to unsynced store creation, while an initialized read-only open loads existing state.

> if initialized, err := sqliteStoreInitialized(ctx, cfg.DatabasePath); err != nil {
>     return nil, err
> } else if !initialized {
>     return newStore(ctx, cfg, false)
> }
> --- `internal/infra/sqlite/store.go`

> if _, err := tx.ExecContext(ctx, `DELETE FROM documents WHERE doc_id = ?`, docID); err != nil {
>     return 0, domain.InternalError("delete missing document", err)
> }
> --- `internal/infra/sqlite/sync.go`

#### MEM-RTE-document-move
Label: Document move maintenance

Part of: [RT-RTE-document-write](runtime.md#rt-rte-document-write)

This narrows the supplied container's move branch, not its creation/replacement witness. Caller supplies source and target; code plans duplicate/stable-ID/link changes, refuses occupied targets, renames, rewrites selected links and synchronizes changed files, then records provenance. Owner: deterministic store and runner; host decides whether to submit the move. SRC-1, `internal/infra/sqlite/document_moves.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: move plan/result, applied link/index changes, provenance and projection freshness or rejection/error.
- Later read-back: future ID/path/link readers see synchronized moved documents and rewritten references.
- Delegated visibility: affected local file bodies reach rewrite code; caller receives results, not a delegated model.
- Selection predicate: explicit source/target plus plan-selected link updates; duplicate target veto; stable-ID addition where needed.
- Invalidation or expiry: new path and rewritten references replace prior locations; downstream refresh follows per-document sync, without route TTL.
- Activation or effect: durable structural curation; promotion changes placement, not independently checked truth or semantic warrant.
- Evidence limits: rename, subsequent body/link writes and sync are sequential; later failure can leave partial effects, not a guaranteed atomic move.

Admission and recovery: caller proposes location, code vetoes conflicts, and runner's mode policy applies. Human content approval remains as limited in [RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary). The early failed-frontmatter-write branch attempts rename restoration; later failures do not establish universal rollback. No answer oracle; open maintenance request, not evaluated improvement.

> if err := s.renameVaultPath(plan.SourcePath, plan.TargetPath, "move document file"); err != nil {
>     return domain.DocumentMoveResult{}, err
> }
> --- `internal/infra/sqlite/document_moves.go`

#### MEM-RTE-projection-read
Label: Retained projection reads

Endpoints/progression: explicit retrieval action → local client → chosen stored lexical/graph/record/service/decision/event/state operation → converted JSON → caller. Owner: code-defined selector, external agent owns interpretation. Distinct from [RT-RTE-context-pack](runtime.md#rt-rte-context-pack): these are independently exposed primitive alternatives; that route composes search/decision evidence for a task. Parts remain separate in the object declarations because encodings, checks and downstream roles differ. SRC-1, `internal/runner/retrieval.go`, `internal/infra/sqlite/documents.go`, `internal/infra/sqlite/decisions.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected snippets/citations or typed entities, relationships, decisions and access/lineage metadata.
- Later read-back: later requests consume already retained corpus/projection state; these read operations do not themselves adopt a new knowledge revision.
- Delegated visibility: converted fields cross the CLI boundary by value; full vault and omitted source rationale do not automatically reach the agent.
- Selection predicate: lexical query, path/metadata/tag filters, IDs, status/scope/owner or graph seed and limits according to action; not a shared universal authority rank.
- Invalidation or expiry: depends on separate synchronization/projection rebuild; a read does not inherently repair stale data.
- Activation or effect: data delivery and selection wired; compliance, complete context and answer improvement unobserved.
- Evidence limits: every composite report's conversion/omission was not inspected; no claim of lossless projection or preservation of all original reasons.

Context control here brings selected external material into a host invocation, not compaction of an accumulated window. Pagination/limits bound selected records, not a demonstrated tokenizer budget. IDs/citations are reload handles for another explicit request, not automatically dereferenced memory pointers. The ordinary lexical SQL ranks BM25 chunks and returns snippets/citations rather than whole bodies.

> ORDER BY bm25(chunk_fts), c.chunk_id
> LIMIT ? OFFSET ?
> --- `internal/infra/sqlite/documents.go`

#### MEM-RTE-synthesis-compile
Label: Synthesis compilation

Part of: [RT-RTE-document-write](runtime.md#rt-rte-document-write)

This is its distinct compiler branch: caller's source refs/body/facts → source evidence and role-fact selection → rendered synthesis → existing-target selection/create-or-replace → synchronized note and freshness/provenance result. Owner: code assembles/selects; caller authors requested claims, potentially through an external model. SRC-1, `internal/runner/compile_synthesis.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected path, created/updated/skipped status, evidence, projection freshness, provenance references and handoff.
- Later read-back: synthesis is a retained Markdown document available to future search/get, audit and policy recall; no compiler-owned host prompt injection.
- Delegated visibility: source citations/selected role facts reach compilation; resulting note/result reaches caller; provider reasoning is not included by this code.
- Selection predicate: explicit target, title, source refs and body/facts; existing candidate inspection chooses create/update, multiple target matches block.
- Invalidation or expiry: synthesis projection recomputes from source links/timestamps/supersession; future source changes do not automatically regenerate prose.
- Activation or effect: durable rendered/augmented synthesis, not independent factual verification; later model dependence unobserved.
- Evidence limits: missing source lookup produces a path citation and continues; `freshness: fresh` is authored frontmatter, not proof of fresh computed projection.

Admission: request plus runner restrictions govern application; code can veto duplicate target, but no independent per-claim human authenticator or answer oracle is shown. It preserves supplied body/facts and adds a narrow source-role transformation: superseded/current source labels and a specially prefixed Summary fact. This is automatic curation, not a general model-generated synthesis of all sources. Missing references can still be retained. Open create/update mode and disposable validation mode are separate contexts. No automatic rollback is shown in this compiler body; replacement recovery uses the broader lifecycle facilities when exposed.

> if !ok {
>     citations = append(citations, Citation{Path: ref})
>     continue
> }
> --- `internal/runner/compile_synthesis.go`

> "type: synthesis",
> "status: active",
> "freshness: fresh",
> "source_refs: " + strings.Join(input.SourceRefs, ", "),
> --- `internal/runner/compile_synthesis.go`

#### MEM-RTE-synthesis-repair
Label: Existing synthesis repair

Endpoints/progression: explicit audit plan/repair request → search/candidate inspection → exactly one existing synthesis → projection and source-event reads → current/superseded source classification → optional Summary replacement → refreshed state/report. Owner: deterministic audit code; caller chooses mode/target. No supplied route counterpart: it uses document replacement but is an independently admitted retrieval-family operation, unlike [RT-RTE-document-write](runtime.md#rt-rte-document-write)'s document-family entry. SRC-1, `internal/runner/retrieval.go`, `internal/runner/audit_contradictions.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected target, repair status, before/after projection state, inspected provenance and optional unresolved conflicts.
- Later read-back: applied Summary persists in canonical Markdown and derived storage for future retrieval/audit; plan-only report has no shown durable proposal queue.
- Delegated visibility: stored source summaries and metadata enter local repair code; caller receives report, not full hidden reasoning or an autonomous model frame.
- Selection predicate: exactly one target; both current and superseded path sets; nonempty Summary from the first current path after sorting.
- Invalidation or expiry: source-classification metadata can change; route reloads evidence rather than committing an earlier plan unchanged.
- Activation or effect: code rewrites a Summary when admitted; it explicitly does not settle unrelated unresolved claims.
- Evidence limits: selecting the first classified source is not content-directed truth adjudication; broad conflict extraction internals not traced here.

Admission: caller requests repair, runner opens writable state/lock for repair modes, and code can skip for duplicate/missing target or insufficient evidence. Human per-content review is unestablished. There is no reference-answer oracle; projection source roles supply the computational criterion, not guaranteed correctness. Replacement retains a current summary, current/superseded paths and a scope disclaimer, not the complete audit reasoning or full source histories. Later search gets that reduced text; later audit can separately read projection reasons/events. Recovery requires another explicit lifecycle operation; no automatic reversal is shown here.

> "Current source summary: " + currentSummary,
> "Current source: " + currentSourcePaths[0],
> "Superseded source: " + supersededSourcePaths[0],
> "Audit repair did not choose unresolved claims beyond source classification.",
> --- `internal/runner/audit_contradictions.go`

#### MEM-RTE-policy-recall
Label: Memory-router policy recall

Endpoints/progression: requested report/query → ordinary search → paginated lookup of fixed policy files and synthesis → session provenance/synthesis state → code-generated summaries and handoff. Owner: Go rules, not an autonomous router. Distinct from [RT-RTE-context-pack](runtime.md#rt-rte-context-pack): the query's search hit count does not determine these fixed evidence paths. SRC-1, `internal/runner/memory_router_recall.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: temporal/advisory/routing/freshness summaries, canonical refs, missing-evidence warnings and handoff.
- Later read-back: later requests read retained policy Markdown plus event/state evidence; this route does not update feedback weights or session policy.
- Delegated visibility: code reads full fixed document bodies, but delivers summaries/references rather than all body text to caller.
- Selection predicate: four fixed `notes/memory-router/` paths and one synthesis path; per-path token-presence tests; query affects initial search/count. Default limit 10, with paginated document scans and separately bounded event/state queries.
- Invalidation or expiry: synthesis freshness and required source-ref checks affect warnings; token-presence success is not semantic validation or expiry enforcement.
- Activation or effect: report assembly wired; no implemented autonomous feedback-weight update or routing decision established by this function.
- Evidence limits: feedback/routing summary statements are code-authored based on file presence; a label saying evidence was inspected does not imply all policy content was interpreted.

The hard-coded selector is a counterexample to treating all “recall” as task-targeted retrieval. Its authority statements are descriptive/requested policy; they do not implement a hidden rank that makes stale evidence impossible to consume. The returned handoff's answer summary is the query/count summary, while specialized temporal/feedback/routing details remain other report fields.

> if docs[memoryRouterFeedbackPath].Found {
>     return "feedback weighting is advisory only and cannot hide stale or conflicting canonical evidence"
> }
> --- `internal/runner/memory_router_recall.go`

#### MEM-RTE-regression-replay
Label: Retrieval regression replay

Endpoints/progression: explicit opt-in capture → execute selected search → append reduced JSONL case → later explicit replay → reissue captured selectors → compare references/latency → caller report. Owner: deterministic runner. Unlike [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn), no external coding-agent session is needed in this route; semantic capture may invoke the supplied embedding path. SRC-1, `internal/runner/retrieval_eval.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: capture row/path/write status or replay case comparisons and aggregate Jaccard/top1/latency summary.
- Later read-back: captured query/action/filters drive later searches; result references supply the comparison baseline.
- Delegated visibility: replay delivers comparisons to caller; captured rows omit document bodies/snippets in the inspected row construction.
- Selection predicate: caller explicitly chooses search or semantic search/capture path; replay limit defaults 100 and caps at 1000.
- Invalidation or expiry: subsequent retrieval changes can alter overlap; captured baseline is not automatically promoted or overwritten as truth by replay.
- Activation or effect: retained trace enables regression checking; this route does not itself install a new ranker or revise canonical notes.
- Evidence limits: reference agreement is not answer correctness; stored query sanitization is named but its adequacy was not audited; no observed regression outcome.

Admission: caller opts into artifact capture and runner applies its write restrictions; software constructs/appends each row. This is not human per-row content approval. Replay is a bounded comparison with captured outputs as an oracle for sameness, not an expected correct answer. Reports ask for further inspection before defaults change. No automatic behavior-shaping derived update follows the trace in these bodies, so raw/reduced trace retention must not be called learned ranking. Artifact deletion/recovery internals remain uninspected.

> FollowUpPrimitiveInspection: "inspect cases with low jaccard or top1 mismatch using search, semantic_search, provenance_events, and projection_states before changing defaults",
> --- `internal/runner/retrieval_eval.go`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-evidence
Label: Retained evidence handoff

Consumer: external coding agent using retrieval/task context. Channel: selected JSON snippets, summaries, citations and report fields from retained Markdown/projections. Force: evidence and natural-language authority guidance, not an OS-enforced instruction priority. Horizon: later tasks/sessions that invoke retrieval, bounded by selected content and host retention. This is distinct from [RT-BAP-skill-routing](runtime.md#rt-bap-skill-routing): that path carries shipped behavioral instructions; this one carries evolving knowledge evidence that those instructions ask the agent to use. Interpretive influence is afforded/wired delivery, not observed compliance or benefit. SRC-1, `skills/openclerk/SKILL.md`, `internal/runner/retrieval.go`, `internal/runner/memory_router_recall.go`; [RT-RTE-context-pack](runtime.md#rt-rte-context-pack) supplies the task-context witness.

> Canonical markdown remains
> authoritative over derived service, record, decision, and synthesis projections.
> --- `skills/openclerk/SKILL.md`

## Annotations

#### On [RT-RTE-context-pack](runtime.md#rt-rte-context-pack)

Read-back is requested, not unsolicited: user/agent task/query triggers deterministic external-material selection. Selected natural-language snippets and decision summaries travel inside symbolic JSON. The count limit is not a demonstrated token-window budget. Citations leave omitted material reachable only through another explicit operation; host eviction, summaries, tail retention and reload after compaction remain uninspected. Selection of material outside a model context fits a reload metaphor, but values delivered into context are not live database references. Storage freshness is separate from successful delivery; see [MEM-RTE-vault-sync](#mem-rte-vault-sync).

#### On [RT-RTE-session-plan](runtime.md#rt-rte-session-plan)

Directly inspected SRC-1, `internal/runner/artifact_candidate_plan.go`, adds the raw-to-candidate step: explicit `Content`/`Body` takes precedence; otherwise extracted local content is used. Code infers kind/title/path/tags/metadata, builds body preview, searches duplicates and emits next create/ingest requests. Local text/PDF has a 10 MB planning read limit. OCR review is explicitly requested and attaches extraction provenance, but process correctness is uninspected here. The local artifact SHA/filename/size is access/provenance metadata, not its readable body. Plan output has `planned_no_write`; no retained derived-memory consumer exists until a later accepted lifecycle request. Possible session origins include handoff, authored note and log; whole host transcripts, automatic compaction and source rationale preservation are not implied.

> WriteStatus:             "planned_no_write",
> --- `internal/runner/artifact_candidate_plan.go`

#### On [RT-RTE-document-write](runtime.md#rt-rte-document-write)

Direct store inspection establishes automatic post-admission refresh, chunk/FTS derivation and projection invalidation. Physical I/O, caller authorship, symbolic mode admission and human content decision remain separate. Imported files, extracted sources, compiler output and repaired summaries can all enter the same canonical-file substrate with different provenance. Replacement preimage receipts are compensating-request data, not a demonstrated durable full-version history. Move and compiler branches are separately declared parts above. Source/transcript acquisition parts remain locally bounded in the coverage table and [MEM-OBJ-source-assets](#mem-obj-source-assets).

#### On [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search)

[MEM-OBJ-semantic-cache](#mem-obj-semantic-cache) is the retained numerical result and symbolic identity metadata read on a subsequent explicit semantic query. Automatic cache acceptance is a software decision after embedding and validation, not separate human approval of each vector. Query text drives current selection; corpus content supplies the cached representation. The stored vectors do not retain provider reasoning or a formulated explanation of relevance. Cache rebuild is derived-content curation, not trace-fed host-session learning. Installed provider configuration and mutable model identity retain the supplied limits.

#### On [RT-RTE-module-install](runtime.md#rt-rte-module-install)

Persisted symbolic configuration is consumed by later module dispatch and can enable/disable a capability. It is not knowledge content, model weights or the semantic cache itself. Caller initiation does not establish a human decision about each configured value. Removal withdraws future configured access, not prior cached bytes, disclosures or arbitrary earlier subprocess effects.

#### On [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn)

Raw stdout/JSONL/stderr, parsed final output and host session ID have different roles: traces support inspection, final output is task return, session ID is a handle for the external host's retained session. The actual host-retained payload, compaction/checkpoint representation and selector are opaque. Future turns also consume changed local scenario knowledge through the normal document/retrieval paths. Single-turn ephemeral mode limits requested host continuity, not persistence of seeded/mutated vault files. No trace-to-revised-product automatic adoption chain is established by this supplied route.

## Write side

Acquisition has several entry points rather than one “remember” operation. Authored and imported Markdown enters the store; PDF/web text and supplied video transcripts are rendered into source notes; explicit session files become candidate previews; compiler/repair functions produce document revisions. Each known automatic transform is retained even when original human control is unknown. Admission is governed by different mechanisms: file selection/parsing for import, runner mode/path checks for document actions, exactly-one-existing-target/source-classification rules for repair, cache identity validation for vector reuse, opt-in artifact capture for regression traces, and module binding/configuration checks for capabilities. Starting any workflow is not per-content human approval ([RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary)).

The most concrete automatic semantic curation witness is [MEM-RTE-synthesis-repair](#mem-rte-synthesis-repair): stored source-role metadata selects a current Summary and replaces a synthesis Summary with source labels/disclaimer. It is not merely a trace log, but it is also not general criticism of every claim. Compiler assembly preserves caller claims and source references without independently proving them. Full reasons may survive in caller prose, but code does not require them. Projection freshness retains narrow computed reasons that later audit/maintenance reads. Generic provenance events retain transition metadata, not necessarily the old document body.

Withdrawal is also split. Refused plans/duplicate targets do not create a document in their checked paths. Missing/ignored files are pruned on full sync, not automatically whenever a read occurs. Supersession can retain old source documents and add stale/current-role metadata rather than delete old text. Source refresh reports dependent staleness but explicitly does not repair synthesis. Move changes paths and references with partial-failure exposure. Module disable removes future configured capability use, not prior data. General filesystem/database/cache/host erasure, complete version recovery and all cleanup apply rules remain uninspected ([MEM-RTE-vault-sync](#mem-rte-vault-sync), [MEM-RTE-document-move](#mem-rte-document-move), [MEM-OBJ-source-assets](#mem-obj-source-assets)).

Trace-fed paths have different endpoints. Session artifact → candidate → separately admitted document can preserve experience, but automatic durable adoption is unestablished. Retrieval execution → reduced JSONL → later replay is a wired trace-to-evaluator chain, not a new behavior-shaping ranker. Evaluation host session continuity is wired externally, but its alternative checkpoints/compaction payloads are opaque. No complete raw-session → automatic summary/checkpoint → later model consumption chain can be asserted from these inspected files; that is a named host inspection limit, not a system-wide absence or a reason to suppress the known planning/caching transformations.

## Read-back

The main read-back is a request chain: agent task/query → deterministic search/decision selector → context pack by value → external model. Primitive get/search/typed/graph reads and promoted reports are alternate request routes. Fixed policy recall is a separate selector: it reads named policy documents regardless of the initial query's retrieved hits. Explicit semantic queries reuse stored document vectors and embed current query text; default lexical context does not silently become semantic ([RT-RTE-context-pack](runtime.md#rt-rte-context-pack), [MEM-RTE-projection-read](#mem-rte-projection-read), [MEM-RTE-policy-recall](#mem-rte-policy-recall), [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search)).

Read-back consumers receive transformed fields, not everything the producer held. Chunks become snippets/citations, formal decisions become summaries, policy bodies become code-authored status statements, provenance becomes references, and vectors become ranked text hits. The skill asks the agent to preserve authority limits and freshness; it does not guarantee that all consumers will see or honor them. External host context lifetime, token budgeting, isolation and compaction are uninspected. Report count/byte limits and subprocess decoding bounds must not be relabeled as model context-window management.

A storage API alone would not establish an external reader; here shipped retrieval dispatch, Chronicler context construction and evaluation turn continuation supply actual wired consumers. In contrast, original PDF bytes, optional video metadata assets and generic historical preimages have no established automatic ordinary-agent read-back in this inspection. Their retention is a storage/acquisition fact, not evidence that the model consumes them. Regression replay's later consumer is deterministic comparison code, not the ordinary answer model ([MEM-OBJ-source-assets](#mem-obj-source-assets), [MEM-RTE-regression-replay](#mem-rte-regression-replay)).

## Integration issues

- **Qualification to read-only terminology:** [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search) already distinguishes writable cache from canonical read-only access. Additionally, `internal/infra/sqlite/store.go`'s read-only constructor initializes an uninitialized database via `newStore(..., false)`. [MEM-RTE-vault-sync](#mem-rte-vault-sync) preserves this physical-initialization counterexample; no contradiction to Chronicler's no-document-write planning claim is asserted. Consequence: do not infer that every “read-only” surface has zero filesystem/database effects.
- **Supplied route scope is not exhaustive:** [RT-RTE-document-write](runtime.md#rt-rte-document-write) is explicitly a creation/replacement witness with broader branch inventory. [MEM-RTE-document-move](#mem-rte-document-move) and [MEM-RTE-synthesis-compile](#mem-rte-synthesis-compile) are declared parts. [MEM-RTE-synthesis-repair](#mem-rte-synthesis-repair) is an alternate retrieval-family admission path; its approvals and selection must not disappear into the document-family account. No supplied fact is otherwise corrected.
- **Identity comparisons:** no possible duplicate remains after comparison with supplied records. Underlying document/chunk/typed/graph/metadata/cache/trace objects are distinct from runtime routes and provider/instruction objects. [MEM-BAP-retained-evidence](#mem-bap-retained-evidence) carries evolving evidence; [RT-BAP-skill-routing](runtime.md#rt-bap-skill-routing) carries shipped behavioral instructions. Shared consumers do not make the payloads identical.
- **Freshness versus correctness:** [MEM-OBJ-projection-states](#mem-obj-projection-states) and [MEM-RTE-synthesis-compile](#mem-rte-synthesis-compile) show computed metadata checks and rendered freshness labels, not truth adjudication. Missing-reference continuation and narrow source-role repair prevent a universal claim of verified knowledge admission.
- **Read-back omissions:** full graph/typed projection merge/conflict rules, every composite report conversion, source update restore paths, cleanup apply rules, Git checkpoint behavior and demo/evaluation artifact consumers are available but partly uninspected. Their paths and prevented conclusions remain in the coverage table. No exhaustive trust/freshness/withdrawal equivalence is claimed across them.
- **Host retention:** [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn) identifies session ID continuation but not payload/checkpoint/compaction internals. It cannot settle whether host-derived summaries retain rationale or how removed context is recovered. Provider parameter changes and exact embedding versions likewise remain uninspected under [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider).

## Limitations and checks

Source identity was rechecked with `git rev-parse HEAD`: `092fb98d243c2d9d95867ad04618ebce88983552`; `git status --short` reported no changes. All additional source reads are SRC-1 implementation/doctrine at that boundary. No external source, prior analysis, target execution, test, provider call or experiment was used. Governing invocation, member/input types, supplied boundary/runtime, collection, worker rules and complete records contract were read; required ranged inputs were recovered before source analysis.

The inventory is not a full implementation audit. Unknowns remain attached to the relevant surfaces, especially initialization's human control, opaque host/provider state, detailed projection conflicts and compound-report omissions. No operation, causal benefit, automatic whole-session learning or exercised self-improvement is claimed. Static skills and retained knowledge can shape future action through separate authority paths without establishing that they did so in a run.

Validation: the required `commonplace-run validate-output` check passed after disambiguating the decision-record query quotation with the validator-supplied source range. Validation establishes form and quotation occurrence, not semantic completeness or acceptance.
