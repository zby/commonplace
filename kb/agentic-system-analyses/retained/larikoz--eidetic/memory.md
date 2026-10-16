---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Eidetic memory: Markdown cards, derived retrieval state, session context, gated consolidation and distinct withdrawal/export paths."
run-id: AAS-2026-10-14-eidetic-0e54f3c114b3-01
source-identity: https://github.com/LARIkoz/eidetic
reviewed-boundary: "67506b62fdd0944c243537c3cb10938f7343b6b2"
---

# Eidetic memory report

## Boundary and evidence

This account covers the shipped personal memory and topic-base loops at SRC-1, commit `67506b62fdd0944c243537c3cb10938f7343b6b2`. The source register and excluded host/provider/application responsibilities remain those of [boundary](boundary.md#source-register). Runtime findings are provisional inputs, not execution evidence. Direct reads added card/event projection, confidence folding, maintenance mutation, cleanup/curation, handoff selection, code extraction, serendipity, session counts, telemetry, M3 provenance/cache and export details. All added evidence is implementation or source-owned doctrine/design. No target code, tests, examples or model services were executed.

Memory includes retained natural-language cards, their symbolic metadata/events, derived lexical and dense indexes, generated context, session-adaptive hints and caches that affect subsequent invocations. Raw host transcripts are inputs, not automatically a complete Eidetic memory store. Product updates are covered by runtime; this member does not reclassify their executable files as learned knowledge. External model weights, host compaction and actual deployment loading remain uninspected. Examples and private corpora do not establish live use or benefit.

### Coverage inventory

“Direct” means inspected in this job; “supplied” means the cited runtime finding supplies the traced facts. Rows marked partial keep unresolved facts beside the prevented conclusion.

| Entry or operation | SRC-1 paths and evidence basis | Records / limit |
| --- | --- | --- |
| Personal creation, append and Stop compounding | Direct `bin/remember.py`, `bin/compound.py` search; supplied `hooks/session-signals.sh` | [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission), [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound), [MEM-OBJ-memory-cards](#mem-obj-memory-cards); exact signal-file formatting remains supplied rather than independently retraced. |
| Personal index and installed skill admission | Direct `bin/index_impl.py` collector and projection | [MEM-OBJ-memory-chunks](#mem-obj-memory-chunks), [MEM-RTE-evidence-projection](#mem-rte-evidence-projection); physical existing-file authorship/control remains unknown. |
| SessionStart push, handoff and fallback | Direct `hooks/smart-memory-inject.sh`, `bin/assemble_context.py`, `bin/session_counter.py` | [RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [MEM-RTE-fresh-handoff](#mem-rte-fresh-handoff), [MEM-RTE-session-hints](#mem-rte-session-hints). |
| Search/detail, bounded enrichment and forked recall | Direct `bin/search_impl.py`; supplied `skill/SKILL.md`, `mcp_server.py` | [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall); detail reads indexed content, not necessarily current file bytes. |
| Serendipity | Direct `bin/serendipity.py`; MCP tool registration searched | [MEM-RTE-serendipity-read](#mem-rte-serendipity-read); result usefulness unobserved. |
| Topic-base init/add/index/attach/refresh | Supplied `bin/base.py`, `mcp_server.py`; CLI dispatch searched; direct base collector interface | [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission), [RT-CLM-base-isolation](runtime.md#rt-clm-base-isolation); refresh internals not retraced, so no independent refresh consistency guarantee. |
| Core library/JSONL index sync, search, reconcile, rerank | Supplied `bin/engine.py`, `bin/eidetic_engine_worker.py` | [RT-RTE-engine-worker](runtime.md#rt-rte-engine-worker); unspecified API callers alone supply no additional agent-consumer route. External SDK applications excluded. |
| M1 diagnostics and M2 region/supersession writes | Direct `bin/m1_contradiction.py`, `bin/m2_synthesis.py`, `bin/evidence.py`, `bin/confidence.py` | [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance), [MEM-OBJ-evidence-events](#mem-obj-evidence-events); no successful maintenance run supplied. |
| Drift, declared relations, decay and withdrawal | Direct `bin/drift_check.py`, `bin/index_impl.py`, `bin/curate.py`, `bin/cleanup.py` | [MEM-RTE-evidence-projection](#mem-rte-evidence-projection), [MEM-RTE-card-withdrawal](#mem-rte-card-withdrawal). |
| M3 recall filing and producer provenance | Direct `bin/m3_hook.py`, `bin/m3_producer_driver.py`, `bin/m3_autofile.py` | [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing), [MEM-OBJ-memory-cards](#mem-obj-memory-cards); optional judge model facts supplied by runtime. |
| M3 rejection cache and acquisition/agent dark lanes | Direct `bin/m3_seen_cache.py`; `bin/m3_acquisition.py` doctrine and `bin/m3_agent_lane.py` bounded searches; supplied hook routing | [MEM-OBJ-admission-traces](#mem-obj-admission-traces). Child-transcript eligibility, detailed dark-lane gates and their later report consumers remain partially inspected; prevents comprehensive lane-quality or evidence-lineage claims, not the supported distinction from card filing. |
| Lifecycle/test correlation | Direct `bin/lifecycle_signals.py`, `bin/m3_autofile.py`; supplied installer/hook wiring | [MEM-RTE-test-affirmation](#mem-rte-test-affirmation); ordinary M3 project identity does not match lifecycle HMAC identity without additional mediation. |
| Optional code memory | Direct `bin/code_index.py`, injection caller | [MEM-RTE-code-projection](#mem-rte-code-projection); parser internals and complete language coverage uninspected. |
| Vault export, polish and topic synthesis | Direct selected regions of `bin/export_vault.py`; MCP registration searched | [MEM-RTE-vault-export](#mem-rte-vault-export), [MEM-CMP-export-models](#mem-cmp-export-models); vault edits are not established as a personal-memory import route. |
| Recall evaluation, usage and passive-value reports | Direct `bin/usage.py`, `bin/curate.py`, `bin/recall_lab.py` dispatch and `bin/passive_stats.py` doctrine; supplied `bin/recall_smoke.py` oracle | [MEM-OBJ-admission-traces](#mem-obj-admission-traces), [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall). Canary/health/lint/replay internals not retraced; no full evaluator inventory, observed score, automated benchmark-to-card update or causal benefit inferred. |
| Product update | Supplied `bin/update.sh`, `bin/check-update.sh` | [RT-RTE-product-update](runtime.md#rt-rte-product-update); distinct from memory curation and parameter training. |

## Core ideas

1. **Markdown is the retained content; databases are operative projections.** Cards carry text and authored metadata. Typed Evidence events are reparsed and folded into confidence; History and M3 Provenance are not interchangeable with those events. The SQLite projections can be rebuilt or cleared while the card remains. [MEM-OBJ-memory-cards](#mem-obj-memory-cards), [MEM-OBJ-evidence-events](#mem-obj-evidence-events), [MEM-RTE-evidence-projection](#mem-rte-evidence-projection).
2. **Push and pull have different selectors and authority.** Successful assembly gives every indexed feedback card a name/cluster representation, not every rule's complete meaning. Other sections compete for character budgets. Search returns candidates and reload identifiers on demand; host loading and agent judgment remain external. Fresh handoffs bypass card indexing, and session counts add directives not derived from factual card content. [RT-CLM-feedback-visibility](runtime.md#rt-clm-feedback-visibility), [RT-BAP-memory-rules](runtime.md#rt-bap-memory-rules), [MEM-RTE-fresh-handoff](#mem-rte-fresh-handoff), [MEM-RTE-session-hints](#mem-rte-session-hints).
3. **Admission control is per path.** Explicit writers, automatic extraction, M3 support gating, M2 relevance gating and human-directed CLI archival do not share a universal approval or correctness gate. Source labels and authority tiers are material inputs to code, not authenticated provenance. A caller can create a new feedback card despite existing-card protections. [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission), [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound), [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing).
4. **Retention and withdrawal are not binary.** Confidence and status usually change prominence; feedback remains name-visible, and detail can expose archived/superseded indexed text. Moving a file to cleanup's archive requires index refresh to remove the old projection. Export copies can outlive their sources. [MEM-RTE-card-withdrawal](#mem-rte-card-withdrawal), [MEM-RTE-vault-export](#mem-rte-vault-export).

## Shared records

### Components

#### MEM-CMP-export-models
Label: Export polish and topic model alternatives

Source-native identities: `POLISH_MODEL_SONNET`, `POLISH_MODEL_HAIKU`, `TOPIC_CLUSTER_MODEL` and `TOPIC_SYNTHESIS_MODEL` in SRC-1 `bin/export_vault.py`. Distinct from the extractor, embedding, reranking and local judge components supplied by runtime; none is a counterpart for these export invocation roles. Distributed-parametric weights reside behind external `claude-batch` routes; input/output text and cached topic clusters are local. Defaults are Sonnet `claude-sonnet-5-5`, Haiku `claude-haiku-4-5-20251001`, and topic synthesis `claude-opus-4-6`; cluster defaults to the Sonnet label. Parameters change during operation: no training invocation at these call sites; provider internals uninspected. Exact version pinned: labels only, not immutable weights. Mutable endpoint can resolve another model: environment overrides and external wrapper resolution can change the model. The “via Sonnet” topic docstring is not the configured default synthesis identity.

> TOPIC_SYNTHESIS_MODEL = os.environ.get("EIDETIC_TOPIC_SYNTHESIS_MODEL", "claude-opus-4-6")
> --- `bin/export_vault.py`

### Operative objects

#### MEM-OBJ-memory-cards
Label: Personal cards and topic corpus files

Source-native identities: card files built by `remember.build_card` and topic docs/notes written by `base.cmd_add`. Natural-language bodies/descriptions are interpreted by agents or humans; symbolic frontmatter controls type, source, kind, status and ranking. Storage is local Markdown: project memory and signal directories, agent memory, and separate base corpus roots. Generic container spans the source inputs of [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission), [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound) and [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing); distinct from the generated [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context), not a duplicate delivery artifact.

Lineage varies per part: caller-authored/promoted answer, transcript-derived signal/History append, imported topic corpus or gated M3 recalled answer. Existing files can have unknown initial authorship/control; metadata alone cannot settle that. M3 files retain query, session, source IDs, truncated cited spans and per-claim scores under Provenance; this is derived support evidence, not the original recalled answer's source-use trace. Default M2 managed regions retain trigger/source/date/score and wikilink one-liners, not a complete semantic argument. Later index/search/detail and successful push assembly consume different selected portions. Feedback text can become a directive through [RT-BAP-memory-rules](runtime.md#rt-bap-memory-rules); other card text is candidate knowledge/context. Natural-language interpretation, not file persistence, determines foreground compliance. SRC-1: `bin/remember.py`, `bin/base.py`, `bin/m3_autofile.py`, `bin/m2_synthesis.py`.

> body = answer + "\n\n" + prov_block
> --- `bin/m3_autofile.py`

> f"card_kind: {kind}",
> f"evidence: {evidence}",
> f"source: {source}",
> f"last_verified: {TODAY}",
> --- `bin/remember.py`

#### MEM-OBJ-memory-chunks
Label: Indexed card sections and dense retrieval parts

Source-native identity: SQLite `memory_chunks` in SRC-1 `bin/index_impl.py`, plus the separate vector database consumed by `bin/search_impl.py`. No supplied object names this source projection; closest supplied object is [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context), which is its generated consumer output, not its identity. Split operative parts: copied natural-language section content; symbolic path/project/heading/hash and metadata used by SQL/ranking; distributed-parametric dense vectors derived by [RT-CMP-embed](runtime.md#rt-cmp-embed), not readable summaries or trained model weights. Database blobs and numerical vectors do not themselves carry the readable reasons preserved in cards.

Lineage: card section splitting and metadata inference populate text rows; typed events derive lifecycle/confidence; declared relations derive effective status. Optional code rows are a separate source-origin part, covered by [MEM-RTE-code-projection](#mem-rte-code-projection). Personal collection also indexes installed `~/.claude/skills/*/SKILL.md`, while excluding MEMORY.md and BACKLOG.md; topic manifests replace personal scanning. Exact initial file admission is not authenticated by this scanner. Later consumers: FTS, vector alignment checks, detail, serendipity, assembly, maintenance neighbor selection, diagnostics and export weighting. Derived symbolic/dense parts hold selection authority, while returned text reaches interpretive consumers. Runtime supplies vector stamp handling; direct source confirms per-content hash rejection. SRC-1: `bin/index_impl.py`, `bin/search_impl.py`; [RT-RTE-engine-worker](runtime.md#rt-rte-engine-worker) separately covers logical-index client records, not necessarily Markdown-backed knowledge.

> skill_pattern = os.path.expanduser("~/.claude/skills/*/SKILL.md")
> --- `bin/index_impl.py`

> if digest != vector_hash:
>             continue
> --- `bin/search_impl.py`

#### MEM-OBJ-evidence-events
Label: Typed Evidence and confidence projection

Source-native identity: card `## Evidence`, derived `card_events` rows and `memory_chunks.confidence`. Distinct from [MEM-OBJ-memory-cards](#mem-obj-memory-cards)' ordinary prose and from runtime's generated rules file; closest supplied route is [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance). Operative parts: symbolic timestamp/type/actor/session fields and confidence algebra; optional natural-language notes explaining origin; local Markdown durable substrate and rebuildable SQLite projection. Authored History lines and M3 Provenance scores are not typed promoting events.

Lineage: path-specific writer emits accepted events; index reparses current Evidence, derives actor tier and recomputes confidence from cold start. Stored delta is decorative, not trusted arithmetic. Managed scope includes feedback and eligible agent-extracted cards; user/reference, concept/entity and imported content are exempt except the explicit feedback precedence. Numerical confidence is localized symbolic state consumed by a fixed formula, not distributed model parameters. Tier-1 observations diminish and cap; tier-3 confirmation establishes a high-water floor against lower-tier negatives; decay has its separate 0.55 floor. Later rank effects require the separate ranking switch. Notes can be indexed/read as text but no inspected ranking consumer reasons from their explanation. Actors and source fields are parsed labels, not authenticated identity. SRC-1: `bin/evidence.py`, `bin/index_impl.py`, `bin/confidence.py`, `bin/search_impl.py`.

> CONF_FLOOR = 0.35        # conf_w = CONF_FLOOR + (1-CONF_FLOOR)*confidence
> --- `bin/confidence.py`

> Only the typed `## Evidence` section is read — NEVER legacy `## History`
>     date-lines (risk #5 double-count guard). The fold recomputes the effective
>     delta from event_type + order; the parsed Δ is decorative/audit only.
> --- `bin/index_impl.py`

#### MEM-OBJ-admission-traces
Label: Admission cache, test correlation and usage traces

Source-native identities and distinct parts: `events/m3_judged.jsonl` stores symbolic session/candidate-key/outcome cache; `m3_filed.jsonl` and `test_signals.jsonl` store filing and test-correlation metadata; lifecycle JSONL stores bounded tool metadata; `db/usage.log` stores path/section/rank/query-hash/confidence; injection/passive-value JSONL stores counts/slugs. Local append-only files, not opaque numerical models or raw transcript archives. Closest supplied records are [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing) and [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall); these are distinct retained parts rather than duplicate routes.

Later consumers differ: judged cache suppresses definitive same-session candidates before retrieval/judging; transient failures retry and another session rejudges. Test/filing metadata can emit Evidence through [MEM-RTE-test-affirmation](#mem-rte-test-affirmation). Usage supports curation proposals, not automatic promotion. Cost/reference statistics support operator reports; a slug mention is not causal benefit. Acquisition/agent dark logs are candidate/outcome evidence, not admitted cards; their exact payloads/report consumers remain partially inspected. Lifecycle cleanup deletes old daily logs, but that function does not delete these sibling M3/test files. No common expiry for all telemetry is established. SRC-1: `bin/m3_seen_cache.py`, `bin/m3_autofile.py`, `bin/lifecycle_signals.py`, `bin/usage.py`, `bin/passive_stats.py`, `bin/cleanup.py`.

> DEFINITIVE = frozenset(
>     {"filed", "deduped_to_m2", "rejected", "would_file", "would_reject"})
> --- `bin/m3_seen_cache.py`

> for rank, r in enumerate(results[:TOP_K_LOG], 1):
> --- `bin/usage.py`

### Routes

#### MEM-RTE-evidence-projection
Label: Evidence and relation projection

Endpoints/progression: event writer or edited card → incremental/full index → parsed Evidence/confidence and recomputed relations → later ranking, context and diagnostics. Index code owns projection; writer/model/caller owns proposed content. Distinct from [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance)' pending M1/M2 dispatch: this route materializes existing card declarations and events even when those transformations are dormant. SRC-1: `bin/index_impl.py`, `bin/evidence.py`, `bin/confidence.py`, `bin/drift_check.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: index diagnostics and durable text/metadata projection; event writer returns written/no-op status.
- Later read-back: effective status/relations and separately enabled confidence weights influence subsequent search/assembly; current Evidence replaces the prior event projection.
- Delegated visibility: inapplicable — deterministic parser/fold/relation code is not a delegated model invocation.
- Selection predicate: file collection/change detection, typed Evidence sections, managed scope, same relation namespace, source/evidence tier and recency authority gates; decay requires a penalizing age-stale finding and managed non-feedback confidence above its floor.
- Invalidation or expiry: deleted source rows/events are pruned on incremental indexing; removed events are cleared on reparsing; removed relation declarations clear effective relations; decay emits at most one event per silence episode.
- Activation or effect: code derives rank/control metadata; events require confidence-events activation and confidence rank effects require confidence-ranking activation; no observed foreground effect.
- Evidence limits: authored labels are not provenance authentication, filesystem timestamps are not semantic truth, and index freshness is best effort at host injection.

Admission/control: event type validation, bounded card locking and deterministic arithmetic control writes; generic caller identity does not establish human approval. Projection's authority gate refuses downranking by insufficiently authoritative/older declarers while retaining diagnostics. Explicit target declarations win. People can edit source text/events and reverse declarations; code recomputes rather than semantically approves edits. Operating mode: changed-file maintenance, not expected-answer evaluation. Answer oracle: none. Guidance is parser/algebra/current metadata; typed events, notes and source declarations persist. Atomic per-card replacement and reindex permit retry/rebuild, not automatic semantic rollback. Decay is an automatic metadata update from absence of verification, not newly discovered factual content.

> conn.execute("DELETE FROM card_events WHERE path = ?", (filepath,))
> --- `bin/index_impl.py`

> explicit = card[column + "_explicit"]
>             updates[(path, column)] = explicit or ", ".join(sorted(desired[path][column]))
> --- `bin/index_impl.py`

#### MEM-RTE-fresh-handoff
Label: Fresh handoff read-back

Part of: [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)

This separately sourced route part selects unindexed state files before context assembly; it is not a second declaration of all injection. Endpoints: CWD/project-pattern candidate paths → freshest file → capped text → rules file → host loader. Python owns selection; external file producer owns handoff authorship and original admission, which remain unresolved. SRC-1: `bin/assemble_context.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: handoff text and character count to assembly.
- Later read-back: retained state.md from memory/output/handoff/.kurdyuk-lite paths enters a later session's Recent Handoff section.
- Delegated visibility: inapplicable — local file read and assembly, not a separate agent invocation.
- Selection predicate: project-pattern or CWD-contained candidates, newest mtime less than 30 minutes old, first 3000 characters; no card index/type/support prerequisite.
- Invalidation or expiry: age expires selection; fresher candidate replaces it on subsequent assembly; existing rules content may survive failed assembly.
- Activation or effect: reduces project budget by half its character cost with a 1000-character minimum and adds handoff content to generated rules; host use unobserved.
- Evidence limits: mtime freshness is not factual validation; producer provenance and actual host consumption uninspected.

> HANDOFF_MAX_AGE_MINUTES = 30
> HANDOFF_MAX_CHARS = 3000
> --- `bin/assemble_context.py`

#### MEM-RTE-session-hints
Label: Session count adaptive hints

Part of: [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)

Endpoints: SessionStart hook → sessions.db append/count by normalized project → fixed HINTS selection → appended Session Awareness → host rules loader. Distinct part uses retained symbolic counts rather than card knowledge; hook and counter code own updates and threshold decisions. SRC-1: `bin/session_counter.py`, `hooks/smart-memory-inject.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: session count, phase and natural-language hint.
- Later read-back: prior session_log rows determine the next count/phase; generated directive reaches later host rules loading.
- Delegated visibility: inapplicable — deterministic counter and shell append.
- Selection predicate: normalized CWD project; count below 10, up to and including 30, or above 30 chooses novice/standard/veteran text.
- Invalidation or expiry: no expiry in this counter; repeated invocation can append another row; manual database changes are outside this route.
- Activation or effect: durable count and rules-file append; request for proactive/terser behavior, not measured expertise or compliance.
- Evidence limits: session count is not an outcome evaluator; no demonstrated benefit or foreground action trace.

Admission: automatic hook/counter code admits session rows with no per-row human content approval. Fixed shipped guidance persists as code and is selected by count. Mode: lifecycle invocation; answer oracle: none. Failure is fail-open at the hook, not correctness rollback. Hint text is natural language on a rules-file substrate; selection state is symbolic SQLite, not learned parameters.

> if count < 10:
>         return HINTS["novice"], "novice"
>     elif count <= 30:
>         return HINTS["standard"], "standard"
>     else:
>         return HINTS["veteran"], "veteran"
> --- `bin/session_counter.py`

#### MEM-RTE-serendipity-read
Label: Serendipity retained connections

Endpoints: query via CLI/MCP → primary FTS rows → wikilinks/key terms → cross-project-first candidates → returned snippets. Code owns selection, caller owns use. No supplied counterpart after comparison with [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall): this is a separate registered discovery command, not its ranked confidence/detail pipeline. SRC-1: `bin/serendipity.py`, `mcp_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: candidate paths/project labels and up to 200-character content snippets.
- Later read-back: previously indexed card sections are selected from query seeds and connections.
- Delegated visibility: inapplicable — subprocess search rather than model delegation.
- Selection predicate: five primary rows; extracted wikilinks and terms; cross-project preference then same-project fill, default three surprises.
- Invalidation or expiry: underlying reindex changes available content; no result persistence or expiry established here.
- Activation or effect: delivers context candidates on request; no card mutation or demonstrated use.
- Evidence limits: connection label does not establish a true semantic relation; no inspected safety/authority guarantee equivalent to ordinary recall confidence.

> surprises = cross_project[:max_surprises]
> --- `bin/serendipity.py`

#### MEM-RTE-code-projection
Label: Optional code entity projection

Part of: [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)

Endpoints: SessionStart CWD → optional tree-sitter extraction → replacement code rows in memory_chunks → later retrieval/assembly. This part is a producer responsibility within the supplied injection route, not a duplicate whole route. Code supplies source spans; parser and indexer own entity selection. SRC-1: `hooks/smart-memory-inject.sh`, `bin/code_index.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: entity count/diagnostics, normally captured by hook caller.
- Later read-back: persisted source bodies and language/name/line headings are available to ordinary index consumers on later queries/assembly.
- Delegated visibility: inapplicable — parser subprocess, not a model call.
- Selection predicate: tree-sitter import/language availability, supported file extensions and extracted entities; hook enforces ten-second subprocess timeout.
- Invalidation or expiry: successful refresh deletes prior code rows for the directory before inserting its current extracted rows; failed/unavailable refresh establishes no current-source guarantee.
- Activation or effect: installs code/observed/code-index metadata and source bodies as derived retrieval material, not formulated lessons from a session trace.
- Evidence limits: exact parser coverage uninspected; source code can be stale at later retrieval; no demonstrated consumer use.

Admission: automatic parser code admits rows; project owner controls files but is not consulted per entity. No truth oracle; fixed parsing rules, source bytes and metadata guide the projection. SQLite transaction supports write recovery, not semantic validation. Natural-language/code bodies are separate from symbolic language/line/path metadata.

> VALUES (?, ?, ?, 'code', 'observed', 'code-index',
>                         'code', 'current', ?, ?, ?, ?, ?)
> --- `bin/code_index.py`

#### MEM-RTE-test-affirmation
Label: Project test correlation promotion

Part of: [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)

Endpoints: PostToolUse Bash classified as test → test_signals JSONL; M3 filing → m3_filed JSONL; enabled index producer joins session/project → Evidence verified_by_test → later confidence fold/ranking. This post-filing part is distinct from pre-filing claim-support judgment. Code owns classification/join/admission, host supplies event success semantics; no claim-specific evaluator participates. SRC-1: `bin/lifecycle_signals.py`, `bin/m3_autofile.py`, `bin/index_impl.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: producer outcomes or no matches; lifecycle event remains metadata plus side-effect correlation signal.
- Later read-back: emitted Evidence can raise the card's folded confidence at a subsequent index and influence separately activated ranking.
- Delegated visibility: inapplicable — classification/join/event code; no model judgment here.
- Selection predicate: producer flag, active M3/evidence rails, matching nonempty session/project, filed page, valid typed affirmation and no duplicate same-source promotion.
- Invalidation or expiry: same-source event guard prevents repeated promotion; event projection reparses edited Evidence; no expiry established for correlation files.
- Activation or effect: path can write verified_by_test, but current ordinary hook identity mismatch prevents inferring it promotes hook-filed pages.
- Evidence limits: project-wide passing test is correlation, not support for a particular claim; host success report and caller-supplied typed affirmation are trusted inputs, not an authenticated claim oracle.

The mismatch is concrete: lifecycle records set project_slug to `project_` plus eight HMAC hex characters; M3 hook takes the transcript parent basename. `produce_test_affirmations` compares strings exactly. No translation at these inspected seams bridges them. This qualifies, not deletes, the implemented producer capacity: caller-supplied matching slugs can take the path, while ordinary hook promotion is not established. Recovery is retry/idempotence or source editing; no automated reversal of a misleading promotion is shown. Operating mode: session correlation; expected-answer oracle: none. People can enable flags or edit records, but activation is not per-card approval.

> record["project_slug"] = f"project_{cwd_hash[:8]}"
> --- `bin/lifecycle_signals.py`

> slug = os.path.basename(os.path.dirname(transcript))
> --- `bin/m3_hook.py`

> if not slug or slug not in passing:           # cross-project / no-project ⇒ no match
>             continue
> --- `bin/m3_autofile.py`

#### MEM-RTE-card-withdrawal
Label: Card curation and withdrawal alternatives

Endpoints: caller asks curate/cleanup → code proposes candidates → explicit CLI write flags or archive mode → status edit or file move → caller reindex → later search/context. Distinct from [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance)' automatic semantic editing and [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission)' content admission. Three operative parts: usage-based promotion proposals only; reversible status archival; physical cleanup archival/log deletion. SRC-1: `bin/curate.py`, `bin/cleanup.py`, `bin/index_impl.py`, `bin/search_impl.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: candidate report, dry run, archival/move tally or lifecycle-file removal count.
- Later read-back: status archived is parsed at reindex and downweights but does not exclude card recall/detail; moved cards leave live scan/index after refresh; retained usage drives later proposals.
- Delegated visibility: inapplicable — deterministic CLI selection and file operations.
- Selection predicate: curate uses distinct query hashes for promotion, or age-stale plus never-pulled and unprotected type for archival; cleanup uses mtime/size/inbound-link score with protected feedback/user exemption; lifecycle cleanup selects old daily JSONL by mtime.
- Invalidation or expiry: status can be reset to current; file move is not immediate index deletion; cleanup's default lifecycle retention is 30 days; card archive content is preserved rather than destroyed.
- Activation or effect: curate requires --apply --yes to write status, cleanup --archive moves selected cards without a per-item dialog; none of these establishes human authorship/approval of each change merely from invocation.
- Evidence limits: surfacing is not use/benefit, stale metadata is not falsity, and physical archive is not recall-preserving status archival; source-native read-only/human-confirmation prose overstates these CLI write barriers.

Code proposes and selects; caller can veto by not running the write mode and can reverse status/move manually. No expected-answer oracle; operation is open corpus maintenance under fixed heuristics. Reasons appear in reports; archival writes status or relocates text, not a complete criticism argument. File integrity/reindex support recovery, not automatic semantic rollback. Cleanup does not perform index refresh itself. Its human-confirmation docstring therefore describes workflow intent, not a built-in per-item gate.

> if not args.yes:
>         print(f"DRY RUN — would set status:archived on {len(rows)} card(s); search keeps\n"
>               f"them, drift stops flagging. Re-run with --apply --yes to write.\n")
> --- `bin/curate.py`

> shutil.move(path, dest)
> --- `bin/cleanup.py`

#### MEM-RTE-vault-export
Label: Derived vault export and synthesis

Endpoints: CLI/MCP request → file discovery/quality gate/templates and link rewrite → vault files/manifest → optional polish and topic synthesis → human-readable vault. Exporter owns physical write/admission; models propose transformed prose. Distinct from [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission) and [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context): destination is an exported artifact, not personal card admission or foreground rules. SRC-1: `bin/export_vault.py`, `mcp_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: written vault notes, navigation/topic pages, source-hash manifest and progress/errors.
- Later read-back: re-export reads manifest/source hashes and cached clusters; topic synthesis reads already exported notes; human vault reading is afforded, not observed; no inspected automatic vault-to-personal-memory import.
- Delegated visibility: external claude-batch receives note body for polish or selected exported notes for synthesis, not necessarily the whole source corpus.
- Selection predicate: project/type/description/size/operational gates, optional all/force; polish chooses ranked notes and skips already polished; topic synthesis sorts by weight, takes top 20 and bounds combined text, truncating to 12000 characters after overflow.
- Invalidation or expiry: delta skips unchanged source hashes and keeps on-disk orphan manifest entries; full rerender is suggested for link changes; export does not establish synchronized withdrawal from every retained copy.
- Activation or effect: creates/transforms derived natural-language material and symbolic lineage/navigation; actual reading or benefit unobserved.
- Evidence limits: preserve-all-facts prompt does not prove preservation; exit/length acceptance is not truth assessment; exported reasons/source lists can be incomplete after selection/truncation; vault-local edits have no established protected merge/import semantics.

Admission: invocation flags and local code gates decide destination writes; polish accepts successful nontrivial stdout, topic synthesis accepts successful output over its length minimum. Caller can disable polish/synthesis or withhold command, but no per-note human semantic approval is built in. Operating mode: corpus export; answer oracle: none. Prompts request preserved facts, coherent sections and source links. Bodies, source-hash manifest, polish markers and topic source lists persist. Failure can retain unpolished/base export; atomic note replacement is not semantic rollback. Topic model defaults and mutability are [MEM-CMP-export-models](#mem-cmp-export-models).

> if delta and rel_path in old_files and old_files[rel_path].get("sha256") == sha:
>             continue
> --- `bin/export_vault.py`

> top_notes = sorted_notes[:20]
> --- `bin/export_vault.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-session-awareness
Label: Session history to behavioral hint

Consumer: foreground host model. Channel: Session Awareness appended to memory-context.md. Force: natural-language directive selected by symbolic count. Horizon: subsequent session invocations as session_log accumulates. Distinct from [RT-BAP-memory-rules](runtime.md#rt-bap-memory-rules)' retained feedback; it does not need authored knowledge cards. [MEM-RTE-session-hints](#mem-rte-session-hints) supplies producer/selector; host loading and compliance remain uninspected. SRC-1: `bin/session_counter.py`, `hooks/smart-memory-inject.sh`.

> "Be proactive. Skip explanations for established patterns. "
>         "Anticipate needs. Flag only novel situations."
> --- `bin/session_counter.py`

## Annotations

#### On [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)

Memory-specific selection: assembly targets 24000 characters, not a precise model-token cap. Project/recent allocations are 0.3/0.2; feedback receives the remainder with a 1000-character minimum after handoff and drift diagnostics. Feedback top/mid/low tiers deliver at most 500-character description, 60-character description or name only; cluster summaries substitute static text for member bodies. Overflow preserves names and can exceed the nominal budget. Fresh handoff and session hints are separate retained-source parts declared above. Cards remain reachable outside the generated file, but path/name cues are text by value, not live references. Source trust weights change prominence, not per-rule approval. SRC-1: `bin/assemble_context.py`; supporting supplied passage: [RT-CLM-feedback-visibility](runtime.md#rt-clm-feedback-visibility).

#### On [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall)

Read-back detail uses memory_chunks by path/section or stable detail ID. It expands the indexed projection, not necessarily current Markdown bytes; a separate caller file read can differ. Bounded search first computes a model-free lexical result, then invokes optional semantic enrichment under a timeout (default 30 seconds), returning lexical results if unavailable/timed out. Weak results remain inspectable in JSON although default text suppresses them. Card confidence fold is distinct from retrieval high/medium/low confidence. Optional forked skill isolation keeps search work out of the foreground context under the host contract; it does not evict existing caller turns or implement host compaction. SRC-1: `bin/search_impl.py`; skill isolation/interpretive-use passage supplied by the cited runtime record.

> native = _run_query(db_path, query, limit, type_filter, lexical_only=True)
> --- `bin/search_impl.py`

#### On [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance)

Curation parts: M1 default opposition detector names a candidate conflict; authority rules can demote through Evidence or leave a relation diagnostic. Its explicit contradiction flag is separate from confidence-events. M2 edits only managed durable eligible targets; user, feedback and todo/handoff targets are excluded. Default synthesis is deterministic linked salient claims, not model-written explanatory synthesis. Relevance uses the separate reranker and fails closed on unavailable/nonfinite scores. Contradictions defer to M1; default temporal supersession is suggestion-only, with an additional autoflag and stricter relevance required for mutation. No inspected global transaction retracts all downstream consequences. SRC-1: `bin/m1_contradiction.py`, `bin/m2_synthesis.py`.

Managed-region editing preserves surrounding page text and replaces its own region. Trigger/source/date/score and related one-liners retain limited lineage; original reasoning is not reconstructed by ranking. Region plus one tier-1 observed event share locked atomic replacement; unchanged body has explicit event recovery/idempotence logic. Broken-region targets fail closed. Source comments saying “skip edit AND event” are qualified by the missing-event recovery branch. These are implemented bounded transformations; no revised meaning, factual correctness or improvement is inferred solely from “synthesis.”

> if t in ("user", "feedback"):
>         return False
> --- `bin/m2_synthesis.py`

> if not recorded:
>                     wrote = _EV.append_event(path, "observed", actor="agent-extracted",
>                                              note=note, _locked=True)
> --- `bin/m2_synthesis.py`

#### On [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)

Read-back lineage: driver re-retrieves up to three source chunks from eligible existing /memory/ files, truncating each to 900 characters for support. These are support witnesses selected now, not evidence that the original answer used them. Persisted Provenance further shortens displayed spans to the one-line formatter's default limit (240 characters), with 80-character claim displays. It labels scores “deterministic span-overlap” even when an alternative support function/judge supplied them. M3 creates cold-start content without minting an observed event from filing itself. Admission cache affects later same-session selection independently of whether a card was admitted. SRC-1: `bin/m3_producer_driver.py`, `bin/m3_autofile.py`, `bin/m3_seen_cache.py`.

Acquisition ground is the cleaned assistant transcript, not independently corroborated world evidence; user turns are excluded by declared lane policy. Acquisition and independently gated agent-lane outputs remain dark evidence logs in the inspected routing, not ordinary card read-back. Detailed lane gate enforcement and log/report schemas are not fully retraced. The separate test producer has the identity mismatch described in [MEM-RTE-test-affirmation](#mem-rte-test-affirmation).

> "score": r.get("score"), "span": body[:max_span],
> --- `bin/m3_producer_driver.py`

## Write side

The primary trace-fed chain is host session text → bounded extractor proposal → code-shaped signal lines → History append/new project signal → reindex → later push or recall. The retained result is derived text, not the whole transcript. Safety prompts and shape filters are admission mechanisms, not guarantees of grounded or complete extraction. Human control is configuration/editing, not per-signal approval. [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound) supplies the limits and protection quote; [MEM-OBJ-memory-cards](#mem-obj-memory-cards) separates raw input from derived retention.

Direct personal promotion and base addition instead admit caller-supplied bodies. The base's explicit-user-only MCP instruction is a policy dependent on the agent; the handler checks content, not an approval credential. Existing-file initialization control remains unresolved, including manual card/corpus/skill edits. Known later indexing and transformations do not erase that uncertainty. [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission), [MEM-OBJ-memory-chunks](#mem-obj-memory-chunks).

The second trace chain is M3 candidate mining → independently retrieved chunks/support gate → novel cold-start answer plus truncated Provenance, or M2 handoff, or rejection. Definitive outcomes also reach the judged cache and affect a later Stop invocation. Dark acquisition/child-agent outcomes are not alternate knowledge-card checkpoints; they remain proposal/evaluation traces. No host conversation compaction checkpoint is established by this code. [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing), [MEM-OBJ-admission-traces](#mem-obj-admission-traces).

Maintenance chains differ: changed card → selected neighbors → M1 Evidence/diagnostic or M2 bounded region/supersession suggestion → reindex/ranking/context. Reasons survive as short notes/provenance and retained text, not a complete tested explanatory account. Decay follows age metadata; test promotion follows project correlation and has an unresolved ordinary identity seam. Usage telemetry influences curation proposals and eventual caller-directed status writes; it is not automatic learning from demonstrated task success. Each admission/recovery mechanism is kept in its record rather than inferred from software authorship or physical file I/O. [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance), [MEM-RTE-evidence-projection](#mem-rte-evidence-projection), [MEM-RTE-test-affirmation](#mem-rte-test-affirmation), [MEM-RTE-card-withdrawal](#mem-rte-card-withdrawal).

Evaluation has no supplied observed results. Runtime's smoke expected-substring/confidence oracle is separate from admission; recall_lab accepts a battery and reports strategy metrics, redirecting usage logs away from the production default. Passive stats declares lexical reference counts and disclaims causation. These artifacts cannot establish improved future capacity, exercised self-improvement or reliable source trust. SRC-1: `bin/recall_lab.py`, `bin/passive_stats.py`; [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall).

> It does NOT prove causation — see the spec's §7 attribution caveat.
> --- `bin/passive_stats.py`

## Read-back

Push is lifecycle-triggered independent supply: code selects feedback representations, project/recent snippets, drift diagnostics, fresh handoff and count-selected hint; local rules file delivers by value to an external loader. Character budgets remove most source content from the delivered artifact but preserve external files/indexes for later reads. Name-only feedback is visibility, not full behavioral-rule transmission. [RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [MEM-RTE-fresh-handoff](#mem-rte-fresh-handoff), [MEM-BAP-session-awareness](#mem-bap-session-awareness).

Pull is caller-requested: query/type/limit selectors deliver ranked snippets and metadata; detail expands indexed sections. Forked recall is a host-owned separate context frame whose return escapes; no live pointer/reference semantics keep external material automatically current. Serendipity supplies a distinct connection-oriented read. Attached bases use separate corpus scanning/tool surfaces; Core worker reads return typed IDs/scores to its client, with external applications unfrozen. A bare library storage/search affordance is not an additional deployed agent route. [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall), [MEM-RTE-serendipity-read](#mem-rte-serendipity-read), [RT-CLM-base-isolation](runtime.md#rt-clm-base-isolation), [RT-RTE-engine-worker](runtime.md#rt-rte-engine-worker).

Maintenance consumers read retained text/events to select or mutate later cards; cache consumers read symbolic outcomes to avoid repeated work. Their operational authority differs from foreground rule authority. Export reads card text and derived weights, then reads its own retained files for synthesis and manifest for later delta export. Human consumption is afforded; no automatic export-to-card read-back is established. Status/archive/obsolete text can remain available via pull and export copies, so withdrawal is consumer-specific. [MEM-RTE-evidence-projection](#mem-rte-evidence-projection), [MEM-OBJ-admission-traces](#mem-obj-admission-traces), [MEM-RTE-vault-export](#mem-rte-vault-export).

## Integration issues

- **Qualification, not wholesale runtime correction:** [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)'s later confidence path must distinguish supported-answer filing from actual ordinary test promotion. [MEM-RTE-test-affirmation](#mem-rte-test-affirmation) finds transcript-parent versus HMAC project identities at the producer join. Consequence: capacity exists for matching supplied records, but ordinary hook-filed-page test promotion is not established without a bridge. An external/deployed bridge was not frozen.
- **Detail freshness clarification:** [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall)'s “selected content” is indexed section content at the inspected detail handler. SRC-1 `bin/search_impl.py` supports this; do not promote it to guaranteed latest Markdown bytes.
- **Source-label correction:** [MEM-CMP-export-models](#mem-cmp-export-models) records default Opus topic synthesis despite the source docstring saying Sonnet. [MEM-RTE-vault-export](#mem-rte-vault-export) records optional model acceptance without fact-preservation validation; export cannot inherit card-admission guarantees.
- **Source-label correction:** `bin/curate.py` read-only/manual-move doctrine differs from its implemented --apply --yes status write; `bin/cleanup.py` human-confirmation prose differs from archive mode without a per-item confirmation dialog. [MEM-RTE-card-withdrawal](#mem-rte-card-withdrawal) keeps their actual admissions and consumer-specific withdrawal.
- **Source-label correction:** `bin/m3_autofile.py` Provenance's deterministic-overlap heading can label non-default judge scores. This limits later audit interpretation in [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)'s annotation; supported by direct `_provenance_block` and the supplied alternate-judge route.
- **Containment, not duplicate records:** [MEM-RTE-fresh-handoff](#mem-rte-fresh-handoff), [MEM-RTE-session-hints](#mem-rte-session-hints), [MEM-RTE-code-projection](#mem-rte-code-projection) are distinct parts of supplied injection; [MEM-RTE-test-affirmation](#mem-rte-test-affirmation) is a post-filing part. No replacement/possible duplicate is proposed. Card/index/event/trace objects name source substrates absent from supplied object declarations; session-awareness authority is distinct from feedback authority.
- **Unresolved included detail:** acquisition/agent lane gate and report-consumer schemas, evaluator/canary/replay internals, base refresh consistency, optional parser coverage and initial existing-file authorship remain locally limited in the coverage table. The known card/cache/dark-log distinctions stand; exhaustive efficacy, rollback, memory provenance or evaluation-feedback closure does not follow.
- **External limits:** actual flag activation, host rules/fork compliance, model/provider behavior, private corpus results and external SDK consumer use remain uninspected. No data in this run closes activation or benefit claims for the retained routes.

## Limitations and checks

Read only supplied invocation inputs and SRC-1 source material; no prior external-system characterizations consulted. Direct inspection is bounded, not a security audit or exhaustive evaluation review. Consequential positives were challenged against counterpaths: feedback name-only/cluster delivery, direct writer bypasses, lexical fallback and stale detail, separate write/rank flags, diagnostic-only maintenance, mismatched test identity, rejected-candidate cache, status versus physical archive and orphaned export copies. Findings are narrowed beside those consumers, not converted to unsupported absences.

Source HEAD was rechecked against the frozen commit and Git status remained clean. Model/effort were read from PI runtime environment and reported in the assigned worker identity. All required supplied files were read completely, including the runtime/records continuation ranges. Deterministic output validation passes; it checks form, identities, references and quotation occurrence, not analytical correctness, actual activation or benefit.
