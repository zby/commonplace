---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LACP memory: separate native keyed entries, host handoffs and SMS, trace-derived research graph, hybrid retrieval and incomplete withdrawal propagation."
run-id: AAS-2026-10-14-lacp-91efd16f7a35-01
source-identity: https://github.com/0xNyk/lacp
reviewed-boundary: e31f134b689afd6a71d94b0420682d1f528d6fa1
---

# LACP memory report

## Boundary and evidence

This member covers retained material and working-context controls inside the supplied whole-system [boundary](boundary.md#boundary-and-evidence). SRC-1 is the repository at the frontmatter commit. Direct reads below establish implementation or doctrine/design, not deployed operation. Private histories, installed hooks, vaults, models, MCP services and live indexes were not supplied. They prevent conclusions about actual content, activation, retrieval quality or improvement. External host compaction and external indexer internals remain outside the frozen source, while their shipped adapters remain included.

The memory boundary is broader than the native memory tools. It includes native conversation restore, keyed entries, host handoffs, SMS episodes/self-model, per-turn extraction, daily trace extraction, research synchronization, promotion/maintenance, hybrid indexing/querying, learning-event capture/advisory retrieval, and source/configuration revisions described by runtime. These are separate substrates and channels, not one automatically coherent memory hierarchy. Static instructions and scaffolds are included as context/admission surfaces, but are not read-back merely because they can be read.

### Coverage inventory

“Direct” means source passages inspected in this job; “supplied” means runtime findings rather than new inspection. Unresolved rows are included responsibilities, not exclusions or claimed absences.

| Entry point or operation | Source path and inspection | Records or missing facts and prevented conclusion |
|---|---|---|
| Native save/resume, clear, result/skill truncation and isolated host delegation | Direct `tui/sessions.py`; supplied `tui/repl.py`, `tui/providers.py`, skill/delegate handlers in `tui/tools.py` | [RT-OBJ-messages](runtime.md#rt-obj-messages), [RT-RTE-native-turn](runtime.md#rt-rte-native-turn), [RT-RTE-host-launch](runtime.md#rt-rte-host-launch), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load); annotations below |
| Registered memory read/write/search/list | Direct `tui/tools.py` | [MEM-OBJ-memory-entries](#mem-obj-memory-entries), [MEM-RTE-keyed-memory](#mem-rte-keyed-memory) |
| Stop-produced handoff; startup/clear/compact injection; handoff show/list/clean | Direct `hooks/stop_quality_gate.py`, `hooks/session_start.py`, `bin/lacp-handoff`; supplied early-stop sequencing | [MEM-OBJ-handoff-artifact](#mem-obj-handoff-artifact), [MEM-RTE-session-memory](#mem-rte-session-memory), [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) |
| Plugin event map and separate startup copy | Direct `plugin/hooks/hooks.json`; bounded search in `plugin/hooks/scripts/session_start.py`; supplied stop-copy parity | Same session route; plugin does not register extraction in inspected event map; deployed installation unresolved |
| SMS write/read, narrative/self-model operations, epoch synthesis | Direct `hooks/self_memory_system.py`, `bin/lacp-sms`, SMS stage of `bin/lacp-brain-expand`; direct episode displays in `bin/lacp-brain` | [MEM-OBJ-episodes](#mem-obj-episodes), [MEM-OBJ-self-model](#mem-obj-self-model), [MEM-OBJ-sms-narrative](#mem-obj-sms-narrative), [MEM-OBJ-agent-narrative](#mem-obj-agent-narrative), [MEM-OBJ-epochs](#mem-obj-epochs), [MEM-RTE-session-memory](#mem-rte-session-memory), [MEM-RTE-epoch-synthesis](#mem-rte-epoch-synthesis) |
| Per-turn extraction and staging→inbox→registry | Direct `hooks/extract_memories.py`, staging/sync stages in `bin/lacp-brain-expand`, admission/persistence slices of `automation/scripts/sync_research_knowledge.py` | [MEM-OBJ-research-memory](#mem-obj-research-memory), [MEM-RTE-trace-research](#mem-rte-trace-research); actual hook registration of extraction unresolved |
| Shared daily memory and optional promotion into durable files | Direct rendering/candidate slices of `automation/scripts/extract_shared_memory.py`, apply slice and bounded search of `automation/scripts/suggest_memory_promotions.py`, complete `automation/scripts/run_memory_pipeline.sh` | [MEM-RTE-daily-promotion](#mem-rte-daily-promotion); raw history parsing/redaction and all score heuristics not fully inspected, preventing completeness/privacy/semantic-validity guarantees |
| Graph semantic merging, prediction-error admission, quarantine/fallback publication | Direct admission/output slices of `automation/scripts/sync_research_knowledge.py`; bounded searches for graph operations | Research route; embedding helper and prediction-error classifier bodies not inspected, preventing semantic contradiction or complete provenance claims |
| Hybrid index build/query and shipped evaluator callers | Direct `automation/scripts/build_memory_rag_index.py` build portion, complete `automation/scripts/query_memory_rag.py`, collector in `automation/scripts/memory_rag_lib.py`, probe slice in `automation/scripts/active_recall_probes.py`; bounded search of `automation/scripts/benchmark_memory_retrieval.py` | [MEM-OBJ-hybrid-index](#mem-obj-hybrid-index), [MEM-CMP-embedding-service](#mem-cmp-embedding-service), [MEM-RTE-hybrid-retrieval](#mem-rte-hybrid-retrieval); evaluator later consumer established, foreground delivery only afforded through CLI |
| Consolidation/pruning/probe feedback and MEMORY.md truncation | Direct `automation/scripts/memory_consolidation.py` decision/apply portions, complete `automation/scripts/memory_index_guard.py`, driver stages | [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance); full strength/clustering helpers not inspected; no proven semantic synthesis or durable supersession |
| Direct resolution, title rename, inbox archival, promotion and acquisition | Direct resolution/apply in `bin/lacp-brain-resolve`, title rename in `automation/scripts/curate_titles.py`, archive main in `automation/scripts/archive_inbox.py`; bounded searches in `bin/lacp-brain-ingest`, `bin/lacp-brain-promote`, `bin/lacp-curate` | Maintenance route. Delegate extraction bodies, destination policies and complete ingestion-quality enforcement remain uninspected; no claim of validated ingest or faithful source capture |
| Other offline transformations: session mirroring, article/repo/code sync, research consolidation, gap/link proposals, review queue, generated MCP memory, quarantine hygiene and threshold recalibration | Inventoried through boundary, driver reads and bounded searches: `automation/scripts/sync_agent_session_history.py`, `automation/scripts/sync_article_memory.py`, `automation/scripts/sync_repo_knowledge.py`, `automation/scripts/consolidate_research.py`, `automation/scripts/generate_review_queue.py`, `automation/scripts/render_mcp_memory.py`, `automation/scripts/prune_agent_quarantine.py`, `automation/scripts/run_weekly_maintenance.sh` | Included but bodies not fully inspected. Exact output retention, admission, lineage, rollback and later consumers remain unresolved individually; prevents an exhaustive maintenance-loop or cross-store consistency conclusion |
| Cross-CLI capture/query/evaluate/promote/rollback | Direct record slice of `bin/lacp-learn-capture`, query slice of `bin/lacp-learn-retrieve`; supplied promotion/rollback; bounded search for consumers | [MEM-OBJ-learning-events](#mem-obj-learning-events), [MEM-RTE-learning-hints](#mem-rte-learning-hints), [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion); eval body not inspected, no causal benefit claim |
| Vault full-text search/read/write and MCP/QMD stack | Direct search/episodes slices of `bin/lacp-brain`; supplied stack/dependency boundary; capability route in runtime | [MEM-RTE-vault-access](#mem-rte-vault-access); read/write bodies, bootstrap configuration and deployed MCP dataflow not fully inspected, preventing write-zone and end-to-end stack guarantees |
| Static scaffold, focus/mode/skill guidance and improvement source/results | Direct `Memory/README.md`; supplied focus/mode/skill and autoresearch findings | [RT-BAP-mode-prompt](runtime.md#rt-bap-mode-prompt), [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment); scaffold does not establish an operator corpus or automatic load |

Additional inspections are within SRC-1, not new sources. The root dispatcher was searched for brain/handoff/SMS dispatch; native registry handlers and plugin events were checked rather than assuming the runtime's primary route enumerated all memory. The inventory explicitly retains uninspected alternative maintenance surfaces.

## Core ideas

1. **Several independent read-back channels coexist.** Native keyed entries are returned by tools; native conversation JSONL is resumed as conversation; root/plugin host hooks push bounded handoff/SMS strings. The research/RAG and learning-event CLIs print separately selected retained material. Delivery into one channel does not establish consumption by another ([MEM-RTE-keyed-memory](#mem-rte-keyed-memory), [MEM-RTE-session-memory](#mem-rte-session-memory), [MEM-RTE-hybrid-retrieval](#mem-rte-hybrid-retrieval), [MEM-RTE-learning-hints](#mem-rte-learning-hints)).
2. **Trace transformation can discard the very content its label suggests it keeps.** Staged signals become inbox notes with an 80-character H1. The graph reader uses a bounded `## Content` section, otherwise the H1, not arbitrary body text. Thus this particular chain can reduce a 280-character signal to its title before graph admission ([MEM-RTE-trace-research](#mem-rte-trace-research)).
3. **Memory quality labels are proxy computations, not warrants.** SMS “success” can mean no recorded failures, without a fresh passing test; graph publication can use fallback promotion; similarity/time/confidence choose consolidation winners without checking logical incompatibility. Retrieval benchmarks/probes evaluate retrieval, not truth of retained assertions ([MEM-RTE-session-memory](#mem-rte-session-memory), [MEM-RTE-trace-research](#mem-rte-trace-research), [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance)).
4. **Withdrawal must reach each consumer separately.** A frontmatter resolution does not automatically exclude a note from the Markdown collector. A graph-file move does not remove its registry item or invalidate an already-built index. Promotion to enforce mode is also distinct from an advisory command that reads environment mode ([MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance), [MEM-RTE-learning-hints](#mem-rte-learning-hints)).

## Shared records

### Components

#### MEM-CMP-embedding-service
Label: Ollama embedding service

Remote/local-service embedding inference accessed by symbolic Python HTTP helpers; resulting dense vectors are distributed-parametric numerical representations retained in JSON. Model default/override is a request identifier, not a frozen parameter revision. Parameters changing during operation: uninspected — service internals are outside SRC-1; inspected builders request inference, not training. Exact version pinned: no weight digest. Mutable endpoint can resolve another model: uninspected externally; host/model overrides and stored index metadata choose endpoints. Distinct from the judgment classifier [RT-CMP-ollama-classifier](runtime.md#rt-cmp-ollama-classifier): different operation, output and consumers. SRC-1, `automation/scripts/build_memory_rag_index.py`, `automation/scripts/query_memory_rag.py`.

> ollama_model = ollama_model_override or str(metadata.get("model") or "nomic-embed-text:latest")
> --- `automation/scripts/query_memory_rag.py`

### Operative objects

#### MEM-OBJ-memory-entries
Label: Native keyed memory entries

JSON files under `~/.lacp/memory/`, one supplied key per filename. `content` is opaque user/model-authored text, ordinarily natural language; key/tags/timestamp are symbolic envelopes. Read returns raw file text; search substring-matches the entire serialized text, including metadata, and returns content previews. No automatic truth check, origin citation or rationale requirement. Consumer is the native model through a tool result; delivery affords knowledge/instruction, not verified compliance. Distinct from conversation messages [RT-OBJ-messages](runtime.md#rt-obj-messages); no supplied record names these entry files. SRC-1, `tui/tools.py`.

> data = {
>     "key": key,
>     "content": content,
>     "updated_at": _t.strftime("%Y-%m-%dT%H:%M:%S"),
>     "tags": params.get("tags", []),
> }
> --- `tui/tools.py`

#### MEM-OBJ-handoff-artifact
Label: HandoffArtifact

JSON on disk in hook contract storage and `~/.lacp/handoffs/<cwd-hash>-latest.json`. Natural-language task summary/diff coexist with symbolic path lists, branch, time and test-status metadata. Summary derives from the last assistant text, files from transcript scanning, test status from a stored eval checkpoint, diff/branch from Git. It is a lossy display/recovery summary, not the raw transcript or independently verified result. Startup reads a subset; CLI show/HTML can display more. Distinct retained result of [RT-RTE-host-hook](runtime.md#rt-rte-host-hook), not a duplicate of its event route. SRC-1, `hooks/stop_quality_gate.py`, `hooks/session_start.py`, `bin/lacp-handoff`.

> task_summary = ctx.stripped[:200] if ctx.stripped else ""
> --- `hooks/stop_quality_gate.py`

#### MEM-OBJ-episodes
Label: SMS Episode records

Append-only `episodes.jsonl` under configurable `LACP_SMS_ROOT` (default `~/.lacp/sms`). Symbolic session/project/time/files/significance fields surround natural-language summaries. Stop truncates assistant text to 200 characters and adds selected branch/mode/file-count context. `decisions_made` and `outcomes` default to empty lists in this producer; episode retention is not a structured decision/outcome analysis. Read recomputes decayed significance without rewriting the source score. Later consumers are startup context, SMS/brain CLI displays and epoch synthesis. Distinct from native messages and from the handoff, though both derive from a stop event. SRC-1, `hooks/stop_quality_gate.py`, `hooks/self_memory_system.py`, `bin/lacp-sms`, `bin/lacp-brain`.

> episodes = read_episodes(days=7, min_significance=0.6)
> --- `hooks/self_memory_system.py`

#### MEM-OBJ-self-model
Label: SMS SelfModel

`self-model.json` under SMS root; natural-language preference/success/failure pattern lists in a symbolic dataclass/JSON envelope with confidence/update counter. Heuristics derive patterns from summary keywords, changed-file count and stored checkpoint failure signals. No stored per-pattern episode citation or reason. Startup supplies only preferred approaches, known biases and failures above confidence 0.4; success patterns and effective contexts are not supplied by this builder. Update count increases confidence irrespective of independent validation. Distinct from narrative and episodes; no supplied counterpart. SRC-1, `hooks/self_memory_system.py`.

> model.confidence_in_self_model = min(0.9, 0.3 + (model.update_count * 0.05))
> --- `hooks/self_memory_system.py`

#### MEM-OBJ-sms-narrative
Label: SMS narrative and epochs

Two distinct operative parts share SMS filesystem storage but not consumers. `narrative.json` contains natural-language arc/themes/strengths/growth within symbolic AgentNarrative fields; exposed library write supports replacement, but initial author/admission and any shipped automatic synthesis are unresolved. Startup reads only an arc capped at 200 characters. `epochs.jsonl` retains symbolic time/count/grouping and at most ten natural-language decisions copied from significant episodes. Epoch synthesis sets empty theme/identity-shifts; epoch CLI displays retained epochs, but the inspected startup builder does not read epochs. This container is distinct from [MEM-OBJ-episodes](#mem-obj-episodes) and [MEM-OBJ-self-model](#mem-obj-self-model); it asserts no common write mechanism. SRC-1, `hooks/self_memory_system.py`, `bin/lacp-sms`.

The separately assessed parts are [MEM-OBJ-agent-narrative](#mem-obj-agent-narrative) and [MEM-OBJ-epochs](#mem-obj-epochs). This valid container remains declared; its shared location does not transfer either part's lineage, admission or consumer findings to the other.

#### MEM-OBJ-agent-narrative
Label: AgentNarrative

Part of: [MEM-OBJ-sms-narrative](#mem-obj-sms-narrative)

Source-native AgentNarrative is serialized as `narrative.json` under configurable SMS_ROOT (default `~/.lacp/sms`). Natural-language current_arc, themes, strengths, growth edges and decision/outcome text sit in a symbolic dataclass/JSON envelope with agent identity and synthesis timestamp. The library writer replaces the whole file. Its caller supplies content; physical software I/O establishes neither human per-content approval nor automatic trace derivation. Initial authorship, admission control and rationale lineage remain unresolved. The bounded search for AgentNarrative/write_narrative/read_narrative in `hooks/`, `bin/`, `automation/`, `tui/` and `plugin/` found the writer definitions but no caller that constructs and admits a narrative; this does not establish system-wide absence of such a caller. SRC-1, `hooks/self_memory_system.py`, `bin/lacp-sms`.

Later consumers differ: the narrative CLI displays the parsed full object; build_session_context selects only a nonempty current_arc capped at 200 characters for the startup string described in [MEM-RTE-session-memory](#mem-rte-session-memory). At the external host, this is interpretive natural-language context, not an executable rule or demonstrated behavior change. It can persist across sessions until replaced; malformed/missing JSON yields no narrative. Neither copied epoch decisions nor the epoch synthesis route establishes a writer of this part. No supplied runtime object names this file; the closest [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) is an event route, not this retained object.

> _narrative_file().write_text(json.dumps(asdict(narrative), indent=2))
> --- `hooks/self_memory_system.py`

> narrative = read_narrative()
> if narrative and narrative.current_arc:
>     parts.append(f"Current arc: {narrative.current_arc[:200]}")
> --- `hooks/self_memory_system.py`

#### MEM-OBJ-epochs
Label: Epoch records

Part of: [MEM-OBJ-sms-narrative](#mem-obj-sms-narrative)

Source-native Epoch records are appended as JSON lines to `epochs.jsonl` under SMS_ROOT. Symbolic IDs, timestamps and episode_count coexist with natural-language label, theme, key_decisions and identity_shifts. Unlike narrative's unresolved initial admission, [MEM-RTE-epoch-synthesis](#mem-rte-epoch-synthesis) establishes a shipped derivation: select significant episodes in a day window, flatten decisions_made in episode order and copy the first ten. Generated theme and identity_shifts are empty. The result retains grouping/count/time and copied decisions, not per-decision episode references or synthesis reasons. The input decision lineage remains as good as the episodes supplied; the Stop producer described in [MEM-OBJ-episodes](#mem-obj-episodes) leaves decisions empty. SRC-1, `hooks/self_memory_system.py`, `bin/lacp-sms`.

Software selects derived content after a caller triggers synthesis; triggering is not per-decision human approval. write_epoch appends, despite its update wording, with no deduplication or replacement in that function. Later read_epochs parses all nonblank valid JSON lines and the epochs CLI displays them. Its concrete consumer is thus CLI display/caller interpretation, not startup host guidance: the inspected build_session_context reads narrative, self-model and episodes, not epochs. Stored epochs remain reachable across later CLI invocations; no expiry is implemented in that reader. No observed activation or benefit is established. Distinct from the episode input and narrative file; no supplied runtime record names this retained object, and [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) is only the closest event-route counterpart.

> with open(_epochs_file(), "a") as f:
>     f.write(json.dumps(asdict(epoch), default=str) + "\n")
> --- `hooks/self_memory_system.py`

> key_decisions=decisions[:10],  # top 10
> identity_shifts=[],
> --- `hooks/self_memory_system.py`

> elif cmd == "epochs":
>     print(json.dumps(read_epochs(), indent=2))
> --- `hooks/self_memory_system.py`

#### MEM-OBJ-research-memory
Label: Research registry and materialized notes

Operative parts: staging JSONL contains extracted assistant text plus session/cwd/time; inbox Markdown wraps selected signals; research `registry.json` under the knowledge root contains text, source/count/observation/provenance/access-strength fields and optional embeddings; published graph Markdown contains derived textual displays and symbolic frontmatter/links. Natural-language claims, symbolic admission/access metadata and dense embeddings must not be treated as one encoding. Registry provenance is derived from history/inbox fields, not authenticated authorship. It persists across synchronizations; graph files are regenerated selected views. No supplied counterpart; only output overlap with hook route [RT-RTE-host-hook](runtime.md#rt-rte-host-hook), not same referent. SRC-1, `hooks/extract_memories.py`, `bin/lacp-brain-expand`, `automation/scripts/sync_research_knowledge.py`.

> if apply_changes:
>     write_registry(registry)
>     GRAPH_RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
>     live_ids = set(promoted_ids)
> --- `automation/scripts/sync_research_knowledge.py`

#### MEM-OBJ-hybrid-index
Label: Hybrid memory index

JSON file under `~/control/knowledge/knowledge-memory/data/rag/hybrid-index.json`. Each chunk retains source-relative path, heading and full chunk text (natural-language/document payload), symbolic sparse term weights/IDs, and optional dense vectors (distributed-parametric representation). Display summaries in text query output are capped at 260 characters; JSON output retains full selected chunk text. The index is a copy, not a live reference to the note; changing/deleting notes does not rewrite an already-built payload. Lineage is current Markdown corpus at build time; dense embedding provenance records service/model metadata without frozen weights. Distinct from native memory store and research registry; no supplied counterpart. SRC-1, `automation/scripts/build_memory_rag_index.py`, `automation/scripts/query_memory_rag.py`, `automation/scripts/memory_rag_lib.py`.

> "path": str(Path(chunk.path).relative_to(Path.home())),
> "heading": chunk.heading,
> "text": chunk.text,
> "sparse_vector": sparse_vec,
> --- `automation/scripts/build_memory_rag_index.py`

#### MEM-OBJ-learning-events
Label: Cross-CLI learning events

Caller-supplied task summary/keywords and outcome status/score/notes become canonical hashed JSON events appended under the configurable learning root. Natural-language task/notes are distinct from symbolic provenance, IDs, score and mode. Hash/schema validation establish payload integrity/form, not truthful outcomes or authenticated agent identity. Later query returns summary plus selected display metadata, omitting outcome notes and detailed provenance; promotion evaluates another aggregation of this store. Distinct retained input to [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion), not its promotion-state result. SRC-1, `bin/lacp-learn-capture`, `bin/lacp-learn-retrieve`.

> # Validate the freshly built event against the schema before persisting.
> --- `bin/lacp-learn-capture`

### Routes

#### MEM-RTE-keyed-memory
Label: Native keyed memory

The foreground model proposes key/content via registered handlers; code writes immediately after nonempty key/content checks. No per-content human approval or answer oracle; starting the REPL is not approving this memory. It is an open-request store operation, not evaluated learning. Same tool boundary as [RT-RTE-native-turn](runtime.md#rt-rte-native-turn), but a distinct persistent-store write/selection chain. SRC-1, `tui/tools.py`; generic delivery/50,000-character result cap is established by that supplied route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: write result/error, raw JSON read, key list or keyword-hit previews.
- Later read-back: a future model-requested memory_read/search/list returns persisted material as foreground tool-result text.
- Delegated visibility: handlers receive only parameter dictionaries; provider receives results, not direct filesystem references.
- Selection predicate: requested key names a file; search lowercases query and matches serialized JSON, returns first 20 sorted hits with 200-character content previews, plus total count.
- Invalidation or expiry: overwrite replaces a key; no expiry in inspected handlers; missing/corrupt entries error or are skipped.
- Activation or effect: filesystem persistence and later tool delivery wired; changed model behavior unobserved.
- Evidence limits: no deployed entry corpus, run or authenticity check; key is directly interpolated into a path, not established as a safe namespace.

> file_path = _MEMORY_DIR / f"{key}.json"
> --- `tui/tools.py:485-485`

#### MEM-RTE-session-memory
Label: Host session memory

Nontrivial Stop attempts create handoff and episode, update self-model before later quality evaluation, as supplied [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) orders it. This is a more specific producer/consumer memory chain, not a replacement for the host-feedback route. Host startup/clear/compact invokes the selector, which supplies strings via `systemMessage`. No per-content approval or outcome oracle at these writes; tests/checkpoints are signals, not proof of the summary. Open host work triggers deterministic capture. Failed later quality checks do not retract these earlier writes. SRC-1, `hooks/stop_quality_gate.py`, `hooks/self_memory_system.py`, `hooks/session_start.py`, `plugin/hooks/hooks.json`, `bin/lacp-handoff`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook feedback plus retained summaries/model updates; failures are caught best effort.
- Later read-back: subsequent host event pushes selected handoff/SMS text; SMS and handoff CLIs also expose retained material to callers.
- Delegated visibility: host receives selected strings, not complete transcript, full self-model, epoch hierarchy or all JSON fields.
- Selection predicate: cwd-hashed handoff under 24h; SMS self-model confidence above 0.4; arc/focus truncation; last three episodes from a seven-day, decayed-significance>=0.6 window. SMS accepts agent/project arguments but inspected builder does not filter by either.
- Invalidation or expiry: handoff overwritten per cwd; handoff clean deletes old files; injection expires by age while stored artifact remains; SMS read windows/decay reduce eligibility, not source deletion.
- Activation or effect: selected text requests awareness/preferences/caution in host context; actual compliance is unobserved and external-host dependent.
- Evidence limits: configured hooks/host protocol required; trivial/loop/circuit exits can skip capture; last summary and stale checkpoint cannot establish a successful task; no observed consumer invocation.

Budget: root startup sorts priority; default 1500 estimated tokens (`len(content)//4`). Handoff is priority 4, SMS 7, mode/workflow 2, focus 3. It stops at the first over-budget block when any part is already kept, omitting all subsequent lower-priority blocks rather than trying smaller ones. First block may exceed budget. Plugin startup has same SMS/handoff supply but differs in other features; parity cannot be generalized.

> if token_estimate + content_tokens > budget_tokens and parts:
>     break  # budget exceeded, skip remaining lower-priority items
> --- `hooks/session_start.py`

SMS success-pattern counterexample: absence of recorded failures plus >15 files creates a string saying tests pass; this producer does not establish that tests ran. `was_blocked=False` also means these writes cannot infer blocking from the current stop decision.

> pattern = "large successful changes (15+ files, tests pass)"
> --- `hooks/self_memory_system.py`

#### MEM-RTE-epoch-synthesis
Label: SMS epoch synthesis

CLI synthesize or brain-expand derives an Epoch from significant episodes and appends it; direct library operations can replace narrative/self-model separately. Distinct from session capture and no supplied counterpart. SRC-1, `bin/lacp-sms`, `bin/lacp-brain-expand`, `hooks/self_memory_system.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: synthesized count/decisions or insufficient-episodes notice.
- Later read-back: SMS epochs command displays the appended [MEM-OBJ-epochs](#mem-obj-epochs); the inspected context builder reads episodes, [MEM-OBJ-agent-narrative](#mem-obj-agent-narrative) and self-model, not epochs. Startup epoch consumption is not established.
- Delegated visibility: inapplicable — deterministic helper/CLI does not delegate to a model.
- Selection predicate: significant episodes in caller's day window, threshold 0.3; brain-expand requires at least three, CLI any nonempty set; copied decisions capped at ten.
- Invalidation or expiry: appended epochs persist; no replacement/deduplication in write_epoch despite its update wording.
- Activation or effect: grouped record available for display, not established behavior-shaping host narrative synthesis.
- Evidence limits: stop producer does not populate decisions/outcomes; initial narrative/preference/bias authorship unresolved; no observed higher-level synthesis.

Software decides content; caller triggers synthesis without per-content approval. No answer oracle, semantic criticism or improvement evidence. Guidance is fixed copying/grouping code, not a model-generated explanation.

#### MEM-RTE-trace-research
Label: Trace research admission

Assistant last-message patterns → at most five extracted signals → staging → apply-enabled brain-expand inbox notes → research sync → registry and selected graph notes. Daily history-derived signals are an alternative input, not the same trace origin. This chain is distinct from hook feedback [RT-RTE-host-hook](runtime.md#rt-rte-host-hook). Code selects/adopts text; model authored original assistant text, while history/inbox authorship can be mixed/unresolved. Caller `--apply` permits software admission, not per-content approval. No truth oracle; mode is offline corpus transformation. SRC-1, `hooks/extract_memories.py`, `bin/lacp-brain-expand`, `automation/scripts/sync_research_knowledge.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: extraction count/debug or pipeline summary; registry/node writes on apply.
- Later read-back: future sync reloads registry; built hybrid index can copy graph Markdown for later query; original inbox notes remain separately readable.
- Delegated visibility: inapplicable — inspected extraction is heuristic, not delegated generation; embedding calls receive selected text, not full transcript.
- Selection predicate: indicator regexes with code/error anti-pattern exclusion and length limits; daily/inbox readers select signals; exact hash, optional semantic dedup and prediction-error branches alter admission; publication normally uses count and score but fallback publishes up to 120 above a lower floor when none meet normal gate.
- Invalidation or expiry: staging rotates above 500 lines and is cleared after conversion; blocked IDs skip new ingestion; graph files outside live promoted IDs are deleted, while registry retains candidate history.
- Activation or effect: selected claims/metadata become graph files and later retrieval input; delivered text can inform a caller, but foreground activation/improved capacity unobserved.
- Evidence limits: extraction hook registration unresolved; plugin map lacks this hook; similarity/classification helper details uninspected; content truncation and title fallback prevent faithful full-signal preservation.

Retained rationale: staging keeps text/source/session/time, not complete original message or match reasoning. Staging conversion writes text as body and H1, but reader's fallback reads only H1. Source/observation/provenance metadata survives portions of registry admission; not every rejected/merged rationale is established as persisted or supplied by later query.

> # Fallback: use title
> title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
> content = title_match.group(1).strip() if title_match else ""
> --- `automation/scripts/sync_research_knowledge.py`

> if not promoted_ids and scored_items:
>     fallback_floor = max(0.60, promotion_min_score - 0.20)
> --- `automation/scripts/sync_research_knowledge.py`

#### MEM-RTE-daily-promotion
Label: Daily memory promotion

History prompt highlights and Codex tool/command counts become daily Markdown; heuristic suggestions can append durable memory/tasks/lessons/tools when explicitly applied. Distinct input/output pipeline, though graph synchronization also consumes daily signals. SRC-1, `automation/scripts/extract_shared_memory.py`, `automation/scripts/suggest_memory_promotions.py`, `automation/scripts/run_memory_pipeline.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: daily capture and scored source-labelled suggestion report; optional counts of applied additions.
- Later read-back: later suggestion/sync calls consume daily notes; an index rebuild copies eligible durable Markdown; no automatic foreground injection established by this driver.
- Delegated visibility: inapplicable — inspected capture/promotion is deterministic text processing, not an agent delegation.
- Selection predicate: rolling history window; latest 30 prompt highlights, 12 lesson candidates using keyword hints; suggestion category scores/focus limits and normalized dedup; apply targets choose files.
- Invalidation or expiry: daily rolling capture overwrites the same day's file; appended durable bullets have no expiry in inspected apply function; score report retained separately.
- Activation or effect: optional durable bullet adoption and later corpus retrieval wired; correctness and useful future behavior unobserved.
- Evidence limits: source parsing/redaction not fully inspected; candidate lessons can be user prompt text rather than demonstrated lessons; complete original traces are not copied.

The pipeline invokes suggestions without `--apply`, so suggestion production is not durable-fact adoption by that invocation. Explicit apply is software content selection after caller enablement; human contribution per bullet is unresolved. Report preserves score/source; applied bullet carries text under a timestamp heading but not that score/source explanation. No answer oracle or causal learning evidence.

> added["memory"] = append_under_heading(MEMORY_FILE, f"## Auto Promoted ({timestamp})", mem_lines)
> --- `automation/scripts/suggest_memory_promotions.py`

#### MEM-RTE-hybrid-retrieval
Label: Hybrid memory retrieval

Markdown collector → chunks/sparse vectors/optional embeddings → index file → caller query or evaluator → ranked result text. Builder and query software own progression; caller supplies query/configuration. Distinct from native tool memory and host injection; nearest supplied capability route [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) does not establish this Python index's integration. SRC-1, `automation/scripts/build_memory_rag_index.py`, `automation/scripts/memory_rag_lib.py`, `automation/scripts/query_memory_rag.py`, `automation/scripts/active_recall_probes.py`, `automation/scripts/run_memory_pipeline.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: index build metadata or ranked path/heading/text results; dense failures can reweight to sparse/lexical fallback, strict mode raises.
- Later read-back: query reloads the saved payload; benchmark/probe callers consume ranked results, and an external CLI caller may read them. Foreground model delivery uninspected — no dedicated REPL tool wiring established.
- Delegated visibility: embedding service receives chunk/query text; caller gets selected text plus paths/scores, not the full registry or all index chunks.
- Selection predicate: collect Markdown under knowledge root excluding `/data/`; query uses sparse, dense and lexical signals, default weights 0.45/0.45/0.10, RRF candidates top_k*4 then blended rerank; default eight final results; no query output token budget.
- Invalidation or expiry: explicit rebuild replaces index; no freshness or resolution-status rejection in inspected query; missing index errors and dense metadata influences fallback.
- Activation or effect: retrieval results drive benchmark/probe ranking judgments and are available to a caller; model task behavior remains unobserved.
- Evidence limits: corpus/model/service and deployed wiring unavailable; text preview is not full payload, embeddings are not claims, and similarity is not truth or relevance ground truth.

Index admission is current filesystem corpus plus build configuration, no per-document approval. Benchmarks use expected paths/reference checks; probes accept item/category stems or >=0.5 token overlap as retrieval hits. These are explicit reference outcomes for retrieval, not expected task answers or semantic validation. A probe status can feed the later forgetting gate.

> if "/data/" in path.as_posix():
>     continue
> files.append(path)
> --- `automation/scripts/memory_rag_lib.py`

#### MEM-RTE-memory-maintenance
Label: Memory maintenance and withdrawal

Several separately controlled operations coexist: explicit resolve edits status/reason; rename selects an H1 then changes names/wikilinks; consolidation selects prune candidates and archives files; cap enforcement destroys tail content; inbox archive applies age retention. These share filesystem outputs, not an admission policy. No supplied duplicate; relation to graph route is changed views of the same research corpus. SRC-1, `bin/lacp-brain-resolve`, `automation/scripts/curate_titles.py`, `automation/scripts/memory_consolidation.py`, `automation/scripts/memory_index_guard.py`, `automation/scripts/archive_inbox.py`, `bin/lacp-brain-expand`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resolution/rename/prune/cap/archive summary or dry-run preview; malformed driver arguments can prevent archive execution.
- Later read-back: edited notes can be read/indexed; prune_history is loaded by maintenance state; latest probe results alter forgetting; no proof all withdrawal marks reach all downstream stores.
- Delegated visibility: inapplicable — inspected operations are deterministic helpers, not delegated model calls.
- Selection predicate: caller node/resolution/reason; title classification/H1 and collision checks; consolidation strength/edge thresholds with probe, bridge and active-category protection; MEMORY.md keeps first 200 lines then byte-prefix up to 25,000; archive selects old top-level inbox notes.
- Invalidation or expiry: physical move/delete/overwrite affects future file reads but not existing index copies; registry can regenerate graph nodes; resolution retains a stale body; cap enforcement has no tail checkpoint/reload in inspected function.
- Activation or effect: executable filesystem changes wired; universal revocation, restored correctness or successful semantic synthesis unestablished.
- Evidence limits: strength/embedding helper internals not inspected; consolidation mutation of supersedes occurs in memory without a registry-write call in inspected run function; no operation trace or recovery test.

Admission differs by mechanism. Resolve caller supplies the actual status/reason and code applies unless dry-run; no authenticated human required. Rename/prune are software selections enabled by `--apply`, not per-item human judgments. Cap enforcement deterministically overwrites without approval of discarded text; it appends a warning after the cap, so final bytes can exceed the nominal limit. No answer oracle at these edits. Renaming changes access/address, not the assertion; candidate clustering is not actual semantic merging. Consolidation's “conflict” criterion is high similarity; winner selection uses event time/confidence, not a contradiction test. Reasons appear in previews, but inspected apply mode does not establish persistent loser→winner registry mutation. Pruning moves graph files and retains prune history, not deletion/blocking of registry items. Future sync can materialize them again.

> if apply and conflicts:
>     for conflict in conflicts:
>         loser_id = conflict["loser"]
>         if loser_id in items:
>             items[loser_id]["supersedes"] = conflict["winner"]
>             superseded_ids.append(loser_id)
> --- `automation/scripts/memory_consolidation.py`

Archive interface mismatch is a static forcing case: brain-expand supplies `--apply` (or `--days` without dry-run), but the inspected archive parser accepts `--dry-run` and not `--apply`. Thus its apply branch cannot be assumed to archive successfully; its non-apply branch can actually move files. No target execution was performed.

> parser.add_argument("--dry-run", action="store_true", help="Show what would be archived without moving")
> --- `automation/scripts/archive_inbox.py`

> run_step_soft "archive_inbox" python3 "${SCRIPTS_DIR}/archive_inbox.py" --days 30 --apply
> --- `bin/lacp-brain-expand`

#### MEM-RTE-learning-hints
Label: Cross-CLI advisory hints

Explicit capture in enabled shadow mode creates schema-checked events; explicit query in enabled advisory mode selects summaries. Generic callers supply outcomes; code owns capture/ranking, not human verification. Distinct from enforce-state promotion [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion). SRC-1, `bin/lacp-learn-capture`, `bin/lacp-learn-retrieve`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: canonical event/hash or capture no-op; query emits advisory summary hints or inactive empty result.
- Later read-back: query reloads event store; promotion/evaluation use event records separately; no shipped automatic foreground injection established in the bounded consumer search.
- Delegated visibility: inapplicable — capture/query does not invoke a model; CLI caller receives selected summary/CLI/status/confidence/time, not outcome notes or rationale.
- Selection predicate: task tokens/keywords and repo-trust match; outcome status/score multiplicatively gate relevance; confidence floor, rank/recency, maximum hint count and estimated summary budget. Defaults in query are three hints, 400 estimated tokens and confidence floor 0.70 before configured cap resolution.
- Invalidation or expiry: disabled/non-advisory environment yields no hints unless force; events retained; promotion rollback clears mode/active state but not event history, per supplied route.
- Activation or effect: advisory printed guidance, explicitly non-routing; no enforce-mode runtime activation established.
- Evidence limits: labels/hashes do not verify outcomes; an oversized first hint can exceed estimated budget; promotion-state file is not read by inspected query, which gates on environment.

No answer oracle at capture; outcome is asserted caller data. Software schema gate can refuse malformed events, not false ones. Recovery preserves history; querying failures does not retract source events. Apply to enforce and advisory selection are not interchangeable modes. No causal capacity improvement follows from the name “learning.”

> if [[ "${LACP_LEARNING_ENABLED}" == "1" && "${LACP_LEARNING_MODE}" == "advisory" ]]; then
>     advisory_active=1
> fi
> --- `bin/lacp-learn-retrieve`

#### MEM-RTE-vault-access
Label: Vault access and displays

Explicit brain search requests REST full-text search, with local file-search fallback. Episodes/review/status commands offer separate retained displays; they are not automatic context injection. Distinct from hybrid query and dynamic MCP capability loading [RT-RTE-extension-load](runtime.md#rt-rte-extension-load). SRC-1, `bin/lacp-brain`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: path/context search results or retained episode/review/status display.
- Later read-back: later CLI callers retrieve retained vault notes, SMS episodes or generated review queue; documented command is an afforded access channel, not proof the native model receives it.
- Delegated visibility: REST request includes query/contextLength; text display limits results/context; JSON API response passed through.
- Selection predicate: caller query, default ten displayed results; REST first then case-insensitive ripgrep path fallback; episodes selected by day window, last ten in textual display.
- Invalidation or expiry: file/API availability and underlying store changes affect future reads; no consistent stale-status exclusion established.
- Activation or effect: information exposed to CLI/operator; model instruction compliance or later task effects unobserved.
- Evidence limits: REST service internals/configuration unavailable; read/write body and external MCP routes not fully traced; no universal write-zone or trust guarantee.

> result="$(curl -s --max-time 3 "${REST_API}/search/simple/?query=${encoded}&contextLength=100" 2>/dev/null || echo "")"
> --- `bin/lacp-brain`

### Claims

#### MEM-CLM-goal-filtering
Label: Goal-relevant SMS filtering

Source doctrine says focus gates memory retrieval, but inspected startup builder appends focus and separately selects episodes by recency/significance, without goal_relevance_score or goal_filtered_query. Those helpers implement a keyword overlap capability/query-prefix transformation; their presence does not establish a wired foreground retrieval filter. Distinct from [RT-BAP-mode-prompt](runtime.md#rt-bap-mode-prompt), which addresses native prompt authority. SRC-1, `hooks/self_memory_system.py`, `bin/lacp-sms`, `hooks/session_start.py`.

- doctrine conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> Simple keyword overlap — could be upgraded to embeddings later.
> --- `hooks/self_memory_system.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-text
Label: Retained memory text authority

Actual consumers differ: native model receives keyed files/resumed messages via conversation tool text; external host receives startup `systemMessage`; CLI/evaluators receive query outputs; maintenance code consumes symbolic counters/probes/status. Natural-language claims/preferences ask the model/human to interpret; metadata determines fixed selection/admission only at the relevant code consumer; dense vectors determine numerical retrieval ranking, not textual authority. Horizon is subsequent invocations, across sessions for persisted stores, subject to route selection and filesystem state. Delivery is wired on the specified paths, compliance/benefit unobserved. Distinct from native mode prompt [RT-BAP-mode-prompt](runtime.md#rt-bap-mode-prompt) and changed executable source [RT-BAP-autoresearch-code](runtime.md#rt-bap-autoresearch-code). Evidence/quotes: [MEM-RTE-session-memory](#mem-rte-session-memory), [MEM-RTE-keyed-memory](#mem-rte-keyed-memory), [MEM-RTE-hybrid-retrieval](#mem-rte-hybrid-retrieval); SRC-1, `hooks/session_start.py`, `tui/tools.py`, `automation/scripts/query_memory_rag.py`.

## Annotations

#### On [RT-OBJ-messages](runtime.md#rt-obj-messages)

Memory-specific lineage: saved messages retain role/content and tool identifiers as symbolic envelopes around text, not a separately derived lesson corpus. Save rewrites the whole JSONL; restore skips malformed lines and returns metadata separately. This is raw-ish conversation persistence, already lossy where tool results were capped, rather than current-window compaction. Resumed provider receives message content but not all metadata; startup resume and `/resume` constitute later read-back. SRC-1, `tui/sessions.py`; source passage in supplied object and route.

#### On [RT-RTE-native-turn](runtime.md#rt-rte-native-turn)

Working-context controls: focus capped at 200 characters; results capped at 50,000; `/clear` removes the whole accumulated conversation; resume reintroduces saved messages. No summarizing transformation established by MAX_SESSION_SIZE in `tui/sessions.py`; constant is not an invoked compactor. Model-selected keyed reads bring external persisted material back by value through a tool result. File path/key in the window is not a live heap reference; code must read it. These are truncation/whole-window discard/reload controls, not preferential automatic eviction of old turns. Supplied route supplies supporting passages; direct `tui/sessions.py` inspection confirms full-message save/load.

#### On [RT-RTE-host-launch](runtime.md#rt-rte-host-launch)

Separate host delegation keeps caller conversation out except explicit task text; OAuth Codex gets last user string, not system/prior turns. Returned/truncated output reenters caller messages and may later persist. This resembles a task frame whose selected inputs enter and return value escapes, but filesystem effects and external host persistence can outlive the frame; retained messages are by value, not shared references. Host's own compaction/tail/checkpoint form remains opaque. Source/quote supplied by route; SRC-1, `tui/tools.py`, `tui/providers.py`.

#### On [RT-RTE-extension-load](runtime.md#rt-rte-extension-load)

Skill file text reload is on demand, capped at 10,000 characters; this route does not retain a newly derived summary or establish automatic skill-frame eviction. Installed capability/configuration revisions have later executable consumers, but write agency and factory internals are unresolved. SRC-1, `tui/tools.py`, `tui/mcp.py`; supplied source passage.

#### On [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion)

Retained enforce/shadow state and promotion receipts are symbolic admission metadata, distinct from event summary hints. Rollback preserves experiences and records but removes active promotion; it does not invalidate copies already delivered to a caller or clear native keyed/SMS/graph material. No downstream enforce-state consumer was established by bounded searches in this job. SRC-1, `bin/lacp-learn-promote`, `bin/lacp-learn-rollback`, `bin/lacp-learn-retrieve`; supplied route and advisory quote above.

#### On [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment)

Changed source/program, result TSV and logs have separate consumers: later process imports execute source; later experiment count reload reads TSV; proposal guidance rereads program. Retained logs/scores do not establish criticism fed back into proposal content. Current imported functions are not necessarily changed by on-disk edits. This is a persistent behavior-organization route distinct from text-memory retrieval, with the runtime's unobserved causal link retained. Source/quotes supplied by route; SRC-1, `tui/idle_agent.py`, `config/autoresearch-program.md`.

## Write side

The routes distinguish five admission families. Foreground keyed writes admit model/caller content after nonempty checks. Host Stop automatically derives summaries/patterns, before final quality judgment. Trace/research transforms are heuristic software admission enabled by an apply flag, with duplicate/gate/fallback behavior. Daily promotion emits suggestions by default and only adopts bullets when explicitly applied. Manual resolution admits caller-supplied status/reason; automated maintenance selects renames/archives/tail deletion using fixed rules. None of these labels establishes authenticated human approval or truth validation ([MEM-RTE-keyed-memory](#mem-rte-keyed-memory), [MEM-RTE-session-memory](#mem-rte-session-memory), [MEM-RTE-trace-research](#mem-rte-trace-research), [MEM-RTE-daily-promotion](#mem-rte-daily-promotion), [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance)).

Known trace-fed paths reach durable behavior-shaping text: assistant/checkpoint/file signals → SMS pattern JSON → later startup preference/caution strings; history/assistant traces → daily/staging text → selected graph/durable files → rebuilt index → caller. Their original input is not uniformly agent experience: daily prompts may be user instructions, inbox notes may be external research, and checkpoint signals may be stale. Reasons are only partly retained: self-model lacks per-pattern provenance, applied daily bullets omit report scores/sources, and graph/index summaries do not preserve full original conversations. Epoch grouping is an alternative derived checkpoint with a display reader, not demonstrated startup consumption ([MEM-RTE-epoch-synthesis](#mem-rte-epoch-synthesis)).

Rejection and withdrawal are local operations. Schema rejection prevents event append; extraction anti-patterns prevent signals; publication can quarantine and later remove graph views while retaining registry. Rename affects addresses; resolution keeps body plus status/reason; pruning archives material without proving registry suppression; cap enforcement discards tail without a retained summary. Cross-CLI rollback resets promotion state, not all learned content. Propagation to later consumers must be re-established separately. Automatic source improvement remains the independently assessed runtime pathway, not evidence every retained note is self-improvement.

## Read-back

Push: host event selects latest eligible handoff and SMS slices into a priority-budgeted string. Demand: foreground native memory tools select key/substring, native resume reintroduces saved conversation, CLI search/query supplies vault/index/events/episodes to an explicit caller. Evaluation: benchmark/probe selects index chunks and turns them into retrieval status; forgetting later consumes probes. Static skill/mode files are ordinary instruction loads unless changed through use; they are not counted as retained experience merely because read on another invocation.

Host `/compact` semantics are external. LACP supplies a post-compaction reminder/handoff and detects pressure proxies; it does not implement host summarization in inspected paths. The retained recovery forms are native JSONL transcript, stop-derived handoff JSON, SMS episodes/patterns, graph/file copies and epochs. Only some are delivered at session start. Native delegation isolates selected task inputs and returns output, whereas ordinary tool results simply add text to the current conversation. No trace establishes activation or useful capacity gain through any of these channels.

## Integration issues

- **Additional forcing case, not correction to runtime:** [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance) shows brain-expand/archive argument mismatch and dangerous non-apply archival default. Runtime left maintenance details open. SRC-1, `bin/lacp-brain-expand`, `automation/scripts/archive_inbox.py`. Consequence: scheduled archival cannot be treated as reliably wired by driver presence alone.
- **Specific route overlap:** [MEM-RTE-session-memory](#mem-rte-session-memory) elaborates retained-state production in [RT-RTE-host-hook](runtime.md#rt-rte-host-hook), but has a distinct later consumer/selection chain; [MEM-RTE-keyed-memory](#mem-rte-keyed-memory) is a distinct store-specific chain inside the native turn. No replacement/duplicate referent is proposed. Other supplied referents received annotations rather than re-declaration.
- **Consolidation persistence/withdrawal:** high-similarity conflict decisions mutate an in-memory registry but inspected function writes only consolidation state and file moves, not updated registry. Graph sync can re-materialize registry items. Existing indexes and unrestricted collectors do not respect resolution marks automatically. Consequence: [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance) does not establish durable semantic supersession or universal revocation. SRC-1, `automation/scripts/memory_consolidation.py`, `automation/scripts/sync_research_knowledge.py`, `automation/scripts/memory_rag_lib.py`.
- **Truncated extraction integration:** [MEM-RTE-trace-research](#mem-rte-trace-research) preserves the title fallback and default confidence, not full body/trace rationale. Extraction source exists but its active installation/registration is unresolved; inspected plugin map registers only quality Stop. Consequence: automatic full-signal adoption is not established. SRC-1, `hooks/extract_memories.py`, `bin/lacp-brain-expand`, `automation/scripts/sync_research_knowledge.py`, `plugin/hooks/hooks.json`.
- **SMS mapping limits:** [MEM-CLM-goal-filtering](#mem-clm-goal-filtering) is an afforded helper, not startup goal-ranked retrieval. [MEM-OBJ-sms-narrative](#mem-obj-sms-narrative) remains a valid container with separately declared parts. [MEM-OBJ-agent-narrative](#mem-obj-agent-narrative) has unresolved initial narrative admission; [MEM-OBJ-epochs](#mem-obj-epochs) has implemented copying/grouping and a display reader. Epoch display does not imply narrative update or startup epoch consumption. Agent/project parameters do not establish compartmentalized SMS selection. Consequence: no unified psychology/goal/temporal guarantee. SRC-1, `hooks/self_memory_system.py`, `bin/lacp-sms`.
- **Advisory versus enforce integration:** [MEM-RTE-learning-hints](#mem-rte-learning-hints) gates environment advisory mode, while [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) writes enforce-state file. Query returns summaries without outcome-note reasoning. No bounded consumer search established enforcement/automatic hint injection. Consequence: state admission is not downstream learning activation. SRC-1, `bin/lacp-learn-retrieve`, `bin/lacp-learn-promote`, `bin/lacp-learn-rollback`.
- **Included opaque/uninspected alternatives:** individually named coverage rows retain unresolved session/article/repo mirrors, research synthesis, MCP-memory rendering, gap/review generation, quarantine/threshold maintenance, ingestion delegates and external stack. Missing admission/lineage/consumer facts prevent exhaustive whole-memory classification, not the supported specific chains. No access failure is claimed for available files.

The correction declares narrative and epoch object parts separately under the existing container. SRC-1, `hooks/self_memory_system.py` and `bin/lacp-sms`, establishes distinct files, writers and readers; the coverage row, epoch read-back and SMS mapping issue now point to those parts. No supplied runtime fact was found requiring replacement; the report adds qualifications to claims that the runtime intentionally left open. No new record is proposed as a duplicate referent of a supplied declaration.

## Limitations and checks

Static inspection establishes capacities and failures in source control flow only. No target command, test, example, provider or service was executed. No observed behavioral dependence, reliable recovery, validated semantic truth, causal learning or exercised self-improvement is established. Uninspected alternative bodies are explicitly retained in coverage, so this report is not an exhaustive audit of all shipped memory transformations.

Source identity recheck: checkout HEAD equals `e31f134b689afd6a71d94b0420682d1f528d6fa1`; repository evidence remains SRC-1. Governing invocation, member types, boundary/runtime, collection, worker rules and record contract were read; input range tails were recovered. Method instructions were used as supplied, not revised. Deterministic validation: the invocation's `commonplace-run validate-output` check passed with exit status 0: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” It checks form/quotation occurrence, not semantic support or acceptance.
