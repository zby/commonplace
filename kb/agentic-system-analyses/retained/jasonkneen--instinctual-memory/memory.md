---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Instinctual Memory: raw journal, sourced facts, admission controls and later agent-context delivery at the frozen Rust product boundary."
run-id: AAS-2026-10-12-instinctual-memory-af48437aa60c-01
source-identity: "https://github.com/jasonkneen/instinctual-memory"
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual Memory memory report

## Boundary and evidence

This report covers the shipped memory loop at the revision in [boundary](boundary.md): adapter acquisition, raw journal retention, rules/model consolidation, direct assertions, maintenance, current and historical-status reads, search, hooks, instruction-file writeback, separate tasks, and retrieval evaluation. It includes the public Rust alternatives, not just MCP. All source findings use SRC-1. Direct reads establish implementation and embedded doctrine; supplied [runtime](runtime.md) records supply the publisher, recovery, transport and model-component baseline. Neither establishes exercised host behavior or improved answers.

Direct inspection added or deepened `src/fact.rs`, `src/entity.rs`, `src/controls.rs`, `src/checkpoint.rs`, `src/index.rs`, `src/ingest.rs`, `src/journal.rs`, `src/consolidate.rs`, `src/ops.rs`, `src/hook.rs`, `src/cli.rs`, `src/tidy.rs`, `src/erasure.rs`, `src/search/lexical.rs`, `src/search/journal.rs`, `src/search/rerank.rs`, `src/evaluation.rs`, `src/mcp.rs`, `src/lib.rs` and the complete `skills/mem/SKILL.md`. CLI dispatch and public exports were searched against the supplied routes. HTTP/shell operation delegation was searched; their detailed transport handling remains supplied runtime evidence. This is additional scope within the registered Git source, not a new source declaration.

External host loading, actual user stores, transcripts, rubric authorship, remote model state, model weights and successful run evidence are not frozen. Provider processing and original authorship of imported content remain uninspected. The missing PRD prevents checking its requirements. Dependency internals and host application scheduling are outside the functional boundary. These limits prevent deployment, reliability and benefit conclusions, not source-level accounts of the included transformations.

| Entry point or operative part | Source path and evidence basis | Coverage and local limit |
|---|---|---|
| CLI ingest; directory/local/all-host backfill; library adapters | Direct `src/cli.rs`, `src/ingest.rs`, `src/journal.rs`, `src/lib.rs`; supplied backfill account | [MEM-RTE-adapter-ingestion](#mem-rte-adapter-ingestion), [MEM-OBJ-journal-event](#mem-obj-journal-event). Local and generic acquisition inspected in detail; all-host discovery and OpenCode text conversion inspected, some per-host discovery plumbing remains supplied. No universal transcript-completeness claim. |
| BulkWriter versus public Journal append | Direct `src/journal.rs` | [MEM-RTE-adapter-ingestion](#mem-rte-adapter-ingestion). Library append lacks bulk dedup and assigns its sequence before locking; the CLI bulk protocol is not universal. |
| Auto/rules/LLM consolidation, clipping, chunking, duplicates and changed files | Direct `src/consolidate.rs`, supporting fact/entity/control schemas; supplied publisher route | [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), annotation below; [MEM-OBJ-fact](#mem-obj-fact), [MEM-OBJ-source-ref](#mem-obj-source-ref). All Note-role input is eligible for the memory-file model framing, not only project instructions. |
| Checkpoint, rejection dispositions and control state | Direct `src/checkpoint.rs`, `src/controls.rs`, actual writes in `src/consolidate.rs` | [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [MEM-OBJ-dispositions](#mem-obj-dispositions), [MEM-OBJ-controls](#mem-obj-controls). No later automatic reconsideration of dispositions established. |
| Caller remember/correct/forget, receipts and intents | Direct CLI construction and operation read helpers; supplied change/publisher inspection | [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change), annotation below. Receipt/intent internals remain supplied evidence; assertion origin and approval are unresolved for generic callers. |
| Search/read/history through CLI/MCP/HTTP/shell or Rust | Direct `src/ops.rs`, lexical/journal/rerank code, CLI enrichment, MCP tools; supplied transport routes | [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval), annotation below. Current-head history payload is not Git commit traversal; ID reads do not share lexical temporal eligibility. |
| Start/prompt push and end sync | Direct complete `src/hook.rs`; supplied setup wiring | [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks), [RT-BAP-host-context](runtime.md#rt-bap-host-context). Host activation and detached child success remain uninspected. |
| Writeback, installed skill, instruction-file re-ingestion | Direct writeback and local Markdown acquisition; complete skill; supplied setup | [RT-RTE-instruction-writeback](runtime.md#rt-rte-instruction-writeback), [RT-OBJ-mem-skill](runtime.md#rt-obj-mem-skill), [RT-BAP-instruction-file](runtime.md#rt-bap-instruction-file). No shared control/temporal gate in writeback. |
| Tidy preview/apply and erasure | Direct `src/tidy.rs` and erasure stage ordering; supplied detailed history scrub account | [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance), [RT-RTE-erasure-maintenance](runtime.md#rt-rte-erasure-maintenance). Reasons and removed content have different consumers; external copies are not revoked. |
| Entity Markdown body and INDEX.md rebuild | Direct `src/entity.rs`, `src/index.rs`, CLI index dispatch | [MEM-OBJ-entity-display](#mem-obj-entity-display), [MEM-RTE-index-rebuild](#mem-rte-index-rebuild). Displays count status-active facts, not all retrieval exclusions. |
| Versioned tasks | Supplied `src/ops.rs` findings; direct export/tool inventory | [RT-OBJ-tasks](runtime.md#rt-obj-tasks), [RT-RTE-task-update](runtime.md#rt-rte-task-update), annotations. Not derived from transcripts and not consolidated into facts. |
| Evaluation and bench | Direct `src/evaluation.rs`, CLI bench; supplied evaluation route | [RT-RTE-search-evaluation](runtime.md#rt-rte-search-evaluation). Bench prints timings/hit counts only; neither driver retains an automatic production-admission result. |
| Provider/cache parameters and configuration | Supplied component/configuration records; direct rerank fallback and exports | [RT-CMP-llm-config](runtime.md#rt-cmp-llm-config), [RT-CMP-jev-reranker](runtime.md#rt-cmp-jev-reranker), [RT-CMP-laya-reranker](runtime.md#rt-cmp-laya-reranker), [RT-RTE-integration-admission](runtime.md#rt-rte-integration-admission). Exact model provenance/provider retention remains unresolved; does not obscure known symbolic/text updates. |

## Core ideas

1. **The journal and facts are independently readable.** Consolidation extracts standing statements rather than replacing the journal. Search interleaves both; a rejected event may still be searchable raw context. Soft forgetting changes fact eligibility, not the originating raw event ([MEM-OBJ-journal-event](#mem-obj-journal-event), [MEM-OBJ-controls](#mem-obj-controls), [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval)).
2. **The retained content and its evidence have different authority.** A statement can become model context or an instruction-file bullet. Its event ID and quote supply lineage, not proof. Ordinary read/history, hooks and writeback omit the evidence quote. The skill requests trust in curated facts, whereas prompt hooks request checking against code. These are host guidance, not enforced trust or verified truth ([MEM-OBJ-fact](#mem-obj-fact), [MEM-OBJ-source-ref](#mem-obj-source-ref), [RT-OBJ-mem-skill](runtime.md#rt-obj-mem-skill)).
3. **Retained facts shape later extraction as well as later answers.** Batches receive bounded existing-entity statements; local word-overlap rejection uses current active statements. This is a trace-to-derived-memory-to-next-update chain, with separate later host consumers. It establishes experience-fed updating, not measured learning or improvement ([RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), annotation below).
4. **Admission and withdrawal are route-specific.** The extraction quote gate does not cover direct assertions. Suppression is an ID gate rather than semantic prohibition. Search uses temporal eligibility; entity read, status-active display and writeback do not uniformly use it. Git publication is distinct from journal/task/instruction-file effects ([MEM-OBJ-controls](#mem-obj-controls), [MEM-OBJ-entity-display](#mem-obj-entity-display), supplied change and maintenance routes).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-journal-event
Label: Raw adapted journal event

Source-native identity: `JournalEvent`. Storage substrate: framed JSONL day files under `journal/`, separate from bare `memory.git`. Natural-language `content` is adapter-extracted text, not necessarily the original complete transcript. Symbolic event/sequence/source/scope/session/hash/time/redaction/project fields identify, order and filter it; metadata can also hold searchable source payloads, such as IDE results. The payload's original authorship and correctness are not authenticated by these labels. SRC-1, `src/journal.rs`, `src/ingest.rs`, `src/search/journal.rs`.

Lineage includes user and assistant chat text, project Markdown, calendar summaries, voice transcript text, IDE commands/results and generic export roles. Codex adapter omits non-final assistant channels and subagent rollouts, and strips environment context before retention. Thus “raw” means retained source-side adapted material rather than an untouched transcript. Acquired event text can later reach consolidation, journal search, ID read and CLI source excerpts. The LLM consolidation selector rejects assistant/tool/system roles, but raw retrieval is a distinct route; no source trust gate makes all raw text authoritative instructions.

Distinct identity: this is the input store traversed by [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) and [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval), not either route or [RT-OBJ-tasks](runtime.md#rt-obj-tasks); no supplied object declares it.

> pub content: String,
> pub content_sha256: String,
> pub redaction: Redaction,
> #[serde(default)]
> pub metadata: serde_json::Value,
> --- `src/journal.rs`

#### MEM-OBJ-fact
Label: Structured fact with behavior-shaping statement

Source-native identity: `Fact` within `EntityFile.facts`. Storage: YAML frontmatter in entity Markdown files in published Git snapshots. Natural-language statements coexist with symbolic predicate/ID/kind/status/visibility/temporal/reference fields; the former informs host or extractor interpretation, the latter controls identity, lookup and eligibility. Source evidence is assessed separately in [MEM-OBJ-source-ref](#mem-obj-source-ref); rendered body is [MEM-OBJ-entity-display](#mem-obj-entity-display). SRC-1, `src/fact.rs`, `src/entity.rs`, `src/consolidate.rs`, `src/ops.rs`.

Lineage: rules or model proposals from eligible events, or caller remember/correct content. Extraction places even model-rephrased statements as `ExplicitAssertion`, with private visibility and active status; the kind label does not distinguish verbatim user assertion from derived sentence. Extraction IDs hash entity, predicate and lowercased statement. Exact re-extraction upserts the fact with the current single source reference, rather than preserving all corroborating sources. Near-duplicate candidates can be dropped without attaching their source. Temporal fields exist, but automatic extraction initializes them to None.

Consumers: later extraction receives active statement summaries and duplicate-check text; lexical search uses status, dates and visibility; entity/ID reads use narrower gates; hooks and writeback select and deliver statements. The actual host receives natural-language information or instructions, not an enforced command. A decision's reason persists only when carried in statement text or source evidence; there is no separate extraction rationale field. Original content validity and host compliance remain unobserved.

Distinct identity: result/input data shared across [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change) and host routes, not a duplicate route or task object.

> let fact = Fact {
>     id: fact_id,
>     predicate: p.predicate,
>     statement: p.statement,
>     kind: FactKind::ExplicitAssertion,
>     status: FactStatus::Active,
> --- `src/consolidate.rs`

#### MEM-OBJ-source-ref
Label: Fact lineage and retained evidence quote

Source-native identity: `SourceRef` in `Fact.sources`. Storage: entity YAML in the same Git snapshot as the statement. Symbolic event ID and role identify lineage; natural-language evidence is a retained source fragment. It is not a stored proof of entailment. SRC-1, `src/fact.rs`, `src/consolidate.rs`, `src/cli.rs`, `src/ops.rs`.

Extraction attaches the cited event role and proposed evidence after quote-presence validation; direct CLI changes synthesize a user-role source with the submitted statement, without journaling that source event in the inspected handler. Shared operation assertions have empty sources. Therefore neither a nonempty reference nor an assertion label guarantees recoverable journal lineage.

Consumers: placement/re-ingestion retirement uses source IDs; erasure derives source-event redaction targets; lexical search returns IDs, and optional CLI enrichment resolves those IDs to initial lines of full journal text. Ordinary search does not return this evidence string. Ordinary read/history returns statements/status, hooks IDs/statements, and writeback IDs/statements. These omissions prevent a claim that the retained reasons/evidence accompany all later uses. A public snapshot API affords inspecting full entity YAML, but no automatic host evidence-reading route is established by that capability alone.

Distinct identity: evidential part of [MEM-OBJ-fact](#mem-obj-fact); compared with [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change) and [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval), which describe operations, not this retained part.

> pub struct SourceRef {
>     pub event_id: String,
>     pub role: Role,
>     pub evidence: String,
> }
> --- `src/fact.rs`

#### MEM-OBJ-controls
Label: Retained suppression and deletion controls

Source-native identity: `Controls` in `state/controls.json` inside Git. Symbolic suppression/retraction/deletion/redacted-event collections affect software eligibility and update placement; optional natural-language suppression reasons explain removal. Lineage is caller forget/erase or computed tidy findings. Consumers read membership, not the reason's content, to exclude fact IDs; consolidation constructs blocked IDs from suppression and deletion. The ID map treats Audience/Review variants as suppressed by presence; the inspected `is_suppressed` does not interpret audience or review date. SRC-1, `src/controls.rs`, `src/consolidate.rs`, `src/search/lexical.rs`, `src/ops.rs`, `src/tidy.rs`.

Tidy retains “duplicate of <ID>” or “session-only, not lasting,” not the model's underlying rationale. No inspected next-update route reads these reasons to revise its extraction criteria. ID-specific controls prevent replaying an identical derived ID, not every reformulation of forgotten content. Raw journal searches, generated instruction blocks and already delivered host context have independent lifetimes. Writeback does not load Controls. These are limits on withdrawal, not a claim that ordinary soft-forget fails: shipped forget/tidy also retract the fact itself.

Distinct identity: persistent policy state used across [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change), [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) and [RT-RTE-erasure-maintenance](runtime.md#rt-rte-erasure-maintenance), not those routes.

> pub fn is_suppressed(&self, target: &str) -> bool {
>     self.suppressions.contains_key(target)
> }
> --- `src/controls.rs`

#### MEM-OBJ-checkpoint
Label: Published journal progress checkpoint

Source-native identity: `Checkpoint` in `state/checkpoint.json`. Symbolic JSON progress/timestamp fields, Git storage. Its schema permits accepted/quarantined event IDs and reasons, but actual consolidation clears both and writes outcomes separately. Later consolidation uses through_seq to select the next window; status/hooks use lag derived from it. It is access/progress metadata, not a compacted conversational summary or learned textual rule. SRC-1, `src/checkpoint.rs`, `src/consolidate.rs`, `src/ops.rs`, `src/hook.rs`.

Distinct identity: progress state of [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), distinct from its derived facts and disposition history; no supplied object counterpart.

> // Outcomes live in the disposition file; the checkpoint only records
> // how far the journal has been consolidated, so it stays small.
> checkpoint.accepted.clear();
> checkpoint.quarantined.clear();
> --- `src/consolidate.rs`

#### MEM-OBJ-dispositions
Label: Per-batch extraction outcome record

Source-native identity: `Dispositions`, stored at `state/dispositions/<request>.json` in published Git. Symbolic request/extractor/window/sequence fields plus natural-language quarantine categories retain which event sequences were accepted or rejected. The producer is consolidation. Event acceptance does not prove a new fact was stored: placement can drop blocked/near-duplicate proposals after the gate, while the sequence still enters accepted. Candidate-specific gate failures are only optionally printed; the durable aggregate may say “no durable fact.” SRC-1, `src/consolidate.rs`.

Later consumer limit: the inspected consolidation loop reads checkpoint, controls and entities, not these outcome files; no implemented automatic retry/criterion-revision consumer of the quarantine explanation was found in that loop. Git storage affords manual inspection. Distinct from [MEM-OBJ-checkpoint](#mem-obj-checkpoint) and [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation); no supplied operative-object counterpart.

> Ok(proposal) => {
>     ex.place(proposal, event);
>     ex.accepted.insert(event.seq);
> }
> --- `src/consolidate.rs`

#### MEM-OBJ-entity-display
Label: Entity body and compact navigation index

Source-native identity: `EntityFile.body` and `INDEX.md`. Storage: Markdown in published Git; natural-language/display text with symbolic fact/entity IDs shown for navigation. They are generated from structured entities, not independent evidence or alternative conversation checkpoints. Entity refresh renders every status-active statement, without temporal or Controls filtering. Index shows entity type/title and status-active counts, sorted by ID, with a 60,000-byte row budget and remainder count. Different readers can therefore see displays whose “active” meaning is weaker than lexical eligibility. SRC-1, `src/entity.rs`, `src/index.rs`, `src/fact.rs`.

Consumers: humans or external snapshot readers can inspect these displays; the core search reads parsed facts, not the Markdown body or INDEX as its retrieval corpus. `mem index` republishes the navigation summary. No implemented host context selection from INDEX is established. Distinct derived display data, compared with [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval) and [RT-OBJ-mem-skill](runtime.md#rt-obj-mem-skill), neither of which declares it.

> for fact in self.facts.iter().filter(|f| f.status == crate::fact::FactStatus::Active) {
>     out.push_str(&format!("- [{}] {}\n", fact.id, fact.statement));
> }
> --- `src/entity.rs`

### Routes

#### MEM-RTE-adapter-ingestion
Label: Adapted source acquisition into journal

Owner/endpoints: caller-selected files or local/all-host discovery → adapters → CLI BulkWriter → journal; public library callers can supply JournalEvent directly. Trigger is an open ingest/backfill request or detached hook sync. Inputs include chat, host transcripts, Markdown, calendar, voice and IDE history. Software parses, filters, assigns lineage/sequence and deduplicates bulk event IDs. Authors supply the original text, but file selection/command invocation does not prove per-content human approval or genuine user origin. Generic caller control remains unresolved. Guidance is format/role parsing and shipped sync procedure, not a truth oracle. No expected-answer oracle is used. Admission is syntactic acquisition, not knowledge validation; adapter/I/O/lock failures can reject or skip input. CLI explicit flush and bulk tail recovery provide persistence/recovery protocols, not observed durability. There is no whole-import rollback; some events can remain after later failure. SRC-1, `src/cli.rs`, `src/ingest.rs`, `src/journal.rs`, `src/lib.rs`.

Distinct identity: acquisition precedes [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), whose declared endpoints start at retained events. It shares hook initiation with [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks), not their context delivery or extraction admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts/plans/skips from CLI; BulkWriter returns admitted event or None for duplicate; direct Journal append returns an event.
- Later read-back: Consolidation reads events after checkpoint; raw search/read/source enrichment reloads journal text in later invocations, independently of consolidation acceptance.
- Delegated visibility: Adapter reads available local files; later extraction sees only selected roles/chunks; later search may expose adapted assistant or tool material too.
- Selection predicate: Caller format/path/project and discovery rules; adapter text/role filters; BulkWriter event-ID seen set. Public Journal::append does not use that seen set.
- Invalidation or expiry: No general raw-event expiry; unchanged Markdown is skipped by path/content-hash ID, changed Markdown becomes a new event; erase separately redacts cited events.
- Activation or effect: Durable input for later extraction or host retrieval is wired; actual retention/completion and downstream reliance are uninspected.
- Evidence limits: Adapted text is not a complete transcript or authenticated human input. Public append assigns sequence before taking the lock and lacks bulk dedup; do not generalize the CLI bulk sequencing/dedup protocol to every library writer.

> pub fn append(&self, mut event: JournalEvent) -> Result<Option<JournalEvent>> {
>     if !self.seen.lock().insert(event.event_id.clone()) {
>         return Ok(None);
>     }
> --- `src/journal.rs`

> pub fn append(&self, mut event: JournalEvent) -> Result<JournalEvent> {
>     let max_seq = max_seq_in(&self.dir)?;
>     event.seq = max_seq + 1;
> --- `src/journal.rs`

#### MEM-RTE-index-rebuild
Label: Current entities to published navigation index

Owner/endpoints: caller `mem index` or public rebuild → current entity parsing/render_index_md → DomainValidator/publisher → new Git revision or unchanged head. Manual open maintenance, no model proposal or answer oracle. Software proposes index content from current structured entities; caller chooses invocation, not individual rows. Parser/budget rules shape the proposal. Invalid candidate/CAS/I/O can reject publication; previous Git state remains, with no automatic semantic rollback. SRC-1, `src/index.rs`, `src/cli.rs`. Distinct auxiliary update from [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) and [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change), which refresh the same index alongside other content.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unchanged head if index matches; otherwise new publication revision and CLI message.
- Later read-back: External snapshot/file inspection can obtain the retained index; core search instead reloads entities, so index use by a host is afforded rather than deployed here.
- Delegated visibility: Publisher sees the candidate index; caller sees revision/outcome; model delegation is inapplicable.
- Selection predicate: Eligible entity files parsed from current head, sorted entity IDs, status-active counts, 60,000-byte row budget.
- Invalidation or expiry: Rebuild or memory writes replace the index; no independent expiry.
- Activation or effect: Maintains navigation display, not extraction criteria or model weights; host reliance is uninspected.
- Evidence limits: Index counts do not establish temporal eligibility, truth or successful host consumption.

> let current = repo.read_snapshot(&base, INDEX_MD)?.map(|b| b.content);
> if current.as_deref() == Some(body.as_str()) {
>     return Ok(base);
> }
> --- `src/index.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation)

Memory-specific input/consumer chain: adapted events → selected user/Note text → rules or bounded model proposals → quoted sourced statements → published entities → next extraction summary/duplicate checks and later search/hooks/writeback. This is automatic derivation into retained behavior-shaping text; no parameter training is established. Rules only use user-role regex matches. LLM Note selection is broader than project memory: CalendarAdapter and VoiceAdapter create Note events; generic Markdown is not restricted to named instruction files. `call_llm` labels every Note as memory_file. The prompt's curated-file trust premise is therefore not an implementation source-authentication boundary (SRC-1, `src/ingest.rs`, `src/consolidate.rs`).

> let kind = if e.role == Role::Note { "memory_file" } else { "user_message" };
> --- `src/consolidate.rs`

Budgets: user text clipped at 2,000 characters; Note text split into paragraph-aligned chunks up to 8,000 characters, then clipped. Batching compares text byte lengths against 16,000. Existing context caps 200 entities, 40 active facts each, and an 8,000-byte statement budget; titles/IDs are additional payload. Parallel batches share pre-batch known entities, while software placement sees accumulated proposals. No complete knowledge-context guarantee follows. A high-water window advances globally even if scope removes events. These omitted events are not automatically reconsidered by a later scope run (SRC-1, `src/consolidate.rs`, `src/cli.rs`).

> const USER_EVENT_CHARS: usize = 2_000;
> const NOTE_EVENT_CHARS: usize = 8_000;
> --- `src/consolidate.rs`

Changed-file retirement compares path/content-hash source IDs and marks active facts superseded when all their sources refer to older versions represented in the batch. It runs after either extractor, not only after successful new extraction. Known later transforms persist even though input authorship is unresolved. Replacement can retire content even with no replacement fact, for example rules processing a Note file. Re-extracting the exact fact overwrites its source with the new reference; missing old facts are superseded, but this is not semantic contradiction diagnosis. SRC-1, `src/consolidate.rs`.

> if outdated {
>     fact.status = FactStatus::Superseded;
>     touched = true;
> }
> --- `src/consolidate.rs`

> retire_outdated_file_facts(&mut extraction, &bounded);
> --- `src/consolidate.rs`

The duplicate word set excludes negation/modality words including not/no/never/must; overlap/containment can reject statements that differ on those terms. Thus duplicate elimination is implemented curation, not proof that kept and dropped statements mean the same thing. Quote presence supplies neither entailment nor lasting usefulness, as the supplied route already establishes. Acceptance dispositions can outlive rejection of a particular placement ([MEM-OBJ-dispositions](#mem-obj-dispositions)).

> "project", "user", "includes", "include", "consists", "assistant", "agent", "must", "always",
> "should", "only", "when", "not", "no", "never", "do", "does", "wants", "want", "prefers",
> --- `src/consolidate.rs`

#### On [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval)

Read paths differ. Lexical facts enforce status, temporal bounds, visibility and control membership; scope_filter applies to journal selection, not every fact. Optional project/source filtering occurs after fact shortlisting. Journal search selects source-side content and metadata and returns excerpts, not entire events; ID read returns full retained event content. Default hits carry source IDs but not evidence quotes. CLI --source-lines adds first-N-line journal excerpts by ID after final selection; a CLI-synthetic source can be missing. SRC-1, `src/ops.rs`, `src/search/lexical.rs`, `src/search/journal.rs`, `src/cli.rs`.

`memory_history` is a current-head entity-fact listing, including retained superseded statuses, not traversal of previous Git commits. `memory_read` by fact ID can return a superseded or expired fact with a status label; entity read filters status Active but does not call temporal eligibility. `find_fact` omits suppressed/deleted IDs, not all temporal ineligibility. Consequently the label current is not proof the statement is currently temporally valid. These are read-contract refinements, not claims that Git history is unavailable through the public repository API.

> let records: Vec<Value> = found
>     .facts
>     .iter()
> --- `src/ops.rs`

#### On [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change)

Caller authors/edits statement content; admission software handles structure and publication, not evidential truth. CLI sources are synthetic, shared operation sources empty. Forget persists supplied reason, but later eligibility uses the ID, not that reason's interpretation. Durable intents/receipts govern recovery/replay, not learned fact content or host instruction authority. These distinct parts should not be classified as equivalent knowledge. SRC-1, `src/cli.rs`, `src/ops.rs`; publisher/recovery evidence supplied in the annotated record.

#### On [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks)

Start and prompt are independent unsolicited supply, even though the host callback initiated the executable. Start selects pref_user via entity read and takes at most 20 statements, with no character/token budget. Prompt takes 600 input characters, requests 12 facts-only lexical hits, applies meaningful-word overlap, and delivers at most six IDs/statements without quotes. Temporal eligibility differs because Start uses entity read while Prompt uses lexical search. The host consumer receives ordinary natural-language guidance; retention/delivery is wired, activation remains external. SRC-1, `src/hook.rs`, `src/ops.rs`.

#### On [RT-RTE-instruction-writeback](runtime.md#rt-rte-instruction-writeback)

The generated block carries statements/IDs and a truncated source revision, not source quotes or full rationale. It can later become host instruction context or a new Markdown Note input during backfill. MarkdownAdapter reads the complete file, including the generated block; there is no managed-block stripping in that adapter. Default file-only-source omission limits some duplication, but --include-file-facts and the reinjected derived block keep a feedback path available. Original hand-authored versus generated-file provenance is not recovered merely from Role::Note (SRC-1, `src/cli.rs`, `src/ingest.rs`).

Writeback skips three inactive status variants but does not call Fact::is_eligible or load Controls. Disputed, future-valid or past-valid active content can therefore reach the block. This qualifies any implied uniform eligibility across read channels. Ordinary forget/tidy status retraction still excludes their facts; external/custom control-only changes do not share that protection.

> if matches!(
>     fact.status,
>     crate::fact::FactStatus::Superseded
>         | crate::fact::FactStatus::Retracted
>         | crate::fact::FactStatus::Expired
> ) {
>     continue;
> }
> --- `src/cli.rs`

#### On [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance)

Cleanup model receives IDs/statements, not retained sources or original event context, in 60-fact batches. Duplicate curation keeps longer text using overlap, not semantic verification. Persistent reasons name duplicate target or session-only classification; no model explanation is requested/retained. Apply reloads/rejudges, so the shown list is not itself the durable admitted candidate. Later control consumers honor IDs; they do not learn a new cleanup rule from the reason. SRC-1, `src/tidy.rs`.

> Some(keep) => format!("tidy: duplicate of {keep}"),
> None => "tidy: session-only, not lasting".to_string(),
> --- `src/tidy.rs`

#### On [RT-RTE-erasure-maintenance](runtime.md#rt-rte-erasure-maintenance)

One removed fact can cite an event that also supports other facts. The journal stage redacts the whole cited event, not only the quote, so surviving facts can lose readable source context. Controls retain deleted IDs and redaction markers; the current publication records Completed before actual journal/history/intents stages. External source transcripts and written AGENTS blocks remain; later re-ingestion of external content or reformulation is not ruled out by ID controls. The supplied partial-failure limitation prevents claiming reliable all-substrate withdrawal. SRC-1, `src/erasure.rs`, `src/journal.rs`, `src/consolidate.rs`.

#### On [RT-OBJ-tasks](runtime.md#rt-obj-tasks)

Task titles are caller-supplied natural-language work descriptions; version/IDs are software coordination metadata, not evidence or derived fact criteria. Persistence horizon is later tasks_read invocations in the same root. Host task execution authority remains a consumer decision, not enforced by storing a title. Supplied record and [RT-RTE-task-update](runtime.md#rt-rte-task-update) support the separate file/lock admission account (SRC-1, `src/ops.rs`, `src/mcp.rs`).

## Write side

Acquisition retains adapted text with caller/discovery selection and software parse/dedup admission ([MEM-RTE-adapter-ingestion](#mem-rte-adapter-ingestion)). It is neither per-fact human approval nor automatic proof of user authorship. All-host and local-host paths, generic formats and public append are different source-selection surfaces.

Consolidation transforms retained events into self-contained standing statements, assigns entities/predicates/IDs, rejects role/harness text, requires model lasting and quote-presence gates, removes near duplicates, spills large entities, retires outdated file-only facts, and publishes outcomes/checkpoint/content together. Rule extraction supplies a narrower alternative. The next batch consumes retained statements and controls, not prior model reasoning. Rejection history persists separately; no later automatic consumer of its reasons is established. The chain is explicit in the annotation on [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation). No target conversation-summary compaction route is established by these reads; imported host summaries can be filtered as injected user text, while provider-internal processing is uninspected. Checkpoints are progress state, not an alternative semantic summary ([MEM-OBJ-checkpoint](#mem-obj-checkpoint)).

Direct remember/correct admits caller content without extraction warrant, with correction changing status and forget changing status/control membership ([RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change)). A user invoking the skill may author or approve a change, but generic transport/library identity does not settle that contribution. Receipts and durable intents retain change/recovery state rather than evidence about truth. Tidy/erasure retain reasons and eligibility/removal state, with human review only a host procedure and irreversible removal only conditional on all stages completing. Reworded content, raw journal and external copies have separate withdrawal limits ([MEM-OBJ-controls](#mem-obj-controls), supplied maintenance routes).

Writeback is material instruction-surface editing, not merely storage: caller chooses target/options; software selects and renders statements without per-content approval. It can also feed derived text back to later extraction. Index rebuilding is deterministic display maintenance. Tasks, installed host configuration/skill, and model-selection files are separate admitted retained results with separate later consumers. Their initialization provenance does not erase the known subsequent file/configuration updates ([MEM-RTE-index-rebuild](#mem-rte-index-rebuild), [RT-RTE-task-update](runtime.md#rt-rte-task-update), [RT-RTE-integration-admission](runtime.md#rt-rte-integration-admission)).

## Read-back

Requested search and ID lookup return selected retained statements or adapted raw text through CLI/shared tools. Search's bounded shortlist and ranking affect delivery, not content truth; an unspecified library caller establishes capability rather than an exercised consumer. The shipped skill supplies an external consumer role and directs answering from hits, prioritizing curated facts and citing IDs. It does not supply evidence of execution:

> JSON `hits`, best first. `fact_…` ids are curated facts (trust these first); `journal:…` ids are raw session excerpts (context, may be outdated). For more on one hit: `mem read <id>`. Answer from the hits and cite fact ids. If nothing relevant comes back, say memory has nothing on it; do not guess.
> --- `skills/mem/SKILL.md`

Automatic hooks push retained preferences or prompt-matched statements into additionalContext. Writeback persists statements in an instruction file that a later host may load. These have independent triggers/budgets and can omit stored rationale. [RT-BAP-host-context](runtime.md#rt-bap-host-context) and [RT-BAP-instruction-file](runtime.md#rt-bap-instruction-file) locate the actual host channels and conditional authority. Within mem, later extraction uses prior statements and controls; status and hook sync consume checkpoint lag; recovery consumes intents/receipts; task reads return their separate versioned file. Delivery to any of these consumers is not demonstrated benefit.

Evaluation consumes the same retrieval pipeline against caller expected IDs/string constraints. Its transient report and CLI benchmark timing output do not feed a retained automatic winner, model update or cleanup decision. Independence and quality of the rubric are unknown ([RT-RTE-search-evaluation](runtime.md#rt-rte-search-evaluation); SRC-1, `src/evaluation.rs`, `src/cli.rs`).

## Integration issues

- **Note trust is broader than the supplied memory-file wording.** Calendar/voice/generic Markdown can enter the same model framing as project instructions. This qualifies source-trust and trace-origin classification of [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation); it does not invalidate known transformations. Evidence: direct `src/ingest.rs`, `src/consolidate.rs`, SRC-1; [MEM-OBJ-journal-event](#mem-obj-journal-event).
- **Current-head history and inconsistent eligibility need retaining.** The supplied retrieval route's broad read/history description should not imply Git traversal or uniform lexical eligibility. ID/entity read, display and writeback differ on temporal/status/control gates. Evidence: `src/ops.rs`, `src/fact.rs`, `src/search/lexical.rs`, `src/cli.rs`, SRC-1; [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval), [RT-RTE-instruction-writeback](runtime.md#rt-rte-instruction-writeback), [MEM-OBJ-entity-display](#mem-obj-entity-display). This prevents a universal current-context validity or suppression guarantee.
- **Public journal admission is not the bulk protocol.** The supplied runtime's journal-lock language is correct for shipped bulk drivers, but does not establish universal append sequencing/dedup. Direct append computes its sequence before locking and does not check event-ID duplicates. Evidence: `src/journal.rs`, SRC-1; [MEM-RTE-adapter-ingestion](#mem-rte-adapter-ingestion), [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation). No concurrency outcome was observed.
- **Accepted event is not equivalent to added fact.** Placement may drop blocked/duplicate content while accepted records the event. Checkpoint accepted/quarantined collections are cleared; dispositions are the actual durable outcome location. Evidence: `src/consolidate.rs`, SRC-1; [MEM-OBJ-dispositions](#mem-obj-dispositions), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation). This prevents treating acceptance counts as verified knowledge growth or retained criticism use.
- **Withdrawal is ID- and channel-bounded.** Reasons persist but later filters use membership; raw events, external instruction blocks and reformulations remain separate. Whole-event erasure can remove context supporting surviving facts, and partial failures remain unresolved. Evidence: `src/consolidate.rs`, `src/tidy.rs`, `src/erasure.rs`, `src/ops.rs`, SRC-1; [MEM-OBJ-controls](#mem-obj-controls), [MEM-OBJ-source-ref](#mem-obj-source-ref), supplied forget/tidy/erase routes. No universal semantic forgetting or all-copy deletion conclusion.
- **Duplicate identity comparison:** no new declaration duplicates a supplied referent. New objects identify retained data absent from the supplied object declarations; new acquisition/index routes are distinct operations, while existing referents receive annotations. [MEM-OBJ-source-ref](#mem-obj-source-ref) separates an evidential part of [MEM-OBJ-fact](#mem-obj-fact); [MEM-OBJ-entity-display](#mem-obj-entity-display) groups display renderings without conflating them with search-consumed structured facts. Reconciliation should preserve these distinctions.
- **Unresolved provenance and exercised effects:** source roles do not authenticate human authorship; generic changes do not prove human approval; provider exact weights/processing and real host use remain uninspected. Some all-host discovery details and history scrub internals remain supplied rather than direct evidence. No additional source or scope change is requested. These gaps prevent completeness of imported history, semantic quality, exercised learning and benefit conclusions across the cited acquisition, extraction, ranking and host routes.

## Limitations and checks

Checkout HEAD was rechecked as `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`; source identity/run identity match the supplied boundary and invocation. Method identity is the supplied job, member types, collection and records contract; no method commit was supplied, and none is inferred. No target, tests, examples, provider calls or runtime fixtures were executed.

Strong claims were checked against alternate paths: direct assertions versus extraction evidence gates, all Note producers versus project-file trust, public append versus bulk writes, direct/entity reads and writeback versus lexical eligibility, and raw/context copies versus fact withdrawal. This is source inspection, not execution or a causal experiment. Remaining uncertainties are beside the mechanisms they limit.

Validation: passed deterministic Commonplace member/artifact content validation; this establishes form, relation resolution and quotation occurrence, not analytical acceptance, exercised operation or benefit.
