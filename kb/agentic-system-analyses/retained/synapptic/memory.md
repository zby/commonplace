---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Synapptic memory: transcript-derived profiles, lossy rationale retention, narrative publication, benchmark selectors and relay/browser stores."
run-id: AAS-2026-10-15-synapptic-9dce97c66546-01
source-identity: https://github.com/appcuarium/synapptic
reviewed-boundary: bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f
---

# Synapptic memory report

## Boundary and evidence

The memory boundary includes transcript acquisition and filtering, observation JSON, weighted global/project profiles and history, extraction-context reuse, saved narratives, all nine output writers, detached maintenance, evaluator caches/results/verdicts, optional relay retention and browser read-back. It excludes the external assistant's actual instruction admission, live context compaction and model-provider internals. Those exclusions prevent claims about actual host compliance, complete host checkpoint forms or provider-side memory. They do not exclude the shipped drivers that persist and consume Synapptic files.

All source findings use SRC-1 at the boundary's full commit. HEAD was rechecked against that commit. Direct inspection added detail in `src/synapptic/{config,state,profile,extract,filter,synthesize,integrate,outputs,benchmark,benchmark_results,cli}.py`, the bundled prompt/skill/hook, and relay store, indexer, sessions, context, tokens, parse and browser handlers. These brace expressions are reading summaries, not source anchors; individual findings below cite actual paths. Evidence is implementation or attributed doctrine, not observed execution. The supplied runtime is provisional supporting evidence; its routes are annotated rather than redeclared. No target code, tests, examples, hooks or providers were executed.

| Entry or memory operation | Source path (SRC-1) | Coverage and limits |
|---|---|---|
| `ingest`, explicit/queued/all `extract`, transcript discovery | `src/synapptic/cli.py`; `src/synapptic/state.py` | Direct reads; [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile), [MEM-OBJ-observations](#mem-obj-observations), [MEM-OBJ-observation-envelope](#mem-obj-observation-envelope). Queue selection differs from ingest. |
| Transcript working-context reduction, scrub, profile context | `src/synapptic/filter.py`; `src/synapptic/extract.py` | Direct reads; annotation on ingest. Scrubber internals rely on supplied runtime; effectiveness unobserved. |
| Prompt customization and installed host skill | `src/synapptic/bundle/patterns/default/prompt.md`; `src/synapptic/bundle/skill/SKILL.md`; `src/synapptic/cli.py` | Prompt/skill read directly; custom loader behavior supplied by [RT-OBJ-pattern-prompt](runtime.md#rt-obj-pattern-prompt). Static instructions are guidance, not experience memory. |
| Merge, promotion, decay, pruning, history | `src/synapptic/profile.py`; `src/synapptic/state.py`; `src/synapptic/cli.py` | Direct reads; [MEM-OBJ-profile-observations](#mem-obj-profile-observations), [MEM-OBJ-profile-metadata](#mem-obj-profile-metadata), [MEM-RTE-state-maintenance](#mem-rte-state-maintenance). |
| Synthesis, explicit target-model filter | `src/synapptic/synthesize.py`; `src/synapptic/config.py` | Direct reads; [MEM-OBJ-archetype](#mem-obj-archetype), publication annotation. Default non-prescriptive thresholds are 0.3 weight and one evidence count, despite stale error text. |
| All configured output writers | `src/synapptic/outputs.py`; `src/synapptic/integrate.py` | Direct reads; publication annotation and [RT-BAP-archetype-host](runtime.md#rt-bap-archetype-host). External loading remains uninspected. |
| SessionEnd and uninstall/reset/rollback | `src/synapptic/bundle/hooks/synapptic-session-end.sh`; `src/synapptic/cli.py`; `src/synapptic/state.py` | Direct reads; hook annotation and maintenance route. Uninstall's state path differs from current configuration. |
| Benchmark, both modes, caches, verdicts, exclusions and results CLI | `src/synapptic/benchmark.py`; `src/synapptic/benchmark_results.py`; `src/synapptic/cli.py` | Direct selected implementation reads plus [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback); [MEM-OBJ-benchmark-cases](#mem-obj-benchmark-cases), [MEM-OBJ-benchmark-results](#mem-obj-benchmark-results). Judge internals/response-resume wiring otherwise supplied by runtime; no execution evidence. |
| Claude evaluator condition sessions | `src/synapptic/providers.py`; `src/synapptic/benchmark.py` | Resume ownership supplied by runtime; source search confirmed condition handles; [MEM-OBJ-claude-session](#mem-obj-claude-session). Provider checkpoint contents, compaction and eviction are uninspected. |
| Relay capture and restart metadata | `src/synapptic/relay/context.py`; `src/synapptic/relay/tokens.py`; `src/synapptic/relay/store.py`; `src/synapptic/relay/sessions.py` | Direct reads; [MEM-OBJ-request-log](#mem-obj-request-log), [MEM-OBJ-session-index](#mem-obj-session-index); forwarding/stream callbacks supplied by [RT-RTE-relay-forwarding](runtime.md#rt-rte-relay-forwarding). |
| Index CLI, browse/search/fallback, display transformation | `src/synapptic/relay/indexer.py`; `src/synapptic/relay/routers/browser.py`; `src/synapptic/relay/parse.py` | Direct reads and template-consumer search; [MEM-RTE-browser-readback](#mem-rte-browser-readback). WebSocket tailing and dashboard handler internals not exhaustively read: full live-update fidelity cannot be concluded. |

The inventory covers retained instruction content, its symbolic selectors and separate observability state. No registered tool grants an extraction model retrieval of omitted transcript material; the supplied runtime establishes text-only internal calls. External hosts may have additional tools and memory mechanisms; these are not inferred from a file writer.

## Core ideas

1. **A profile changes later extraction, not only external assistants.** High-weight text enters a later extraction prompt as already-established context; that prompt requests novelty, refinements and contradictions. Software then merges text by similarity, not by a semantic contradiction operation. This closes a trace-to-future-prompt path without proving improved accuracy. See the annotation on [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile).
2. **Evidence and rules lose different information.** Observation JSON may retain a model-supplied evidence string. New profile entries retain observation text and lineage counters, not that evidence field. Synthesis receives the resulting profile, so its request for failure-traced reasons is stronger than its guaranteed input provenance. Observation files remain separately readable by merge; the synthesis route does not reopen them. See [MEM-OBJ-observations](#mem-obj-observations) and [MEM-OBJ-profile-observations](#mem-obj-profile-observations).
3. **Instruction text and selection metadata have different authority.** Profile weights, exclusion flags and model verdicts determine software eligibility. Natural-language guards only influence a downstream model if delivered and interpreted. Excluding an entry does not immediately withdraw an older published narrative. See [MEM-OBJ-profile-metadata](#mem-obj-profile-metadata), [MEM-OBJ-archetype](#mem-obj-archetype) and [RT-CLM-target-filtering](runtime.md#rt-clm-target-filtering).
4. **The relay is a second retention loop, not demonstrated automatic learning.** It saves request displays and metrics for browser/operator consumers and restores session bookkeeping. The inspected extraction discovery scans Claude JSONL, not the relay database. Browser access to retained traces therefore does not establish a relay-to-profile update. See [MEM-RTE-browser-readback](#mem-rte-browser-readback).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-observations
Label: Per-session observation content

Source-native identity: the model-produced dictionaries under `observations` in per-session JSON. Natural-language `observation` and optional `evidence` text are derived memory, not raw transcripts; JSON is the storage container. They reside under `~/.synapptic/projects/<slug>/observations/` or `global/observations/`, using paths from `src/synapptic/config.py` and serialization in `src/synapptic/state.py` (SRC-1). The default prompt asks for a brief quote or description, not necessarily verbatim evidence. Parsing preserves extra model fields but requires only a known dimension and truthy observation, defaulting confidence. No evidence-truth gate is implemented in that loop. SRC-1, `src/synapptic/extract.py`, `src/synapptic/bundle/patterns/default/prompt.md`.

> "evidence": "brief quote or description of what supports this"
> --- `src/synapptic/bundle/patterns/default/prompt.md`

> if not obs.get("observation"):
>             continue
>
>         obs.setdefault("confidence", 0.5)
>         obs["session_id"] = session_id
>         obs["timestamp"] = now
>         valid.append(obs)
> --- `src/synapptic/extract.py`

Software admits the model-authored text after these shape checks; the human initiates processing but does not approve each item. The later standalone merge reloads these files and turns selected text/confidence into profiles. Evidence is retained here if supplied, but does not receive a distinct behavioral-authority path in the inspected synthesis consumer. Closest supplied record: [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile), a producing route rather than this stored content. No supplied object counterpart.

#### MEM-OBJ-observation-envelope
Label: Observation routing and processed markers

Source-native identity: filename/session ID, `project_slug`, `session_id`, observation dimension, confidence and extraction timestamp. Symbolic JSON fields and file existence control routing, weighting and processed-session selection. This is distinct from [MEM-OBJ-observations](#mem-obj-observations)' interpreted text, although stored in the same files. Producer: CLI tags projects, extraction adds time/session metadata, writer wraps the list. Later `find_all_observations` reads embedded routing even when the raw transcript has gone; processed discovery reads filenames, including empty results. SRC-1, `src/synapptic/state.py`, `src/synapptic/cli.py`.

> payload = {
>         "project_slug": project_slug,
>         "session_id": session_id,
>         "observations": observations,
>     }
> --- `src/synapptic/state.py`

The empty-file marker means attempted/selected processing, not a successful observation extraction. `load_observations` is a storage capability; the shipped standalone merge uses `find_all_observations`, not an inferred universal caller of that helper. Closest supplied route: [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile); no supplied envelope object counterpart.

#### MEM-OBJ-profile-observations
Label: Weighted profile observation text

Source-native identity: `dimensions.<dimension>[].observation` in global/project `profile.yaml`. Natural-language content on YAML files, with YAML history copies. Lineage: model observations become code-selected/reinforced text; longer similar text may replace the old wording. It is not a raw-trace archive or a vector store. Synthesis interprets this content; future extraction interprets selected high-weight items as established observations. SRC-1, `src/synapptic/profile.py`, `src/synapptic/state.py`, `src/synapptic/extract.py`, `src/synapptic/synthesize.py`.

For a new preference the constructor copies observation, weight, counts, times, source IDs and project origin, but not the model's separate evidence field:

> dimensions[dim].append({
>                 "observation": obs["observation"],
>                 "weight": obs.get("confidence", 0.5),
>                 "evidence_count": 1,
>                 "first_seen": now,
>                 "last_seen": now,
>                 "sources": [session_id] if session_id else [],
>                 "projects": [project] if project else [],
>             })
> --- `src/synapptic/profile.py`

An observation can itself include a reason, but that is content-dependent, not guaranteed retention of the separate evidence. Sources offer coarse lineage, not a later automatic lookup of supporting passages. Similarity merging is software curation, not warranted contradiction resolution. Closest supplied records are the producing/consuming [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile) and [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes); neither is this stored text object.

#### MEM-OBJ-profile-metadata
Label: Profile eligibility and lineage metadata

Source-native identity: `weight`, `evidence_count`, `first_seen`, `last_seen`, `sources`, `projects`, profile version/session counters, `excluded` and `model_verdicts` in the same profile/history YAML. Symbolic data, distinct from [MEM-OBJ-profile-observations](#mem-obj-profile-observations). Merge supplies confidence blending, multiplicative and time decay, sorting and deletion below threshold. Benchmark code supplies verdict/exclusion values. Software consumers use these fields to select context, skip previously merged IDs, promote entries and filter narrative inputs; they are not themselves instructions to a coding agent. SRC-1, `src/synapptic/profile.py`, `src/synapptic/cli.py`, `src/synapptic/benchmark.py`, `src/synapptic/synthesize.py`.

> # Add source session (cap at 10 most recent to prevent unbounded growth)
>             sources = existing.get("sources", [])
>             if session_id and session_id not in sources:
>                 sources.append(session_id)
>                 if len(sources) > 10:
>                     sources = sources[-10:]
>             existing["sources"] = sources
> --- `src/synapptic/profile.py`

The ten-source cap and preference pruning make current `sources` an incomplete historical merge ledger. Standalone merge derives its skip set from those fields; it cannot guarantee permanent once-only admission of old observation files. Excluded entries remain in profile data and can still appear in extraction's high-weight summary, which does not check exclusions. Weight is code-maintained confidence, not measured truth or benefit. No supplied object counterpart; overlaps the state touched by [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile) and [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback).

#### MEM-OBJ-archetype
Label: Saved narrative and published copies

Source-native identity: global/project `archetype.md` plus combined platform outputs. Natural-language user descriptions, imperative guards and known weaknesses in Markdown; Claude/Cursor wrappers and target markers are symbolic delivery metadata. Files are generated from filtered profile YAML, then saved and later reloaded by integration and benchmarks. Host copies persist across sessions until replaced or removed. Actual host precedence and interpretation remain outside the inspected implementation. SRC-1, `src/synapptic/state.py`, `src/synapptic/synthesize.py`, `src/synapptic/integrate.py`, `src/synapptic/outputs.py`.

> - Include the "why" so Claude can apply judgment in edge cases
> - Do NOT pad with generic best practices - only include guards backed by evidence
> --- `src/synapptic/synthesize.py`

This is a request to retain rationale, not proof a generated narrative contains it or that its reasons follow from observations. The synthesis path accepts nonempty returned text after fence stripping. The same saved file is used regardless of the later integration target: there is no per-target version identity or freshness link to the current profile. Closest supplied records: [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes) produces this object; [RT-BAP-archetype-host](runtime.md#rt-bap-archetype-host) supplies its external authority path. No object counterpart.

#### MEM-OBJ-benchmark-cases
Label: Retained benchmark scenarios

Source-native identity: `*_tests*.json` containing format version, guards hash and `test_cases` in `BENCHMARKS_DIR`. Mixed content: natural-language rule/scenario/criteria interpreted by respondent and judge; symbolic cache identity/version selects reuse. Model-generated from selected guards, not observed user tasks. Software admits parsed cases under benchmark generation checks; starting the benchmark is not per-case human approval. Reused cases affect later evaluator invocations, not direct production host context. SRC-1, `src/synapptic/benchmark.py`.

> cache_data = {
>         "format_version": CACHE_FORMAT_VERSION,
>         "guards_hash": guards_hash,
>         "test_cases": test_cases,
>     }
> --- `src/synapptic/benchmark.py`

Per-guard calls provide project, seed, model and guards hash. Batched calls supply only project/seed, so their cache selection does not invalidate against changed guards/model in the same way. Refresh and CLI flush options are explicit invalidation controls. Closest supplied record: [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback); this is one of its retained inputs, not a second feedback route.

#### MEM-OBJ-benchmark-results
Label: Saved evaluator results

Source-native identity: benchmark result JSON named by project/provider/model/seed/temperature/time. Natural-language scenarios, responses and explanations, where produced, accompany symbolic scores/classifications/configuration. Saved by `save_benchmark`; consumed by shipped `results list`/`results compare` via `benchmark_results.py`. Selection is provider/model/project plus filename ordering, not semantic retrieval. Profile feedback stores a reduced per-model classification separately; the inspected verdict writer does not attach the complete test or its rationale to the preference. SRC-1, `src/synapptic/benchmark.py`, `src/synapptic/benchmark_results.py`, `src/synapptic/cli.py`.

> pref["model_verdicts"][model] = classification
> --- `src/synapptic/benchmark.py`

Thus detailed result retention and actual later synthesis inputs differ. The CLI can flush result/cache files; profile verdicts are separate state. Closest supplied [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback) owns evaluation progression; no supplied object counterpart. Result schema quality and model judgment are not independent outcome evidence.

#### MEM-OBJ-claude-session
Label: Opaque resumed evaluator context

Source-native identity: `session_with` and `session_without` handles passed through `call_llm` to Claude CLI resume. Substrate: external Claude session storage, not the in-memory handle alone. Encoding of retained context and any provider-internal checkpoint form is uninspected; readable responses do not establish the full retained payload. Parameters are addressed separately by [RT-CMP-call-llm](runtime.md#rt-cmp-call-llm); this object is conversation state, not weights. Supplied [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback) establishes separate condition-session reuse across cases, and [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes) is not a consumer of these handles. SRC-1, `src/synapptic/benchmark.py`, `src/synapptic/providers.py`.

Code chooses the handles; no per-turn human admission is established. Later respondent calls can receive retained condition history through the external resume contract. Exact history, eviction, summarization and retention horizon beyond the benchmark are unknown. This prevents treating each resumed trial as an isolated fresh context or asserting any particular compaction algorithm. No supplied stored-context object counterpart.

#### MEM-OBJ-request-log
Label: Relay request displays and metrics

Source-native identity: SQLite `request_log`, including `request_messages`, `response_content`, token/count/latency fields and session IDs. Mixed form: message/response text is natural language; structured metrics and IDs have fixed software consumers. Producer is the forwarding callback via `RequestContext`; it retains a derived message representation, not the original raw request body. Ordinary text is retained in full by `summarize_messages`; tool inputs/results and thinking can also enter its representation. This path is not the scrubbed extraction context. SRC-1, `src/synapptic/relay/context.py`, `src/synapptic/relay/tokens.py`, `src/synapptic/relay/store.py`; callback wiring supplied by [RT-RTE-relay-forwarding](runtime.md#rt-rte-relay-forwarding).

> elif btype == "tool_use":
>                         parts.append(f"[tool_use: {block.get('name', '?')}({json.dumps(block.get('input', {}), ensure_ascii=False)})]")
> --- `src/synapptic/relay/tokens.py`

Store insertion is automatic software admission of host-supplied content, not model-authored profile curation or human content approval. Dashboard request detail and browser fallback later read the database. The browser display can omit repeated users and truncate user text to 5,000 characters, so visible turns are not a lossless archive. Its content informs operators; no inspected profile extractor consumes these rows. No supplied object counterpart; a retained part of the broader relay account, not a duplicate forwarding route.

#### MEM-OBJ-session-index
Label: Transcript search index

Source-native identities: SQLite `session_index`/`session_fts`. Symbolic identity, paths and time metadata govern browse/search. Indexed titles/first-user text are readable natural language with FTS software selection, not instruction content. Their source is external JSONL, not observation synthesis. Indexer extracts a first-user snippet capped at 500 characters and a fallback title capped at 120; FTS searches titles and first messages, not full conversations. SRC-1, `src/synapptic/relay/indexer.py`, `src/synapptic/relay/store.py`.

> if session_id in existing_ids:
>                 continue
> --- `src/synapptic/relay/indexer.py`

Incremental indexing skips already-indexed IDs, whereas a full scan refreshes available files; the index is not guaranteed current with later transcript edits/deletions. This object has different consumers from [MEM-OBJ-request-log](#mem-obj-request-log), even though both use SQLite. Closest supplied record: [RT-RTE-relay-forwarding](runtime.md#rt-rte-relay-forwarding); no supplied object counterpart.

#### MEM-OBJ-session-bookkeeping
Label: Relay session bookkeeping

Source-native identities: SQLite `sessions`, `ended_sessions`, and restored `SessionTracker` entries. Symbolic IDs, counters, timestamps, fingerprints and session keys, stored in SQLite and reconstructed Python objects. Lineage is relay requests and session-ended events, automatically admitted by software; it is not synthesized instruction content. Restart restoration reloads recent session metadata under a timeout. Consumer authority is session assignment and UI active/ended display, not model instruction. Grouping uses tool identity rather than a content-derived semantic session. Ended IDs persist for UI state. SRC-1, `src/synapptic/relay/sessions.py`, `src/synapptic/relay/store.py`; broader forwarding responsibility is [RT-RTE-relay-forwarding](runtime.md#rt-rte-relay-forwarding).

> tool = _extract_tool(user_agent)
>         session_key = tool
>
>         if session_key in self._sessions:
> --- `src/synapptic/relay/sessions.py`

Timeout expires active grouping, not stored transcript content. The supplied runtime's OpenAI tuple-contract defect prevents assuming identical successful admission across provider handlers. This differs from the transcript-search index and request displays by producer and consumer. No supplied object counterpart.

### Routes

#### MEM-RTE-state-maintenance
Label: Profile recovery and state withdrawal

Distinct from [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile), [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes) and [RT-RTE-session-hook](runtime.md#rt-rte-session-hook): this route changes or removes already-retained state through `rollback`, `reset` or `uninstall`, rather than producing new observations. Human invokes the command; software selects snapshots or paths and performs copying/deletion. Context is local history/configuration and existing output files. SRC-1, `src/synapptic/cli.py`, `src/synapptic/state.py`, `src/synapptic/config.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI messages after a previous-global-profile copy, confirmed state reset, or hook/skill/Claude-output removal; actual execution not observed.
- Later read-back: Restored global YAML is used by later extraction/synthesis. Already-saved narratives and non-Claude output copies can remain separately available to consumers.
- Delegated visibility: inapplicable — these commands perform local filesystem maintenance without a model invocation.
- Selection predicate: Rollback chooses `history[1]` for global; reset deletes configured `SYNAPPTIC_DIR`; uninstall scans Claude project memory and uses a separate legacy state path.
- Invalidation or expiry: Reset removes current configured state/history; rollback replaces only global profile; uninstall removes Claude archetype files and generated index references, not all platform copies.
- Activation or effect: Recovery/withdrawal changes local availability, but is not guaranteed to retract already-loaded external context or every published instruction copy.
- Evidence limits: No execution trace, all-output withdrawal transaction or provider-session erasure evidence; uninstall's state path mismatch prevents claiming it deletes current state.

Human control is explicit at reset confirmation and uninstall's optional artifact deletion; rollback requires invocation but no per-file content review. Software chooses the previous global snapshot; there is no answer oracle or model-proposed revision. Operating mode is maintenance, not experimental learning. Recovery from deletion is not supplied by `reset_all`; profile history helps only while present. In uninstall:

> synaptic_state = claude_dir / "synaptic"
> --- `src/synapptic/cli.py`

Current storage instead uses:

> SYNAPPTIC_DIR = Path.home() / ".synapptic"
> --- `src/synapptic/config.py`

This is inspected implementation tension with the bundled skill's clean-removal claim, not an observed uninstall failure. It concerns [MEM-OBJ-profile-observations](#mem-obj-profile-observations), [MEM-OBJ-profile-metadata](#mem-obj-profile-metadata) and [MEM-OBJ-archetype](#mem-obj-archetype).

#### MEM-RTE-browser-readback
Label: Operator transcript and relay read-back

Part of: [RT-RTE-relay-forwarding](runtime.md#rt-rte-relay-forwarding)

The supplied route's observability portion is expanded here as a material subroute with separate consumers. Browser user requests project/session lists, FTS search or a session detail; handler selects indexed metadata or file-scan fallback, parses matching JSONL, or reads relay database turns. Dashboard detail reads retained request bodies/metrics. Browser template fetch sites confirm a shipped UI consumer, not only storage helper affordances. SRC-1, `src/synapptic/relay/routers/browser.py`, `src/synapptic/relay/store.py`, `src/synapptic/relay/parse.py`, `src/synapptic/relay/templates/browser.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON lists, search hits or structured display turns; HTTP/UI delivery is implemented but not observed.
- Later read-back: New browser requests read accumulated transcript/index/relay state after its original production; tracker restart also reloads session bookkeeping, not instruction content.
- Delegated visibility: Human browser consumer receives display text/blocks and metadata, not necessarily complete original tool payloads or raw HTTP requests.
- Selection predicate: Explicit request query/project/session ID; FTS searches title/first-user fields with limit 50, session list limit 200. Session detail searches JSONL by ID before relay fallback.
- Invalidation or expiry: Index full/incremental choices affect freshness; file deletion prevents that file's display but does not itself remove database retention. Session tracker timeout is not content deletion.
- Activation or effect: Retained material informs operator viewing and software session grouping. No inspected automatic read-back from these displays into profile generation or host behavioral instructions.
- Evidence limits: No observed UI use, no established cross-surface transcript fidelity; provider session defect in the supplied runtime also limits OpenAI capture. Full WebSocket/dashboard behavior not exhaustively inspected.

This is requested pull, not unsolicited context injection into a model. Code performs parsing and display reductions; the operator decides what to inspect, not admission of each stored request. No answer oracle or content-revision proposal is involved. Raw source remains independently reachable through local JSONL when present; browser summaries are values, not references that the extraction model can dereference. API fallback is gated by the existence of the Claude project root, even for relay sessions:

> if not CLAUDE_PROJECTS_DIR.exists():
>         return JSONResponse({"error": "No Claude projects found"}, status_code=404)
> --- `src/synapptic/relay/routers/browser.py`

Display parsing retains compaction markers but does not implement the host's compaction or prove its summary contents. Tool-result text is capped at 2,000 characters, thinking at 5,000 and tool inputs are summarized. SRC-1, `src/synapptic/relay/parse.py`.

### Claims

#### MEM-CLM-append-only
Label: Append-only observation claim

The bundled skill describes Tier 1 observations as append-only. The writer instead opens the per-session filename with `"w"`; explicit `extract -s` can revisit a processed session. The supported contract is replaceable per-session extraction snapshots, not enforced append-only event retention. SRC-1, `src/synapptic/bundle/skill/SKILL.md`, `src/synapptic/state.py`, `src/synapptic/cli.py`.

> **Tier 1 — Observations** (append-only, per session): Raw observations extracted by LLM. Stored as JSON with embedded project metadata.
> --- `src/synapptic/bundle/skill/SKILL.md`

> with open(obs_path, "w") as f:
>         json.dump(payload, f, indent=2)
> --- `src/synapptic/state.py`

No supplied claim counterpart. Closest supplied [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile) already acknowledges explicit re-extraction; this claim qualifies the stronger doctrine, not that route's identity.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile)

**Trace chain and admission.** Raw input is external coding-session JSONL, mixing user text and assistant text. User corrections are indicators, not an independent answer key. Code drops non-conversation records/tool content/thinking, boosts lexical correction/preference/reaction turns and short user replies after long answers, then fills the approximate budget with priority and recent text. Transcript text is scrubbed at conversion. The extraction model sees that reduced data and static pattern guidance, not full tool evidence. Model/software admission creates [MEM-OBJ-observations](#mem-obj-observations) and [MEM-OBJ-observation-envelope](#mem-obj-observation-envelope), then software produces profile text and selectors. SRC-1, `src/synapptic/filter.py`, `src/synapptic/extract.py`, `src/synapptic/cli.py`.

**Working-context control.** Trigger is extraction of a selected session. Selector is Python, not a model deciding what to forget. Default 50,000 approximate tokens means 200,000 text characters, excluding template/profile formatting; proportional priority truncation has a minimum share, so it is not a strict total-model-window bound. The extraction call is a separate context frame: selected input goes in and only observation output escapes into local state. It does not pop or compact the foreground host window. Omitted raw material stays in the external file if not independently deleted, but the extractor has no supplied tool to reload it. This resembles isolated computation with a returned value, not a pointer-backed store accessible to the model. SRC-1, `src/synapptic/filter.py`, `src/synapptic/config.py`; text-only call boundary is supplied by runtime.

**Later profile read-back.** Code loads profiles once for extraction context, combines global then project entries, and supplies them only if the global profile has dimensions. The summary selects weight at least 0.7, first eight per dimension. Because concatenation is global-first, this is not necessarily the highest eight of a globally re-sorted combined dimension. Selection has a count/weight bound, not a total text/token budget. Excluded/model-verdict flags are not checked by this summary. The model receives selected text, weights and counts as prompt context; it does not autonomously request it. This is automatic supply at the extraction trigger, not independent unsolicited injection or user-query semantic retrieval. SRC-1, `src/synapptic/cli.py`, `src/synapptic/extract.py`.

> top = [p for p in prefs if p.get("weight", 0) >= 0.7]
> --- `src/synapptic/extract.py`

> - Contradictions to existing patterns (flag these explicitly with confidence reflecting how strong the contradiction is)
> --- `src/synapptic/extract.py`

**Curation and survival.** Merge matches within a dimension at SequenceMatcher threshold 0.7, increments evidence count, blends old pre-decay weight 0.7 with confidence 0.3, caps sources at ten and can retain the longer wording.

> existing["weight"] = min(
>                 1.0,
>                 old_weight * 0.7 + obs.get("confidence", 0.5) * 0.3,
>             )
> --- `src/synapptic/profile.py`

 Unmatched entries get confidence as initial weight. Unreinforced entries undergo per-merge decay and time half-life, then entries below 0.1 are removed from current dimensions; the word “archive” does not denote a dedicated archive object here. Standalone merge defaults to 0.95, whereas ordinary ingest uses the function default 0.98. Promotion searches mixed dimensions across at least two projects with text-similarity candidate grouping; the configuration includes `ai_failures` and `guards` as mixed, contrary to the skill's project-only labels. Neither operation checks whether two similar sentences assert incompatible claims. SRC-1, `src/synapptic/profile.py`, `src/synapptic/config.py`, `src/synapptic/cli.py`, `src/synapptic/bundle/skill/SKILL.md`.

**Known limits of retained reasons.** Separate extraction evidence is not copied by the new-profile constructor; source IDs permit coarse provenance but no automatic synthesis lookup. Whole YAML history preserves snapshots of what was retained, not the omitted raw evidence. Claiming semantic conflict resolution or guaranteed evidence-grounded guards would exceed these consumers. The source-fed update is behavior-shaping through later prompt content; reliable learning or improvement remains unestablished.

#### On [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes)

**Eligibility and budget.** The synthesis consumer receives filtered profile YAML, not raw transcript or observation-file evidence. `guards`/`ai_failures` require weight at least 0.5; other dimensions use configured weight 0.3 and evidence count one. Global exclusion is honored; an explicit target model additionally rejects its `backfire`/`redundant` verdicts. The output prompt asks for 800–1500 words but no inspected word-count gate enforces it. There is no hard selection cap on the remaining profile entries. SRC-1, `src/synapptic/synthesize.py`, `src/synapptic/config.py`.

> NARRATIVE_MIN_WEIGHT = 0.3  # include in archetype above this
> NARRATIVE_MIN_EVIDENCE = 1  # weight is the primary quality filter
> --- `src/synapptic/config.py`

**Write agency and rationale.** Software chooses eligible data; the model authors narrative/rules/why text. Code accepts truthy output without per-document human review or independent grounding. Persisted natural-language reasons may guide host judgment, but the requested reason's presence and correctness are not demonstrated by a retained generated example. Evidence-count/weight filtering is not a grounding check. The source requests formulated prescriptions; the supplied runtime's separate theory-condition limits remain applicable rather than being strengthened by persistence alone.

**Delivery details.** Integration reloads saved global/project narratives and concatenates them. Claude writes `user_archetype.md` and inserts/moves its reference near the top of an existing `MEMORY.md`; it does not create a missing index. Cursor uses `.cursor/rules/synapptic.mdc` with `alwaysApply: true`. Copilot, Gemini and Codex update marked sections of `.github/copilot-instructions.md`, `.gemini/styleguide.md` and `AGENTS.md`. Windsurf, Cline, Aider and Continue replace `.windsurfrules`, `.clinerules`, `CONVENTIONS.md` and `.continuerules` respectively. Destination discovery and configured target control publication; current task content does not select narrative passages. These paths afford host loading, not proof every host reads them. SRC-1, `src/synapptic/outputs.py`, `src/synapptic/integrate.py`; authority is [RT-BAP-archetype-host](runtime.md#rt-bap-archetype-host).

**Withdrawal lag.** No qualifying synthesis or failed model response leaves an older saved narrative rather than deleting it. Profile exclusion, pruning or rollback therefore does not directly retract that narrative or already-published copies. Target-specific integration counts do not edit saved text, as [RT-CLM-target-filtering](runtime.md#rt-clm-target-filtering) establishes. Atomic per-file writes do not provide lineage-linked freshness or a multi-output transaction.

#### On [RT-RTE-session-hook](runtime.md#rt-rte-session-hook)

The retained chain is explicit-session extraction JSON → standalone merge profile/history → project/global saved archetype. It does not publish external copies. This directly contradicts the bundled skill's claim that the hook runs full ingest after every session. The shell also skips concurrent work without enqueuing retry, so the skill's no-loss/catch-up claim is not a demonstrated guarantee. Source-supported alternative: explicit extraction can revisit the skipped session later; that capability does not establish automatic catch-up. SRC-1, `src/synapptic/bundle/hooks/synapptic-session-end.sh`, `src/synapptic/bundle/skill/SKILL.md`, `src/synapptic/cli.py`.

> A hook runs `synapptic ingest` in the background after every session (fully detached, zero exit lag). PID-locked to prevent stacking. If it fails, the next session's hook catches up — nothing is permanently lost.
> --- `src/synapptic/bundle/skill/SKILL.md`

The installed hook's source passage in the supplied route establishes the differing commands; it need not be repeated here. Automatic admission remains software/model-controlled, not later human confirmation.

#### On [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback)

Memory inputs include saved narrative plus profile guard text, generated/cached scenarios and, in per-guard Claude runs, opaque condition sessions. Outputs include detailed result JSON and reduced profile selectors. Code automatically writes non-unclear/non-untestable classifications into `model_verdicts`; separate confirmations control global exclusion reasons. Human refusal at those prompts does not undo the prior verdict write. `include_guards` deletes `excluded`, not `model_verdicts`, so re-inclusion can still leave a guard filtered for an explicit target model. SRC-1, `src/synapptic/benchmark.py`, `src/synapptic/cli.py`.

> del all_excluded[idx]["excluded"]
> --- `src/synapptic/benchmark.py`

Matching is textual/prefix similarity; verdicts are not immutable guard identities tied to a specific narrative version. Feedback records classifications rather than a content-directed criticism with preserved blame and revised explanatory account. The detailed test record may survive in benchmark files, but the later `filter_for_narrative` consumer reads profile flags/verdicts, not those reasons. This is trace-fed changed reliance through selector metadata; it does not establish improved future action or a complete theory-criticism cycle.

Cache differences matter: per-guard cache keys include guard hash/model, whereas batched mode's project/seed-only calls can reuse cases across changed profile content. Both are wired reuse, not independent replication. The runtime's comparison distinction remains: individual-guard removal/addition versus full archetype/no archetype. Saved per-rule results from the latter do not identify each rule's individual effect. Source passages for that comparison and its judgments are supplied by the runtime; memory inspection does not upgrade the causal status.

## Write side

The principal chain is external user/assistant traces → code-filtered/scrubbed text → model-authored per-session observations → code-routed weighted profile → model-authored narrative → software-published host files. Acquisition and physical I/O are separate from admission: users launch or install the machinery, models propose interpretation/wording, and software accepts most content without per-item approval. Raw logs are external inputs; observation JSON is already derived, as [MEM-OBJ-observations](#mem-obj-observations) records. The append-only label is qualified in [MEM-CLM-append-only](#mem-clm-append-only).

Maintenance changes meaning and eligibility in different ways. Text matching/rewording, dimension routing and cross-project promotion curate content; weights/decay/pruning curate survival; benchmark feedback curates eligibility. The profile constructor loses separately supplied evidence, while narrative rationale is requested again from the reduced input. These are known transformations despite unobserved initial user history and opaque model processing. Detailed profile and benchmark annotations carry the exact consumers and admission checks.

Rejection/withdrawal is not one operation. Extraction drops malformed/unknown-dimension/empty entries; provider or JSON failure can still leave an empty processed marker. Merge removes low-weight entries from the current profile, leaving prior observation files/history distinct. Exclusion preserves the entry with a reason flag. Re-inclusion clears that flag but not per-model verdicts. Rollback restores only a global profile. Reset removes configured internal state, not all independently published files. Uninstall removes Claude outputs and machinery but its optional state deletion uses a different path. See [MEM-RTE-state-maintenance](#mem-rte-state-maintenance) and the ingest/benchmark/publication annotations.

The optional relay independently converts current host requests into stored display bodies, responses and metrics, and derives index snippets from JSONL. Those writes have software admission and operator later readers, not demonstrated automatic instruction production. The browser also represents externally emitted compaction markers. That is evidence of a marker parser, not a Synapptic compactor or a guarantee about the host's retained summary. No alternative provider checkpoint form was available to inspect; [MEM-OBJ-claude-session](#mem-obj-claude-session) retains that uncertainty rather than equating visible responses with the whole state.

## Read-back

| Retained input → later consumer | Trigger/selector and budget | Delivery and actual authority |
|---|---|---|
| Observation JSON → standalone merge | `merge` scans files, skips source IDs found in current profiles, ignores empty lists; no semantic evidence retrieval | Python dictionaries; software controls profile updates. Source cap/pruning prevents a permanent complete merge ledger. |
| Profile text/metadata → extraction | Selected session, global-profile gate, combined global-first dimensions, weight ≥0.7 and first eight/dimension | Automatic prompt supply tells model what is established and requests novel/refined observations; no observed changed response. |
| Profile text/metadata → synthesis | CLI/hook; exclusions/verdicts/thresholds; no hard total input cap | Filtered YAML in a separate model invocation; output prose/rules is admitted without a grounding gate. |
| Saved narratives → integration | Ingest integration, configured targets and discovered project paths | Combined Markdown into host-specific files; selection is destination-based, not task-targeted. Host loading/compliance remains external. |
| Narratives/profile/cases → evaluators | Explicit benchmark, mode/seed/cache/guard selection | Model prompts and possibly resumed condition context; model judgments, not live host task outcomes. |
| Results/verdicts → operator or synthesis | Results CLI provider/model/project selection; target-model synthesis reads only reduced profile verdicts | Operator report or symbolic eligibility decision; detailed rationale is not automatically read by synthesis. |
| History → rollback/diff | Explicit maintenance; previous global snapshot or compared snapshots | Files/copied YAML and human display; profile recovery is not output rollback. |
| Relay/index/JSONL → browser, dashboard, tracker | Explicit HTTP/UI requests, FTS metadata selection, restart/timeout | Display and bookkeeping, not demonstrated agent-context injection; detailed caps and fallback limits in browser route. |

The first six rows are grounded by the objects and annotations above (SRC-1, `src/synapptic/cli.py`, `src/synapptic/extract.py`, `src/synapptic/synthesize.py`, `src/synapptic/integrate.py`, `src/synapptic/benchmark.py`, `src/synapptic/benchmark_results.py`). The remaining rows are [MEM-RTE-state-maintenance](#mem-rte-state-maintenance) and [MEM-RTE-browser-readback](#mem-rte-browser-readback). An exposed load/save helper alone is not counted as another later-consumer route.

## Integration issues

- **No correction to supplied runtime facts is required.** Direct reads support its distinctions between full ingest and hook maintenance, saved-text publication and computed filtering, empty processed markers, per-file atomicity and whole-pipeline recovery. The current report adds missing stored parts rather than redeclaring those route identities.
- **No intended duplicate declarations.** Stored objects have no supplied object counterparts; their closest producing/consuming routes are named in each declaration. [MEM-RTE-browser-readback](#mem-rte-browser-readback) is explicitly part of the observability portion of [RT-RTE-relay-forwarding](runtime.md#rt-rte-relay-forwarding). [MEM-RTE-state-maintenance](#mem-rte-state-maintenance) spans rollback/reset/uninstall, distinct from production or feedback routes. Reconciliation should preserve these distinct consumers, not equate content, selectors and observability logs merely because they share files or SQLite.
- **Rationale loss constrains guard-grounding conclusions.** [MEM-OBJ-observations](#mem-obj-observations) may retain separate evidence; [MEM-OBJ-profile-observations](#mem-obj-profile-observations) drops it at new-entry construction. [MEM-OBJ-archetype](#mem-obj-archetype) asks for why text without reopening observation evidence. Whether actual generated observations embed sufficient reasons in their text is unresolved without generated artifacts. Consequence: requested evidence-grounded guard rationale is not guaranteed by the storage chain.
- **Curation is not semantic conflict resolution.** Similarity reinforcement/longer-text replacement can conflate assertions, and the profile-aware contradiction request has no distinct code-level contradiction field/decision. Source basis is `src/synapptic/profile.py` and `src/synapptic/extract.py` (SRC-1), recorded in the ingest annotation and [MEM-OBJ-profile-metadata](#mem-obj-profile-metadata). Without examples, the frequency and practical severity are unresolved; no quantified failure claim is made.
- **Withdrawal and identity are incomplete across stages.** [MEM-RTE-state-maintenance](#mem-rte-state-maintenance) retains uninstall's legacy path mismatch. [MEM-OBJ-archetype](#mem-obj-archetype) can outlive eligibility changes; no current-profile freshness binding is checked. [MEM-OBJ-profile-metadata](#mem-obj-profile-metadata)'s capped sources also cannot guarantee once-only remerge. Consequence: exclusion, rollback, reset and uninstall cannot be treated as equivalent all-consumer retractions.
- **Doctrine differs from code beyond the supplied target-filtering claim.** [MEM-CLM-append-only](#mem-clm-append-only) qualifies observation retention. Hook annotation qualifies full-ingest/every-session/catch-up claims. `ai_failures`/`guards` are mixed promotion dimensions in `src/synapptic/config.py`, despite project-only labels in the bundled skill. Configuration gives ordinary narrative thresholds 0.3/one, despite stricter stale error text in `src/synapptic/synthesize.py` (SRC-1). These are source qualifications, not disputes with supplied runtime values.
- **Evaluator state requires separate identities and limits.** [MEM-OBJ-benchmark-cases](#mem-obj-benchmark-cases) has mode-dependent cache invalidation; [MEM-OBJ-benchmark-results](#mem-obj-benchmark-results) is not the reduced profile verdict; [MEM-OBJ-claude-session](#mem-obj-claude-session) has opaque contents. Consequence: neither repeat-cache use nor a readable result establishes independent context isolation, full rationale consumption or guard-specific causality in batched mode.
- **Relay coverage remains bounded.** [MEM-OBJ-request-log](#mem-obj-request-log), [MEM-OBJ-session-index](#mem-obj-session-index) and [MEM-RTE-browser-readback](#mem-rte-browser-readback) establish storage and shipped operator readers. Complete WebSocket/dashboard fidelity, actual OpenAI persistence and provider checkpoint contents remain uninspected/unobserved. The supplied OpenAI return-contract mismatch and the source's early Claude-root check specifically prevent universal fallback claims. No evidence here establishes a relay-database-to-profile extractor.

## Limitations and checks

All source conclusions are code-grounded or attributed doctrine under SRC-1, not observed operation. No generated profile, narrative, real benchmark result or deployment trace was supplied. Therefore accuracy, confidentiality in practice, host activation, learning benefit and successful self-improvement are not established. Trace-fed prompt modification is wired; that fact is retained independently of those unestablished benefits.

The registered repository identity and full HEAD were rechecked; no source or method file was changed. Available unread supporting code is reported as uninspected detail, not an access gap or evidenced absence. No new source identity, historical analysis or live web source was used. Supplied member IDs are retained unchanged; all new IDs use the memory prefix. Deterministic validation: the required `commonplace-run validate-output` check passed (member content only; invocation residue not checked). This establishes form and quotation occurrence, not claim support or job acceptance.
