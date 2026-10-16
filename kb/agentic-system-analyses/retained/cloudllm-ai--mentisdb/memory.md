---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MentisDB memory: thought content, derived retrieval state, checkpoint selection, instruction versions and lossy import/export at the frozen Rust/Python boundary."
run-id: AAS-2026-10-14-mentisdb-a8b5903ae3e2-01
source-identity: "https://github.com/cloudllm-ai/mentisdb"
reviewed-boundary: "4c9b95041da68c5a26dece9f8776ff54b05b910c"
---

# MentisDB memory report

## Boundary and evidence

MentisDB retains structured thoughts and versioned instruction documents, derives retrieval indexes from that state, and exposes request-driven ways to return it. This report includes the Rust chain, REST/MCP operations, CLI admission/search, dashboard import/copy/deletion, Python prompt adapter, operating skill, retrieval maintenance, webhooks and shipped retrieval evaluators. It uses SRC-1 at commit `4c9b95041da68c5a26dece9f8776ff54b05b910c`, with the whole-system functional boundary supplied by `boundary.md`. External host execution, dependency internals, downloaded weights, providers and deployed chain contents remain outside frozen evidence. These exclusions prevent conclusions about actual instruction obedience, provider accuracy, deployed visibility or task benefit.

Direct inspection added bounded source reads of summary selection, context bundles, invalidation/deduplication, embedding inputs and sidecar rebuilding, implicit-edge updates, Markdown export/import, dashboard agent copying and chain deletion, webhook dispatch/retries, CLI add/search and evaluator matching. Full reads covered `MENTISDB_SKILL.md`, `pymentisdb/langchain.py`, `src/search/summary_index.rs` and `src/search/bundle.rs`. Other large modules were inspected by named functions/ranges and bounded searches. The supplied runtime is a provisional implementation trace, not an execution record. Its quoted passages supply evidence for routes annotated below; additional findings cite directly inspected SRC-1 paths. No program, example, benchmark, test, model or service was executed.

### Coverage inventory

“Direct” means source inspection in this job; “supplied” means the runtime's findings. Neither establishes observed operation. Unresolved rows are included responsibilities, not exclusions or evidenced absences.

| Entry point / memory operation | Source path and evidence basis | Covering records or local limit |
|---|---|---|
| Binary daemon/headless/combined, local/proxied stdio; HTTP REST/MCP and legacy tool dispatch | SRC-1, `src/bin/mentisdb.rs`, `src/server.rs`; supplied transport trace, direct searches of registered operations | [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [RT-RTE-access-control](runtime.md#rt-rte-access-control). Transport differences do not create a universal admission envelope. |
| CLI add/search | SRC-1, `src/cli/mod.rs`; direct dispatch and HTTP callers | [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip). Explicit caller supplies content; code posts to shared REST admission, not a separate review workflow. |
| Bootstrap, append, retrospective append, direct Rust append, reopen | SRC-1, `src/server.rs`, `src/lib.rs`; supplied open/storage and direct append/retrospective reads | [RT-OBJ-thought](runtime.md#rt-obj-thought), [MEM-OBJ-thought-content](#mem-obj-thought-content); roundtrip annotation. Retrospective defaults a type/role; it does not itself derive lessons from a trace. Bootstrap initial content remains caller supplied. |
| Correction, invalidation and optional lexical deduplication | SRC-1, `src/lib.rs`, `MENTISDB_SKILL.md`; direct | [MEM-RTE-correction-update](#mem-rte-correction-update). Automatic replacement is similarity-driven, not verified correction. |
| Flat query, lexical/ranked search, ancestor traversal, federated search, point-in-time filtering | SRC-1, `src/lib.rs`, `src/server.rs`; supplied ancestor trace; direct ranked/federated/filter reads | Roundtrip annotation; [MEM-OBJ-retrieval-state](#mem-obj-retrieval-state). Flat and federated routes differ in thesaurus application. |
| Exact thought/genesis/history traversal and bootstrap prompt | SRC-1, `src/server.rs`, `src/lib.rs`; registered-tool inventory, supplied API trace | Alternative addressed/full-history access, not proof of topical selection or automatic prompt loading. Detailed invalidation behavior of every exact/history handler not inspected; cannot generalize ranked filtering to them. |
| Recent-context and direct catch-up prompt | SRC-1, `src/server.rs`, `src/lib.rs`; direct | Roundtrip annotation. Service filters invalidation before rendering; direct `to_catchup_prompt` takes an unfiltered tail. |
| Context bundles, dashboard bundle search | SRC-1, `src/search/bundle.rs`, `src/lib.rs`, `src/server.rs`, `src/dashboard.rs`; direct core/service, dashboard handler inventory | [MEM-RTE-bundle-read](#mem-rte-bundle-read). Dashboard-specific option defaults not fully traced. |
| Summary candidate tool/service/library; host checkpoint instructions | SRC-1, `src/search/summary_index.rs`, `src/lib.rs`, `src/server.rs`, `MENTISDB_SKILL.md`; direct | [MEM-OBJ-summary-candidate](#mem-obj-summary-candidate), [MEM-RTE-summary-selection](#mem-rte-summary-selection), [RT-BAP-core-skill](runtime.md#rt-bap-core-skill). Selection is not summary generation or host compaction. |
| Python message storage and prompt-variable loading | SRC-1, `pymentisdb/langchain.py`; direct full read | Roundtrip annotation, [MEM-OBJ-thought-content](#mem-obj-thought-content). Raw messages can be labelled Summary; session field does not isolate this route. |
| Optional extraction | SRC-1, `src/llm.rs`, `src/server.rs`; supplied extraction trace; direct library forwarding search | [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction). No durable result until separate append; provider state/retention unresolved. |
| Skill upload/search/version/read; deprecate/revoke/delete; dashboard upload | SRC-1, `src/skills.rs`, `src/server.rs`, `src/dashboard.rs`; supplied upload/persistence, direct read snapshots | [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [MEM-OBJ-skill-body](#mem-obj-skill-body). Lifecycle status and document warnings are different returned fields. |
| Managed vectors, sidecar/WAL/HNSW rebuild and implicit semantic neighbors | SRC-1, `src/lib.rs`, `src/search/vector.rs`, `src/search/implicit_edges.rs`; direct | [MEM-OBJ-embedding-vector](#mem-obj-embedding-vector), [MEM-OBJ-retrieval-state](#mem-obj-retrieval-state), [MEM-RTE-derived-update](#mem-rte-derived-update). Full WAL replay, HNSW persistence and all metadata-change invalidation cases remain uninspected; no exhaustive freshness assurance. |
| Query expansion, PPR, query intent, lexical internals and embedding synonyms | SRC-1, `src/search/mod.rs`; direct module/export inventory; core ranked wiring inspected | Available alternative retrieval machinery; full utility callers and all weighting/expansion internals not inspected. Cannot claim every exported helper is used in the ordinary daemon route. |
| Markdown export/import through service, dashboard and library | SRC-1, `src/lib.rs`, `src/server.rs`, `src/dashboard.rs`; direct | [MEM-OBJ-memory-markdown](#mem-obj-memory-markdown), [MEM-RTE-markdown-exchange](#mem-rte-markdown-exchange). Export is a formatted view, not a guaranteed complete semantic summary or faithful backup. |
| Branch, merge, archive backup/restore | SRC-1, `src/lib.rs`, `src/server.rs`, `src/backup.rs`, `src/cli/mod.rs`; supplied baseline, direct branch/merge inventory | [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance). Supplied limits on graph loss and partial writes retained; full archive conflict reconciliation not inspected here. |
| Dashboard agent-copy and whole-chain deletion | SRC-1, `src/dashboard.rs`, `src/lib.rs`; direct | [MEM-RTE-agent-copy](#mem-rte-agent-copy), [MEM-RTE-chain-withdrawal](#mem-rte-chain-withdrawal). Copy drops graph lineage; deletion defeats a universal “forever-record” reading. |
| Agent/entity registries, access grants and service interaction logs | SRC-1, `src/lib.rs`, `src/server.rs`; supplied registries/access plus direct embedding/log reads | [MEM-OBJ-retrieval-state](#mem-obj-retrieval-state), [RT-RTE-access-control](runtime.md#rt-rte-access-control). Attribution/search metadata and access policy are not substantive learned memories. Logs' complete file rotation/reload consumers remain uninspected. |
| Append callbacks and webhooks | SRC-1, `src/lib.rs`, `src/server.rs`, `src/webhooks.rs`; direct | [MEM-RTE-webhook-delivery](#mem-rte-webhook-delivery). Push of the new event, not selected historical read-back; external later retention unknown. |
| TUI and host integration writers | SRC-1, `src/tui.rs`, `src/integrations/mod.rs`, `src/integrations/targets/codex.rs`, `src/integrations/targets/claude_code.rs`, `src/integrations/targets/opencode.rs`; direct function/hook search, supplied integration trace | TUI display/copy/update controls and host connection configuration are not demonstrated automatic memory consumption. Full key-event loop and every integration target remain uninspected; no universal host-hook guarantee. |
| Retrieval evaluation and retained diagnostics | SRC-1, `lme-benches/longmemeval_bench.py`, `lme-benches/convomem_bench.py`, `locomo-benches/locomo_bench.py`; direct ingest/matching/evaluate/output searches | [MEM-RTE-retrieval-evaluation](#mem-rte-retrieval-evaluation). Rust tests and benchmark suites remain supplied inventory, not fresh results or automatic model-learning consumers. |

## Core ideas

1. **Memory meaning and memory control are separate.** Thought text can contain facts, raw conversation, a checkpoint or a rule. UUIDs, types, hashes, tags and relations govern storage and selection; they do not validate the text. Content becomes guidance only through a later interpreter. The Python producer stores both human and assistant messages under the same configured type, ordinarily Summary, without summarizing them. See [MEM-OBJ-thought-content](#mem-obj-thought-content) and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).
2. **Replacement usually hides rather than erases.** An admitted `Corrects`, `Invalidates` or `Supersedes` relation updates an exclusion set used by ordinary query paths. Old text remains in the canonical history. Configured token-set deduplication can create the same exclusion without a factual judgment. Audit options, direct renderers and lossy copies/imports challenge any system-wide guarantee that stale claims never reach consumers. See [MEM-RTE-correction-update](#mem-rte-correction-update), [MEM-RTE-markdown-exchange](#mem-rte-markdown-exchange) and [MEM-RTE-agent-copy](#mem-rte-agent-copy).
3. **Context selection is implemented; context discipline is mostly delegated.** Recent context, scored retrieval and lexical-seed bundles restrict delivered records. Summary candidates identify windows; they do not generate or append summaries. The operating skill asks agents to checkpoint before compaction and prepare shared memory before spawning. No host window eviction, frame isolation or obedience follows from that request. See [MEM-RTE-summary-selection](#mem-rte-summary-selection), [MEM-RTE-bundle-read](#mem-rte-bundle-read) and [RT-BAP-core-skill](runtime.md#rt-bap-core-skill).
4. **Derived state shapes retrieval without replacing source text.** Embedding vectors and semantic-neighbor overlays are automatic derivatives with numerical/symbolic authority at the search code, not new verified propositions. Selected original content reaches downstream prompts. Instruction-version deltas likewise reconstruct bodies; version ordering is not quality selection. See [MEM-RTE-derived-update](#mem-rte-derived-update) and [MEM-OBJ-skill-body](#mem-obj-skill-body).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-thought-content
Label: Thought content
Part of: [RT-OBJ-thought](runtime.md#rt-obj-thought)

Source-native identity: `Thought.content`, distinct from the parent's symbolic envelope. Representational form: ordinarily natural-language statements/messages, with arbitrary caller text also possible; no semantic interpretation is enforced at append. Storage substrate: the parent's canonical binary or JSONL/custom-adapter chain and loaded thought collection. Lineage: explicit author/caller input, Python raw message, imported Markdown, copied thought or separately admitted extracted candidate. Roles and type labels do not prove which transformation occurred. SRC-1, `src/lib.rs`, `src/server.rs`, `pymentisdb/langchain.py`.

Later consumers include human/API clients, host agents receiving recent/ranked context and the Python prompt formatter. Authority is knowledge or instruction only at the interpreting consumer; storage/selection is fixed code. Reasons can live in content and linked thoughts but are not required, nor automatically followed by the Python adapter or recent-context renderer. Distinct material part: the runtime explicitly separates content from the envelope; this is not a duplicate envelope declaration.

> Each message is converted to a Thought with:
> - HumanMessage -> ThoughtType.SUMMARY with role Memory
> - AIMessage -> ThoughtType.SUMMARY with role Memory
> --- `pymentisdb/langchain.py`

The implementation passes `msg.content` directly with the configured type. Thus raw conversational traces remain raw despite their default Summary label. No observed learned heuristic or improved capacity is established by that write.

#### MEM-OBJ-skill-body
Label: Reconstructed skill instruction body
Part of: [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry)

Source-native identity: uploaded raw skill document and `SkillReadOutput.content`, reconstructed via `read_skill_from_entry`. Representational form: natural-language instruction sections; document metadata and lifecycle machinery remain symbolic parts of the parent. Storage substrate: full initial text plus later delta content in the bincode registry; requested-format export is transient text. Lineage: caller upload, structural import/validation, immutable version storage, patch reconstruction, document parsing and export. No live uploaded instruction or reasoned revision history was supplied. SRC-1, `src/skills.rs`; upload/persistence passages in [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission).

The consumer receives rendered content, document warnings and the entry's lifecycle status. `status_reason` retained on the entry is not itself copied into `warnings` by the inspected reader. This distinction matters: a revoked document with no authored warnings can still return content and empty warnings alongside Revoked status. Execution avoidance depends on the downstream reader checking status as well as document notices. Authority is conditional natural-language guidance, not an enforced skill execution ban.

> Ok(SkillReadOutput {
>     content: snapshot.content,
>     warnings: snapshot.warnings,
>     status: entry.status,
> })
> --- `src/skills.rs`

The material part is instruction content, not a replacement for the registry container. Earlier-version addressing affords textual recovery; it does not roll back an external host automatically.

#### MEM-OBJ-embedding-vector
Label: Thought embedding vector

Source-native identity: `VectorSidecarEntry.vector` and provider-generated `EmbeddingVector.values`. Representational form: distributed-parametric dense numerical representation, not model weights or a readable memory summary. Storage substrate: managed vector sidecar snapshot/WAL and cached vector backend; exact persistence internals are not exhaustively inspected. Lineage: `thought_embedding_text` combines content, concepts, tags and available agent display name, aliases, owner and description; selected provider embeds it. SRC-1, `src/lib.rs`, `src/search/vector.rs`.

Consumer: later vector ranking and implicit-neighbor derivation, under fixed code rules. It has selection authority, not proposition authority. Parent thought text remains separately readable. Closest supplied record is [RT-CMP-fast-embed-provider](runtime.md#rt-cmp-fast-embed-provider), which denotes provider weights/inference rather than each retained output vector; no supplied output-vector counterpart. Provider/model fixity and fallback limits remain in that component. The local hash-based provider is a separate implementation alternative, not trained MiniLM weights.

> pub struct EmbeddingVector {
>     /// Dense numeric representation in the provider's embedding space.
>     pub values: Vec<f32>,
> }
> --- `src/search/vector.rs`

#### MEM-OBJ-retrieval-state
Label: Derived retrieval indexes and semantic neighbors

Source-native identity: query/lexical indexes, UUID/hash lookup, invalidation set, explicit adjacency, `ImplicitEdgeOverlay` and registry metadata used to construct retrieval inputs. Representational form: symbolic lookup/filter/graph structures with numeric scores, distinct from dense embeddings and natural-language thought content. Storage substrate: rebuilt in-memory indexes; persisted agent/entity/chain metadata and implicit-edge binary overlay; HNSW backend files are additional derived retrieval substrate whose full persistence was not inspected. SRC-1, `src/lib.rs`, `src/search/mod.rs`, `src/search/implicit_edges.rs`.

Lineage: admitted thoughts and metadata → index observation/rebuild; vector sidecar → threshold/top-K neighbors → overlay. Consumer: code selecting candidates and expanding graph paths. Authority: procedural selection, not validation of the semantic truth of an edge. `RelatedTo` neighbors are inferred similarity, unlike caller-authored reasons in typed relations. Closest supplied object [RT-OBJ-thought](runtime.md#rt-obj-thought) is the canonical source envelope, not these derived indexes; no counterpart after comparison. This grouped record describes symbolic retrieval state, not a declaration of every index's identical lifecycle.

> pub struct ImplicitEdgeOverlay {
>     /// Source thought id → top-K nearest neighbors above threshold.
>     pub edges: HashMap<Uuid, Vec<ImplicitNeighbor>>,
>     /// Threshold used when this overlay was built.
>     pub threshold: f32,
>     /// K used when this overlay was built.
>     pub k: usize,
> }
> --- `src/search/implicit_edges.rs`

Interaction logs are separate access/operation diagnostics, optionally written when verbosity or a log file is enabled. The inspected `log_interaction` does not turn them into thought content or a learned rule. Their later file-reading consumers remain uninspected. SRC-1, `src/server.rs`.

#### MEM-OBJ-summary-candidate
Label: Summary source candidate

Source-native identity: `SummaryCandidate` carrying indices, IDs, group and start/end bounds. Representational form: symbolic source-window descriptor, not summary prose. Storage substrate: transient library/service response; the candidate selector does not persist it. Lineage: committed thought metadata sorted/grouped/windowed minus fully covered windows. Consumer: an explicitly documented caller may retrieve sources, author a Summary and append it with `Summarizes` relations. The source selector itself does not read or judge the statements' meaning. SRC-1, `src/search/summary_index.rs`, `src/lib.rs`, `src/server.rs`.

Closest supplied route [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) can admit the eventual summary, but no candidate-object counterpart was declared. This record is not accumulated memory until a caller retains a derived result.

> /// This type only controls source selection. It does not create, append, or
> /// persist summary thoughts.
> --- `src/search/summary_index.rs`

#### MEM-OBJ-memory-markdown
Label: MEMORY Markdown view

Source-native identity: `to_memory_markdown` output and importable bullet lines. Representational form: natural-language content inside a symbolic section/metadata format. Storage substrate: generated string/service or dashboard response; caller-saved file is afforded, not observed. Lineage: selected thoughts grouped by enumerated type lists and formatted with content plus some attribution/role/importance/confidence/tags. Other types can be omitted; graph relations, UUIDs, session identifiers and source episodes are not rendered by the inspected section formatter. SRC-1, `src/lib.rs`, `src/server.rs`, `src/dashboard.rs`.

Consumers: external readers and the shipped Markdown parser. Prose is interpreted downstream; the parser admits newly indexed thoughts from matching lines. The document is a display/import view, not an opaque complete backup payload. Closest supplied records [RT-OBJ-thought](runtime.md#rt-obj-thought) and [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) concern source records/archive maintenance, not this lossy presentation. No counterpart after comparison.

> /// The source index `[#N]` is **discarded** — thoughts receive new
> /// append-order indices assigned by this chain. Lines that do not match
> /// the pattern (section headers, blank lines, malformed entries) are
> /// silently skipped.
> --- `src/lib.rs`

### Routes

#### MEM-RTE-correction-update
Label: Relation-driven memory correction
Part of: [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip)

Endpoints/progression: caller correction/replacement text and relation, or configured append deduplication → normal append → invalidation set → later default retrieval excludes target. Owner: caller chooses substantive revision; software may independently choose lexical near-duplicate replacement. Context/state effect: source record survives; search reliance changes through a symbolic exclusion. This is the correction subset of the supplied general admission/read-back route, not a duplicate of its entire progression. SRC-1, `src/lib.rs`, `MENTISDB_SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normal append result or error; optional automatic Supersedes relation is stored with the new thought.
- Later read-back: query/ranked/recent service routes normally hide target IDs; include-invalidated and point-in-time routes can expose earlier claims.
- Delegated visibility: clients sharing permitted chain access can retrieve replacement content or audit history; deployed readers are uninspected.
- Selection predicate: explicit relation target; dedup uses normalized token-set Jaccard against the configured recent scan window, choosing the most similar prior thought above threshold.
- Invalidation or expiry: Supersedes, Corrects and Invalidates mark target exclusion; this does not delete canonical text or implement automatic expiry.
- Activation or effect: candidate filtering changes in code; host belief/action changes remain uninspected.
- Evidence limits: lexical similarity is not contradiction analysis; cross-chain enforcement and every exact/history/export consumer are not established by this filter.

Admission: explicit append admits a proposed revision under the general structural/storage checks; human per-content approval is unresolved. The skill guides hosts to search, identify the original and state changed scope, but the append gate does not require that work. Dedup is software decision, enabled by configuration, not a user's approval of each supersession. Caller can withhold; storage can reject; later corrective appends and audit retrieval support recovery, not automatic restoration of reliance. Answer oracle: inapplicable — no expected answer decides correction. Operating mode: open caller requests with optional automatic similarity control, not an evaluation curriculum. Raw failure/fix → lesson/constraint → later agent is prescribed, not observed. Reasons persist only if authored in text/links; no rationale requirement or universal rationale reader is shown.

> pub const fn is_invalidating_relation_kind(kind: ThoughtRelationKind) -> bool {
>     matches!(
>         kind,
>         ThoughtRelationKind::Supersedes
>             | ThoughtRelationKind::Corrects
>             | ThoughtRelationKind::Invalidates
>     )
> }
> --- `src/lib.rs`

#### MEM-RTE-summary-selection
Label: Summary candidate selection and caller checkpointing

Endpoints/progression: explicit candidate request → committed metadata/filter → grouped append-order windows → candidate response → optional caller source retrieval/summary authorship → separate append → later ordinary memory request. Owner: code chooses windows; caller chooses whether and what to summarize and admit. Distinct from [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), which supplies the final append/read rather than the window selector. SRC-1, `src/search/summary_index.rs`, `src/lib.rs`, `src/server.rs`, `MENTISDB_SKILL.md`.

- implementation conclusion status: wired
- consumer conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: source IDs/indices and grouping bounds, paginated by the service; not generated summary content.
- Later read-back: candidate selection alone is inapplicable — no candidate persistence; caller-appended Summary/Checkpoint content is available to subsequent roundtrip routes.
- Delegated visibility: candidate IDs can be shared with authorized clients; actual host/sub-agent use is uninspected.
- Selection predicate: window size 50 and overlap 0 by default, grouped by session and entity type, optionally by agent; service defaults to 100 candidates/page. Windows fully covered by local Summarizes targets are skipped.
- Invalidation or expiry: unfiltered source selection uses all thoughts, including invalidated ones; filtered selection uses query semantics. Coverage collects local Summarizes targets from all thoughts without checking whether the summarizing thought remains valid.
- Activation or effect: deterministic source selection is wired; durable semantic compaction requires separately authored/admitted content, and host eviction is external.
- Evidence limits: the selector consumes metadata, not source text; no generated summary, guaranteed reason retention, token budget, host compaction or improved future action was observed.

Admission control is split: read-only selection admits nothing; caller authors/reviews or discards a summary, and normal append admits it. Generic caller identity leaves human review unresolved. The core skill guides Summary with Checkpoint role before compaction/handoff; no server scheduler requires or invokes that append. Answer oracle: inapplicable — existing coverage and window rules are not reference-answer judgments. Operating mode: explicit requests and host-chosen milestones, not automatic trace distillation. Recovery: original records remain reachable; no automatic summary-quality rollback. Alternatives include a standalone Checkpoint thought, Summary with Checkpoint role and broader StateSnapshot; labels do not guarantee compression or preserved rationale. SRC-1, `MENTISDB_SKILL.md`, `src/lib.rs`.

> .flat_map(|thought| thought.relations.iter())
> .filter(|relation| {
>     relation.kind == ThoughtRelationKind::Summarizes && relation.chain_key.is_none()
> })
> --- `src/lib.rs`

#### MEM-RTE-bundle-read
Label: Lexical-seed context bundle read

Endpoints/progression: REST/MCP text/filter/graph request → current-chain candidates → lexical seeds → optional graph expansion → grouped seed/support response. Owner: caller targets query; code filters and orders. Context effect: selected original text plus provenance, not a newly inferred prose summary. Distinct from the flat recent/ranked return in [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip). SRC-1, `src/lib.rs`, `src/server.rs`, `src/search/bundle.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: paginated bundles with seed thought, lexical score/matched terms, supporting thoughts, depth, relation kinds and paths; blank text yields none.
- Later read-back: committed thought content is selected on later calls; bundles themselves are not persisted by this route.
- Delegated visibility: response can be supplied to a host or human; no supplied deployed consumer proves further interpretation.
- Selection predicate: invalidation/as-of and supplied filters precede lexical seeding; service applies thesaurus for text. Default page size 50 bundles; graph uses caller depth/visited/mode controls and core caps graph seeds at 20.
- Invalidation or expiry: inherited candidate exclusion unless explicitly overridden; request output expires as transient response, while canonical sources remain.
- Activation or effect: code groups supporting locators and returns original source content; changed host behavior is uninspected.
- Evidence limits: core bundle selection is lexical, not a full vector/RRF reranking path despite accepting the ranked query structure; service counts/selects all bundles before pagination, not a token-window budget.

The helper removes duplicate seeds, omits depth-zero support by default, groups by seed, and retains shortest/deterministically ordered provenance paths per support locator. This is selection/packaging, not substantive editing or automatic memory adoption. With no graph supplied the route can return lexical seeds without supporting expansion. Reasons survive when explicitly linked content is selected; provenance is a traversal explanation, not a truth warrant.

> let graph_hits = request
>     .graph
>     .as_ref()
>     .map(|graph| self.expand_ranked_candidate_paths(&candidates, graph, &lexical_scores))
>     .unwrap_or_default();
> --- `src/lib.rs`

#### MEM-RTE-derived-update
Label: Derived retrieval state update

Endpoints/progression: admitted thought/explicit managed-provider registration or rebuild/reopen → embedding input → sidecar/index → optional implicit-neighbor overlay → later ranked/vector/graph selection. Owner: core/provider code computes; caller/operator chooses provider/configuration. Context/state effects: derived numeric vectors and symbolic neighborhoods change selection without replacing text. Distinct from admission in [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) and inference weights in [RT-CMP-fast-embed-provider](runtime.md#rt-cmp-fast-embed-provider). SRC-1, `src/lib.rs`, `src/search/vector.rs`, `src/search/implicit_edges.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: sidecar/status or append result/error; some backend construction is asynchronous.
- Later read-back: later search code uses cached/reloaded vectors and overlays to select thought text; it does not deliver the dense vectors as prose memories.
- Delegated visibility: clients receive selected content and scores/provenance; direct library users can access sidecar APIs. Actual clients are uninspected.
- Selection predicate: provider metadata and text/agent metadata determine vectors; threshold/K determine inferred neighbors; ranked query text, filters and graph controls determine subsequent use.
- Invalidation or expiry: unreadable/stale managed sidecars can rebuild from canonical thoughts; later query filtering hides invalidated content even though rebuild inputs include all thoughts.
- Activation or effect: append and registered rebuilds update derived selection machinery; search consumes it. No observed task-quality improvement or training update is established.
- Evidence limits: full provider behavior, metadata freshness propagation, WAL/HNSW replay and cross-process consistency were not audited; deferred/fallible derived writes limit atomicity.

Admission is computational and conditional on configuration: providers generate vectors, code validates/builds derived substrate; no human approves every vector/edge. Caller can disable management or choose rebuild; embedding/I/O errors can reject derived work after canonical admission. Recovery is rebuilding, not rollback of every append. Guidance is source text plus metadata and fixed derivation rules; no answer oracle selects embeddings or edges. Operating mode: automatic append synchronization and explicit maintenance. Raw conversation can feed the derivative, but the result is retrieval machinery, not a formulated lesson from success/failure. Provider inference parameters and numerical memory output are different objects.

> // The append-only chain is canonical and the sidecar is derived,
> // so an unreadable sidecar (for example a WAL that no longer
> // matches its snapshot) degrades to a rebuild instead of
> // blocking the chain from opening. This matches the other
> // sidecar load sites and the documented contract.
> --- `src/lib.rs`

#### MEM-RTE-markdown-exchange
Label: Memory Markdown export and import

Endpoints/progression: caller export/filter → type-section rendering → response/caller-edited Markdown → service/dashboard/library import → parse matching lines → sequential new appends → later memory requests. Owner: caller selects/edits/initiates; parser and append code decide admission. Distinct from archive restore in [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance). SRC-1, `src/lib.rs`, `src/server.rs`, `src/dashboard.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Markdown string or imported indices/count; malformed lines are skipped, an append error fails the operation after possible earlier writes.
- Later read-back: imported thoughts become normal retained records; generated view persistence depends on a caller saving it.
- Delegated visibility: dashboard can export an agent's view, service exports queried content; no deployed saved-file consumer is supplied.
- Selection predicate: enumerated type sections and optional query. Core None exports all source thoughts before type filtering; service chooses None when query_is_empty, even though it first computes filtered matches for logging.
- Invalidation or expiry: nonempty query can filter invalidated sources; empty service export can render invalidated thoughts. Import does not restore original invalidating relations.
- Activation or effect: formatting changes representation; import admits fresh text with new IDs/indices and partial metadata, potentially re-exposing obsolete claims without their graph exclusions.
- Evidence limits: no byte-faithful backup or complete semantic summary guarantee; multiline content/parser fidelity and every label-identity roundtrip case were not audited.

Admission: caller proposes Markdown; software parses known line format and admits each thought. Authorship/edits and human approval remain caller-dependent; no per-line human gate. Rejection: malformed lines are skipped; normal append can error. No whole-batch rollback is demonstrated. Recovery: original source chain/archive or explicit corrective append, not reversible import. Answer oracle: inapplicable — structural parsing is not fact validation. Operating mode: open import/export, no automatic experience-driven revision. Retained content can keep authored reasons in prose; omitted UUID/relations/source_episode metadata prevents faithful graph-lineage reconstruction.

> let markdown = if query_is_empty(&query) {
>     chain.to_memory_markdown(None)
> } else {
>     chain.to_memory_markdown(Some(&query))
> };
> --- `src/server.rs`

This positive counterexample limits the nearby comment that Markdown always uses query filtering: the actual empty-query output takes the unfiltered renderer.

#### MEM-RTE-agent-copy
Label: Dashboard agent memory copy

Endpoints/progression: dashboard agent/source/target request → collect that agent's source thoughts → create/open target and propagate registry metadata → append copied content/type/role/importance/confidence/tags/concepts → later target retrieval. Owner: caller chooses source/target; code transforms and admits. Distinct from merge in [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance): one agent is copied, source survives and same-agent existing target thoughts veto copying. SRC-1, `src/dashboard.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: copied count, zero for no source thoughts, conflict if target already has thoughts for that agent, or error.
- Later read-back: fresh target thoughts participate in normal queries; source content remains available separately.
- Delegated visibility: dashboard-authorized callers and later target clients; deployed access set uninspected.
- Selection predicate: all source thoughts matching agent ID in append order, not only currently valid thoughts.
- Invalidation or expiry: graph refs/relations are dropped, so source correction exclusions do not accompany copied text; target dedup behavior is configuration-dependent, not identity-preserving invalidation replay.
- Activation or effect: creates fresh target records and registry metadata; actual downstream behavioral use uninspected.
- Evidence limits: copy omits session/entity/source-episode fields in the inspected ThoughtInput construction as well as graph links; no batch-wide rollback is demonstrated.

Admission: explicit dashboard request; PIN/session envelope is not per-content approval. Code rejects same source/target or existing target agent thoughts; generic user identity leaves actual human authorship unresolved. Fixed copy rules supply guidance, not a superior-memory oracle. Answer oracle: inapplicable — existing-target conflict rule is structural. Operating mode: explicit administration. Recovery: source remains; an error can leave an appended prefix. This route can retain invalidated old text while losing the relation that hid it.

> // refs and relations are positional/UUID references into the
> // source chain; they cannot be meaningfully carried over.
> input
> --- `src/dashboard.rs`

#### MEM-RTE-chain-withdrawal
Label: Dashboard whole-chain withdrawal

Endpoints/progression: explicit dashboard deletion → cached-chain removal → deregister chain and remove selected backing files → later chain discovery/retrieval no longer uses registered retained state. Owner: caller requests; code executes filesystem/registry changes. Distinct from the successful-merge cleanup subset of [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), because no target copy is required. SRC-1, `src/dashboard.rs`, `src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: deleted flag/key or error.
- Later read-back: registered source state is withdrawn; already delivered copies, archives and external host windows are not retracted by this operation.
- Delegated visibility: later clients cannot discover the removed registration normally; external copies and all other open handles are not fully traced.
- Selection predicate: explicit chain key and its registration/storage location, associated registries/config, vector JSON prefix and auto-edge filename.
- Invalidation or expiry: physical removal rather than relation-driven hiding; not a TTL or individual-thought deletion route.
- Activation or effect: registry/filesystem state changes; no observed deletion or complete erasure is established.
- Evidence limits: sequential fallible removal is not atomic secure erasure; WAL/HNSW residual files and live independent handles are not fully accounted for.

Admission: caller requests destructive administration; route access permits it but does not prove a human's per-item consent. Software decides registered file targets; I/O can reject after earlier effects. No expected-answer oracle or memory-quality selection. Operating mode: explicit administration. Recovery requires retained backup/source elsewhere; automatic undo is not shown. This is a source-supported counterexample to interpreting the skill's “forever-record” language as an absolute product invariant.

> let storage_path = PathBuf::from(&entry.storage_location);
> if storage_path.exists() {
>     fs::remove_file(&storage_path)?;
> }
> --- `src/lib.rs`

#### MEM-RTE-webhook-delivery
Label: Append event webhook delivery

Endpoints/progression: core append with attached manager → active registration/type/chain matching → bounded queue → HTTP payload/retries → external endpoint. Owner: operator/caller registers endpoint; code selects and dispatches. Distinct from [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip): this is unsolicited current append-event delivery, not a later request selecting retained history. SRC-1, `src/lib.rs`, `src/webhooks.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: nonblocking dispatch attempt; append does not await endpoint completion.
- Later read-back: uninspected — external endpoint retention/consumer not frozen; current event delivery alone is not historical memory read-back.
- Delegated visibility: matching registered external endpoints receive the new thought's payload if delivery succeeds; actual registrations and delivery are uninspected.
- Selection predicate: append trigger, active registration, optional chain-key and thought-type filters; selected part is the new WebhookThought payload, not a ranked history window.
- Invalidation or expiry: registration deletion/active filtering stops future selection; queued transient jobs and previously delivered payloads are not an external recall mechanism.
- Activation or effect: JSON push with bounded concurrency, HTTP timeout and exponential-backoff retries; queue full/unavailable drops jobs.
- Evidence limits: no durable replay guarantee or inspected external behavioral-authority consumer; does not establish checkpoint loading or agent activation.

> if let Err(error) = queue.try_send(job) {
>     log::warn!(
>         target: "mentisdb::webhooks",
>         "dropping webhook delivery because the queue is full or unavailable: {}",
>         error
>     );
> }
> --- `src/webhooks.rs`

#### MEM-RTE-retrieval-evaluation
Label: Retrieval evaluator memory and diagnostics

Endpoints/progression: supplied dataset → raw turns admitted as FactLearned → question-driven search → evidence-text matching → counters/miss diagnostics/optional result files. Owner: evaluator code controls ingest/query/scoring; operator chooses dataset/configuration/run. Distinct from [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip): this shipped caller uses it in a bounded retrieval test and owns an answer-reference comparison. SRC-1, `lme-benches/longmemeval_bench.py`, `lme-benches/convomem_bench.py`, `locomo-benches/locomo_bench.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: retrieval-hit rates, per-type/category diagnostics, errors or optional JSON/JSONL output.
- Later read-back: subsequent questions read retained conversation turns; result files are intended diagnostics for operators, not automatically admitted lessons or updated instruction versions in the inspected drivers.
- Delegated visibility: dataset text is sent to configured service; operator can inspect diagnostics. Actual runs and recipients are uninspected.
- Selection predicate: query text/top-K and driver graph/reranking options; evidence oracle uses dataset labels/text, not a generated-answer judge. LongMemEval links turns within sessions and weights user/assistant differently.
- Invalidation or expiry: ConvoMem changes chain key per item to avoid retrieval bleed; this is namespace change, not removal of old retained chains. Other cleanup and dataset lifecycle are not comprehensively audited.
- Activation or effect: raw traces and diagnostic output can be produced by code; no automatic diagnostic-to-rule-to-agent loop or benchmark execution is established.
- Evidence limits: LoCoMo expands evidence to neighboring turns; substring matching can count partial text, and empty-reference cases in some matchers are not excluded uniformly. Metrics do not establish answer accuracy or learned capacity.

Admission: operator starts a bounded driver, then code admits individual raw dataset turns without per-turn human review. Software/model factual quality review is not part of these append calls; FactLearned is a label. Oracle provider: dataset answer/evidence annotations. Use: case-insensitive substring containment in either direction; LoCoMo broadens target evidence via neighboring turns. ConvoMem abstention counts not surfacing evidence rather than an agent explicitly abstaining. Operating mode: bounded retrieval evaluation, not an autonomous improvement curriculum. Driver flags guide retrieval; persisted outputs are scores/misses/returned text, not a selected successor policy. Ordinary append/storage failure can reject; retry or a fresh namespace can recover, with no whole-ingest rollback shown. Human interpretation of results is possible, not observed causal revision.

> if ev_l in c or c in ev_l:
>     return True
> --- `lme-benches/longmemeval_bench.py`

### Claims

#### MEM-CLM-scope-visibility
Label: Claimed scope visibility

Claimed operation: User scope shares with user identity, Session limits to creating session and Agent limits to creating agent. SRC-1, `MENTISDB_SKILL.md`. Doctrine conclusion status: claimed. Implementation conclusion status: wired for scope tags and explicit filtering, not a universal identity-bound visibility invariant. The inspected `ThoughtInput.with_scope` stores a tag; recent-context has no scope argument, and the Python read does not pass scope/session/agent filters. [RT-RTE-access-control](runtime.md#rt-rte-access-control) is a separate credential envelope, not proof that tags enforce the skill's identity semantics.

> Scopes stored as `scope:{variant}` tags:
>
> - `user` (default): visible to all agents sharing the user identity.
> - `session`: visible only within the creating session.
> - `agent`: visible only to the creating agent.
> --- `MENTISDB_SKILL.md`

Closest supplied [RT-RTE-access-control](runtime.md#rt-rte-access-control) concerns token scope rather than this memory-scope claim; distinct identity. No observed scope isolation is supplied.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-thought](runtime.md#rt-obj-thought)

Memory-specific lineage/control: attribution, role, confidence, importance, tags, concepts, session/source episode and typed links can accompany text; confidence/importance are caller values clamped to ranges, not checked epistemic warrant. Source episodes are stored attribution, not automatically retrieved reasons. Canonical storage and derived indexes differ in authority and failure lifecycle. The content part is separately declared as [MEM-OBJ-thought-content](#mem-obj-thought-content). Direct reads: SRC-1, `src/lib.rs` append construction and index update; `src/server.rs` append parsing. The supplied envelope quote supports append-order identity, not factual truth.

#### On [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip)

Read-back details: recent service selects the last twelve valid records by default, optional attribution filter, chronological delivery as text. It renders content/type/role/agent labels, not all stored relations or reasons. Direct `to_catchup_prompt(last_n)` instead slices the unfiltered tail. Ranked core combines lexical/vector/graph and metadata signals, optionally RRF; a named “session cohesion” boost uses append-index proximity within radius twelve, not a session-ID equality test. The server ordinary ranked route applies static thesaurus; direct Rust use must supply expansion, and the inspected federated service builds its text query without the thesaurus helper. SRC-1, `src/lib.rs`, `src/server.rs`, `src/search/mod.rs`.

> const SESSION_COHESION_RADIUS: u64 = 12;
> const SESSION_COHESION_BOOST: f32 = 1.2;
> const SESSION_COHESION_MIN_SEED_LEXICAL: f32 = 3.0;
> const SESSION_COHESION_MAX_HIT_LEXICAL: f32 = 5.0;
> --- `src/lib.rs`

Federated selection explicitly targets multiple keys, takes limited per-chain hits, merges/deduplicates and returns source-chain annotations; unknown/open-failing chains can be silently skipped. Automatic ancestor reads in the supplied ordinary route remain distinct from explicit federation. Budgets are record/page/graph limits, not a guaranteed model token cap. Human or host tool requests pull retained content; this is not independent automatic startup injection. SRC-1, `src/server.rs`; supplied roundtrip and branch passages.

Python consumer: write passes the same attribution/type/role/scope for every nonempty string message; original speaker class and configured session ID are not passed. Read requests twenty of the configured type, no current-input text and no session/agent/scope filter, then infers speaker from agent-ID equality. Error becomes no messages; clear does nothing. Content is joined into a string under `memory_key`, normally `chat_history`, which has knowledge authority only if an external prompt consumes it. This confirms the runtime finding, not a new duplicate route. SRC-1, `pymentisdb/langchain.py`; supplied role-reconstruction and prompt-format passages in the cited runtime route and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).

Write agency: CLI add, service append/retrospective, Python automatic messages, imported/copied text and user-authored correction/checkpoints all reach structural append but differ in authorship and admission guidance. Retrospective appending chooses a default LessonLearned/Retrospective label without automatically extracting a lesson. Authentication and generic caller identity leave per-content human judgment unresolved. SRC-1, `src/cli/mod.rs`, `src/server.rs`, `src/lib.rs`, `pymentisdb/langchain.py`.

#### On [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Memory-specific read-back and withdrawal: explicit IDs/versions select reconstructed bodies; omitted version picks latest, not evaluated best. The reader returns content even for a revoked entry, with separate status and authored-document warnings. Entry reasons remain metadata; they are not synthesized into warnings by `read_skill_from_entry`. Deprecate/revoke retain versions; delete removes the entry and all versions; upload preserves Revoked but can reactivate other lifecycle states. Earlier version addressing affords recovery of text only. SRC-1, `src/skills.rs`; direct read output/snapshot and lifecycle searches; admission/persistence evidence supplied in the cited route. Instruction content is [MEM-OBJ-skill-body](#mem-obj-skill-body).

Actual human authorship/approval and proposal guidance remain unresolved for uploaded skills. Structural parsing and conditional signatures establish neither safe instructions nor task-performance selection. Body/patch/provenance persistence does not itself establish retained content-directed criticism. The core skill's warning-check request should not be read as proof that every lifecycle reason reaches an agent through the warnings list. SRC-1, `src/skills.rs`, `MENTISDB_SKILL.md`.

#### On [RT-BAP-retained-context](runtime.md#rt-bap-retained-context)

Authority at consumption: human/model interpretation of returned natural-language content remains separate from symbolic query selection and numerical retrieval scores. Python prompt loading is wired; host obedience and actual action change remain uninspected. Recent-context provides source text by value rather than a live dereferenceable chain pointer. Linked rationale can remain reachable in the store without being delivered in that selected slice. SRC-1, `src/lib.rs`, `pymentisdb/langchain.py`. This annotation supplies memory-specific delivery limits, not another authority-path declaration.

## Write side

### Acquire, author, transform and admit

Callers supply thought text; the server parses symbolic types/relations and the core constructs/persists a linked envelope. No universal prior-search or truth gate is implemented by those steps. The skill asks hosts to distill durable rules rather than raw logs, search before append and connect reasons; Python and evaluator writers instead persist raw utterances directly. These are different acquisition/curation paths with a shared physical append, not uniform “automatic semantic learning.” Extraction returns untrusted model candidates; separate append remains the admission step. See [RT-RTE-memory-extraction](runtime.md#rt-rte-memory-extraction), [MEM-OBJ-thought-content](#mem-obj-thought-content), roundtrip annotation and [MEM-RTE-retrieval-evaluation](#mem-rte-retrieval-evaluation). Source: SRC-1, `MENTISDB_SKILL.md`, `pymentisdb/langchain.py`, `src/server.rs`, `src/lib.rs` and the three evaluator paths.

Automatic transformations include metadata normalization/clamping, positional-reference conversion, similarity supersession, index/vector/implicit-edge updates and skill patch storage/reconstruction. They do not imply a model generated a new warranted proposition. Raw transcript → vector/neighbor index → later retrieval is a wired derivative chain; raw work outcome → authored lesson/checkpoint → later host is a prescribed/afforded semantic chain. Candidate windows alone do not close the latter chain. Reasons are optional content/links, not required admission fields. See [MEM-RTE-derived-update](#mem-rte-derived-update), [MEM-RTE-correction-update](#mem-rte-correction-update), [MEM-RTE-summary-selection](#mem-rte-summary-selection), [MEM-OBJ-skill-body](#mem-obj-skill-body).

### Maintain, reject and withdraw

Correction hides source claims in default query paths but preserves audit text. Read-only source-window coverage can continue to treat an invalidated summary's targets as summarized. Markdown exchange and copying can strip invalidation/lineage and create fresh visible records; neither is a faithful graph backup. Skill revocation retains both body and status; deletion removes history. Whole-chain deletion removes registered backing state, not external copies. These qualifications trace effects through later consumers rather than equating “invalidated,” “revoked,” “cleared” and “deleted.” See [MEM-RTE-correction-update](#mem-rte-correction-update), [MEM-RTE-summary-selection](#mem-rte-summary-selection), [MEM-RTE-markdown-exchange](#mem-rte-markdown-exchange), [MEM-RTE-agent-copy](#mem-rte-agent-copy), [MEM-RTE-chain-withdrawal](#mem-rte-chain-withdrawal) and skill annotation.

Rejection is route-specific: type/UUID/reference parsing, storage failure, registered-agent/signature checks on service skill upload, import-line skipping, existing-agent conflict on copy and archive checks on restore are not interchangeable human approval. Direct library/UI paths differ. Canonical append precedes fallible derived work, while imports/copies/merges append sequentially; an error can leave retained state. The supplied runtime's atomicity and durability limits therefore remain consequential. See [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) and new transformation routes above.

Evaluation retains source turns and optionally diagnostic files; inspected drivers do not automatically convert misses into lessons, modify skills or adopt a new retrieval policy. Scores are reference-text retrieval judgments, not observed learning outcomes. Available native reports and Rust tests were not rerun. This does not prove no reflective learning can occur in an external host; it limits attribution to these inspected driver routes. See [MEM-RTE-retrieval-evaluation](#mem-rte-retrieval-evaluation).

## Read-back

### Pull, selection and delivery

Most retained-content delivery is requested: recent context, flat lexical/ranked search, explicit federation, grouped bundles, exact IDs/history, Markdown view and skill read. Content reaches clients as response JSON/text, or through the Python prompt-variable string. Each is a different selector, not a promise to inject all relevant facts. Topical text/filters, time/as-of, type/role, metadata, score and graph budgets select what is delivered; identifiers alone establish addressing, not relevance. Exact/history routes remain alternative access whose full filtering was not inspected. SRC-1, `src/server.rs`, `src/lib.rs`, `pymentisdb/langchain.py`; coverage table, roundtrip annotation and [MEM-RTE-bundle-read](#mem-rte-bundle-read).

Service recent-context, direct catch-up and Markdown's empty-query branch differ in stale-content filtering. Summary selection differs again: an unfiltered candidate request takes all thoughts, and coverage is not conditioned on current validity of the summary. Skill read retains lifecycle status but delivers revoked text. These source-supported exceptions prevent generalizing “default search hides stale memory” into “no stale content can reach any later consumer.” See [MEM-RTE-correction-update](#mem-rte-correction-update), [MEM-RTE-summary-selection](#mem-rte-summary-selection), [MEM-RTE-markdown-exchange](#mem-rte-markdown-exchange) and skill annotation.

Webhook delivery is the inspected push alternative. Its trigger is append, input is new thought plus registrations, selector checks active/chain/type, budget is queue/concurrency/timeout/retry rather than host context tokens, and channel is external HTTP. It selects no historical memory, and later external retention/behavior is uninspected. Service read/append callbacks are optional configured functions, not proved automatic context reload. SRC-1, `src/server.rs`; [MEM-RTE-webhook-delivery](#mem-rte-webhook-delivery).

### Working-context control

Recent-tail selection, filtering/scoring, graph grouping and Python formatting determine what external material can enter a later invocation. They do not themselves evict the host's existing turns. The core skill asks for checkpoints before compaction/truncation/handoff and shared pre-warming before sub-agents; the host decides when to isolate or remove context. Alternative retained forms include Summary/Checkpoint and StateSnapshot, with source text still reachable by later requests. No invoked host frame, actual eviction or returned sub-agent artifact was supplied. SRC-1, `MENTISDB_SKILL.md`, `src/lib.rs`, `src/server.rs`, `pymentisdb/langchain.py`; [RT-BAP-core-skill](runtime.md#rt-bap-core-skill), [MEM-RTE-summary-selection](#mem-rte-summary-selection).

A separate sub-agent context would resemble a frame whose selected result escapes, but that frame is host-owned, not a MentisDB implementation evidenced here. Chain keys/UUIDs are retrieval addresses outside the window; returned text is copied by value and requires another explicit tool/API call to reload. There is no model-window liveness/reference-count implication from storing a pointer-like identifier. The skill's ≤50% context target is advice, not an enforced token measurement or budget. SRC-1, `MENTISDB_SKILL.md`, `src/lib.rs`, `src/server.rs`.

## Integration issues

1. **No duplicate redeclarations intended.** Thought content and skill instruction bodies are explicit parts of the supplied containers. Correction is a subset of the supplied roundtrip. New derived/candidate/view objects and bundle/Markdown/copy/deletion/webhook/evaluator routes have distinct identities stated beside their closest supplied records. Reconciliation should retain those distinctions rather than supersede the valid envelope/registry containers. See [RT-OBJ-thought](runtime.md#rt-obj-thought), [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry), [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) and this member's Part of fields.
2. **Markdown invalidation exception.** The service computes query-filtered matches for logging but an empty query renders `to_memory_markdown(None)`, which traverses all source thoughts before type grouping. This qualifies any broad interpretation of the supplied roundtrip's stale-memory exclusion; it does not contradict its specifically ranked/recent account. Evidence: SRC-1, `src/server.rs`, `src/lib.rs`; [MEM-RTE-markdown-exchange](#mem-rte-markdown-exchange). Consequence: metadata logs can describe a filtered count while delivered Markdown includes stale claims. Exact/history handlers remain a named unresolved alternative, preventing a universal read-back claim.
3. **Revocation notices are split.** The supplied skill route correctly notes that reads need not reject revoked content. The inspected reader additionally distinguishes authored document warnings from entry status/reason; an empty warnings list is not proof of Active status. Evidence: SRC-1, `src/skills.rs`; [MEM-OBJ-skill-body](#mem-obj-skill-body), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Consequence: consumers must be described as receiving separate fields, not guaranteed synthesized safety rationale. Actual host checks remain unresolved.
4. **Labels and scope claims do not establish mechanisms.** Python default Summary is raw message storage; “session cohesion” is index proximity; Session/Agent scopes are tags/filter inputs, not demonstrated identity isolation. These confirm or qualify the runtime's Python and branch-isolation warnings. Evidence: SRC-1, `pymentisdb/langchain.py`, `src/lib.rs`, `MENTISDB_SKILL.md`; [MEM-OBJ-thought-content](#mem-obj-thought-content), [MEM-CLM-scope-visibility](#mem-clm-scope-visibility), [RT-RTE-access-control](runtime.md#rt-rte-access-control). Consequence: no transcript-role fidelity, per-session partitioning or user-identity visibility invariant can be inferred from labels.
5. **Unsettled selector/copy semantics.** Summary coverage retains targets even when a summarizing source is invalidated; unfiltered windows include invalidated records. Agent copy/Markdown import drop graph lineage, while the supplied merge also loses relations. Federated service does not automatically apply the ordinary ranked service's thesaurus helper; bundles accept a ranked request but select lexical seeds rather than full vector/RRF results. Evidence: SRC-1, `src/lib.rs`, `src/server.rs`, `src/dashboard.rs`; [MEM-RTE-summary-selection](#mem-rte-summary-selection), [MEM-RTE-agent-copy](#mem-rte-agent-copy), [MEM-RTE-markdown-exchange](#mem-rte-markdown-exchange), [MEM-RTE-bundle-read](#mem-rte-bundle-read), [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance). Consequence: preserve route-specific semantics. Whether these edge cases were exercised or intentionally desirable is unresolved, not settled by implementation labels.
6. **Remaining included inspection limits.** Full sidecar/WAL/HNSW freshness and deletion residue, metadata-update re-embedding, every exact/history/bootstrap filter, every dashboard search default, TUI key loop, all integration targets, exported expansion/PPR/intent callers and full restore conflict reconciliation remain incompletely inspected. Evidence/affected records are in the coverage table and [MEM-RTE-derived-update](#mem-rte-derived-update), [MEM-RTE-chain-withdrawal](#mem-rte-chain-withdrawal), [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance). These prevent exhaustive reliability/security/erasure claims, not the positive bounded paths established here.
7. **Execution and semantic-update evidence unresolved.** No retained live chain, uploaded skill, external webhook consumer, diagnostic-driven update or host compaction trace was supplied. The evaluator's reference matching and optional output do not prove quality or a diagnostic-to-learning loop. Evidence: SRC-1, three evaluator scripts and `MENTISDB_SKILL.md`; [MEM-RTE-retrieval-evaluation](#mem-rte-retrieval-evaluation), [RT-BAP-retained-context](runtime.md#rt-bap-retained-context). Consequence: learned capacity, reliable rationale use, actual behavioral activation and end-to-end improvement remain unestablished independently of persistence and wiring.

## Limitations and checks

The frozen checkout HEAD matched `4c9b95041da68c5a26dece9f8776ff54b05b910c`; `git status --short` returned no tracked or untracked changes. Source identity, run identity and reviewed boundary repeat the supplied boundary/run values. Input type contracts and the complete invocation/worker/records instructions were read; the named runtime and records ranges were delivered without content truncation. Inspection did not expand the source register or functional boundary.

Counterchecks included raw messages labelled Summary, configured similarity supersession without criticism, invalidation-bypassing direct/empty-query renderers, summary coverage from invalidated sources, revoked-body return without synthesized warnings, lossy graph copies/imports, physical chain deletion, unknown-chain skipping, route-specific expansion and bounded webhook drops. These qualify strong labels and claims rather than infer absence from missing runs. Available but unread internals remain named inspection limits above; external provider/host behavior remains outside frozen source. No causal benefit or exercised learning claim is made.

Deterministic validation: completed through the invocation's `commonplace-run validate-output` check; a pass establishes record/identity/citation/quotation form, not analytical acceptance or observed operation.
