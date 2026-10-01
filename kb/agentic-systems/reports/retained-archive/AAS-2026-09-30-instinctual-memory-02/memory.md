---
type: types/agent-memory-analysis-report.md
description: "Instinctual Memory retains source events and Git-published facts, then supplies selected facts through hooks, requested reads, or writeback; host use and factual warrant remain unestablished."
run-id: AAS-2026-09-30-instinctual-memory-02
source-identity: "https://github.com/jasonkneen/instinctual-memory"
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
report-status: complete
memory-comparison:
  scope: "Retained journal events, extracted or explicitly changed entity facts, their Git access structures, and the automatic hook, requested query/change, and requested writeback routes that can carry them to later consumers. Excludes static bundled guidance, model weights, ordinary in-session context, task state, and host behavior after delivery."
  axes:
    storage_substrate:
      assessment: known
      values: [files, repo]
      evidence:
        files: {basis: wired, records: [MEM-OBJ-1, MEM-OBJ-2], note: "The journal and Markdown entity files are file-backed retained objects."}
        repo: {basis: wired, records: [MEM-OBJ-2, MEM-OBJ-3], note: "Curated facts and their index and controls are published in a Git memory repository."}
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3]
      note: "The journal is outside Git; curated memory and access metadata are in Git. No other retained substrate is included."
    representational_form:
      assessment: known
      values: [natural-language, symbolic]
      evidence:
        natural-language: {basis: wired, records: [MEM-OBJ-1, MEM-OBJ-2], note: "Journal content and fact statements are text."}
        symbolic: {basis: wired, records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3], note: "Event envelopes, fact fields, and access metadata have structured fields."}
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3]
      note: "Both source text and structured representations participate in retained memory."
    lineage:
      assessment: known
      values: [authored, imported, trace-extracted]
      evidence:
        authored: {basis: wired, records: [MEM-RTE-3], note: "Explicit remember and correction requests supply fact content."}
        imported: {basis: wired, records: [MEM-RTE-1], note: "Project instruction and other supported source files can be ingested as note events before extraction."}
        trace-extracted: {basis: wired, records: [MEM-RTE-1], note: "Session events can be transformed into retained facts with source evidence."}
      records: [MEM-RTE-1, MEM-RTE-3]
      note: "The set includes directly supplied changes, imported note content, and facts derived from session traces."
    behavioral_authority:
      assessment: known
      values: [instruction, knowledge, ranking]
      evidence:
        instruction: {basis: wired, records: [MEM-RTE-4], note: "Requested writeback places fact statements in a host instruction file; the host's authority rules remain external."}
        knowledge: {basis: wired, records: [MEM-RTE-2, MEM-RTE-3], note: "Hooks and requested reads deliver facts as information; host use is uninspected."}
        ranking: {basis: wired, records: [MEM-RTE-3], note: "Search may use reranking to order returned facts; this orders retrieval results rather than enforcing their content."}
      records: [MEM-RTE-2, MEM-RTE-3, MEM-RTE-4]
      note: "Actual memory consumer paths supply information, rank search results, or write instructions for later host loading. No system-enforced authority over the host is established."
    write_agency:
      assessment: known
      values: [automatic, manual]
      evidence:
        automatic: {basis: wired, records: [MEM-RTE-1], note: "The session-end route can backfill and consolidate events automatically."}
        manual: {basis: wired, records: [MEM-RTE-1, MEM-RTE-3, MEM-RTE-4], note: "Operators can ingest, request changes, or write back explicitly."}
      records: [MEM-RTE-1, MEM-RTE-3, MEM-RTE-4]
      note: "Automatic trace ingestion and extraction coexist with operator-triggered source ingestion and changes."
    curation_operations:
      assessment: known
      values: [evolve, invalidate]
      evidence:
        evolve: {basis: wired, records: [MEM-RTE-3], note: "Correction supersedes an existing fact and adds its replacement."}
        invalidate: {basis: wired, records: [MEM-RTE-1, MEM-RTE-3], note: "Changed source-file versions supersede old-only facts, while forget retracts and suppresses a selected fact."}
      records: [MEM-RTE-1, MEM-RTE-3]
      note: "These are content operations; index rebuilding and candidate rejection during extraction are excluded. No merge of already-retained near duplicates, decay, or promotion operation was identified in the inspected memory routes."
    read_back_direction:
      assessment: known
      values: [pull, push]
      evidence:
        pull: {basis: wired, records: [MEM-RTE-3, MEM-RTE-4], note: "A caller requests searches, reads, or a writeback selection."}
        push: {basis: wired, records: [MEM-RTE-2], note: "The installed prompt hook selects eligible facts and supplies them without a separate memory request."}
      records: [MEM-RTE-2, MEM-RTE-3, MEM-RTE-4]
      note: "Both automatically injected hook context and caller-requested retrieval are wired."
    read_back_signal:
      assessment: known
      values: [identifier, inferred-lexical]
      evidence:
        identifier: {basis: wired, records: [MEM-RTE-2], note: "At session start the hook reads the retained preference entity by the explicit ID pref_user."}
        inferred-lexical: {basis: wired, records: [MEM-RTE-2], note: "For each prompt, lexical overlap selects matching fact statements for injection."}
      records: [MEM-RTE-2]
      note: "Push selection uses an identity lookup at session start and lexical matching at prompt time; no embedding or judgment selector was identified."
    trace_learning:
      assessment: known
      values: ["yes"]
      evidence:
        "yes": {basis: wired, records: [MEM-RTE-1], note: "Session events feed automatic extraction and publication of durable facts used by later retrieval routes; this establishes the memory-axis mechanism, not improved task performance."}
      records: [MEM-RTE-1, MEM-OBJ-1, MEM-OBJ-2]
      note: "This is trace-fed memory writing, not a claim that the host learns or improves."
    trace_source:
      assessment: partial
      values: [session-logs]
      evidence:
        session-logs: {basis: wired, records: [MEM-RTE-1], note: "Session backfill and transcript adapters feed journal events to extraction."}
      records: [MEM-RTE-1, MEM-OBJ-1]
      note: "Session logs are established. The runtime inventory also mentions other supported input formats; their mapping to event-streams, tool-traces, or trajectories was not traced here, so the complete source set is unresolved."
    learning_scope:
      assessment: known
      values: [cross-task, per-project]
      evidence:
        cross-task: {basis: claimed, records: [MEM-RTE-1], note: "The extractor's declared retention test targets usefulness weeks later in a different task; actual later use is unobserved."}
        per-project: {basis: wired, records: [MEM-RTE-1, MEM-RTE-2], note: "Project-scoped facts and project filtering are wired in extraction and prompt retrieval."}
      records: [MEM-RTE-1, MEM-RTE-2]
      note: "General preference and project fact scopes cross tasks by design; this does not establish a per-task memory-learning route."
    learning_timing:
      assessment: known
      values: [staged]
      evidence:
        staged: {basis: wired, records: [MEM-RTE-1], note: "Session events are first backfilled to the journal; thresholded consolidation later extracts and publishes facts."}
      records: [MEM-RTE-1]
      note: "The automatic route has an event-collection stage followed by a separate consolidation stage."
    distilled_form:
      assessment: known
      values: [natural-language, symbolic]
      evidence:
        natural-language: {basis: wired, records: [MEM-OBJ-2], note: "Extracted and explicitly supplied facts retain natural-language statements."}
        symbolic: {basis: wired, records: [MEM-OBJ-2], note: "Facts retain structured entity, predicate, status, validity, provenance, and visibility fields."}
      records: [MEM-OBJ-2]
      note: "Distilled facts combine text claims with typed metadata."
    faithfulness_tested:
      assessment: known
      values: ["no"]
      evidence:
        "no": {basis: wired, records: [MEM-RTE-1, MEM-RTE-2], note: "The inspected boundary has no retained execution evidence testing whether task behavior depends on recalled content; extraction traceability checks do not test downstream faithfulness."}
      records: [MEM-RTE-1, MEM-RTE-2, MEM-CLM-1]
      note: "The repository includes held-out retrieval-rubric evaluation, but it scores search results rather than whether an agent task depends on recalled content."
---

# Instinctual Memory memory analysis

## Boundary and evidence

This report examines memory accumulated or changed through use: source events in the durable journal; curated facts and their metadata in the Git-backed memory tree; index and controls used for access; and the routes that return or write back that material. It excludes bundled static instructions as memory, ordinary current-run context, host orchestration and interpretation after delivery, provider internals, and task state. The frozen source is Instinctual Memory commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`, a whole-system repository boundary, with code-grounded evidence. Relevant inspected paths include `src/journal.rs`, `src/fact.rs`, `src/entity.rs`, `src/consolidate.rs`, `src/hook.rs`, `src/search/lexical.rs`, `src/change.rs`, and `src/cli.rs`. No installed host, deployed store, live session, or model service was available; actual host use, provider behavior, and user benefit remain unestablished. The broader ingestion adapter set was not fully classified for trace-source categories.

## Core ideas

Instinctual Memory separates an append-only event journal from a Git-published fact store. Session and other source material first enter the journal; consolidation proposes durable facts, checks that each proposal points to a batch event and that its evidence matches source text, then publishes accepted changes and dispositions. The code-grounded implementation supports traceability and structure, not proposition truth or utility. It also suppresses a proposed fact when an active fact is judged to restate it; this is candidate admission control, not merging existing retained content, so it does not meet the type's `dedup` definition. The implementation compares content-word overlap:

> if self.blocked.contains(&fact_id) || self.restates_existing(&p, &fact_id) {
> --- `src/consolidate.rs:370-370` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> jaccard(&words, &other) >= NEAR_DUPLICATE || contained(&words, &other)
> --- `src/consolidate.rs:443-443` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The extractor's declared target is cross-task persistence:

> A fact is worth keeping only if it will still be true and useful in a session weeks from now, in a different task: the user's identity and role, standing preferences and working rules, project facts (what it is, stack, architecture, conventions, commands, decisions and why), and named people or organisations with a stated relationship.
> --- `src/consolidate.rs:578-578` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The journal is a durable file-backed source object outside the Git snapshots. Curated facts are Git-tracked Markdown entity files with structured fact fields. The profile treats both text and structure as retained forms:

> //! The journal is the canonical input to memory. It lives outside the Git
> //! repository and is governed independently of memory snapshots.
> --- `src/journal.rs:3-4` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> pub struct Fact {
>     pub id: String,
>     pub predicate: String,
>     pub statement: String,
>     pub kind: FactKind,
>     pub status: FactStatus,
> --- `src/fact.rs:13-18` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The prompt hook is an automatic push path: start reads a preference entity by ID, while each sufficiently substantive prompt retrieves matching facts by lexical content and injects them as Claude context. It requires at least two meaningful shared words (one if the prompt contains only one) and returns at most six facts. This is delivery evidence; whether the host model attends to or follows the material remains outside the inspected boundary:

> let read = crate::ops::execute(root, "personal", "default", "memory_read", &json!({"id": "pref_user"}));
> --- `src/hook.rs:90-90` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> let needed = terms.len().min(2);
> --- `src/hook.rs:139-139` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Other read-back is caller-requested: MCP, CLI, shell, and loopback HTTP expose search, read, and history operations, while explicit writeback places selected active facts into a host instruction file. Retrieval dispatch and the managed-block write are wired; later host loading and behavioral effect are not established. Change routes explicitly remember, correct, or forget facts. Correction supersedes the old fact; forget retracts and suppresses it. Source-file refresh can supersede facts that only cite older file versions. These are scoped content maintenance operations, distinct from index rebuilds.

The repository also implements held-out retrieval-rubric evaluation. It compares lexical and reranked result IDs and statements against expected content, so it can evaluate retrieval recall and ranking. It does not run agent tasks with and without returned memory; it therefore does not establish task faithfulness or behavioral effect:

> //! once in lexical order and once reranked. A case passes when every
> //! expected id is in the top `limit` hits, every `must_include` string
> //! appears in them, and no `must_not_include` string does.
> --- `src/evaluation.rs:5-7` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-1 — Source-event journal

The durable append-only JSONL journal stores source events with event identity, role, scope/session identity, content, timestamps, content hash, redaction and metadata. It is file-backed outside the Git memory repository and is input to fact extraction and general journal search. It retains imported source material and session records; assistant or harness-injected text is excluded from the LLM fact-candidate route. Its contents are natural-language text in a structured event envelope. Evidence: `SRC-1` `src/journal.rs`, `src/consolidate.rs`, and `src/ingest.rs`.

#### MEM-OBJ-2 — Curated entity facts

The Git memory tree stores Markdown entity files with typed fact records. A fact carries a natural-language statement plus fields such as predicate, status, validity, provenance, and visibility. Facts originate in extraction from journal events or in explicit change requests. The Markdown body is a human-readable rendering; the structured fields govern eligibility and retrieval. Evidence: `SRC-1` `src/entity.rs`, `src/fact.rs`, `src/consolidate.rs`, and `src/change.rs`.

#### MEM-OBJ-3 — Memory access metadata

The Git tree also carries the index and controls used to locate entities and suppress, retract, or otherwise filter facts. These are symbolic access structures, not themselves the natural-language fact payload. They are updated with content changes. Evidence: `SRC-1` `src/index.rs`, `src/controls.rs`, `src/consolidate.rs`, and `src/change.rs`.

### Routes

#### MEM-RTE-1 — Ingest, backfill, and consolidate

Operators or session-end hooks ingest source material into the journal; a configured automatic route can backfill a completed session and consolidate after a threshold. Rules or an external chat-completion model propose facts from bounded events and existing entities. Code checks source references, exact evidence traceability and domain constraints, rejects proposals that restate an active fact, then publishes entity files, index, dispositions and checkpoint through Git. Inputs include transcript/session events and memory-file notes. The route is automatic for thresholded hook work and manual for direct ingest/consolidation. Later consumers include search/read and the prompt hook. Evidence matching does not establish factual correctness; no per-fact human approval or answer oracle is specified. No later consumer of retained extraction criticism was identified. The route's source-event type coverage is broader than the session-log adapter paths traced here. Evidence: `SRC-1` `src/ingest.rs`, `src/consolidate.rs`, `src/hook.rs`, and `src/repo.rs`.

> // Only the user's own words and memory files can carry durable facts.
> --- `src/consolidate.rs:631-631` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### MEM-RTE-2 — Automatic hook read-back

The Claude start hook reads the `pref_user` entity, and prompt hooks lexically select eligible fact statements for injection into `additionalContext`. Prompt selection requires shared meaningful words and caps results at six. This is wired delivery by the hook implementation, not evidence of host activation or behavioral change. Evidence: `SRC-1` `src/hook.rs`, `src/search/lexical.rs`, and `src/setup.rs`.

#### MEM-RTE-3 — Requested retrieval and changes

A caller explicitly requests search, read, history, remember, correct, or forget over MCP or another operation surface. The caller chooses operation and arguments; code filters results and validates changes. Correct supersedes an existing fact with a new one; forget retracts and suppresses a selected fact while retaining history. Results are returned to the caller for possible later use. The route does not establish the client model's use of results. Evidence: `SRC-1` `src/ops.rs`, `src/mcp.rs`, `src/change.rs`, `src/repo.rs`, and `src/validate.rs`.

> entity.supersede(&old_id, &new_fact.id)?;
> --- `src/change.rs:127-127` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### MEM-RTE-4 — Requested writeback

An operator requests `mem writeback`, which selects eligible facts for a project and preference scope and writes a generated natural-language block into a chosen instruction file. Its file write is wired; the host's later loading and interpretation are uninspected. Evidence: `SRC-1` `src/cli.rs`, `src/setup.rs`, and `skills/mem/SKILL.md`.

### Claims

#### MEM-CLM-1 — Retrieval rubric evaluation measures search results

The shipped evaluation module runs real search with and without reranking and scores expected fact IDs plus required and excluded strings in the returned hits. It evaluates retrieval quality; it does not compare downstream agent task performance with and without recalled content. Consequently it does not make `faithfulness_tested` positive. Evidence: `SRC-1` `src/evaluation.rs`.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Write side

The journal preserves source events separately from curated facts. Ingestion can be automatic at session end or manually invoked. Consolidation is a second stage that selects events after a checkpoint and within a bounded batch, then proposes and validates facts. The LLM extraction path accepts user-authored words and memory-file notes as candidates, excluding assistant turns and harness-injected material. Its evidence quote must match a source event, but the code does not test whether the resulting statement is true or useful.

Explicit remember requests author new facts; correction replaces current reliance by superseding a selected fact; forget retracts and suppresses it while retaining ordinary history. Changed source-file versions can supersede old-only facts. The route does not show merging of already-retained near-duplicate facts, decay, or salience promotion. Its near-duplicate check suppresses a candidate before publication; it does not combine retained entries. Erasure is a distinct history rewrite; its operational detail belongs to the runtime route and is not treated as ordinary curation.

## Read-back

Automatic push occurs through the Claude hooks. At session start the hook supplies preference material selected by the explicit entity ID `pref_user`; for prompts, lexical matching selects up to six eligible curated facts. Selection trigger, inputs and delivered parts are therefore explicit. The hook's session-end sync is a write path, not read-back.

Pull occurs when a caller requests a search, read, history result, or writeback. Caller-selected queries and operation arguments control retrieval. Search may rank candidates; writeback selects facts by project/preference scope and writes the chosen subset into a destination file. A later host read of that file depends on host configuration and is not established by the write operation. Delivery is wired on inspected routes; activation and benefit are uninspected.

## Comparison rationale

The profile includes both the external file journal and the Git repository because both retain memory objects. Structured event/fact fields make symbolic form operative alongside natural-language source and statement text. Lineage covers explicitly authored changes, imported memory-file material and trace-extracted facts. Consumer authority is advisory knowledge through hooks and requested reads, ranking within search, and instruction-like content when written into a host instruction file; the host retains control over whether and how it follows that content.

The trace-learning value means only that traces automatically feed durable facts that can shape later context. It does not imply observed learning. The scope is cross-task by extractor design and project-scoped for project facts; prompt-hook filtering has an explicit project input. Timing is staged because event backfill and fact consolidation are separate steps. Trace source is partial because session-log routes are evidenced while the entire set of other adapters was not mapped to the controlled source categories. Faithfulness tested is no: no retained execution record tests dependence of task behavior on recalled facts, and source-evidence matching only tests provenance/format.

## Integration issues

- Reconciliation superseded MEM-RTE-2 by RTE-1 for the automatic hook route; its memory-specific selector findings remain represented in the report profile and prose.
- Reconciliation retained MEM-RTE-1 as a memory-specific lifecycle grouping: runtime records separate hook scheduling from manual ingestion and consolidation.
- Reconciliation retained MEM-RTE-3 as a memory-specific grouping of requested retrieval and changes, while runtime records separate operation surfaces.
- Reconciliation superseded MEM-RTE-4 by RTE-6 for requested writeback.
- The prior `dedup` classification is withdrawn: consolidation rejects a new candidate that restates an active fact but does not merge existing retained content. The comparison in `src/consolidate.rs` establishes candidate suppression only.
- The run boundary names other supported input formats, but this pass did not trace every adapter's mapping to trace-source categories. This limits completeness of `trace_source`; no negative absence finding is made.
- No configured host or retained execution evidence was available to test activation, downstream faithfulness, or behavioral benefit. This prevents claims that delivered memory changes task behavior.

## Limitations and checks

The memory analysis is source-grounded at SRC-1's frozen commit. It did not inspect a deployed store, execute a live host or provider, or observe consumer behavior. The broader adapter set remains only partially classified under the trace-source axis. No source identity recheck or independent method-commit verification was run by this job.

Deterministic validation: `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-02/memory-report-1.md` passed cleanly (all checks pass, no warnings or failures).
