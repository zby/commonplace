---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Mnemosyne memory: proposed curated vault, conversation promotion and context exports, contrasted with the legacy bridge's normalization and opaque backend retrieval."
run-id: AAS-2026-10-15-isaacclupus-mnemosyn-spec-1887e13dcc13-01
source-identity: "https://github.com/noirblue/IsaacCLupus_mnemosyn_spec"
reviewed-boundary: "0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92"
---

# IsaacCLupus_mnemosyn_spec memory report

## Boundary and evidence

Mnemosyne proposes a shared memory substrate for external agents. This report includes source acquisition, compiled pages, explicit memory proposals, conversation retention, feedback, graph retrieval, exports and maintenance. It distinguishes canonical design, draft extensions, study snippets and statically wired legacy adapters. The frozen boundary and sole source are those in [boundary](boundary.md#source-register): SRC-1 at `0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92`. No target execution, live vault, backend implementation or model weights were supplied. Backend storage, actual context assembly, successful synchronization and behavioral benefit cannot be established.

Direct source reads added to the supplied runtime findings cover `SPECIFICATION.md`, `MNEMOSYNE_SPEC_v0.2.md`, `ARCHITECTURE.md`, `schema/001-init.sql`, `config.sample.yaml`, the beginning of `AGENTS.md`, complete legacy `cli.py`, `mcp_gateway.py` and `vault_sync.py`, and selected compilation, watcher, graph and export study sections. These are SRC-1 doctrine/design except the SQL and legacy Python implementation. Study code remains design evidence even when concrete. Supplied runtime findings additionally cover package dispatch, launch units and the proxy; these were not all independently reread here.

| Entry point / memory operation | Source path (SRC-1) | Coverage / limit |
|---|---|---|
| Legacy CLI init, publish, MCP and proxy dispatch | `prior-art/v0-glue/jarvis_kb/cli.py` | Direct read; init creates directories, not backend memories. Publication and later query: [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish), [RT-RTE-client-query](runtime.md#rt-rte-client-query). |
| All six registered MCP handlers | `prior-art/v0-glue/jarvis_kb/mcp_gateway.py` | Direct read; ingest/compile/audit, remember and search/ask are independent dispatch paths: [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools), [RT-RTE-link-remember](runtime.md#rt-rte-link-remember), [RT-RTE-client-query](runtime.md#rt-rte-client-query). No additional memory tool in this dispatcher. |
| Copy, normalize, reindex, snapshot/load and optional Git history | `prior-art/v0-glue/jarvis_kb/vault_sync.py` | Direct read; [MEM-OBJ-unified-vault](#mem-obj-unified-vault); supplied publication route annotated below. |
| Proposed raw/draft/published/archived pages and memory inbox | `ARCHITECTURE.md`, `AGENTS.md`, `SPECIFICATION.md`, `schema/001-init.sql` | [MEM-OBJ-vault-pages](#mem-obj-vault-pages), [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle). Automatic archive criteria and external admission implementation unresolved. |
| Proposed conversations, profiles and heat promotion | `SPECIFICATION.md`, `MNEMOSYNE_SPEC_v0.2.md` | [MEM-OBJ-conversations](#mem-obj-conversations), [MEM-OBJ-user-profiles](#mem-obj-user-profiles), [MEM-RTE-conversation-promotion](#mem-rte-conversation-promotion). Profile visibility explicitly undecided. |
| Compilation, rejection and incremental rewrite | `python_thoughts/05-heavy-llm-compilation.md`, `rust_thoughts/04-file-watcher-incremental-compile.md` | Selected direct reads; [MEM-OBJ-rejection-feedback](#mem-obj-rejection-feedback), [MEM-RTE-feedback-recompile](#mem-rte-feedback-recompile); general pipeline remains [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle). Watcher internals outside selected ranges remain uninspected; no exhaustive scheduling guarantee. |
| Graph load, traversal and query assembly | `rust_thoughts/05-graph-traversal.md` | Selected direct reads; [MEM-OBJ-knowledge-graph](#mem-obj-knowledge-graph), [MEM-RTE-graph-context](#mem-rte-graph-context). Snippet/schema mismatches prevent a working end-to-end claim. |
| Export CLI, pack writer, file-aware agent entry point; maintenance flags | `rust_thoughts/06-pack-export-cli.md`, `SPECIFICATION.md` | Selected direct reads; [MEM-OBJ-agent-pack](#mem-obj-agent-pack), [MEM-RTE-pack-export](#mem-rte-pack-export). Prune-audit, clear-cache and repair flags declare intent, not inspected maintenance bodies. Cache payload, admission and reuse remain unresolved. |
| Audit, contradiction and job state; receipts and draft governance | `schema/001-init.sql`, `SPECIFICATION.md`, `MNEMOSYNE_SPEC_v0.2.md` | [MEM-OBJ-state-metadata](#mem-obj-state-metadata). Hashes/counters are not readable reasoning traces. Draft claims/verdicts/dissents and optional proof exports are future design, not current memories or guaranteed query inputs. |
| Hybrid/vector retrieval and model storage | `ARCHITECTURE.md`, `config.sample.yaml` | Optional vector re-ranking and embedding alias are design only; vector store, embedding lineage, updates and consumer implementation uninspected. Supplied model records cover fast/heavy/chat, not an inspected embedding pipeline. |
| Service launchers and model proxy | `prior-art/v0-glue/systemd/`, `prior-art/v0-glue/jarvis_kb/ollama_proxy.py` | Supplied runtime findings: [RT-RTE-model-proxy](runtime.md#rt-rte-model-proxy), [RT-OBJ-proxy-queues](runtime.md#rt-obj-proxy-queues). Current-request queues are not retained read-back; provider-side state unresolved. |

External Synto, Synthadoc, LLM-WIKI, Link, Ollama and enclosing clients remain outside the frozen source. Other study details, superseded v0.1 details and asset images were not used to infer additional operative behavior. Available but uninspected material is not an access gap or evidence of absence.

## Core ideas

1. **Memory is proposed to pass through content admission, not just storage.** Agent-authored inbox text and model-compiled pages become searchable after review/approval, with configurable automatic approval. The legacy bridge does not implement that universal gate: its direct Link write and filesystem publication have different admission controls. [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle), [RT-RTE-link-remember](runtime.md#rt-rte-link-remember), [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish).
2. **Content and governance metadata have different survival paths.** Legacy publication preserves the page body while replacing metadata. The consumer may receive citations/provenance and a maturity label but not approval or audit hashes. A high confidence number even takes precedence over contradicted status in the normalizer. [MEM-OBJ-unified-vault](#mem-obj-unified-vault).
3. **Retained criticism has a specific future consumer.** Rejection feedback is proposed as rewrite input and the rejection count as a scheduling constraint. This is stronger than merely logging an audit but weaker than demonstrated improvement or a deployed feedback loop. [MEM-RTE-feedback-recompile](#mem-rte-feedback-recompile).
4. **Context promises exceed inspected selection code.** Canonical budgets, graph-neighbor labels and export completeness must be checked at delivery. The legacy ask echoes a budget; the graph sketch supplies primary text plus selected relationship summaries; a file-aware pack consumer is documented but not deployed. [RT-RTE-client-query](runtime.md#rt-rte-client-query), [MEM-RTE-graph-context](#mem-rte-graph-context), [MEM-RTE-pack-export](#mem-rte-pack-export).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-vault-pages
Label: Vault pages

Source-native `raw/`, `wiki/.drafts/`, published namespace pages and `memory/inbox/` / `memory/committed/` are proposed filesystem Markdown bodies with SQLite page metadata. Bodies are natural-language content; paths, IDs, stage, namespace and link relations are symbolic access/control data. Provenance JSON identifies source files, line intervals and extractors, but does not prove extraction correctness. Raw documents are retained sources, not necessarily agent interaction traces. Compiled pages are model-derived knowledge, while explicitly proposed memories can originate with an external caller. Initial actual content and caller identity are uninspected. Consumer roles are later compilation, query and exported-file clients; body authority is interpretive knowledge rather than enforced instructions. Distinct from [RT-OBJ-compile-template](runtime.md#rt-obj-compile-template): pages are its source/related material and output, not the template. Closest route is [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle), not an object counterpart. SRC-1, `ARCHITECTURE.md`, `SPECIFICATION.md`, `schema/001-init.sql`.

> ├── raw/                     # immutable sources
> --- `ARCHITECTURE.md`

> | `provenance` | TEXT | JSON: `[{source_file, line_start, line_end, extractor}]` |
> --- `SPECIFICATION.md`

#### MEM-OBJ-unified-vault
Label: Unified vault

The legacy `frontline.unified_vault` receives filesystem Markdown normalized from Synto and Synthadoc wiki pages. Natural-language bodies survive; symbolic frontmatter is replaced with selected title, maturity, source tool, sync timestamp, provenance and optional citations. Approval, content hash and arbitrary producer fields do not survive that replacement. Confidence-to-maturity is automatic label transformation, not independent truth assessment. Numeric confidence selects a branch before contradicted status, so a confident contradicted source can be labeled established. Lineage is file copy/transformation from backend-produced pages; underlying raw origin is whatever provenance/body actually carries, not guaranteed by the adapter. Later LLM-WIKI indexing and requested Link reload are consumers; exact backend-visible payload and successful indexing remain external. This object is the retained output of [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish), distinct from that route and from the proposed unified pages above. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`.

> if isinstance(confidence, (int, float)):
>     maturity = "established" if confidence > 0.8 else "refining" if confidence > 0.5 else "seed"
> elif status == "contradicted":
>     maturity = "disputed"
> --- `prior-art/v0-glue/jarvis_kb/vault_sync.py`

The copied body's reasons can survive if present in the body; governance reasons stored only in omitted keys do not. The normalizer does not inspect or reconstruct such reasons.

#### MEM-OBJ-conversations
Label: Conversations

`conversations` in initial `state.db` stores role/content, session ID, model, tokens, cost and timestamp. Content is natural-language/raw interaction material; role/session/token fields are symbolic metadata. DDL establishes a storage shape, not a working history selector. Canonical Phase 2 adds tier, heat, last-reference, decay and promoted-page ID; these columns are not in initial DDL. The proposed later consumers are query history and extraction/promotion; the inspected legacy gateway does not persist or reload these rows itself. Distinct from [RT-RTE-client-query](runtime.md#rt-rte-client-query), which delegates to an external history implementation, and no supplied object counterpart. SRC-1, `schema/001-init.sql`, `SPECIFICATION.md`.

> content     TEXT NOT NULL,                      -- Message content
> --- `schema/001-init.sql`

> | `tier` | TEXT | `short` (7 turns), `mid` (heat-decay), `long` (committed memory) |
> --- `SPECIFICATION.md`

#### MEM-OBJ-user-profiles
Label: User profiles

Phase 2 `user_profiles` is proposed SQLite extracted key/value facts with confidence, source-conversation IDs, extraction/verification times and active/stale/superseded status. Values are natural-language facts; keys, status and lineage references are symbolic. The fast model derives these from conversation text, unlike the raw turns in [MEM-OBJ-conversations](#mem-obj-conversations). Consumer visibility remains an explicit open question, so no automatic system-prompt injection is established. No supplied object counterpart; this is an additional design artifact rather than a model component or generic lifecycle route. SRC-1, `SPECIFICATION.md`, `MNEMOSYNE_SPEC_v0.2.md`.

> 1. Should `user_profiles` be agent-visible or internal-only? If visible, how does it affect privacy?
> --- `MNEMOSYNE_SPEC_v0.2.md`

#### MEM-OBJ-rejection-feedback
Label: Rejection feedback

`pages.rejection_feedback` is proposed persisted natural-language criticism, separate from symbolic `rejected_count`. The later ArticleWriter sketch includes the feedback in a rewrite request; scheduling reads the counter and tests approvals. The raw audit result, stored feedback and rewritten page must not be conflated. Whether all audit reasons are copied into feedback is uninspected. Stored feedback supplies reasons when populated, not a hash-only trace; later consumers are planner and writer, not demonstrated ordinary query clients. Distinct material result of [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle), which supplies the general rejection loop. No supplied object counterpart. SRC-1, `schema/001-init.sql`, `rust_thoughts/04-file-watcher-incremental-compile.md`.

> rejection_feedback  TEXT,                     -- Prompt injection for recompile
> --- `schema/001-init.sql`

#### MEM-OBJ-state-metadata
Label: State metadata

Initial SQLite `links`, `jobs`, `audit_log` and `contradictions` retain distinct operative parts. Links are symbolic page relations plus natural-language relationship context. Jobs retain symbolic status/payload/result JSON with potentially opaque content; pending-job views support scheduling, not knowledge retrieval. Audit rows retain hashes, model, operation, timing and cost, not full input/output content or readable reasoning. Contradictions retain page IDs/severity/resolution metadata plus a natural-language conflict description. SQL views expose published pages, open conflicts, pending jobs and aggregated audits; a view alone is not an established model consumer. Canonical receipts add route/artifact/phase metadata as Phase 2 design. Draft claims, verdicts and dissents add claim text, rationale and counter-evidence in Phase 3; this is future semantic governance, not present in initial DDL. Draft optional proof exports attest serialized artifacts by design, not factual truth. No supplied object counterpart; unlike [RT-OBJ-proxy-queues](runtime.md#rt-obj-proxy-queues), the jobs table is proposed durable SQLite state, not RAM queue state. SRC-1, `schema/001-init.sql`, `SPECIFICATION.md`, `MNEMOSYNE_SPEC_v0.2.md`.

> input_hash  TEXT,                               -- SHA-256 of input prompt/content
> output_hash TEXT,                               -- SHA-256 of output content
> --- `schema/001-init.sql`

> description TEXT NOT NULL,                      -- Human-readable explanation of the conflict
> --- `schema/001-init.sql`

#### MEM-OBJ-knowledge-graph
Label: Knowledge graph

The graph study proposes RAM `KnowledgeGraph`, a symbolic derived view of SQLite published-page nodes and links, rebuilt on startup. Nodes carry identity/path/namespace/maturity/confidence/hash, not a content field in the displayed `PageNode`. Edge context is natural-language relationship description. Publication is intended to update the view; the complete database/view withdrawal protocol is not established by a standalone remove method. Consumers are graph operations and the proposed QueryEngine. Distinct from the durable metadata above and from [RT-RTE-client-query](runtime.md#rt-rte-client-query)'s opaque external Link query. No supplied object counterpart. SRC-1, `rust_thoughts/05-graph-traversal.md`.

> /// The in-memory graph, rebuilt from SQLite on startup
> pub struct KnowledgeGraph {
> --- `rust_thoughts/05-graph-traversal.md`

#### MEM-OBJ-agent-pack
Label: Agent pack

Proposed filesystem pack copies published Markdown into `articles/`, serializes metadata to `index/INDEX.json`, and generates `AGENTS.md` navigation and a manifest. Markdown bodies are natural-language knowledge; index/manifest are symbolic display/access metadata, not a substitute for page content. Lineage is exported page content plus generated navigation. Canonical layout additionally lists graph links and recent audit JSONL; those outputs are not written by the inspected pack function. File-aware agents are explicitly documented later consumer roles, not observed integrations. No supplied counterpart; this is a separate retained delivery artifact from [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)'s live publication. SRC-1, `SPECIFICATION.md`, `rust_thoughts/06-pack-export-cli.md`.

> This pack contains compiled knowledge articles for agent consumption.
> --- `rust_thoughts/06-pack-export-cli.md`

### Routes

#### MEM-RTE-memory-lifecycle
Label: Memory proposal lifecycle

Endpoints: agent proposal → inbox file → audit/approval → committed page/graph → later search; stale material → archive. Proposed OS owns admission and stale handling; agent supplies content; human or configured auto-approval decides commitment. Open requests, not a curriculum; no expected-answer oracle. Guidance is the source-native lifecycle, not an inspected model prompt. Rollback/recovery across graph/search/files is unspecified. Distinct from the compilation loop [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle) and from the implemented external Link dispatch [RT-RTE-link-remember](runtime.md#rt-rte-link-remember); neither establishes this inbox route as wired. SRC-1, `AGENTS.md`, `ARCHITECTURE.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed memory stored and flagged for review; concrete API response uninspected.
- Later read-back: committed memories are intended to be linked, searchable and cited; proposed items await admission.
- Delegated visibility: audit receives proposed content; later query sees committed content; exact assembled context uninspected.
- Selection predicate: approval/auto-approval before commitment; system stale threshold before archival, numerical threshold uninspected.
- Invalidation or expiry: archived content retained for provenance but excluded from active search by design; refresh and index removal implementation uninspected.
- Activation or effect: intended knowledge supply to external clients, not authority over their controller; changed client behavior unobserved.
- Evidence limits: policy prose and lifecycle caption; no deployed admission/archive mechanism inspected.

> | **Archived** | `wiki/archived/` | System (stale threshold) | Retained for provenance, not active search |
> --- `AGENTS.md`

#### MEM-RTE-conversation-promotion
Label: Conversation memory promotion

Endpoints: logged turns → fast-model extracted profile facts/proposals → heat/reference updates → daily decay/promotion → inbox → human-approved committed memories; cold memories archived. Proposed conversation engine owns transformation and background maintenance. Open ongoing conversations supply traces; fast model proposes facts, human approves committed memories; profile-row veto/control is unspecified separately. No answer oracle. This route consumes [MEM-OBJ-conversations](#mem-obj-conversations), produces [MEM-OBJ-user-profiles](#mem-obj-user-profiles) and memory pages, and overlaps the final admission segment of [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle). No supplied route counterpart; unlike [RT-RTE-client-query](runtime.md#rt-rte-client-query), this concerns proposed retained trace transformations rather than a legacy query call. SRC-1, `SPECIFICATION.md`, `MNEMOSYNE_SPEC_v0.2.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed extracted profile rows and memory candidates, not inspected live results.
- Later read-back: committed memories intended for later graph/search consumers; direct user-profile consumer remains undecided.
- Delegated visibility: fast model sees conversations by proposal; full selector inputs and privacy filtering uninspected.
- Selection predicate: short tier is seven turns; references raise heat, daily decay affects retention and hot mid-tier promotion; thresholds and exact window assembly uninspected.
- Invalidation or expiry: cold memories archived with provenance retained; profile active/stale/superseded states proposed; concrete expiry and recovery uninspected.
- Activation or effect: trace-derived facts may shape later knowledge requests through commitment; no live activation or improved capacity shown.
- Evidence limits: canonical schema additions plus draft pipeline, not implemented initial DDL; rejection and mistaken-fact rollback beyond approval/archive are unspecified.

> 2. Fast model extracts key facts → `user_profiles` + proposed memories
> 3. Heat score updated on reference
> 4. Decay job runs daily (background)
> 5. Hot mid-term memories promoted to `memory/inbox/`
> 6. Human approves → `memory/committed/`
> 7. Cold memories archived (retained for provenance)
> --- `MNEMOSYNE_SPEC_v0.2.md`

#### MEM-RTE-feedback-recompile
Label: Feedback guided recompilation

Part of: [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle)

This material subroute traces rejection to a later writer, rather than redeclaring the whole compilation lifecycle. Endpoints: audit rejection → persisted feedback/count → planner → queued compilation → ArticleWriter input → new article candidate. Proposed scheduler applies counter/hash rules; model writes the candidate; subsequent audit/human gate belongs to the enclosing route. Trigger is affected-concept recompilation, not autonomous deployment improvement. No reference-answer oracle; five rejections with no approvals block scheduling in the sketch, hand-edited pages are protected. Rejection can withhold publication; manual unblock and source retention afford human recovery, not a demonstrated coordinated rollback. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`, `rust_thoughts/04-file-watcher-incremental-compile.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: compile plan with queued/protected/blocked concepts, then proposed rewritten article.
- Later read-back: stored feedback is read for scheduling and proposed as writer prompt text on a later attempt.
- Delegated visibility: writer receives concept, source excerpts, style guide and previous rejection feedback; complete raw audit trace is not shown as writer input.
- Selection predicate: affected concepts; rejection_count >= 5 with no approvals blocks; hand-edit check skips protected pages.
- Invalidation or expiry: feedback replacement/clearing and count reset uninspected; snippets do not establish deployed state transitions.
- Activation or effect: feedback requests changed article content and counter affects planned retry admission; actual revision and benefit unobserved.
- Evidence limits: sketch references audit_log page_id/action absent from initial DDL and a feedback lookup inconsistent with local scope; it does not establish executable wiring.

> Previous rejection feedback: {}
> Address this in your rewrite.
> --- `rust_thoughts/04-file-watcher-incremental-compile.md`

This supplies retained content-directed reasons by design, but does not independently establish any theory-builder condition beyond the conditional account in [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle). Generic feedback and a new article label do not prove criticism assigns blame to a formulated theory or that improved future capacity results.

#### MEM-RTE-graph-context
Label: Graph query context

Endpoints: retained published pages/links → reconstructed graph → get_context(page_id, depth) → assembled pack text → Ollama generation. Proposed QueryEngine owns selection; a supplied page ID seeds it, with question-to-ID resolution not shown. This is a distinct study route from external [RT-RTE-client-query](runtime.md#rt-rte-client-query). SRC-1, `rust_thoughts/05-graph-traversal.md`, `schema/001-init.sql`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed Answer from generation; graph API alone returns ContextGraph.
- Later read-back: published page/edge state from earlier writing is intended to become later query context.
- Delegated visibility: assembly asks for primary title/content and up to five outbound neighbor titles with edge type/context; inbound pages and full neighbor bodies are not included by that assembler.
- Selection predicate: page ID selects primary; BFS traverses incoming/outgoing reachability when depth >= 1; assembler takes first five outbound entries and requires an edge for each displayed entry. No semantic ranking shown.
- Invalidation or expiry: startup reload plus proposed incremental graph updates; complete coordinated stale-page removal uninspected.
- Activation or effect: generation receives knowledge text; compliance, answer quality and changed behavior unobserved.
- Evidence limits: PageNode lacks content used by assembler; link query uses from_id/to_id/weight unlike initial source_id/target_id schema. Positive depth enables unrestricted BFS, not an enforced one-hop bound; token counting/trimming is not shown.

> for neighbor in context.outbound.iter().take(5) {
>     if let Some(edge) = &neighbor.edge {
> --- `rust_thoughts/05-graph-traversal.md`

> let mut bfs = Bfs::new(&*graph, *primary_idx);
> while let Some(neighbor_idx) = bfs.next(&*graph) {
> --- `rust_thoughts/05-graph-traversal.md`

#### MEM-RTE-pack-export
Label: Pack export readback

Endpoints: SQLite published-page selection + vault files → copied articles/index/navigation/manifest → documented import by a file-aware agent. Proposed export command owns snapshot selection and physical copying; external agent controls which files it actually reads. Export is an open operator request, not new semantic approval or an answer-oracle comparison. Published-stage selection inherits prior admission rather than re-auditing content. Distinct from [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish)'s external-backend synchronization. SRC-1, `rust_thoughts/06-pack-export-cli.md`, `SPECIFICATION.md`.

- design conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: proposed export directory and completion log, optional compression request.
- Later read-back: documented file-aware agents can import the retained directory and navigate articles by title/ID; no deployed client wiring inspected.
- Delegated visibility: copied Markdown bodies, selected page metadata and generated navigation, not necessarily canonical graph/audit export files.
- Selection predicate: stage = published; file must exist for copying, but an index entry is added even if it does not; title sanitization determines output filename.
- Invalidation or expiry: no deletion of old export files in inspected function; duplicate sanitized titles can share a destination; fresh-directory export and later pack replacement are not enforced here.
- Activation or effect: affords later knowledge delivery; directory import recommendation is not evidence of model consumption or compliance.
- Evidence limits: study snippet, not shipped binary; no consumer token budget, approval recheck, complete source inclusion or proof verification established. Export failure recovery is unspecified beyond returning errors.

> Import this directory into any file-aware agent.
> --- `rust_thoughts/06-pack-export-cli.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-feedback-guidance
Label: Retained feedback guidance

Consumer: proposed ArticleWriter model. Channel: previous rejection feedback appended after source material in the generation prompt. Force: interpretive rewrite instruction, not code-enforced factual correction. Horizon: later compilation attempt after feedback persistence. Referent: [MEM-OBJ-rejection-feedback](#mem-obj-rejection-feedback); route: [MEM-RTE-feedback-recompile](#mem-rte-feedback-recompile). Distinct from [RT-BAP-compile-guidance](runtime.md#rt-bap-compile-guidance), which concerns a reusable compilation template rather than use-derived criticism. SRC-1, `rust_thoughts/04-file-watcher-incremental-compile.md`; the route's quoted instruction supplies the passage.

#### MEM-BAP-query-knowledge
Label: Query knowledge supply

Consumer: proposed query model and external file-aware agents. Channel: graph-assembled generation input or imported pack files. Force: knowledge and relationship context interpreted by a model/client, not control over the agent's own tool policy. Horizon: later queries/sessions if retained pages/packs are selected. Referents: [MEM-OBJ-knowledge-graph](#mem-obj-knowledge-graph), [MEM-OBJ-agent-pack](#mem-obj-agent-pack); distinct from [RT-BAP-compile-guidance](runtime.md#rt-bap-compile-guidance)'s compiler instruction. SRC-1, `rust_thoughts/05-graph-traversal.md`, `rust_thoughts/06-pack-export-cli.md`.

> self.ollama_client.generate(question, &pack_text).await
> --- `rust_thoughts/05-graph-traversal.md`

## Annotations

#### On [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish)

Retained result is [MEM-OBJ-unified-vault](#mem-obj-unified-vault). Curation is software normalization/copying and collision renaming, not fresh content validation. Starting publish does not supply per-page human consent. Synto `.drafts` exclusion has no Synthadoc counterpart; neither copier checks page approval/hash/write guard. Subsequent overwrites are known even though original authoring control is external. Source deletion does not remove copied destinations in these loops; optional Git history does not itself restore search indexes or Link state. Downstream Link snapshot calls pass tag/vault, not unified text/path, so exact content transfer into Link remains unresolved. SRC-1, `prior-art/v0-glue/jarvis_kb/vault_sync.py`; supplied route passages support these limits.

#### On [RT-RTE-client-query](runtime.md#rt-rte-client-query)

Read-back is caller-requested backend retrieval, not independent unsolicited push. Link receives q and limit; LLM-WIKI receives search/ask text and vault. The gateway assembles no retained page context itself, filters no source namespace and enforces neither returned context_budget nor unused history_budget. Its MCP text wrapper contains backend display output, not evidence that all backend memory or reasoning was exposed. Session/history state and model-visible budgets remain backend-owned. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`; the supplied route contains the exact returned-budget contrast.

#### On [RT-RTE-link-remember](runtime.md#rt-rte-link-remember)

Write agency is generic caller content, with human participation unresolved. Physical persistence and admission belong to opaque Link; the adapter supplies neither local inbox review nor durable deduplication. Content/tags/project HTTP input and content/tags CLI fallback are different admission paths. The later read consumer is Link query, but matching rules, storage substrate, forgetting, rejection and response summaries are not inspectable inside this source set. Source-native “commit” language in the tool description cannot establish final approval. SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`.

#### On [RT-OBJ-compile-template](runtime.md#rt-obj-compile-template)

Context construction includes related-page summaries truncated to 200 characters, flagged claim pairs/severity and source text truncated using max_tokens - 500. Jinja truncation operates on text length, not demonstrated token accounting. The selector supplying related_pages is not shown in the inspected template. The source remains in retained raw material by design, while a bounded rendering reaches the compiler; no automatic reload tool is demonstrated inside that invocation. Source reliability scoring is proposed in fast extraction, not proof of trust isolation. SRC-1, `python_thoughts/05-heavy-llm-compilation.md`.

> - [[{{ page.title }}]] ({{ page.namespace }}): {{ page.summary | truncate(200) }}
> --- `python_thoughts/05-heavy-llm-compilation.md`

> {{ source_content | truncate(max_tokens - 500) }}
> --- `python_thoughts/05-heavy-llm-compilation.md`

## Write side

**Acquisition and authorship.** Legacy ingest delegates caller-selected files to external tools; later compilation and audit do not automatically publish. Original content control cannot be inferred from invoking the CLI. The unified design separately proposes immutable raw retention, model extraction, article generation and review. Model roles do not make all supplied notes or proposals model-authored. The exact backend admission and raw provenance stay unresolved where external. [RT-RTE-foundry-tools](runtime.md#rt-rte-foundry-tools), [MEM-OBJ-vault-pages](#mem-obj-vault-pages).

**Admission, editing and maintenance.** Proposed human/configured automatic approval is distinct from physical filesystem writes. Canonical open/protected/frozen guards are policy; initial hashes/approved_at are metadata, and legacy copying does not enforce them. [RT-CLM-write-guards](runtime.md#rt-clm-write-guards). Legacy publication can overwrite existing pages and retain stale removed-source copies; failure after writes leaves partially synchronized state. [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish). Proposed archive excludes cold/stale content from search while retaining provenance; SQL link/contradiction cascades apply to actual database deletes, not proof that archiving, deleting files and removing index hits are coordinated. The export study's maintenance flags advertise clearing response cache and pruning audits (default 90 days), but the inspected flag declaration does not establish cache reuse, pruning effects or content withdrawal. SRC-1, `schema/001-init.sql`, `rust_thoughts/06-pack-export-cli.md`.

**Trace-fed transformations.** Conversation turns → extracted profile facts/proposed memories → committed pages → later query is a proposed raw-to-derived-to-consumer chain, with direct profile consumption still open. Audit rejection → persisted feedback → rewrite input is a separate proposed chain whose artifact can retain reasons. Raw audit hash/cost records alone do not provide that learning path. Neither establishes parameter learning, successful future-capacity improvement or exercised self-improvement. [MEM-RTE-conversation-promotion](#mem-rte-conversation-promotion), [MEM-RTE-feedback-recompile](#mem-rte-feedback-recompile), [MEM-OBJ-state-metadata](#mem-obj-state-metadata).

**Rejection and withdrawal.** The study requests drafts with audit feedback, and the watcher sketch blocks repeatedly rejected concepts; legacy audit merely returns external evaluation outputs without itself quarantining pages. Draft Phase 3 verdict/dissent schemas preserve reasons and possible supersession, but query effects and reversible-verdict semantics remain unimplemented/open. No automatic trace compactor or alternative checkpoint form was established in the inspected snippets; this is a coverage limit, not a repository-wide absence. Retained turn rows, profile facts, feedback and file exports are different artifacts, not interchangeable checkpoints. SRC-1, `MNEMOSYNE_SPEC_v0.2.md`, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`; records above bound each route.

## Read-back

**Request-led delivery.** The inspected bridge is pull-driven: a client asks/searches after separately invoked writes or publication. Backend stores determine actual selected content. Proposed graph context is also request-led: page ID seeds selection, then software assembles primary material and relationship summaries. Proposed pack import establishes an afforded external consumer role rather than a bare storage API, but actual reads and authority remain client-controlled. [RT-RTE-client-query](runtime.md#rt-rte-client-query), [MEM-RTE-graph-context](#mem-rte-graph-context), [MEM-RTE-pack-export](#mem-rte-pack-export).

**Automatic transformations are not unsolicited delivery.** Daily heat decay/promotion selects retained traces for memory admission, and incremental recompile selects affected content for another writing stage. Neither establishes an unsolicited memory push into an external foreground agent. The feedback writer is a known intended update consumer; direct user-profile delivery remains undecided. [MEM-RTE-conversation-promotion](#mem-rte-conversation-promotion), [MEM-RTE-feedback-recompile](#mem-rte-feedback-recompile).

**Working-context control.** Canonical design promises 24,000 context, 3,000 history and 6,000 source tokens in sample configuration, with max_sources 8; these are not enforcement evidence. Template truncation preferentially limits related summaries and raw source text, while unrendered source remains retained in the vault. Graph assembly caps displayed outbound candidates at five without demonstrated token accounting; inbound nodes returned by graph retrieval do not cross into the illustrated model input. Proposed short/mid/long retention differentiates seven-turn recent state from heat-selected older material, but exact removal, surviving tail, reload and window ordering are unspecified. The legacy gateway shows no per-task context isolation, host compaction or current-window eviction; its backend may do so, but is opaque here. Separate satellites communicate selected files/typed outputs by design, not demonstrated agent stack frames with inspected context disposal. Retained vault files resemble externally reachable storage only metaphorically: content enters a model window by value after selection, not as automatically dereferenced memory pointers. SRC-1, `config.sample.yaml`, `SPECIFICATION.md`, `python_thoughts/05-heavy-llm-compilation.md`; cited routes delimit delivery.

**Trust and authority.** Source citations, hashes and maturity labels help provenance/navigation but do not establish truth, safe prompt priority or model compliance. The compile study recommends source/system separation yet its illustrated call uses one user message, as [RT-BAP-compile-guidance](runtime.md#rt-bap-compile-guidance) notes. Legacy normalization may remove the governance metadata needed to evaluate prior approval. The consumer boundary matters: rejection text can instruct a compiler rewrite, while published bodies primarily supply query knowledge; neither grants the memory OS control of an external agent's loop. [MEM-BAP-feedback-guidance](#mem-bap-feedback-guidance), [MEM-BAP-query-knowledge](#mem-bap-query-knowledge).

## Integration issues

- **No correction to a supplied fact is required.** Added study inspection narrows interpretations that would exceed the supplied runtime: a graph depth label does not enforce one hop, a budget comment is not trimming, and the assembler uses an undeclared content field and incompatible link columns. Preserve these limits if combining graph retrieval with [RT-RTE-client-query](runtime.md#rt-rte-client-query) or [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle). Evidence: SRC-1, `rust_thoughts/05-graph-traversal.md`, `schema/001-init.sql`; [MEM-RTE-graph-context](#mem-rte-graph-context).
- **Identity overlaps, not duplicate replacement.** [MEM-RTE-feedback-recompile](#mem-rte-feedback-recompile) is explicitly a part of [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle). [MEM-RTE-memory-lifecycle](#mem-rte-memory-lifecycle) is explicit memory admission rather than raw-source compilation or direct external Link write. [MEM-RTE-pack-export](#mem-rte-pack-export) is a separate proposed file-consumer path, not legacy synchronization. Objects in this member are retained inputs/results, not replacements for supplied route/template/model records. No further possible duplicate is identified from the supplied runtime comparison.
- **Conversation/profile authority remains open.** Canonical Phase 2 establishes intended fields, draft prose supplies promotion, but no profile consumer or privacy policy is settled. Do not infer automatic profile injection, window assembly or approval of profile-row updates. Evidence: SRC-1, `SPECIFICATION.md`, `MNEMOSYNE_SPEC_v0.2.md`; [MEM-OBJ-user-profiles](#mem-obj-user-profiles), [MEM-RTE-conversation-promotion](#mem-rte-conversation-promotion).
- **Feedback integration is not executable.** Audit-log approval queries in the watcher sketch reference columns not in initial DDL; its feedback variable also does not establish complete plumbing. The writer prompt supports intended consumption, not live retries. Evidence: SRC-1, `rust_thoughts/04-file-watcher-incremental-compile.md`, `schema/001-init.sql`; [MEM-RTE-feedback-recompile](#mem-rte-feedback-recompile).
- **Export completeness and withdrawal remain unresolved.** Canonical graph/audit export entries are not written by the selected pack function; missing source files can leave indexed nonfiles, sanitized names can collide, and output-directory reuse has no cleanup. This prevents complete snapshot or revocation guarantees, not the afforded file-consumer route. Evidence: SRC-1, `SPECIFICATION.md`, `rust_thoughts/06-pack-export-cli.md`; [MEM-OBJ-agent-pack](#mem-obj-agent-pack), [MEM-RTE-pack-export](#mem-rte-pack-export).
- **Opaque alternatives stay separate.** External Link admission/storage/query, LLM-WIKI history/selection, optional vector re-ranking and proposed response cache are unresolved included surfaces. Their exact state, provenance, selectors, invalidation and later authority cannot be inferred from tool labels or aliases. Scope and missing facts are retained in the coverage table and annotations. [RT-RTE-link-remember](runtime.md#rt-rte-link-remember), [RT-RTE-client-query](runtime.md#rt-rte-client-query), [MEM-OBJ-state-metadata](#mem-obj-state-metadata). Evidence: SRC-1, `prior-art/v0-glue/jarvis_kb/mcp_gateway.py`, `ARCHITECTURE.md`, `config.sample.yaml`, `rust_thoughts/06-pack-export-cli.md`.

## Limitations and checks

Source identity was rechecked with Git HEAD and tracked-tree inspection: exact reviewed commit, clean checkout. Method identity is the supplied memory job, member type, worker rules and shared records contract, read completely. No cross-run reports or external sources were used. Direct source checks challenged confidence/disputed precedence, universal approval, one-hop graph selection, token-budget enforcement, profile injection and pack completeness; the report preserves their counterexamples and uncertainties.

Evidence remains design-led with static implementation for the legacy bridge and SQL only. Model outputs, successful admission, later activation, end-to-end recovery, deployed privacy controls and quality gains remain unobserved. Selected study sections do not establish exhaustive behavior of every study. The required deterministic invocation check returned: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Its initial finding concerned the status marker, subsequently removed. No substantive finding was narrowed or withdrawn.

Validation: passed the member content check; invocation residue, analytical support and job acceptance are not established by that check.
