---
type: "agentic-systems/types/agent-memory-analysis-report.md"
description: "Memory mechanisms of instinctual-memory: journal-to-fact extraction, Git controls, requested retrieval, host hooks and instruction writeback"
run-id: "AAS-2026-10-01-instinctual-memory-07"
source-identity: "https://github.com/jasonkneen/instinctual-memory"
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
report-status: "complete"
memory-comparison: {"scope": "Accumulated journal events, sourced entity facts and their structured metadata, suppression/deletion controls, generated index/entity renderings, task titles/version, and generated project-memory blocks; includes acquisition, curation and later read routes. Excludes static shipped skills/prompts, unchanged model weights/cache selection, ordinary HTTP result maps, publisher receipts/intents and consolidation progress as runtime control state, and external host/provider internals.", "axes": {"storage_substrate": {"assessment": "known", "values": ["files", "repo"], "evidence": {"files": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "MEM-OBJ-1"], "note": "Journal JSONL, task JSON and generated Markdown persist in local files."}, "repo": {"basis": "wired", "records": ["OBJ-1", "RTE-3", "RTE-4"], "note": "Entity facts, controls and index are versioned in bare Git memory.git."}}, "records": ["OBJ-1", "OBJ-2", "MEM-OBJ-1", "RTE-3", "RTE-4"], "note": "All scoped durable surfaces are local files or Git snapshots; model caches and provider weights are excluded because use does not train them."}, "representational_form": {"assessment": "known", "values": ["natural-language", "symbolic"], "evidence": {"natural-language": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "MEM-OBJ-1"], "note": "Statements, transcript content, task titles and rendered memory are readable prose."}, "symbolic": {"basis": "wired", "records": ["OBJ-1", "OBJ-2"], "note": "IDs, predicates, source references, status, controls and task versions are structured records."}}, "records": ["OBJ-1", "OBJ-2", "MEM-OBJ-1"], "note": "The actual fact payload combines structured YAML with prose, rather than a hidden semantic representation; no learned parameters are scoped."}, "lineage": {"assessment": "known", "values": ["authored", "imported", "other-compiled", "trace-extracted"], "evidence": {"authored": {"basis": "wired", "records": ["RTE-3", "RTE-8"], "note": "Explicit callers author remembered statements and task titles."}, "imported": {"basis": "wired", "records": ["MEM-RTE-1", "OBJ-1"], "note": "Adapters import external session text and memory files into the journal."}, "other-compiled": {"basis": "wired", "records": ["MEM-OBJ-1", "OBJ-1", "RTE-6"], "note": "Index rows, entity bodies and writeback blocks are deterministic projections of retained records."}, "trace-extracted": {"basis": "wired", "records": ["RTE-4", "RTE-5"], "note": "Rules/model extraction turns user session messages into sourced fact statements."}}, "records": ["RTE-3", "RTE-8", "MEM-RTE-1", "OBJ-1", "MEM-OBJ-1", "RTE-6", "RTE-4", "RTE-5"], "note": "File-derived facts additionally inherit imported source material. Static shipped skills are excluded from retained-memory lineage."}, "behavioral_authority": {"assessment": "known", "values": ["enforcement", "instruction", "knowledge"], "evidence": {"enforcement": {"basis": "wired", "records": ["OBJ-1", "RTE-3", "RTE-4", "RTE-9"], "note": "Retained suppression/deletion controls veto retrieval and re-admission of matching fact IDs."}, "instruction": {"basis": "wired", "records": ["RTE-5", "RTE-6"], "note": "Retained standing preferences/rules are emitted as host guidance or project instructions."}, "knowledge": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-8"], "note": "Requested facts, source events and tasks supply advisory information to the caller."}}, "records": ["OBJ-1", "RTE-3", "RTE-4", "RTE-9", "RTE-5", "RTE-6", "RTE-1", "RTE-2", "RTE-8"], "note": "Enforcement belongs to local controls, not to compliance with prose. Ranking uses fixed/model algorithms rather than retained learned ranking policy; activation by excluded host models is uninspected."}, "write_agency": {"assessment": "known", "values": ["automatic", "manual"], "evidence": {"automatic": {"basis": "wired", "records": ["MEM-RTE-1", "RTE-4", "RTE-5"], "note": "Adapters and extractors perform writes computationally, including host-end background sync."}, "manual": {"basis": "wired", "records": ["RTE-3", "RTE-8", "RTE-9"], "note": "Open explicit remember/correct/forget/task/maintenance requests supply content or choose admission."}}, "records": ["MEM-RTE-1", "RTE-4", "RTE-5", "RTE-3", "RTE-8", "RTE-9"], "note": "A human-triggered extraction remains automatic; an explicit content-authoring request is manual at this interface boundary."}, "curation_operations": {"assessment": "known", "values": ["consolidate", "dedup", "evolve", "invalidate", "decay"], "evidence": {"consolidate": {"basis": "wired", "records": ["RTE-4"], "note": "Retained events are reduced to durable sourced statements; original journal content remains independently available."}, "dedup": {"basis": "wired", "records": ["RTE-4", "RTE-9"], "note": "Near-duplicate proposals are rejected and tidy suppresses duplicate retained facts."}, "evolve": {"basis": "wired", "records": ["RTE-3"], "note": "Correct revises retained entity knowledge through supersession and replacement; same-ID upsert replaces entries."}, "invalidate": {"basis": "wired", "records": ["RTE-3", "RTE-4", "RTE-9"], "note": "Forget, tidy and changed-file retirement withdraw current reliance while preserving history for soft changes."}, "decay": {"basis": "wired", "records": ["RTE-1"], "note": "Temporal eligibility forgets expired or ended facts from current search context without deleting stored history."}}, "records": ["RTE-4", "RTE-9", "RTE-3", "RTE-1"], "note": "No semantic novelty is required by consolidation. Temporal decay is a read-time exclusion over populated metadata, not a background aging writer; default extraction leaves expiry empty. Hard erasure is described separately rather than equated with history-retaining invalidation."}, "read_back_direction": {"assessment": "known", "values": ["pull", "push"], "evidence": {"pull": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-8"], "note": "Search/read/history/tasks_read fulfill explicit requests for accumulated material."}, "push": {"basis": "wired", "records": ["RTE-5"], "note": "Host start and prompt hooks automatically supply selected accumulated preferences/facts."}}, "records": ["RTE-1", "RTE-2", "RTE-8", "RTE-5"], "note": "Writeback is an explicit projection write followed by an afforded host read; hook callbacks provide the direct automatic-supply witnesses."}, "read_back_signal": {"assessment": "known", "values": ["coarse", "identifier", "inferred-lexical"], "evidence": {"coarse": {"basis": "wired", "records": ["RTE-5"], "note": "Session start gates on any active fact and clips selected preference statements to twenty."}, "identifier": {"basis": "wired", "records": ["RTE-5"], "note": "Session start actually matches the pref_user entity ID and supplies its current fact statements."}, "inferred-lexical": {"basis": "wired", "records": ["RTE-5"], "note": "Prompt submission selects lexical matches with meaningful-word overlap and a six-fact budget."}}, "records": ["RTE-5"], "note": "Ordinary pull reranking can use inferred model judgment, but the push hooks disable reranking; no embedding or model-judged push selector is wired."}, "trace_learning": {"assessment": "known", "values": ["yes"], "evidence": {"yes": {"basis": "wired", "records": ["RTE-4", "RTE-5"], "note": "Session-log user words automatically become durable facts that later hooks/read tools deliver as context/guidance."}}, "records": ["RTE-4", "RTE-5"], "note": "This is trace-fed artifact production, not demonstrated capacity improvement or parameter learning. Raw log storage alone is not the witness."}, "trace_source": {"assessment": "known", "values": ["session-logs"], "evidence": {"session-logs": {"basis": "wired", "records": ["MEM-RTE-1", "RTE-4"], "note": "Claude/Codex/OpenCode session messages supply user-role source events for durable extraction."}}, "records": ["MEM-RTE-1", "RTE-4"], "note": "Tool/assistant/system events are excluded by the qualifying extraction branches; imported project files/calendar/VTT notes are other source material, not evidence of a separate agent tool-trace learning path."}}}
---

# instinctual-memory memory report

## Boundary and evidence

The boundary is the `mem` product at SRC-1/SRC-2 commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`. Direct inspection covered the paths below. Runtime findings seed record identity but are checked against implementation; no source tests or target services were executed. SRC-3's attributed recorded-search snippets provide reported operation, not observed pass results or causal benefit. Enclosing agents and model/provider internals are excluded. Memory scope is the accumulated objects and routes stated in the profile; protocol receipts, checkpoint positions and static prompts are discussed only where they constrain those routes.

| Entry point or memory operation | Directly inspected source paths | Covering IDs or exclusion |
|---|---|---|
| CLI dispatch and general/local/all backfill, ingest | SRC-1 `src/cli.rs`, `src/ingest.rs`, `src/journal.rs` | MEM-RTE-1, OBJ-1; supplied runtime had downstream consolidation but no separate acquisition route |
| Remember/correct/forget and retained controls | SRC-1 `src/change.rs`, `src/entity.rs`, `src/controls.rs`, `src/ops.rs` | RTE-3, OBJ-1 |
| Rules/LLM extraction, quarantine, checkpoint and changed-file retirement | SRC-1 `src/consolidate.rs` | RTE-4; checkpoint/dispositions are runtime-control context, not an extra memory payload |
| Requested combined search and fact eligibility | SRC-1 `src/ops.rs`, `src/search/mod.rs`, `src/search/lexical.rs`, `src/fact.rs`; supplied runtime model-fallback account | RTE-1; model weights excluded from accumulated memory |
| Fact/entity/event read and history | SRC-1 `src/ops.rs` | RTE-2 |
| Host start/prompt/end/sync | SRC-1 `src/hook.rs`, `src/cli.rs` | RTE-5, BAP-1 |
| Generated project instructions and index | SRC-1 `src/cli.rs`, `src/index.rs` | RTE-6, MEM-OBJ-1, OBJ-1, BAP-2 |
| Versioned tasks | SRC-1 `src/ops.rs` | OBJ-2, RTE-8 |
| Tidy/erase, rejection and withdrawal | SRC-1 `src/tidy.rs`, `src/erasure.rs`, `src/change.rs` | RTE-9, RTE-3 |
| MCP tool registration and shared operation dispatch; shell and HTTP | SRC-1 `src/mcp.rs`, `src/ops.rs`, `src/shell.rs`, `src/http_serve.rs`; supplied runtime interface account | RTE-1, RTE-2, RTE-3, RTE-8; no separate curation path in registered shared operations |
| Evaluate/bench/model setup/initialization | SRC-1 `src/cli.rs`; supplied runtime RTE-7, RTE-10 | Excluded as measurement/configuration/static scaffolding: no retained trace-fed learned ranking policy is established |

## Core ideas

The journal and curated facts remain separate. Retrieval can return raw event excerpts beside sourced statements, so automatic consolidation does not monopolize what the agent can recall. The curated store is a pinned Git tree of structured facts; the journal is an independently governed file store. Provenance carries event IDs and short evidence quotes, not model deliberation. These are operative source references rather than a proof that the paraphrase is true (OBJ-1, RTE-1, RTE-4; SRC-1 `src/journal.rs`, `src/consolidate.rs`, `src/ops.rs`).

Automatic supply has two selectors. Start selects the exact preference entity, with a twenty-statement cap and a coarse any-active-fact gate. Prompt supply uses lexical relevance plus one or two meaningful shared terms, and emits at most six statements. It performs no semantic reranking. User-requested search may rerank facts and journal excerpts with the remote/local models, but that optional pull branch does not change the push-signal classification (RTE-1, RTE-5; SRC-1 `src/hook.rs`, `src/ops.rs`).

Trust and withdrawal differ by consumer. Extraction filters user/note roles and requires source passage occurrence on the LLM branch. Search applies controls and temporal eligibility; direct entity read uses active status after suppression/deletion filtering. Writeback uses its own narrower status exclusions and does not load controls or check time metadata. A prior generated instruction block also persists after the underlying fact changes. Therefore store withdrawal does not imply immediate withdrawal from every delivery path or external file copy (RTE-2, RTE-3, RTE-6, RTE-9; SRC-1 `src/ops.rs`, `src/cli.rs`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-1 — Generated project-memory block

Source-native identity: generated block delimited by `mem:begin`/`mem:end` in AGENTS.md or an explicit destination. Storage substrate: files. Representational form: natural-language statements plus symbolic fact IDs and generation metadata. Lineage: other-compiled from stored facts, preserving statements rather than creating new claims. Consumers: enclosing hosts that load the target as project instructions; behavioral authority: instruction when loaded under that host contract, otherwise advisory knowledge. Persistence: across sessions until another writeback or exterior file edit. No automatic retraction or refresh propagates from memory.git. Implementation conclusion status: wired for projection persistence; host-consumption conclusion status: afforded; activation conclusion status: uninspected. Evidence: SRC-1 `src/cli.rs`, supplied RTE-6/BAP-2 quotation. Closest supplied object is OBJ-1; distinct identity is a separately written external projection, not the canonical Git store. No new record duplicates RTE-6.

### Routes

#### MEM-RTE-1 — Adapter acquisition into the journal

Endpoints/progression: explicit ingest/backfill/local/all or hook sync → selected source files → format adapter → Journal/BulkWriter append. Owner: CLI and adapters; selector is explicit paths or discovered host transcript/project-memory roots. Input: external session messages, Markdown memory files and supported chat/calendar/VTT sources. Retained output: source events with role/content, stable source/event identity, metadata and sequence in OBJ-1's journal files. Immediate return: imported/skipped counters, plan for dry run, or error. Later read-back: RTE-1/RTE-2 raw event recall and RTE-4 automatic fact extraction; RTE-5 can deliver resulting facts in later sessions. Delegated visibility: shared-store readers, with no separately wired delegated-agent propagation. Selection predicate: adapter format and source inventory; Codex subagent rollouts are excluded by its adapter, and assistant final-channel filtering prevents importing intermediate assistant text from those logs. Invalidation/expiry: no acquisition expiry; erasure redacts selected source-event content, original external files remain excluded. Effect: durable imported event write; activation by host models uninspected. Implementation conclusion status: wired; operation conclusion status: uninspected. Guarantee strength: best effort for a multi-file backfill that can report skipped sources. Evidence: SRC-1 `src/cli.rs`, `src/ingest.rs`, `src/journal.rs`. Closest supplied RTE-4 consumes this output and RTE-5 invokes backfill; neither is the adapter acquisition route itself. Acquisition is imported lineage and automatic write agency, even when manually initiated. It alone is not trace learning: that requires RTE-4 and later consumption.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On OBJ-1 — Memory content and access controls

Memory-specific parts are raw journal text, derived facts with evidence references, generated entity bodies/index, and suppression/deletion controls. Substrates are files for JSONL and repo for Git content. Forms combine natural-language text and symbolic metadata. Lineage is imported raw source material, authored explicit facts, trace-extracted session facts, and other-compiled body/index renderings. Controls are durable accumulated maintenance decisions enforcing current reliance and re-admission; reasons are retained strings, while predicates normally inspect IDs. Raw journal remains separately searchable and is not covered by fact-only forget. The body is a readable rendering of active statuses; the actual consumed facts reside in YAML, so display alone cannot establish temporal eligibility or control enforcement. Generated index rows count active status rather than all search gates. Consumers are RTE-1, RTE-2, RTE-4, RTE-5 and RTE-6; memory content is advisory knowledge or emitted instructions, controls have enforcement force. Evidence: SRC-1 `src/fact.rs`, `src/journal.rs`, `src/entity.rs`, `src/index.rs`, `src/controls.rs`, `src/ops.rs`.

> pub struct Fact {
>     pub id: String,
>     pub predicate: String,
>     pub statement: String,
>     pub kind: FactKind,
>     pub status: FactStatus,
>     pub observed_at: DateTime<Utc>,
>     #[serde(skip_serializing_if = "Option::is_none")]
>     pub valid_from: Option<DateTime<Utc>>,
>     #[serde(skip_serializing_if = "Option::is_none")]
>     pub valid_from_precision: Option<DatePrecision>,
>     #[serde(skip_serializing_if = "Option::is_none")]
>     pub valid_to: Option<DateTime<Utc>>,
>     #[serde(skip_serializing_if = "Option::is_none")]
>     pub expires_at: Option<DateTime<Utc>>,
>     #[serde(skip_serializing_if = "Option::is_none")]
>     pub review_after: Option<DateTime<Utc>>,
>     #[serde(default, skip_serializing_if = "Vec::is_empty")]
>     pub supersedes: Vec<String>,
>     #[serde(default)]
>     pub sources: Vec<SourceRef>,
>     pub visibility: Visibility,
> --- `src/fact.rs:13-34` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> pub schema_version: u32,
>     pub event_id: String,
>     pub seq: u64,
>     pub scope_id: String,
>     pub session_id: String,
>     pub occurred_at: DateTime<Utc>,
>     pub ingested_at: DateTime<Utc>,
>     pub role: Role,
>     pub source: Source,
>     pub content: String,
>     pub content_sha256: String,
>     pub redaction: Redaction,
>     #[serde(default)]
> --- `src/journal.rs:58-70` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> let active = entity.facts.iter().filter(|f| f.status == FactStatus::Active).count();
>         let row = format!(
>             "- `{}` ({}) {} — {active} active fact{}\n",
>             entity.id,
>             entity.entity_type,
>             entity.title,
>             if active == 1 { "" } else { "s" }
>         );
>         if body.len() + row.len() > INDEX_MD_BUDGET {
>             break;
>         }
> --- `src/index.rs:31-41` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On OBJ-2 — Retained task content

Substrate: files (`tasks.json`). Forms: natural-language title and symbolic ID/version. Lineage/write agency: authored/manual explicit task request; no automatic trace-fed transformation. Consumer: later `tasks_read` returns all saved tasks as advisory knowledge; no task execution is established. Persistence crosses requests/sessions on the selected store, with no inspected expiry. Evidence: SRC-1 `src/ops.rs`; RTE-8.

#### On RTE-1 — Requested recall and temporal downweighting

Read-back direction: pull. Retained selection is eligible fact prose and raw journal excerpts. Later consumers are the requesting agent/human via CLI/MCP/HTTP/shell. Facts use stemmed/weighted lexical terms over statements, titles and aliases, capped before project/source filtering; journal scanning is a distinct branch and no fact-ID suppression blanket is applied to raw event recall. Optional reranking and result limits refine the requested return. Read-back conclusion status: wired; activation conclusion status: uninspected. Stored expiry/valid-to dates automatically exclude facts from later search, classified as decay by omission from current context; stored history is retained. Default extractors create no such dates, so the branch needs populated metadata, available through fact payloads/library calls. Evidence: SRC-1 `src/ops.rs`, `src/search/lexical.rs`, `src/fact.rs`; supplied RTE-1 passages support reranking and filter order.

> if let Some(expires) = self.expires_at {
>             if expires <= now {
>                 return false;
>             }
>         }
>         if let Some(to) = self.valid_to {
>             if to <= now {
>                 return false;
>             }
>         }
>         if let Some(from) = self.valid_from {
>             if from > now {
>                 return false;
>             }
> --- `src/fact.rs:73-86` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-2 — Direct reads are not the search predicate

Read-back direction: pull; channel: requested JSON/text. Entity read supplies active-status fact statements; exact fact read can return status-labeled non-current material; history returns status records from the current entity, rather than replaying every Git revision. All use `find_fact`, which excludes suppressed/deleted facts, but does not call `Fact::is_eligible`, enforce entity/fact audience, or apply the retractions set independently. Thus an active fact with elapsed expires_at can be called current by entity read while search excludes it. Journal IDs bypass fact controls and return current event content. Persistence is that of the underlying store; immediate response not retained by this route. Read-back conclusion status: wired; activation conclusion status: uninspected. Evidence: SRC-1 `src/ops.rs`.

> let facts: Vec<Value> = found
>                     .facts
>                     .iter()
>                     .filter(|fact| fact.status == FactStatus::Active)
>                     .map(|fact| json!({"id": fact.id, "statement": fact.statement}))
>                     .collect();
>                 ok(json!({
>                     "id": id,
>                     "statement": current.statement,
>                     "label": "current",
>                     "fact_id": current.id,
> --- `src/ops.rs:270-280` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-3 — Authored revision and history-preserving withdrawal

Manual authored statements pass structural admission, not an independent truth test. Correction evolves an entity's retained knowledge with supersession/upsert; remember with an existing ID also overwrites that fact payload. Forget retains suppression/retraction decisions and reason, excludes fact lookup/search and blocks matching extraction IDs; original journal events remain searchable. Later read-back consumers are the same recalled fact routes and host supply. Evidence: SRC-1 `src/change.rs`, `src/entity.rs`, `src/ops.rs`; supplied RTE-3 publication/replay limits remain material. Reasons can persist in controls but ordinary context results do not expose a full criticism/adoption rationale. No demonstrated improved capacity follows.

> entity.supersede(&old_id, &new_fact.id)?;
>             entity.upsert_fact(new_fact.clone());
>             (entity, None, None)
> --- `src/change.rs:127-129` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-4 — Automatic sourced extraction and curation

Write agency: automatic. Trace-learning conclusion status: wired for session-log user words becoming fact statements delivered later by RTE-1/RTE-2/RTE-5/RTE-6. Other note-role inputs are imported material rather than agent tool-trace learning. The LLM accepts Note/User candidates, removes recognized harness text, chunks memory files and clips user text; rules accept User only. Assistant/tool/system content is excluded in those extraction branches. Source facts retain evidence quotes/event IDs, not model reasoning. Derived statements are trace-extracted for session messages; index/body are other-compiled. Curation operations: consolidate durable statements from retained raw material; dedup near-overlap proposals; invalidate outdated solely file-derived facts through Superseded status. Later extraction reads existing fact statements to avoid restating them. Progress checkpoints select unseen events and outcomes are stored in dispositions, but outcome logging alone does not revise the extraction policy. Evidence: SRC-1 `src/consolidate.rs`, supplied RTE-4 admission quote and roles.

> Role::Note => Some(event.content.clone()),
>             Role::User => user_words(&event.content),
>             _ => {
>                 ex.quarantined.insert(event.seq, "not a user statement or memory file".into());
>                 continue;
>             }
>         };
>         match text.filter(|t| !t.trim().is_empty()) {
>             // A memory file is read whole, in paragraph-aligned chunks, so a
>             // long AGENTS.md is not cut off at the first few kilobytes.
>             Some(text) if event.role == Role::Note => {
>                 for chunk in chunks(&text, NOTE_EVENT_CHARS) {
>                     candidates.push((event, chunk));
> --- `src/consolidate.rs:635-647` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> fn restates_existing(&self, p: &Proposal, fact_id: &str) -> bool {
>         let words = content_words(&p.statement);
>         if words.is_empty() {
>             return false;
>         }
>         // The same rule often lands on both the project and the user's
>         // preferences. Check both sides, whichever was stored first. Two
>         // different projects are not compared with each other.
>         let family = |base: &str, id: &str| {
>             id == base || id.strip_prefix(base).and_then(|r| r.strip_prefix('_')).is_some_and(|n| n.parse::<u32>().is_ok())
>         };
>         let proposal_is_pref = family("pref_user", &p.entity_id);
>         self.entities
>             .iter()
>             .filter(|(id, _)| {
>                 family(&p.entity_id, id)
>                     || family("pref_user", id)
>                     || (proposal_is_pref && id.starts_with("w_"))
>             })
>             .flat_map(|(_, e)| e.facts.iter())
>             .filter(|f| f.status == FactStatus::Active && f.id != fact_id)
>             .any(|f| {
>                 let other = content_words(&f.statement);
>                 jaccard(&words, &other) >= NEAR_DUPLICATE || contained(&words, &other)
>             })
>     }
> --- `src/consolidate.rs:420-445` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> && fact.sources.iter().all(|s| {
>                     versions
>                         .iter()
>                         .any(|(prefix, current)| s.event_id.starts_with(prefix) && &s.event_id != current)
>                 });
>             if outdated {
>                 fact.status = FactStatus::Superseded;
> --- `src/consolidate.rs:237-243` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Faithfulness is limited independently of the quote-occurrence check. The deterministic preference regex captures the instruction body after `always`, `never` or `don't`; its statement renders only that capture. Therefore `please never use tabs` yields `User requested: use tabs` while evidence retains the original negative wording. This is a source-inspected defective transformation, not novel-claim synthesis. The same shared content-word stoplist drops `not`, `no`, `never`, so near-duplicate checks can treat opposite assertions as equivalent when their remaining words agree. Both limit preservation of instructions; neither was executed here. Evidence: SRC-1 `src/consolidate.rs`.

> let pref_re = Regex::new(r"(?i)please (?:always|never|don't)\s+([a-z][^.!?]+)").unwrap();
> --- `src/consolidate.rs:286-286` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> found.push(Proposal {
>                 entity_id: "pref_user".into(),
>                 entity_type: "preference".into(),
>                 title: "User preferences".into(),
>                 predicate: "comms_preference".into(),
>                 statement: format!("User requested: {}", cap[1].trim()),
>                 evidence: cap[0].to_string(),
>             });
>         }
> --- `src/consolidate.rs:319-327` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> /// Word-overlap ratio at which two statements count as the same fact.
> pub(crate) const NEAR_DUPLICATE: f64 = 0.6;
>
> const STOPWORDS: &[&str] = &[
>     "a", "an", "the", "is", "are", "be", "to", "of", "in", "on", "for", "and", "or", "with",
>     "that", "this", "it", "its", "as", "by", "at", "from", "has", "have", "uses", "use",
>     "project", "user", "includes", "include", "consists", "assistant", "agent", "must", "always",
>     "should", "only", "when", "not", "no", "never", "do", "does", "wants", "want", "prefers",
> --- `src/consolidate.rs:448-455` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-5 — Automatic context delivery

Direction: push for start/prompt output. Start's trigger is SessionStart with nonzero active-fact count; it explicitly matches `pref_user` and takes at most twenty statements. The identity match selects the delivered retained part, so identifier is warranted independently of coarse availability/budget. Spill preferences such as `pref_user_2` are not selected by this exact entity read. Prompt trigger is UserPromptSubmit, excluding slash commands and fewer than three words; selector input is first 600 prompt characters, lexical facts-only search with project predicate, then meaningful-word overlap. It supplies at most six statements in JSON additionalContext as advisory knowledge/standing instructions. No embedding/judgment push is wired. Budget is count/character based, not token accounting. Direct-start read inherits RTE-2's time/visibility limits. End callback's detached sync produces memory through MEM-RTE-1/RTE-4; errors and child statuses do not prove completion. Read-back implementation conclusion status: wired; activation conclusion status: uninspected. Evidence: SRC-1 `src/hook.rs`, supplied RTE-5 quotation.

> }
>     let read = crate::ops::execute(root, "personal", "default", "memory_read", &json!({"id": "pref_user"}));
>     let prefs: Vec<String> = read.payload["facts"]
>         .as_array()
>         .map(|a| a.iter().filter_map(|f| f["statement"].as_str().map(str::to_string)).collect())
>         .unwrap_or_default();
> --- `src/hook.rs:89-94` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

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

#### On RTE-6 — Projection selection and delayed host use

Explicit writeback selects project family plus preferences, or all for local/explicit-all, excluding file-only derived facts by default. It rejects stored Superseded/Retracted/Expired statuses and checks fact visibility for a Private audience. It does not load Controls, enforce entity visibility, call temporal `is_eligible`, or exclude Disputed status. These differences prevent a uniform eligibility assertion across search and writeback. The written block is MEM-OBJ-1; any later host read is afforded by the project-instruction contract, with delivery/compliance unobserved. Requested writeback is not independently another automatic push; actual hook supply is the push witness. Persistence has no automatic link to subsequent correction/forget/erase. Evidence: SRC-1 `src/cli.rs`; supplied managed-block quote.

> for fact in &entity.facts {
>             if matches!(
>                 fact.status,
>                 crate::fact::FactStatus::Superseded
>                     | crate::fact::FactStatus::Retracted
>                     | crate::fact::FactStatus::Expired
>             ) {
>                 continue;
>             }
>             if !fact.visibility.allows(Visibility::Private) {
>                 continue;
>             }
>             // Facts that only restate AGENTS.md/CLAUDE.md/README.md are
>             // already in files agents read; writing them back duplicates them.
>             let from_files_only = !fact.sources.is_empty()
>                 && fact.sources.iter().all(|s| s.event_id.starts_with("evt_ide_md:"));
>             if from_files_only && !include_file_facts {
>                 continue;
>             }
>             active.push((fact.id.clone(), fact.statement.clone(), fact.visibility));
> --- `src/cli.rs:1782-1801` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-8 — Task return and persistence limitation

Direction: pull through explicit tasks_read. Selection returns saved list/version, with caller-authored titles delivered as advisory knowledge. Write agency: manual explicit update, computational version-checked append. Persistence is store-local JSON. The writer opens tasks.json with truncate, writes and syncs it; it does not replace via temporary file/rename. Locking serializes cooperating callers but a write failure can leave partial content. This corrects the supplied atomic-replacement assertion rather than changing its record identity. Read/write implementation conclusion status: wired; actual failure recovery and task execution uninspected. Evidence: SRC-1 `src/ops.rs`.

> fn write_tasks_file(root: &Path, file: &TaskFile) -> Result<()> {
>     std::fs::create_dir_all(root).map_err(|e| crate::error::Error::io(root, e))?;
>     let path = root.join("tasks.json");
>     let mut out = OpenOptions::new()
>         .create(true)
>         .write(true)
>         .truncate(true)
>         .open(&path)
>         .map_err(|e| crate::error::Error::io(&path, e))?;
>     let body = serde_json::to_string_pretty(file)?;
>     out.write_all(body.as_bytes())
>         .map_err(|e| crate::error::Error::io(&path, e))?;
>     out.sync_all().map_err(|e| crate::error::Error::io(&path, e))?;
>     Ok(())
> --- `src/ops.rs:716-729` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### On RTE-9 — Retained suppression versus erasure

Tidy's duplicate removal is dedup and history-retaining invalidate; optional model session-only judgment produces withdrawal candidates, not a source of new durable fact claims. Caller `--apply` admits them and `--keep` vetoes IDs; reasons name duplicate target or session-only classification in retained controls. Its consumer checks IDs, not the rationale's explanatory adequacy. Erasure separately deletes facts, redacts cited journal events, rewrites selected history and removes intents in successive fallible steps. Soft forget does not perform this erasure and cannot promise raw-source recall disappears. Source transcripts and prior writeback copies remain outside erasure's local reach. Implementation conclusion status: wired; observed completion/atomicity/benefit: uninspected. Evidence: SRC-1 `src/tidy.rs`, `src/erasure.rs`; supplied RTE-9 quotations.

## Write side

MEM-RTE-1 copies selected external text into raw journal events. RTE-4 transforms eligible user/note content into sourced standing statements and publishes entity changes together with generated index, dispositions and checkpoint. Automatic writes do not require manual review of each fact. The rules branch does not cover note files; the model branch treats notes as candidate memory-file text even though adapters also emit other note-role sources. Durability is a fixed policy/model judgment with occurrence and length checks, not verified long-term truth. Rejected events can be recorded as quarantined; checkpoint advancement means a later ordinary batch does not automatically retry those already passed events (SRC-1 `src/consolidate.rs`).

RTE-3 provides direct authored remember/correct/forget admission with intents and validated Git publication. RTE-9 tidy asks for withdrawal and retains reasons if applied; erasure removes more local source/history material but is not atomic across every effect. Recovery protocols cannot correct the source-faithfulness defects by themselves. File changes generate new source IDs on re-ingest; retirement checks sole support from older versions. Neither revision nor persisted reasons demonstrates a content-criticizing method-revision loop (SRC-1 `src/change.rs`, `src/consolidate.rs`, `src/tidy.rs`, `src/erasure.rs`; RTE-3, RTE-4, RTE-9).

## Read-back

RTE-1/RTE-2 return accumulated facts and events on request, and RTE-8 returns saved tasks. Optional source excerpts can expose the input passage behind a fact; raw-event recall is separately available. RTE-5 supplies preference/project statements automatically on later host callbacks. RTE-6 produces a durable project-file projection whose later host use is afforded; its updates require an explicit command. A supplied statement is available to the host, but no trace establishes behavior changed because of it or that it improved answers. External propagation to delegated agents is uninspected (SRC-1 `src/ops.rs`, `src/hook.rs`, `src/cli.rs`; RTE-1, RTE-2, RTE-5, RTE-6, RTE-8).

## Comparison rationale

Files and repo describe two independent retained substrates, not a vector/graph memory inferred from model-assisted ranking or entity links. Symbolic metadata and readable prose both survive in the actual payload. Imported source events, extracted session facts, caller-authored statements and compiled renderings have distinct derivation paths. Unchanged model parameters are processing components, not learned retained memory within this scope (OBJ-1, OBJ-2, MEM-OBJ-1, MEM-RTE-1).

The curation union combines source reduction, overlap-based suppression, authored revision, history-retaining withdrawal and time-based search exclusion. No synthesis or promotion is inferred from the name consolidate or the movement from raw journal to facts. The negative-rule loss is a faithfulness defect, not synthesis. The positive trace-learning value needs only the wired raw-session-to-derived-fact-to-later-context chain, independent of demonstrated learning in the stronger improved-capacity sense (RTE-1, RTE-3, RTE-4, RTE-5, RTE-9).

Identifier push is witnessed by the exact preference-entity lookup, while lexical push is witnessed by prompt-term selection. Requested ID reads alone would not justify identifier push. Model-judged reranking stays in the pull branch and does not add inferred-judgment to push signals. Instruction authority is emitted guidance at the host boundary; local controls enforce fact-ID exclusions, without enforcing the host's compliance with prose (RTE-2, RTE-5, RTE-6, OBJ-1).

## Integration issues

1. RTE-8 and OBJ-2: replace the supplied atomic-file-replacement/rename claim with locked truncate/write/sync. SRC-1 `src/ops.rs`, annotation RTE-8 quote proves the implementation differs. Locking and version checking remain; crash-safe replacement is not established.
2. RTE-6: qualify supplied eligible-status/visibility language. Writeback omits controls, entity visibility and time checks and permits Disputed status; SRC-1 `src/cli.rs` versus `src/search/lexical.rs`/`src/fact.rs`. This prevents all-delivery withdrawal/expiry guarantees, even though normal forget also sets Retracted status.
3. RTE-2/RTE-5: entity current reads mean Active status after suppression/deletion, not full search eligibility. Start reads only exact pref_user, leaving spill preference files out. SRC-1 `src/ops.rs`, `src/hook.rs`; consequences are stale temporal context and incomplete start preference supply.
4. RTE-4: retain the deterministic preference negation-loss and overlap stopword risk above. SRC-1 `src/consolidate.rs` supports source-inspected failures of faithfulness, without an executed outcome or synthesis classification.
5. OBJ-1 combines materially distinct parts: raw journal, sourced facts/renderings, and retained controls have different consumers and checks. The annotations assess them separately; reconciliation may canonically split them if needed. MEM-OBJ-1 is distinct from OBJ-1 because writeback produces a separately persisted exterior projection. MEM-RTE-1 is distinct from RTE-4 (acquisition versus extraction) and RTE-5 (adapter work versus host callbacks); no new declarations knowingly duplicate supplied records.
6. RTE-4/RTE-9: no run evidence resolves extraction accuracy, duplicate-rejection adequacy, model judgment reliability or improved future capacity. Those are limits on stronger conclusions, not completion blockers. External copies/hosts prevent a whole-environment forgetting or activation claim.

## Limitations and checks

Source identity recheck: checkout HEAD equals the frozen full commit and git status --porcelain is empty. The method instructions and supplied contracts were read; no other run, retained analysis or prior-review prose was consulted. No target executable, tests, example, provider or runtime fixture was run. Checked-in tests and reported snippets cannot attest passing execution. Structural self-validation is recorded below and is not workflow acceptance or independent integrated correctness. Host activation, demonstrated benefit, deployment/provider behavior and global deletion remain uninspected.

Validation: commonplace-validate --full on this report returned exit 0, Overall PASS (clean), with no warnings or failures. After recording this result, the final report was validated again.
