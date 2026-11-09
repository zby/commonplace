---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "llm-wiki-cli memory: agent-authored Wiki, temporal capsules, retrieval controls, discussion continuity and independent learning stores."
run-id: AAS-2026-11-08-llm-wiki-cli-135ef8fbe608-01
source-identity: https://github.com/janyork/llm-wiki-cli
reviewed-boundary: e1be6ab30e83947e4b0dba97ba910acfe3bd9821
---

# llm-wiki-cli memory report

## Boundary and evidence

The subject is LWC's shipped memory loop at SRC-1, commit `e1be6ab30e83947e4b0dba97ba910acfe3bd9821`. The scope includes ordinary Wiki sources/pages, explicit retrieval controls, temporal memory, Discussion, Plan/Todo continuity, lifecycle context, private Tutor/Book/Practice stores, archive admission, and replicated/team and browser consumers. External host inference and compaction internals are not supplied implementations. No target commands, tests, examples, providers or services were executed. Implementation and doctrine establish capacities and requested behavior, not exercised learning or improved answers.

The runtime is a supplied provisional account, not a coverage limit. Direct reads added the temporal, retrieval-feedback, Discussion, Book-window, Practice-grading/scheduling and archive paths below. All new paths are in the registered Git source, not additional sources. Supplied runtime quotations support the page, changeset, ingest, hook, MCP, Tutor and team annotations. The following inventory distinguishes that dependence from direct reads and retains uninspected alternatives rather than silently excluding them.

| Operation or surface | SRC-1 paths and evidence basis | Coverage and remaining limit |
| --- | --- | --- |
| Dispatch inventory, source acquisition, metadata, deletion | Direct: `src/cli/dispatch.rs`, `src/store/content_search.rs`, `src/store/changeset_merge.rs`, `src/store/materialize.rs` | [MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-pages](#mem-obj-pages), [MEM-OBJ-purpose-schema](#mem-obj-purpose-schema), [MEM-RTE-source-admit](#mem-rte-source-admit), [MEM-RTE-content-withdraw](#mem-rte-content-withdraw). File acquisition's scanner/converter internals not audited; no universal safe-input or byte-equivalence claim. |
| Page mutation, changeset, ingest completion | Supplied [RT-RTE-page-write](runtime.md#rt-rte-page-write), [RT-RTE-changeset-commit](runtime.md#rt-rte-changeset-commit), [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete); direct memory-policy reference | Annotations retain lineage/admission distinctions; detailed ingest-analysis storage and failure/retry transitions remain uninspected. Completion does not admit every page. |
| Search, spans, weights, feedback | Direct: `src/store/indexing.rs`, `src/store/graph_search.rs`, `src/store/graph_ingest.rs`, `src/store/content_search.rs`; doctrine: core-memory and memory-policy references | [MEM-OBJ-retrieval-state](#mem-obj-retrieval-state), [MEM-RTE-retrieval-adjust](#mem-rte-retrieval-adjust). Sentence/passage fusion and span-expand algorithms not fully traced; no exhaustive ranking/parity claim. |
| Explicit tag load, autoload, MCP explore | Direct: `src/store/tags.rs`, strong-context reference; supplied [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall) | [MEM-OBJ-tags](#mem-obj-tags), hook annotation. Direct load is a requested full-page route, not the same selector as search. |
| Temporal record, recall, feedback, maintenance, hints | Direct: `src/store/temporal_memory.rs`, temporal-memory reference | [MEM-OBJ-memory-events](#mem-obj-memory-events), [MEM-OBJ-memory-controls](#mem-obj-memory-controls), [MEM-RTE-temporal-cycle](#mem-rte-temporal-cycle). Relation-chain traversal/cycle edge cases not exhaustively audited. |
| Discussion apply/read and host reply capture | Direct: `src/store/discussion.rs`, `src/agent.rs`, `skills/using-discussion/SKILL.md` | Separate [MEM-RTE-discussion-revise](#mem-rte-discussion-revise) and [MEM-RTE-discussion-capture](#mem-rte-discussion-capture). Exact prompt extraction for every host remains uninspected; capture is conditional. |
| Plan and Todo commands, tracking and hook reminders | Direct dispatch, selected `src/agent.rs` readiness branches; `skills/using-plan/SKILL.md`, `skills/using-todo/SKILL.md` | Separate objects and [MEM-RTE-task-continuity](#mem-rte-task-continuity). Store CAS/revision/reconcile internals and all stop-hook effects not fully traced. No complete enforcement or semantic-reconciliation claim. |
| Tutor turn, Soul, goal/plan, learner facts | Supplied [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn), [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish); direct learning-suite contracts | [MEM-OBJ-tutor-turns](#mem-obj-tutor-turns), [MEM-OBJ-soul](#mem-obj-soul). Goal/plan/learner-fact transformations are included but not deeply inspected; prevents a complete Tutor adaptation account. |
| Book original/normalized blobs, leases, reports, synthesis | Direct: `src/learning/book.rs` selected schema, window, commit, budget and synthesis checks; `skills/using-book/SKILL.md`, learning-suite contracts | [MEM-OBJ-book-blocks](#mem-obj-book-blocks), [MEM-OBJ-book-reports](#mem-obj-book-reports), [MEM-RTE-book-window](#mem-rte-book-window), [MEM-RTE-book-synthesis](#mem-rte-book-synthesis). Converter execution and every synthesis projection/read-back branch uninspected. |
| Practice items/papers, responses/grades, FSRS cards/queue | Direct: `src/learning/practice.rs` schema/function inventory, grading, review.rate and queue; Practice skill | Three distinct objects and [MEM-RTE-practice-assess](#mem-rte-practice-assess), [MEM-RTE-practice-review](#mem-rte-practice-review). Item verification/retirement, blueprint and override internals not deeply traced; no complete assessment-quality claim. |
| Compress/decompress/merge and overwrite | Direct: `src/archive.rs` admission/continuation/rebuild; memory-archive reference | [MEM-RTE-archive-admit](#mem-rte-archive-admit). Lower-level semantic merge resolution and continuity replay not fully audited. |
| Replica/team and SSH Sync, server/cloud reads | Supplied [RT-RTE-team-sync](runtime.md#rt-rte-team-sync); direct dispatch inventory, learning-suite contracts | Team annotation. SSH Sync/plugin-unit merge and cloud object/blob transformations remain included but uninspected; prevents complete cross-device preservation and privacy claims. |
| Physical document graph and Word Graph | Direct: graph forwarding in `src/store/graph_ingest.rs`; document-graph and word-graph references | [MEM-OBJ-derived-indexes](#mem-obj-derived-indexes). Edge validation/retraction and sidecar algorithms uninspected. Word Graph is bounded sampled co-occurrence by doctrine, not semantic verification. External CodeGraph internals outside source. |
| Maintenance, checkpoints and restore | Supplied [RT-RTE-work-runner](runtime.md#rt-rte-work-runner); direct recovery-maintenance and memory-policy references | Index/projection rebuild and checkpoint recovery are not conversation compaction. Restore implementation not deeply inspected; no proven recovery-success claim. |
| Local viewer, team/admin browser, native plugins and other host adapters | Supplied boundary/runtime reader findings; direct inventory of `src/agent/targets/` | Human readers are later consumers; pi delivery supplied by runtime. Frontend selection/rendering and non-pi adapter parity remain uninspected here. Their availability is not denied. |
| Tests and benchmarks | Supplied boundary inventory; direct memory-policy retrieval-acceptance doctrine | No new observed-run evidence established. Fixed task-specific questions/paraphrases are agent-run acceptance instructions, not an always-on CLI evaluator. Stored benchmark results not inspected; no causal benefit inferred. |

## Core ideas

1. **Evidence, compiled knowledge and history have different consumers.** Immutable source text is separately addressable from replaceable Wiki pages. Temporal capsules preserve selected changes/reasons/outcomes; Discussion retains exact visible exchanges and separately derived summaries. None is a complete automatic transcript of the agent's hidden work. See [MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-pages](#mem-obj-pages), [MEM-OBJ-memory-events](#mem-obj-memory-events), [MEM-OBJ-discussion-items](#mem-obj-discussion-items).
2. **Semantic admission is largely agent-operated, but selection is often software-owned.** Agents propose Wiki replacements and feedback; Store checks structure and concurrency. Tags bypass relevance search, weights rerank lexical candidates, hooks push bounded continuity/context, and explicit reads recover full material. A tag's priority, a retrieval weight, or a `confirmed` field is not itself evidence of a human judgment. See [MEM-RTE-retrieval-adjust](#mem-rte-retrieval-adjust), [MEM-RTE-task-continuity](#mem-rte-task-continuity) and the hook annotation.
3. **Retention can change future work without changing model weights.** Soul is natural-language guidance for later teaching; Practice converts review ratings into durable scheduler state for later queues. The latter is a code-consumed trace-derived update, distinct from storing raw responses. Neither implemented route establishes improved capacity. See [MEM-OBJ-soul](#mem-obj-soul), [MEM-RTE-practice-review](#mem-rte-practice-review), [RT-CMP-host-model](runtime.md#rt-cmp-host-model).
4. **Context recovery is not semantic compaction by LWC.** Bounded search, hooks, Book windows and status/brief calls select retained material. The host owns loss of old turns. LWC preserves restartable state outside that window rather than supplying a general summarizer for every discarded conversation. The relevant boundaries and exceptions are under Read-back.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-sources
Label: Immutable source text

Identity: `sources` rows keyed by content hash/ID, with separately tracked path revisions. Form: natural-language evidence body; symbolic hash, ID, origin and revision lineage. Substrate: selected Wiki SQLite; Markdown is a projection, not canonical authority. Producer: caller-supplied `SourceAddInput.content`, potentially after file conversion. Initial external authorship and conversion fidelity are not established by the row. New text creates a new content-hash object rather than revising the old text. Consumers: source show/diff, search, ingest windows, page citations and human readers. Citation linkage preserves a lead to evidence, not a truth guarantee. SRC-1, `src/store/changeset_merge.rs`, `src/store/content_search.rs`.

Distinct from [RT-RTE-page-write](runtime.md#rt-rte-page-write): this is its evidence referent, not a replacement page or mutation route. No supplied operative-object counterpart.

> let content_hash = hash_content(&input.content);
> --- `src/store/changeset_merge.rs`

> let source_id = tx.query_row(
>         "SELECT id FROM sources WHERE content_hash = ?1",
> --- `src/store/changeset_merge.rs`

#### MEM-OBJ-pages
Label: Compiled Wiki pages

Identity: slug-addressed page title/kind/summary/body. Form: natural-language knowledge; citations, provenance classes and wikilinks are symbolic relations with code-defined effects. Substrate: canonical SQLite and rebuildable Markdown. Lineage: agent/user authored replacements may derive from immutable sources, user statements, observations or hypotheses; source citation is not compulsory for every provenance class. Later consumers: CLI page show, search, hooks, MCP and browser readers. Body meaning is reference knowledge interpreted by agent/human, not a code-enforced instruction hierarchy. Evidence and replacement semantics: [RT-RTE-page-write](runtime.md#rt-rte-page-write), [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory), SRC-1, `skills/using-lwc/references/memory-policy.md`. Distinct object from those supplied routes/claims; no supplied object counterpart.

> User statements, session decisions, and Agent observations may lack immutable
> source IDs. If genuinely durable, store them with an explicit provenance and
> date; never invent a citation.
> --- `skills/using-lwc/references/memory-policy.md`

#### MEM-OBJ-purpose-schema
Label: Purpose and schema text

Identity: `meta` values named purpose/schema. Form: natural-language operational/domain guidance, not merely symbolic table schema. Substrate: selected Wiki SQLite; caller set/show and context expose it. `context_store` returns full schema/purpose alongside bounded page summaries and operations. Skill asks an agent to read existing policy before change; software physically replaces supplied text transactionally. Exact downstream compliance and semantic validation are unobserved. SRC-1, `src/store/content_search.rs`, `src/store/materialize.rs`, `skills/using-lwc/references/memory-policy.md`. Closest supplied context route is [RT-RTE-hook-context](runtime.md#rt-rte-hook-context); this explicit context payload is a distinct object/consumer path, not another hook record.

> schema: self.schema_text()?,
>             purpose: self.purpose_text()?,
>             pages: self.load_page_summaries(limit, 0)?,
>             recent_operations: self.load_operations(limit)?,
> --- `src/store/materialize.rs`

#### MEM-OBJ-retrieval-state
Label: Retrieval weights and feedback

Identity: `retrieval_weights` by target/provenance and `retrieval_feedback` additionally by query-token fingerprint. Substrate: Wiki SQLite, plus durable operation records. Operative symbolic parts are integer weight/signal, target, provenance and fingerprint; natural-language reasons are retained explanations. The search consumer reads numeric state, not the reason, to adjust candidate ranks. `user-provided` rows take precedence over agent observations without deleting them. Caller supplies the provenance string; human origin remains a policy obligation, not independently authenticated. Lineage: explicit caller judgment after evaluation, not passive clicks or mere retrieval. SRC-1, `src/store/graph_ingest.rs`, `src/store/graph_search.rs`, `skills/using-lwc/references/memory-policy.md`. Distinct from [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), which consumes search results; no supplied object counterpart.

> FROM retrieval_feedback
>          WHERE query_fingerprint = ?1
>          ORDER BY target_type, target_identifier,
>                   CASE provenance WHEN 'user-provided' THEN 0 ELSE 1 END
> --- `src/store/graph_search.rs`

#### MEM-OBJ-tags
Label: Explicit tag context policy

Identity: `tags` autoload policy and `page_tags` membership, priority and reasons. Substrate: Wiki SQLite. Form: symbolic enablement/order/budget/slug metadata; natural-language reason is explanatory metadata, separately from page bodies. Caller chooses membership, code stores/selects; no inferred topic assignment follows. Direct load returns complete selected pages by doctrine; lifecycle loading is budget-limited as in [RT-RTE-hook-context](runtime.md#rt-rte-hook-context). Later readers include agents inspecting reasons and hooks consuming numeric policy. SRC-1, `src/store/tags.rs`, `skills/using-lwc/references/strong-context.md`. Distinct input object to supplied hook route; no supplied object counterpart.

> Tag membership and auto-load policy are explicit durable mutations. Never infer
> or enable tags from words, links, embeddings, frontmatter, graph edges, or page
> length.
> --- `skills/using-lwc/references/strong-context.md`

#### MEM-OBJ-memory-events
Label: Temporal event capsules

Identity: event type/context plus observed, decision, constraint, learned, unresolved and outcome fragments; before/after/reason changes; evidence refs/excerpts. Substrate: Wiki SQLite tables `memory_events`, `memory_fragments`, `memory_changes`, `memory_evidence`. Form: natural-language selected history and conclusions, with symbolic identity/time/pin metadata. Producer is caller-normalized capsule, not a raw transcript collector. `learned` is a fragment label, not proof of improved capacity. Reasons/evidence survive in event payload and `memory show`/recall can return them. Lineage of an external claim remains caller-reported unless checked. SRC-1, `src/store/temporal_memory.rs`, temporal-memory reference. Distinct from [RT-RTE-page-write](runtime.md#rt-rte-page-write); no supplied temporal record counterpart.

> kind TEXT NOT NULL CHECK(kind IN (
>                 'observed', 'decision', 'constraint', 'learned', 'unresolved', 'outcome'
>             )),
> --- `src/store/temporal_memory.rs`

#### MEM-OBJ-memory-controls
Label: Temporal relations feedback and hints

Identity: `memory_relations`, `memory_feedback`, `memory_hint_state`, counters and contentless FTS. Substrate: same SQLite. Form: symbolic relations/scores/cooldowns and index terms, with separate natural-language basis/reason fields. Source: caller relations and usefulness feedback, plus automatic hint rules over retained events. Consumers: recall ranks and supersession/conflict state, retention, hint emission, status and external agent review. Relations do not rewrite old event bodies. Reasons/bases can be read with retained events, but ranking uses relation types/signals rather than semantic understanding of their prose. The cooldown state is not a retained synthesis. SRC-1, `src/store/temporal_memory.rs`. Closest supplied route is [RT-RTE-core-command](runtime.md#rt-rte-core-command), a transport that can invoke these commands; distinct object, no supplied counterpart.

> relation_type TEXT NOT NULL CHECK(relation_type IN (
>                 'supersedes', 'contradicts', 'resolves', 'supports', 'related'
>             )),
> --- `src/store/temporal_memory.rs`

#### MEM-OBJ-discussion-items
Label: Visible discussion and derived summaries

Identity: stable question/answer/option/reply/gap/summary items in Discussion JSON, with original/current text and refs. Substrate: Wiki SQLite `discussions`; submitted mutation inputs in `discussion_revisions` preserve history rather than duplicating every preceding answer snapshot. Form: natural-language visible exchanges and agent-authored summaries; symbolic IDs, DAG refs, stale/confirmed/withdrawn flags, context binding and revisions are separate operative parts. Summary refs preserve evidence lineage and software invalidates dependent summaries; current/history/item reads expose text and flags. Summary generation is external-agent interpretation, not an internal model call. SRC-1, `src/store/discussion.rs`, `skills/using-discussion/SKILL.md`. Distinct from the general mutation transport [RT-RTE-core-command](runtime.md#rt-rte-core-command); no supplied Discussion object counterpart.

> tx.execute("INSERT INTO discussion_revisions(discussion_id,revision,request_id,input,body) VALUES(?1,?2,?3,?4,?5)",params![input.id,revision+1,input.request_id,encoded,"{}"])?;
> --- `src/store/discussion.rs`

#### MEM-OBJ-plans
Label: Durable execution Plan

Identity: objective, done criteria, constraints, ordered stable steps, result/blocker/revision history and explicit context tracking. Substrate: Wiki SQLite plan tables, with symbolic status/revision/track metadata and natural-language work guidance. Caller authors/revises; `brief`, show/history and hook tracking supply later continuity. Source-native purpose is current coarse execution, not timeless Wiki knowledge or hidden reasoning. Read-only reconcile returns candidates/comparison by doctrine, not an automatic semantic adoption. SRC-1, `src/cli/dispatch.rs`, `src/agent.rs`, `skills/using-plan/SKILL.md`. Distinct from supplied general hook route [RT-RTE-hook-context](runtime.md#rt-rte-hook-context); no supplied Plan object counterpart. Deep Store enforcement remains uninspected.

> Keep execution state in this Plan. File maps should point to it, not mirror its progress. Use Wiki for stable knowledge and Memory for historical evidence.
> --- `skills/using-plan/SKILL.md`

#### MEM-OBJ-todo-items
Label: Durable deferred Todo

Identity: title, cue, detail, optional parent/tags/time, status/result and explicit context tracking. Substrate: Wiki SQLite Todo tables; natural-language task description and symbolic reminder/state metadata. Caller-authored deferred work is separately persisted from current Plan. Later consumers use show/list/search or a bounded hook reminder. Parentage does not itself mean dependencies or cascading completion by doctrine. SRC-1, `src/cli/dispatch.rs`, `src/agent.rs`, `skills/using-todo/SKILL.md`. Separate from [MEM-OBJ-plans](#mem-obj-plans), and a distinct input to [RT-RTE-hook-context](runtime.md#rt-rte-hook-context).

> Use Todo only for independent future or deferred work. It is not the current execution plan and must never be converted to or from a Plan automatically.
> --- `skills/using-todo/SKILL.md`

#### MEM-OBJ-tutor-turns
Label: Private Tutor turns and checkpoints

Identity: exact input/reply plus checkpoint and session/owner/revision binding. Substrate: independent Tutor plugin SQLite under the global plugin root; private projections are not ordinary Wiki. Form: natural-language visible teaching and selected learner-state description, symbolic binding/anchor/mode/next-action fields. These are neither hidden chain-of-thought nor a full host transcript under the contract. Lineage: submitted external-agent teaching/checkpoint, not an LWC model-produced summary. Later status/pending/show and cached hot state recover it. Evidence: [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn), SRC-1, `docs/learning-suite-contracts.md`. Distinct object from supplied route; no supplied object counterpart.

> Tutor teaching checkpoints may carry a hidden cognitive anchor containing the current
>   node, evidenced mastered nodes, mode, clearance status, and next action. The visible
>   reply never contains this raw anchor.
> --- `docs/learning-suite-contracts.md`

#### MEM-OBJ-soul
Label: Versioned private Soul

Identity: current natural-language learner guidance body plus evidence fact refs, reason and revision/history. Substrate: Tutor plugin `soul_versions` and materialized `soul.md`. Form: body is natural-language behavior-shaping preferences/constraints; refs/revision/approval/sensitivity/budget are symbolic metadata. External agent proposes revisions; command data and policy distinguish ordinary from sensitive/behavior-changing publication. Cold/recovery status supplies the complete current body for the teaching agent to cache. Reasons persist, but no supplied evidence establishes that every subsequent hot turn rereads them. Evidence: [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish), [RT-BAP-soul-guidance](runtime.md#rt-bap-soul-guidance). Distinct object from these routes/authority paths; no supplied object counterpart. Actual teaching influence and improvement remain unobserved.

#### MEM-OBJ-book-blocks
Label: Book source blobs and ordered blocks

Identity: exact original bytes, normalized text hashes, ordered block IDs/locators/ranges and preparation anomalies. Substrate: content-addressed files under Book plugin `blobs/sha256`, transactional SQLite metadata. Raw original bytes can be opaque PDF/EPUB; normalized text is natural-language evidence. Hashes, offsets, block order and lease state are symbolic, not an embedding model. Lineage: original import then direct text normalization or external conversion; provenance records converter/arguments/hash by contract, not proven converter fidelity. Later `read next`/lease recovery retrieves text; peek/search do not advance coverage. SRC-1, `docs/learning-suite-contracts.md`, `src/learning/book.rs`. Distinct from fixed executable installation [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install); no supplied Book object counterpart.

> Original and normalized bodies are content-addressed files at
>   `~/.lwc/plugins/book/blobs/sha256/<first-two>/<hash>`. SQLite stores hashes,
>   lengths, kinds, and references.
> --- `docs/learning-suite-contracts.md`

#### MEM-OBJ-book-reports
Label: Book window reports and synthesis

Identity: window summary/key points/new concepts/prior links/open threads/anomalies, followed by versioned hierarchy summaries, mainline and relations. Substrate: Book SQLite report/synthesis tables and private Wiki projection. Form: natural-language agent-derived accounts, symbolic source ranges/hashes and coverage/revision metadata. Distinct operative parts: window reports returned with committed lease; synthesis has a separate full-coverage and anomaly gate. Reasons/open threads may survive in reports; no general claim that the next window automatically includes all earlier reports is established. SRC-1, `src/learning/book.rs`, `skills/using-book/SKILL.md`. No supplied object counterpart; related supplied installer [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install) does not characterize this retained material.

> "INSERT INTO book_window_reports(
>            lease_id,summary,key_points_json,new_concepts_json,prior_links_json,
>            open_threads_json,anomalies_json,created_at
> --- `src/learning/book.rs`

#### MEM-OBJ-practice-items
Label: Practice item and paper revisions

Identity: versioned prompts, answer JSON, rubric, exact source refs and state; frozen paper item revisions. Substrate: private Practice SQLite. Natural-language text/rubric is interpreted by learner/grading agent; answer JSON and fixed paper bindings are symbolic inputs to exact objective grading. External caller generates items, verification/publication is a separate transition; initial truth is not proved by `verified` alone. The skill asks rereading sources before verification. Consumers: paper/attempt, objective comparator and subjective grading agent. SRC-1, `src/learning/practice.rs`, `skills/using-practice/SKILL.md`. No supplied operative counterpart; unlike [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn), these are durable assessment material rather than lightweight teaching turns.

> Generated items stay draft until prompt, answer, rubric, and exact source ref are
>    re-read and verified.
> --- `skills/using-practice/SKILL.md`

#### MEM-OBJ-practice-responses
Label: Practice responses grades and mistakes

Identity: durable visible response/history, frozen-revision grade/rationale/confidence/method/review state and mistake history. Substrate: independent Practice SQLite. Form: natural-language responses/rationale and symbolic scores, revisions and state. Lineage: learner-visible response submitted by caller; objective code comparison or agent-rubric judgment produces grade. Preserving these raw/assessed records alone is not a derived learning update. Later response/grade/attempt reads expose them; skill requires recovery before creating another attempt. SRC-1, `src/learning/practice.rs`, `skills/using-practice/SKILL.md`. Distinct from [MEM-OBJ-practice-items](#mem-obj-practice-items) and supplied Tutor turn route; no supplied counterpart.

> submission freezes already durable responses.
>    Abandonment preserves history.
> --- `skills/using-practice/SKILL.md`

#### MEM-OBJ-fsrs-cards
Label: Derived Practice scheduling state

Identity: `fsrs_cards`, ordered `review_events`, review controls and debt. Substrate: private Practice SQLite, serialized card JSON plus numeric/date/version fields. Form: symbolic numerical state interpreted by fixed scheduling rules, not distributed-parametric model weights. Source: submitted 1–4 rating/review time and existing card, configured retention and default scheduler parameters. `review.rate` derives a successor; queue reads due/risk/goal metadata under a time budget. Ordered history and parameters persist, enabling inspection of how a date arose; queue does not need a natural-language rationale to select. SRC-1, `src/learning/practice.rs`. No supplied counterpart; closest supplied learning route [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn) does not compute scheduler state.

> let next = FSRS::new(parameters).next(card, reviewed, rating);
> --- `src/learning/practice.rs`

#### MEM-OBJ-derived-indexes
Label: Derived retrieval and graph projections

Identity: lexical FTS, sentence/passage search spans, document graph sidecars and sampled Word Graph output. Substrate: SQLite/index and selected graph sidecar; browser response for Word Graph. Form: symbolic tokens/offsets/edges/IDs, not evidence of dense embeddings. Derived from source/page content, citations, links and explicit semantic relations. Search and graph traversals consume indexes; agents/humans interpret retrieved text/relationships. Different operative parts have different freshness: inactive spans are revision boundaries; document graph can lag canonical commits; Word Graph is a bounded on-demand sample. SRC-1, `src/store/indexing.rs`, `src/store/graph_ingest.rs`, core-memory/document-graph/word-graph references; [RT-RTE-work-runner](runtime.md#rt-rte-work-runner) supplies rebuild execution. No supplied object counterpart. Sidecar internals and full span fusion remain uninspected, so complete parity/semantic quality is not established.

> A displayed edge proves sampled term occurrence, not semantic
> equivalence or causality.
> --- `skills/using-lwc/references/word-graph.md`

### Routes

#### MEM-RTE-source-admit
Label: Source acquisition and later evidence read

Caller supplies curated input; CLI source add/add-dir/add-manifest prepares it; Store inserts hash-addressed content, indexing it and registering a pending ingest job. Different from supplied [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete): this admits raw evidence before semantic integration. SRC-1, `src/cli/dispatch.rs`, `src/store/content_search.rs`, `src/store/changeset_merge.rs`, memory-policy reference.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: source identity/created state and possible graph Work, not a completed synthesis.
- Later read-back: source show/diff, lexical source search and ingest windows return retained evidence on later commands.
- Delegated visibility: requesting external agent or authorized human reader; no model worker is created.
- Selection predicate: exact selected scope/path/manifest inputs on write; source ID/window offsets or query on read.
- Invalidation or expiry: same content hash reuses source; new path revision can supersede tracked head without rewriting older text; guarded removal is separate.
- Activation or effect: canonical text and ingest-pending state persist; comprehension and downstream use remain unobserved.
- Evidence limits: complete scanner/converter preparation and source-window delivery were not audited; immutable means retained snapshot, not proven faithful original or live truth.

Admission control: caller chooses content; software transactions/checks admit physical rows; skill requests secret review/redaction and acknowledgement only after inspection. Starting ingestion is not per-content human approval. Proposer/semantic reviewer is external caller, software can reject invalid preparation. Mode: open sources; no semantic answer oracle. Recovery: transaction failure prevents that transaction; post-commit projection error need not undo canonical insertion. Semantic guidance is source safety, immutable citations and explicit provenance; source text, path lineage and operation metadata persist.

> "INSERT OR IGNORE INTO ingest_jobs(source_id, status, updated_at)
>              VALUES (?1, 'pending', {TIMESTAMP_SQL})"
> --- `src/store/changeset_merge.rs`

#### MEM-RTE-content-withdraw
Label: Guarded canonical content withdrawal

Caller invokes page/source remove; Store checks inbound links or citations, deletes canonical object and its retrieval state/index, then reconciles projection. This is a distinct deletion route, not another declaration of [RT-RTE-page-write](runtime.md#rt-rte-page-write). SRC-1, `src/store/content_search.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: removal receipt/graph Work or page_in_use/source_in_use rejection.
- Later read-back: ordinary reads/search use remaining canonical content; deleted content no longer supplies those routes, though backups/history may remain.
- Delegated visibility: later store readers see admitted removal; no delegated model.
- Selection predicate: exact scope and slug/source ID; references determine veto.
- Invalidation or expiry: removes FTS and retrieval feedback/weights; spans deactivate; removing tracked source head can untrack its path lineage.
- Activation or effect: transaction withdraws active content before graph projection finishes.
- Evidence limits: no universal erasure claim across checkpoints, archives, replicas or prior model contexts; all projection recovery branches uninspected.

Proposer: caller. Veto: structural code check, not an independent truth evaluator. Human content approval unresolved. Open maintenance, no answer oracle. Recovery is separate checkpoint/restore or new content admission, not automatic semantic undo. Withdrawal guidance and preserved operation metadata do not prove reasons for every removal are retained.

> "SELECT COUNT(*) FROM links WHERE to_slug = ?1 AND from_slug <> ?1",
> --- `src/store/content_search.rs`

> "SELECT COUNT(*) FROM page_sources WHERE source_id = ?1",
> --- `src/store/content_search.rs`

#### MEM-RTE-retrieval-adjust
Label: Explicit evaluation changes retrieval ranks

Caller writes document weight or exact-query relevance feedback; Store validates target/provenance/reason and persists it. Later search reads effective rows and adjusts lexical-candidate rank before selection. Distinct from supplied [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall): this changes persistent selector state, not just requests a result. SRC-1, `src/store/graph_ingest.rs`, `src/store/graph_search.rs`, memory-policy reference.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stored weight/feedback receipt or validation error.
- Later read-back: search loads effective weights and query-fingerprint feedback, changing candidate rank; weight list exposes state.
- Delegated visibility: later requesters receive reranked results, not necessarily the durable natural-language reason.
- Selection predicate: target type/ID; feedback uses ordered tokenizer fingerprint, weights apply across queries; user-provided provenance wins.
- Invalidation or expiry: explicit clear/replacement; page/source deletion clears related rows; no paraphrase generalization follows from fingerprint equality.
- Activation or effect: code-level numeric ranking dependence is wired; relevant results and improved answers are unobserved.
- Evidence limits: no passive-success learning, semantic query matching or proof that a caller's user-provided label came from a human.

Admission: caller evaluates/proposes, software checks fields and commits; no universal human content gate. Guidance requests inspecting exact result/current evidence, not clicks or rank position. Rejection/rollback: invalid fields fail; explicit clear withdraws rows. Mode: open judgments. The skill's separate fixed retrieval gate predeclares expected page/source IDs and repeats questions/paraphrases; that is an agent-supplied acceptance oracle, not part of the numeric feedback command. It retains reasons but the search consumer uses scores. This is explicit evaluation-fed adaptation of selection, not internal semantic synthesis or demonstrated learning.

> explanation.signals.feedback_adjustment =
>             feedback.get(&key).copied().unwrap_or_default() as f64;
> --- `src/store/graph_search.rs`

#### MEM-RTE-temporal-cycle
Label: Temporal capsule retention and recall

External caller submits a normalized event; transaction adds fragments/evidence/relations/index, applies retention and emits review hints. Later recall lexically searches retained events, accounts for supersession and feedback, labels conflict/latest-known and returns bounded events. Closest supplied [RT-RTE-core-command](runtime.md#rt-rte-core-command) is only a transport; this distinct route was not declared there. SRC-1, `src/store/temporal_memory.rs`, temporal-memory reference.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: event identity, retention/pressure and up to three hints; normal compact receipt may require show/full for full event.
- Later read-back: explicit memory recall/show returns persisted event with reasons/evidence; feedback modifies later recall ranking, not old prose.
- Delegated visibility: caller receives history/hints; lifecycle policy forbids raw temporal recall or maintenance solely from a hook.
- Selection predicate: token OR FTS, time bounds, default supersession visibility, feedback adjustment; candidate pool is limit times eight clamped to 1000, final limit 1–1000.
- Invalidation or expiry: ordinary retention evicts old/unprotected events and then oldest eligible capacity candidates; replica stores preserve events and can reject over-capacity writes; supersession is explicit relation, not timestamp-only replacement.
- Activation or effect: retained event/relations and bounded hint/score effects are wired; synthesis of a hint into Wiki remains a separate external-agent decision.
- Evidence limits: recall sets live_verified=false; historical latest_known does not establish current truth. Relation-chain edge cases and complete protection predicate semantics were not audited.

Admission: caller authors content and relations; code normalizes/validates, rejects disabled scope, request-ID content conflict or unfit protected capacity. `request_id` is retry identity, not semantic deduplication. Age/capacity eviction is automatic code curation, not a human decision for each event. Hints inspect explicit contradictions/supersession, five same-type/context events, aged unresolved fragments or 80% pressure, with seven-day cooldown. The retained hint state is access metadata; a review request is not derived knowledge. No answer oracle is present. Mode: open milestone history. Rollback is transaction-level on failure; explicit successor relation preserves history subject to retention, not an automatic contradiction resolution. Raw tool logs/chat are excluded by doctrine, not a proven arbitrary-content detector.

> live_verified: false,
> --- `src/store/temporal_memory.rs`

> "memory_capacity_exceeded", "replicated memory is preserved; increase the configured capacity instead of evicting unsynced events"
> --- `src/store/temporal_memory.rs`

#### MEM-RTE-discussion-revise
Label: Discussion editing and summary invalidation

Agent submits visible Q/A and derived summaries via apply; code keeps stable items/original text and revision inputs. Revisions/moves/withdrawals invalidate dependent summaries, clearing confirmation. Later current/item/show/history recovers state. Distinct from [RT-RTE-core-command](runtime.md#rt-rte-core-command), whose transport does not define this transformation. SRC-1, `src/store/discussion.rs`, Discussion skill.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: apply receipt/current revision or validation/conflict error.
- Later read-back: current returns bounded pending questions/last item and capture state; show/history page 1–100 items/revisions; export exposes full body when requested.
- Delegated visibility: exact owning context or imported unbound discussion; another context is not silently entitled to take over by the skill protocol.
- Selection predicate: discussion ID/context, item ID or offset/limit; current selects active unanswered questions, at most 20 IDs and three bounded question texts.
- Invalidation or expiry: revise/withdraw/restore/move can mark dependent summaries stale and unconfirmed; history retained; stale summary cannot simply count as current confirmation.
- Activation or effect: code flags dependency changes; semantic rewriting is external agent work. Later compliant consumers should recheck stale summary evidence.
- Evidence limits: confirmed is caller-submitted state, not independently authenticated user approval; display is only reported with host message evidence, not observed delivery.

Proposer: agent/user via caller. Software admission: structural refs/DAG/state/revision and size checks; agent supplies meaningful summary/revision reason. Human confirmation is required by policy only for explicit confirmation, not for all writes. Open iterative discussion, not a fixed curriculum; no independent answer oracle. Withdrawal is non-destructive flags; restore exists; summary revision retains current refs and history. Guidance asks addressable conclusions with Q/A refs and preserves corrections, tradeoffs, rationale and unresolved issues. This is trace-to-derived-summary capacity, but automatic code invalidation alone does not formulate content-directed criticism.

> item["stale"] = json!(true);
>                 item["confirmed"] = json!(false);
> --- `src/store/discussion.rs`

#### MEM-RTE-discussion-capture
Label: Conditional exact host reply capture

Prompt/turn-start hook checks bound context, message ID, raw-submitted prompt form and active Discussion. It opens existing project storage for capture and inserts an unassigned reply through discussion_apply, notifying the agent to associate it. This is an alternate admission path, distinct from agent-authored [MEM-RTE-discussion-revise](#mem-rte-discussion-revise) and broader supplied [RT-RTE-hook-context](runtime.md#rt-rte-hook-context). SRC-1, `src/agent.rs`, `src/store/discussion.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: persisted-unassigned notice or capture-failed notice; unsupported/no-active-discussion branches do not capture.
- Later read-back: current shows unassigned count/continuity; item/export/show reads exact retained reply for association and possible summary.
- Delegated visibility: current host context receives notice; no semantic worker is spawned.
- Selection predicate: exact RawSubmitted prompt plus nonempty at-most-256-byte message ID, active bound Discussion in existing project store.
- Invalidation or expiry: duplicate message ID with identical original text replays; changed text fails and requires explicit correction.
- Activation or effect: raw visible reply is retained automatically without per-reply approval; summary derivation is a separate agent action.
- Evidence limits: not complete host capture, not arbitrary prompt/tool/system logging; host-specific prompt extraction and delivery success unobserved.

Admission owner: hook condition and Store checks. User authored visible text; software initiates physical write; no separate per-content human approval. Mode is active discussion. No oracle or semantic successor selection. Failure exposes a gap, rather than authorizing fabricated capture. This is automatic raw trace retention, not by itself a durable derived behavior-shaping update.

> exact.form == targets::PromptForm::RawSubmitted
> --- `src/agent.rs`

> "host message changed; explicit correction required",
> --- `src/store/discussion.rs`

#### MEM-RTE-task-continuity
Label: Explicit task records and context-bound cues

Caller uses Plan/Todo command families; dispatch opens selected Store for mutation/read. Explicit track binds records to an opaque context. Later brief/show and hooks provide durable continuity rather than loading a full execution transcript. This distinct task-record route feeds, but does not duplicate, [RT-RTE-hook-context](runtime.md#rt-rte-hook-context). SRC-1, `src/cli/dispatch.rs`, `src/agent.rs`, Plan/Todo skills.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mutation/read receipt, including changed state/revision or Store error; hook returns bounded readiness/continuity cue.
- Later read-back: Plan brief/show/history and Todo show/list/search reopen retained state; matching context hook readiness selects tracked records.
- Delegated visibility: cues target resolved current context, not a general broadcast to model subagents; legacy unbound/internal readiness fallbacks require care.
- Selection predicate: exact scope/ID/context and explicit tracking, enabled capabilities; context-bound Todo readiness truncates aggregate reminders to three.
- Invalidation or expiry: untrack stops that context association; Plan revisions and Todo transitions supersede current state; task completion/cancellation does not mean canonical history was purged.
- Activation or effect: retained task guidance/cues can shape continuation; host compliance and actual completed work remain unobserved.
- Evidence limits: detailed Store CAS/reconcile enforcement and all stop-hook branches uninspected; dispatch plus doctrine do not establish semantic correctness of evidence/completion.

Write admission is caller-authored content plus selected Store operations; skill asks inspect-current/if-revision before mutation and refuses blind conflict overwrite. Human approval of each step/result is not mandated; waiving Plan work requires user-instruction basis by policy. No answer oracle: supplied done criteria/evidence are task-specific, not proven verification. Open task workflow. Read-only reconcile proposes comparison candidates, not autonomous mutation. Separate Plan/Todo enablement is consent to capability, not approval of each persisted description.

> todo_omitted += todo_reminders.len().saturating_sub(3);
>         todo_reminders.truncate(3);
> --- `src/agent.rs`

#### MEM-RTE-book-window
Label: Ordered leased reading and recovery

Caller imports/prepares Book, then asks read next with budget/owner/revision. Code selects whole contiguous blocks from durable cursor, stores an exact lease, and returns source text. Agent submits structured report; commit checks live lease owner/revision/hash/order then advances coverage. Separate from supplied [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install), which only admits executable capability. SRC-1, `src/learning/book.rs`, Book skill.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: exact source lease or committed lease/report and coverage receipt; insufficient budget/stale owner/expired lease can reject.
- Later read-back: outstanding lease recovery rereads same selected source range; status/coverage recover position; subsequent next reads durable cursor, not the agent's claimed position.
- Delegated visibility: external reading agent receives text/locators/hashes; forwarding to another host is not observed.
- Selection predicate: exact book ID and next ordinal, ready/reading state and one active lease; whole blocks fit source budget; no relevance ranking.
- Invalidation or expiry: lease expiry prevents coverage advance; renewal/takeover separate; stale revision/range mismatch rejects; committed report advances cursor.
- Activation or effect: ordered committed coverage gates later synthesis; it proves accepted report submission, not actual complete comprehension.
- Evidence limits: source token budget is not exact model-token counting; converter fidelity and pedagogical effect remain unobserved.

Working context: code keeps all other Book text out of this window. Explicit UTF-8 budget measures bytes; tokens branch uses floor(value×55/100) against character count; absent budget defaults to 65,536 bytes in inspected code. This is source allocation, not reserving an exact fraction of a host model window. Report stores summary/key points/concepts/links/open threads/anomalies, not hidden reasoning. Repeated request/owner protocol and lease recovery support context-loss continuity without a new compaction summary.

Admission: external agent writes report, software checks report fields/refs/lease; no mandatory per-window human content approval or semantic answer oracle. Guidance: read complete ordered text, commit only after reading. Recovery renews/takes over exact identity rather than guessing title. Current code allows no report-based skip to arbitrary cursor in this path.

> if next != start {
>         return Err(Error::new(
>             "coverage_order_conflict",
> --- `src/learning/book.rs`

> budget.value.saturating_mul(55) / 100,
>                 true,
> --- `src/learning/book.rs`

#### MEM-RTE-book-synthesis
Label: Full-coverage Book synthesis publication

External agent proposes hierarchy summaries/mainline/relations and anomaly dispositions; code admits only covered or explicitly corrected latest synthesis, checks required summaries and anomaly state, and persists private synthesis. Distinct from [MEM-RTE-book-window](#mem-rte-book-window): derived semantic product has a later gate than raw range/report admission. Closest supplied [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install) is not a synthesis route. SRC-1, `src/learning/book.rs`, Book skill.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: publication receipt or coverage/incomplete-summary/anomaly/revision error.
- Later read-back: Book synthesis/show/search surfaces and private projection afford later reading; complete display transformations were not traced here.
- Delegated visibility: private Book consumer, not automatically ordinary Wiki consumers; transfer requires separately selected stable reference by skill policy.
- Selection predicate: exact book revision, 100% committed coverage, required hierarchy/range summaries, nonempty mainline/relations and anomaly disposition.
- Invalidation or expiry: correction must supersede latest synthesis revision; old revisions remain in versioned tables; no purge established.
- Activation or effect: derived account is persisted after structural gate; later actual interpretation and source-grounding quality unobserved.
- Evidence limits: submitted full-coverage reports are not proof of correct absorption; every materialization/read consumer branch not inspected.

Proposer/semantic author: external agent. Admission/veto: code structural/range/revision checks; no universal human confirmation. Mode: bounded whole-book reading, not autonomous curriculum discovery. Source is the reference corpus but no expected correct semantic summary is supplied as an answer oracle. Rejection leaves correction/retry; semantic guidance demands every hierarchy summary, mainline, relation and anomaly disposition. Reasons can persist in submitted reports/synthesis, but no established internal critic revises them based on outcomes. Formulated-theory content, content-directed criticism and iterative dependence cannot be inferred from the word synthesis.

> "book must have 100% committed ordered coverage before synthesis",
> --- `src/learning/book.rs`

#### MEM-RTE-practice-assess
Label: Durable response assessment

External agent/user supplies item/paper and responses; objective grading compares saved response to frozen answer JSON, subjective grading accepts an agent-rubric score/rationale against frozen revision/rubric, retaining grade/review/mistake state. No supplied assessment route counterpart; [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn) is distinct lightweight teaching persistence. SRC-1, `src/learning/practice.rs`, Practice skill.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: durable grade receipt or response/item/rubric/revision validation error.
- Later read-back: response/grade/attempt reads recover saved assessment; mistake history is retained; complete later pedagogical selection from grades was not traced.
- Delegated visibility: external grading/teaching agent and learner-facing display; no internal model call established.
- Selection predicate: exact response revision and frozen paper item binding, objective versus subjective kind; low subjective confidence below 0.6 becomes pending_review.
- Invalidation or expiry: learner override/history is prescribed and has a separate command; override internals uninspected. Abandonment preserves history by policy.
- Activation or effect: canonical grade and possible mistake event change; improved skill or learner capacity not observed.
- Evidence limits: exact JSON equality is not a universal semantic answer judge; agent confidence/rationale are submitted claims, not independent verification.

Proposer: external item author and respondent; decider: exact comparator or external rubric-grading agent plus code validation; learner override is a prescribed human contribution. Human signoff for every grade is not required. Answer oracle: frozen paper answer JSON for objective items; frozen rubric guides subjective agent but is not an independent ground-truth answer. Mode: durable assessment; no self-generated improvement objective inferred. Rejection checks exact bindings/score bounds; subjective rationale/method/confidence and review state persist, retaining reasons rather than only a score. Grade storage alone is not trace-derived behavior revision.

> let score = if correct == actual { row.4 } else { 0.0 };
> --- `src/learning/practice.rs`

> let state = if input.confidence < 0.6 {
>         "pending_review"
>     } else {
>         "accepted"
>     };
> --- `src/learning/practice.rs`

#### MEM-RTE-practice-review
Label: Ratings derive later review queues

Caller submits flashcard rating/time; code validates verified flashcard, replays same request safely, checks monotonic time, applies pinned scheduler policy to old card, then persists review event/card/debt. Later queue computes due selection from that derived state. Separate from raw assessment [MEM-RTE-practice-assess](#mem-rte-practice-assess), with no supplied equivalent. SRC-1, `src/learning/practice.rs`, Practice skill.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: successor card/review receipt or invalid-rating/time/item error; queue returns selected/deferred items and debt.
- Later read-back: queue reads persisted card/due/debt, item state and controls; explicit card read exposes ordered review events and scheduler metadata.
- Delegated visibility: external learning agent receives schedule, not a complete raw review conversation; learner-facing exercise is host-mediated.
- Selection predicate: subject, optional goal bank, current verified flashcards, due time; order is overdue seconds, forgetting risk, goal value, stable ID; selected minutes fit min(requested, configured budget).
- Invalidation or expiry: successor card replaces selected current state, ordered reviews remain; queue filters current verified item state; no arbitrary due-date editing is prescribed.
- Activation or effect: review trace changes durable schedule that later code consumes; actual later review performance or learning gain unobserved.
- Evidence limits: scheduler crate internals not inspected; rating provenance is caller-supplied; grade does not automatically equal rating in this inspected route.

Trace chain: submitted review rating/time → numeric card/due/debt → later queue → externally operated exercise. Original trace is learner-review evidence by intended protocol, not hidden model reasoning or raw tool trajectory; its authenticity is not proved by an adapter label. Parameters/default weights are recorded, not optimized by this path. Code owns update/admission and selection; caller supplies rating, no compulsory human approval of each generated schedule. Mode: scheduled review with retention/time objective. No answer oracle determines whether a rating was truthful. Invalid/stale input rejects transaction; review history remains for inspection, not automatic rollback. This is automatic trace-fed behavior-shaping state, not demonstrated improved capacity or revised formulated theory.

> let effective_budget = configured.map_or(budget, |hard| hard.min(budget));
> --- `src/learning/practice.rs`

> due.retain(|row| row.6 <= queue_time);
> --- `src/learning/practice.rs`

#### MEM-RTE-archive-admit
Label: Archive import merge and overwrite

Caller provides complete selected-scope archive; code decodes/validates, imports missing store, returns unchanged identical state, stages differing state, or requires bound confirmation token for overwrite. Resumable conflict handling and canonical publication precede derived rebuild. Distinct from supplied [RT-RTE-team-sync](runtime.md#rt-rte-team-sync): offline archive recipient/admission, not authenticated team exchange. SRC-1, `src/archive.rs`, memory-archive reference.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: unchanged/staged/conflict/confirmation-required/completed receipt, or post-commit rebuild recovery error.
- Later read-back: admitted canonical Wiki is available through ordinary CLI/MCP/hook/browser consumers; resume recognizes publication receipt and continues rebuild instead of republishing.
- Delegated visibility: trusted recipient gets complete plaintext semantic archive, not just rendered summaries; conflict packets give external resolver bounded candidates.
- Selection predicate: exact scope/archive digest/payload hash/current target identity and merge-session state; all/cross-scope import rejected by contract.
- Invalidation or expiry: changed target/archive invalidates overwrite confirmation; conflict sessions retain state/digests; derived rebuild can resume after canonical commit.
- Activation or effect: imported or merged knowledge becomes live; safe interpretation and useful semantic merge remain unobserved.
- Evidence limits: token equality is a data gate, not independent proof of separate human consent; lower-level merge content checks and all replay transformations uninspected.

Admission proposer: archive author/recipient and optional external conflict resolver; software verifies identity/state and publishes. Skill requires separate human confirmation for destructive whole-store overwrite, not every missing-store import or merge. No answer oracle for semantic conflict resolution. Guidance treats archive content as untrusted data. Recovery repeats exact resume, not blind overwrite. Archive v1 excludes independent Tutor/Book/Practice and CodeGraph; it is not a universal export of every learning memory surface.

> if confirmation != Some(token.as_str()) {
>             return Err(AppError::new(
>                 "archive_confirmation_stale",
> --- `src/archive.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-review-schedule
Label: Review card governs queue selection

Consumer: Practice queue code, then external learning agent. Channel: stored card JSON/due/debt, read by queue; bounded selected/deferred response delivered to host. Force: deterministic selection under configured/requested budget, then skill-directed teaching rather than enforced human behavior. Horizon: durable cross-session private Practice store. Evidence: [MEM-RTE-practice-review](#mem-rte-practice-review), SRC-1, `src/learning/practice.rs`. Distinct from supplied [RT-BAP-soul-guidance](runtime.md#rt-bap-soul-guidance): code interprets symbolic schedule instead of model interpreting guidance prose. Reasons are in rating/history/parameter metadata, not a natural-language theory.

#### MEM-BAP-discussion-summary
Label: Discussion summary as recovered task evidence

Consumer: external agent/user. Channel: context-qualified current/item/show/history calls and saved summary delivery at close by skill protocol. Force: reference account with refs/currentness/confirmation state, not authority to implement a proposal. Horizon: across compact/restart and future explicit recovery of same Discussion. Evidence: [MEM-RTE-discussion-revise](#mem-rte-discussion-revise), SRC-1, `skills/using-discussion/SKILL.md`, `src/store/discussion.rs`. Distinct from supplied [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context): visible Q/A and derived summary remain in Discussion, not automatically Wiki reference context.

> Do not equate a generated summary with user
> approval or implementation authorization.
> --- `skills/using-discussion/SKILL.md`

## Annotations

#### On [RT-RTE-page-write](runtime.md#rt-rte-page-write)

Storage/form/lineage: canonical [MEM-OBJ-pages](#mem-obj-pages) versus [MEM-OBJ-sources](#mem-obj-sources) evidence. Natural-language replacement is authored by external caller; SQLite I/O and structural admission do not make LWC the semantic author. Supported provenance permits non-source-grounded knowledge. Later consumers include full explicit read, bounded MCP and unsolicited tag-selected context; actual reference influence remains model-mediated. Preserve valid citations by resubmitting them: replacement does not infer which old citations remain valid. Supplied route's direct-live alternate prevents a universal draft-evaluation claim.

#### On [RT-RTE-changeset-commit](runtime.md#rt-rte-changeset-commit)

Curation/adoption: sparse draft is an isolation surface for dependent knowledge edits, not a separate agent context. Canonical commit, checkpoint and derived projection have distinct persistence/recovery. Human content decision is not compulsory in code; lint override and direct-live writes prevent universal structural gate claims. Semantic retrieval acceptance is external-agent doctrine. SRC-1, `skills/using-lwc/references/memory-policy.md`.

> On a miss, wrong page, shallow answer, stale
> claim, or unsupported claim, revise the compiled pages and rerun the same set;
> do not weaken or rewrite a failing query after seeing results.
> --- `skills/using-lwc/references/memory-policy.md`

#### On [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete)

Raw/derived distinction: source addition already makes raw evidence searchable; source-summary and non-source pages are agent transformations with different later uses. Completion counts structure, not reading or reasoning. Rationale/contradictions are requested in maintained prose, but their exact preservation depends on supplied replacement body; no universal explanatory lineage follows from citation joins. Source refs are direct citation candidates, not computed semantic impact. SRC-1, `skills/using-lwc/references/memory-policy.md`.

#### On [RT-RTE-hook-context](runtime.md#rt-rte-hook-context)

Retained inputs are tag policy plus full page bodies, separately from symbolic readiness/task cues. This is automatic push at mapped lifecycle triggers, not query search. Supplied route establishes 100,000-character global bound and whole-page omission under tag/global/render budgets; code selects, model does not choose that set. Source bodies, transcripts and raw temporal capsules are not automatically included by that tag selector. Explicit page/source reads and requested tag load remain reload routes. Pi's one-shot pending context is not a persistent semantic summary.

New memory-specific scope limit: the hook family also conditionally captures exact Discussion replies as [MEM-RTE-discussion-capture](#mem-rte-discussion-capture) establishes. Therefore “hooks only read memory” would be false. Bound-context Plan/Todo cues are distinct from Wiki pages; legacy readiness branches with no context can inspect aggregate state, so code-wide context isolation must not be inferred solely from the skill's matching-ID rule. SRC-1, `src/agent.rs`.

#### On [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall)

Requested direction: host asks query → code selects lexical/ranked documents → bounded page text returns as tool result. Not an unsolicited memory push, and source hits are not equivalent to full source delivery. [MEM-OBJ-retrieval-state](#mem-obj-retrieval-state) can alter candidate ranks without changing stored page meaning. The supplied per-page/aggregate limits and truncation flags distinguish current display from canonical content; CLI full reads remain available. Actual forwarding/compliance by external host is unobserved.

#### On [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn)

Retention is [MEM-OBJ-tutor-turns](#mem-obj-tutor-turns), including both exact visible I/O and separately selected checkpoint state. Its cognitive anchor is not a general hidden reasoning trace. Recovery status is invoked on cold/compacted/error entry; hot turns use cached exact binding, so repeated physical loading of full retained history is neither required nor established. Supplier contract and runtime disagree in breadth about full Soul on every turn; runtime's inspected command-specific limit should remain explicit. No new source correction to the supplied runtime is asserted.

#### On [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish)

Natural-language body has later behavior-guidance authority, not executable code force. [MEM-OBJ-soul](#mem-obj-soul) preserves reasons/refs and history, but code approval metadata is not human provenance proof. Body-budget enforcement rejects oversize rather than silently truncating by contract; semantic reduction is an explicit agent revision. Trace-to-Soul updates are agent-mediated stable observation proposals, distinct from automatic FSRS updates. Triggering evidence may be learner facts/experience, but complete learner-fact update lineage is uninspected here.

#### On [RT-RTE-team-sync](runtime.md#rt-rte-team-sync)

Replicated Wiki is another persistence/delivery substrate for the same knowledge, not automatically a new semantic store ontology. Conflict resolution can revise content; transport copying alone does not synthesize knowledge. Canonical state and bounded candidate displays must remain distinct. Private learning-unit Sync is separately specified, with exact typed refs and preserved-not-ready exports when runtime missing; no all-unit merge or recovery correctness follows from team Wiki wiring. SRC-1, `docs/learning-suite-contracts.md`.

> Derived FTS/Wiki/graph files never cross.
> --- `docs/learning-suite-contracts.md`

## Write side

The principal write mechanisms have different admission owners:

| Mechanism | Content authorship versus admission | Retained result and later use |
| --- | --- | --- |
| Source add | External author/caller chooses evidence; software prepares/checks/inserts. Secret review and acknowledgement are agent policy, not proof of redaction. | Immutable evidence and tracked revisions → source/ingest/search consumers. [MEM-RTE-source-admit](#mem-rte-source-admit). |
| Page put / purpose-schema set | Caller authors semantic text. Store validates/commits; no universal human review. Changeset is an optional mechanical gate. | Replaceable knowledge/domain policy → explicit context, reads, MCP, hooks. Page source/provenance sets must be deliberately preserved. |
| Weights / tags | Caller supplies judgment or policy; code validates/persists metadata. Authorship of the judgment is separate from physical SQL. | Selector state → ranking or full-page loading. Reasons retained, but selector uses symbolic fields. [MEM-RTE-retrieval-adjust](#mem-rte-retrieval-adjust), [MEM-OBJ-tags](#mem-obj-tags). |
| Temporal record/feedback | External caller supplies capsule/usefulness; code admits and automatically retains/evicts/emits hints. | Event history → recall; feedback → future rank; hint → review opportunity, not automatically Wiki. [MEM-RTE-temporal-cycle](#mem-rte-temporal-cycle). |
| Discussion apply versus hook capture | Agent authors summaries and submits Q/A; alternate hook software saves exact raw visible reply without per-reply approval. | Raw reply → explicit association → agent-derived summary → recovery; revisions invalidate dependent summary flags. Two distinct routes, not a blanket automatic summarizer. |
| Plan / Todo | Caller proposes objectives/results and explicit tracking; dispatch delegates checks to Store; skill requires exact revisions and current evidence. | Current coarse execution or deferred work → bounded cue and explicit brief/show, not automatic Wiki promotion. [MEM-RTE-task-continuity](#mem-rte-task-continuity). |
| Tutor turn / Soul | External agent writes checkpoint/guidance; software gates pending/revision/owner or Soul revision/approval data. Sensitive human approval is policy plus data gate, not independently authenticated. | Exact I/O/checkpoint and separately versioned guidance → cold recovery/cache, later teaching. Supplied Tutor/Soul routes. |
| Book | Original author supplies raw bytes; converter/direct normalization creates ordered text. Agent writes report/synthesis; software checks lease/hash/order/coverage/anomalies. | Blob → bounded range → report/coverage → full synthesis; separate consumers and gates. [MEM-RTE-book-window](#mem-rte-book-window), [MEM-RTE-book-synthesis](#mem-rte-book-synthesis). |
| Practice | External author/learner/caller supplies item/response/rating; objective comparator, agent rubric judgment and scheduler have different authority. | Raw/graded work versus derived card/debt/queue must remain separate. [MEM-RTE-practice-assess](#mem-rte-practice-assess), [MEM-RTE-practice-review](#mem-rte-practice-review). |
| Archive / replica / Sync | Recipient or resolver proposes transfer/merge. Code enforces identity/publication gates; destructive archive consent has token protocol. | Imported live memory → ordinary consumers; interrupted projection does not mean canonical content was never admitted. Private plugin Sync internals remain unresolved. |

Maintenance is not uniformly semantic curation. Reindex/materialize/graph Work rebuilds projections; compact is database/WAL maintenance, not summary generation. Semantic contradiction reconciliation, orphan linking, duplicate merging and overview revision are agent duties prescribed by memory-policy. Guarded removal, changeset rollback/checkpoint restore, temporal retention, Discussion withdraw/restore, Book synthesis correction and Practice retirement/override are different withdrawal/revision surfaces. Their evidence and uninspected details remain beside each route; no universal delete, purge or semantic rollback is established.

The qualifying automatic trace-derived path inspected most directly is rating → FSRS card → later review queue. Temporal hints are automatic trace-triggered review metadata, not automatically adopted knowledge. Discussion raw capture alone is raw retention; summary authorship is agent-mediated. Wiki write-back and Soul revision can preserve conclusions and reasons after experience, but source code does not establish their truth or benefit. Fixed executable/runtime installation is not a learned capability update. These distinctions prevent inferring learning from every retained log or changed field.

## Read-back

**Explicit request routes.** `context` returns purpose/schema, bounded page summaries and recent operations; it is broader than a mere readiness signal but not full corpus loading. `search` returns ranked/snippet candidates, then `page show`/`source show` or spans expose chosen evidence. Feedback only reranks admitted lexical candidates. `load tag` directly requests deterministic complete pages, while MCP explore has its own document/body budgets. `memory recall/show`, Discussion current/item/show/history, Plan brief and Todo show recover use-accumulated material through later command invocations. Source-native IDs specify exact lookup targets; their mere presence is not semantic targeting.

**Unsolicited supply.** Lifecycle code selects enabled tag memberships and tracked task cues at mapped events, within budgets/deadlines. Pi appends the resulting reference envelope to `systemPrompt`; that channel is not evidence that page text can safely overrule instructions. Scope/context selection, omitted counts and fail-open behavior matter as much as successful body delivery. Conditional Discussion capture is a write side effect of prompt hooks, not a raw-history auto-recall route. Supplied [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) and [MEM-RTE-discussion-capture](#mem-rte-discussion-capture) must both be retained.

**Private learning read-back.** Tutor cold/recovery status supplies Soul/binding/checkpoint; hot teaching uses cached binding. Book reads durable cursor and exact lease text, with report submission advancing later coverage. Practice queue reads derived numeric review state rather than loading every old response/rationale. Skill-directed source transfer uses exact IDs/revisions/hashes, not copying private projections wholesale into Wiki. Browser/local/cloud readers can consume saved content without making it an agent instruction. The incomplete frontend/cloud inspection prevents claims of every byte reaching each reader.

**Working-context control.** These are predominantly bounded selection and exact reload mechanisms, not autonomous semantic summarization of the current conversation. Tag pages can be omitted whole; MCP truncates bodies with flags; Discussion current gives bounded pending/last-item summaries with explicit item/history reload; Book pushes only a contiguous source window and retains remaining blocks externally. Host compaction determines which old conversation turns disappear, and LWC recovery protocols reload exact identity/state afterwards. The stack-frame analogy fits the one-shot pi pending envelope or bounded Book window only partially: whole external material stays outside the current window, but no model subagent frame is created by these operations, and no by-reference pointer automatically resolves in model context. IDs/commands are reload instructions for a future tool call, not live references tracked by a garbage collector. No LWC-produced universal compacted conversation summary or exact host eviction preference was established; this is an inspection limit, not an evidenced absence across all hosts.

## Integration issues

1. **Hook scope must include a conditional write.** [MEM-RTE-discussion-capture](#mem-rte-discussion-capture) extends [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) with raw visible reply admission. SRC-1, `src/agent.rs`, `src/store/discussion.rs`. It does not contradict the supplied tag-selector findings, but a reconciliation that calls the entire hook family read-only would be false. Retain separate write/selection routes.
2. **Token-labelled Book budget is a heuristic, not tokenization.** [MEM-RTE-book-window](#mem-rte-book-window) traces the actual character-based floor(55%) branch in SRC-1, `src/learning/book.rs`; contracts describe a token source budget. Do not promote the label to an exact token-window guarantee. Documentation's configurable fallback is not established by the inspected `read_budget(None)` constant branch.
3. **Context-bound cues are not a universal isolation proof.** [MEM-RTE-task-continuity](#mem-rte-task-continuity) and the hook annotation retain both bound-context readiness and legacy no-context aggregate branches in SRC-1, `src/agent.rs`. Actual host selection/stop-hook wiring across every target remains uninspected. Prevents asserting universal cross-agent privacy or every hook's matching-ID enforcement.
4. **No duplicate declarations intended.** New objects have no supplied operative-object counterparts. Each new route names its closest supplied route and distinct identity. In particular retrieval-state update versus MCP read, archive versus team transport, Book/Practice operation versus installer, and Discussion capture versus lifecycle page loading are not aliases. Behavioral paths for symbolic review queues and Discussion evidence differ from supplied Wiki/Soul reference paths. No correction to a supplied factual finding is established; additions and source-label qualifications above are integration constraints.
5. **Included opaque alternatives remain unresolved.** Goal/learner-fact/Tutor-plan updates, Practice item verification/retirement/overrides/blueprints, Book synthesis display/projection, SSH Sync/private-unit merge/recovery, low-level semantic graph edges/retraction, full span fusion, checkpoint restore, non-pi host adapters and frontend/cloud rendering remain partly or wholly uninspected as the coverage table specifies. Their missing admission/lineage/delivery facts prevent exhaustive system-wide quality, privacy, semantic preservation, restoration and adaptation conclusions. Do not collapse these into absent functionality or infer them from familiar command names. Relevant records: [MEM-OBJ-soul](#mem-obj-soul), [MEM-OBJ-practice-items](#mem-obj-practice-items), [MEM-OBJ-book-reports](#mem-obj-book-reports), [MEM-OBJ-derived-indexes](#mem-obj-derived-indexes), [RT-RTE-team-sync](runtime.md#rt-rte-team-sync), [RT-RTE-work-runner](runtime.md#rt-rte-work-runner).
6. **Learning-store retention differs from Wiki withdrawal.** Learning-suite doctrine says no v1 forget/clear/purge and preserves canonical data on disable/runtime replacement; ordinary Wiki has guarded removals and temporal automatic eviction. SRC-1, `docs/learning-suite-contracts.md`, [MEM-RTE-content-withdraw](#mem-rte-content-withdraw), [MEM-RTE-temporal-cycle](#mem-rte-temporal-cycle). No all-memory erasure or uniform retention conclusion is warranted.

## Limitations and checks

All new findings are SRC-1 implementation or doctrine/design at the frozen revision. Git HEAD was checked directly and equalled the boundary pin. Supplied runtime is the only prior characterization used; no other analysis or benchmark interpretation was opened. Required job, type, collection, worker rules, records contract, boundary and both runtime ranges were read; the oversized search delivery was recovered before use. No source mutation, target execution or delegation occurred.

No supplied run establishes that delivered text changed an answer, that an agent obeyed source-trust/approval policy, that semantic summaries were correct, or that capacity improved. Implemented numeric queue/rank dependence is not causal evidence of useful outcomes. Distributed-parametric provider internals remain under [RT-CMP-host-model](runtime.md#rt-cmp-host-model), not reclassified from SQLite fields. Formulated theories, criticism, autonomy and self-improvement are not inferred from synthesis, learned fragments or scheduled learning labels.

Validation: passed the invocation-specific `commonplace-validate` member content check against this candidate and the supplied artifact (exit 0: “Member content check passes; invocation residue not checked”). This checks form and quotation occurrence, not semantic support, execution or workflow acceptance.
