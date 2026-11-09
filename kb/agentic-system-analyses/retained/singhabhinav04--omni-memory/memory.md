---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Omni-Memory retention, source-binding, maintenance and later context consumers at the frozen revision."
run-id: AAS-2026-11-08-omni-memory-09378abbfe6b-01
source-identity: "https://github.com/singhabhinav04/omni-memory"
reviewed-boundary: "20f9f9ffd7ece0c6514542677ba6a549841f5536"
---

# Omni-Memory memory report

## Boundary and evidence

This report covers the shipped project-memory loop, global memory, shared imports, generated documents, dashboard operations and host context adapters within the whole-system boundary. SRC-1 is the Git source registered in [boundary](boundary.md). The checkout HEAD was rechecked as `20f9f9ffd7ece0c6514542677ba6a549841f5536`; its status was clean. Direct reads below establish implementation and static instructions, not exercised operation. No target code or tests were executed. External host transcripts, model state, installed IDE behavior and live SQLite contents were not supplied. Consequently delivery wiring can be established, but actual adoption, complete source truth and effectiveness cannot.

Memory scope follows the supplied runtime routes, with direct checks of dispatch, hooks, storage, cleanup, selection, maintenance and service handlers. It excludes neither the dashboard nor imports merely because they call a library. External host compaction policy and provider internals are outside the source boundary. Available but incompletely inspected parser, map and browser internals remain explicitly unresolved, not absent.

| Entry point / operative part | SRC-1 paths; inspection basis | Coverage and limits |
|---|---|---|
| `remember`, global remember, capture, build and Markdown scan | Direct: `omni_memory/cli.py`, `omni_memory/session_memory.py`, `omni_memory/cleanup.py`; supplied backend/context facts | [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission), [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits); annotations below. Model proposals versus code admission kept separate. Context gather/model implementation details rely on runtime, not a new direct audit. |
| SessionStart, prompt, PreCompact, SessionEnd, PostToolUse | Direct: `hooks/hooks.json`, `omni_memory/cli.py`; OpenCode template in `omni_memory/install.py` | [MEM-RTE-transcript-window](#mem-rte-transcript-window), [MEM-OBJ-observation-state](#mem-obj-observation-state), context-delivery annotation. Host event delivery and summary contents unobserved. |
| Rank/inject/recall/global/linked reads | Direct: `omni_memory/inject.py`, `omni_memory/rank.py`, `omni_memory/store.py`, `omni_memory/graph/proximity.py` | [MEM-RTE-recall-search](#mem-rte-recall-search), context-delivery annotation; linked sibling inclusion is bounded, not proof of a complete causal chain. |
| Root AGENTS.md, MEMORY.md, api-map/linkup | Direct: `omni_memory/agentsmd.py`, `omni_memory/digest.py`; generation facts supplied by runtime; direct dashboard save/read | [MEM-OBJ-agents-context](#mem-obj-agents-context), [MEM-OBJ-memory-digest](#mem-obj-memory-digest), [MEM-OBJ-generated-documents](#mem-obj-generated-documents). These are different projections, not equivalent evidence filters. |
| Refresh/check/branch sync/reanchor/conflict/duplicate handling | Direct: `omni_memory/branch.py`, `omni_memory/staleness.py`, relevant `omni_memory/store.py` methods | [MEM-RTE-anchor-maintenance](#mem-rte-anchor-maintenance). Git adapter internals and symbol propagation helpers not exhaustively inspected; no algorithm-correctness guarantee. |
| gc, forget, restore, flush, store-opening migration | Direct: `omni_memory/eviction.py`, store migration/quarantine/restore methods; flush supplied by runtime | [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits). No current quarantine inventory supplied. |
| Team shard, root snapshot, trusted explicit import | Direct: `omni_memory/team.py`, store import/export and start-hook bootstrap | [RT-RTE-shared-import](runtime.md#rt-rte-shared-import) annotation. No authenticated contributor identity or distributed deletion protocol established. |
| Dashboard reads/edits/docs/watcher | Direct: `omni_memory/serve.py` route handlers; watcher behavior supplied by runtime | [MEM-RTE-recall-search](#mem-rte-recall-search), local-edits annotation. Browser rendering and minified vendors uninspected; prevents browser-security and UI-compliance conclusions. |
| Code graph, knowledge graph and derived maps | Direct: `omni_memory/graph/build.py`, `omni_memory/graph/proximity.py`, `omni_memory/graphbuild.py`, store schema; map handlers | [MEM-OBJ-code-graph](#mem-obj-code-graph). `omni_memory/graph/extract.py`, `omni_memory/healthmap.py`, `omni_memory/systemmap.py` internals not deeply inspected; parser completeness/map fidelity unresolved. `flows` schema alone supplies no evidenced retained-flow consumer. |
| Events, read ledger, witness, savings, cache, cursor | Direct: store schema/methods, hook code, `omni_memory/savings.py`; witness conclusions supplied by runtime | [MEM-OBJ-event-log](#mem-obj-event-log), [MEM-OBJ-observation-state](#mem-obj-observation-state), [MEM-OBJ-savings](#mem-obj-savings), [RT-OBJ-inject-cache](runtime.md#rt-obj-inject-cache), [MEM-RTE-transcript-window](#mem-rte-transcript-window). Counters are not content learning by themselves. |
| Registered/exposed operations | CLI function/parser inventory, hooks file, HTTP dispatch and install template checked directly | Inspected operative interfaces are CLI, hooks, HTTP and Store methods. Mentions of MCP in comments/metadata are not wiring evidence; no MCP route is asserted. Uninspected test bodies provide no passing-run or quality result. |

## Core ideas

1. Natural-language project claims persist independently of source-access metadata. Anchors, read digests, use counts and evidence labels affect ranking, pruning and warning display. They do not make the claim a theorem of the source bytes. [MEM-OBJ-memory-text](#mem-obj-memory-text), [MEM-OBJ-memory-state](#mem-obj-memory-state).
2. Context is a lossy projection of retained state. Ranked injection clips text and suppresses duplicates; managed AGENTS.md and MEMORY.md choose different scopes and omit warning fields. Retained full text remains reachable through recall/dashboard, but supplied text need not preserve a decision's rationale. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [MEM-OBJ-agents-context](#mem-obj-agents-context), [MEM-OBJ-memory-digest](#mem-obj-memory-digest).
3. Trace-fed capture can change later agent context, while citation feedback changes the selector and retention policy. Neither demonstrates improved capacity. In particular, graduation's cited-plus-unchanged-anchor predicate is weaker than its source-native “verified by outcome” display wording. [MEM-RTE-anchor-maintenance](#mem-rte-anchor-maintenance).
4. Maintenance mostly changes accessibility, labels and lineage rather than rewriting meaning. Supersession, conflict flags, quarantine and restore preserve or remove eligibility for later reads. A source-specific check must not be generalized to every admission path. [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-text
Label: Memory claim text

SRC-1: `omni_memory/store.py`, `omni_memory/session_memory.py`. Source-native `Memory.text` is natural-language content in SQLite `.omni-memory/omni.db`; global content uses a separate user-level store. Lineage may be agent-supplied JSON, manual-source CLI, dashboard, heuristic transcript/doc text, model extraction or imported content. This is distinct from the supplied cache object and model components; no supplied object declares the retained claims themselves. The write and read routes already declared in runtime operate on these rows rather than constituting duplicate objects.

> text: str
>     kind: str = "fact"
>     branch: str = "main"
> --- `omni_memory/store.py`

The extractor asks for decisions “and why”, but the retained unit is one text field plus anchors, not separate criticism, reason or outcome objects. Reasons can survive if included in that sentence; no guaranteed rationale preservation is established. Consumers include injector, recall, dashboard and document renderers. Update consumers use fixed symbolic tests; the downstream coding agent interprets the prose as contextual knowledge/instructions, not enforced action authorization. Cross-session persistence is wired, exercised adoption uninspected. Source admission controls are described in the runtime-route annotations rather than inferred from the word manual.

#### MEM-OBJ-memory-state
Label: Memory lineage and access state

SRC-1: `omni_memory/store.py`. Distinct operative part of the SQLite memory rows from [MEM-OBJ-memory-text](#mem-obj-memory-text): symbolic JSON file/symbol lists and digests; branch/commit/source/author/evidence/status/confidence fields; supersedes pointer; use/last-used/stale/quarantine/protected/noise-exempt state. SQLite columns and JSON encodings supply localized fixed rules, not embeddings or learned weights. Store migration adds later columns. Authorship/proposal lineage is not authenticated by Git user text. No closest supplied object represents these metadata; [RT-RTE-use-check](runtime.md#rt-rte-use-check) operates on a related but separately stored witness.

> ("uses", "INTEGER DEFAULT 0"), ("last_used", "REAL"),
>                           ("quarantined_at", "REAL"), ("quarantine_reason", "TEXT"),
> --- `omni_memory/store.py`

Capture binds available file hashes, preferring a read ledger; without a read record provenance is declared, not observation-bound. Stored `supersedes_id` gives a navigable chain, but is a single pointer and duplicate retirement may process multiple rows: it should not be represented as a complete multi-parent justification graph. Ranker, staleness logic, quarantine, importer and UI consume different subsets. Their authority is eligibility/ordering/diagnostics; the foreground model does not receive all metadata.

#### MEM-OBJ-code-graph
Label: Persisted code graph

SRC-1: `omni_memory/store.py`, `omni_memory/graph/build.py`, `omni_memory/graph/proximity.py`, `omni_memory/graphbuild.py`. Symbolic SQLite `code_nodes`/`code_edges` hold source-derived symbol identities, positions, signatures, doc text and call names/relations. Embedded doc text is natural language; edge and range consumers apply fixed rules. This graph is distinct from claims and the supplied model components. Consumers are staleness propagation, proximity ranking and dashboard dossiers/maps. Rebuild admits parser output automatically; no per-node human review. Empty new extraction preserves a prior graph when one exists, so retained topology need not be a fresh complete source inventory.

> if not real and store.has_code_graph():
> --- `omni_memory/graph/build.py`

Proximity walks calls/inherits/contains in both directions, normally two hops with weights 1, 0.5 and 0.25, keyed by symbol name; name collisions can therefore soften targeting. Knowledge graph is another projection: memory/file/branch nodes and about/remembers edges, generated on dashboard request or written to `graph.json` by build. That file is not established as an agent read-back route. Parser language coverage and map internals remain uninspected; graph labels alone cannot establish semantic architecture understanding.

#### MEM-OBJ-agents-context
Label: Managed AGENTS.md context

SRC-1: `omni_memory/agentsmd.py`. Natural-language file block, derived automatically from up to 2000 active rows across branches plus static usage instructions. Distinct retained artifact from the SQLite rows and [RT-OBJ-inject-cache](runtime.md#rt-obj-inject-cache); it is the file surface of [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not a new delivery route. Inline kinds/counts are user 2, feedback 3, decision 4, gotcha 3, flow 2, endpoint 2; rows arrive recency-ordered rather than query-ranked. Full text and first file are shown, but per-row stale/evidence/external/conflict fields are not rendered.

> lines.append(f"- {m['text']}  `[{m['id']}]`{where}")
> --- `omni_memory/agentsmd.py`

The writer preserves text outside a well-formed managed marker pair, refuses an unmatched start, and atomically replaces changed output. It is automatic software admission after row writes/refresh, not approval of each rendered claim. The documented later consumer is an IDE loading root context. Force is natural-language standing guidance across sessions; loading and compliance are unobserved. “Verified memories” in the header is not a verified-only filter.

#### MEM-OBJ-memory-digest
Label: MEMORY.md digest

SRC-1: `omni_memory/digest.py`, `omni_memory/serve.py`. Natural-language Markdown at `.omni-memory/MEMORY.md`, derived from at most 2000 active rows across branches, grouped by branch and kind. Distinct from managed context: a human/agent-readable full-text knowledge base, linked by AGENTS.md and served by the dashboard, not itself always pushed by hooks. It displays inferred markers and up to three file paths, not each stale/external/conflict marker. Code admission is automatic rendering; the dashboard rejects direct saves to this generated file. Changes require row edits, then regeneration; other unsynchronized routes can leave old projections until regeneration.

> "> Agents: treat this as verified project truth. Cite `[id]`s you use. "
> --- `omni_memory/digest.py`

The source invites interpretive authority stronger than its selector warrants. A later agent can read it through the documented reference or dashboard; actual loading is uninspected. It is not a raw transcript and not a complete export, since kinds/limit and active status shape it. [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts) and [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission) produce this projection but did not declare its identity.

#### MEM-OBJ-generated-documents
Label: API map and linkup documents

SRC-1: `omni_memory/artifacts.py`, `omni_memory/serve.py`; generation evidence in [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts). These paired natural-language Markdown files persist separately at `.omni-memory/api-map.md` and `.omni-memory/linkup.md`. Their content differs, but their admission and consumers coincide: bounded repository context → model response → minimum-length check → file replacement; local dashboard can save either without that model-generation check. They are distinct from MEMORY.md and store claims, not aliases of the build route. Dashboard lists/serves their text; a model re-consuming them automatically as future memories is not established. The Markdown scan excludes the generated directory. Human/agent interpretation of a requested file is afforded; no mandatory host loading or outcome check is established. Generation reasons/model internals are not retained as separate rationale.

> if name not in ("api-map.md", "linkup.md"):
> --- `omni_memory/serve.py`

#### MEM-OBJ-observation-state
Label: Read ledger and witness state

SRC-1: `omni_memory/store.py`, `omni_memory/cli.py`; use-check behavior supported by [RT-RTE-use-check](runtime.md#rt-rte-use-check). Distinct symbolic SQLite tables: read ledger maps path to digest/time; witness maps memory/path to digest, binding kind and pin time. These are access metadata, not retained tool-result content. Read events hash current in-repo files up to 2 MB; capture consumes the ledger; injector pins emitted rows; use-check compares pins later. SessionStart clears both. They can survive individual CLI calls but are not guaranteed isolated per concurrent conversation. They are not the injection digest cache.

> s.clear_read_ledger()                  # fresh session: prior-session reads must not bind now
> --- `omni_memory/cli.py`

No new generic use route is declared: runtime already owns it. Binding confirms digest identity relative to a recorded event, not entailment of the memory or exact correspondence to host-displayed bytes. Pin failures do not stop context output.

#### MEM-OBJ-event-log
Label: Cross-session event summaries

SRC-1: `omni_memory/store.py`, `omni_memory/cli.py`. SQLite `events` stores timestamp/branch (symbolic) and a one-line natural-language summary. Capture counts, merge reconciliation and witness warnings can produce it automatically. Unlike raw host transcripts it is target-retained derived activity text. SessionStart reads the latest three events without branch filtering and prints them before the seed, except in manual mode. Scope is recent orientation/warnings, not a complete episodic transcript. No closest supplied object; delivery is already part of [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

> "SELECT ts, branch, summary FROM events ORDER BY id DESC LIMIT ?",
> --- `omni_memory/store.py`

#### MEM-OBJ-savings
Label: Savings ledger

SRC-1: `omni_memory/savings.py`, `omni_memory/store.py`. Symbolic SQLite rows retain event/branch/time, emitted IDs and estimated served/baseline/files counts. Injector records emitted rows, not all pre-render candidates. `gain` and dashboard summaries consume the ledger as telemetry; no automatic memory revision decision based on savings is established. Caller-selected tuning is a different control. This object is distinct from source claims and use counters; raw bookkeeping alone is not trace-fed content learning.

> CHARS_PER_TOKEN = 4
> _FILE_CAP = 8_000          # tokens: nobody reads more of one file to answer one question
> SEARCH_OVERHEAD = 250      # tokens: the grep/glob call + its result listing, per pull
> --- `omni_memory/savings.py`

Baseline estimates re-reading resolving source files plus fixed search overhead, not an observed no-memory counterfactual. Automatic prompt block construction records savings before identical-output suppression in the hook, so ledger pulls need not equal actually printed blocks. Thus even source-native “what memory bought” wording does not establish causal token savings or improved task performance.

### Routes

#### MEM-RTE-transcript-window
Label: Transcript window and extraction checkpoint
Part of: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)

SRC-1: `omni_memory/cli.py`, `omni_memory/session_memory.py`. This material preprocessing/checkpoint part has a distinct omission risk; it does not replace the parent capture route. Host provides JSONL path; code flattens text-only message blocks forward from a per-path line cursor persisted in SQLite meta `capture_offsets`; capture then chooses JSON/model/heuristic admission. Raw transcript lives in the host file, not a new target transcript database. Static prompts request durable concise memory, including decisions and why; only accepted claim text/anchors persist.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Flattened role/text and next line cursor to the hook; accepted counts downstream.
- Later read-back: Cursor resumes a later capture call; derived admitted claims reach future inject/recall/context. Cursor is control state, not model-readable experience.
- Delegated visibility: Model branch receives only `raw[:_LLM_WINDOW]`, with `_LLM_WINDOW = 30000`; flattening has a separate 140000-character stop threshold.
- Selection predicate: Skip already consumed lines; accept text content, not arbitrary tool payloads; stop before a next line when accumulated size reached transcript budget. Heuristic and model see different bounded representations.
- Invalidation or expiry: Start does not reset capture offsets; a completed hook saves the returned cursor. No drain loop is shown. Intra-line oversized text may exceed the flattening threshold and still advance its whole line.
- Activation or effect: Later hooks skip consumed lines, while selected derived text becomes retrieval-eligible. Full causal capture coverage is not guaranteed by the cursor.
- Evidence limits: No real transcript/run supplied. In the model branch a flattening window above 30000 characters can advance the cursor over text never sent to extraction; later hooks cannot recover that skipped tail merely by resuming at the saved line.

> _TRANSCRIPT_BUDGET = 140_000
> --- `omni_memory/cli.py`

> items = llm.extract_memories(EXTRACTION_PROMPT, raw[:_LLM_WINDOW])
> --- `omni_memory/session_memory.py`

> offsets[tpath] = total
> --- `omni_memory/cli.py`

Admission remains the parent's open capture/software cleanup, with no per-item human veto or semantic answer oracle. This narrows any claim that the persisted cursor necessarily saves *all* text past the model window for the next hook. It does not negate the parent's observation that no final drain/retry guarantee exists.

#### MEM-RTE-anchor-maintenance
Label: Anchor reconciliation and retirement

SRC-1: `omni_memory/branch.py`, `omni_memory/staleness.py`, `omni_memory/store.py`. Distinct from runtime's point-of-use diagnostic: refresh/check/branch sync drives automatic topology/staleness maintenance and trust graduation, while store admission/branch merges handle duplicate retirement and conflicts. These transformations share later eligibility/ranking consumers, but have different tests, detailed below. Proposed changes are labels, branch tags, supersedes pointers and conflict state, not new model-authored semantic corrections.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts, branch transitions or refresh snapshot; hook failures may be hidden.
- Later read-back: Updated labels/branch/status affect ranking, visible warnings and active-only reads; history exposes supersedes chains; conflicts can reach dashboard/CLI and injection markers.
- Delegated visibility: inapplicable — inspected maintenance predicates are local Python/Git/SQLite, with no model call.
- Selection predicate: Active anchored rows for staleness/reconciliation; stated rows with uses greater than zero and nonempty matching recorded hashes for graduation; duplicate/conflict tests use branch, kind, text overlap and code anchors.
- Invalidation or expiry: Source movement can revoke verified; changed topology can move merged-branch rows. Reanchor clears stale/sets commit but does not replace recorded blob hashes. Explicit resolve can retire a partner or keep both.
- Activation or effect: Fixed-rule consumers alter eligibility and trust weights; delivery of revised context is wired, external behavior and better correctness unobserved.
- Evidence limits: A citation and fresh hash are not outcome success. Conflict is a same-symbol/different-text heuristic in selected kinds, not an established contradiction. No semantic repair or quality experiment is evidenced.

> "AND evidence='stated' AND COALESCE(uses,0) > 0"))
> --- `omni_memory/staleness.py`

> if _integrity_verdict(root, shas, current) == "FRESH":
> --- `omni_memory/staleness.py`

Admission owners/tests: code automatically promotes from the above predicate, demotes verified when hashes drift/vanish, and marks stale using changed-symbol propagation or file fallback; no model or mandatory human approval. Reconcile counts whole-file drift but leaves ordinary drift staleness to recompute, flags orphaning itself. Graduation includes shared memories. Its guidance says verified is earned “by outcome + reality”, but no reference outcome is consulted here. Rank uses verified/inferred multipliers 1.2/0.8 for nonempty queries and eviction shields verified by 0.30. This is trace-fed selector/retention change from citations, not proved improved capacity.

Store insertion retires sufficiently overlapping same-branch/same-kind unprotected rows. Anchor-relaxed matches additionally shield previously cited or higher-tier rows; strict matches do not get that additional shield. Merged-branch reconciliation instead chooses cited/higher-evidence duplicates and can flag shared-symbol claims. It does not apply the same protected-row predicate, so protection must not be called a universal veto over all retirement. Explicit conflict resolution is caller-selected, can keep both, and has no semantic answer oracle. Recovery is retained superseded rows/history, not a complete versioned rollback of all edits. Every such decision uses symbolic metadata/text tests, not content-directed criticism establishing which claim is false.

#### MEM-RTE-memory-withdrawal
Label: Quarantine and restoration

SRC-1: `omni_memory/eviction.py`, `omni_memory/store.py`. Distinct from broad [RT-RTE-local-edits](runtime.md#rt-rte-local-edits): this route establishes the automatic sweep and retained consequences, including store-opening migration. CLI gc/caller request or versioned legacy sweep → noise/score rules → abandoned rows → active-read exclusion; restore returns eligibility; explicit purge deletes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate/noise/purgeable lists or changed-row counts; migration reports may be swallowed.
- Later read-back: Active-only inject/recall/doc regeneration excludes abandoned rows; restoration makes them candidates again. Quarantine reason/time remain browsable until restore/deletion. Already emitted host context is not withdrawn by a database status change.
- Delegated visibility: inapplicable — local deterministic maintenance, no model delegation.
- Selection predicate: Sweep evaluates active rows using branch dormancy, uncited staleness age, kind/confidence, evidence and citation shields; separate retro-noise predicate exempts cited/protected/noise-exempt rows. Default score threshold 0.5; explicit purge needs aged abandoned never-cited rows, default grace 90 days.
- Invalidation or expiry: Quarantine is reversible; restore sets noise_exempt to prevent the unchanged-text noise loop from immediately reversing that decision. Score-based eligibility still applies later. Hard deletion only on explicit purge/delete/flush paths, not automatic quarantine.
- Activation or effect: Code changes retrieval eligibility without per-item human approval; caller may dry-run, restore or protect. This removes suspect material from later reads but does not demonstrate corrected downstream behavior.
- Evidence limits: Noise/score are relevance/retention heuristics, not a truth oracle. Versioned store-opening noise sweep is not the identical predicate as gc; protected is not a veto against explicit deletion, flush or every merge path.

> "UPDATE memory SET status='active', quarantined_at=NULL, "
>             "quarantine_reason=NULL, noise_exempt=1 WHERE id=? AND status='abandoned'",
> --- `omni_memory/store.py`

Automatic software admission decides removal; user/agent startup merely triggers the workflow. Inputs are existing claims and use metadata; no new explanatory claim or answer reference is proposed. Guidance is fixed cleanup/eviction policy; persisted results are statuses, reasons and exemption flags. Explicit forget also archives with a timestamp; purge physically removes old eligible rows. Restoration is local, not a cross-clone revocation protocol. Generated files only reflect withdrawal after their writer runs, and old host-window copies remain outside this authority.

#### MEM-RTE-recall-search
Label: Recall and dashboard read routes

SRC-1: `omni_memory/cli.py`, `omni_memory/serve.py`, `omni_memory/store.py`. Explicit recall request → scoped store rank → full memory text/stdout; HTTP request → active memory/symbol/doc/history query → JSON/text to dashboard. Distinct from [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)'s clipped push/pull prompt block: these consumers have different selectors and payloads. No duplicate delivery route is intended.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recall prints at most 30 full-text matches plus IDs/branch/stale/file fields, or not-in-memory; service returns selected JSON/docs.
- Later read-back: Caller retrieves previously accumulated rows, source-derived graph/dossiers, history or saved documents on demand. Document reference in AGENTS.md affords a later agent reader; actual reads unobserved.
- Delegated visibility: Requesting CLI host or HTTP client receives selected parts, not an extraction model. Direct Store.get_memory capability alone does not prove an additional autonomous agent consumer.
- Selection predicate: Recall scopes current/base (or all if awareness off) and query ranks; it does not call refresh first. HTTP memories scopes similarly, with kind/query and limit 500. Dashboard global search uses text LIKE and symbol name/signature/doc, at most 25 each; it is not the same ranker. Docs use allowlisted names; history uses a supplied ID.
- Invalidation or expiry: Status changes alter future active reads; no withdrawal of copies already returned. Stored documents persist until rewritten; recall can report cached stale flags before a refresh.
- Activation or effect: Text/metadata supply informational authority for human/agent interpretation. Dashboard mutations are separately governed; read result alone neither admits an edit nor compels use.
- Evidence limits: No host/client trace; service endpoints prove wired return, not automatic loading into a model. No model-visible isolation frame, summary replacement or tool authorization gate is implemented by this route.

> query=" ".join(args.query), limit=30)
> --- `omni_memory/cli.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)

Write agency: JSON can be authored by foreground agent/caller, prose can be transformed by optional model or heuristic. Starting capture is not human per-claim approval. `remember_many` applies noise filtering then source-sensitive clamp/anchor observation/store admission; local single remember bypasses that batch cleanup. Physical SQLite write is not the admission decision. Source trust differs from author identity. Direct source checks: SRC-1 `omni_memory/session_memory.py`, `omni_memory/cleanup.py`, `omni_memory/store.py`.

> items, dropped = cleanup.filter_items(items, source=source)
> --- `omni_memory/session_memory.py`

Strict doc/heuristic paths require a named concrete anchor; other batch sources still reject fragments, metrics dumps, chatter, questions and structural noise but do not require that strict anchor predicate. Heuristic extraction strips role prefixes, accepts lines of 12–240 characters and returns at most 40 candidates. Doc scan caps files at 300, filters before stamping the current document path, then subjects results to normal admission. Model capture uses at most 30000 characters. Full reasoning and arbitrary tool payloads are not retained. [MEM-RTE-transcript-window](#mem-rte-transcript-window) qualifies checkpoint coverage. Raw-to-derived-to-later-consumer chain is host transcript text → candidate claims/anchors → SQLite → later rank/projection → host model. This is a wired trace-fed update, not evidence of model-weight training or improved capacity.

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

SRC-1 direct selection inspection: `omni_memory/inject.py`, `omni_memory/rank.py`, `omni_memory/graph/proximity.py`, `omni_memory/store.py`. Default local initial limit 8, fallback 4, global append up to 3, siblings up to 2 for each first-five pick. Those append stages mean 8 is not a hard final item cap. The 1400-character budget applies rendered rows only, clipping text at 200 characters, preserving at least the first row even if oversized. Headers/legends/closing lines are outside it. Siblings share a file or symbol and prioritize uses/verified/kind; they can still be omitted by duplicate/budget processing. Thus “chain-complete” is a bounded co-anchor heuristic, not a guarantee all reasons or constraints reach the consumer.

> for m in mems[:5]:
>             for sib in store.linked_memories(m, seen, limit=2):
> --- `omni_memory/inject.py`

Query rank scores lexical field matches, term coverage, phrase/file/proximity, recency, kind, confidence, uses and tier. Empty query without file/proximity inputs sorts by recency only, a counterexample to a universal trust-weighted ordering claim. Working-context control consists of selecting external retained text, clipping and suppressing duplicate blocks before adding to the host window. Full rows remain outside and reloadable through [MEM-RTE-recall-search](#mem-rte-recall-search). The target does not choose what the host compaction removes or preserves. PreCompact extraction is not a replacement summary/tail checkpoint; OpenCode's compacting hook pushes an independently selected memory block into host compaction context. No isolated foreground subagent frame is evidenced by this path. The optional completion subprocess is a separate, opaque execution/context boundary, not proof of a managed stack of agent frames. By-value injected text is not a dereferenceable heap handle; stored IDs require another explicit retrieval operation.

#### On [RT-RTE-local-edits](runtime.md#rt-rte-local-edits)

SRC-1: `omni_memory/cli.py`, `omni_memory/store.py`, `omni_memory/serve.py`. Explicit callers can supply/edit knowledge and trust labels; their being human is unresolved, since agent invocation is supported. Dashboard add goes directly to low-level Store.add_memory with source dashboard, and update changes text/kind/files/evidence in place. These paths do not inherit capture's source clamp/observation binding. In-place edit does not refresh blob hashes, and reanchor resets commit/stale without refreshing those hashes. `merge_memories` unions file paths and archives drops without synthesizing their text or recomputing hashes. This preserves access to the chosen claim, not guaranteed complete provenance for merged anchors.

> self.update_memory(keep_id, files=files)
> --- `omni_memory/store.py`

Rows versus regenerated projections have different clocks: local remember and build directly write digest but not an immediate managed AGENTS.md update in their inspected bodies; hooks/dashboard/refresh can later update that file. Dashboard document save accepts api-map/linkup text, rejects MEMORY.md. Treating every edit as a simultaneous update to all copies would overstate consistency. [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) owns automatic withdrawal detail, not a duplicate of the caller-edits route.

#### On [RT-RTE-shared-import](runtime.md#rt-rte-shared-import)

SRC-1: `omni_memory/store.py`, `omni_memory/team.py`. Import retains text, selected anchors/hashes, author, confidence and recognized evidence (clamped unless explicit trust). It inserts active with a new local updated time. It does not copy observed/unbound/protected/use counts/supersedes/quarantine state through the inspected INSERT; defaults therefore differ from a full store restore. Existing IDs skip even if incoming text/status changed. Team shard writer exports this Git author's active default-branch rows; source is changed to shared on import. Different clones do not automatically revoke a previously imported row when it disappears from a later shard. There is no tombstone application in this positive-ID insertion path, so local archive is not established as distributed withdrawal.

> if self.db.execute("SELECT 1 FROM memory WHERE id=?", (mid,)).fetchone():
>                 continue
> --- `omni_memory/store.py`

Shared/imported origin is visible in ranked injection, not universal projections. Local re-graduation can promote shared rows when cited and hash-fresh. The later consumer's authority therefore depends on rendering and local policy, not merely the shared source label. Explicit trusted import permits caller-selected evidence, not authenticated human review.

#### On [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts)

SRC-1: `omni_memory/cli.py`, `omni_memory/session_memory.py`, `omni_memory/artifacts.py` (writer findings supplied by runtime). Build facts and doc-scan facts enter the same text store but have different proposal origins; default inferred labeling and cleanup apply. Generated API/linkup documents remain separate file artifacts, with dashboard consumers rather than automatic row admission. Model parameters remain external/unpinned as the supplied component records state. No learned parameter change follows from persistence of these files. Build's graph.json is written before the later AI/doc passes, so it is not guaranteed a projection of all claims admitted by that build invocation.

## Write side

Admission mechanisms must be distinguished: foreground JSON proposes content but cleanup/clamp/store decide batch admission; model and heuristic prose extraction supply different candidates; direct manual-source remember and dashboard editing allow caller authority without authenticated human approval; import skips existing IDs and can lower incoming tiers; generated documents use a length gate; graph rebuild accepts parser output; maintenance changes labels/eligibility automatically. Their physical substrates and later consumers are [MEM-OBJ-memory-text](#mem-obj-memory-text) through [MEM-OBJ-savings](#mem-obj-savings), and the runtime-route annotations. The scope contains no warranted universal “all memory is verified” admission gate.

Automatic transformations include noise rejection, role-prefix stripping, source binding, duplicate retirement, topology retagging, evidence graduation/demotion, source-change warnings, generated projections and quarantine. These are concrete curation operations, not necessarily new explanatory knowledge. Rejection reasons for capture drops need not survive as individual records; quarantine does keep reason/time, while supersession keeps limited lineage. Initial user memory and imported prose can have opaque epistemic provenance even when their subsequent transformations are known. [MEM-RTE-anchor-maintenance](#mem-rte-anchor-maintenance), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal).

Trace origin is mixed: user/assistant text flattened from host transcript, optional model interpretation, heuristic line extraction, and code/document bootstrap are not interchangeable. Trace-fed durable changes include extracted claims and citation-driven ranking/retention. Raw logs alone are not the result. No prescribed semantic criticism of retained claims follows merely from their being duplicated, cited, stale or archived; inferred/stated/verified labels express source-native policy. No outcome-grounded improved capacity is demonstrated by these implementation paths.

## Read-back

Push: SessionStart selects recent events and a seed, auto prompt mode selects from prompt/current file context with de-duplication, and OpenCode compaction explicitly appends the CLI output. Managed AGENTS.md is persistent standing context for a documented external reader; it is not the same payload as ranked injection. Request-directed: inject uses query/files and graph context; recall gives fuller rows; dashboard requests access memory, graph, documents, history and metadata. Global memory is appended only if its store exists and configured allowance is positive. Shared content reaches the same local consumers after import, with rendering-specific caveats. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [MEM-RTE-recall-search](#mem-rte-recall-search).

At update consumers the metadata has fixed-rule authority over ordering, warnings, retention and branch visibility. At the external agent, natural-language content and instructions ask for trust/citation/reverification; they are not a tool-action lock. Source pins support later movement diagnostics, not a semantic answer oracle. Reason retention and later visibility are separate: full stored prose can contain reasons, while 200-character injected projections can omit them; co-anchor siblings do not guarantee reconstruction. No deployed activation or benefit is inferred from any wired read-back path. [RT-BAP-agent-context](runtime.md#rt-bap-agent-context), [RT-RTE-use-check](runtime.md#rt-rte-use-check).

## Integration issues

- Checkpoint qualification: [MEM-RTE-transcript-window](#mem-rte-transcript-window) refines [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission). The 140000 flatten threshold versus 30000 model slice permits cursor advancement past unextracted text. Do not adopt the session-memory comment that all excess is picked up next hook as a guarantee; runtime already limits final drain and should preserve this stronger omission case.
- Selection qualification: [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) includes both rank and general fallback. Direct rank inspection shows recency-only empty-query behavior without file/proximity input. Eight is the initial local limit, not final count after global/sibling append. Budgeted output cannot guarantee chain completeness.
- Path-specific authority: [MEM-RTE-anchor-maintenance](#mem-rte-anchor-maintenance), [MEM-OBJ-memory-state](#mem-obj-memory-state) and [RT-RTE-local-edits](runtime.md#rt-rte-local-edits) distinguish source-hash checks, caller labels, strict duplicate handling and merge handling. “Protected” and “verified by outcome” must not become universal semantic or retirement guarantees.
- Import/withdrawal limit: [RT-RTE-shared-import](runtime.md#rt-rte-shared-import) preserves selected fields, not full observation/use/rollback state; existing-ID skip prevents updates and shard disappearance alone does not revoke local rows. [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) is local eligibility maintenance.
- Projection consistency: [MEM-OBJ-agents-context](#mem-obj-agents-context), [MEM-OBJ-memory-digest](#mem-obj-memory-digest), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits) do not imply every mutation refreshes every file immediately. AGENTS.md and digest also omit warning fields present in injection. Existing host-window copies cannot be withdrawn by row archival.
- Savings qualification: [MEM-OBJ-savings](#mem-obj-savings) estimates baseline cost and can record auto-block constructions later suppressed. It supports bookkeeping wiring, not an observed or causal savings claim.
- Identity review: no replacement-capable duplicate declaration is intended. Transcript-window is explicitly part of runtime capture; withdrawal specializes automatic maintenance rather than redeclaring caller editing. Memory rows, file projections, events, graph, telemetry and observation tables are new operative-object identities, not aliases of runtime routes or injection cache. Recall/search is a distinct fuller-return path adjacent to runtime context delivery. Integration can retain these relations without supersession.
- Unresolved included parts: code parser fidelity, symbol-diff propagation completeness, map construction semantics, browser rendering and `flows` table's operative population/consumer remain unestablished by this bounded inspection. The coverage table names available evidence and prevented conclusions. Provider/host internals and actual state are outside SRC-1's inspected implementation; no deployment-quality claim can be supplied from them.

## Limitations and checks

Frozen identity was checked against the registered full commit; source status was clean. All citations concern SRC-1 implementation/doctrine at that revision or supplied runtime records, not prior analyses. No observed-run/causal-experiment layer is registered. Dispatch and interfaces were inspected statically; no target runtime, tests, models, doctor probes or network operations were run. The required role-scoped deterministic validator exited successfully and reported: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Form/quotation validation does not establish claim truth, host adoption or coverage completeness.

Validation: passed.
