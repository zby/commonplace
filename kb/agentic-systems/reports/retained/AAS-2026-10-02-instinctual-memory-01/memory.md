---
type: agentic-systems/types/agent-memory-analysis-report.md
description: "Memory mechanisms of instinctual-memory across its retained journal, published facts, controls, task state and host context routes"
run-id: AAS-2026-10-02-instinctual-memory-01
source-identity: "https://github.com/jasonkneen/instinctual-memory"
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
report-status: complete
memory-comparison:
  scope: "Included: the file journal, Git-published facts and controls, checkpoint/dispositions, task list, generated project instructions, and preference or fact context supplied by implemented hooks. Excluded: host-owned session lifecycle and model behavior after hook output, actual user stores and traces, external model state, and ordinary static instructions except where ingested as source data."
  axes:
    storage_substrate:
      assessment: known
      values: [files, repo]
      evidence:
        files:
          basis: wired
          records: [OBJ-1, OBJ-3, MEM-OBJ-1, RTE-5, MEM-RTE-7]
          note: "The append journal, task list, and generated project instruction region use ordinary files."
        repo:
          basis: wired
          records: [OBJ-2, RTE-2, RTE-4]
          note: "Facts, controls, index, checkpoint, and dispositions are persisted as Git tree revisions in memory.git."
      records: [OBJ-1, OBJ-2, OBJ-3, MEM-OBJ-1, RTE-2, RTE-4, RTE-5, MEM-RTE-7]
      note: "All included retained surfaces are accounted for; file-backed and Git-tree storage are both present."
    representational_form:
      assessment: known
      values: [natural-language, symbolic]
      evidence:
        natural-language:
          basis: wired
          records: [OBJ-1, OBJ-2, OBJ-3, MEM-OBJ-1, MEM-RTE-7]
          note: "Journal content, fact statements, and generated instruction text retain natural-language content."
        symbolic:
          basis: wired
          records: [OBJ-1, OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RTE-2]
          note: "Structured event fields, IDs, fact states, controls, task versions, checkpoint sequence, and disposition outcomes provide symbolic representation."
      records: [OBJ-1, OBJ-2, OBJ-3, MEM-OBJ-1, MEM-OBJ-2, RTE-2, MEM-RTE-7]
      note: "The profile covers content and access/control structures. Extractor and reranker parameters are not retained memory objects."
    lineage:
      assessment: known
      values: [authored, imported, trace-extracted]
      evidence:
        authored:
          basis: wired
          records: [RTE-4, MEM-OBJ-1, MEM-OBJ-2, MEM-RTE-7]
          note: "Explicit remember/correct requests and appended task titles are operator- or client-authored retained material."
        imported:
          basis: wired
          records: [RTE-1, OBJ-1, MEM-OBJ-1]
          note: "Backfill can import project files, transcripts, chat exports, calendar entries, voice transcripts, and IDE history into the journal."
        trace-extracted:
          basis: wired
          records: [RTE-2, OBJ-2]
          note: "Consolidation transforms eligible user-message and note events into curated facts, retaining source event references and evidence."
      records: [OBJ-1, OBJ-2, OBJ-3, MEM-OBJ-1, MEM-OBJ-2, RTE-1, RTE-2, RTE-4, RTE-5]
      note: "Manual authoring, imported source material, and automatic extraction are separate included lineages."
    behavioral_authority:
      assessment: known
      values: [enforcement, instruction, knowledge, learning, ranking, routing, validation]
      evidence:
        enforcement:
          basis: wired
          records: [OBJ-2, MEM-OBJ-2, RTE-4]
          note: "Retained suppressions, retractions, and deletions filter facts from search and read results."
        instruction:
          basis: wired
          records: [OBJ-3, RTE-5, MEM-RTE-6]
          note: "Stored preferences and generated project guidance are supplied as host additional context by hook routes."
        knowledge:
          basis: wired
          records: [OBJ-1, OBJ-2, RTE-3, MEM-RTE-6]
          note: "Search and read results expose retained event text and curated facts to callers; prompt hooks supply matched facts."
        learning:
          basis: wired
          records: [OBJ-1, OBJ-2, RTE-2]
          note: "Automatically extracted durable facts from prior user and note events shape later available memory. This establishes a wired behavior-shaping update, not improved capacity or benefit."
        ranking:
          basis: wired
          records: [OBJ-2, MEM-OBJ-2, RTE-3]
          note: "Fact statements, entity titles, and aliases are lexical-ranking inputs; optional rerankers can reorder the candidate pool."
        routing:
          basis: wired
          records: [OBJ-2, MEM-OBJ-2, RTE-2]
          note: "The retained checkpoint selects the next journal sequence range for consolidation."
        validation:
          basis: wired
          records: [OBJ-2, MEM-OBJ-2, RTE-2, RTE-4]
          note: "Retained blocked IDs and fact/control state are checked during extraction and validated before publication."
      records: [OBJ-1, OBJ-2, OBJ-3, MEM-OBJ-1, MEM-OBJ-2, RTE-2, RTE-3, RTE-4, MEM-RTE-6, MEM-RTE-7]
      note: "Each force is tied to a retained part and an implemented consumer. This does not establish host compliance or model activation beyond the hook output boundary."
    write_agency:
      assessment: known
      values: [automatic, manual]
      evidence:
        automatic:
          basis: wired
          records: [RTE-1, RTE-2, RTE-5]
          note: "Adapters append imported events, consolidation publishes extracted facts, and hook sync may invoke both automatically."
        manual:
          basis: wired
          records: [RTE-4, MEM-OBJ-1, MEM-OBJ-2, MEM-RTE-7]
          note: "A caller supplies explicit fact changes; task updates append supplied titles."
      records: [RTE-1, RTE-2, RTE-4, RTE-5]
      note: "Both automatic and caller-authored write paths are implemented."
    curation_operations:
      assessment: known
      values: [consolidate, dedup, evolve, invalidate]
      evidence:
        consolidate:
          basis: wired
          records: [RTE-2, OBJ-1, OBJ-2]
          note: "Consolidation extracts and compresses selected journal content into retained facts."
        dedup:
          basis: wired
          records: [EPI-OBJ-1, EPI-RTE-2, OBJ-2, MEM-OBJ-2]
          note: "The tidy duplicate branch identifies a retained fact as a duplicate of the more complete fact; with operator --apply, it retracts and suppresses the duplicate so it disappears from later reads."
        evolve:
          basis: wired
          records: [RTE-4, OBJ-2]
          note: "A correction supersedes an existing fact and publishes its replacement through the explicit change route."
        invalidate:
          basis: wired
          records: [RTE-4, OBJ-2]
          note: "Forget and retraction controls withdraw facts from ordinary reliance; erase also purges targeted stored material through its separate route."
      records: [OBJ-1, OBJ-2, MEM-OBJ-2, RTE-2, RTE-4, EPI-OBJ-1, EPI-RTE-2]
      note: "Dedup is established by applying tidy's duplicate findings to already-retained facts. Consolidation's rejection of duplicate proposals is a separate admission behavior. No decay or promotion route was found in the inspected memory operations."
    read_back_direction:
      assessment: known
      values: [pull, push]
      evidence:
        pull:
          basis: wired
          records: [RTE-3, RTE-4]
          note: "CLI, MCP, HTTP, and shell callers request search, read, and history operations."
        push:
          basis: wired
          records: [MEM-RTE-6]
          note: "Claude start and prompt hooks select and emit retained preferences or matching facts as additional context without a per-item request."
      records: [RTE-3, RTE-4, MEM-RTE-6, MEM-RTE-7]
      note: "Requested retrieval and automatic hook supply are distinct routes. Hook installation and host consumption are unobserved in the supplied boundary."
    read_back_signal:
      assessment: known
      values: [identifier, inferred-lexical]
      evidence:
        identifier:
          basis: wired
          records: [MEM-RTE-6]
          note: "The session-start hook reads the preference entity by the fixed identifier pref_user."
        inferred-lexical:
          basis: wired
          records: [MEM-RTE-6]
          note: "The prompt hook searches with prompt text and admits facts using overlap between meaningful lexical terms in the prompt and fact statement."
      records: [MEM-RTE-6]
      note: "These are push selection signals. Search result ranking and a general availability check do not add separate push signal values."
    trace_learning:
      assessment: known
      values: ["yes"]
      evidence:
        "yes":
          basis: wired
          records: [OBJ-1, OBJ-2, RTE-2, RTE-5]
          note: "Hook sync backfills session records and may consolidate them into durable facts when the event threshold is reached and the configured extractor is LLM. The explicit consolidation command also wires this transformation."
      records: [OBJ-1, OBJ-2, RTE-2, RTE-5]
      note: "Automatic trace-fed writes create retained behavior-shaping facts. This is a route classification, not evidence of observed improvement."
    trace_source:
      assessment: partial
      values: [event-streams, session-logs]
      evidence:
        event-streams:
          basis: wired
          records: [RTE-1, RTE-2]
          note: "Calendar, voice, and other timestamped or position-indexed event inputs can be journaled and consolidated."
        session-logs:
          basis: wired
          records: [RTE-1, RTE-2, RTE-5]
          note: "Backfilled agent conversations and automatically synced session transcripts can be consolidated."
      records: [RTE-1, RTE-2, RTE-5]
      note: "The inspected adapters and consolidation path establish these source classes. Custom adapters can supply additional qualifying note inputs with opaque origins; their possible sources are unresolved, preventing a complete trace-source union. Tool-role messages are excluded by the inspected extractors; this does not rule out a custom note adapter whose source origin is tool traces or trajectories."
---

# instinctual-memory memory report

## Boundary and evidence

The target and reviewed commit are the repository and commit registered in the supplied boundary. The memory scope includes accumulated or changed retained material, its access structures, and its write and later-consumer routes. Inspected surfaces are the JSONL journal; Git-published entity facts, controls, index, checkpoint, and dispositions; the root task list; the project instruction writeback region; and Claude hook context construction. The supplied source register identifies the reviewed implementation and design paths. Evidence is implementation plus declared design; no actual store, host installation, operation trace, or provider response is supplied.

The host remains outside the boundary. Hook code establishes an implemented output route to Claude's hook protocol, but setup or host registration and downstream model use are not observed. Project writeback can create text that a later host may read; no consuming host route for that file is established here. Provider internals are inaccessible. Memory outcomes and improved future performance therefore remain unobserved.

| Entry point or operation | Source paths | Record coverage or limitation |
|---|---|---|
| Ingest and local backfill | `src/cli.rs`, `src/ingest.rs`, `src/journal.rs` | `RTE-1`, `OBJ-1`; imported files and history enter the journal. |
| Consolidation and checkpointing | `src/consolidate.rs`, `src/checkpoint.rs`, `src/repo.rs`, `src/validate.rs` | `RTE-2`, `OBJ-2`; a bounded journal window produces candidate facts and retained control state. |
| Search, rerank, read, and history | `src/ops.rs`, `src/search/`, `src/mcp.rs`, `src/http_serve.rs` | `RTE-3`; caller-requested retrieval, without evidence that an external model receives arbitrary API results. |
| Explicit change and erasure | `src/change.rs`, `src/erasure.rs`, `src/controls.rs`, `src/ops.rs` | `RTE-4`; caller-authored corrections, withdrawal, and purge paths. |
| Setup and generated writeback | `src/setup.rs`, `src/cli.rs` | `RTE-5`; setup configures host routes and writeback edits project instructions. Actual host consumption is unobserved. |
| Claude hook context and sync | `src/hook.rs`, `src/ops.rs`, `src/search/`, `src/cli.rs` | `MEM-RTE-6`; code constructs start and prompt additional context and end-triggered sync. Host installation and activation are unobserved. |
| Root task list | `src/ops.rs`, `src/mcp.rs`, `src/shell.rs` | `MEM-OBJ-1`, `MEM-RTE-7`; versioned append-only task file is directly read or updated. |

## Core ideas

`mem` separates raw source events from curated facts. The journal provides immediate search and a durable source for later consolidation. Consolidation reads events after a retained sequence checkpoint, processes a bounded high-water window, and publishes fact changes together with checkpoint and disposition state. Rule extraction recognizes narrow patterns; LLM extraction considers eligible user words and note content and checks proposed evidence against the source event. The code retains source references. It can suppress repeats, reject near-duplicate proposals, and supersede facts derived only from older versions of project instruction files. The separate `mem tidy` route compares live retained facts, keeps the most complete duplicate, and, only with operator `--apply`, retracts and suppresses the duplicate. The duplicate branch uses deterministic word overlap; optional LLM classification concerns session-only facts. This applied removal establishes `dedup` even though consolidation itself rejects duplicate proposals rather than merging them.

Search combines curated facts and raw journal events. Lexical fact ranking uses statement, entity title, and aliases; optional external or local reranking can reorder candidates. Pull interfaces return results to a caller. Separately, Claude hook code supplies stored preferences at session start and prompt-matched facts on each qualifying prompt. Prompt selection uses meaningful-term overlap and a six-fact cap. This is the clearest automatic push route in the inspected implementation. Hook output is wired; installation, host delivery, compliance, and downstream behavior are not evidenced by a run.

Controls are part of memory because they alter later access and extraction. Suppression, retraction, deletion, and redaction state can prevent material from being returned or reintroduced. Explicit corrections and forget requests provide a manual maintenance route. A separate versioned task file stores caller-supplied task titles. The repository also writes selected facts into marked project instruction regions, but this path depends on a later host read that is not evidenced.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-1 — Versioned task list

Source-native identity and form: JSON task titles and IDs with a monotonically increasing version. Substrate is `tasks.json` under the memory root. MCP/shell callers append titles when the expected version matches; a later read returns the retained list. `SRC-2`, `src/ops.rs`, `src/mcp.rs`, `src/shell.rs`.

#### MEM-OBJ-2 — Retained access and control state

Source-native identity and form: checkpoint and disposition records plus suppression, retraction, deletion, and redaction controls associated with the published memory tree. Substrate is JSON blobs in `memory.git`. Consolidation reads the checkpoint to select a later journal window; search, read, validation, and consolidation consume controls. `SRC-2`, `src/checkpoint.rs`, `src/consolidate.rs`, `src/controls.rs`, `src/search/lexical.rs`.

### Routes

#### MEM-RTE-6 — Hook-selected context supply and session sync

Endpoints: `OBJ-2` preference/fact material and `OBJ-1` session inputs to Claude hook output and subsequent journal/consolidation state. Trigger: SessionStart reads `pref_user`; UserPromptSubmit searches facts using prompt text; SessionEnd may start background sync. Code selects preferences by entity ID and prompt facts by lexical match, then emits hook-specific additional context. Sync backfills project history and may consolidate after the configured threshold. Later consumer: the configured host hook protocol; actual host installation and model consumption are not observed. `SRC-2`, `src/hook.rs`, `src/ops.rs`, `src/setup.rs`.

> let out = json!({"hookSpecificOutput": {"hookEventName": name, "additionalContext": text}});
> --- `src/hook.rs:77-77` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### MEM-RTE-7 — Versioned task update and read

Endpoints: a caller-supplied task title to `MEM-OBJ-1`, and the retained task list back to a requesting caller. The caller supplies the expected version; code checks it under a file lock, appends the task, increments the version, and writes `tasks.json`. A later task read is requested pull. A stale version returns a conflict without changing the list. `SRC-2`, `src/ops.rs`, `src/mcp.rs`.

> file.version += 1;
>         file.tasks.push(TaskItem {
>             id: format!("t_{}", file.version),
>             title: title.clone(),
>         });
>         write_tasks_file(root, &file)?;
> --- `src/ops.rs:514-519` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On EPI-OBJ-1 — Tidy findings

Memory-specific fields: this transient report identifies live retained facts as duplicates or session-only. Duplicate findings name a retained fact to keep. The findings have no persistent memory effect unless the operator invokes `--apply`; for duplicates, apply retracts the selected fact and adds a suppression so it is absent from later reads. `SRC-2`, `src/tidy.rs`; supplied epistemic record `EPI-OBJ-1`.

> // Duplicates: longest statement first, so the most complete one is kept.
>     let mut by_length: Vec<&(String, String, String)> = live.iter().collect();
> --- `src/tidy.rs:100-101` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On EPI-RTE-2 — Tidy classification and withdrawal

Memory-specific fields: the operator invokes tidy to compare retained facts. Duplicate selection is automatic within that invocation, but durable removal is manual because it requires `--apply`. The applied duplicate is retracted and suppressed in `OBJ-2`, changing later retrieval and consolidation eligibility. This route supports the `dedup` classification for retained memory. `SRC-2`, `src/tidy.rs`; supplied epistemic record `EPI-RTE-2`.

> //! Without `--apply` nothing changes. With it, every listed fact is
> //! forgotten in one commit: retracted in its entity file and suppressed in
> //! `state/controls.json` with the reason, so it disappears from every read
> --- `src/tidy.rs:12-15` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On OBJ-1 — Append-only source journal

Memory-specific fields: substrate is files; representational form is natural-language event content plus symbolic roles, source IDs, timestamps, scope/session/project metadata, and sequence. Lineage is imported for backfilled sources and trace-derived for qualifying agent session records. It is immediate retained memory and a later search/consolidation input. Raw events remain distinct from extracted facts. `SRC-2`, `src/journal.rs`, `src/ingest.rs`.

#### On OBJ-2 — Published memory tree

Memory-specific fields: substrate is the bare `memory.git` repository; form is natural-language entity/fact content and symbolic identity, status, control, checkpoint, index, and disposition structures. Lineage includes manually authored changes and trace-extracted facts. Later consumers include search/read, consolidation, hook context construction, and validation. Searchable fact text supplies knowledge and ranking input; controls supply enforcement and validation; checkpoint state routes later consolidation. `SRC-2`, `src/repo.rs`, `src/controls.rs`, `src/ops.rs`, `src/consolidate.rs`.

#### On OBJ-3 — Project instruction writeback region

Memory-specific fields: substrate is a project file; form is generated natural-language guidance; lineage is derived from selected retained project facts. Writeback is explicit and later host reading is possible, but not established by the supplied boundary. The memory system's own hook context route is separate. `SRC-2`, `src/cli.rs`, `src/setup.rs`.

#### On ABS-1 — No operation traces or deployed host configuration in this boundary

This supplied absence limits claims about actual hook installation, host delivery, activation, and benefit. It does not negate the implementation-wired hook context path recorded in `MEM-RTE-6`.

#### On RTE-1 — File backfill to journal

Memory-specific fields: caller or host invokes an adapter, which imports supported chat, calendar, voice, IDE-history, or project-file content into the file journal. The journal is durable and later read by search or consolidation. This is automatic acquisition after invocation, not yet fact curation. `SRC-2`, `src/ingest.rs`, `src/cli.rs`, `src/journal.rs`.

#### On RTE-2 — Journal consolidation to published facts

Memory-specific fields: the trigger is explicit consolidation or hook sync after a threshold. The retained checkpoint selects a bounded next sequence window; rules or an LLM extractor process eligible inputs, then domain validation and Git publication retain facts and disposition state. The later consumers are search, read, and hook context generation. This route provides automatic trace-fed durable writes but no observed improvement. `SRC-2`, `src/consolidate.rs`, `src/repo.rs`, `src/hook.rs`.

> let all_after: Vec<JournalEvent> = journal.read_from(checkpoint.through_seq + 1)?;
> --- `src/consolidate.rs:115-115` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> fn rules_extract(
>     entities: BTreeMap<String, EntityFile>,
>     blocked: std::collections::HashSet<String>,
>     events: &[JournalEvent],
> ) -> Extraction {
> --- `src/consolidate.rs:279-283` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> let receipt = repo.publish(&base, &options.request_id, &change_set, &DomainValidator)?;
> --- `src/consolidate.rs:203-203` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-3 — Search and rerank to caller

Memory-specific fields: the caller requests a query; search selects facts and journal events using filters and ranking, and returns IDs, statements or excerpts. Search is pull when called through CLI, MCP, HTTP, or shell. The later caller is responsible for any further delivery. This annotation excludes the separately implemented hook push path detailed under `MEM-RTE-6`. `SRC-2`, `src/ops.rs`, `src/search/lexical.rs`, `src/mcp.rs`.

> let haystack = format!("{} {} {}", fact.statement, entity.title, entity.aliases.join(" "));
> --- `src/search/lexical.rs:121-121` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-4 — Explicit change and erasure

Memory-specific fields: the caller authors a remember, correction, forget, or erase request. Changes publish authored facts or retained controls; corrected facts supersede prior facts, and suppression controls remove targets from normal retrieval. These are manual write and maintenance routes. `SRC-2`, `src/change.rs`, `src/erasure.rs`, `src/controls.rs`, `src/ops.rs`.

> pub fn is_suppressed(&self, target: &str) -> bool {
>         self.suppressions.contains_key(target)
>     }
> --- `src/controls.rs:83-85` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-5 — Generated writeback and host setup

Memory-specific fields: explicit setup may register hooks and MCP for supported hosts; explicit writeback selects project facts and replaces the marked region of an instruction file. Hook end sync may backfill and consolidate. The latter is represented in `MEM-RTE-6` as a separate memory route because it also creates and supplies retained content. Project instruction consumption remains possible but unobserved. `SRC-2`, `src/setup.rs`, `src/cli.rs`, `src/hook.rs`.

#### On CMP-1 — LLM consolidation extractor

Memory-specific fields: this model is a transformation component, not itself a retained memory object. It can process eligible user event text and note content into fact proposals; evidence, validation, and publication gates remain code paths. Its actual invocation and provider behavior are unobserved. `SRC-2`, `src/consolidate.rs`.

#### On CMP-2 — JEV reranker

Memory-specific fields: external reranking is a retrieval component, not retained memory. It can affect order after candidate construction when configured; activation and effect are unobserved. `SRC-2`, `src/search/rerank.rs`, `src/jev.rs`.

#### On CMP-3 — Local Laya cross-encoder

Memory-specific fields: local reranking is a retrieval component, not retained memory. Download, activation, and effect are unobserved. `SRC-2`, `src/search/laya.rs`, `src/search/rerank.rs`.

## Write side

Adapters acquire input and append source events to the journal. Inputs include local chat exports, agent history, project guidance files, calendar entries, voice transcripts, and supported IDE history. Acquisition can be invoked directly or by hook sync. The task list is separately updated by appending a caller-supplied title under an expected-version check.

Consolidation reads after a sequence checkpoint in a bounded window. Rule or LLM extraction selects durable facts from eligible user messages or notes. The code checks evidence against its cited event, suppresses blocked IDs and near-duplicate candidates, and writes entity changes with checkpoint and per-batch dispositions. Changed project memory files can supersede facts tied only to older versions. The retained derived fact stores a source event reference and evidence excerpt, but the full rationale for why a fact is useful is not necessarily retained as a later-read object. In the LLM path, the extraction prompt and evidence are implementation inputs; no runtime traces show the model's internal reasoning.

Manual change requests author or correct facts and can add forget controls. The separate tidy maintenance route proposes duplicate/session-only findings; operator `--apply` retracts and suppresses selected facts, including already-retained duplicates. Erasure is a separate purge path. Generated writeback copies selected facts into a marked project instruction region. These routes do not use the same admission transaction in every case: fact publication is validated through the memory Git publisher, while task state and project-file writes are ordinary file operations with their own local versioning or marker behavior.

## Read-back

Requested pull routes include search, read, history, status, and task-list reads. Tidy can also remove active facts after an operator invokes `--apply`; duplicate findings select a retained duplicate for removal, while session-only findings use an optional LLM judgment. Search combines curated fact hits and raw journal hits, applies scope/project/source filters, and may rerank the pool. IDs returned by search support later reads. A caller receives the result; actual further use is outside the API's evidence.

The hook path is an automatic push. At session start, it checks whether facts exist, reads the `pref_user` entity, and emits general memory guidance plus available preference statements. On a qualifying user prompt, it searches curated facts only, with the prompt as query, disables reranking, requires meaningful-term overlap, limits output to six facts, and emits them through hook-specific additional context. Session-end handling can spawn background sync; sync backfills the project's history and invokes LLM consolidation only when the configured threshold is met and the selected extractor is LLM. The code wires these producer and consumer-facing outputs. The supplied boundary contains no deployed hook config or observed host run, so delivered model context and activation remain unobserved.

> let needed = terms.len().min(2);
>     let hits: Vec<_> = found
>         .hits
>         .iter()
>         .filter(|h| {
>             let words = content_terms(&h.statement);
>             terms.iter().filter(|t| words.contains(*t)).count() >= needed
>         })
>         .take(PROMPT_FACTS)
>         .collect();
> --- `src/hook.rs:139-148` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

## Comparison rationale

The memory profile includes raw journal files, Git facts and controls, checkpoint/disposition access state, tasks, and the generated instruction output. It excludes static program instructions and model weights as retained memory. Natural language covers source text, facts, and generated guidance; symbolic form covers IDs, typed event/fact fields, controls, versions, and selection checkpoints. Both pull and push read-back exist. Push selection uses a fixed preference identifier at session start and inferred lexical matching for prompt facts. Trace-fed automatic consolidation qualifies as wired trace learning because it produces durable facts available to later consumers, although no benefit is observed.

Trace-source coverage is partial. Built-in paths show conversational session logs and timestamped/calendar/voice event inputs. The generic custom-adapter route allows note content of opaque origin, and the complete source union for such automatically consolidated notes cannot be established from this boundary. Tool-role events are excluded from the inspected extraction paths; no tool-trace or trajectory value is asserted.

## Integration issues

- Correction to the prior profile: add `dedup` to `curation_operations` because `EPI-RTE-2` can apply duplicate findings to already-retained facts by retracting and suppressing them. This is distinct from consolidation rejecting a duplicate proposal. Evidence: `SRC-2`, `src/tidy.rs`; records `EPI-OBJ-1`, `EPI-RTE-2`, `OBJ-2`, `MEM-OBJ-2`.
- The supplied reconciliation resolves the prior hook-route coverage issue and record overlap: `MEM-RTE-6` and `EPI-RTE-1` describe overlapping hook behavior; they are not independent operations. No further hook correction is required here.
- No memory-declared record is intended as a duplicate declaration. The tidy findings and route are annotated from the supplied epistemic member; runtime records are annotated above.

## Limitations and checks

The conclusion that memory is made available to later work is implementation-wired. Actual operator stores, hook installation, runtime host delivery, model consumption, extractor/reranker calls, and task benefit are not observed. The repository's custom adapter contract leaves possible source origins open, so the trace-source union remains partial. `SRC-1` and `SRC-2` and the reviewed commit were taken from the supplied boundary; source paths used in quotations were resolved with `commonplace-quote` against the supplied run-state and frozen revision. Deterministic validation passed cleanly with no warnings or failures using `commonplace-validate --full` on this output. Source identity and reviewed commit match the supplied boundary; all quoted source paths are from the frozen revision and use citations generated with the supplied run-state. Prevented conclusions remain deployment activation, host consumption, and improved performance; trace-source coverage remains partial because custom adapter origins are opaque.
