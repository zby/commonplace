---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Eidetic runtime baseline: lifecycle extraction and injection, recall, admission gates, logical-index worker and product updates."
run-id: AAS-2026-10-14-eidetic-0e54f3c114b3-01
reviewed-boundary: "67506b62fdd0944c243537c3cb10938f7343b6b2"
---

# Eidetic runtime report

## Runtime account

Eidetic supplies a memory lifecycle and retrieval service to coding-agent hosts. It does not own the foreground agent's task loop. Its consequential work is to turn selected session content into durable cards, reload selected cards into subsequent sessions, and provide query-driven recall. The distinction between personal PUSH and attached-base PULL, frozen scope and external-host limits come from [boundary](boundary.md#boundary-and-evidence). Implementation findings below use SRC-1 at the reviewed commit. No target code, test, example or provider was executed; operation and benefit remain unobserved.

### Ordinary lifecycle invocation

The installer registers SessionStart injection and asynchronous Stop extraction. Claude Code supplies the lifecycle event, session ID, transcript path and current working directory. The injection script owns the sequence once invoked: acquire the shared memory lock; refresh the lexical index; attempt drift, optional code and vector maintenance; record a session hint; assemble context; append the hint; return a status message. The terminal useful artifact is `~/.claude/rules/memory-context.md`, not the hook's stdout. The host must load that file for the content to reach its agent. Locks coordinate participating hooks; a busy hook can skip, and failed refresh can leave a prior index or rules file. This is best-effort delivery, not a fresh-context transaction. SRC-1: `install.sh`, `hooks/smart-memory-inject.sh`; [RT-RTE-context-injection](#rt-rte-context-injection).

At Stop, the host transcript is reduced to a bounded text excerpt for a separate extraction invocation. A model proposes signal lines; code keeps contract-shaped lines, then compounding code selects an eligible existing card or creates a project signal card. The signal hook refreshes the index under its lock before compounding, but ignores refresh failure. A successful card write persists beyond the extraction subprocess and can reach a later injection or recall. This loop has distinct identities: host session, transcript file, CWD-derived project memory directory, card path and index row. The extractor is not a delegated foreground worker: it returns parsed proposal text, not task execution authority. SRC-1: `hooks/session-signals.sh`, `bin/compound.py`; [RT-RTE-signal-compound](#rt-rte-signal-compound).

Recall is a second ordinary entry, selected by the foreground agent or MCP client rather than independently pushed. The forked recall skill requests a separate general-purpose context and shells to search; MCP calls subprocess search and detail handlers. Search code owns lexical/vector selection and confidence annotation; the consuming agent owns whether to inspect and act. This is a useful context-control boundary: the recall frame can keep intermediate search work out of the caller's window, with only its return escaping, but the host owns actual frame isolation. MCP returns result data directly. Neither path trims the foreground conversation. SRC-1: `skill/SKILL.md`, `mcp_server.py`, `bin/search_impl.py`; [RT-RTE-memory-recall](#rt-rte-memory-recall).

### Material alternate and forcing routes

Four forcing cases bound the runtime claims:

1. **Unavailable semantic retrieval.** The engine can return no vector hits when model/runtime or stamps are unsuitable. Personal recall can still use lexical results; the logical-index worker instead returns a degraded vector response. An empty vector response does not certify absent knowledge. [RT-RTE-memory-recall](#rt-rte-memory-recall), [RT-RTE-engine-worker](#rt-rte-engine-worker).
2. **Protected existing card and direct writer.** Compounding skips existing `feedback` and `user` cards. `remember.py` also refuses append into those types, but can create a new `feedback` card through its kind/type arguments. Direct shell edits remain outside these guards. Protection is mutation-path-specific, not a store-wide authority barrier. [RT-RTE-signal-compound](#rt-rte-signal-compound), [RT-RTE-explicit-admission](#rt-rte-explicit-admission).
3. **M3 driver enabled but judge unavailable.** Driver activation is not filing activation. Filing requires both confidence-events and autofile switches; inability to register an LLM judge leaves the deterministic overlap scorer available. Consequently, “all auto-filed answers are independently LLM-judged” is false even within M3. [RT-RTE-m3-filing](#rt-rte-m3-filing).
4. **Base write without user approval evidence.** MCP advertises an explicit-user-only add policy, but the handler checks text and dispatches to `base.py`, which writes without receiving an approval token. The policy depends on host/agent compliance. Base scan realpath containment is a different code invariant, not a write approval gate. [RT-RTE-explicit-admission](#rt-rte-explicit-admission), [RT-CLM-base-isolation](#rt-clm-base-isolation).

The inspected admission paths also include M1/M2 maintenance and caller-driven product updates. Maintenance processes pending ingests and gates distinct transformations; updates replace runtime scripts from upstream HEAD. Neither should be confused with model-parameter training. See [RT-RTE-semantic-maintenance](#rt-rte-semantic-maintenance) and [RT-RTE-product-update](#rt-rte-product-update). Memory-specific revision semantics belong to the memory analyst; this baseline establishes callers, owners and effect boundaries.

### Controls, authority and evidence limits

The capability surface includes subprocess execution, local card writes, indexing, MCP tools, extension callbacks for scoring/synthesis and an index sync protocol. The current grant set is configuration-dependent: registered hooks, attached bases, environment switches, installed CLIs and provider credentials. This analysis has no deployed settings or isolation evidence. Only the plain Codex extraction invocation explicitly requests a read-only sandbox; the shell caller that subsequently writes cards is not confined by that flag. The Claude route replaces the system prompt but does not add a comparable sandbox in its inspected command. Private wrappers, the local gateway, SDK and host permission enforcement are external contracts. SRC-1: `hooks/session-signals.sh`, `bin/m3_judge.py`, `bin/m3_recall_miner.py`.

The load-bearing guarantees are scoped separately: feedback name visibility during assembly, base file-scan containment, M3 support-before-filing, and per-file atomic replacement during updates. Their owners and counterpaths are recorded below. Delivery of an `ALWAYS APPLY` heading is natural-language behavioral authority, not proof of compliance. Search confidence is a ranking/annotation decision, not an expected-answer oracle. The smoke evaluator has explicit expected substrings and confidence thresholds, but its results were not supplied and it is not a runtime admission gate. SRC-1: `bin/recall_smoke.py`; [RT-CLM-feedback-visibility](#rt-clm-feedback-visibility), [RT-BAP-memory-rules](#rt-bap-memory-rules).

Added inspection beyond the boundary's initial coverage includes base realpath collection; M3 support, judge registration and local-only miner routing; M1/M2 selection and activation; engine-worker sync/search; query-translation model identity; lifecycle test correlation; update notice/install/recovery; and smoke evaluator decision logic. These are implementation or doctrine/design evidence from SRC-1, not new sources or observed operation. Export, cleanup, confidence algebra, replay and evaluator-internal details not traced here remain available, not absent. No complete security audit, deployment-activation inference, model-quality estimate or successful self-improvement attribution is made.

## Shared records

### Components

#### RT-CMP-session-extractor
Label: Session signal extraction model routes

Source-native identity: the extraction functions in SRC-1 `hooks/session-signals.sh`. Distributed-parametric provider/local models interpret a natural-language safety/system prompt and excerpt; weights reside in external CLI/service runtimes, not the card store. Claude is attempted first unless skipped, followed by configured local and Antigravity alternatives and Codex fallback. Default configured labels include `claude-sonnet-4-6`, `gpt-5.5` and Codex fallback `gpt-5.4-mini`; plain Codex normally uses its own configured model unless overridden. Parameters changing during operation: provider internals uninspected; no training request appears in these call sites. Exact version pinned: model labels/configuration, not immutable weight revisions. Mutable endpoint can resolve another model: yes, through configuration, CLI defaults and explicit route fallback. These facts do not establish provider-side parameter stability.

> SIGNAL_CODEX_MODEL="${EIDETIC_SIGNAL_CODEX_MODEL:-gpt-5.5}"
> --- `hooks/session-signals.sh`

#### RT-CMP-embed
Label: Embedding profiles

Source-native identity: `PROFILES` and `get_model` in SRC-1 `bin/embed.py`, consumed through `bin/engine.py`. Distributed-parametric embedding models create dense vectors stored as SQLite blobs. Default multilingual profile uses `intfloat/multilingual-e5-large` with 1024 dimensions; fast profile uses `BAAI/bge-small-en-v1.5` with 384. Parameters change during operation: inspected path loads and infers, not trains; external package/model internals uninspected. Exact version pinned: no immutable weight revision in the inspected profile/loading code. Mutable endpoint can resolve another model: environment/configuration changes profile; package cache resolution is external. Model/dimension/hash/runtime stamps detect specified compatibility changes, not every possible weight change.

> "model": "intfloat/multilingual-e5-large", "dim": 1024,
> --- `bin/embed.py`

#### RT-CMP-rerank
Label: Cross-encoder relevance model

Source-native identity: `MODEL_NAME` and `get_model` in SRC-1 `bin/rerank.py`. Distributed-parametric `TextCrossEncoder` weights are cached locally; scores are ephemeral numerical outputs. Used for ambiguous recall corroboration and M2 relevance, with different failure consequences. Parameters change during operation: no training request at the inspected loader/scoring call sites. Exact version pinned: named model, not immutable weights. Mutable endpoint can resolve another model: the fixed name resolves through external package/cache infrastructure; no code-level alternate name was found in this loader. Model internals and actual loaded artifact uninspected.

> MODEL_NAME = "jinaai/jina-reranker-v2-base-multilingual"
> --- `bin/rerank.py`

#### RT-CMP-shimnachi-local
Label: Local mining and default entailment endpoint

Source-native identity: `shimnachi/local`, used by SRC-1 `bin/m3_recall_miner.py` and `bin/m3_judge.py`. Distributed-parametric weights are external; prompts, returned JSON and routing metadata are local text/symbolic material. The miner requests this exact route with same-family failover disabled. The default judge uses a configured local HTTP gateway and a named prompt version; nonlocal judge providers/models are configurable alternatives. Parameters change during operation: uninspected at gateway/provider, no training request in these call sites. Exact version pinned: no weight revision; local is a routing identity, not an immutable model version. Mutable endpoint can resolve another model: possible through gateway or configuration; actual deployment resolution uninspected.

> res = sdk.chat_for_route(provider="shimnachi", model="local",
>                                  task="memory_mining", volume="bounded",
>                                  allow_same_family_failover=False,
> --- `bin/m3_recall_miner.py`

#### RT-CMP-query-translation
Label: Optional translation model alternatives

Source-native identity: backend selection in SRC-1 `bin/translate.py`. This is an alternative-component inventory, not a claim that the backends are equivalent or active. Distributed-parametric alternatives are Apple on-device NMT, Opus-MT/CTranslate2 and Codex CLI inference; storage is installed OS language packs, local model cache or external CLI/provider. Parameters changing during operation: no training request in the inspected adapter; backend internals uninspected. Exact version pinned: Opus-MT defaults to model `gaudi/opus-mt-ru-en-ctranslate2` at revision `d5c98dcc59a677e768e00ab6e29fbdea80a53729`, overridable by environment; Apple and CLI weights are not pinned here. Mutable endpoint can resolve another model: configured backend and CLI/gateway defaults can change; the default Opus revision is fixed unless overridden. Default backend is off, so all are optional routes, not deployed facts.

> OPUSMT_REVISION = os.environ.get("EIDETIC_OPUSMT_REVISION",
>                                  "d5c98dcc59a677e768e00ab6e29fbdea80a53729")
> --- `bin/translate.py`

### Operative objects

#### RT-OBJ-memory-context
Label: Generated memory context rules file

Source-native identity: `RULES_FILE` in SRC-1 `hooks/smart-memory-inject.sh`, written by `bin/assemble_context.py`. Natural-language rules, snippets, names, paths and session hints on a local Markdown file substrate. Assembly ordering and selection are symbolic Python/SQL rules; they are not themselves the content consumed by the host model. This object is the generated delivery artifact, distinct from source cards and derived vector indexes. Its later consumer is Claude Code's rules loader and foreground model, under an external loading/compliance contract.

> output.append("## Behavioral Rules (type=feedback) — ALWAYS APPLY\n\n")
> --- `bin/assemble_context.py`

### Routes

#### RT-RTE-context-injection
Label: SessionStart context injection

Endpoints/progression: Claude Code lifecycle event → lock-owning shell hook → index and maintenance attempts → assembly → rules file → host rules loader. Owner/next-step policy: hook code sequences executors; assembly's SQL and budget rules choose content. Principal/identities: current user process, CWD-derived project slug and exported host session ID. Effect boundary: local files/databases and returned status, not direct agent action. SRC-1: `hooks/smart-memory-inject.sh`, `bin/assemble_context.py`, `install.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook stdout reports update/fallback/busy or warnings; useful content is written to the rules file.
- Later read-back: selected retained cards and session hints enter a later host rules load; old generated content can survive failed assembly.
- Delegated visibility: local maintenance subprocesses see their selected DB/project inputs; foreground visibility depends on host loading the file.
- Selection predicate: all indexed feedback paths are represented at least by name or configured cluster; project slug, recency, weights and character budgets select other snippets; fresh handoff selection is an additional assembly path.
- Invalidation or expiry: reindex and subsequent assembly replace derived context; status/drift weights reduce prominence rather than universally deleting content; fallback copies at most 200 lines of CWD-matched MEMORY.md.
- Activation or effect: code writes/replaces a rules file and appends a hint; downstream behavioral activation is unobserved.
- Evidence limits: no installed rules loader or agent trace; busy lock, absent index, refresh failure and assembly failure are material alternates, so fresh/all-card delivery is not guaranteed.

Working-context control: independent lifecycle-triggered supply, not query-driven recall. Budgeting removes most card body text before delivery; the original cards remain reachable via recall/detail. Low-tier feedback may retain only its name. The window receives selected content by value; paths are reload cues, not live references. Recovery is next-hook retry or manual lock repair on the legacy lock path.

> python3 "$MEMORY_SYSTEM/bin/assemble_context.py" "$DB" "$RULES_FILE" "$(pwd)" || true
> --- `hooks/smart-memory-inject.sh`

#### RT-RTE-signal-compound
Label: Stop transcript extraction and compounding

Endpoints/progression: Stop payload → transcript tail → extractor proposal → line filter → locked index refresh → `compound.py` → existing-card History append or new signal file. Code owns routing, excerpt limits and write selection; model owns proposed signal content. Principal is the installed hook's user, not a per-write human approver. Existing-card candidate selection uses FTS and overlap/vector alternatives; protected type candidates are skipped, with near-duplicate warnings. SRC-1: `hooks/session-signals.sh`, `bin/compound.py`; model component [RT-CMP-session-extractor](#rt-cmp-session-extractor).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: asynchronous hook exits, usually silently; compounding summary/logs and optional session-scoped signal output are side channels.
- Later read-back: appended History or new project signal cards can be reindexed and later injected/recalled; busy-lock spool is retried by a subsequent nonempty signal invocation.
- Delegated visibility: extractor sees only parsed user/assistant text in a tail excerpt, not the full tool transcript; compounding sees filtered signal lines and local index candidates.
- Selection predicate: transcript exists and is at least 1000 bytes; at most 2 MB tail, last 20 text turns, each capped at 1500 characters; recognized prefixes then keyword/candidate rules decide writes.
- Invalidation or expiry: temporary prompt files are removed; spool draining caps retained files at 20 and drops oldest excess; durable card content has no expiry enforced by this route.
- Activation or effect: code appends History without updating last_verified, or creates a durable signal card; this changes later available content but no downstream action is observed.
- Evidence limits: formatting checks do not establish factuality, privacy or extraction completeness; refresh can fail before candidate selection; external wrapper/provider behavior is not frozen.

Admission: transcript facts are proposed under instructions to exclude hypotheticals, pasted sources and sensitive personal data. Model and code decide; a human can configure/disable the hook or edit cards but is not consulted on each signal. Operating mode is open session extraction under bounded input, not a curriculum. Answer oracle: none; output-prefix acceptance is not an expected-answer test. Rejection is EMPTY, malformed lines, excluded/failed candidates or provider failure. Recovery uses spooling, retries and atomic file replacement, not semantic rollback. The existing-type guard is an invariant of this write path only: manual writes and new-card creation do not inherit a store-wide rule-authority guarantee.

> if file_type in PROTECTED_TYPES:
>                         if dup_candidate is None:
>                             dup_candidate = path
>                         continue
> --- `bin/compound.py`

> if role in ('user','assistant') and content:
>             lines.append(f'{role}: {content[:1500]}')
> --- `hooks/session-signals.sh`

#### RT-RTE-memory-recall
Label: Requested recall and detail expansion

Endpoints/progression: foreground query → forked skill/search shell or MCP handler → lexical retrieval, optional vectors/translation and confidence annotation → snippets/structured results → optional detail read → caller judgment. MCP validates inputs and subprocess JSON/exit results; search code decides candidates; agent decides use. SRC-1: `skill/SKILL.md`, `mcp_server.py`, `bin/search_impl.py`, `bin/engine.py`. Model components: [RT-CMP-embed](#rt-cmp-embed), [RT-CMP-rerank](#rt-cmp-rerank), [RT-CMP-query-translation](#rt-cmp-query-translation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked snippets with paths, detail identifiers, confidence and no_confident_results; detail handler returns selected content or an error.
- Later read-back: query-selected retained card content; usage telemetry records surfaced results, but this return does not by itself write a revised knowledge card.
- Delegated visibility: forked recall skill is declared context: fork with agent: general-purpose; its host controls frame isolation and what crosses back; MCP subprocess sees DB/query and returns JSON rather than a delegated agent conversation.
- Selection predicate: query/type/limit, lexical strategies, weighted ranking, conditional vector fallback or non-ASCII forcing, path/heading/hash alignment and confidence corroboration; enabled translation adds a second query.
- Invalidation or expiry: vectors incompatible with model/runtime stamps or chunk content are excluded; lifecycle/drift/freshness metadata downrank retained content; underlying cards remain inspectable.
- Activation or effect: delivers candidate text and reload pointers; skill instructs weak-result inspection and checking both sides of contradictions; compliance is unobserved.
- Evidence limits: confidence is heuristic; no supplied result trace, private corpus or causal comparison; lexical and semantic failure paths differ, and translation correctness is not mechanically assured.

Working-context control is on-demand reintroduction of external/retained text, optionally via a separate host-owned skill frame. It neither removes old caller turns nor implements host compaction. Decision role is code ranking plus model/human use judgment. Operating mode is open queries. Answer oracle: no runtime expected answer. The separate `recall_smoke.py` evaluator compares results to case-authored expect_any substrings and minimum confidence, and negative cases to no_confident_results; its existence supplies test design, not test outcomes or a filing gate.

> if digest != vector_hash:
>             continue
> --- `bin/search_impl.py`

> If `no_confident_results` is
> true, treat rows as weak candidates to inspect, not as usable memory.
> --- `skill/SKILL.md`

#### RT-RTE-explicit-admission
Label: Direct personal promotion and topic-base addition

Endpoints/progression: caller supplies title/body/kind to `remember.py`, or base name/text/file to `base.py`; base MCP add delegates to the latter; local Markdown write then, for base addition, incremental index. Personal promotion resolves a project directory and appends to an eligible same-slug/explicit target or creates a card; base addition creates a collision-suffixed file under docs or notes. Owner: code handles persistence; caller supplies content and type choices. These are separate stores grouped only for the shared caller-supplied admission contrast. SRC-1: `bin/remember.py`, `bin/base.py`, `mcp_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: personal promotion returns path/action; base add reports added relative path and index exit; MCP maps subprocess failure to tool error.
- Later read-back: persisted personal cards reach injection/recall; base docs/notes reach attached-base recall after indexing.
- Delegated visibility: MCP base add passes text/title/as to the subprocess; no transcript or explicit approval evidence is supplied.
- Selection predicate: nonempty caller content; kind/type and body length choose card/directory; slug existence chooses append, collision handling or new file.
- Invalidation or expiry: personal updates append rather than erase previous body; base addition does not expire content; later reindex rebuilds derived state.
- Activation or effect: durable Markdown creation/update; caller-selected rule kind can create a new feedback card, making later rule delivery possible.
- Evidence limits: caller identity does not prove human authorship or approval; base write can persist even if subsequent indexing fails; direct shell file edits bypass these application guards.

Admission policy: MCP description says add only when the user explicitly asks; enforcement strength is policy, owned by the consuming agent/host. Handler and base CLI check data, not permission provenance. Personal promotion is an affordance for agent-extracted bodies with source/evidence/type arguments, not an automatic grounding check. Human veto is available by withholding tool/command invocation or host authorization, not by a built-in per-content approval dialog. Answer oracle: none. Operating mode: caller-supplied content. Guidance is body/title/kind plus tool instructions; the body and metadata persist. Personal atomic replacement protects file integrity, not correctness; base writes are followed by index and have no transactional rollback in this function.

> "description": f"Curate-write into the '{_P}' base — ONLY when the user explicitly asks to save "
>                         f"something to it. Writes a note (or a doc for long text) and reindexes. Never "
>                         f"call autonomously.",
> --- `mcp_server.py`

> with open(dest, "w", encoding="utf-8") as f:
>         f.write(fm + body.rstrip() + "\n")
> --- `bin/base.py`

#### RT-RTE-m3-filing
Label: M3 transcript mining and supported-answer filing

Endpoints/progression: enabled Stop background driver → local transcript miner → seen-cache filter → recall lane source retrieval → support/dedup gate → M2 handoff or personal card creation; acquisition lane instead emits dark outcomes. Driver derives project memory location from transcript parent slug and requires store/memory directory. Code routes lanes, model proposes candidates and optionally judges support. SRC-1: `bin/m3_hook.py`, `bin/m3_recall_miner.py`, `bin/m3_producer_driver.py`, `bin/m3_autofile.py`, `bin/m3_judge.py`, `bin/m3_acquisition.py`; [RT-CMP-shimnachi-local](#rt-cmp-shimnachi-local), [RT-CMP-embed](#rt-cmp-embed).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: driver prints JSON tally/meta; gate returns noop/rejected/deduped_to_m2/filed; Stop runs driver independently in background with log output.
- Later read-back: filed recall pages and M2-admitted changes can reach indexing/recall/injection; seen-cache affects later mining; acquisition/agent dark logs are not knowledge-card admission.
- Delegated visibility: miner sees a bounded text excerpt; producer retrieves source card spans for the recall query; judge sees claim/spans, with external-route redaction; independent agent lane additionally inspects eligible child transcripts when its own switch is on.
- Selection predicate: driver enabled, store present, parsed candidate kind, freshness in seen-cache; filing additionally requires events/autofile activation, nonempty sources, material claims passing support and no sufficiently close neighbor.
- Invalidation or expiry: definitively judged candidates enter session seen-cache; transient failures remain retryable; exact cache outcome policy is owned by the cache module, not inferred from a mere tally.
- Activation or effect: supported novel recall answer can become a personal card at cold-start confidence; near duplicate hands off to M2; dark acquisition computes/logs outcomes without filing a card.
- Evidence limits: flags and provider availability in an installed deployment unknown; source retrieval is not original-answer provenance; registered judge can be absent, leaving deterministic overlap support; successful grounding and downstream use unobserved.

Admission: miner proposes under source-native instructions to copy rather than generate; code rejects malformed/unsafe candidates, independently retrieved source spans supply support input, optional judge scores material claims, and code admits or vetoes. Operating mode is bounded session mining, not an expected-answer curriculum. Answer oracle: no expected correct answer; source spans constrain support judgment but can themselves be wrong. The gate owns a protocol guarantee: no sources or any below-floor material claim rejects before routing to M2 or filing. It is not a universal guarantee over `remember.py`, signal compounding or manual writes. `_active()` requires confidence-events and M3 autofile; driver and agent-lane flags are additional entry controls. Recovery is retry/seen-cache and dormant-mode no-op; no semantic correctness rollback is established.

> return _EV.events_enabled() and m3_enabled()
> --- `bin/m3_autofile.py`

> if sc is None or sc <= support_min():
>             _oplog(index_db_path, OP_REJECTED, title,
>                    extra=f"reason=unsupported_claim score={sc}")
>             return {"action": "rejected", "reason": "unsupported_claim",
>                     "claim": claim, "score": sc}
> --- `bin/m3_autofile.py`

> _log(f"DO_NOT_REGISTER SDK/route absent ({exc!r}) → M3 keeps deterministic overlap")
> --- `bin/m3_judge.py`

#### RT-RTE-semantic-maintenance
Label: Pending ingest M1/M2 maintenance

Endpoints/progression: incremental indexing/pending queue → bounded batch → M1 contradiction checks → only on no captured failure/deferral, M2 synthesis → queue/status commit and later reindex. Background maintenance hook takes its own lock, invokes incremental indexing and optional vector refresh. Owner: index/maintenance code; deployer controls activation and extension callbacks. SRC-1: `hooks/semantic-maintenance.sh`, `bin/index_impl.py`, `bin/m1_contradiction.py`, `bin/m2_synthesis.py`; [RT-CMP-embed](#rt-cmp-embed), [RT-CMP-rerank](#rt-cmp-rerank).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: diagnostics/outcomes, pending counts and hook/index exit; soft failures are captured rather than silently acknowledging the path as completed.
- Later read-back: pending/status affect retry; admitted Evidence events, bounded synthesis regions and optional supersession metadata can influence later indexing/ranking/content delivery.
- Delegated visibility: each module sees changed card metadata/body and selected neighbor records; optional registered functions replace confirmer/relevance/synthesis decisions, not a new foreground worker.
- Selection predicate: activation/batch/resource rules, semantic neighbors, same-project filters, editable/managed/authority rules; M2 relevance must pass before editing; M1 confidence-lowering requires its own activation flag.
- Invalidation or expiry: failed paths return to pending; M2 edits its managed region rather than replacing arbitrary whole page; idempotence and card locks constrain repeated mutation.
- Activation or effect: diagnostic-only outcomes are distinct from confidence event writes, synthesis edits and supersession; deployment switch settings and actual mutations unobserved.
- Evidence limits: same-project and authority rails do not establish semantic correctness; callbacks and model scoring remain fallible; detailed memory-revision findings are left to the memory analyst.

Admission: code selects candidates, deterministic production confirmer proposes contradiction, optional stronger confirmer can override that seam, authority rules decide which candidate can be demoted, and M2 uses relevance/contradiction/supersession checks. Human contribution is deployment configuration or content edits, not routine per-change approval. Answer oracle: none; model relevance and heuristic conflict tests are not expected correct outcomes. Operating mode: event-triggered maintenance of changed cards. M2's default synthesis body is deterministic consolidation, with an optional `synth_body_fn` extension; invoking a function does not establish model authorship. Guidance comprises fixed algorithm, card content and metadata. Changed card regions/events persist; pending diagnostics support retry, not demonstrated learning. No general product/capability rewrite is admitted by this path.

> if not failures and deferred_count() == before_deferrals:
>                     try:
>                         import m2_synthesis
>                         m2_synthesis.run_on_ingest(conn, db_file, [path])
> --- `bin/index_impl.py`

> if P["project"] != T["project"]:
>             outcomes.append({"path": path, "action": "skip_cross_project"})
>             continue  # cross-project neighbors never synthesized OR superseded
> --- `bin/m2_synthesis.py`

#### RT-RTE-engine-worker
Label: Core-owned logical-index JSONL worker

Endpoints/progression: client JSONL request → protocol dispatch → logical index resolution → capabilities/health/reconcile/sync/search/rerank → correlated JSON response. Sync validates records/snapshot, computes content hashes, acquires build lock, embeds changed records and deletes absent IDs only for complete snapshots. Search resolves the same logical index, checks model stamps and returns object IDs, titles, kinds and scores. Owner: Core worker and engine; client chooses records and operation. SRC-1: `bin/eidetic_engine_worker.py`, `bin/engine.py`; [RT-CMP-embed](#rt-cmp-embed), [RT-CMP-rerank](#rt-cmp-rerank).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON protocol result/error including sync receipt or search hits/degradation/session ID, not an agent answer.
- Later read-back: synced derived vectors are consumed by later search/reconcile; authoritative text belongs to the caller, not a new Core knowledge-card write.
- Delegated visibility: process receives bounded normalized records or query/docs; storage path derives from Core config/logical ID, not a request-supplied raw SQLite filename.
- Selection predicate: strict operation payload/record schema, unique record IDs and hash collision checks; changed digests trigger embedding; complete snapshot permits deletion; partial snapshot cannot repair stamp drift.
- Invalidation or expiry: missing/deleted records and stamp/content changes require reconcile/sync/rebuild; search returns degraded no hits on incompatible stamps.
- Activation or effect: writes derived index and returns typed search/rerank data; external SDK/application use is outside the frozen boundary.
- Evidence limits: logical ID validation is not caller authentication or an OS sandbox; Core-configured paths may be outside default state root; per-operation recovery is not a demonstrated atomic whole-sync rollback.

Admission: client supplies records, code validates and installs derived numerical state; no per-content human approval or truth assessment. Operating mode: bounded client requests. Answer oracle: none; hashes/stamps test identity/compatibility. Recovery includes retryable busy/unavailable errors and requiring complete snapshots for drift repair. This is production-state maintenance, not a mechanism modifying the engine's source or trained parameters.

> if stamp_drift and snapshot != "complete":
>             raise ProtocolError(
>                 "stale_index",
>                 "A complete snapshot is required after an Engine stamp change",
>                 details={"repair": "rebuild"},
>             )
> --- `bin/eidetic_engine_worker.py`

#### RT-RTE-product-update
Label: Caller-driven upstream runtime installation

Endpoints/progression: background check compares remote main SHA and writes notice → caller runs `update.sh` → clone upstream HEAD → ancestry check → replace runtime files/hooks/contracts → refresh derived artifacts → install metadata/oplog. Owner: update script under local user's filesystem authority; upstream supplies proposed source. SRC-1: `bin/check-update.sh`, `bin/update.sh`, `hooks/smart-memory-inject.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: update notice or update progress; exit 2 warns runtime updated but derived refresh failed; non-fast-forward refusal exits 3 unless explicitly forced.
- Later read-back: subsequent hooks/tools execute replaced source; refreshed rules/indexes and installed SHA metadata are used later.
- Delegated visibility: local Git subprocess fetches upstream; refresh subprocesses receive installed paths/current CWD; no model delegated source-change proposal in this path.
- Selection predicate: fetched HEAD, installed SHA ancestry when available, optional EIDETIC_UPDATE_FORCE override; missing installed commit permits first-tracked-update behavior.
- Invalidation or expiry: notice is throttled for six hours and removed after update; refresh-pending supports retry despite unchanged installed SHA.
- Activation or effect: per-file atomic replacement changes behavior-determining executable source and hook files; check alone only records availability.
- Evidence limits: ancestry does not validate source correctness or safety; files are replaced individually, not a whole-install transaction; upstream revision fetched in a future deployment is not evidence in this frozen run.

Admission: human or agent caller initiates command, which does not imply inspection/approval of each source change. Upstream commits supply the candidate product; script can reject known non-ancestor HEAD, caller can force acceptance. Operating mode: update to upstream, not learning/experiment. Answer oracle: none; ancestry is an integrity rule, not a behavior evaluator. Guidance is updater code/upstream history; executable files and metadata persist. Hook `.pre-update` backups provide a partial rollback artifact, not full rollback for bin/contracts/indexes. This establishes an implemented change-admission route, not evidence-responsive self-improvement of the bounded system.

> elif [ "${EIDETIC_UPDATE_FORCE:-}" = "1" ]; then
>             echo "WARNING: non-fast-forward update accepted because EIDETIC_UPDATE_FORCE=1."
> --- `bin/update.sh`

> echo "WARNING: Runtime files updated, but one or more derived refresh steps failed."
> --- `bin/update.sh`

### Claims

#### RT-CLM-feedback-visibility
Label: Feedback never-invisible assembly rule

Claimed operation: all indexed feedback memories remain represented in assembled context. Owner/enforcement: `fetch_feedback` in SRC-1 `bin/assemble_context.py`; guarantee strength: invariant for names/cluster representation within successful assembly, not full semantic rule delivery. Covered path: feedback query and formatting including overflow. Counterpaths: failed/skipped assembly, project MEMORY.md fallback, missing/unindexed cards, and cluster summaries that are not full member texts. Required external contract: current index, successful file write and host rules loading. The budget is adaptive and can overflow to preserve names; it is not a strict maximum for all output.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> for _, rest_name, _ in individual[i:]:
>                 result.append(f"- {rest_name}\n")
>                 used += len(rest_name) + 3
> --- `bin/assemble_context.py`

#### RT-CLM-base-isolation
Label: Base scan containment

Claimed operation: base indexing scans only its declared contained corpus, not personal memory. Owner/enforcement: `_collect_base_files` in SRC-1 `bin/index_impl.py` checks realpath containment of roots and each Markdown file. Guarantee strength: invariant of this scanner's selection. Covered alternatives include absolute roots, traversal and symlink escapes. Required external contract: correct base manifest/root and ordinary filesystem behavior; this is not adversarial concurrent-filesystem isolation. Alternate paths not covered: arbitrary external clients, direct shell reads/writes and Core-configured SDK index paths. An attached-base tool subset is surface narrowing, not an OS access boundary.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if fp in seen or not _inside(fp):   # per-file realpath: blocks symlinked leaks
>                     continue
> --- `bin/index_impl.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-memory-rules
Label: Retained feedback to foreground rules

Consumer: foreground host model. Channel: assembled `memory-context.md` loaded through Claude Code rules. Force: natural-language directive under `ALWAYS APPLY`; name-only overflow and cluster summaries weaken delivered content, and no inspected code forces model compliance. Horizon: subsequent sessions whose rules loader reads this artifact. SRC-1: `bin/assemble_context.py`, `hooks/smart-memory-inject.sh`; delivered object [RT-OBJ-memory-context](#rt-obj-memory-context), route [RT-RTE-context-injection](#rt-rte-context-injection). This path establishes possible later behavioral authority, not observed changed behavior or demonstrated benefit.

> output.append("## Behavioral Rules (type=feedback) — ALWAYS APPLY\n\n")
> --- `bin/assemble_context.py`

## Annotations

none
