---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Virtual Context memory: canonical history, derived summaries and facts, actor cards, reversible payload reduction and later consumer gates."
run-id: AAS-2026-10-14-virtual-context-bbd06cc3ac95-01
source-identity: "https://github.com/virtual-context/virtual-context"
reviewed-boundary: "74ccc570c40bb551820fcd330c42e0dfc0588f05"
---

# Virtual Context memory report

## Boundary and evidence

This report covers the memory responsibilities inside the whole-system boundary: live and imported conversation acquisition, compaction, fact lifecycle, canonical edits, optional person cards, assembly and paging, proxy payload reduction/restoration, persistence and evaluator reuse. External authorization, model service internals, host completion delivery and unavailable repair inputs remain outside the source boundary. All new source findings use SRC-1 at the reviewed commit. HEAD was checked against that commit. Evidence is implementation or explicitly attributed design; there is no supplied execution trace, benchmark result inspection or causal experiment.

Direct reads added the bodies of fact-lifecycle documentation, summary audience/rendering functions, retrieval assembly/filtering, paging management, record editing, fact-verdict and refusal read-back, compaction storage and summary rejection, actor-card input/replacement and assembly, proxy restoration and chain storage, core-file loading, types, fact-vector ranking, tag-rollup persistence/hint input and a LongMemEval checkpoint branch. CLI dispatch, other benchmark runners and repair application were searched. Supplied runtime findings cover driver/provider/hook wiring, imported acquisition, engagement and checkpoint ownership; those findings are not described as new direct inspection.

### Coverage inventory

The table distinguishes covered mechanisms from unresolved included parts. A path names source coverage, not an assurance that every branch was audited. Storage methods with no traced caller do not count as consumer routes.

| Included operation or part | SRC-1 paths; evidence basis | Records or remaining limit |
|---|---|---|
| Live headless/TUI and proxy acquisition, completion tagging | `virtual_context/tui/headless.py`, `virtual_context/proxy/server.py`, `virtual_context/proxy/state.py`, `virtual_context/core/tagging_pipeline.py`; supplied runtime | [RT-RTE-headless-chat](runtime.md#rt-rte-headless-chat), [RT-RTE-proxy-request](runtime.md#rt-rte-proxy-request), [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance). TUI replay/export fidelity beyond supplied boundary remains uninspected. |
| Canonical source content and physical provenance | `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/record_editing.py`, `virtual_context/types.py`; direct | [MEM-OBJ-source-content](#mem-obj-source-content), [MEM-OBJ-source-metadata](#mem-obj-source-metadata). Ingest reconciliation internals remain uninspected; initial truth and metadata authenticity depend on caller/host. |
| Batch import | `virtual_context/cli/import_cmd.py`, `virtual_context/import_adapters/`; supplied runtime | [RT-RTE-import-history](runtime.md#rt-rte-import-history). Adapter byte fidelity and source-origin preservation are unresolved, not absent. |
| Segmentation, merge, stub passthrough, model summary/fact extraction, tag rollups | `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/compactor.py`; selected direct bodies and searches | [MEM-OBJ-stored-segment](#mem-obj-stored-segment), [MEM-OBJ-tag-summary](#mem-obj-tag-summary), [MEM-OBJ-search-vectors](#mem-obj-search-vectors), [MEM-OBJ-fact](#mem-obj-fact); annotation on [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance). Tag-rollup generation and segmentation heuristics not fully traced; no exhaustive compression-fidelity conclusion. |
| Fact comparison, deduplication, source trust, refusals, rejection/restoration | `virtual_context/ingest/supersession.py`, `virtual_context/storage/fact_mutations.py`, `virtual_context/storage/record_edits.py`, `virtual_context/core/fact_lifecycle.py`, `docs/fact-lifecycle.md`; direct functions plus design | [MEM-RTE-fact-admission](#mem-rte-fact-admission), [MEM-OBJ-fact-ledgers](#mem-obj-fact-ledgers). SQL locking and all backend equivalences are not audited. |
| Canonical editing, forgetting, rebuild and interrupted retry | `virtual_context/core/record_editing.py`, `virtual_context/storage/record_edits.py`; direct and supplied runtime | Annotation on [RT-RTE-record-edits](runtime.md#rt-rte-record-edits); source withdrawal is distinct from model summary rejection. All caches during unfinished rebuild remain unresolved. |
| Inbound automatic selection, fact curation memo, protected DB recovery, core files, budget/filtering | `virtual_context/core/retrieval_assembler.py`, `virtual_context/core/assembler.py`, `virtual_context/core/summary_identity.py`; direct | [MEM-RTE-inbound-context](#mem-rte-inbound-context), [MEM-OBJ-curation-memo](#mem-obj-curation-memo). Retriever strategy internals and fact-curator model quality not fully inspected. |
| Model-selected paging, cold-page collapse/eviction, reassembly | `virtual_context/core/paging_manager.py`, `virtual_context/core/tool_loop.py`; direct paging plus supplied loop | Annotation on [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop). Topic removal changes the window, not underlying source retention. |
| Optional actor profile/card derivation and request-time adoption | `virtual_context/core/community/actor_card_rebuild.py`, `virtual_context/core/community/actor_card_admission.py`, `virtual_context/core/assembler.py`, `virtual_context/types.py`; selected direct reads/searches | [MEM-OBJ-actor-card](#mem-obj-actor-card), [MEM-RTE-card-refresh](#mem-rte-card-refresh). Semantic admission implementation and store disclosure transactions need further inspection for a complete privacy guarantee. |
| Proxy tool, chain and media reduction/read-back | `virtual_context/proxy/message_filter.py`, `virtual_context/proxy/handlers.py`, `virtual_context/proxy/media.py`, `virtual_context/storage/sqlite.py`; direct tool/chain bodies; media write search | [MEM-OBJ-payload-archives](#mem-obj-payload-archives), [MEM-RTE-payload-restore](#mem-rte-payload-restore). Media encoding lineage and full reduction thresholds not audited. |
| Store checkpoint, Redis/provider alternatives, canonical recovery | `virtual_context/engine.py`, `virtual_context/types.py`, `virtual_context/proxy/session_state.py`; supplied runtime plus direct type | Annotation on [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state). SQLite/PostgreSQL/filesystem/composite and Redis equivalence, TTLs and crash consistency remain uninspected. |
| MCP tools, resources/prompts; bundled OpenClaw hooks; CLI recall/retrieve/transform and admin dispatch | `virtual_context/mcp/server.py`, `virtual_context/openclaw/virtual-context.mjs`, `virtual_context/cli/main.py`; supplied recall/hooks and direct dispatch/function searches | [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools), [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks). MCP quote/date/search/resource bodies and admin backfills/migrations beyond dispatched names are not fully inspected; no universal admission/read-back invariant. |
| Engagement retained candidate/post history | `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/poster.py`; supplied runtime | Annotation on [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage). Full candidate-source selection and history substrate not directly audited. |
| LongMemEval, LocOMo, BEAM, MRCR retained cache and reader reuse | `benchmarks/longmemeval/vc_runner.py`, `benchmarks/locomo/vc_runner.py`, `benchmarks/beam/vc_runner.py`, `benchmarks/mrcr/vc_runner.py`; direct LongMemEval branch and scoped searches | [MEM-RTE-evaluator-reuse](#mem-rte-evaluator-reuse). Cache-hit watermark tests are not correctness certificates; dataset origin and reader-visible oracle handling not fully inspected. |
| AMB, JEV, context contracts, tests and CI evaluators | `benchmarks/amb/vc_provider.py`, `benchmarks/jev/`, `benchmarks/context_contracts/`, `tests/`, `.github/workflows/contracts.yml`; boundary inventory only | Included but uninspected here. Prevents comprehensive evaluator coverage, regression-outcome and measured-learning conclusions. |
| Dated export, reconstruction, disposition and canonical repair | `scripts/export_discord_guild_transcript_20260802.py`, `scripts/rebuild_men_canonical_from_discord_20260802.py`, `scripts/extend_men_vast_disposition_20260802.py`, `scripts/apply_canonical_repair_artifact_20260802.py`; boundary plus application search | Included alternative source replacement. Application search shows artifact checksum/cardinality checks, dry-run/live distinction, rollback snapshot and derived clearing names. Bodies and unavailable external artifacts prevent declaring a verified repair route or actual source faithfulness. |
| Diagnostic payload captures, telemetry and tool logs | `virtual_context/types.py`, `virtual_context/storage/sqlite.py`, `benchmarks/longmemeval/vc_runner.py`; type/read and storage/runner searches | Content and access diagnostics exist, but no traced automatic update consumer for general logs. Do not equate them with derived memory or weight training. |

## Core ideas

1. Compaction retains both a smaller interpretation and a reloadable source representation. A stored segment contains summary, full text, messages and exact-source metadata. Later context can select a summary or full depth; reduction need not mean deletion. The strongest limitation is representational fidelity, not merely whether the row persists: [MEM-OBJ-stored-segment](#mem-obj-stored-segment).
2. Source authority is enforced differently at different consumers. Fact retraction/rejection affects software eligibility; audience checks affect disclosure; a surviving summary or fact reaches the answer model as interpreted text. Names such as “verified” and “proved” do not establish truth or complete attribution. In particular, the inspected summary renderer returns stored text and tolerates missing individual source rows: [MEM-CLM-renderer-proof](#mem-clm-renderer-proof).
3. Automatic inbound retrieval and foreground model-selected paging coexist. Inbound code supplies retained material after a user request; it is not an independently timed unsolicited memory notification. Paging changes topic depth and can evict cold pages while source material remains stored. Proxy restoration additionally puts removed raw tool/chain material back into a mutable request: [MEM-RTE-inbound-context](#mem-rte-inbound-context), [MEM-RTE-payload-restore](#mem-rte-payload-restore).
4. Rejection has a retained consumer, not only an audit display. Fact-verdict keys stop the same statement from the same sources being re-admitted. Refused supersession fingerprints stop unchanged proposals being repeated. New source/fact/policy versions can reopen comparison. This is a source-responsive memory update mechanism, not demonstrated improvement: [MEM-RTE-fact-admission](#mem-rte-fact-admission).
5. Optional person cards derive behavior-shaping preferences from exact actor evidence and pass a separate model admission stage. Their assembly is gated and bounded. This is distinct from simply injecting every extracted fact or treating user text as authenticated policy: [MEM-RTE-card-refresh](#mem-rte-card-refresh).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-content
Label: Canonical turn content

Source-native identity: canonical user/assistant content loaded into compaction, and the source turns exposed for fact review. Natural-language form; substrate: canonical store rows, with caller history as an acquisition input rather than the authoritative compaction payload. Lineage includes human messages, assistant output and adapter-normalized imports; a generic importer does not prove the original author or transport. Consumers: compactor, record editor and optional canonical recent-window recovery. The compactor transforms content; the answer model interprets recovered content. SRC-1 `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/record_editing.py`, `virtual_context/core/retrieval_assembler.py`.

Closest supplied referents: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance) is a route producing derivatives from these sources; [RT-RTE-import-history](runtime.md#rt-rte-import-history) is one acquisition route. This content is not [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state)'s checkpoint metadata. No supplied content-object counterpart was found.

> "user": by_id[turn_id].user_content,
> "assistant": by_id[turn_id].assistant_content,
> --- `virtual_context/core/record_editing.py`

#### MEM-OBJ-source-metadata
Label: Canonical source identity and provenance

Source-native identity: canonical turn IDs, physical source mappings, author/audience fields, turn numbers and lifecycle epochs. Symbolic form; substrate: canonical relational rows and segment metadata, separate from message text. Lineage: host-supplied provenance plus code mappings; initialization authenticity is unresolved. Compaction binds segment membership to exact IDs; disclosure and card replacement use owner/audience identities and source epochs. These have software authority at those consumers, not model instruction authority. SRC-1 `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/summary_identity.py`, `virtual_context/types.py`.

Distinct from [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state)'s cached index/watermarks: this is source provenance used to validate or reconstruct derivatives. The source itself explicitly rejects a positional shortcut:

> # Source ids, not a conversation-sized history map, define evidence.
> # Historical merge sources are added on demand below; corrected old
> # source rows are read afresh instead of trusting cached segment text.
> --- `virtual_context/core/compaction_pipeline.py`

#### MEM-OBJ-stored-segment
Label: StoredSegment and StoredSummary content views

Source-native identity: segment summary/full text/messages and lightweight summary views. Substrate: configured store through `store_segment`/`update_segment`; the inspected SQL storage family is not a universal deployment assertion. Natural-language parts are summary and transcript/tool text; symbolic part is tags, source IDs, times, model label and references, described separately in [MEM-OBJ-source-metadata](#mem-obj-source-metadata). `StoredSummary` is a lightweight view, not a new provenance source. Tag rollups are further text derivatives; their complete generation policy remains uninspected. SRC-1 `virtual_context/types.py`, `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/summary_identity.py`.

Lineage: canonical rows → topic segmentation/optional merge → model summarization or source-text fallback → stored segment; stub passthrough can preserve text without a model rewrite. Consumers: retriever/assembler, paging and search/tool readers. At the assembler, depth chooses full text when available, otherwise summary. The answer model receives evidence/guidance, not code-enforced truth. No automatic human approval is established. This object is an output of [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance), not its duplicate and not a checkpoint.

> if depth == "full":
>     full = getattr(item, "full_text", None)
>     if isinstance(full, str) and full.strip():
>         return full
> summary = getattr(item, "summary", None)
> return summary if isinstance(summary, str) else ""
> --- `virtual_context/core/summary_identity.py`

Reasons can survive as summary prose or source transcript. The prompt requests causal rationale, but no guarantee follows that every derivative includes its reasons, or that a later selector delivers all rationale. Full-depth retrieval is a concrete alternative to relying only on a summary.

#### MEM-OBJ-tag-summary
Label: TagSummary rollup and description

Source-native identity: layer-two `TagSummary`, distinct from `StoredSummary`'s lightweight segment view. Natural-language summary/one-line description plus symbolic cover/source references and structured-summary fields; substrate: one stored rollup per cover tag/conversation. Lineage: segment summaries, turns, canonical IDs and existing rollups are passed to `compact_tag_summaries`; software writes admitted output. Consumers: context-hint construction and tag-summary embedding/scoring. A hint derived from retained descriptions can affect the model's next selection, but exact hint rendering and all structured-summary migration consumers remain uninspected. SRC-1 `virtual_context/types.py`, `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/retrieval_assembler.py`.

Different from [MEM-OBJ-stored-segment](#mem-obj-stored-segment)'s source-sized segment and from [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state)'s checkpoint. It is a distinct result of [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance). Recovery mode can leave a pre-existing rollup and its embedding untouched instead of replacing them. Thus fresh segment creation does not imply every layer-two description was regenerated.

> class TagSummary:
>     """Layer-2 summary: one per cover tag, rolls up all segment summaries for that tag."""
>     tag: str
>     summary: str = ""
>     description: str = ""  # 1-line tag description (~15-20 words) for enriched context hints
> --- `virtual_context/types.py`

#### MEM-OBJ-search-vectors
Label: Fact, chunk and tag-summary embeddings

Source-native identity: stored dense search representations, not encoder weights or readable summaries. Distributed-parametric form; substrate: configured embedding storage/search backend. Fact-vector lineage is `Fact.embed_text()` through the configured embedder; tag-summary lineage embeds the first 2,000 summary characters; chunk-vector construction is wired by compaction but its exact chunking is uninspected. Numerical vectors change on content writes/rebuilds; no encoder parameter training is established. The encoder's fixity/version/endpoint limits belong to [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider), not these output vectors. SRC-1 `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/retriever.py`.

Later consumer: fact retrieval compares query vectors, optionally recent-context query vectors, against current-model stored vectors; native store search or loaded-vector cosine ranking yields a top-N list, unioned with the tag floor. Software ranking influences which fact text is later eligible for assembly. It is not semantic truth proof or a model-readable rationale. Distinct from [MEM-OBJ-fact](#mem-obj-fact)'s statement and [MEM-OBJ-tag-summary](#mem-obj-tag-summary)'s prose, and not a redeclaration of the encoder component.

> loaded = self.store.load_fact_embeddings(
>     self._conversation_id, model, expected_dim=len(bare_vec),
> )
> --- `virtual_context/core/retriever.py`

> emb = embed_fn([ts.summary[:2000]])[0]
> --- `virtual_context/core/compaction_pipeline.py`

Missing/degraded embedding paths can return the legacy fact floor instead of stopping all retrieval. Complete model-version equivalence, stale-vector handling and all backend indexes remain unresolved. Vectors retain no independently interpretable reasons; source statements/provenance carry those separately.

#### MEM-OBJ-fact
Label: Fact content and lifecycle fields

Source-native identity: extracted `Fact` statement, event/session dates, source segment, author attribution, status and trust state. Text statement and optional `why` receive natural-language interpretation; symbolic lifecycle/source fields control eligibility, linking and chronological comparison. Substrate: fact rows and links in configured store; fact embeddings are separate numerical search representations. SRC-1 `virtual_context/core/compactor.py`, `virtual_context/core/fact_lifecycle.py`, `virtual_context/core/compaction_pipeline.py`, `docs/fact-lifecycle.md`.

Lineage: requested extraction from raw conversation, not from the generated summary; storage binds segment/conversation and refreshes source trust. Actual extraction fidelity remains unobserved. Consumers include inbound fact selection, fact tools, supersession and actor-card generation. At admission, lifecycle policy has software authority; at answer generation, text is evidence, not an expected-answer oracle. Existing [RT-RTE-record-edits](runtime.md#rt-rte-record-edits) and [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance) describe write routes, not this operative content object.

> Also extract facts from the RAW CONVERSATION TEXT above (not from your summary).
> The summary may omit details — facts must capture ALL substantive information
> from every speaker in the conversation, even details not included in the summary.
> --- `virtual_context/core/compactor.py`

“Verified” in `docs/fact-lifecycle.md` means source mapping and relevant speaker proof, not external factual correctness. Unverified material is not universally excluded: the inspected eligibility function withholds retracted/rejected states.

> return [fact for fact in facts if getattr(fact, "trust_state", "") not in WITHHELD_TRUST_STATES]
> --- `virtual_context/core/fact_lifecycle.py`

#### MEM-OBJ-fact-ledgers
Label: fact_verdicts and fact_decisions

Source-native identity: admin verdict ledger and comparison/admission decision ledger. Symbolic keys, policy/version fingerprints, source versions and outcomes drive later decisions; natural-language reasons and saved fact payload support inspection/restoration. Substrate: relational ledger tables. Lineage: explicit caller verdict or software policy decision over a model/comparison proposal. Exact host principal authentication remains outside this object. SRC-1 `virtual_context/storage/record_edits.py`, `virtual_context/storage/fact_mutations.py`, `virtual_context/ingest/supersession.py`.

Consumers: extraction admission reads rejected keys; source-trust refresh applies verdicts; restoration can reconstruct a missing fact from saved payload; candidate selection reads prior refusals. The retained reason is inspectable, but repeat suppression consumes version/policy fields rather than interpreting the prose reason. These are additional objects under the operations of [RT-RTE-record-edits](runtime.md#rt-rte-record-edits); they are not the entire edit route.

> """The facts whose statement and source turns no admin has rejected.
>
> Consulted before a segment's facts are written, so a statement an admin
> rejected is not stored again when the same turns are extracted again.
> """
> --- `virtual_context/storage/record_edits.py`

Ledger durability is bounded: the design document states deletion of the conversation removes its ledgers. “Append-only” does not mean undeletable across conversation deletion. Backend trigger equivalence is not fully audited here.

#### MEM-OBJ-curation-memo
Label: Retrieval curation memo

Source-native identity: shared-session `curation:` memo of kept candidate indices. Symbolic form; substrate: injected session-state provider, not universally the content database. Lineage: question plus fact prompt lines → SHA-256 key → curator selection → saved indices. Consumer: a later matching continuation/inbound curation invocation can reuse the decision. Authority: code selects the corresponding facts without rerunning curation; it does not add new facts or certify truth. Changes to question or formatted candidate lines select a new memo key. SRC-1 `virtual_context/core/retrieval_assembler.py`.

Distinct from [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state)'s durable checkpoint: a provider memo is a separate interface/selection cache. Its TTL and cross-worker persistence depend on provider implementation and remain uninspected.

> provider.save_retrieval_memo(conversation_id, memo_key, {"kept": indices})
> --- `virtual_context/core/retrieval_assembler.py`

#### MEM-OBJ-actor-card
Label: ActorCard and entry provenance

Source-native identity: `ActorCardEntry` bodies and `ActorCardEntrySource` evidence rows, served as an `ActorCard`. Natural-language body is a derived preference/context statement; symbolic confidence, kind, scope, supersession, validity/expiry and source IDs govern admission/rendering. Substrate: tenant/actor-scoped store cache plus rebuild status. Lineage: exact actor-authored turns and attributed facts, with candidate carryovers reconsidered against evidence. SRC-1 `virtual_context/types.py`, `virtual_context/core/community/actor_card_rebuild.py`, `virtual_context/core/assembler.py`.

Consumers: rebuild/admission models, store replacement and gated requester-card assembly. The later answer model interprets rendered bodies as contextual guidance. A card is not the source of truth and not authenticated instruction from the actor. Distinct from [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state) and the generic maintenance route: actor-scoped derived entries have their own semantic admission and request consumer.

> The card is a CACHE, not a second source of truth: every entry is derived
> from exact actor-authored canonical turns and/or facts carrying that
> actor's ``author_actor_id`` and is fully rebuildable. ``superseded_by``
> preserves the card replacement chain.
> --- `virtual_context/types.py`

#### MEM-OBJ-payload-archives
Label: Tool-output, chain and media archives

Source-native identity: full tool-output content, `chain_json` message snapshots and media metadata/file references. Substrate: store rows plus local media files for the inspected restore path. Natural-language tool/assistant content is distinct from symbolic envelope/refs; image payload is opaque to this text inspection and is not a readable textual memory summary. Lineage: proxy request tool/message bodies; stored tool/chain content is raw retained context, not automatically learned policy. Media transformation detail is uninspected. SRC-1 `virtual_context/proxy/message_filter.py`, `virtual_context/proxy/handlers.py`, `virtual_context/proxy/media.py`.

Consumers: proxy restore runtime and tool search. A stub/ref is access metadata, not the archived content itself. Restoring a chain rechecks eligibility and can remove VC-derived tool/assistant material, so the delivered object need not equal the stored snapshot. Distinct content parts of [RT-RTE-proxy-request](runtime.md#rt-rte-proxy-request) and [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop), rather than their whole route or engine checkpoint.

> store.store_chain_snapshot(
>     ref=ref,
>     conversation_id=conversation_id,
>     turn_number=canonical_turn,
>     chain_json=chain_json,
>     message_count=len(pf_msgs),
>     tool_output_refs=",".join(tool_output_refs_for_chain),
> )
> --- `virtual_context/proxy/message_filter.py`

### Routes

#### MEM-RTE-inbound-context
Label: Automatic inbound memory selection

Endpoints/progression: inbound message and recent context → retriever → audience/trust filtering and optional fact curation → core files/working pages → measured-budget assembler → caller/model channel. Owner: retrieval/assembler code; query tagging/curation may use configured models. This is a narrower selection operation shared across [RT-RTE-headless-chat](runtime.md#rt-rte-headless-chat), [RT-RTE-proxy-request](runtime.md#rt-rte-proxy-request) and [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools), not a duplicate of their driver lifecycles. SRC-1 `virtual_context/core/retrieval_assembler.py`, `virtual_context/core/assembler.py`, `virtual_context/core/summary_identity.py`.

- Immediate return: assembled prepend text, tags, budget metadata and recent-history view to the calling driver; convenience transform returns text.
- Later read-back: summaries, facts, working-set pages and optionally recent canonical rows reach a subsequent answer invocation; static core files are context supply, not trace-fed memory by themselves.
- Delegated visibility: selected surviving text only; other stored sources are reachable via separate paging/search routes, not present by reference in the model window.
- Selection predicate: current message/reply query, bounded recent context, active tags, utilization and post-compaction state; fact servability/audience checks precede curation; rendered costs constrain admission.
- Invalidation or expiry: changing candidates/question invalidates curation memo key; current audience is reapplied; history filtering removes old nonmatching pairs but preserves recent pairs, unknown tag data and rule-tagged pairs.
- Activation or effect: code changes model-visible context; downstream compliance and answer improvement are unobserved.
- Evidence limits: retriever ranking and fact-curator internals not exhaustively traced; protected DB merge is gated; no universal context inclusion or audience guarantee established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Automatic selector trigger is inbound work, not a scheduler. Budget is `context_window` with an optional invocation cap and per-part configuration. Core context is priority-sorted file content; actor cards, hints, tag text, facts and recent history compete for bounded space. Assembler enforcement uses rendered cost, rather than assuming the stored summary estimate equals the transmitted cost. SRC-1 `virtual_context/core/assembler.py`:

> token_budget = max(0, int(token_budget))
> injection_budget = token_budget
> if max_context_tokens is not None:
>     injection_budget = min(injection_budget, max(0, int(max_context_tokens)))
> core_budget = min(self.config.core_context_max_tokens, injection_budget)
> --- `virtual_context/core/assembler.py`

Curation proposes selection, not content replacement; code can omit material due to audience, trust or budget. User initiating retrieval is not per-fact approval. No expected-answer oracle; operating mode is open incoming requests. DB recent-window recovery introduces canonical rows only under its merge/participant logic. This is accumulated-context filtering and reload, not an isolated agent frame. Like eviction, it keeps less in the window; unlike a heap pointer, a source ref is inert until a tool performs read-back.

#### MEM-RTE-fact-admission
Label: Fact policy and retained refusal read-back

Endpoints/progression: extracted/new fact → eligible source-bound candidate snapshots → model comparison proposal → deterministic policy/transaction revalidation → supersession/link/decision ledger; admin verdict → saved verdict/key → trust refresh and future extraction gate. Owners: comparison proposes; policy/store admits or vetoes; explicit caller may reject/restore a fact. It refines [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance) and [RT-RTE-record-edits](runtime.md#rt-rte-record-edits) across both routes, not either whole referent. SRC-1 `virtual_context/ingest/supersession.py`, `virtual_context/storage/fact_mutations.py`, `virtual_context/storage/record_edits.py`, `docs/fact-lifecycle.md`.

- Immediate return: comparison/admission outcomes or verdict report and trust-state counts.
- Later read-back: refusal versions suppress unchanged comparison proposals; rejected statement/source keys block re-extraction; restored saved content can become servable again; admitted facts reach retrieval/actor-card consumers.
- Delegated visibility: comparison receives pre-admitted candidate snapshots; admin review can expose fact and source turns; neither sees an expected answer to every future user question.
- Selection predicate: matching owner/subject/author/role/audience/chronology policy; refusal equality over policy, fact and source versions; verdict identity includes normalized statement and source turns.
- Invalidation or expiry: changed fact/source/policy reopens refused comparisons; stale-proposal refusals are not merit judgments; restore lifts a verdict; conversation deletion bounds ledger retention.
- Activation or effect: admission and later eligibility change in code; eventual answer behavior and improved capacity remain unobserved.
- Evidence limits: full model-comparison and transaction/backends not exhaustively audited; an admin actor string does not prove human identity; source proof does not establish external truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger is incoming extracted fact, repeated comparison or explicit administrative verdict. The model proposes a relation, not arbitrary ownership/chronology changes. Software can veto before and after model processing. Human contribution is explicit content/verdict for a human admin, unresolved for a generic API caller; no per-fact human approval on automatic extraction. Guidance is source evidence and lifecycle policy, not a benchmark correct-answer oracle. Operating modes are open conversation maintenance and explicit administration. Recovery is changed evidence, rebuild or restore, not proof of atomic reversal of every downstream view.

> return any(
>     entry["policy_version"] == POLICY_VERSION
>     and entry["source_versions"] == versions["expected_source_versions"]
>     and entry["fact_versions"].get(old_id) == versions["expected_old_version"]
>     and entry["fact_versions"].get(new_id) == versions["expected_new_version"]
>     for entry in refused.get(old_id, ())
> )
> --- `virtual_context/ingest/supersession.py`

#### MEM-RTE-card-refresh
Label: Actor card refresh and requester consumption

Endpoints/progression: enabled/due or forced rebuild → actor facts/turn sources/carryovers → curation → separate semantic admission → calibrated/capped entries → epoch/build-marker-checked replacement → requester card read and token-capped rendering. Owner: service code coordinates model proposals and store acceptance. SRC-1 `virtual_context/core/community/actor_card_rebuild.py`, `virtual_context/core/assembler.py`, `virtual_context/types.py`. Closest supplied route is [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance); this optional actor-scoped cache refresh is a distinct maintenance/consumer path, not a redeclaration of generic compaction.

- Immediate return: count of written card entries or failure/superseded outcome; assembly separately returns rendered card text or empty text.
- Later read-back: later requester invocations can receive surviving card bodies; subsequent rebuilds reconsider carryovers and current evidence.
- Delegated visibility: curation receives bounded actor evidence and carryovers; answer model receives a bounded subset of entries, not the full evidence corpus or every rejection reason.
- Selection predicate: gate, tenant/actor/request audience, valid/scoped/non-superseded store result, entry confidence and token cap; rebuild input and carryover evidence limits apply separately.
- Invalidation or expiry: source mutations dirty profiles; stale build markers/epochs can decline replacement; supersession and validity/expiry fields exist; additive refresh may leave last known-good entries visible.
- Activation or effect: derived preferences are wired to later assembly when enabled; actual personalization and privacy outcomes are unobserved.
- Evidence limits: separate admission/store predicates not fully audited; caller configuration determines activation; no complete cross-context safety claim or independent measurement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is not authorship. Actor-authored evidence informs model-written proposals; a separate model and code checks can veto. Input initiation or enabling the feature is not per-entry human approval. Guidance asks durable, source-grounded entries; source evidence is a reference, not an expected-answer oracle. Replacement is bounded by build-marker/epoch checks and can legitimately clear the cache to empty when no durable entries remain. Failed/stale writes can retain the old card and trigger later refresh. Operating mode is optional background/administrative refresh and foreground requester use.

> # Drop whole lowest-confidence entries. Never truncate mid-entry:
> # half a preference is worse than none of it.
> entries.remove(min(entries, key=self._card_sort_key))
> --- `virtual_context/core/assembler.py`

#### MEM-RTE-payload-restore
Label: Proxy archived payload restoration

Endpoints/progression: proxy reduction stores raw output/chain/media and leaves stub → foreground model requests restore → request-bound runtime loads ref → validates/sanitizes → modifies current payload or returns media → continuation model call. Model selects ref; proxy code owns mutation. This is a material restoration branch of [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop) also used within [RT-RTE-proxy-request](runtime.md#rt-rte-proxy-request); it is not their entire referent. SRC-1 `virtual_context/proxy/message_filter.py`, `virtual_context/proxy/handlers.py`.

- Immediate return: restoration acknowledgement/error or media blocks; ordinary tool/chain restoration can put full content in request history instead of returning the full text as the tool result.
- Later read-back: archived content removed from earlier payload windows reaches the continuation; chain restoration removes ineligible VC-derived messages before delivery.
- Delegated visibility: selected archived content whose ref resolves and whose current stub/runtime permits restoration; model does not receive store-wide capability or unrestricted file access.
- Selection predicate: model-supplied ref, ref prefix, bound conversation, mutable request body and matching stub; chains must decode to a list of message dicts and have restorable source messages after sanitization.
- Invalidation or expiry: missing row/file/stub or unavailable mutable payload refuses restoration; storage retention/TTL and all media transformations remain uninspected.
- Activation or effect: code replaces stubs or returns media to provider continuation; request to use recovered evidence is not observed compliance.
- Evidence limits: no live restore trace; surrounding payload-size and provider-format branches not exhaustively audited; ref naming alone does not establish author/audience safety.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission checks choose recoverable source material rather than approving new product knowledge. Foreground model proposes selection; software can reject malformed/missing content. No human per-restore decision or answer oracle is established. Operating mode is open provider continuation. Removal is preferentially tool/message chains and media; reachable remainder is a stub/summary plus archive. This resembles eviction/reload, not a popped sub-agent frame or a model-dereferenceable pointer.

> sanitized_chain = sanitize_chain_snapshot_messages(chain)
> if not sanitized_chain:
>     return {"error": f"chain snapshot ref {ref} has no restorable source messages"}
> --- `virtual_context/proxy/handlers.py`

#### MEM-RTE-evaluator-reuse
Label: Evaluator ingestion checkpoint and reader reuse

Endpoints/progression: dataset history → engine ingestion/manual compaction → persistent store/checkpoint/cache manifest → current or later cache-hit engine → question assembly → reader with tools. Owner: evaluator runner code. SRC-1 `benchmarks/longmemeval/vc_runner.py`; other runner cache paths were searched, not fully traced. Distinct caller mode from [RT-RTE-headless-chat](runtime.md#rt-rte-headless-chat); it uses [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop) rather than redeclaring its executor.

- Immediate return: evaluator response/result records and diagnostic payload/cost files.
- Later read-back: cached ingested sources and derivatives serve later reader questions/runs; cost snapshots restore accounting, not answer content.
- Delegated visibility: reader receives assembled question/evidence and tool results; whether all oracle data is excluded from all provider payloads remains uninspected.
- Selection predicate: dataset/question identity and cache policy, ingestion/compaction state, then ordinary engine selection and reader tool choices.
- Invalidation or expiry: fresh/cache-clear and recompact paths exist in runner searches; LongMemEval rejects failed checkpoint saving; cache hit alone is not semantic validation.
- Activation or effect: cache reuse and reader invocation are wired; accuracy, realized benefit and causal component contribution are unobserved.
- Evidence limits: external datasets, scoring/results and oracle isolation not fully inspected; JEV/AMB/context-contract methods remain included uninspected parts.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Dataset history is selected by the evaluator, not approved statement by statement by a human. Model maintenance and engine policy admit derived content. This is bounded evaluation, not an autonomous curriculum or deployment-time learning claim. `gold_answer` occurs in runner diagnostics; its provider/use in judging and possible payload exposure require separate tracing before an answer-oracle claim. No successful benchmark or expected-answer-independent capacity increase follows from persistence.

> if engine._save_state(messages) is not True:
>     engine.close()
>     raise RuntimeError("Benchmark cache checkpoint failed; rerun with --fresh")
> --- `benchmarks/longmemeval/vc_runner.py:824-826`

### Claims

#### MEM-CLM-renderer-proof
Label: Summary rendering proof is narrower than its name

Claimed operation assessed: “proved” rendering and canonical-transcript wording in assembler helper contracts might suggest the visible summary is reconstructed/verified against exact sources. Actual inspected summary rendering selects stored text and performs audience admission. `is_proved_summary_rendering` only checks nonempty string and not quarantine. Missing individual source rows are skipped, and unsourced items can pass. Thus this path establishes neither complete source mapping nor factual fidelity. SRC-1 `virtual_context/core/assembler.py`, `virtual_context/core/summary_identity.py`. This qualifies source labels, not a contradiction of [RT-BAP-assembled-context](runtime.md#rt-bap-assembled-context)'s interpreted-text authority.

> def is_proved_summary_rendering(text: object) -> bool:
>     """Whether *text* is a summary the renderer admitted."""
>     return isinstance(text, str) and bool(text.strip()) and text != SUMMARY_ATTRIBUTION_QUARANTINE
> --- `virtual_context/core/summary_identity.py`

> row = rows.get((conversation_id, source_id))
> if row is None:
>     continue
> --- `virtual_context/core/summary_identity.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-fact-refusals
Label: Retained decisions to later fact admission

Consumer: supersession candidate selector and rejected-fact write filter. Channel: retained ledger keys, policy/source/fact versions and verdict state. Force: software excludes unchanged refused proposals or rejected re-extractions, rather than asking the answer model to respect a prose criticism. Horizon: subsequent extraction/comparison while the relevant conversation and versions persist. SRC-1 `virtual_context/ingest/supersession.py`, `virtual_context/storage/record_edits.py`. Distinct from [RT-BAP-engine-watermarks](runtime.md#rt-bap-engine-watermarks)'s history eligibility and [RT-BAP-assembled-context](runtime.md#rt-bap-assembled-context)'s interpreted guidance; supporting passages are in [MEM-RTE-fact-admission](#mem-rte-fact-admission) and [MEM-OBJ-fact-ledgers](#mem-obj-fact-ledgers).

## Annotations

#### On [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state)

Memory-specific finding: symbolic snapshot fields carry paging depth, fingerprints, tag entries and watermarks into later selection; they are not the full source archive. The type also contains telemetry rollup/request captures, which serve diagnostic consumers unless another update route is traced. Store snapshot, optional Redis/cache history and provider-owned saving are alternative checkpoint ownership/forms; the supplied record retains their evidence and limits. Canonical-row restoration is a further recovery route supplied by the boundary/runtime, not proof that every old model-visible payload is recovered exactly. SRC-1 `virtual_context/types.py`, `virtual_context/engine.py`.

> working_set: list[WorkingSetEntry] = field(default_factory=list)  # paging depth state
> trailing_fingerprint: str = ""  # hash of last N user messages for session matching on restart
> telemetry_rollup: dict = field(default_factory=dict)  # persisted telemetry totals (survives restart)
> request_captures: list[dict] = field(default_factory=list)  # lightweight request summaries for dashboard
> --- `virtual_context/types.py`

#### On [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance)

Raw-to-derived chain: canonical physical source rows → optional merged/stub segment → summarizer and fact extractor → stored summary/full text/messages, facts and search vectors → later inbound assembly/paging. New segment storage and fact replacement are separate writes; recovery mode can skip replacement, supersession and link passes. The pipeline refreshes source trust after admitted fact insertion and embeds inserted facts. Dense vectors are derived retrieval state, not parameter training. Their initial model-version/provenance remains bounded by [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider).

Authorship/admission: models propose text and facts; code parses, judges, retries or falls back, and persists. Ordinary availability-oriented compaction can preserve bounded source text after generation failure; strict regeneration can fail closed. A fallback may have empty extracted facts. Reasons are requested in summaries and optional fact `why`; verbatim source retention supplies a reload alternative, not guaranteed delivery of every rationale. SRC-1 `virtual_context/core/compactor.py`, `virtual_context/core/compaction_pipeline.py`.

> Preserve polarity, negation, intent, and causal rationale exactly. Never turn "does not want",
> "wants to remain infertile", "did not happen", or similar negative statements into their
> positive opposites. If the segment is only a greeting, acknowledgement, or short reply, summarize
> only that content; do not infer or import the topic, recommendation, or outcome from nearby context.
> --- `virtual_context/core/compactor.py`

That is requested behavior, not a fidelity invariant. The inspected fallback countercase:

> if fail_closed:
>     raise
> logger.warning(f"LLM summarization failed for segment {segment.id}: {e}")
> parsed = {
>     "summary": conversation_text[:target_tokens * 4],
>     "entities": [],
>     "key_decisions": [],
>     "action_items": [],
>     "date_references": [],
>     "refined_tags": segment.tags,
> }
> --- `virtual_context/core/compactor.py`

#### On [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop)

Memory selection: model-selected expand/collapse updates topic depth; cost uses freshly rendered memory and revalidates existing pages. Auto-eviction orders by least-recent access, collapses to summary when it saves tokens, otherwise removes the page. Store sources remain reachable even when a working-set entry disappears. Failed expansion can return insufficient budget rather than forcing over-budget inclusion. Persistence of working-set metadata follows the supplied checkpoint owner; reassembly delivery and tool limits remain in the supplied loop. SRC-1 `virtual_context/core/paging_manager.py`.

> # Collapse to SUMMARY (not NONE) to keep minimum context
> memory = self.render_memory(tag, DepthLevel.SUMMARY, speaker_context=speaker_context)
> summary_tokens = memory.measured_cost if memory is not None else 0
> delta = ws.tokens - summary_tokens
> if delta <= 0 or memory is None:
>     # Already at summary or less, remove entirely
>     freed += ws.tokens
>     del target[tag]
>     memories.pop(tag, None)
> --- `virtual_context/core/paging_manager.py`

#### On [RT-RTE-record-edits](runtime.md#rt-rte-record-edits)

Memory-specific curation: canonical edits and topic forgetting can immediately change the tag index, then queue derived segment rebuilds. `process` retags specified turns, rebuilds each unfinished segment, refreshes topic summaries and shared retrieval snapshots; caught segment failures remain in operation status for retry. Fact retraction/rejection is a distinct withholding mechanism; fact-verdict restoration can recover saved content. A failed rebuild does not warrant a claim that every model consumer is synchronized. SRC-1 `virtual_context/core/record_editing.py`, `virtual_context/storage/record_edits.py`, `docs/fact-lifecycle.md`.

> Rebuilt facts start `unverified` and are set to `verified` or `unverified` from
> their source proof once stored. A record edit retracts the facts of every segment
> it queues for rebuild in the same transaction as the edit, and the rebuild
> replaces them. Retracted and rejected facts are withheld from `vc_query_facts` and its linked
> facts, the facts attached to `vc_find_quote`, `vc_remember_when`, the facts
> injected before a model call, and supersession candidates. If a rebuild fails,
> the facts stay retracted and withheld.
> --- `docs/fact-lifecycle.md`

The full multi-tool withholding statement is design evidence; direct inspection here verifies inbound filtering and comparison exclusion, not every named tool branch.

#### On [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage)

Retained history has software admission authority over later repetition/day selection. It is not just a raw delivery log: an ambiguous-send claim can keep the day unavailable even without a successful receipt. Candidate/source text informs model qualification/drafting; ledger fields constrain later outward action. Source fidelity rejection and recorded reasons are not an expected-answer oracle or evidence that memory improves answers. Storage substrate and detailed history/candidate transformations remain uninspected here; supplied runtime passages support the retained claim-before-send and later repetition consumer. SRC-1 `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/poster.py`.

## Write side

Acquisition and authorship differ from admission. Live clients supply conversation text; driver/model output is retained through completed-turn tagging. Import callers choose a file/adapter/conversation, while normalization and ingestion admit each resulting record. Neither caller initiation nor a configuration flag establishes human approval of each statement. Canonical provenance authenticity at initialization remains host-dependent; known subsequent compaction and source-bound transformation are not suppressed by that unknown. Supplied acquisition routes are [RT-RTE-headless-chat](runtime.md#rt-rte-headless-chat), [RT-RTE-proxy-request](runtime.md#rt-rte-proxy-request) and [RT-RTE-import-history](runtime.md#rt-rte-import-history).

Trace-fed update is concrete in maintenance: raw human/assistant history yields tags, summaries, facts, vectors and optional cards that later alter context. This is more than retaining raw logs, but it establishes no measured learning or weight modification. Compaction source IDs, merge/stub alternatives, fallbacks and recovery replacement gates are retained in the maintenance annotation and [MEM-OBJ-stored-segment](#mem-obj-stored-segment). Summary rejection mostly changes generation/retry/fallback; it is not automatically a durable prohibition on the rejected content. Durable fact verdicts and versioned policy refusals do have later update consumers: [MEM-RTE-fact-admission](#mem-rte-fact-admission).

Editing changes canonical text under host authority and rebuilds derivatives separately. Saved reasons can explain a verdict to a human, while software consumes its key/outcome. Optional card refresh has separate proposal, semantic admission and replacement checks; later card adoption is separately gated. Proxy reduction archives raw content and emits display stubs, not an authored durable strategy. Evaluators produce reusable engine caches; diagnostic payload/cost artifacts are not themselves a demonstrated feedback loop. Dated repair scripts are an additional explicitly selected replacement path whose unavailable inputs and uninspected bodies prevent an applied-repair claim.

## Read-back

Two main directions coexist: request-triggered automatic supply to assembly and explicit model/host tool requests. Inbound assembly selects from retained material without requiring the foreground model to call a tool first; the selector is still triggered by an incoming request. Paging/restore selects by model arguments and code permission/cost rules. CLI/MCP recall and OpenClaw transform return text to a host role; supplied wiring affords later consumption, not evidence the host actually includes or follows it. Core files are static instruction/context supply unless edited and subsequently consumed; no traced use-fed update to those files is established.

At the consumer boundary, stored summary/full text is not necessarily the whole produced segment; facts pass trust/audience/curation/budget gates; cards lose whole low-confidence entries; chain restoration sanitizes stored messages; provider continuation may see acknowledgement plus changed history rather than a full textual tool return. Those transformations bound claims of completeness. Software admission consumers differ from answer models: ledger state can directly prevent writes, while injected memory is interpreted text. [RT-BAP-engine-watermarks](runtime.md#rt-bap-engine-watermarks) and [MEM-BAP-fact-refusals](#mem-bap-fact-refusals) establish rule-governed effects; [RT-BAP-assembled-context](runtime.md#rt-bap-assembled-context) establishes a delivery channel, not activation.

Working-context control in inspected routes is reduction/reload of an accumulated conversation: protected tails, tag relevance, summarized old content, token caps, cold-page collapse and archived tool/media stubs. No inspected route here establishes a separate sub-agent context whose whole frame is discarded and whose only return crosses back. This is a scope limitation, not a repository-wide evidenced absence. A memory reference in text is not an automatically live pointer; a successful reload operation must materialize content into the next provider request.

## Integration issues

- Supported refinement, not a contradiction of runtime: [MEM-CLM-renderer-proof](#mem-clm-renderer-proof) limits any inference from “proved”/canonical-transcript labels to truth or complete attribution. Its concrete missing-row countercase matters to [MEM-RTE-inbound-context](#mem-rte-inbound-context) and [MEM-OBJ-stored-segment](#mem-obj-stored-segment). Do not upgrade the supplied interpreted-context authority path to a fidelity guarantee.
- No supplied generic fact was found false. Maintenance admission remains valid but should integrate the ordinary fallback versus strict regeneration distinction, separate fact/refusal gates and optional card branch. See annotations on [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance), [MEM-RTE-fact-admission](#mem-rte-fact-admission) and [MEM-RTE-card-refresh](#mem-rte-card-refresh).
- Potential record overlap: [MEM-RTE-inbound-context](#mem-rte-inbound-context) spans the selector inside headless/proxy/MCP rather than their entire driver routes; [MEM-RTE-payload-restore](#mem-rte-payload-restore) is a material branch within paging/proxy; [MEM-RTE-fact-admission](#mem-rte-fact-admission) spans maintenance and admin verdicts; [MEM-RTE-card-refresh](#mem-rte-card-refresh) adds an optional actor-scoped derivative; [MEM-RTE-evaluator-reuse](#mem-rte-evaluator-reuse) adds the evaluator caller/cache mode. No whole-referent duplicate is intended. Objects describe material outputs or source parts, not replacement IDs for supplied routes/checkpoint.
- Unresolved initial provenance: imported/caller metadata authenticity and adapter fidelity affect [MEM-OBJ-source-content](#mem-obj-source-content) and [MEM-OBJ-source-metadata](#mem-obj-source-metadata). Subsequent source checks do not independently authenticate the original transcript.
- Unresolved consumer consistency: all cached summaries, cards, tool results and provider contexts during unfinished edit rebuilds were not traced. The record-edit annotation and [MEM-RTE-fact-admission](#mem-rte-fact-admission) establish local withholding/retry, not atomic withdrawal from every past or concurrent consumer.
- Unresolved backend/checkpoint equivalence: store/Redis/provider ownership, TTLs, crash recovery and all mutation guards remain bounded by [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state) and [RT-CLM-compaction-fence](runtime.md#rt-clm-compaction-fence). No universal durability, concurrency or tenant-isolation guarantee follows.
- Unresolved optional card semantic/privacy details: curation/admission parser bodies and store disclosure transactions were not fully read. [MEM-RTE-card-refresh](#mem-rte-card-refresh) supports a gated wired route, not operational safety or reliable preference inference.
- Unresolved alternative operations: full MCP resource/search/date/quote paths, admin migrations/backfills, repair application bodies, engagement history details and JEV/AMB/context contracts remain explicitly inventoried. Their missing facts prevent a system-wide admission/read-back invariant, verified repair or comprehensive evaluator/oracle claim. They do not negate the positive paths established above.
- No improvement inference: persisted caches and source-native tests/reports cannot establish observed activation, reliable answers or causal benefit. [MEM-RTE-evaluator-reuse](#mem-rte-evaluator-reuse) leaves oracle use/exposure and scoring unresolved rather than treating model judgment as a correct-answer oracle.

## Limitations and checks

The source identity and full revision match the supplied boundary; no new source, model call, test execution or external capture was introduced. Supplied runtime is distinguished from direct implementation reads throughout the inventory. The frozen method consists of the supplied memory job, member types, collection, worker rules and records contract; no prior target characterization or other run was read.

Static evidence establishes wired storage/transformation/consumer paths only. It prevents conclusions about observed use, answer improvement, all-backend equivalence, live authorization and supplied repair faithfulness. Available but uninspected branches are named beside their prevented conclusions; they are not access gaps or evidenced absences. The validator result below checks structure, record links, identity and quotation occurrence, not semantic acceptance.

Validation: the first validate-output check found one ambiguous repeated checkpoint quotation. Its attribution now uses the validator-supplied range for the inspected occurrence. The final validate-output check passed.
