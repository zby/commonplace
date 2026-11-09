---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "KHMS memory: trace-derived proposals, reviewed cards, correction-aware recall and separate operational ledgers at the frozen source boundary."
run-id: AAS-2026-11-08-khms-memory-c5267e800c56-01
source-identity: https://github.com/ksx-cz/khms-memory
reviewed-boundary: f739eb976dab199fd4cd64e352192cc0b112c047
---

# KHMS memory report

## Boundary and evidence

This report covers the whole shipped memory loop fixed by [boundary](boundary.md): capture, generation, per-MARK evaluation, admission, views, optional dense indexing, hook/CLI consumption, review coordination, maintenance and evaluation. The enclosing agent's own conversation management, provider internals and storage-service retention are dependencies, not KHMS mechanisms. The deployed base, private prompt extensions and real transcripts are unavailable. Source text supports implementation and doctrine, not successful operation or benefit.

All new source citations below are SRC-1 at `f739eb976dab199fd4cd64e352192cc0b112c047`. HEAD matched that pin and Git status was clean before inspection. Runtime findings are provisional; direct inspection found that generated MEMORY.md no longer embeds the bootstrap card, despite the instructions quoted in runtime. It also established narrower archive and pending-evidence behavior. No target program, test or example was executed.

### Coverage inventory

“Direct” means source slices inspected in this job; “supplied” means the runtime record supplies the account and passages. Uninspected internals remain limits, not absent mechanisms.

| Entry point or operation | Source paths and evidence basis | Records or local limit |
|---|---|---|
| Journal capture, inline candidate, bootstrap setup | Direct doctrine: `AGENTS.md`, `spec/khms-spec.md` | [MEM-OBJ-trace-material](#mem-obj-trace-material), [MEM-OBJ-card-content](#mem-obj-card-content); capture completeness and initial writer identity unresolved |
| Transcript/Git generation, generated-line admission | Direct implementation: `tools/preprocess_transcripts.py`, `tools/generated_marks.py`; supplied driver | [MEM-OBJ-trace-material](#mem-obj-trace-material), [MEM-OBJ-inbox](#mem-obj-inbox), [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) |
| Queue, resume, carry, publication, rejection | Direct ledger contract/functions: `tools/mark_ledger.py`; supplied nightly/carry route | [MEM-OBJ-mark-ledger](#mem-obj-mark-ledger), [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals); full crash interleavings not audited |
| Per-MARK packets and proposal revisions | Direct `tools/permark.py` packet builder, `tools/prompts/nightly-marks.md`; supplied evaluation | [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation), annotation below; short-prompt alternative and private rendering not fully inspected, so exact deployed guidance unresolved |
| Reviewed card import, direct file alternatives | Supplied `tools/approve_inbox.py`; direct doctrine and build refresh comments | [RT-RTE-card-admission](runtime.md#rt-rte-card-admission), [MEM-OBJ-card-content](#mem-obj-card-content); review authorization remains protocol, not authenticated per-content human consent |
| Views, belief, condensation ranking, MEMORY.md | Direct `tools/build_views.py` | [MEM-OBJ-views](#mem-obj-views), [MEM-RTE-index-bootstrap](#mem-rte-index-bootstrap) |
| CLI/library recall, optional dense service | Direct `tools/khms_search.py`, `tools/khms_recall_hybrid.py`, `tools/embed_index.py`; supplied model components | [RT-RTE-recall-return](runtime.md#rt-rte-recall-return), [MEM-OBJ-card-metadata](#mem-obj-card-metadata), [MEM-OBJ-embedding-index](#mem-obj-embedding-index); daemon internals and actual artifacts not independently inspected here |
| Unreviewed read-back bypassing card admission | Direct `tools/khms_pending.py` | [MEM-RTE-pending-evidence](#mem-rte-pending-evidence) |
| Hook dispatch and selection | Direct `claude-code/settings.hooks.json`, `tools/khms_hook.py`, `tools/khms_select.py` | [RT-RTE-recall-return](runtime.md#rt-rte-recall-return), [MEM-OBJ-hook-state](#mem-obj-hook-state); SessionStart is operational reminders, not card search |
| Risky-action precheck, manual file/topic/archive access | Direct `tools/precheck.sh`, `AGENTS.md` | [MEM-RTE-precheck-return](#mem-rte-precheck-return); explicit file/grep access is prescribed, not observed |
| Weekly, triage, validity proposal/application | Supplied `tools/weekly_synthesis.sh`, `tools/apply_triage.py`, `tools/khms_validity_daily.sh`, `tools/card_validity.py` | [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission); full judge adapters and all verdict transformations not reread, preventing independent exhaustive maintenance-quality conclusions |
| Archive, erratum and retired-claim retrieval | Direct `tools/khms_archive.py`, `tools/khms_erratum.py`, `tools/tombstone_lookup.py`, ledger archive coverage | [MEM-OBJ-tombstones](#mem-obj-tombstones), [MEM-RTE-retired-lookup](#mem-rte-retired-lookup), maintenance annotation |
| Review delivery, operational reminders | Direct `tools/khms_review_deputy.py`, SessionStart; supplied receipt machinery | [MEM-OBJ-mark-ledger](#mem-obj-mark-ledger), [MEM-OBJ-hook-state](#mem-obj-hook-state); transport-specific reviewer context unavailable |
| Export and historical restoration | Direct `tools/khms_export.sh`, `tools/khms_versions.py` interface; supplied recovery account | [MEM-RTE-export-copy](#mem-rte-export-copy), [RT-RTE-card-admission](runtime.md#rt-rte-card-admission); external copy consumer and DAV retention unobserved |
| Evaluation and measurement | Direct design/interface slices: `tools/eval/run_eval.py`, `tools/inject_cited.py`, `tools/khms_debt.py`; supplied synthetic-test and historical-experiment account | [MEM-CLM-evaluation-scope](#mem-clm-evaluation-scope); no evaluation executed, no real outcome cache acquired |
| Configuration and instruction replacement | Supplied `tools/khms_prompt.py`, release procedure | [RT-RTE-operational-change](runtime.md#rt-rte-operational-change); private authorship/admission unresolved, not erased by known automatic transformations |

## Core ideas

1. **Raw evidence, proposals and approved knowledge are different layers.** Trace selection and model interpretation can produce reusable descriptions, rationales, policies or methods, but producing a candidate does not approve it. A separately labelled read path exposes OPEN evidence before approval. See [MEM-OBJ-trace-material](#mem-obj-trace-material), [MEM-OBJ-inbox](#mem-obj-inbox), [MEM-RTE-pending-evidence](#mem-rte-pending-evidence).
2. **Semantic memory is text; graph and queue rules are symbolic.** Card bodies shape model judgments through interpretation. Statuses, correction edges and coverage decisions shape what code serves and revisits. Neither evidence labels nor computed belief authenticate truth. See [MEM-OBJ-card-content](#mem-obj-card-content), [MEM-OBJ-card-metadata](#mem-obj-card-metadata), [MEM-OBJ-mark-ledger](#mem-obj-mark-ledger).
3. **Read-back is selective and mostly shallow.** Hooks push first-line summaries selected from event text, not whole supporting evidence. Explicit recall returns ranked excerpts and limited links; opening the full card remains a separate consumer action. The generated index now avoids preloading card content. See [RT-RTE-recall-return](runtime.md#rt-rte-recall-return), [MEM-RTE-index-bootstrap](#mem-rte-index-bootstrap).
4. **Withdrawal changes ordinary visibility, not necessarily historical coverage.** Archived cards leave normal search but can still cover their original MARKs. Errata replace live wording while keeping retractions; separate tombstone lookup renders those as error or dated-value records. See [MEM-OBJ-mark-ledger](#mem-obj-mark-ledger), [MEM-OBJ-tombstones](#mem-obj-tombstones).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-trace-material
Label: Raw transcripts, journal MARKs and filtered digests

Identity/form/substrate: raw external-agent JSONL transcripts and journal Markdown reside in configured file trees; current-run traces become retained inputs when later nightly jobs consume them. Journal event text and message prose are natural language; roles, timestamps, tool names, error flags and MARK syntax are symbolic. They are not yet derived behavioral rules. Closest supplied route: [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals); this is its retained input, not a duplicate route. SRC-1: `AGENTS.md`, `tools/preprocess_transcripts.py`.

Journal capture is foreground-agent behavior requested by instructions; operator words, decisions and outcomes can supply its content. Human initiation of the session is not approval of each MARK. Exact deployed initial authorship/control is unavailable. Digests are code-produced selections of user/assistant text, tool names and short errors. Ordinary tool outputs and thinking are not carried wholesale; subagent attribution and final-report handling differ from simple prefix clipping. The raw external transcript remains the richer evidence layer where retained by deployment. Mixed user, agent and repository-change origins prevent calling all downstream material firsthand observation.

> elif bt == "tool_result":
>                 if blk.get("is_error"):
> --- `tools/preprocess_transcripts.py`

The `digest_file` branch emits at most 300 characters of an error snippet and handles text with `clip`; successful tool results are not copied by that branch. Later generator jobs consume digest/Git chunks, while per-MARK packets can recover a session-time excerpt or commit stat. This is trace preprocessing for another invocation, not evidence KHMS compacts the foreground conversation or stores hidden reasoning. Raw-to-digest loss prevents claims of complete experience capture.

#### MEM-OBJ-inbox
Label: Generated lines and candidate inbox documents

Identity/form/substrate: source-labelled generated MARK lines in `memory/ledger/generated/*.md`, model candidate documents in staging/carry/inbox, and associated reject/decision logs are retained files. Semantic findings, quotes, candidate bodies and dismissal reasons are natural language. G/M IDs, temporary labels, relation fields and publication hashes are symbolic framing. They are distinct stages, not approved K cards. No object counterpart is declared in supplied runtime; [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) and [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation) establish their producers and consumers. SRC-1: `tools/generated_marks.py`, `tools/prompts/nightly-marks.md`.

Generated-line admission is software-controlled after model authorship: shape, reference/span, non-status kind, source quote occurrence and deduplication checks decide which lines persist. Rejects can be retained separately; this checks located text, not the correctness of the interpretation.

> elif VQ.classify(rec["span"], src)[0] == "ABSENT":
>                     why = "ungrounded (span not in its source)"
> --- `tools/generated_marks.py`

Per-MARK evaluation reads these and journal MARKs, writes or replaces candidate blocks and proposes coverage/dismissal verdicts. The same night's prior candidates are retrieved into later packets; resume and carry preserve accepted progress. This gives automatic trace-fed derived material a later model consumer even before approval, but not approved-knowledge authority. Review then edits, rejects, approves or dismisses. No per-content human approval precedes generated-line or candidate creation. Proposal reasons/quotes survive in the proposal layer; no evidence establishes every reason is copied into every later hook snippet.

#### MEM-OBJ-card-content
Label: Approved K-card bodies

Identity/form/substrate: natural-language bodies in YAML-frontmatter Markdown `memory/know/K-*.md`, with archived history under `memory/archive/know/`. A source-native card may describe an event, problem/solution, fact, requirement, decision/rationale, principle, policy, method or overview. Descriptive and normative types have different templates and lineage requirements; the body is interpreted by later agents, not executed as a symbolic rule. Distinct retained object underlying [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) and [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery); runtime declares no matching object. SRC-1: `spec/khms-spec.md`, `AGENTS.md`.

> | `decision→rationale` | A decision that was made | an alternative was chosen | `DECIDED:` `WHY:` `REJECTED:` | observation |
> --- `spec/khms-spec.md`

Lineage can be journal/transcript/Git evidence, reported external findings, or other cards via derived_from. Instructions require locating quotes for observations and nonempty derivation links for derived cards. A policy/method is behavior-guiding text; a decision card can retain its WHY and rejected alternative. Later full-file readers can inspect that rationale, but first-line delivery does not ensure they see it. Whether any actual deployed card carries a substantive explanation is unavailable, not inferable from templates.

The approved import is a checked application path after prescribed review, not the only possible filesystem writer. Initialization is also prescribed through reviewed candidates, not copying seed text directly into know/. Generic caller identity does not resolve human approval. Maintenance can change metadata, archive cards and replace text with an erratum; “immutable” is qualified by these implemented operations. Subsequent search uses corrected/current files, while full reads can expose retracted wording with its marker. No weight update or increased capacity is inferred from this text persistence.

#### MEM-OBJ-card-metadata
Label: Card provenance, relations and status

Identity/form/substrate: the symbolic part of the same card files: IDs, status/type/level, evidence class, tags, source scalar, links, MARK coverage and errata metadata. Natural-language source descriptions remain interpretable provenance within that framing. This is distinct from body content because symbolic consumers apply fixed visibility, graph and coverage rules. Closest supplied referents are [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) and [RT-RTE-recall-return](runtime.md#rt-rte-recall-return), not metadata objects. SRC-1: `spec/khms-spec.md`, `tools/khms_search.py`, `tools/build_views.py`.

> DEAD = ("superseded", "refuted")
> --- `tools/khms_search.py`

Search loads know/ only, constructs successor relations from supersedes/superseded_by/refuted_by, and replaces dead hits transitively with loaded live successors. Challenged is not dead. History bypasses live replacement but does not add archived files to the loaded set. Reverse contradiction/supersession edges furnish correction pointers. A correction in prose alone is not equivalent to an edge; lint/import requirements address that gap. File edits or reviewed applications can change the metadata and hence later selection independently of textual rationale.

At build time belief is a deterministic tanh of active support minus opposition weights; it is neither learned model confidence nor proof of a card's content. Condense ranking uses age, absorption and protected categories. Its later use is view/reviewer guidance; ordinary lexical recall does not simply rank by belief. These computed numbers are symbolic access/maintenance metadata, not distributed parameters.

#### MEM-OBJ-mark-ledger
Label: MARK coverage and review ledger

Identity/form/substrate: symbolic JSONL/JSON state, queue documents, review markers and event records under `memory/ledger/` and configured shared review state; text fields retain original findings and reasons. Distinct from the knowledge cards and retrieval-use state. It supports [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) and [RT-RTE-card-admission](runtime.md#rt-rte-card-admission), neither a duplicate of it. SRC-1: `tools/mark_ledger.py`.

> memory/ledger/events.jsonl   the reviewer's decisions (dismiss / card / reopen) — the only state
>                           that cannot be derived; the LAST event of an id wins, and `reopen` really
>                           reopens (it also overrides the `marks:` links of the cards that existed when
>                           it was recorded)
> --- `tools/mark_ledger.py`

Journal M IDs and generated G IDs remain distinguishable. Sync derives coverage from retained inputs, structured marks links, pending proposals/carry and explicit events, not arbitrary prose mentions. Hash-bearing per-unit markers bind review to content. Code creates derived state; reviewer commands supply dismissal/card/reopen decisions and reasons, without authenticating a human behind the command. Subsequent jobs skip covered/proposed work, requeue unresolved work and surface counts to sessions. The state has operational authority over what gets processed, not authority to declare an assertion true.

Archive coverage deliberately persists after ordinary recall visibility is withdrawn:

> archived cover must not reopen them into the night's queue. `why` is the card's archive.jsonl line
> --- `tools/mark_ledger.py`

Floor dates, excluded status kinds and uncaptured events bound coverage. OPEN 0 means tracked work was covered/dismissed, not all knowledge was retained. Delivery of a review request does not close it: `tools/khms_review_deputy.py` sends unit descriptions through configured transport and waits for a receipt-bearing reply, but writes no reviewed marker.

#### MEM-OBJ-views
Label: Generated views and MEMORY index

Identity/form/substrate: Markdown topic/type/recent/condense/errata views and MEMORY.md regenerated from card files and registry/filesystem metadata. Headings and navigation prose are natural language; card lists, IDs, counts and belief ordering encode symbolic selections. A rebuild is software admission of projections, not new semantic approval. These views expose approved material for full agent/reviewer interpretation; they are not a second primary knowledge store. No object counterpart in runtime; their related paths are [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) and [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery). SRC-1: `tools/build_views.py`.

> "- Search before every hypothesis and every proposal: tools/recall.sh \"<query>\"."
> --- `tools/build_views.py`

The current MEMORY writer carries search instructions, active-card count, up to two recent plan paths, latest journal path and topic counts, not card IDs or bootstrap-digest body. This is a consequential difference from AGENTS/spec doctrine. Ordinary views still contain card lines and maintenance rankings. Rebuild overwrites generated material; no semantic enrichment or independent model judgment is performed by computing belief or generating an index.

#### MEM-OBJ-embedding-index
Label: Card vectors and freshness manifest

Identity/form/substrate: distributed numerical card representations stored as float16 vectors in compressed NPZ, with symbolic IDs/hashes/model-name/dimension/count metadata in JSON. The numerical vectors are not readable card summaries; later output text is fetched from card objects. Closest supplied components [RT-CMP-qwen](runtime.md#rt-cmp-qwen) and [RT-CMP-bge](runtime.md#rt-cmp-bge) are producers, not duplicate stored objects. SRC-1: `tools/embed_index.py`, `tools/khms_recall_hybrid.py`.

> texts = {c["id"]: card_text(c) for c in cards}
> --- `tools/embed_index.py:330-330`

The encoded text combines first line, tags and body, clipped to 4000 characters. Inference produces/replaces vectors for changed cards; this does not modify encoder weights. Content hashes include the model name, not a pinned weight-artifact revision, so they cannot prove freshness after an alias/artifact change. Fixedness of models remains as bounded in the supplied components. Local or daemon inference is an alternative producer; actual deployed path is unavailable.

The build merges unchanged vectors, drops IDs no longer loaded and writes NPZ before manifest. Build_views requests refresh; explicit recall can request capped warm-daemon refresh or emit stale/fallback warnings. Read-only deployments do not update shared index state. These are automatic derivation/admission rules, not human semantic approval of each vector. Cosine ranks and reciprocal-rank fusion select later delivery candidates, but cannot establish correctness or relevance. Archive exclusion propagates through load_cards to this store.

#### MEM-OBJ-tombstones
Label: Retired claims, errata and archive records

Identity/form/substrate: natural-language wrong-claim/evidence/correction/reason text in tombstone ledger/body Markdown, with TS IDs, recurrence dates and links as symbolic fields; archive JSONL records separately document movement/unlinking and reasons. These records differ from ordinary K cards and from the raw trace. Related supplied route [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) contains their writers; no matching object is declared there. SRC-1: `tools/khms_erratum.py`, `tools/khms_archive.py`, `tools/tombstone_lookup.py`.

> new_body = body[:s] + marked(a.now, a.ts) + body[e:]
> --- `tools/khms_erratum.py`

Erratum apply requires an existing declaration tied to the target card, one located occurrence and nonempty corrected wording; lint can reject the resulting card. It appends the ERRATUM block, adds frontmatter metadata and records application in the tombstone body. Explicit caller choices supply the correction; software physically applies/checks it. That does not establish a human reviewed its truth. Subsequent full-card readers can see the replacement and retracted wording, while hook/CLI renders flag errata but do not necessarily deliver the reasons. Retired-claim lookup has a separate reader below; lint also consumes retractions to reject reassertions.

Archive apply moves files and records reasons, links removed/kept and MARKs. Remaining card bodies are guarded against alteration in that operation. Archive withdrawal is not refutation: state-only or replaced cards can be removed without tombstones. Counterevidence to a universal external-only-backup account is the optional `backup_dir` branch, which copies affected files before archive mutation. This is an alternate local copy capability, not a demonstrated atomic restore.

#### MEM-OBJ-hook-state
Label: Session retrieval state and operational logs

Identity/form/substrate: session-keyed JSON files retaining injected IDs/times, recent delivery times, query hashes and bypass use; log files retain query/result/skip/error records. Symbolic metadata affects later selection without storing new semantic rules. Natural-language fail-open explanations can be surfaced to later sessions. Distinct from approved content and MARK coverage; related supplied record [RT-RTE-recall-return](runtime.md#rt-rte-recall-return). SRC-1: `tools/khms_hook.py`, `tools/khms_select.py`.

> state["injected"][kid] = t
> --- `tools/khms_select.py`

Code admits these state updates without per-content human approval. Dedup/TTL, rate windows and cooldown limit subsequent deliveries for the session. They suppress repeated text, not delete old turns from the host context. Actual V2 policy includes finite TTL, damping, high-score bypass and prompt-event dense rescue; LIVE defaults in the selector differ, and deployment overrides remain possible. SessionStart returns pending-inbox, ledger and recent fail-open information plus a static directive. Those operational records reach a later consumer but are not knowledge-card learning. Injection/citation/debt tools read logs for human/agent calibration; no automatic policy optimizer is established by those readers.

### Routes

#### MEM-RTE-index-bootstrap
Label: Generated navigation loaded into agent context

Distinct identity: unlike query-driven [RT-RTE-recall-return](runtime.md#rt-rte-recall-return), this is a generated navigation artifact with prescribed host loading, not matched-event card selection. The build owns content selection; external host/agent owns loading. SRC-1: `tools/build_views.py`, `AGENTS.md`.

- Immediate return: build writes MEMORY.md or a preview on final write failure, plus line-count/status output.
- Later read-back: instructions prescribe keeping generated MEMORY.md in subsequent agent context; it supplies search duties and paths, not card bodies.
- Delegated visibility: uninspected — host propagation to another agent's context is outside shipped build implementation.
- Selection predicate: active count, latest two plan paths by mtime, latest journal filename and grouped topic counts; no card body or card ID is selected by write_memory_md.
- Invalidation or expiry: later rebuild replaces generated contents; persistent loading is a host contract, not enforced by this writer.
- Activation or effect: affords navigation and retrieval guidance; loading and compliance are unobserved.
- Evidence limits: doctrine claims bootstrap-body inclusion, but current writer contradicts it; no deployment context trace is supplied.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> " a card reaches you through a search or the hook's injection, never from this index.",
> --- `tools/build_views.py`

#### MEM-RTE-pending-evidence
Label: Lexical return of OPEN unreviewed findings

Part of: [RT-RTE-recall-return](runtime.md#rt-rte-recall-return)

This is the alternative retained-input branch of CLI recall, not a second whole recall route. It reads ledger OPEN rows and journal findings collected from the nightly checkpoint floor. Code owns token-overlap selection; the foreground agent receives explicitly unreviewed evidence. SRC-1: `tools/khms_pending.py`; CLI invocation is supplied in the parent record.

- Immediate return: prints up to five overlapping findings with ID/location and at most 400 characters each, or an unavailable-evidence warning.
- Later read-back: accumulated findings reach later explicit recall invocations without card approval.
- Delegated visibility: uninspected — enclosing tool-result propagation is external; this helper creates no subagent.
- Selection predicate: OPEN known records plus newly collected findings not already closed; positive token intersection, descending overlap with stable ID tie-break, default limit five.
- Invalidation or expiry: closed known state removes the item; unreadable/bad checkpoint evidence yields warning while approved results can continue.
- Activation or effect: informational source evidence, not approved-knowledge admission; model reliance remains unobserved.
- Evidence limits: no semantic truth check or demonstrated behavioral benefit; this does not establish the hook pushes pending findings as cards.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> out = {k:v for k,v in known.items() if v.get('state') == 'OPEN'}
> --- `tools/khms_pending.py`

#### MEM-RTE-precheck-return
Label: Tagged policy and gotcha precheck

Part of: [RT-RTE-recall-return](runtime.md#rt-rte-recall-return)

A distinct selector/delivery branch in the parent's CLI/hook return surface, triggered explicitly with tags or automatically for recognized dangerous commands. It does not use hybrid free-text ranking. SRC-1: `tools/precheck.sh`, `tools/khms_hook.py`.

- Immediate return: matching card's first four body lines with POLICY, GOTCHA or challenged/refuted labels, or nothing-on-record output.
- Later read-back: retained policy/gotcha/dead-end material reaches a later pre-action invocation; precheck use is logged.
- Delegated visibility: uninspected — host decides which agent sees tool output or hook context.
- Selection predicate: tag intersection in know/; challenged/refuted, active gotcha, or active policy, in that precedence order. Automatic trigger uses risky-command tags and per-session/tag cooldown.
- Invalidation or expiry: subsequent file/status/tag changes alter hits; hook cooldown suppresses repetition but does not remove previously delivered context.
- Activation or effect: warnings/guidance delivered before actions; not a code veto on the risky action itself.
- Evidence limits: comment “zero LLM tokens” describes selection cost, not zero context cost when text reaches a model. No observed action prevention.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not (set(meta.get("tags") or []) & tags):
>         continue
> --- `tools/precheck.sh`

#### MEM-RTE-retired-lookup
Label: Explicit tombstone retrieval

Distinct from [RT-RTE-recall-return](runtime.md#rt-rte-recall-return): this reads a separate ledger and returns retired assertions as error/dated records rather than current K-card knowledge. Related writer is [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). SRC-1: `tools/tombstone_lookup.py`.

- Immediate return: fixed error-record or dated-value prefix, original claim, why wrong/moved, corrected truth, dates/recurrence and keys.
- Later read-back: previously retracted claims/reasons reach a later review or diagnostic reader via this CLI.
- Delegated visibility: uninspected — no shipped transport into a particular subagent established.
- Selection predicate: case-insensitive term matches against keys/claim/wrong text, --all, or --repeats with recurrence-count ordering.
- Invalidation or expiry: ledger updates alter output; no expiry specified in inspected lookup.
- Activation or effect: affords historical recognition and countermeasure review, not ordinary card assertion delivery.
- Evidence limits: operator/agent consumer role is documented; no deployed invocation or changed countermeasure observed.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> prefix = DATED_PREFIX if dated else PREFIX
> --- `tools/tombstone_lookup.py`

#### MEM-RTE-export-copy
Label: Portable file export for external readers

Distinct from [RT-RTE-recall-return](runtime.md#rt-rte-recall-return): creates a separately deployed file copy rather than answering the foreground invocation. Exporter code owns copying; deployment owner supplies target/distribution. SRC-1: `tools/khms_export.sh`.

- Immediate return: know/ file copy, optional archive/know/ and manifest with counts/build/source/bytes.
- Later read-back: documented field-device reader can search copied cards offline; supplied source does not wire a concrete external consumer implementation.
- Delegated visibility: uninspected — distribution and remote agent grants are deployment-owned.
- Selection predicate: K-file pattern in know/, plus archive only when requested; no per-card active-status parsing, despite the comment calling them active cards.
- Invalidation or expiry: rsync deletion removes files withdrawn from source on refresh; manifest is written last; no automatic remote refresh interval established.
- Activation or effect: affords portable retained knowledge; copying alone does not prove consumption or currentness on the receiver.
- Evidence limits: admission checks concern safe destination ownership/overlap/writability, not renewed semantic review of each copied card. No external consumer trace.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> rsync -a --delete --delete-excluded --include='K-[0-9][0-9][0-9][0-9][0-9].md' --exclude='*' "$KNOW/" "$TARGET/know/"
> --- `tools/khms_export.sh`

### Claims

#### MEM-CLM-evaluation-scope
Label: Retrieval evaluation is not demonstrated memory benefit

Claim/source: the production-path evaluator measures expected-card retrieval against frozen query/gold pairs and distinguishes gated regressions from open debt. Shipped rows refer to fictional examples. This is an inspectable evaluation mechanism, not an observed successful run or evidence that a retrieved card improved action. Closest supplied [RT-RTE-recall-return](runtime.md#rt-rte-recall-return) describes delivery, not this evaluator. SRC-1: `tools/eval/run_eval.py`.

> def hit(ranked, gold, k):
>     return any(g in ranked[:k] for g in gold)
> --- `tools/eval/run_eval.py`

The expected card IDs are an explicit retrieval oracle supplied by gold-file authors. They do not determine correct final task answers. Injection-use measurement joins injection times to possibly ambiguous sessions and checks ID mentions in subsequent assistant messages; an unmentioned influence is invisible. Contradiction-debt measurement reads proposals/application ledgers/card/log denominators, not just planned model work. These tools support calibration by later reviewers, not automatic evidence-responsive policy changes. SRC-1: `tools/inject_cited.py`, `tools/khms_debt.py`.

> cited = an injected K-id appears in one of the next ≤3 assistant messages
> --- `tools/inject_cited.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation)

Memory inputs are retained card text and earlier tonight candidates, selected using the MARK text, named IDs and lexical/hybrid nearest neighbors. Some cards are whole, others summaries; optional links expose graph structure. Code trims lowest-ranked cards/candidates first, then the start of the source excerpt, then journal context farthest from the MARK, while retaining the MARK itself. Packet character budget is not a guaranteed bound on total model context or an exact cap when mandatory content alone exceeds it. A fresh tool-less call has no automatic full-source reload ability. SRC-1: `tools/permark.py`.

> for _i, _o, sec, key in ranked:                     # 1. the lowest-ranked cards and candidates
> --- `tools/permark.py`

Raw journal/generated findings → selected evidence packet → model candidate/verdict → persisted proposal → later MARK packets/review → approved card → later recall is the retained trace-fed chain. The intermediate candidates already affect later proposal judgments through model interpretation. Their proposed coverage reasons are not themselves reviewer events. No independent improvement evidence follows.

#### On [RT-RTE-recall-return](runtime.md#rt-rte-recall-return)

The hook's actual pushed card material is normally first-line text limited to 100 characters, IDs, score/flags, optional umbrella and correction pointers, not whole cards or complete supporting reasons. Ordinary primary slots and character cap coexist with corrector and precheck exceptions. Corrector pointers are bounded to two, their text to 110 first-line characters, and building a failing pointer can silently drop it. This qualifies doctrine promising every correction always accompanies a served card. SRC-1: `tools/khms_select.py`.

> except Exception:
>             pass          # a pointer that cannot be built is dropped, never raised
> --- `tools/khms_select.py`

CLI differs: first line up to 110 characters, an optional rare-matched-token body line up to 150 characters, and depth-one links for configured top results. It is query-triggered retrieval; the hook is independent automatic selection from prompt/tool-event text, not a user request to deliver a specific card. SRC-1: `tools/khms_recall_hybrid.py`, `tools/khms_hook.py`.

SessionStart does not search card bodies in main: it emits review/ledger/fail-open reminders and the report directive, then returns. UserPromptSubmit searches up to 500 characters of cleaned prompt; Edit/Write selection uses a domain-filtered field composite up to 400 characters; Bash uses extracted command text with precheck before ordinary ranking. Thus a broad “hook on session start retrieves relevant cards” account is incorrect. The explicit settings example wires these events but not all implemented host branches. Code selects/deduplicates before delivery; external host continuation remains uninspected. SRC-1: `tools/khms_hook.py`, `claude-code/settings.hooks.json`.

Dense hook rescue augments lexical candidates rather than generally fusing and replacing lexical order; an optional reserved dense slot is off in shipped LIVE/V2 settings. Explicit CLI hybrid_rank instead fuses ranked channels. No global “one hybrid ranking everywhere” conclusion follows from shared search helpers. Both use live replacement for dead loaded cards. Archive is not added by --history. SRC-1: `tools/khms_select.py`, `tools/khms_recall_hybrid.py`, `tools/khms_search.py`.

#### On [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission)

Maintenance leaves distinct retained results: weekly proposals and review work, status/graph changes, explicit errata and tombstone bodies, moved archives and archive reasons. Full card bodies retain different evidence than emitted summaries. Archive movement is exclusion from normal recall, not semantic invalidation of historical coverage. Errata are content editing, not merely status changes. Direct implementation read: SRC-1 `tools/khms_erratum.py`, `tools/khms_archive.py`, `tools/mark_ledger.py`; proposal/triage/validity branches remain supplied findings rather than fresh exhaustive inspection.

#### On [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)

The natural-language policy/method/card content has informational or normative prompt force at the receiving agent, not an enforced downstream instruction hierarchy. IDs/status/cooldown have code-level force at the selector, a different consumer. Body rationale is reachable via an explicit full-card open, but current MEMORY generation does not preload it or the bootstrap-digest card. SRC-1: `tools/build_views.py`, `tools/khms_select.py`, `AGENTS.md`. See [MEM-RTE-index-bootstrap](#mem-rte-index-bootstrap) for implementation/doctrine divergence.

## Write side

Acquisition begins with instructed foreground MARKs and externally retained transcripts/Git history. There is no evidence that every experience is captured or that a human approves each journal line. Code-derived digests omit much raw content; generator models interpret those selections. Their source-labelled findings must pass generated-line shape/span checks before ledger retention. These checks are automatic content admission, separate from model authorship and file I/O. See [MEM-OBJ-trace-material](#mem-obj-trace-material), [MEM-OBJ-inbox](#mem-obj-inbox).

Per-MARK calls synthesize approve-ready candidates or propose “already carded”, “covered by”, duplicate or not-know-how verdicts. Selected previous candidates affect later proposals. Quotations/reasons remain in retained proposals; structural coverage and actual dismissal depend on later review tools. Unparsed failures, quota/deadline stops and publication conflicts retain retryable state; configurable format checking does not impose universal rejection. The supplied driver evidence also qualifies the older sweep/consolidate doctrine: current per-MARK guidance says no consolidate follows its answer. See [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation), [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals), [MEM-OBJ-mark-ledger](#mem-obj-mark-ledger). SRC-1: `tools/prompts/nightly-marks.md`.

Card admission is reviewer invocation plus software schema/lint/receipt checks. A reviewer can edit or withhold content; invoking a job is not per-content human approval. Alternate manual writers/file-tool capabilities prevent a universal review-enforcement claim. Build generates views, belief and vectors without another semantic review of each projection. Private template extensions have unresolved authorship/admission but known later model consumers. See [RT-RTE-card-admission](runtime.md#rt-rte-card-admission), [RT-RTE-operational-change](runtime.md#rt-rte-operational-change), [MEM-OBJ-views](#mem-obj-views), [MEM-OBJ-embedding-index](#mem-obj-embedding-index).

Maintenance separates proposals from explicit applications. Archive can withdraw files while preserving coverage/reasons. Erratum can replace a specific false or dated claim while preserving old wording in a marked history. Tombstone text feeds later lookup and lint, giving retraction a later admission-control consumer as well as a human/model reader. Recovery primarily relies on external file versions and reconciliation; the optional archive backup branch is an additional local-copy capability, not a universal transaction rollback. See [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission), [MEM-OBJ-tombstones](#mem-obj-tombstones). SRC-1: `tools/khms_versions.py`, `tools/khms_archive.py`.

This is an automatic trace-fed memory construction path with reviewed adoption, not demonstrated improved capacity, model training or autonomous self-improvement. Evidence/rationale templates and stored criticisms permit later reasoning; neither schema membership nor a judge label proves that criticism was content-directed, used iteratively or beneficial. Such semantic conclusions require actual retained content and consumer behavior unavailable here.

## Read-back

The main later consumers are (a) generator/evaluator models receiving selected retained evidence and earlier proposals, (b) review/maintenance sessions, (c) foreground agents receiving approved-card snippets or pending evidence, and (d) code consuming status/graph/coverage/retrieval metadata. These are different authorities and horizons. Session state can change selection in the next invocation without making a new factual assertion; reviewed K text persists across sessions/problems sharing the base. See the object records and runtime annotations above.

Automatic hook supply is event-triggered push. Explicit recall, precheck, file opens and tombstone search are reader-requested paths. Query hashes, TTL, thresholds and text budgets can prevent delivery; live-successor substitution and correction pointers can change which retained material arrives. Neither an ID pointer nor a title delivers the underlying rationale. Generated MEMORY is navigation guidance, not card preload. Exports afford another machine a file-copy reader role, but do not establish an exercised remote-consumption path. See [MEM-RTE-pending-evidence](#mem-rte-pending-evidence), [MEM-RTE-precheck-return](#mem-rte-precheck-return), [MEM-RTE-retired-lookup](#mem-rte-retired-lookup), [MEM-RTE-export-copy](#mem-rte-export-copy).

Working-context control is mainly selective introduction and isolated background calls, not editing an accumulated foreground window. Fresh generator groups and per-MARK packets resemble per-task frames: selected inputs enter, parsed outputs and files escape, and another fresh invocation reloads selected retained results. File-tool generator sessions can read beyond listed inputs under external permissions. Per-MARK tools are empty, so omitted source/reasons are not automatically reloadable inside that call. The analogy breaks at the host window: delivered text is by value, and pointers require an explicit new read rather than automatic reference/liveness handling. No foreground compaction route was established by the inspected KHMS dispatch; host compaction remains external/uninspected, not an evidenced global absence. See [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals), [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation), recall annotation.

## Integration issues

1. **Correct bootstrap delivery, not merely its label.** [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) quotes AGENTS saying MEMORY contains the bootstrap-digest body. Direct `tools/build_views.py` contradicts that doctrine. [MEM-OBJ-views](#mem-obj-views) and [MEM-RTE-index-bootstrap](#mem-rte-index-bootstrap) establish current generated search instructions/navigation without any card IDs/body. Retain the doctrine as claimed, not implemented content delivery. The external host's actual loading remains unknown.
2. **Separate SessionStart from ranked recall.** The parent [RT-RTE-recall-return](runtime.md#rt-rte-recall-return) can remain a valid container, but its event generalization must not imply every matched event searches the base. Direct `tools/khms_hook.py` returns from SessionStart after operational reminders/directive. [MEM-OBJ-hook-state](#mem-obj-hook-state) and the annotation supply the distinction; actual installation is still unknown.
3. **Narrow history/archive conclusions.** --history exposes dead cards still loaded from know/, not archived cards. `tools/khms_search.py` excludes archive entirely; `tools/mark_ledger.py` still counts archived coverage. This qualifies broad historical-return readings of [RT-RTE-recall-return](runtime.md#rt-rte-recall-return), while [MEM-OBJ-card-metadata](#mem-obj-card-metadata) and [MEM-OBJ-mark-ledger](#mem-obj-mark-ledger) preserve the different consumers.
4. **Qualify universal correction-pointer language.** Direct `tools/khms_select.py` bounds pointers and drops construction exceptions, and delivers first-line summaries. The parent recall route's correction-aware wiring remains supported, but doctrine promising every correction unconditionally is stronger than this evidence. See recall annotation and [MEM-OBJ-card-metadata](#mem-obj-card-metadata).
5. **Keep recovery alternatives explicit.** [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) and [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) correctly deny a universal transaction undo. However `tools/khms_archive.py` has an optional prewrite backup_dir copy branch despite external-version-only doctrine. [MEM-OBJ-tombstones](#mem-obj-tombstones) retains that counterexample; it does not prove deployed recovery or change the main approval receipt account.
6. **No new whole-route duplicates intended.** Pending-evidence and precheck routes declare Part of the supplied recall container; bootstrap, retired lookup and export have distinct artifacts/selectors/readers. New objects have no runtime object counterpart. Maintenance and delivery enhancements annotate supplied routes/authority rather than redeclaring them. [MEM-RTE-retired-lookup](#mem-rte-retired-lookup) overlaps maintenance outputs, not its proposal/application progression.
7. **Unresolved deployment/semantic facts.** Actual initial content authorship, per-content review decisions, private prompts, corpus/embedding artifacts, host propagation and live consumers are unavailable. Full maintenance adapters/short prompt variants were not independently inspected here beyond supplied findings. These limits prevent exhaustive semantic curation, autonomous learning, actual rationale use and improved-action conclusions, but not the supported write/read mechanisms above. [MEM-OBJ-card-content](#mem-obj-card-content), [MEM-OBJ-embedding-index](#mem-obj-embedding-index), [MEM-CLM-evaluation-scope](#mem-clm-evaluation-scope) carry the affected scopes.

## Limitations and checks

Source/method identity: prompt and required job/type/collection/worker/record inputs were read completely, including separate continuations; a truncated search result was recovered from its saved output before use. Registered Git HEAD was rechecked against the exact boundary and the checkout was clean. Added inspections all stayed in SRC-1 at that commit; no external source or prior analysis was used. The invocation's contracts, not external source instructions, governed this work. No source or artifact member was modified.

Evidence remains implementation/doctrine with bounded supplied reported-operation context. No target execution, model call, synthetic test run, deployed-corpus audit or causal experiment was performed. Deterministic validation is recorded after execution below; it checks form, references and quote occurrence, not support, completeness or benefit.

Validation: completed successfully with the required role-specific commonplace-validate command; see this invocation's shell result. No operational or causal status is inferred from that content pass.
