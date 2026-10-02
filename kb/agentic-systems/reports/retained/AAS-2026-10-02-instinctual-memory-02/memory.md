---
type: agentic-systems/types/agent-memory-analysis-report.md
description: "Instinctual-memory retained facts, source journal, eligibility state and host delivery"
run-id: AAS-2026-10-02-instinctual-memory-02
source-identity: "https://github.com/jasonkneen/instinctual-memory"
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
report-status: complete
memory-comparison: {"scope": "Accumulated curated facts, source-event journal, index/controls/checkpoint and operation metadata, versioned task list, and derived project-file exports, including their acquisition, curation and later-consumer routes. Excludes static shipped skills/prompts, installation configuration, model assets/selection and temporary query/evaluation state; host internals and provider weights remain outside the frozen boundary.", "axes": {"storage_substrate": {"assessment": "known", "values": ["files", "repo"], "evidence": {"files": {"basis": "wired", "records": ["OBJ-2", "OBJ-3", "OBJ-4"], "note": "Journal, task list and exported project guidance persist in files."}, "repo": {"basis": "wired", "records": ["OBJ-1"], "note": "Curated content and its controls/checkpoint/index persist in Git."}}, "records": ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4"], "note": "Git snapshots hold curated facts and access state; JSONL, task and exported Markdown files hold remaining scoped retained material."}, "representational_form": {"assessment": "known", "values": ["natural-language", "symbolic"], "evidence": {"natural-language": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4"], "note": "Statements, source text, task titles and exports contain prose."}, "symbolic": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "OBJ-4"], "note": "Structured metadata and retained access state govern later operations."}}, "records": ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4"], "note": "Statements and source text coexist with structured provenance, IDs, eligibility controls, checkpoints and versions. External ranker/extractor weights are machinery, excluded from accumulated-memory scope."}, "lineage": {"assessment": "known", "values": ["authored", "imported", "trace-extracted", "other-compiled"], "evidence": {"authored": {"basis": "wired", "records": ["RTE-2", "RTE-7"], "note": "Explicit changes and task additions author retained content."}, "imported": {"basis": "wired", "records": ["RTE-10"], "note": "Adapters import session text and project files into the journal."}, "trace-extracted": {"basis": "wired", "records": ["RTE-3"], "note": "Rules or model extraction converts retained experience into facts."}, "other-compiled": {"basis": "wired", "records": ["OBJ-1", "RTE-8"], "note": "Published index/checkpoint/controls and rendered exports are generated from content or operation outcomes."}}, "records": ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4", "RTE-2", "RTE-3", "RTE-10"], "note": "User/host authoring, transcript/file imports, extracted facts, and generated access/export state all fall inside the stated scope."}, "behavioral_authority": {"assessment": "known", "values": ["knowledge", "instruction", "learning", "ranking", "routing", "validation", "enforcement"], "evidence": {"knowledge": {"basis": "wired", "records": ["RTE-1", "OBJ-4"], "note": "Facts, raw sessions and tasks supply reference context to callers."}, "instruction": {"basis": "wired", "records": ["RTE-5", "OBJ-3"], "note": "Retained preferences are emitted as working guidance to a host."}, "learning": {"basis": "wired", "records": ["RTE-3", "OBJ-2"], "note": "Retained user turns and note events feed durable fact production for later context."}, "ranking": {"basis": "wired", "records": ["RTE-1", "OBJ-1", "OBJ-2"], "note": "Retained text, aliases and journal content determine lexical candidate priority."}, "routing": {"basis": "wired", "records": ["RTE-3", "OBJ-1"], "note": "Checkpoint sequence selects the next journal window."}, "validation": {"basis": "wired", "records": ["RTE-3", "OBJ-1"], "note": "Retained suppressed/deleted IDs reject fact proposals."}, "enforcement": {"basis": "wired", "records": ["RTE-1", "RTE-3", "OBJ-1", "RTE-7"], "note": "Controls exclude curated facts and veto re-admission; task version vetoes stale updates."}}, "records": ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4", "RTE-1", "RTE-3", "RTE-5", "RTE-7"], "note": "Forces refer to the consumed part. Target-side selection and admission are wired; instruction/knowledge delivery does not establish excluded-host compliance."}, "write_agency": {"assessment": "known", "values": ["automatic", "manual"], "evidence": {"automatic": {"basis": "wired", "records": ["RTE-3", "RTE-10"], "note": "Adapters and consolidation automatically acquire/transform records."}, "manual": {"basis": "wired", "records": ["RTE-2", "RTE-7"], "note": "Caller supplies fact statements or task titles for explicit admission."}}, "records": ["RTE-2", "RTE-3", "RTE-7", "RTE-10"], "note": "Manual authoring and automatic trace transformation coexist; an operator triggering extraction does not make extraction manual."}, "curation_operations": {"assessment": "partial", "values": ["consolidate", "dedup", "evolve", "invalidate", "decay"], "evidence": {"consolidate": {"basis": "wired", "records": ["RTE-3"], "note": "Standing facts reduce retained conversation/note content."}, "dedup": {"basis": "wired", "records": ["RTE-3", "RTE-4"], "note": "Near-duplicate word overlap rejects restatements and tidy suppresses duplicates."}, "evolve": {"basis": "wired", "records": ["RTE-2"], "note": "Correction supersedes a fact with revised content."}, "invalidate": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "Forget, tidy and changed-file retirement withdraw current reliance while retaining history."}, "decay": {"basis": "wired", "records": ["RTE-1"], "note": "Fact expiry and valid-to timestamps exclude retained facts from current lexical retrieval; ordinary producers leave expiry unset."}}, "records": ["RTE-2", "RTE-3", "RTE-4", "RTE-6", "RTE-1"], "note": "Inspected deterministic operations support these values. Model-generated proposal content is opaque; no complete claim about every semantic transformation, including possible synthesis, is justified."}, "read_back_direction": {"assessment": "known", "values": ["pull", "push"], "evidence": {"pull": {"basis": "wired", "records": ["RTE-1", "RTE-7"], "note": "Explicit search/read/history and task reads return retained content."}, "push": {"basis": "wired", "records": ["RTE-5"], "note": "Session/prompt hooks emit retained preferences or prompt-matched facts without a memory request."}}, "records": ["RTE-1", "RTE-5", "RTE-7", "RTE-8"], "note": "Requested tool/CLI reads coexist with automatic hook supply. Export writing is requested; later host startup consumption is afforded rather than demonstrated."}, "read_back_signal": {"assessment": "known", "values": ["coarse", "identifier", "inferred-lexical"], "evidence": {"coarse": {"basis": "wired", "records": ["RTE-5"], "note": "Session start checks that active facts exist before emitting startup context; preferences are budgeted to twenty."}, "identifier": {"basis": "wired", "records": ["RTE-5"], "note": "Session start requests pref_user, selecting its retained preference statements."}, "inferred-lexical": {"basis": "wired", "records": ["RTE-5"], "note": "Prompt words rank facts, then meaningful-term overlap selects at most six for injection."}}, "records": ["RTE-5", "RTE-8"], "note": "Hook pushes combine availability gating, fixed preference-entity selection and prompt-word matching. Explicit model-reranked search is pull and adds no inferred-judgment push signal."}, "trace_learning": {"assessment": "known", "values": ["yes"], "evidence": {"yes": {"basis": "wired", "records": ["RTE-3", "RTE-5"], "note": "Retained user turns and qualifying note events become persistent context/guidance facts."}}, "records": ["RTE-3", "RTE-5", "OBJ-2"], "note": "Automatic trace-fed writes create durable facts subsequently available to retrieval and hook context; this classifies a write route, not demonstrated capacity improvement."}, "trace_source": {"assessment": "known", "values": ["session-logs", "event-streams"], "evidence": {"session-logs": {"basis": "wired", "records": ["RTE-3", "RTE-10"], "note": "User conversational records feed rules and model extraction."}, "event-streams": {"basis": "wired", "records": ["RTE-3", "RTE-10"], "note": "Calendar and voice adapters produce Note events; the model extractor admits Note content as candidates."}}, "records": ["RTE-3", "RTE-10", "OBJ-2"], "note": "User turns qualify as session logs; imported calendar summaries and timestamped voice content qualify as event streams when admitted through note extraction. Tool-role IDE events are raw retrieval only on inspected extractors, not a qualifying tool-trace update."}}}
---

# Instinctual-memory memory report

## Boundary and evidence

The boundary is the source register's frozen Git commit. SRC-1 supplies executable mechanisms; SRC-2 supplies declared use. There is no observed run or causal experiment. The memory scope includes material accumulated or changed through use, including access metadata that affects later selection/admission. External inference components CMP-1, CMP-2 and CMP-3 are processing machinery, not memory learned by this target. Supplied runtime findings were checked against direct source reads; no host execution is inferred from registration or output.

| Operation / surface | Direct source reads | Covering records / limit |
|---|---|---|
| CLI and library exposure; MCP tools | `src/cli.rs`, `src/lib.rs`, `src/mcp.rs`, `src/ops.rs` | RTE-1, RTE-2, RTE-7, RTE-10; same operation dispatch behind transports |
| Import and raw journal | `src/ingest.rs`, `src/ops.rs` | OBJ-2, RTE-10; runtime supplies journal durability account, no run evidence |
| Rules/model extraction, checkpoint, rejection | `src/consolidate.rs` | OBJ-1, RTE-3; provider semantic choices uninspected |
| Curated retrieval and temporal eligibility | `src/search/lexical.rs`, `src/fact.rs`, `src/ops.rs` | RTE-1; runtime supplies remote/local rerank fallback account |
| Correction/forget and tidy/erase | `src/change.rs`; supplied runtime `src/tidy.rs`, `src/erasure.rs` findings | RTE-2, RTE-4, RTE-6; no recovery or erasure outcome observed |
| Hook selection and asynchronous sync | `src/hook.rs` | RTE-5; emitted context is wired, host activation uninspected |
| Project export | `src/cli.rs` | OBJ-3, RTE-8; later host consumption afforded |
| Versioned tasks | `src/ops.rs` dispatch; supplied runtime task account | OBJ-4, RTE-7; task execution belongs to host |
| Evaluation and benchmark | `src/cli.rs` dispatch; supplied RTE-11 | No retained update loop established; excluded from accumulated-memory profile |
| Setup and model administration | `src/lib.rs`, `src/cli.rs` dispatch; supplied RTE-8 and RTE-9 | Static integration and production machinery excluded |

## Core ideas

Memory has two content channels. The journal retains raw imported material; Git entities retain selected standing facts with sources. Combined search interleaves fact and journal hits before optional reranking. Facts-only hook retrieval bypasses the raw journal. Suppression of a fact therefore does not itself remove the originating conversation from raw retrieval. Erasure has a separate journal-redaction stage. SRC-1: `src/ops.rs`, `src/consolidate.rs`; RTE-1, RTE-6, RTE-10.

Access state matters independently of prose. A retained checkpoint chooses future extraction windows. Suppressed/deleted IDs prevent exact-ID re-admission and exclude curated search hits. Neither implies general semantic rejection of every paraphrase. Near-duplicate detection uses stemmed word overlap and removes negation words from its word set, so its equivalence test does not establish semantic identity. SRC-1: `src/consolidate.rs`, `src/search/lexical.rs`; RTE-1, RTE-3.

Automatic supply has narrower selection than requested retrieval. Startup selects the preference entity and caps it at twenty statements. Prompt hooks use facts-only lexical matching and at most six facts. No token budget is enforced on the resulting statement text. The emitted prompt warns that recorded facts may need checking against current code. These are delivery mechanisms, with no evidence of host uptake or improved performance. SRC-1: `src/hook.rs`; RTE-5.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On OBJ-1 — Content and access parts of the published snapshot

Memory-specific parts: fact statements are natural-language knowledge/instruction; predicates, source identities, status and temporal fields are symbolic access/provenance. Storage substrate: repo. Lineage: authored or trace-extracted facts; imported project material contributes fact content; generated index/checkpoint/control/receipt data are other-compiled. Fact text and entity title/aliases influence ranking at lexical search. Controls act as enforcement and validation at search and extraction. Checkpoint sequence supplies routing at consolidation. Dispositions record batch outcomes, but the next window reads checkpoint position rather than those outcome reasons. Sources/evidence persist on facts; no route here proves a later consumer reads every rationale. Distinct parts need separate canonical assessment despite shared Git publication. SRC-1: `src/fact.rs`, `src/consolidate.rs`, `src/search/lexical.rs`, `src/change.rs`.

> let mut checkpoint = repo
>             .read_snapshot(&base, "state/checkpoint.json")?
>             .map(|b| Checkpoint::parse(&b.content))
>             .transpose()?
>             .unwrap_or_else(Checkpoint::empty);
>
>         let extractor = resolve_extractor(options.extractor);
>         let all_after: Vec<JournalEvent> = journal.read_from(checkpoint.through_seq + 1)?;
> --- `src/consolidate.rs:108-115` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> for fact in entity.facts {
>                 if controls.is_suppressed(&fact.id)
>                     || controls.is_retracted(&fact.id)
>                     || controls.is_deleted(&fact.id)
>                 {
>                     continue;
>                 }
>                 if !fact.visibility.allows(query.audience) {
>                     continue;
>                 }
>                 if !fact.is_eligible(now, query.include_disputed) {
>                     continue;
>                 }
>                 let haystack = format!("{} {} {}", fact.statement, entity.title, entity.aliases.join(" "));
>                 let words = tokenize(&haystack).iter().map(|t| stem(t)).collect();
>                 candidates.push((
>                     SearchHit {
>                         fact_id: fact.id.clone(),
> --- `src/search/lexical.rs:108-125` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On OBJ-2 — Raw source material and provenance

Storage substrate: files. Representational form: natural-language source content plus symbolic source/sequence/role/project metadata. Lineage: imported session logs and files, automatically acquired through RTE-10. Raw user turns and Note events supply learning inputs at RTE-3; journal content supplies knowledge and ranking inputs at RTE-1. IDE tool-role events remain raw traces on inspected extraction paths. Calendar summaries and voice cues are event-stream inputs even though their adapter emits Note records. No model parameters are stored or updated in this object. SRC-1: `src/ingest.rs`, `src/consolidate.rs`, `src/ops.rs`.

> let event = JournalEvent::new(
>                         scope_id,
>                         session_id,
>                         Role::Note,
>                         Source::Calendar {
>                             source_id: uid,
>                             position,
>                             occurred_at: when,
>                         },
>                         summary,
>                         Redaction::None,
>                     );
>                     events.push(event);
>                     position += 1;
> --- `src/ingest.rs:628-641` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> let event = JournalEvent::new(
>                 scope_id,
>                 session_id,
>                 Role::Note,
>                 Source::Voice {
>                     source_id: path
>                         .file_stem()
>                         .and_then(|s| s.to_str())
>                         .unwrap_or("voice")
>                         .to_string(),
>                     position,
>                     occurred_at: current_when,
>                 },
>                 current_text.clone(),
>                 Redaction::None,
> --- `src/ingest.rs:719-733` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On OBJ-3 — Derived project exports and emitted preferences

Only accumulated-memory parts are included: generated managed project blocks and retained facts/preferences emitted through hooks. Export storage substrate: files; stdout is a delivery channel. Representational form: natural-language statements with symbolic IDs and markers. Lineage: other-compiled rendering of retained facts. Exported standing preferences/instructions are afforded instruction at a later host startup consumer; hook preference supply is wired target-side. Other fact content supplies knowledge. Static installed skills and setup configuration are excluded. Existing exports are not automatically retracted by later fact suppression. SRC-1: `src/cli.rs`, `src/hook.rs`; RTE-8.

#### On OBJ-4 — Retained task content and version

Storage substrate: files. Representational form: natural-language titles and symbolic version/IDs. Lineage: authored titles, automatically maintained version. Later task reads supply knowledge/context to callers. Retained version supplies an enforced admission veto for stale tasks_update requests; this is enforcement and validation rather than learned task-execution skill. Write agency: manual content authoring. SRC-1: `src/ops.rs`; RTE-7.

#### On RTE-1 — Requested accumulated-memory retrieval

Read-back direction: pull. Consumers: requesting CLI/tool/library client. Selected retained parts: eligible fact statements and matching raw journal excerpts, or explicitly named fact/entity/event/history. Search budget: operation limit 1–20, default eight; fact query condensed to 200 characters; reranked fact pool capped at twenty. Selection inputs: query, retained text/title/aliases, optional filters and optional ranker judgment. Raw and curated pools are interleaved. Knowledge delivery and ranking are wired. Suppression/status/temporal enforcement applies to curated search; it is not a universal rule for every retained-file read. Delegated visibility: same-root client access, no agent-specific memory grant. Activation and benefit: uninspected excluded-host behavior. SRC-1: `src/ops.rs`, `src/search/lexical.rs`; supplied RTE-1 retains ranker fallback evidence.

Time-based exclusion supports decay at this consumer, conditional on a populated expires_at or valid_to. Ordinary immediate/consolidation producers set expiry to None; public Fact/change APIs expose richer temporal fields. This does not establish automatic age decay on all newly created memories. SRC-1: `src/fact.rs`, `src/change.rs`, `src/lib.rs`.

> if let Some(expires) = self.expires_at {
>             if expires <= now {
>                 return false;
>             }
>         }
>         if let Some(to) = self.valid_to {
> --- `src/fact.rs:73-78` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-2 — Authored correction and withdrawal

Write agency: manual statement/target selection followed by automatic structural admission. Curation: evolve through correction and invalidate through forget. Retained successor content, old status, source fields and suppression reasons outlive the request. Later consumers: retrieval, consolidation and export/hook routes; eligibility varies by path. Guarantee strength and replay limits remain as supplied RTE-2. Admission is structural and does not establish truth or an answer oracle. SRC-1: `src/change.rs`, `src/ops.rs`.

> .clone()
>                 .unwrap_or_else(|| new_fact.id.clone());
>             entity.supersede(&old_id, &new_fact.id)?;
>             entity.upsert_fact(new_fact.clone());
>             (entity, None, None)
>         }
>         ChangeKind::Forget => {
>             let Some(mut entity) = current else {
>                 return Err(Error::InvalidChange(format!(
>                     "forget: entity {} does not exist",
>                     request.entity_id
>                 )));
> --- `src/change.rs:125-136` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-3 — Automatic trace-fed durable facts

Write agency: automatic, including operator-triggered batches. Curation: consolidate user/note text into standing facts, dedup by deterministic near-overlap, invalidate facts whose sole file sources become outdated. Trace learning: yes, implementation conclusion status: wired; operation conclusion status: uninspected. Original trace sources: session-logs for user conversational turns; event-streams for calendar/voice Note content. Imported static project instructions have imported lineage, without themselves being experience traces. Tool and assistant roles do not enter the inspected extractors. Model proposal semantics are opaque; prompt intent and occurrence checks do not prove faithful extraction. SRC-1: `src/consolidate.rs`, `src/ingest.rs`; runtime RTE-3 retains the occurrence-check passage.

Raw-to-derived-to-later-consumer chain: OBJ-2 user/Note text → rules or model proposal → retained sourced OBJ-1 facts → later RTE-1 or RTE-5. Retained checkpoint selects sequence window; existing entities condition extraction and dedup; suppressed/deleted IDs validate and veto proposal placement. Sources/evidence and dispositions persist; outcome reasons are not used to revise the extraction prompt. Batch high-water bounds journal positions; separate model text chunk limits and sixty changed entities bound publication. Visibility: model receives candidate text and known entities, same-root clients later read admitted facts. Admission/roles/mode/recovery remain those of supplied RTE-3; no reference-answer oracle or human semantic admission gate is added. SRC-1: `src/consolidate.rs`.

> let mut ex = Extraction::new(entities);
>     ex.blocked = blocked;
>
>     // Only the user's own words and memory files can carry durable facts.
>     let mut candidates: Vec<(&JournalEvent, String)> = Vec::new();
>     for event in events {
>         let text = match event.role {
>             Role::Note => Some(event.content.clone()),
>             Role::User => user_words(&event.content),
>             _ => {
>                 ex.quarantined.insert(event.seq, "not a user statement or memory file".into());
>                 continue;
>             }
>         };
> --- `src/consolidate.rs:628-641` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> .suppressions
>             .keys()
>             .cloned()
>             .chain(controls.deletions.iter().map(|d| d.target.clone()))
>             .collect();
>         let mut extraction = match extractor {
>             ExtractorKind::Llm => llm_extract(existing, blocked, &bounded)?,
>             _ => rules_extract(existing, blocked, &bounded),
>         };
>         retire_outdated_file_facts(&mut extraction, &bounded);
> --- `src/consolidate.rs:149-158` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> .filter(|f| f.status == FactStatus::Active && f.id != fact_id)
>             .any(|f| {
>                 let other = content_words(&f.statement);
>                 jaccard(&words, &other) >= NEAR_DUPLICATE || contained(&words, &other)
>             })
> --- `src/consolidate.rs:440-444` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-4 — Tidy retained facts

Curation: dedup and invalidate, implementation conclusion status: wired from supplied RTE-4. Deterministic overlap/session-only findings can lead to retained retractions/suppressions after explicit apply; operator can keep named facts. Later search and consolidation consume changed controls. This does not establish useful cleanup in operation or automatic improvement. SRC-1: `src/tidy.rs`; supplied RTE-4.

#### On RTE-5 — Automatic retained-context supply

Read-back direction: push. Trigger: SessionStart or UserPromptSubmit. Startup availability is coarse (nonzero active-fact count); identifier selection requests pref_user; budget takes at most twenty preferences. Prompt selector receives up to 600 characters, ignores slash commands and fewer than three words, requests twelve facts-only lexical candidates, then selects at most six with at least two meaningful shared words (one if only one remains). Selected content: retained curated statements; no journal or model-reranked push. Signals: coarse, identifier and inferred-lexical. Channel: hook additionalContext. Host knowledge/instruction delivery implementation conclusion status: wired; host activation/operation conclusion status: uninspected. Errors emit nothing. End/sync adds source events and can invoke RTE-3 after backlog threshold, default 200. No host-context expiry/retraction protocol or per-agent visibility control is evidenced. SRC-1: `src/hook.rs`.

> }
>     let read = crate::ops::execute(root, "personal", "default", "memory_read", &json!({"id": "pref_user"}));
>     let prefs: Vec<String> = read.payload["facts"]
>         .as_array()
>         .map(|a| a.iter().filter_map(|f| f["statement"].as_str().map(str::to_string)).collect())
>         .unwrap_or_default();
> --- `src/hook.rs:89-94` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> if prompt.starts_with('/') || prompt.split_whitespace().count() < 3 {
>         return Ok(None);
>     }
>     let query: String = prompt.chars().take(600).collect();
>     let found = combined_search(
>         root,
>         &SearchParams {
>             query: &query,
>             limit: PROMPT_FACTS * 2,
>             rerank: false,
>             facts_only: true,
>             project,
>             ..Default::default()
>         },
>     )?;
>     // Injected context has to earn its place: a fact must share at least
> --- `src/hook.rs:117-132` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

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
>     if hits.is_empty() {
> --- `src/hook.rs:139-149` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-6 — Cross-store erasure limits

Write effect: removes targeted retained content from current Git tree, redacts linked journal sources and rewrites history; controls record withdrawal/deletion. Later retrieval is changed by those stages. Source-relative targeting and sequential recovery limits remain supplied RTE-6. Host originals, provider copies and prior project exports remain outside this erasure effect. No observed completion supports an operational deletion guarantee. SRC-1: `src/erasure.rs`; supplied RTE-6.

#### On RTE-7 — Requested task read-back and authored additions

Read-back direction: pull for tasks_read. Retained titles supply caller context; whole-list selection has no semantic push signal. Authored title admission increments retained version; expected-version mismatch blocks updates. Immediate response and future reads see the updated list when publication succeeds. No automatic task execution or trace-fed behavior update is established. SRC-1: `src/ops.rs`; supplied RTE-7 retains version-veto evidence.

#### On RTE-8 — Requested export with afforded later host read

Memory-specific part: explicit writeback request renders selected project entities and preferences into a persistent project file. Identifier/project filtering chooses scope; local-store default or all can select all. File-origin-only facts are excluded by default to avoid repeating project instructions. Operator selects destination/options; code writes a managed block, with force able to replace the file. Later startup consumption by the documented coding-agent role is afforded; actual host reading remains uninspected. No host token budget or automatic refresh guarantee is shown. Static setup is outside the accumulated-memory scope. SRC-1: `src/cli.rs`.

Writeback filters enum status and visibility rather than calling Fact::is_eligible or reading controls. It can include disputed facts and facts whose Active status remains despite a past expiry timestamp. This narrows the supplied description of “current active” export to its implemented predicate. SRC-1: `src/cli.rs`, `src/fact.rs`.

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

#### On RTE-10 — Automatic acquisition versus derived learning

Write agency: automatic acquisition, even when paths are chosen manually. Lineage: imported. Adapters preserve original content categories: project Markdown, conversation turns, calendar summaries, voice cues and IDE tool commands/results. Event identity dedup at append is acquisition idempotence, separately from content dedup at RTE-3/RTE-4. Raw journal retention alone is not trace learning; qualifying learning begins where user/Note content automatically produces durable facts. Source and batch provenance survive for later raw retrieval and consolidation. SRC-1: `src/ingest.rs`, `src/consolidate.rs`; supplied RTE-10 retains append-ID evidence.

## Write side

Explicit changes and tasks retain caller-authored content. Ingestion acquires raw source events. Rules or model consolidation automatically transforms admitted raw content into sourced facts, persists extraction position/outcomes, and makes the results available to future clients/hooks. Checkpoint position is published with facts, preventing a successful batch from advancing without its candidate snapshot. It is not an alternative continuation summary; this system's derived material is standing facts. SRC-1: `src/change.rs`, `src/consolidate.rs`, `src/ops.rs`; RTE-2, RTE-3, RTE-7, RTE-10.

Forget and tidy retract/suppress; changed-file extraction supersedes outdated facts; erase targets content across Git/journal/history. Those operations have different persistence and recovery effects. Reasons and source evidence remain with applicable records, but no inspected automatic loop uses them to improve its own admission rules. Runtime RTE-3's fixed extraction guidance is applied rather than revised. SRC-1: `src/change.rs`, `src/consolidate.rs`; supplied RTE-4, RTE-6.

## Read-back

Requested search/read/history and tasks_read deliver prior accumulated material to callers. Automatic hooks emit a smaller curated context selected by startup preference identity or current prompt lexical overlap. Requested export writes content that a future host may load. A tool return is pull even though delivery is automatic; model reranking belongs to that pull route. Hook output is push because the user did not request retained memory. SRC-1: `src/ops.rs`, `src/hook.rs`, `src/cli.rs`; RTE-1, RTE-5, RTE-7, RTE-8.

Delivery is target-side wired. Host compliance, retrieval benefit and improved future capacity remain uninspected. Git history makes earlier versions available; it does not itself prove a later host reads or uses them. Evaluation RTE-11 returns rubric comparisons without a retained policy-update route. Its definitions establish neither observed quality nor causal improvement. Supplied RTE-11; SRC-1: `src/evaluation.rs`, `src/cli.rs`.

## Comparison rationale

Repo and files are both required because curated snapshots and raw/export/task files have separate persistence routes. Natural-language and symbolic are both required because retained access state has force independently of statements. Ranking describes retained text's effect under fixed lexical code, not learned ranker policy. Learning authority describes journal text consumed to produce durable context, while trace_learning describes that automatic write route. Neither asserts demonstrated improved capacity.

Event-streams is supported specifically by calendar/voice content consumed as Note candidates, not merely by journal serialization. Static project files add imported lineage without adding a trace source. Tool-role traces are retrieved but excluded from inspected extraction. Coarse/identifier/lexical push signals do not import judgment or embedding signals from the model-reranked pull path. Curation coverage is partial because model-generated content cannot establish a complete operation taxonomy; inspected deterministic witnesses remain positive.

## Integration issues

1. OBJ-1 combines facts, controls, checkpoint, dispositions and index/receipts with different consumers and forces. Canonical splitting would preserve fact knowledge/instruction, ranking inputs, control vetoes and checkpoint routing separately. This report annotates those parts without redeclaring their identity. Evidence: SRC-1 `src/consolidate.rs`, `src/search/lexical.rs`, `src/change.rs`; concerns OBJ-1, RTE-1, RTE-3.
2. OBJ-3 and RTE-8 combine static setup with derived exports. Only the derived content belongs to accumulated memory. Reconciliation should preserve that scope distinction, and replace “current active” export with its enum-status/visibility predicate. Writeback omits Superseded/Retracted/Expired status but does not call temporal eligibility, exclude Disputed, or consult controls. Evidence: retained writeback passage, SRC-1 `src/cli.rs`, `src/fact.rs`; concerns OBJ-3, RTE-8, RTE-1.
3. RTE-1's stated lack of TTL applies to ordinary producers, not all library-created facts. Temporal Fact eligibility is wired; supplied public Fact/change APIs permit populated expiry/validity fields. This correction supports conditional decay without claiming every consumer applies it. Evidence: retained expiry passage; SRC-1 `src/lib.rs`, `src/change.rs`, `src/fact.rs`; concerns RTE-1, RTE-2, OBJ-1.
4. RTE-10's local transcript/file summary also covers calendar/voice Note adapters. Those original contents feed RTE-3's Note branch and add event-streams to the memory profile. Tool-role IDE inputs do not add tool-traces to that learning route. Evidence: retained calendar/voice/role passages; SRC-1 `src/ingest.rs`, `src/consolidate.rs`; concerns RTE-10, RTE-3, OBJ-2.
5. Opaque model semantic choices prevent complete curation-operation coverage and faithfulness/benefit conclusions. This does not block the supported consolidation, dedup, evolution, invalidation and conditional decay findings. SRC-1 `src/consolidate.rs`; concerns CMP-1, RTE-3. No new declarations duplicate seeded records; all overlap uses annotations.

## Limitations and checks

No target code, tests, examples or provider calls were executed. No observed retention/retrieval trace, model reply, successful recovery, host uptake or causal comparison was supplied. These limits prevent demonstrated reliability, improved capacity, complete semantic curation coverage and dependency-internal conclusions. Reranker weights/configuration are excluded machinery rather than scoped learned memory. Source identity recheck: HEAD equalled 6acb13dc35765bf5ccfc87e445dd09c480f1c28a, origin equalled https://github.com/jasonkneen/instinctual-memory and git status --porcelain was empty. All direct source reads remained inside the registered checkout. Quotes were generated through commonplace-quote against the supplied run-state; no manual attribution was used.

Validation result: commonplace-validate --full on this report passed cleanly (exit 0), with thirteen well-formed quotation attributions, resolved declared/annotated comparison references, and no warnings or failures. Code's acceptance record remains authoritative for structural acceptance.
