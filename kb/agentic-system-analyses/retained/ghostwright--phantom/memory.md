---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Phantom memory: heuristic vector extraction, selective file instruction loading, and durable chat recovery at the frozen revision."
run-id: AAS-2026-10-15-phantom-cc566f03ac40-01
source-identity: "https://github.com/ghostwright/phantom"
reviewed-boundary: "f8c7ab42d885936ee54abc785528000260f4acc5"
---

# Phantom memory report

## Boundary and evidence

Phantom has several retained-state loops, not one universal memory pipeline. This member includes channel-fed vector extraction, vector recall, reflection-managed files, foreground notes, SDK session continuation, web-chat transcript/event/timeline retention, recovery tools, and operator withdrawal/editing. It uses SRC-1 from [boundary](boundary.md), at commit f8c7ab42d885936ee54abc785528000260f4acc5. All direct source findings below are implementation evidence unless labelled doctrine/design. No target execution, deployment capture or causal experiment was supplied or performed.

The supplied runtime establishes outer invocation and grants. I independently inspected the memory transformations and later consumers rather than treating that account as an inspection limit. External SDK transcript storage, compaction algorithms, model reasoning and provider internals remain outside the available implementation; their opacity prevents full-context and successful-recovery conclusions. Static roles and security instructions are context inputs, not memories accumulated through use. Dynamic executable tools and operator skills/hooks remain included through runtime records, but are not recast as vector knowledge.

| Entry point or operation | Directly inspected SRC-1 paths, unless marked supplied | Coverage and limit |
|---|---|---|
| CLI and hooks | `src/cli/index.ts`, `src/agent/hooks.ts` | CLI dispatch exposes start/init/doctor/token/status, not a separate memory-maintenance command. Edit/Write tracker retains path metadata, not file content or semantic approval. Startup memory wiring: `src/index.ts`; [MEM-RTE-vector-extraction](#mem-rte-vector-extraction). |
| Channel consolidation and alternate ingress | `src/index.ts`, `src/memory/consolidation.ts`; supplied [RT-RTE-direct-work](runtime.md#rt-rte-direct-work) | [MEM-RTE-vector-extraction](#mem-rte-vector-extraction), [MEM-ABS-procedure-learning](#mem-abs-procedure-learning). Shared read access does not establish web/scheduler/trigger trace admission. |
| Vector stores, embeddings and retrieval | `src/memory/system.ts`, `src/memory/episodic.ts`, `src/memory/semantic.ts`, `src/memory/procedural.ts`, `src/memory/embeddings.ts`, `src/memory/ranking.ts`, selected `src/memory/qdrant-client.ts` search/update methods, `config/memory.yaml` | [MEM-OBJ-episodes](#mem-obj-episodes), [MEM-OBJ-semantic-facts](#mem-obj-semantic-facts), [MEM-OBJ-procedures](#mem-obj-procedures), [MEM-OBJ-retrieval-indexes](#mem-obj-retrieval-indexes), [MEM-RTE-vector-context](#mem-rte-vector-context). Initial deployed contents and embedding versions unresolved. |
| Prompt selection and file notes | `src/agent/prompt-assembler.ts`, `src/agent/prompt-blocks/evolved.ts`, `src/agent/prompt-blocks/working-memory.ts`, `src/agent/prompt-blocks/instructions.ts`, `src/agent/prompt-blocks/agent-memory-instructions.ts`, `src/evolution/engine.ts` | [MEM-OBJ-evolved-files](#mem-obj-evolved-files), [MEM-OBJ-reflection-context](#mem-obj-reflection-context), [MEM-OBJ-working-memory](#mem-obj-working-memory), [MEM-OBJ-agent-notes](#mem-obj-agent-notes). New arbitrary strategy files are not automatically selected by the fixed evolved loader. |
| Reflection admission and maintenance | `src/evolution/queue.ts`, `src/evolution/batch-processor.ts`, selected gate/cadence/invariant/runner/versioning ranges, full teaching prompt and engine | [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission), memory annotations, [MEM-OBJ-evolution-queue](#mem-obj-evolution-queue), [MEM-OBJ-evolution-log](#mem-obj-evolution-log). Source-supported correction to runtime's compact-status qualification below. |
| Agent and external MCP lookup | `src/agent/in-process-reflective-tools.ts`, memory core of `src/mcp/tools-universal.ts`, memory/config resources in `src/mcp/resources.ts`, codebase query in `src/mcp/tools-swe.ts` | [MEM-RTE-memory-tools](#mem-rte-memory-tools). Role-specific SWE review memory gathering identified but not fully traced; no comprehensive claim about every role-specific rendering. |
| Chat continuity, transcript recovery and cleanup | `src/chat/writer.ts` persistence/context branches, `src/chat/event-log.ts`, `src/chat/transcript-search.ts`, selected `src/chat/continuity-context.ts`, `src/chat/run-timeline.ts`, `src/chat/session-store.ts`, full `src/chat/sweep.ts`; supplied SDK transform findings | [RT-RTE-chat-context](runtime.md#rt-rte-chat-context), [MEM-OBJ-chat-transcript](#mem-obj-chat-transcript), [MEM-OBJ-chat-events](#mem-obj-chat-events), [MEM-OBJ-chat-timelines](#mem-obj-chat-timelines), [MEM-RTE-transcript-recovery](#mem-rte-transcript-recovery). SDK summary payload and exact transcript pruning remain uninspected. |
| Dashboard read, edit and delete | `src/ui/api/memory.ts`, memory-file API mutation branches, `src/memory-files/paths.ts`, storage list/read/write/delete branches | [MEM-RTE-operator-memory](#mem-rte-operator-memory), [MEM-OBJ-user-memory](#mem-obj-user-memory). UI/API admission differs from reflection. SDK loading of arbitrary Markdown beneath user settings is not established. |
| Evaluation and claims | `docs/memory.md`, reflection teaching prompt, selected `e2e/reflection-subprocess.spec.ts` fixture/protection helpers; supplied runtime evaluation limits | [MEM-CLM-universal-memory](#mem-clm-universal-memory). Test source is a specification, not passing execution or later task benefit. |
| Other persistent capabilities | Supplied [RT-OBJ-dynamic-tools](runtime.md#rt-obj-dynamic-tools), [RT-RTE-operator-config](runtime.md#rt-rte-operator-config), [RT-OBJ-session-store](runtime.md#rt-obj-session-store) | Symbolic definitions, instruction bodies and opaque SDK history remain distinct. Dependency loading, forked skill/subagent contexts and output transfer are uninspected; no claim that these isolate exactly the same material as chat context replacement. |

## Core ideas

1. **Vector extraction and reflection are parallel writes.** The former truncates channel user input into episodes and pattern-matched preference/correction facts. The latter asks a separate model to curate long-lived files. Neither stores a complete, verified account of every conversation. [MEM-RTE-vector-extraction](#mem-rte-vector-extraction), [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission).
2. **The consumer sees less than the retained store.** Automatic vector context exposes fact text/confidence, episode summaries and selected procedure steps, omitting much provenance and procedure conditions. Evolved prompts select fixed files; corrections/principles are reflection context, not directly loaded evolved prompt fields. [MEM-RTE-vector-context](#mem-rte-vector-context), [MEM-OBJ-evolved-files](#mem-obj-evolved-files), [MEM-OBJ-reflection-context](#mem-obj-reflection-context).
3. **Two foreground note surfaces have different authority.** Working memory is automatically injected with an explicit trust instruction and truncated by code. Agent notes are deliberately kept out of the automatic prompt and must be read through tools. Their append-only rule is guidance, not a global filesystem invariant. [MEM-RTE-foreground-notes](#mem-rte-foreground-notes).
4. **Chat recovery uses multiple retained representations.** SDK resume is opaque; committed messages support bounded lexical reload; event-derived checkpoint metadata and timeline-derived page artifacts support automatic continuity. These are neither complete provider checkpoints nor equivalent substitutes for the transcript. [RT-RTE-chat-context](runtime.md#rt-rte-chat-context), [MEM-RTE-transcript-recovery](#mem-rte-transcript-recovery).

## Shared records

### Components

none declared in this member. Model roles and their unpinned parameter versions are already declared in runtime, including [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client).

### Operative objects

#### MEM-OBJ-episodes
Label: Vector episode payloads

Source-native identity: Qdrant `episodes` payloads via `EpisodicStore`. Natural-language summary/detail/outcome-detail/lessons coexist with symbolic IDs, timestamps, outcome, importance, decay and access metadata. Dense retrieval vectors are separately assessed in [MEM-OBJ-retrieval-indexes](#mem-obj-retrieval-indexes). No counterpart object is declared by runtime; these are different from SQLite session rows in [RT-OBJ-session-store](runtime.md#rt-obj-session-store).

Lineage: consolidation takes the first user message, truncates it to 200 characters, and derives a short detail from that summary plus tools/files/outcome/cost. It does not preserve assistant messages or the full raw transcript; lessons are initialized empty. The caller supplies empty tools and an outcome based on the `Error:` prefix. Later consumers are automatic context, MCP tools/resources and dashboard viewers; prompt delivery is guidance, not an outcome oracle. Access/decay metadata influences selection rather than asserting truth. [SRC-1: `src/memory/consolidation.ts`, `src/memory/episodic.ts`, `src/memory/ranking.ts`, `src/index.ts`]

> const summary = firstMessage.length > 200 ? `${firstMessage.slice(0, 197)}...` : firstMessage;
> --- `src/memory/consolidation.ts`

#### MEM-OBJ-semantic-facts
Label: Semantic fact payloads

Source-native identity: Qdrant `semantic_facts` payloads via `SemanticStore`. Natural-language statement and subject/predicate/object text are retained alongside symbolic category, confidence, validity, version and episode IDs. Confidence is extractor-assigned, not measured accuracy. The automatic extractor copies up to 300 characters of matching user messages and sets correction confidence 0.8 or preference confidence 0.9. External/preexisting contents and original admission remain unresolved; known subsequent store behavior still applies. No counterpart object appears in runtime. [SRC-1: `src/memory/consolidation.ts`, `src/memory/semantic.ts`]

The store's “contradiction” operation searches at most ten same-subject, currently valid payloads, applies a similarity threshold of 0.85 and tests unequal object strings. Despite its comment, the filter does not require equal predicate. A new fact with greater/equal confidence dates out the old payload; lower-confidence new facts are still stored. Normal recall excludes any non-null `valid_until`; explicit time-range recall instead filters creation time and can return expired facts. This is heuristic supersession, not demonstrated semantic contradiction resolution. Episode provenance remains in the payload, but automatic fact formatting omits it. [SRC-1: `src/memory/semantic.ts`, `src/memory/context-builder.ts`]

> if (newFact.confidence >= existingFact.confidence) {
> 	await this.qdrant.updatePayload(this.collectionName, existingFact.id, {
> 		valid_until: new Date(newFact.valid_from).getTime(),
> 	});
> }
> --- `src/memory/semantic.ts`

#### MEM-OBJ-procedures
Label: Procedure payloads

Source-native identity: Qdrant `procedures` via `ProceduralStore`. Natural-language description, trigger, actions, preconditions and postconditions are stored with symbolic step order, parameters, source episode IDs, confidence/version and success/failure counters. Counter/parameter encoding does not make natural-language actions executable code. This object has no supplied counterpart; it differs from executable [RT-OBJ-dynamic-tools](runtime.md#rt-obj-dynamic-tools). [SRC-1: `src/memory/procedural.ts`]

`storeProcedure` and `updateProcedureOutcome` expose write capabilities; source search did not establish a shipped trace-fed caller. Initial procedure authorship/admission, rationale and counter validity are unresolved. `find` returns one candidate above score 0.3; automatic context renders name, trigger, confidence, counters and ordered actions, not description/preconditions/postconditions/parameters/provenance. The model interprets the selected advice; no procedure interpreter or automatic success oracle is established. [SRC-1: `src/memory/system.ts`, `src/memory/procedural.ts`, `src/memory/context-builder.ts`]; [MEM-ABS-procedure-learning](#mem-abs-procedure-learning).

> limit: 1,
> withPayload: true,
> --- `src/memory/procedural.ts`

#### MEM-OBJ-retrieval-indexes
Label: Dense and sparse retrieval indexes

Source-native identity: named Qdrant vectors `summary`, `detail`, `fact`, `description`, `text_bm25`. Dense numerical representations come from Ollama embedding inference over payload text; sparse hashed token-frequency features come from deterministic `textToSparseVector`. Dense encodings are distributed numerical representations; sparse indices/values are localized symbolic retrieval features, despite the BM25 label. No IDF weighting is computed in the inspected sparse builder. These are indexes, not text replacements or provider weight updates. [SRC-1: `src/memory/embeddings.ts`, `src/memory/episodic.ts`, `src/memory/semantic.ts`, `src/memory/procedural.ts`]

Distinct from [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client), which is the producing model. The repository does not pin the deployed model digest or ensure old and new embeddings use identical model versions. Episode recall queries the summary vector plus sparse text; its retained detail vector is not used by that recall method. Qdrant hybrid search dispatch requests rank fusion, but server semantics/durability were not executed. [SRC-1: `src/memory/episodic.ts`, `src/memory/qdrant-client.ts`]

> values.push(count / tokens.length);
> --- `src/memory/embeddings.ts`

#### MEM-OBJ-evolved-files
Label: Automatically loaded evolved instruction files

Source-native identity: `persona.md`, `user-profile.md`, `domain-knowledge.md`, and the three fixed `strategies/task-patterns.md`, `tool-preferences.md`, `error-recovery.md` files under `phantom-config`. Natural-language filesystem content becomes an in-process `EvolvedConfig` snapshot and appended prompt text. Constitution is static identity context and a reflection protection target, not a learned output merely because the same loader loads it. This retained output is distinct from the transformation route [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission). [SRC-1: `src/evolution/engine.ts`, `src/agent/prompt-blocks/evolved.ts`]

Reflection may rewrite, compact or promote entries under the teaching prompt; foreground filesystem rights also afford edits without that admission gate. Boot loads files; accepted changed reflection drains notify runtime. Evolved sections other than constitution need more than one nonblank, nonheading content line to appear. There is no per-query character/token budget in this formatter. New strategy filenames may pass reflection scope checks but are not in the fixed loader, so acceptance does not imply automatic foreground consumption. Content is guidance at the model, not code-enforced policy. [SRC-1: `src/evolution/invariant-check.ts`, `src/evolution/engine.ts`, `src/agent/prompt-blocks/evolved.ts`, `src/index.ts`]

> taskPatterns: readConfigFile(join(dir, "strategies/task-patterns.md")),
> toolPreferences: readConfigFile(join(dir, "strategies/tool-preferences.md")),
> errorRecovery: readConfigFile(join(dir, "strategies/error-recovery.md")),
> --- `src/evolution/engine.ts`

#### MEM-OBJ-reflection-context
Label: Reflection-only corrections and principles

Source-native identity: `memory/corrections.md`, `memory/principles.md` and newly permitted strategy Markdown outside the fixed loader. Filesystem natural-language material can retain corrections, rules and explanations; no observed generated content is supplied. It is distinct from [MEM-OBJ-evolved-files](#mem-obj-evolved-files) by consumer and from [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) by object identity. [SRC-1: `src/evolution/subprocess-prompt.ts`, `src/evolution/invariant-check.ts`, `src/evolution/engine.ts`]

The teaching prompt affords reflection reading and revising these files in later drains. `getConfig()` does not select them, so they do not automatically reach the foreground model as evolved sections. They can influence later foreground context indirectly if a later reflection promotes their content into a selected file. Optional `memory/session-log.jsonl` is separate raw-history context named by the teaching prompt; a default path/seed is not proof of active population. Its production writer was not established by the bounded search for `session-log` and `session_log` references. That uncertainty prevents claiming a complete historical record. [SRC-1: `src/evolution/subprocess-prompt.ts`, `src/evolution/config.ts`, `src/evolution/engine.ts`]

> - memory/principles.md: distilled strategic principles from repeated observations.
> --- `src/evolution/subprocess-prompt.ts`

#### MEM-OBJ-working-memory
Label: Foreground working memory file

Source-native identity: `data/working-memory.md`. Filesystem natural-language notes are seeded by startup and automatically read during prompt assembly. Foreground instructions ask the agent to maintain preferences/project facts/corrections, summarize near 50 lines and remove facts already adopted into evolved sections. Known lineage is startup seed plus afforded agent edits; actual deployed authorship and exercised compaction are unobserved. No counterpart object is declared in runtime, although [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) covers its authority channel. [SRC-1: `src/index.ts`, `src/agent/prompt-blocks/instructions.ts`, `src/agent/prompt-blocks/working-memory.ts`]

The formatter retains the first three and last seventy lines when the file exceeds 75 lines, plus a warning asking for compaction. It does not rewrite the source. Line caps are not token caps; long lines remain possible. Automatic text says “Trust them,” even though file provenance is not authenticated by the formatter. Omitted middle text remains available for direct file reading. [SRC-1: `src/agent/prompt-blocks/working-memory.ts`]

> const header = lines.slice(0, 3);
> const recent = lines.slice(-(MAX_LINES - 5));
> --- `src/agent/prompt-blocks/working-memory.ts`

#### MEM-OBJ-agent-notes
Label: Agent-owned append notes

Source-native identity: `phantom-config/memory/agent-notes.md`; natural-language filesystem notes. Main-agent instructions request short dated entries for durable preferences, discoveries and hidden constraints, not task-state logs. Docker startup can seed a missing file; subsequent agent-generated entries are afforded, not observed. Unlike [MEM-OBJ-working-memory](#mem-obj-working-memory), this file is intentionally not injected by prompt assembly. This is a distinct object absent from runtime's declarations. [SRC-1: `src/agent/prompt-blocks/agent-memory-instructions.ts`, `src/agent/prompt-assembler.ts`, `scripts/docker-entrypoint.sh`]

Future foreground Read/Grep and reflection Read are afforded readers. Dashboard exposes it read-only. The instruction's “Nothing else reads from it for you” is not a literal global claim: reflection can read it and the dashboard displays it. Append-only is natural-language guidance for foreground tools; reflection's admission check treats modifications as violations, but foreground writes do not traverse that check. [SRC-1: `src/evolution/subprocess-prompt.ts`, `src/evolution/invariant-check.ts`, `src/memory-files/storage.ts`]

> "- Append new entries at the end of the file. Never rewrite or reorder older",
> "  entries. Never delete anyone else's entry. Never reorganize the file.",
> --- `src/agent/prompt-blocks/agent-memory-instructions.ts`

#### MEM-OBJ-evolution-queue
Label: Retained evolution inputs and rejection state

Source-native identity: SQLite `evolution_queue`, `evolution_queue_poison` and transient `.staging` JSONL. Session-summary user/assistant arrays and gate reasons are natural-language evidence; IDs/retry counts/dispositions are symbolic control metadata. This is not a full tool transcript: channel caller supplies empty tools, tracked file paths and prefix-derived outcome. Feedback submissions carry empty message arrays; the gate also sets reactions to `(none)`, so feedback direction/content is not fully represented to that selector. Distinct from [RT-OBJ-session-store](runtime.md#rt-obj-session-store) and the consuming [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission). [SRC-1: `src/evolution/queue.ts`, `src/evolution/gate.ts`, `src/index.ts`]

Queue enqueue replaces the previous row for the same conversation key. Cadence drains rows in age order; reflection receives staged summaries plus gate source/reason. Clean ok/skip deletes queue rows; transient errors keep them without retry increment; invariant failures increment retry and move rows to poison at three. Poison listing is a library capability; no automatic reinjection into reflection was established. Staging is removed best effort, not durable memory rationale. [SRC-1: `src/evolution/queue.ts`, `src/evolution/cadence.ts`, `src/evolution/batch-processor.ts`, `src/evolution/reflection-subprocess.ts`]

> this.db.run("DELETE FROM evolution_queue WHERE session_key = ?", [sessionKey]);
> --- `src/evolution/queue.ts`

#### MEM-OBJ-evolution-log
Label: Evolution metadata and reasons

Source-native identity: version JSON, gate/evolution JSONL and metrics under `phantom-config/meta`. Symbolic version/status/counters and session IDs accompany natural-language change summaries, gate reasons and failure messages. These are separate from retained instruction content. No supplied object counterpart exists; [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) describes their producing admission process. [SRC-1: `src/evolution/gate.ts`, `src/evolution/versioning.ts`, `src/evolution/reflection-subprocess.ts`]

Commit builds one change per touched file, preserving sentinel summary or a mechanical line-count description. Its `rationale` is a drain/count string, not the reflection model's argument. Teaching instructions omit dates/session IDs from bullets because version history carries them. MCP config/changelog resources and engine/dashboard-facing accessors can read metadata; ordinary evolved prompt rendering does not include these reasons. Thus some lineage survives outside the instruction, but no generic per-bullet evidential justification or automatic rationale read-back is established. Snapshots are transient rollback maps, not a retained repository of every prior file version. [SRC-1: `src/evolution/subprocess-prompt.ts`, `src/evolution/reflection-subprocess.ts`, `src/evolution/versioning.ts`, `src/mcp/resources.ts`, `src/agent/prompt-blocks/evolved.ts`]

> const rationale = `drain=${drainId} sessions=${sessionIds.length}`;
> --- `src/evolution/reflection-subprocess.ts`

#### MEM-OBJ-chat-transcript
Label: Committed chat transcript

Part of: [RT-RTE-durable-chat](runtime.md#rt-rte-durable-chat)

Containment is cross-kind: this object is the route's committed-message state, not another declaration of its progression. Source-native identity: SQLite `chat_messages.content_json` plus attachment metadata/files. User and successful assistant text are natural language; sequence/session/status and attachment descriptors are symbolic access data; binary attachments remain separate payloads, not readable text merely because a filename is shown. Writer commits user content before querying and assistant text after successful completion; an error can leave events without a committed assistant message. Later consumers are browser history and the bound transcript-search tool. [SRC-1: `src/chat/writer.ts`, `src/chat/transcript-search.ts`]

Transcript recovery extracts/redacts text and attachment descriptors, not binary content or complete SDK reasoning/tool history. Soft-deleted sessions are excluded from search, and sweep eventually hard-deletes their rows/files. A fork records parent ID/message sequence but inspected `fork()` only inserts a new session row; it does not itself copy transcript or SDK state. No fork-history prompt inheritance is established by the searched production references. [SRC-1: `src/chat/session-store.ts`, `src/chat/transcript-search.ts`, `src/chat/sweep.ts`]

> const transcriptContent = options?.transcriptContent ?? userText;
> --- `src/chat/writer.ts`

#### MEM-OBJ-chat-events
Label: Durable translated chat events

Part of: [RT-RTE-durable-chat](runtime.md#rt-rte-durable-chat)

This object is the route's event state, distinct from its committed messages. Source-native identity: SQLite `chat_stream_events.payload_json`, translated wire frames with symbolic event identities/sequence/status and natural-language text/tool previews. These are host event traces, not the opaque provider transcript. `session.compact_boundary` retains trigger/pre-token metadata, not a model-generated summary of everything removed. Event replay serves browser reconnect; continuity scans the recent tail for checkpoints/page-tool artifacts. [SRC-1: `src/chat/event-log.ts`, `src/chat/writer.ts`, `src/chat/continuity-context.ts`]

Startup wires a sweep; the sweep removes events older than 24 hours, including those of undeleted sessions. Therefore event-based checkpoints and artifact extraction have a shorter horizon than committed messages or durable timelines. [SRC-1: `src/index.ts`, `src/chat/sweep.ts`]

> const EVENT_HOURS = 24;
> --- `src/chat/sweep.ts`

#### MEM-OBJ-chat-timelines
Label: Durable derived run timelines

Part of: [RT-RTE-durable-chat](runtime.md#rt-rte-durable-chat)

This is the route's derived timeline state, not an alias of raw events or [RT-OBJ-chat-context](runtime.md#rt-obj-chat-context). Source-native identity: SQLite `chat_run_timelines.summary_json`, code-derived run/tool/artifact summaries from translated events. Symbolic status, sequence and artifact fields accompany readable labels/output summaries. These retain selected activity even after raw event expiry; no model distillation or learned rule is implied by the summary label. Browser timeline consumers and continuity's page-artifact extractor read them. [SRC-1: `src/chat/run-timeline.ts`, `src/chat/writer.ts`, `src/chat/continuity-context.ts`]

Continuity loads page artifact summaries from timelines as well as recent events. Its current checkpoint list, however, comes from event compact-boundary frames; storing a timeline compact summary does not show its automatic reinjection as a checkpoint. Session hard deletion explicitly deletes timelines. [SRC-1: `src/chat/continuity-context.ts`, `src/chat/session-store.ts`]

> summary_json = excluded.summary_json,
> --- `src/chat/run-timeline.ts`

#### MEM-OBJ-user-memory
Label: Dashboard user-scope memory files

Source-native identity: eligible `.md` files beneath the user `.claude` root (environment-overridable), excluding reserved skills/plugins/agents and hidden paths. Natural-language filesystem instructions have symbolic path/mtime/size access metadata; audit actor labels do not authenticate authorship. Distinct from [MEM-OBJ-agent-notes](#mem-obj-agent-notes), which the dashboard only surfaces through a separate read-only virtual path. The operator extension route [RT-RTE-operator-config](runtime.md#rt-rte-operator-config) covers other reserved surfaces, not these files. [SRC-1: `src/memory-files/paths.ts`, `src/memory-files/storage.ts`, `src/ui/api/memory-files.ts`]

Dashboard callers can create/edit/delete these files. Foreground SDK calls request project/user settings, but this does not prove the SDK automatically consumes every arbitrary Markdown file exposed by the dashboard. Exact SDK file selection and downstream authority remain uninspected. Known direct reader is the dashboard, and generic agent filesystem reads are afforded. [SRC-1: `src/memory-files/storage.ts`]; supplied [RT-RTE-operator-config](runtime.md#rt-rte-operator-config).

> const MAX_BYTES = 256 * 1024; // 256 KB per memory file
> --- `src/memory-files/storage.ts`

### Routes

#### MEM-RTE-vector-extraction
Label: Channel trace vector extraction

Distinct from [RT-RTE-channel-work](runtime.md#rt-rte-channel-work): this is its nonblocking retained-memory transformation after delivery, not foreground execution. Trigger/owner: channel callback after each response, despite the session-end label. The in-process conversation accumulator supplies all collected user/assistant messages for that key, but the heuristic extractor uses user text and metadata, not assistant reasoning. Code proposes/admits episodes and facts without per-content human approval; the user authored source text, not the extraction verdict. Outcome prefix and regex matches are not truth oracles. Operating mode is open conversations. [SRC-1: `src/index.ts`, `src/memory/consolidation.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: counts of created episodes/facts and elapsed time; zero detected procedures.
- Later read-back: stored episode/fact payloads can reach automatic query context or requested MCP/dashboard lookup.
- Delegated visibility: Ollama receives selected text for embedding; later foreground model receives formatted projections, not the consolidation input arrays.
- Selection predicate: memory ready; correction/preference pattern matches on user messages; one episode for every call, potentially re-extracting earlier accumulated messages.
- Invalidation or expiry: fact store may date out prior candidates; dashboard deletion removes individual payloads; no generic extraction rollback or episode/fact transaction is shown.
- Activation or effect: durable write and later retrieval are wired; changed decisions and benefit are unobserved.
- Evidence limits: error-prefix outcomes are not verified success; repeated conversation input can generate repeated facts/episodes; web and direct callers do not traverse this callback merely by sharing runtime.

Fact admission attempts heuristic supersession before storing the new fact; storage/embedding failure can interrupt the sequence, so counts and old validity changes are not evidence of an atomic update. Guidance is static extraction patterns rather than a model curator. Recovery is logging the nonblocking error or later deletion, not semantic rollback. [SRC-1: `src/memory/semantic.ts`, `src/index.ts`]

> proceduresDetected: 0,
> --- `src/memory/consolidation.ts`

#### MEM-RTE-vector-context
Label: Automatic vector context selection

Distinct from the general execution [RT-RTE-channel-work](runtime.md#rt-rte-channel-work) and artifact supplement [RT-RTE-chat-context](runtime.md#rt-rte-chat-context). Code triggers the builder on foreground query text, automatically pushes selected retained material into appended prompt context, and owns selection. Main model owns subsequent decisions. Both channel and chat query helpers call the builder when wired/appropriate text is available. [SRC-1: `src/memory/context-builder.ts`, `src/agent/runtime.ts`, `src/agent/chat-query.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted memory context string or empty string after unavailable/failed retrieval.
- Later read-back: prior stored facts, episodes and one procedure become future model input.
- Delegated visibility: model sees fact text/confidence; episode type/summary/outcome/relative age; procedure name/trigger/confidence/counters/actions. IDs, episode details, fact source episodes and procedure conditions are omitted.
- Selection predicate: current query embeddings plus hashed sparse query; episode recency/durability reranking and inclusion filter; valid facts by default; one procedure above threshold. Shipped limits are 10 episodes, 20 facts and a 50,000 estimated-token memory budget.
- Invalidation or expiry: dated-out facts are omitted by default; episode age/access affects rank and context admission, not physical deletion; each invocation rebuilds the string.
- Activation or effect: selected content reaches the model as natural-language guidance; neither complete recall nor model compliance is demonstrated.
- Evidence limits: estimate is characters divided by four, not tokenizer accounting; procedure_limit 5 is configured but builder calls singular findProcedure; budget does not include the rest of the assembled prompt.

Facts have priority but their entire section is omitted if too large; it is not progressively clipped. Episodes require over 500 remaining estimated tokens and stop at the available character budget; procedure requires over 200 remaining and must fit as a whole. Episodic metadata updates are attempted before final context admission; a retrieval access therefore does not prove exposure or use. `updatePayload` forwards `$inc`-shaped values as ordinary payload data; without inspecting/executing Qdrant semantics, intended counter reinforcement is not established as a working increment. [SRC-1: `src/memory/context-builder.ts`, `src/memory/episodic.ts`, `src/memory/qdrant-client.ts`]

> const factTokens = this.estimateTokens(factSection);
> if (factTokens <= tokenBudget) {
> 	sections.push(factSection);
> 	tokenBudget -= factTokens;
> }
> --- `src/memory/context-builder.ts`

#### MEM-RTE-memory-tools
Label: Requested memory lookup

Distinct from [MEM-RTE-vector-context](#mem-rte-vector-context): foreground agent or external MCP client requests retrieval rather than receiving unsolicited automatic selection. Registration is wired through startup/in-process factories and MCP server registration. [SRC-1: `src/index.ts`, `src/mcp/server.ts`, `src/agent/in-process-reflective-tools.ts`, `src/mcp/tools-universal.ts`, `src/mcp/resources.ts`, `src/mcp/tools-swe.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON text with recalled payloads or resource-specific projections/errors.
- Later read-back: prior episodes/facts/procedures or fresh disk-loaded evolved configuration/changelog reach requesting clients; main agent gets its tool results.
- Delegated visibility: in-process memory tool returns episode/fact payloads; external tools can additionally return a procedure; resource and SWE query projections vary, not necessarily complete evidence.
- Selection predicate: requester query/type/limit; tools cap per-type results at 50, default 10. In-process days_back enters episode/fact store time-range filters; external days_back post-filters only returned episodes. Resources use fixed recent-activity query/10 or topic query/20 facts; SWE codebase query uses 5 episodes and 10 facts plus evolved text.
- Invalidation or expiry: current store validity/deletion applies; time-range fact search can include expired facts; no persistent copy or automatic adoption of tool output is established here.
- Activation or effect: tool/resource delivery is wired, not proof that a client trusts or acts on it.
- Evidence limits: in-process description mentions optional procedures but implementation searches only episodes/facts; external caller deployment and actual invocations are unobserved. A supplied topic is a query, not proof of a hard category filter.

External grants follow runtime's MCP admission account; this route is read-only except incidental episode-access updates. The `thread` skill's requested broad lookup is doctrine/design, not evidence it fired. [SRC-1: `skills-builtin/thread/SKILL.md`]; supplied [RT-RTE-dynamic-tools](runtime.md#rt-rte-dynamic-tools) for external scope limitations.

> opts.timeRange = { from: daysAgo(input.days_back), to: new Date() };
> opts.strategy = "temporal";
> --- `src/agent/in-process-reflective-tools.ts`

#### MEM-RTE-foreground-notes
Label: Foreground note maintenance

Distinct from [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission): foreground model writes working memory or agent notes through ordinary filesystem tools under foreground permissions. Instructions request content selection and maintenance; there is no dedicated note-write API or independent semantic reviewer in this path. Human input can supply preferences, but no per-entry human approval is required. Operating mode is open user work; there is no fixed answer oracle. [SRC-1: `src/agent/prompt-blocks/instructions.ts`, `src/agent/prompt-blocks/agent-memory-instructions.ts`]; supplied [RT-RTE-channel-work](runtime.md#rt-rte-channel-work).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: ordinary SDK file-tool result; no separate durable-learning verdict.
- Later read-back: working-memory file is automatically projected into later prompts; agent notes require tool reading or later reflection reading.
- Delegated visibility: current foreground model gets note-writing guidance and the selected working-memory text; append notes stay out unless explicitly read.
- Selection predicate: model judges durable preferences/facts/gotchas under the supplied writing rules; automatic working-memory selection uses line bounds rather than topical relevance.
- Invalidation or expiry: working-memory instructions request consolidation/removal of adopted or obsolete facts; agent notes request append-only entries; no automatic expiry or common rollback gate is established.
- Activation or effect: tool capability plus maintenance guidance affords durable edits and later use; exercised edits and improvement remain unobserved.
- Evidence limits: append-only and compaction instructions do not prove compliance. Ordinary shell/file effects can bypass note-specific intent; known startup seeds are not learned observations.

These writes can retain user instructions and agent-discovered patterns, so their trace origin is mixed. Reasons can be included in prose but are not structurally required or separately authenticated. This is experience-fed retention capacity, not demonstrated improved future-action capacity. No source-supplied content-directed criticism/revision episode warrants a theory-builder assessment beyond runtime's bounded reflection account.

#### MEM-RTE-transcript-recovery
Label: Bound chat transcript recovery

Distinct from [RT-RTE-chat-context](runtime.md#rt-rte-chat-context): that route automatically supplies artifact/checkpoint metadata and a reload instruction; this route is the foreground model's optional tool request returning committed conversational snippets. [SRC-1: `src/agent/in-process-reflective-tools.ts`, `src/chat/transcript-search.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: cited, redacted transcript snippets with sequence/role/status/date and attachment descriptors, or scope error.
- Later read-back: committed prior user/assistant messages become a later tool result after details leave provider context.
- Delegated visibility: foreground model receives text snippets and `chat:<session>#msg:<seq>` citations; binary attachments, omitted structured content and full SDK internal history are not supplied.
- Selection predicate: tool is bound to current chat session ID and rejects any other; optional role and before/after sequence constrain descending candidates; up to 2,000 rows scanned for a query, default 10/max 50 results, first 12 query tokens, 700-character snippets.
- Invalidation or expiry: soft-deleted sessions are excluded; hard deletion removes transcript; source remains after clipping/redaction, but returned snippets are not a full restoration.
- Activation or effect: bounded reload is wired and asked for by continuity instructions; actual invocation or changed task performance is unobserved.
- Evidence limits: lexical phrase/all-token match is not semantic search; no guarantee of finding old material beyond the scan window or recovering every compacted tool result.

The request has no independent content admission: query/role/session guards control access, and redaction filters output. It cannot recreate reasoning removed by the opaque SDK. [SRC-1: `src/chat/transcript-search.ts`]

> if (input.session_id !== options.currentChatSessionId) {
> 	return err("Transcript search is restricted to the current Phantom chat session.");
> }
> --- `src/agent/in-process-reflective-tools.ts`

#### MEM-RTE-operator-memory
Label: Operator memory inspection and withdrawal

Distinct from [RT-RTE-operator-config](runtime.md#rt-rte-operator-config): this route targets vector payload deletion and memory Markdown CRUD, not YAML/extensions. Authenticated caller selects content; the API does not independently establish a human behind each request. The dashboard's confirmation intent is not per-content human approval enforced in the memory API itself. [SRC-1: `src/ui/api/memory.ts`, `src/ui/api/memory-files.ts`, `src/memory-files/storage.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: list/detail/status/error; vector DELETE confirms deletion, file writes return saved/read-back content and retain audit inputs.
- Later read-back: later vector queries omit deleted points; dashboard sees modified Markdown, while arbitrary SDK Markdown loading remains uninspected.
- Delegated visibility: operator/client receives payloads or file content; automatic model injection is a separate route.
- Selection predicate: cookie-authenticated dispatch, vector type/ID/query validation; Markdown relative-path/extension/reserved-tree checks, existence rules and 256 KiB content cap; agent-notes virtual path rejects writes/deletes.
- Invalidation or expiry: vector point deletion and file rewrite/delete are explicit withdrawals; Markdown save uses temporary file/rename, not semantic version rollback.
- Activation or effect: storage mutation is wired; revocation of already injected text, external copies, SDK history or derived facts is not established.
- Evidence limits: deleting an episode does not show cascading deletion of its extracted facts; queryless dashboard browsing and query recall have different validity/filter behavior. Path checks are not a security audit of symlink/OS confinement.

No semantic truth/quality oracle gates caller-authored files; software rejects invalid shapes/paths/sizes/existence and protected virtual paths. Recovery requires rewriting/recreating or separate backup, not an admission transaction spanning all memory stores. [SRC-1: `src/memory-files/storage.ts`, `src/ui/api/memory.ts`]

> await deleteItemById(deps, type, idParsed.data);
> return json({ deleted: true, id: idParsed.data });
> --- `src/ui/api/memory.ts`

### Claims

#### MEM-CLM-universal-memory
Label: Universal memory production and nightly maintenance claims

Doctrine/design says web chat produces the same episodic/semantic/procedural memories as Slack and describes nightly episode compression/pattern promotion/pruning. Inspected callers instead place vector extraction only in the channel callback; extraction detects zero procedures. Shared read access does not establish equivalent write behavior. This specializes and qualifies the broad accumulating-memory claim [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker), not a duplicate assertion of its wording. [SRC-1: `docs/memory.md`, `src/index.ts`, `src/chat/writer.ts`, `src/memory/consolidation.ts`]

> All channels share the same memory system. A conversation in the web chat at `/chat` produces the same episodic, semantic, and procedural memories as a Slack conversation. Switching channels does not lose context.
> --- `docs/memory.md`

The document also calls episodes session transcripts, whereas consolidation preserves a first-message summary and sparse metadata. Its top-five-procedures description exceeds the inspected builder's singular lookup. These are source conflicts, not evidence of absent deployments or of every external writer. [SRC-1: `docs/memory.md`, `src/memory/context-builder.ts`, `src/memory/consolidation.ts`]

### Evidenced absences

#### MEM-ABS-procedure-learning
Label: Shipped automatic procedure learning not established

- implementation conclusion status: absent

At this frozen revision, searched non-test `src/` for `storeProcedure(`, `updateProcedureOutcome(`, consolidation/nightly references, and inspected `src/memory/system.ts`, `src/memory/procedural.ts`, `src/memory/consolidation.ts`, `src/index.ts`. Store/outcome methods exist, but search found no shipped callers of those two public write methods; consolidation explicitly returns zero procedures and the class method named `consolidateSession` is a no-op. No nightly vector maintenance wiring was established in that bounded source search. The supported absence is a shipped automatic trace-to-procedure call chain in those roots, not procedure storage/read capacity, external writers or future versions. Distinct from [RT-ABS-task-executor](runtime.md#rt-abs-task-executor), which concerns task execution rather than memory creation. [SRC-1: `src/memory/system.ts`, `src/memory/consolidation.ts`, `src/memory/procedural.ts`, `src/index.ts`]

> async consolidateSession(_sessionId: string): Promise<ConsolidationResult> {
> 	return { episodesCreated: 0, factsExtracted: 0, proceduresDetected: 0, durationMs: 0 };
> }
> --- `src/memory/system.ts`

### Behavioral-authority paths

none declared in this member. [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) already declares the foreground channel; object/route findings above qualify its selected parts and limits rather than redeclaring it.

## Annotations

#### On [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission)

Memory lineage and consumers: gate selects using only first/last user snippets (240 characters each), last assistant snippet (400), counts/outcome/cost and placeholder reactions; retained queue can carry longer message arrays. A queue row is replaced per conversation key. Reflection sees staged JSONL, current files and teaching guidance, can skip observations, promote across files, rewrite or compact content. These are requested model transformations, not observed quality gains. Raw inputs are [MEM-OBJ-evolution-queue](#mem-obj-evolution-queue); derived consumers differ between [MEM-OBJ-evolved-files](#mem-obj-evolved-files) and [MEM-OBJ-reflection-context](#mem-obj-reflection-context). [SRC-1: `src/evolution/gate.ts`, `src/evolution/queue.ts`, `src/evolution/subprocess-prompt.ts`, `src/evolution/engine.ts`]

Write agency is computational proposal/edit plus branch-limited software rejection; source user corrections do not establish per-edit human control. Rationale retention is limited as [MEM-OBJ-evolution-log](#mem-obj-evolution-log) states. A later reflection can read current rules, but a foreground evolved prompt receives neither all supporting traces nor generic per-entry reasons.

Correction to supplied read-back qualification: `compact` is a **change action/type**, not an accepted top-level status. `SubprocessStatus` and `isSentinelShape` admit only ok/skip/escalate. Normal compaction is status ok with a compact action and therefore follows the changed-ok callback. A top-level compact sentinel is parse failure, defaults to ok without annotation, and still undergoes checks. The comment “ok / compact path” does not establish a separate compact result state. Runtime's claim that compact status can commit without live refresh is unsupported at this pin. [SRC-1: `src/evolution/types.ts`, `src/evolution/reflection-subprocess.ts`, `src/evolution/engine.ts`]

> if (status !== "ok" && status !== "skip" && status !== "escalate") return false;
> --- `src/evolution/reflection-subprocess.ts`

The real skip/snapshot limitations remain: skip returns without comparing/restoring state, and meta/staging are excluded from snapshot coverage. These supplied findings retain their supporting passages in the runtime record. Accepted changes reach only the fixed evolved loader automatically; corrections/principles may instead influence later reflection. No theory/learning/property status is inferred merely from this delivery.

#### On [RT-OBJ-chat-context](runtime.md#rt-obj-chat-context)

Backing-store lineage has three distinct parts: committed transcript, transiently retained event traces, and durable derived timelines. Artifact extraction combines timelines and events, while checkpoint metadata is extracted from recent events. Neither readable artifact summaries nor compact-boundary counters are the SDK's opaque retained summary. [SRC-1: `src/chat/continuity-context.ts`, `src/chat/run-timeline.ts`, `src/chat/event-log.ts`]

#### On [RT-RTE-chat-context](runtime.md#rt-rte-chat-context)

Read-back horizons: recent event tail is capped at 5,000; page artifacts at eight; checkpoint records at three. Event sweep removes frames older than 24 hours, but timeline page summaries can supply artifacts afterwards. This qualifies durable continuity without denying the route. Reload instruction is backed by [MEM-RTE-transcript-recovery](#mem-rte-transcript-recovery), not just a hypothetical API. Provider-owned summaries and remaining verbatim context cannot be reconstructed from these host metadata alone. [SRC-1: `src/chat/continuity-context.ts`, `src/chat/sweep.ts`, `src/agent/in-process-reflective-tools.ts`]

#### On [RT-OBJ-session-store](runtime.md#rt-obj-session-store)

Memory storage distinction: SQLite SDK IDs/access timestamps are symbolic access metadata, not the dependency-owned transcript they select. Expiry/retry can abandon an SDK history without deleting vector memory, file notes or committed web transcript. Those stores use separate selectors and withdrawal rules; SQL row presence is not evidence of readable or complete SDK history. [SRC-1: `src/agent/session-store.ts`; supplied supporting runtime record]

## Write side

Admission mechanisms remain separate:

- **Heuristic vector writes:** automatic code extracts user-message fragments; same-subject similarity/confidence may invalidate old facts. Failure/error labels are caller conventions, not evaluations of correctness. Existing procedure state can still be read despite unresolved initialization and absent shipped automatic procedure learning. [MEM-RTE-vector-extraction](#mem-rte-vector-extraction), [MEM-OBJ-procedures](#mem-obj-procedures).
- **Reflection:** gate model can decline, failsafe enqueues on error, cadence batches, reflection edits before software post-check, and invariant failure attempts restoration. Clean skip deletes queue inputs despite bypassing post-state verification. Invariant failures retry then enter poison; transients stay queued. The actual cadence does not immediately poison credential failures through `moveToPoisonPile`; that method's existence is not a wired exceptional policy. [MEM-OBJ-evolution-queue](#mem-obj-evolution-queue), [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission); SRC-1: `src/evolution/cadence.ts`, `src/evolution/queue.ts`.
- **Foreground notes/files/capabilities:** ordinary model filesystem actions can bypass reflection admission. Working-memory rewriting and agent-note append instructions are model-followed rules. Skills/subagents/hooks and dynamic code have their own runtime admission, not evidence of a common knowledge reviewer. [MEM-RTE-foreground-notes](#mem-rte-foreground-notes), [RT-RTE-operator-config](runtime.md#rt-rte-operator-config), [RT-RTE-dynamic-tools](runtime.md#rt-rte-dynamic-tools).
- **Caller edits and withdrawal:** memory files are validated then written atomically per file; vector deletion has ID/type checks. Caller identity is not established as human per content, and no cross-store cascade retracts already-derived facts or injected context. [MEM-RTE-operator-memory](#mem-rte-operator-memory).
- **Chat trace transformations:** user/assistant commits and translated frames feed code-generated timeline summaries; those summaries and recent compact-boundary metadata feed future artifact context. SDK compaction has an opaque raw-to-summary transformation; Phantom's removed-context reload uses committed transcript, not every discarded provider/tool item. Fork metadata alone is not a copied checkpoint. [MEM-OBJ-chat-transcript](#mem-obj-chat-transcript), [MEM-OBJ-chat-events](#mem-obj-chat-events), [MEM-OBJ-chat-timelines](#mem-obj-chat-timelines), [RT-RTE-chat-context](runtime.md#rt-rte-chat-context).

Reflection's teaching prompt requests obsolete-entry removal, duplicate merging, cross-file promotion, credential exclusion and constitution consistency. Post-checks establish narrow structural constraints, not that claims are true or improvements beneficial. Version metadata retains source session IDs and summaries, not the model's full reasons; automatic foreground reading omits even that metadata. The inspected e2e fixture asks for an exact durable marker and defines allowed/protected files; it is not observed production learning or a downstream benefit test. [SRC-1: `src/evolution/subprocess-prompt.ts`, `src/evolution/invariant-check.ts`, `src/evolution/versioning.ts`, `e2e/reflection-subprocess.spec.ts`]

## Read-back

The automatic push routes are query-driven vector selection, fixed evolved-file prompt loading, working-memory projection and chat artifact/checkpoint supplementation. “Automatic” here means code initiates selection during an invocation without a model memory-tool request; it does not mean an unsolicited new agent invocation. Inputs, selected parts and budgets differ. [MEM-RTE-vector-context](#mem-rte-vector-context), [MEM-OBJ-evolved-files](#mem-obj-evolved-files), [MEM-OBJ-working-memory](#mem-obj-working-memory), [RT-RTE-chat-context](runtime.md#rt-rte-chat-context).

Requested pull routes are in-process memory search, bound transcript snippets, direct Read/Grep of notes and external MCP/dashboard retrieval. A registered resource establishes an exposed client route, not a deployed external client or automatic main-agent use. Metadata-only session lookup selects an opaque SDK history; procedure write methods alone establish no later consumer route beyond the separately wired reads. [MEM-RTE-memory-tools](#mem-rte-memory-tools), [MEM-RTE-transcript-recovery](#mem-rte-transcript-recovery), [RT-OBJ-session-store](runtime.md#rt-obj-session-store).

Working-context control is selective by-value supply, not a reference-counted memory heap. The Murph transform removes previous tagged host supplements and inserts a replacement; it does not itself summarize all old turns. Line-based working-memory clipping omits middle content while leaving the file reachable; vector context omits details/provenance while leaving payloads available to tools. Reflection uses a separate context that reads selected batches/files and returns sentinel/results, not its whole reasoning context. The stack-frame analogy fits that separation only loosely: persistent file edits also escape, not just a return value. Exact dependency subagent frames, remaining transcript tails and opaque summary contents are uninspected. [RT-RTE-chat-context](runtime.md#rt-rte-chat-context), [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission), [MEM-RTE-vector-context](#mem-rte-vector-context).

Cleanup changes availability: events expire after 24 hours; deleted sessions' messages/timelines/attachments are removed after 30 days; vector point deletion is separate; old facts can remain stored but omitted from default recall. Suppression, deletion and retraction from a model's already-consumed context are not equivalent. [SRC-1: `src/chat/sweep.ts`, `src/chat/session-store.ts`, `src/memory/semantic.ts`, `src/ui/api/memory.ts`]

## Integration issues

1. **Correct the supplied compact-status claim.** [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) and runtime account describe compact status committing without refresh. Accepted statuses are ok/skip/escalate; compact action under ok receives the ordinary callback. Comment terminology is not status grammar. Evidence and exact parser passage are in the annotation above; SRC-1: `src/evolution/types.ts`, `src/evolution/reflection-subprocess.ts`, `src/evolution/engine.ts`. This changes the live-read-back conclusion, not the supported skip/snapshot weaknesses.
2. **Narrow “eligible for later evolved configuration consumption.”** Runtime groups corrections/principles with automatically loaded files. [MEM-OBJ-reflection-context](#mem-obj-reflection-context) distinguishes reflection readers from the foreground fixed loader in [MEM-OBJ-evolved-files](#mem-obj-evolved-files). New strategy files likewise need promotion or direct tool reading, not merely acceptance. Evidence: SRC-1 `src/evolution/engine.ts`, `src/agent/prompt-blocks/evolved.ts`, `src/evolution/invariant-check.ts`. No duplicate record is intended: these are retained parts absent as runtime object declarations.
3. **Do not equate ingress read sharing with write sharing.** [MEM-CLM-universal-memory](#mem-clm-universal-memory) preserves conflicting target doctrine. Channel extraction and web/direct work remain separate; procedure and nightly claims exceed the inspected shipped wiring. [MEM-RTE-vector-extraction](#mem-rte-vector-extraction), [MEM-ABS-procedure-learning](#mem-abs-procedure-learning), [RT-RTE-direct-work](runtime.md#rt-rte-direct-work). This corroborates runtime's channel/web qualification rather than correcting it.
4. **Retain local unknowns:** initial procedure/vector contents and admission; exact deployed embedding versions; SDK transcript/compaction/subagent bodies and activation; arbitrary user Markdown loading; population/reader completeness of optional session-log; exercised model note curation; literal Qdrant counter-update semantics. These prevent complete provenance, successful-recovery, counter-reinforcement and benefit claims, not the known retrieval/write paths. Relevant records: [MEM-OBJ-procedures](#mem-obj-procedures), [MEM-OBJ-retrieval-indexes](#mem-obj-retrieval-indexes), [MEM-OBJ-user-memory](#mem-obj-user-memory), [MEM-OBJ-reflection-context](#mem-obj-reflection-context), [MEM-RTE-vector-context](#mem-rte-vector-context), [RT-RTE-chat-context](runtime.md#rt-rte-chat-context).
5. **Preserve separate chat objects and horizons.** The three new chat objects are material parts of [RT-RTE-durable-chat](runtime.md#rt-rte-durable-chat), not replacements for it or duplicates of [RT-OBJ-chat-context](runtime.md#rt-obj-chat-context). Event expiry does not imply timeline or transcript expiry; timeline artifact persistence does not establish automatic checkpoint-summary reinjection. Source: SRC-1 `src/chat/continuity-context.ts`, `src/chat/sweep.ts`, `src/chat/session-store.ts`. No other possible duplicates were found after comparing supplied declarations; memory field additions to existing referents use annotations.

## Limitations and checks

Source identity was rechecked with Git HEAD and clean status before inspection: f8c7ab42d885936ee54abc785528000260f4acc5 at the boundary's registered SRC-1 root. The member's run ID, source identity and reviewed boundary equal the supplied values. New reads remained within that source and this attempt's supplied contracts; no prior analysis or sibling attempt was consulted. No target code/tests/providers/services were run.

Two exploratory searches named unavailable guessed paths (`src/chat/run-timeline-store.ts` and `src/db/migrations*`) and returned exit 2. They were not used as negative evidence: the actual timeline implementation was found/read at `src/chat/run-timeline.ts`, and deletion behavior was read in session-store rather than inferred from missing migrations. Search and selected code reading support the bounded absence above, not an exhaustive correctness/security audit.

Unknown deployed state, external SDK/storage semantics and missing run evidence prevent claims of exercised learning, complete context restoration, reliable semantic contradiction detection or beneficial self-improvement. This does not erase source-supported retention and later-consumer wiring. Runtime's independently bounded theory/learning account remains separate; this member does not infer those properties from memory labels.

Deterministic validation: the exact invocation-specific `commonplace-run validate-output` check passed after repairing three malformed nested citation labels. One intervening call had a mistyped invocation path and failed before checking the member; the corrected exact command returned: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The pass does not establish analytical acceptance or behavioral benefit.
