---
type: agentic-systems/types/agent-memory-analysis-report.md
description: "Memory mechanisms of instinctual-memory across its journal, Git fact store, controls, and later retrieval routes"
run-id: AAS-2026-10-01-instinctual-memory-01
source-identity: https://github.com/jasonkneen/instinctual-memory
reviewed-boundary: 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
report-status: complete
memory-comparison:
  scope: "The local append-only journal and its imported/session inputs; derived fact entities and their Git history; controls, checkpoint/dispositions and generated index used for admission, invalidation, processing position and lookup; CLI, service, hooks and writeback consumers. Excludes enclosing agent runtimes, their uninspected prompt assembly and permissions, provider internals, and static instructions except when ingested as source material."
  axes:
    storage_substrate:
      assessment: known
      values: [files, repo]
      evidence:
        files: {basis: wired, records: [MEM-OBJ-1, MEM-OBJ-3, MEM-OBJ-4, MEM-OBJ-5], note: "Journal JSONL and store state are local files; controls and processing state are retained beside the Git fact store."}
        repo: {basis: wired, records: [MEM-OBJ-2], note: "Entities and facts are published as snapshots in the bare memory Git repository."}
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3, MEM-OBJ-4, MEM-OBJ-5]
      note: "Covers the journal, Git-backed facts, controls and processing/index files. The optional local reranker model is a retrieval dependency, not accumulated memory, so model-weights are excluded."
    representational_form:
      assessment: known
      values: [natural-language, symbolic]
      evidence:
        natural-language: {basis: wired, records: [MEM-OBJ-1, MEM-OBJ-2], note: "Journal content and fact statements are conversational or prose text."}
        symbolic: {basis: wired, records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3, MEM-OBJ-4, MEM-OBJ-5], note: "Events, structured fact fields, statuses, source references, controls, checkpoints, dispositions and index entries carry typed identifiers and relations."}
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3, MEM-OBJ-4, MEM-OBJ-5]
      note: "Both forms occur in the scoped retained parts; natural-language fact statements do not subsume their structured status and source fields."
    lineage:
      assessment: known
      values: [authored, imported, other-compiled, trace-extracted]
      evidence:
        authored: {basis: wired, records: [MEM-RTE-3], note: "An operator or live caller can author a fact through remember/correct requests."}
        imported: {basis: wired, records: [MEM-RTE-1, MEM-OBJ-1], note: "Curated project instruction files are ingested as note events and may become facts."}
        other-compiled: {basis: wired, records: [MEM-OBJ-5], note: "The generated entity index is compiled from the entity files for navigation."}
        trace-extracted: {basis: wired, records: [MEM-RTE-2, MEM-OBJ-1, MEM-OBJ-2], note: "Session events are transformed into derived facts with source references."}
      records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-5]
      note: "Includes direct fact authoring, imported notes, generated lookup structure and trace-derived facts."
    behavioral_authority:
      assessment: known
      values: [enforcement, instruction, knowledge, learning, ranking, routing, validation]
      evidence:
        enforcement: {basis: wired, records: [MEM-OBJ-3, MEM-RTE-3, MEM-RTE-6], note: "Suppression and deletion controls veto ordinary retrieval and prevent consolidation from restoring a forgotten or erased fact."}
        instruction: {basis: wired, records: [MEM-RTE-5, MEM-RTE-7], note: "Session-start guidance and written-back standing facts are supplied as directions to an agent or project instruction file."}
        knowledge: {basis: wired, records: [MEM-OBJ-2, MEM-RTE-4], note: "Fact content and journal passages are returned as evidence or context to a requesting caller."}
        learning: {basis: wired, records: [MEM-RTE-2], note: "Session traces feed an automatic update that creates durable fact artifacts for later invocations; this is a mechanism classification, not evidence of improved capacity."}
        ranking: {basis: wired, records: [MEM-OBJ-2, MEM-RTE-4, MEM-RTE-5], note: "Retained fact text and aliases are scored against the query and influence relative result order, including hook selection."}
        routing: {basis: wired, records: [MEM-OBJ-4, MEM-RTE-2], note: "The retained checkpoint chooses the next journal sequence window for consolidation."}
        validation: {basis: wired, records: [MEM-OBJ-2, MEM-OBJ-3, MEM-RTE-2, MEM-RTE-3], note: "Schemas and domain checks gate published fact changes, while controls block previously forgotten/deleted identities."}
      records: [MEM-OBJ-2, MEM-OBJ-3, MEM-OBJ-4, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4, MEM-RTE-5, MEM-RTE-6, MEM-RTE-7]
      note: "Forces are recorded at actual in-repository consumers. Host compliance with hook context and resulting agent behavior are outside this boundary."
    write_agency:
      assessment: known
      values: [automatic, manual]
      evidence:
        automatic: {basis: wired, records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-5], note: "Adapters append events and consolidation extracts facts; the session-end hook can start backfill and consolidation automatically."}
        manual: {basis: wired, records: [MEM-RTE-1, MEM-RTE-3], note: "Operators can ingest selected paths and callers can submit explicit remember/correct/forget requests."}
      records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-5]
      note: "A manually triggered operation can still perform automatic extraction; agency is classified by who authors the retained content."
    curation_operations:
      assessment: known
      values: [consolidate, dedup, evolve, invalidate]
      evidence:
        consolidate: {basis: wired, records: [MEM-RTE-2], note: "The extractor turns selected journal events into fact records while retaining their source references."}
        dedup: {basis: wired, records: [MEM-RTE-2], note: "Consolidation drops proposals that restate an existing active fact."}
        evolve: {basis: wired, records: [MEM-RTE-2, MEM-RTE-3], note: "A correction supersedes a prior fact; changed source files can also supersede facts sourced only from older versions."}
        invalidate: {basis: wired, records: [MEM-RTE-2, MEM-RTE-3, MEM-RTE-6], note: "Forget, supersession, expiry and erasure remove facts from current reliance; soft forget retains history, while erase rewrites it."}
      records: [MEM-RTE-2, MEM-RTE-3, MEM-RTE-6]
      note: "Inspected transformations support these four operations. Temporal eligibility is not a decay operation; no inspected route supports promotion or synthesis as defined by the comparison contract."
    read_back_direction:
      assessment: known
      values: [pull, push]
      evidence:
        pull: {basis: wired, records: [MEM-RTE-4], note: "A caller requests search, read or history by query or identifier and receives retained material."}
        push: {basis: wired, records: [MEM-RTE-5], note: "Installed Claude hooks add selected context at session start and on user prompt submission without an explicit memory request for that specific material."}
      records: [MEM-RTE-4, MEM-RTE-5, MEM-RTE-7]
      note: "Writeback is an explicitly invoked export route; the hook's automatic context injection establishes push."
    read_back_signal:
      assessment: known
      values: [coarse, inferred-lexical]
      evidence:
        coarse: {basis: wired, records: [MEM-RTE-5], note: "Session start supplies the preference entity and general memory guidance without query-specific selection."}
        inferred-lexical: {basis: wired, records: [MEM-RTE-5], note: "Prompt hooks select facts by lexical search followed by a minimum meaningful-word overlap with the current prompt."}
      records: [MEM-RTE-5]
      note: "The push boundary has both broad session-start context and prompt-conditioned lexical selection. No automatic identifier, embedding or model-judgment selector is wired in the inspected hook route."
    trace_learning:
      assessment: known
      values: ["yes"]
      evidence:
        "yes": {basis: wired, records: [MEM-RTE-2], note: "Journaled user turns can be automatically consolidated into durable facts later retrieved as context or standing guidance."}
      records: [MEM-RTE-1, MEM-RTE-2, MEM-OBJ-1, MEM-OBJ-2]
      note: "This classifies a wired trace-fed durable write, not demonstrated improvement. Static memory-file imports are not traces."
    trace_source:
      assessment: known
      values: [session-logs]
      evidence:
        session-logs: {basis: wired, records: [MEM-RTE-2, MEM-OBJ-1], note: "The qualifying automatic fact update consumes retained user turns from agent sessions."}
      records: [MEM-RTE-1, MEM-RTE-2, MEM-OBJ-1]
      note: "The qualifying trace-learning route's trace input is user session turns. Tool outputs and assistant turns are rejected by inspected extraction; imported instruction files are note inputs, not trace sources."
---

# instinctual-memory memory report

## Boundary and evidence

The subject is `mem` at commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`. The memory boundary includes its event journal, Git-backed entity facts, controls and processing metadata, generated lookup index, and their write, maintenance and later-consumer routes. It excludes enclosing hosts, provider internals, and any claim about agent uptake or benefit. The repository register is in the run overview: implementation evidence is `SRC-1`; README intent and integration description is `SRC-2`. The runtime member supplies the CLI, MCP, hook and writeback entry routes; the paths below were directly inspected to refine those routes.

| Entry point or operation | Directly inspected source | Records | Coverage or limit |
|---|---|---|---|
| Journal model and durable inputs | `src/journal.rs`, `src/cli.rs` | MEM-OBJ-1, MEM-RTE-1 | Session, imported note and other typed event inputs; no deployed ingestion trace. |
| Fact extraction, checkpoint and disposition | `src/consolidate.rs`, `src/checkpoint.rs` | MEM-OBJ-2, MEM-OBJ-4, MEM-RTE-2 | Rules and model extractors, bounded batches, filtering, retention and publication. Provider behavior is outside scope. |
| Fact schema, Git publication and generated index | `src/fact.rs`, `src/entity.rs`, `src/repo.rs`, `src/index.rs` | MEM-OBJ-2, MEM-OBJ-5 | Structured facts and versioned snapshots; generated index is a lookup structure, not a separate fact source. |
| Controls, correction, forget and erasure | `src/controls.rs`, `src/change.rs`, `src/erasure.rs`, `src/tidy.rs` | MEM-OBJ-3, MEM-RTE-3, MEM-RTE-6 | Inspected current-state invalidation, rejection and hard erasure paths. |
| Search, read, MCP/HTTP and hooks | `src/ops.rs`, `src/search/`, `src/mcp.rs`, `src/http_serve.rs`, `src/hook.rs`, `README.md` | MEM-RTE-4, MEM-RTE-5 | Pull APIs and installed Claude push hooks are wired in code/design; installation and host consumption are not observed. |
| Writeback and cleanup | `src/cli.rs`, `src/erasure.rs` | MEM-RTE-6, MEM-RTE-7 | Explicit writeback and erase mechanisms inspected; no evidence of resulting agent use. |
| Runtime seeded entry points | Supplied `runtime.md`; checked against paths above | OBJ-1, RTE-1, RTE-2, RTE-3 | Memory-specific annotations are below. No duplicate memory-only declaration of the shared executable or entry routes. |

The source does not contain execution traces, provider outputs, or host prompt records. Therefore it establishes wired mechanisms and declared integrations, not actual deployment, context acceptance, changed decisions, reliability, or improved capacity.

## Core ideas

The memory pipeline separates a durable append-only journal from a curated Git snapshot. Ingestion records source events; consolidation processes events after a retained checkpoint in bounded windows, publishes entity files and an index, then advances the checkpoint with per-event dispositions. The journal is outside Git, while derived facts and their revision history are inside the memory repository. Evidence: SRC-1 `src/journal.rs`, `src/consolidate.rs`.

Consolidation is selective, not a transcript summary. The rules extractor accepts a few user-statement patterns. The model extractor consumes user turns and imported memory files, asks for durable facts, checks that cited evidence occurs in its source event, and drops restatements. Assistant and tool turns and harness-injected text are filtered. These checks constrain provenance and admissibility but do not establish that paraphrased facts are true or useful. 

> Turns journal events into curated facts in the Git store. Two extractors:
> //! - **rules**: a few high-confidence regex patterns, no model call.
> //! - **llm**: sends user turns and memory files (AGENTS.md, CLAUDE.md, ...)
> //!   to an OpenAI-compatible chat endpoint in bounded batches and asks for
> //!   durable facts. A proposed fact is kept only when its evidence quote is
> //!   found verbatim in the event it cites, so the model cannot invent a
> //!   source. `Auto` picks llm when a key is configured, else rules.
> --- `src/consolidate.rs:3-9` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Facts carry entity, predicate, statement, kind, status, temporal fields, source references and visibility. Retrieval eligibility excludes superseded, retracted and expired facts and normally excludes disputed facts. Soft forgetting adds suppression/retraction controls and blocks later re-extraction; erasure removes content from the fact tree, redacts cited journal events and rewrites store history. Evaluation and tidy can identify retrieval failures or likely duplicates, but they do not by themselves improve the extractor or prove a quality gain. Evidence: SRC-1 `src/fact.rs`, `src/change.rs`, `src/controls.rs`, `src/erasure.rs`, `src/evaluation.rs`, `src/tidy.rs`.

> /// True if the fact is eligible for current-context retrieval at `now`.
>     ///
>     /// Excludes superseded, retracted, expired, and (optionally) disputed facts.
> --- `src/fact.rs:63-65` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Retrieval has requested and automatic paths. CLI, shell, MCP and HTTP callers can request search/read/history. Search combines eligible facts and raw journal events, uses lexical scoring, and may rerank the combined pool with a configured remote judge or local model. The installed Claude hook path adds session-start guidance/preferences and lexically selected facts for sufficiently long user prompts. The code constructs hook context, but the enclosing host's delivery and the model's use are outside the boundary. The optional reranker changes ordering; no retained policy or trace-fed parameter update is established.

## Shared records

### Components

none declared in this member.

### Operative objects

#### MEM-OBJ-1 — Source-event journal
- Closest supplied record: RTE-1 (the local invocation route); distinct object.
- Source-native identity: framed, append-only event records with role, source identity, timestamps, content, hash, scope and session metadata.
- Representational form: natural-language event content plus symbolic event/source fields.
- Storage substrate: per-day JSONL files under the store's journal directory, outside the Git snapshot.
- Lineage: imported session history, instruction-file note events, and supported event adapters.
- Consumers and authority: consolidation consumes eligible user and note events; search can return journal excerpts as knowledge. Other event roles can remain searchable even when excluded from fact extraction.
- Evidence: `src/journal.rs`, `src/cli.rs`, `src/consolidate.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-OBJ-2 — Entity fact snapshots
- Closest supplied record: OBJ-1 (the executable and service, not the stored facts); distinct object.
- Source-native identity: entity Markdown files with structured fact frontmatter and a human-readable body; each fact carries identifiers, status, source refs, visibility and temporal fields.
- Representational form: symbolic fact schema and natural-language statements.
- Storage substrate: bare local Git repository with versioned entity snapshots.
- Lineage: trace-extracted, imported from memory files, or authored by an explicit change request.
- Consumers and authority: search/read and prompt hooks return facts as knowledge; preferences and written-back facts can function as instruction; fact text affects lexical ranking.
- Persistence: retained across invocations in Git history until erased; current eligibility is filtered by status, time and controls.
- Evidence: `src/fact.rs`, `src/entity.rs`, `src/repo.rs`, `src/search/lexical.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-OBJ-3 — Retrieval and admission controls
- Closest supplied record: OBJ-1; distinct retained control object.
- Source-native identity: `state/controls.json` suppression, retraction, deletion and source-event redaction state.
- Representational form: symbolic identifiers and typed states with optional natural-language reason.
- Storage substrate: file in Git snapshots.
- Lineage: authored by forget/erase maintenance operations.
- Consumers and authority: retrieval filters facts using suppression/retraction/deletion state; consolidation blocks deleted or suppressed fact IDs; controls therefore carry enforcement and validation authority at those consumers.
- Evidence: `src/controls.rs`, `src/change.rs`, `src/consolidate.rs`, `src/search/lexical.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-OBJ-4 — Consolidation checkpoint and dispositions
- Closest supplied record: RTE-1; distinct processing state.
- Source-native identity: checkpoint sequence position plus per-request disposition records listing accepted and quarantined source event sequences.
- Representational form: symbolic JSON.
- Storage substrate: files in Git snapshots.
- Lineage: other-compiled from consolidation processing.
- Consumers and authority: checkpoint selects the next journal window; dispositions retain accepted/quarantined outcomes, but no later consumer that changes a subsequent extraction decision from disposition history was found in the inspected route.
- Evidence: `src/consolidate.rs`, `src/checkpoint.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-OBJ-5 — Generated entity index
- Closest supplied record: OBJ-1; distinct derived lookup structure.
- Source-native identity: generated `INDEX.md` entries for entity navigation.
- Representational form: symbolic identifiers and short natural-language labels.
- Storage substrate: file in Git snapshots.
- Lineage: other-compiled from entity files.
- Consumers and authority: index supports navigation/status, not the inspected content-ranking or fact-admission decision; actual memory content remains in entity files.
- Evidence: `src/index.rs`, `src/repo.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

### Routes

#### MEM-RTE-1 — Ingest source material into the journal
- Closest supplied record: RTE-1 and RTE-3; distinct memory progression within their invocation routes.
- Endpoints and owner: operator/host-selected session or file source → adapter/backfill/ingest → journal append; the caller selects paths or source integration.
- Retained input and persistence: supported conversation history and memory files become deduplicated journal events in per-day files; immediate result reports ingestion counts/errors.
- Later consumer: consolidation reads user and note events; search can return journal events.
- Status: implementation wired; no ingest execution observed.
- Selection/invalidation: source adapter and event identity select inputs; source-event redaction is performed by erase. Deduplication and source coverage vary by adapter.
- Evidence: `src/cli.rs`, `src/ingest.rs`, `src/journal.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-RTE-2 — Consolidate events into facts
- Closest supplied record: RTE-1; distinct automatic material transformation.
- Endpoints and owner: caller or session-end sync → checkpoint-bounded journal window → rules or model extractor → entity facts, index, checkpoint and dispositions in one publication.
- Retained input: user events and memory-file notes are eligible for the model route; rules use matching user statements. Assistant/tool events and injected harness text are rejected by the model route.
- Admission/rejection: source quote checks, lastingness/entity/evidence validation, blocked-ID check, duplicate rejection and domain validation govern acceptance. Rejected events receive dispositions; checkpoint advances through the bounded sequence window.
- Persistence/read-back: accepted facts persist in Git; later search/read/hooks/writeback can consume them. Dispositions are retained but not shown to feed later extraction decisions.
- Status: wired; provider call quality and real outcomes are unobserved.
- Evidence: `src/consolidate.rs`, `src/checkpoint.rs`, `src/repo.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-RTE-3 — Explicit remember, correction and soft forget
- Closest supplied records: RTE-1, RTE-2; distinct mutation path.
- Endpoints and owner: caller submits a validated request via CLI or `memory_request_change` → change operation → Git publisher and receipt; request fields determine entity, fact and target.
- Effects: remember upserts an authored fact; correct supersedes the target and upserts replacement; forget retracts and suppresses the target. A durable intent supports recovery and a receipt makes retries idempotent.
- Later read-back: changed facts are visible through later reads subject to eligibility and controls; forget blocks both ordinary retrieval and consolidation re-creation.
- Status: wired; caller access policy and operational invocation unobserved.
- Evidence: `src/change.rs`, `src/ops.rs`, `src/mcp.rs`, `src/controls.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-RTE-4 — Requested search, read and history
- Closest supplied records: RTE-1, RTE-2; distinct consumer operation.
- Endpoints and owner: CLI/shell/MCP/HTTP caller requests query or ID → common operation layer → eligible facts and/or raw journal → response to caller.
- Selection: query lexical match and optional reranker; optional project/scope/source filters and result limit. Identifier read/history addresses an entity, fact or journal event.
- Immediate return/later use: results are returned to caller; a later agent consumer is host-dependent. The request is pull, not a push selector.
- Invalidation: fact eligibility and controls filter retained facts; erasure redacts journal source content.
- Status: implementation wired; no host uptake or answer benefit observed.
- Evidence: `src/ops.rs`, `src/search/`, `src/mcp.rs`, `src/http_serve.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-RTE-5 — Installed hook context injection
- Closest supplied record: RTE-3; annotation records the memory-specific start, prompt and end paths.
- Endpoints and owner: installed Claude lifecycle hooks → `mem hook start` or `prompt` → constructed `additionalContext`; session-end starts background sync.
- Push trigger and selector: session-start returns preference facts and general memory guidance. User-prompt submission skips slash/short prompts, searches facts only against up to 600 prompt characters, then keeps at most six facts with two meaningful lexical terms in common (one for a one-term prompt).
- Budget/channel/persistence: six facts at prompt hook; context is emitted in hook JSON. Session start limits displayed preferences to 20. Hook context is ephemeral delivery; source facts persist in Git. Session-end can backfill and consolidate when threshold/configuration permits.
- Status: hook behavior wired and README describes setup; installation, host delivery, model consumption and changed behavior are unobserved. Hook errors are swallowed unless debug is enabled.
- Evidence: `src/hook.rs`, `src/setup.rs`, `README.md` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-RTE-6 — Tidy and hard erase
- Closest supplied record: RTE-1; distinct maintenance route.
- Endpoints and owner: explicit operator command → duplicate/session-only review or erase operation → fact/control/journal/history updates.
- Tidy can report candidate duplicates/session-only facts; applying it forgets selected facts while retaining history unless kept. Erase removes target facts from current entity files, redacts source events, records deletion, rewrites memory history and removes matching intents.
- Later consumer: controls block retrieval and re-extraction; erased source event content is replaced with a marker.
- Status: wired; no execution/recovery trace observed.
- Evidence: `src/tidy.rs`, `src/erasure.rs`, `src/controls.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### MEM-RTE-7 — Explicit writeback to project instructions
- Closest supplied record: RTE-1; distinct export consumer.
- Endpoints and owner: operator invokes writeback → active facts are grouped and written inside a managed block in a chosen project instruction file.
- Selection: project-specific facts and preferences; file-sourced facts are excluded by default. Superseded, retracted and expired facts are skipped; private facts are eligible for private local output. `--force` can replace the whole file.
- Persistence/consumer: output persists in the target file and can later be imported as a note event or read by an enclosing agent; external read and behavior are not observed.
- Status: implementation wired; no writeback run observed.
- Evidence: `src/cli.rs`, `README.md` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

### Claims

none declared in this member.

### Evidenced absences

none declared in this member; the runtime/source boundary's lack of traces is an evidence limitation, not evidence that hooks or consumers are absent.

### Behavioral-authority paths

none declared in this member; the declared routes carry the memory-specific effects and limits.

## Annotations

#### On OBJ-1 — Memory-specific stores and service routes
- Storage substrate: local journal files plus bare Git memory repository and related retained state files.
- Representational form: executable/service is not itself memory; the consumed retained objects are described by MEM-OBJ-1 through MEM-OBJ-5.
- Memory consumers and authority: CLI, MCP, HTTP, shell and hooks can search/read facts or events; hooks can inject context. Exposed service operation does not establish a host grant or actual use.
- Evidence: `src/ops.rs`, `src/mcp.rs`, `src/hook.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

#### On RTE-1 — Memory-specific local CLI paths
- Includes ingestion, consolidation, explicit changes, retrieval, tidy, erase and writeback; these operations have separate record IDs above because their retained effects and later consumers differ.
- Evidence and limits: `src/cli.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`; no CLI invocation supplied.

#### On RTE-2 — Memory-specific MCP operations
- MCP exposes requested search/read/history/status and explicit request-change operations through the shared operation layer. Requests pull returned material; they do not establish automatic injection.
- Evidence and limits: `src/mcp.rs`, `src/ops.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`; client registration/use unobserved.

#### On RTE-3 — Memory-specific hook and writeback operations
- Hook annotation: see MEM-RTE-5 for selectors, context limit and session-end write path. Writeback is separately recorded as MEM-RTE-7. These are distinct consumers within the supplied broad integration route.
- Evidence and limits: `src/hook.rs`, `src/cli.rs`, `src/setup.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`; actual installation and host use unobserved.

## Write side

Ingestion writes raw source events first. Conversation adapters and explicit file ingestion record source identity, role, scope/session and content. Memory instruction files enter as note events. Deduplication uses source identity and position/message ID, not content equality. The journal persists independently of Git fact snapshots.

Consolidation reads after a sequence checkpoint in a bounded batch, selects either deterministic rules or a configured model extractor, and writes accepted facts plus checkpoint and dispositions in one snapshot publication. The checkpoint also routes the next pass. The disposition file records accepted and quarantined sequence outcomes, but inspected code does not use those records as guidance for later proposals. Facts preserve source event IDs and evidence snippets; they do not retain a full explanation of the model's rationale or a later rationale consumer.

> let blocked: std::collections::HashSet<String> = controls
>             .suppressions
>             .keys()
>             .cloned()
>             .chain(controls.deletions.iter().map(|d| d.target.clone()))
>             .collect();
> --- `src/consolidate.rs:148-153` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Explicit changes permit authored remember/correct/forget operations. Correction supersedes an earlier fact; forget retracts and suppresses it. These operations use validation, compare-and-swap publication, durable intents and receipts. The “only path” comment in `change.rs` is scoped to live-agent authored changes: consolidation is a separate automatic write path, so the phrase does not describe all writes to memory.

> ChangeKind::Forget => {
>             let Some(mut entity) = current else {
>                 return Err(Error::InvalidChange(format!(
>                     "forget: entity {} does not exist",
>                     request.entity_id
>                 )));
>             };
>             let target = request.target_fact_id.clone().expect("validated");
>             entity.retract(&target)?;
> --- `src/change.rs:131-139` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Forget retains a suppressed historical fact; erase is a separate stronger operation. Erase redacts source events and rewrites history. Tidy's candidate report is not itself a curation change; only its apply path forgets selected facts. Expiry and validity fields filter eligibility but do not establish an implemented decay/downweighting process.

> for event_id in &source_events {
>         controls.add_redaction(event_id.clone());
>     }
> --- `src/erasure.rs:128-130` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

## Read-back

Search/read/history operations are caller-requested pulls. They return fact content, source-backed journal excerpts or status to CLI/service clients. Search matches both raw journal events and curated facts, filters fact eligibility and controls, applies scope/project/source/limit constraints, and may rerank. Scores and fact text can shape selection, but no observed retrieval quality or downstream activation is supplied.

Installed Claude hooks add a distinct push path. Session start can provide preferences and guidance; each qualifying user prompt triggers lexical fact search and term-overlap filtering. The selector is automatic once the host invokes the hook, and the context limit is six prompt facts. README describes this installation; source code constructs the hook response. The repository cannot show that the host installed the hook, delivered `additionalContext`, or that a model followed it.

> // Injected context has to earn its place: a fact must share at least
>     // two of the prompt's meaningful words (one when the prompt has only
>     // one), so a single incidental word match never pulls a fact in.
> --- `src/hook.rs:132-134` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> - `UserPromptSubmit` → `mem hook prompt`: the curated facts that match the message (a fact must share at least two meaningful words with it; short prompts and slash commands are skipped). Lexical only, about half a second, no network.
> --- `README.md:114-114` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Writeback is an explicitly invoked export rather than an automatic selector. It copies eligible project facts and user preferences into a managed instruction-file block. That creates durable authored-project context, but no evidence establishes that the receiving agent reads the file later. File-derived facts are excluded by default to avoid copying instructions back into themselves.

> for fact in &entity.facts {
>             if matches!(
>                 fact.status,
>                 crate::fact::FactStatus::Superseded
>                     | crate::fact::FactStatus::Retracted
>                     | crate::fact::FactStatus::Expired
>             ) {
>                 continue;
>             }
> --- `src/cli.rs:1782-1790` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

## Comparison rationale

The profile treats the journal, fact repository, controls and checkpoint as separate memory substrates because they have distinct persistence and consumers. Generated index content is included as a compiled access structure, not as a second authored knowledge store. Symbolic status/source metadata coexists with prose and conversation content.

`learning` and `trace_learning: yes` describe the wired conversion of session traces into durable facts for future retrieval. They do not claim improved capacity or demonstrated use. The trace source is session logs: automatic fact extraction accepts user turns, while the other included inputs such as static instruction files are imported notes rather than traces. Tool and assistant content are not inputs to the model extractor.

`instruction` is limited to preference/context delivered by hooks and facts exported to project instruction files. `knowledge` covers retrieved fact and event text. `ranking` is supported because stored text affects lexical scoring; it does not imply learned ranking. `enforcement` and `validation` are grounded in stored suppression/deletion state and schema/domain checks. The checkpoint is retained routing state. No evidence supports model-weights as memory or a vector store.

The prompt hook is a push route with inferred-lexical selection, while session-start context is coarse. Requested APIs and writeback are pulls/explicit exports. A returned response is not automatically evidence of host activation. Curation includes consolidation, duplicate rejection, replacement/correction and invalidation. Extraction is classified as consolidation where it restates source claims; no separate evidence establishes synthesis of a claim absent from inputs, promotion, or decay.

## Integration issues

- The supplied runtime calls state-changing paths broadly “validated” but does not specify the separate automatic consolidation admission route. MEM-RTE-2 records the batch, source-quote, blocked-ID, duplicate and domain checks; this distinction matters because `ChangeRequest` validation is not the only write path. Supplied IDs: RTE-1, RTE-2; new: MEM-RTE-2.
- Runtime RTE-3 groups hooks and writeback. This report separates automatic hook injection/sync (MEM-RTE-5) from explicit instruction-file export (MEM-RTE-7), because their triggers and consumers differ. Supplied ID: RTE-3.
- `change.rs` describes its request route as the only live-agent write path. That scope must not be read as “only memory writer”: consolidation writes entity snapshots independently. This qualifies the wording rather than contradicting its narrower authored-change role. Relevant: MEM-RTE-2, MEM-RTE-3.
- No supplied runtime record duplicates the journal, facts, controls, checkpoint or generated index. MEM-OBJ-1 through MEM-OBJ-5 are distinct from executable OBJ-1. Runtime route records are annotated rather than redeclared.
- The README says facts reach the model through installed Claude hooks. Source code wires hook response generation, but installation, runtime delivery and compliance are not observed. This prevents an activation or benefit conclusion. Relevant: RTE-3, MEM-RTE-5.
- The remembered dispositions record accepted and quarantined events; inspected consolidation reads the checkpoint, not prior dispositions, for its next input window. Do not treat outcome retention as a feedback loop. Relevant: MEM-OBJ-4, MEM-RTE-2.

## Limitations and checks

No execution traces or host prompt records were supplied. Prevented conclusions include actual installation, successful provider extraction, retained fact correctness, hook delivery/activation, user reliance, improved future capacity, and causal benefit. The local reranker and model provider are not run or assessed. Source identity and revision match the boundary register and requested commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

Validation: first full pass confirmed the schema, records, comparison profile and eight quote anchors. It found two malformed prose source links and the pending marker; those were corrected before final validation.
