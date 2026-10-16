---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "beads_rust memory: issue state, inherited governing context, bounded MCP projections, local evaluation evidence and recovery history."
run-id: AAS-2026-10-16-beads-rust-e82d5506d2ff-01
source-identity: https://github.com/Dicklesworthstone/beads_rust
reviewed-boundary: 53f7a3d30aca8cab3c3e4abdefeade459e8a3089
---

# beads_rust memory report

## Boundary and evidence

The memory boundary is retained project work and the shipped paths that admit, revise, select and withdraw it. It includes SQLite issue state, JSONL transfer/reconstruction, ancestor instructions, local event and gate evidence, saved filters, instruction installation and recovery snapshots. It does not include an external host's conversation store, model parameters, context-compaction implementation or Agent Mail implementation. Those exclusions prevent conclusions about host instruction priority, actual recall, conversation eviction and compliance. The frozen source and evidence layers are SRC-1 in [boundary.md](boundary.md#source-register). HEAD was rechecked as `53f7a3d30aca8cab3c3e4abdefeade459e8a3089`.

The runtime findings are supplied implementation evidence, not observed execution. Direct source reads added `src/model/mod.rs`, `src/inheritance.rs`, inherited-context portions of create/update/show, MCP prompt/resource/tool projections and registration, deletion storage, export eligibility, history backup/restore, audit, gate, saved-query, scheduler and lint paths. Searches covered CLI dispatch, registered MCP endpoints, compaction hook references and interaction-log consumers. These are implementation reads except where documentation is explicitly identified. No target program or evaluator was run.

| Entry or memory operation | SRC-1 source path | Coverage and limits |
|---|---|---|
| CLI create, update/claim, close, JSONL import and no-db reconstruction | `src/main.rs`, `src/cli/commands/create.rs`, `src/cli/commands/update.rs`, `src/storage/sqlite.rs`, `src/sync/mod.rs` | Supplied [RT-RTE-create-issue](runtime.md#rt-rte-create-issue), [RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue), [RT-RTE-close-issue](runtime.md#rt-rte-close-issue), [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import); direct reads add distinct retained parts below. Not every mutation/retry audited. |
| Content, relations, context and lineage | `src/model/mod.rs`, `src/inheritance.rs` | [MEM-OBJ-issue](#mem-obj-issue), [MEM-OBJ-dependency](#mem-obj-dependency), [MEM-OBJ-agent-context](#mem-obj-agent-context); separate interpretation from fixed predicates. |
| Ready/list/search/show, saved query, scheduler and aggregate graph views | `src/cli/commands/ready.rs`, `src/cli/commands/search.rs`, `src/cli/commands/show.rs`, `src/cli/commands/query.rs`, `src/cli/commands/scheduler.rs`, `src/mcp/resources.rs` | Supplied ready route; direct show/query/scheduler reads and scoped search inventory: [MEM-RTE-state-read](#mem-rte-state-read), [MEM-RTE-saved-query](#mem-rte-saved-query). Search/list filter implementation and every graph/statistics projection remain incompletely inspected; no complete ranking-equivalence claim. |
| MCP seven tools, twelve resources, four prompts | `src/mcp/mod.rs`, `src/mcp/tools.rs`, `src/mcp/resources.rs`, `src/mcp/prompts.rs` | Registration checked against supplied routes. [MEM-RTE-state-read](#mem-rte-state-read), [MEM-RTE-guided-context](#mem-rte-guided-context); mutations use supplied [RT-RTE-mcp-request](runtime.md#rt-rte-mcp-request). No deployed host grant set supplied. |
| Opt-in ancestor re-delivery | `src/inheritance.rs`, `src/cli/commands/show.rs`, `src/cli/commands/update.rs` | [MEM-RTE-inherited-context](#mem-rte-inherited-context); show and text update differ. No host compaction hook is established by this feature. |
| Events, explicit interaction recording, labels and coordination evidence | `src/storage/sqlite.rs`, `src/cli/commands/audit.rs`, `src/mcp/resources.rs`, `docs/AGENT_INTEGRATION.md` | [MEM-OBJ-event](#mem-obj-event), [MEM-OBJ-audit-entry](#mem-obj-audit-entry), [MEM-RTE-audit-record](#mem-rte-audit-record). Interaction log inspection supports existence/label lookup, not a downstream learning consumer. |
| Gate results, closure evidence and quality review | `src/cli/commands/gate.rs`, `src/close_policy.rs`, `src/cli/commands/lint.rs`, `src/mcp/prompts.rs` | [MEM-OBJ-gate-result](#mem-obj-gate-result), [MEM-RTE-gate-report](#mem-rte-gate-report), guided context route and supplied closure route. Caller reports are not independent verification. |
| Delete/purge, export omissions, history restore/prune | `src/cli/commands/delete.rs`, `src/storage/sqlite.rs`, `src/sync/mod.rs`, `src/sync/history.rs`, `src/cli/commands/history.rs` | [MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal), [MEM-OBJ-history-backup](#mem-obj-history-backup). Doctor rebuild and WAL recovery are inventoried in boundary/runtime; detailed preservation/recovery branches remain uninspected, preventing universal losslessness claims. |
| Physical compaction and candidate recovery-family retention | `src/config/mod.rs`, `docs/COMPACTION_RETENTION.md`, `src/model/mod.rs` | [MEM-CLM-compaction-scope](#mem-clm-compaction-scope). Retention activation not established. Legacy issue compaction fields do not establish semantic summarization. |
| Shipped agent blurb, skill/plugin/installer and migration guidance | `src/cli/commands/agents.rs`, `.claude/skills/br/SKILL.md`, `skills/`, `install.sh` | Supplied [RT-OBJ-agent-blurb](runtime.md#rt-obj-agent-blurb), [RT-RTE-agents-update](runtime.md#rt-rte-agents-update), [RT-CLM-explicit-sync](runtime.md#rt-clm-explicit-sync). Other distribution/migration transformations are included but not audited here; cannot assert identical instructions or approval on every installation route. |
| Other local operational state | `src/storage/sqlite.rs`, `src/cli/commands/capacity.rs`, `src/cli/commands/coordination.rs`, `src/model/acceptance.rs` | Schema/API searches expose capacity occupancy/exemptions, acceptance items and auxiliary close state. Full initialization, revision, external-snapshot provenance and consumer selection for these parts remain uninspected. This prevents a complete local-policy/evidence roundtrip account, not the positive gate/context findings below. |
| Evaluators, self-use and build artifacts | `tests/`, `scripts/`, `benches/`, `fuzz/`, `.beads/`, `agent_baseline/` | Included by boundary; no fresh execution, corpus audit or performance evaluation. Test assertions and source-native claims cannot establish operational success. Excluded samples/coordination artifacts remain excluded as specified in boundary. |

## Core ideas

1. **The durable unit is a work item, not a conversation.** Descriptions, design, criteria, notes and comments can preserve reasons, while status, priority and dependencies supply software-readable work selection. They have different consumers and authority ([MEM-OBJ-issue](#mem-obj-issue), [MEM-OBJ-dependency](#mem-obj-dependency)). No admission route establishes the truth of authored prose merely by accepting it.
2. **A second retained surface is explicitly governing content.** Ancestor `agent_context` is re-selected when a child is shown or starts work. This is opt-in, bookend selection, not inheritance of every ancestor or an implementation of host compaction ([MEM-RTE-inherited-context](#mem-rte-inherited-context)).
3. **Context is projected before delivery.** MCP planning/quality/status prompts select issues and fields using fixed rules and row caps; they return guidance to an external model rather than invoking one. Quality labels can overstate what was checked ([MEM-RTE-guided-context](#mem-rte-guided-context)).
4. **Retention is not uniformly portable.** Issue JSONL carries relations and comments, whereas ordinary audit events and gate evidence are local; export excludes ephemeral/wisp material and expired tombstones. Backups preserve earlier bytes, not every intermediate edit. These countercases limit any claim that JSONL reproduces the entire memory ([MEM-OBJ-event](#mem-obj-event), [MEM-OBJ-gate-result](#mem-obj-gate-result), [MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-issue
Label: Issue content

Source-native identity: prose fields of `Issue` and associated `Comment` bodies. Natural-language representational form, within symbolic records in SQLite and exported JSONL; field names/IDs are not their semantics. Lineage is caller content from create/update/comment or upstream imported records; initial human/model authorship is unresolved. Design, acceptance criteria, prerequisites, notes and close reasons can retain rationale, but their presence and adequacy depend on authored content. Show and detail tools deliver it to later readers; compact ready/quality projections omit much of it. Distinct from the executable [RT-CMP-beads-rust](runtime.md#rt-cmp-beads-rust), and from the static [RT-OBJ-agent-blurb](runtime.md#rt-obj-agent-blurb). SRC-1: `src/model/mod.rs`, `src/mcp/tools.rs`, `src/cli/commands/show.rs`.

> /// Technical design notes.
> #[serde(default, skip_serializing_if = "Option::is_none")]
> pub design: Option<String>,
> --- `src/model/mod.rs`

#### MEM-OBJ-dependency
Label: Issue selection state and dependency relations

Source-native identity: issue status/priority/assignee/defer fields and typed dependency/label relations. Representational form: symbolic values with fixed query and admission consumers; substrate: SQLite rows and exportable JSONL relations. Caller proposals and import determine values, then storage maintains dirty markers/cache invalidation. Dependency and readiness consumers exclude work or order it; this is actual software selection authority, not authority to execute the described task. Events, export hashes and import witnesses are separate evidence/access metadata, not additional issue meaning. Closest supplied record is [RT-RTE-ready-query](runtime.md#rt-rte-ready-query), a consumer route rather than this retained object. SRC-1: `src/model/mod.rs`, `src/storage/sqlite.rs`, `src/sync/mod.rs`; readiness evidence passage supplied by that runtime record.

#### MEM-OBJ-agent-context
Label: Ancestor agent_context

Source-native identity: `Issue.agent_context`, an open-shaped JSON document stored as TEXT in SQLite and carried by issue serialization. Its governing instructions have natural-language force at the agent reader; JSON normalization is symbolic encoding, not an executable policy schema. Producer: create/update caller supplying inline JSON or a JSON/YAML file; empty argument clears the value. The CLI parser rejects invalid syntax but does not establish safe or correct instructions. Other library/import writers are not proven to enforce the same parser. Reasons persist only if the caller includes them. Distinct from project-file [RT-OBJ-agent-blurb](runtime.md#rt-obj-agent-blurb): this is mutable per-issue content selected by ancestry. SRC-1: `src/model/mod.rs`, `src/cli/commands/create.rs`, `src/cli/commands/update.rs`, `src/inheritance.rs`.

> /// Validation happens here because the storage column is opaque TEXT —
> /// without this guard we'd happily round-trip syntactically invalid
> /// JSON through SQLite and then have the emission path discover the
> /// problem at agent claim time. (beads_rust#297)
> --- `src/cli/commands/update.rs`

#### MEM-OBJ-event
Label: Mutation event trail

Source-native identity: `events` rows with actor, old/new values, timestamp and optional agent/harness/model attribution. Symbolic event encoding with possibly natural-language payloads; SQLite substrate. Mutation bookkeeping generates raw local traces, later displayed by audit log/summary, recent-events resource and show tool. These displays are derivations for a reader, not retained learned instructions. Existing import updates do not manufacture an equivalent event history. Events are not ordinary issue JSONL payloads. Distinct from supplied issue-admission routes, which generate or bypass this trace rather than denote it. SRC-1: `src/storage/sqlite.rs`, `src/storage/schema.rs`, `src/mcp/resources.rs`, `src/mcp/tools.rs`.

> // surface is unaffected (events are DB-only). Idempotent: ensure_columns
> --- `src/storage/schema.rs`

> /// transaction: import-path upserts never write events, so any change is
> --- `src/storage/sqlite.rs`

#### MEM-OBJ-audit-entry
Label: Interaction AuditEntry

Source-native identity: explicit `AuditEntry` records in `.beads/interactions.jsonl`, distinct from SQLite mutation events. Symbolic JSON envelope plus caller-supplied natural-language prompt, response, error, reason or evidence summary; content need not be a literal host trace. `audit record` accepts flags/JSON; `audit coordination` transforms supplied claim snapshots into bounded incident records and a source hash; `audit label` appends a child annotation with parent ID and optional reason. This preserves traces and review labels, not an automatically revised method. Later label admission scans the file for a parent ID; a semantic planning/learning reader is not established by inspected code. No counterpart after comparison with supplied runtime objects. SRC-1: `src/cli/commands/audit.rs`, `docs/AGENT_INTEGRATION.md`.

> fn interactions_file_path(beads_dir: &Path) -> PathBuf {
>     beads_dir.join("interactions.jsonl")
> }
> --- `src/cli/commands/audit.rs`

#### MEM-OBJ-gate-result
Label: Scoped gate result

Source-native identity: local gate result/history with issue, from/to statuses, status revision, gate, provider, verdict and note. Symbolic verdicts govern permitted transitions; natural-language notes can explain them. SQLite substrate; reports are caller-provided, not automatically evaluated test outputs. The provider string is attribution rather than authenticated competence. Later gate list and transition enforcement consume the results. Different from close reason/auxiliary bypass metadata in [RT-RTE-close-issue](runtime.md#rt-rte-close-issue); this is pre-transition retained evidence. SRC-1: `src/cli/commands/gate.rs`, `src/storage/sqlite.rs`, `src/close_policy.rs`.

> //! Gate results are auxiliary, project-local metadata (like `close_metadata`):
> //! they are not synced through JSONL. Enforcement at the close/transition
> //! chokepoint lives in `close_policy::evaluate_gates`, hooked from
> //! `commands::update` and `commands::close`.
> --- `src/cli/commands/gate.rs`

#### MEM-OBJ-saved-query
Label: SavedQuery

Source-native identity: named `SavedQuery`/`SavedFilters`, JSON serialized into config table keys prefixed `saved_query:`. Symbolic access metadata, not a snapshot of matching issues or a natural-language memory summary. Caller-supplied filters persist; later run merges invocation overrides and delegates to list. Description is readable metadata, not executed. Distinct from supplied ready route: retained query definitions choose subsequent reads. SRC-1: `src/cli/commands/query.rs`.

> /// Prefix for saved query keys in the config table.
> const QUERY_KEY_PREFIX: &str = "saved_query:";
> --- `src/cli/commands/query.rs`

#### MEM-OBJ-history-backup
Label: JSONL history backup

Source-native identity: timestamped export-source backup plus target/digest metadata under `.beads/.br_history`. Substrate: files; representation: copied serialized issue state, with symbolic sidecar evidence. Automatic pre-export copying can deduplicate/throttle/rotate by configuration; it is not semantic compression. Explicit pre-salvage backups instead retain rejected source bytes without ordinary rotation. Later diff/restore consumes bytes; no model reads backups automatically in the inspected route. Different from admitted state in [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import), although restore can supply its later input. SRC-1: `src/sync/history.rs`, `src/cli/commands/history.rs`.

> /// Preserve the exact source generation before an operator-authorized JSONL
> /// salvage. Unlike ordinary export history, this backup is never throttled,
> /// deduplicated, or rotated: rejected source bytes must remain recoverable.
> --- `src/sync/history.rs`

### Routes

#### MEM-RTE-inherited-context
Label: Ancestor instruction read-back

Caller show/start-work request → opt-in check → ancestor traversal → root/parent bookend blocks → CLI output → later agent reader. Code owns selection; caller chooses child and can edit/clear source instructions. SRC-1: `src/inheritance.rs`, `src/cli/commands/show.rs`, `src/cli/commands/update.rs`. This is an additional read-back path related to, not a duplicate of, [RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue).

- Immediate return: Child output enriched with ancestor source ID, role, title, field and content; text update prints blocks after its summary.
- Later read-back: Reads retained ancestor agent_context on a later child show or eligible in-progress transition.
- Delegated visibility: Invoking host/agent can receive the output; no worker launch or isolated context is created.
- Selection predicate: Opt-in environment/config, selected child's parent-child chain, immediate parent and root (preferring topmost epic); at most two blocks, root first, intermediate layers omitted. Missing/tombstoned/empty sources and cycles limit traversal.
- Invalidation or expiry: Source edits, clearing, ancestry changes or deletion change future selection; already emitted copies remain in the host until the host removes them.
- Activation or effect: Re-delivers instructions as reader input; compliance and restored behavior after compaction are unobserved.
- Evidence limits: CLI show JSON/TOON attaches blocks per issue; text show deduplicates shared sources. Update emission is in the non-JSON/non-TOON, non-quiet branch. No equivalent inherited delivery established for MCP detail tools.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Budget is a block-count bound, not a token/byte cap. Content remains in the store for another show even when omitted from a particular delivery. This is automatic enrichment of a requested operation, not independent unsolicited retrieval or a host eviction detector. Admission of the source text is covered by [MEM-OBJ-agent-context](#mem-obj-agent-context); downstream authority is [MEM-BAP-inherited-guidance](#mem-bap-inherited-guidance).

> //! v1 emits the **two bookends** of the ancestor chain — the immediate
> --- `src/inheritance.rs`

#### MEM-RTE-state-read
Label: State and trace retrieval

CLI/MCP request → storage query/detail load → projection/formatting → requesting reader. Selection owner is fixed software plus caller parameters; the reader chooses subsequent action. SRC-1: `src/cli/commands/show.rs`, `src/cli/commands/scheduler.rs`, `src/mcp/tools.rs`, `src/mcp/resources.rs`, `src/cli/commands/audit.rs`. Separate from supplied [RT-RTE-ready-query](runtime.md#rt-rte-ready-query): detail/history and ranked scheduler paths, not a second declaration of readiness.

- Immediate return: Issue text/relations/comments, selected events, audit summaries or ranked candidates depending on endpoint.
- Later read-back: Later invocations consume accumulated issues and events; derived display is not automatically persisted.
- Delegated visibility: CLI output or MCP result/resource reaches the requesting host; deployment/model choice uninspected.
- Selection predicate: Requested IDs or filters; show_issue loads detail with event limit 20 then emits at most 10 recent events; recent-events resource requests 50. Scheduler filters ready candidates with configured statuses, external blockers and candidate cap before fixed scoring using relation/domain/staleness inputs.
- Invalidation or expiry: Later state changes invalidate snapshots; retrieved lists reserve no work. Hard purge removes current-store content and its events.
- Activation or effect: Supplies evidence and candidate rankings; actual choice remains external. Stored status/dependency predicates directly affect selection.
- Evidence limits: No recall/precision measurement or exhaustive equivalence across CLI, MCP and direct JSONL paths. Issue resource loads details but projects no recent_events field, unlike show_issue.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This is requested read-back, not an embedding similarity service established by the inspected paths. Full prose remains reachable through detail reads even where selected candidate summaries omit it. MCP's optional read cache is access acceleration, not learned content; lifecycle/invalidation evidence is supplied in [RT-RTE-mcp-request](runtime.md#rt-rte-mcp-request).

> let events = storage.get_all_events(50).map_err(to_mcp)?;
> --- `src/mcp/resources.rs`

#### MEM-RTE-guided-context
Label: MCP planning and quality context

Host requests status_report/plan_next_work/polish_backlog → validate argument → read issue state → bounded symbolic analysis and projection → user-role data plus instruction messages. Code selects; external agent proposes changes; subsequent mutation handlers decide admission. No internal model call or independent answer oracle is shown. Open guided requests, not experiments. Distinct from supplied [RT-RTE-triage-prompt](runtime.md#rt-rte-triage-prompt), which covers the fourth registered prompt. SRC-1: `src/mcp/mod.rs`, `src/mcp/prompts.rs`.

- Immediate return: Two user-role messages containing current derived context and static guidance, not a completed status report, accepted plan or revised backlog.
- Later read-back: Re-reads accumulated issue state; generated recommendations are not persisted automatically. Caller must use update/dependency tools to retain changes.
- Delegated visibility: Messages reach requesting host/model, not a launched specialist.
- Selection predicate: Validated goal/focus/period; status fetches at most 50 in-progress/display 20, blocked display 10 and labels 10. Plan bottleneck fetch cap 10000/display 10, quick wins display 5, ready display 10. Polish completeness fetch 100/sample 10; dependency health fetch 500/orphan display 15.
- Invalidation or expiry: A fresh request recomputes from current state; old prompt text is not actively revoked in host context.
- Activation or effect: Fixed checks flag missing/short descriptions, default priorities and graph connectivity; guidance requests agent editing, not proof those edits occurred.
- Evidence limits: Counts and samples can be bounded, and priority/length are proxies, not semantic completeness. Status period changes instruction, not a historical event query in this handler. Planning's graph-analysis label does not establish optimization or PageRank execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Context budget is row counts, not tokens; no prompt truncation of long text by token budget is established. The quality prompt says to inspect full issues before adding descriptions and asks for background, approach, success criteria and test plans. That is an afforded human/model curation loop whose proposed edits can persist through existing mutations, not an automatic trace-to-method transformation. Source trust is inherited from issue authors/imports; presentation as user-role text does not authenticate those assertions.

> Some(d) if d.len() < 50 => short_description.push(issue),
> --- `src/mcp/prompts.rs`

> const COMPLETENESS_FETCH_LIMIT: usize = 100;
> const QUALITY_SAMPLE_LIMIT: usize = 10;
> --- `src/mcp/prompts.rs`

#### MEM-RTE-saved-query
Label: Saved filter read-back

Caller save → list-argument validation → serialized config write; later run → load/decode → CLI override merge → list query/output. Caller proposes and can delete then resave; software rejects invalid filters and existing-name conflicts. No content-truth oracle; open maintenance/retrieval operation. SRC-1: `src/cli/commands/query.rs`; no equivalent supplied record.

- Immediate return: Save/delete confirmation or current query results on run.
- Later read-back: Retained filter values select a new result set on later invocations, not replay of old results.
- Delegated visibility: Invoking reader receives normal list output.
- Selection predicate: Named config key; non-empty CLI vectors/options and true booleans override/merge saved values; retained limit/offset/sort apply unless overridden.
- Invalidation or expiry: Explicit delete/resave or config loss; matching issue population changes independently.
- Activation or effect: Deterministically reuses retained selection instructions in the list consumer.
- Evidence limits: Human approval/authorship unresolved; no portable JSONL preservation or semantic learning established. Recovery is explicit resave/config restoration, not an automatic versioned query history.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let merged_args = saved_query.filters.merge_with_cli(&args.filters);
> --- `src/cli/commands/query.rs`

#### MEM-RTE-audit-record
Label: Interaction recording and review labels

Explicit audit request or supplied coordination snapshot → parse/validate/normalize → append AuditEntry → optional later label lookup/append. Caller proposes content and labels; code rejects malformed input and nonexistent parent IDs. Human per-entry decision unresolved; no external correctness oracle. Open recording operation, not a training curriculum. SRC-1: `src/cli/commands/audit.rs`, `docs/AGENT_INTEGRATION.md`; distinct from mutation events in [MEM-OBJ-event](#mem-obj-event).

- Immediate return: Entry ID, incident IDs/count or appended label result.
- Later read-back: audit label scans retained interaction IDs to validate its parent. A later semantic consumer of recorded prompts/responses or incident evidence is uninspected.
- Delegated visibility: File can be inspected by operators; the documentation affords review and handoff use, not deployed host injection.
- Selection predicate: Caller record or JSON stdin; coordination snapshot claims yield one normalized incident each; label targets exact retained ID.
- Invalidation or expiry: Labels append rather than rewrite parent; manual edits/deletion possible outside this route. No automatic expiry in inspected append path.
- Activation or effect: Persists caller evidence and review annotations; does not automatically repair claims, change policy or learn instructions.
- Evidence limits: File retention is not proof of automatic host trace capture; downstream learning or complete trace fidelity not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Append writes and syncs the file; no automatic rollback of earlier entries in a partially completed multi-incident operation is established. The normalized incident result is derived evidence, but its later semantic consumer remains unresolved. The label's optional reason retains criticism only if supplied and meaningful, not merely because `label` exists.

> file.write_all(&line)?;
> file.sync_all()?;
> --- `src/cli/commands/audit.rs`

#### MEM-RTE-gate-report
Label: Evaluation evidence retention

Caller report → resolve issue/current revision/target → scoped gate result write → later list or guarded transition evaluation. Caller supplies verdict/provider/note; symbolic policy and storage decide admission and applicability. No authenticated test executor or independent answer oracle is established. Open evidence reporting, not autonomous evaluation. SRC-1: `src/cli/commands/gate.rs`, `src/storage/sqlite.rs`, `src/close_policy.rs`; related to [RT-RTE-close-issue](runtime.md#rt-rte-close-issue) but retaining earlier evidence is distinct from applying closure.

- Immediate return: Report record including scope/revision and verdict, or validation error.
- Later read-back: Gate list displays history; transition enforcement consumes effective scoped results for required gates.
- Delegated visibility: CLI report/list can reach agents and reviewers; no external reviewer is invoked by naming a provider.
- Selection predicate: Issue/from/to/status revision, gate/provider and policy; named gates require a pass, min-reviewers counts distinct reviewer providers. Current revision prevents indiscriminate reuse of old passes.
- Invalidation or expiry: Scope/status revision and newer verdicts affect applicability; history can remain as audit evidence. Purge removes local gate records.
- Activation or effect: Evidence changes admission decisions at software consumers; it is not only displayed knowledge. Explicit bypass and import paths limit universal gate guarantees as in supplied closure/import records.
- Evidence limits: Full gate initialization and all auxiliary-recovery branches uninspected; no claim that reported passes prove task success. Results do not ordinarily travel in issue JSONL.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Notes may preserve reasons, but the inspected gate predicate operates on provider/gate/pass values rather than interpreting note quality. Rejection retains reported history; subsequent reports can change effective evidence without rewriting issue prose.

> let passed = matches!(args.status, GateStatus::Pass);
> --- `src/cli/commands/gate.rs`

#### MEM-RTE-state-withdrawal
Label: Withdrawal and recovery selection

Caller deletion/purge, export retention or history restore/prune request → deterministic safety/eligibility checks → changed active state or recovery files → later query/import consumer. Caller chooses explicit destructive changes; code/config chooses automatic export omissions and backup rotation. Human per-content approval is unresolved. Open maintenance, no semantic truth oracle. SRC-1: `src/storage/sqlite.rs`, `src/sync/mod.rs`, `src/sync/history.rs`, `src/cli/commands/history.rs`, `src/cli/commands/delete.rs`.

- Immediate return: Tombstone/purge/restore/prune result or error; export can omit records without purging the database row.
- Later read-back: Tombstone state affects readiness and propagates through eligible exports; purge removes issue/relations/events from current store. History restore publishes saved JSONL bytes for a later import, not an immediate universal DB rollback.
- Delegated visibility: Cooperating workspace may consume exported deletion; already delivered host text and independent Git/backup copies are not revoked.
- Selection predicate: Explicit issue IDs or hard-delete tombstone collection; export excludes ephemeral=true, IDs containing -wisp-, expired tombstones. Backups use target identity, digest, throttle and configured rotation; restore validates target/source and requires force to overwrite existing target.
- Invalidation or expiry: Purge is destructive to current rows; retained earlier backups may allow restoration, subject to rotation/pruning. No guarantee that every edit had a backup.
- Activation or effect: Later query population changes; restore changes export bytes, whose admission is separate [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import).
- Evidence limits: Full merge/reconcile/doctor/WAL behavior not audited. Deletion cannot establish erasure from all external or historical copies; restore cannot establish replay of DB-only evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Tombstoning keeps ordinary issue text while marking terminal deletion metadata and clearing close metadata. Purge explicitly removes comments, labels, both directions of dependencies, events and auxiliary state; pending-export bookkeeping handles publication. Restore captures verified immutable backup bytes, writes a synced temporary file and uses rollback protection for forced overwrite. This is data recovery, not restoration of a previous agent conversation. Parent-related supplied records are create/import/close routes, not this withdrawal mechanism; no duplicate identity proposed.

> !issue.ephemeral
>     && !issue.id.contains("-wisp-")
>     && !issue.is_expired_tombstone_at(retention_days, as_of)
> --- `src/sync/mod.rs`

### Claims

#### MEM-CLM-compaction-scope
Label: Compaction does not identify semantic memory compression

The source has legacy issue compaction fields, database VACUUM/recovery machinery and a candidate recovery-family retention contract. None of those names alone establishes a session-trace summarizer or an automatic raw-conversation → derived-instructions → later-model path. SRC-1: `src/model/mod.rs`, `src/config/mod.rs`, `docs/COMPACTION_RETENTION.md`. The doctrine explicitly conditions the retention hook on separate activation; the inspected config module's compaction-retention reference search returned no match at this commit. This qualifies candidate activation, not a claim that the implementation file does not exist. No supplied record counterpart after comparison; boundary already warns about this distinction.

> // Compaction (legacy/compat)
> --- `src/model/mod.rs`

> activation commit exists, the implementation is not wired into compaction.
> Do not infer passing tests or a deployed fix from the candidate commit alone.
> --- `docs/COMPACTION_RETENTION.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-inherited-guidance
Label: Ancestor governing guidance authority

Consumer: external coding agent/human reading a child's CLI output. Channel: selected retained ancestor text with provenance, via [MEM-RTE-inherited-context](#mem-rte-inherited-context). Force: requested governing instructions at the downstream reader, not enforced by the tracker. Horizon: subsequent work in that host's conversation and future repeated reads while source remains. Different from [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions), which uses project instruction files, and [RT-BAP-triage-guidance](runtime.md#rt-bap-triage-guidance), which uses a static MCP prompt. SRC-1: `src/inheritance.rs`, `src/cli/commands/show.rs`, `src/cli/commands/update.rs`.

> //! output. This re-delivers governing instructions at the surface
> //! where the agent actually interacts with `br`, mitigating three
> //! failure modes:
> --- `src/inheritance.rs`

This is an implementation of delivery and a doctrine claim about mitigation. Actual instruction retention after host compaction, priority relative to other instructions, and changed work behavior are unobserved.

## Annotations

#### On [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import)

Memory lineage: import consumes externally authored retained issue records, not a replay of interactive semantic decisions. Local event history and gate evidence are different persistence parts; a reconstructed JSONL-only database is not necessarily the complete local evidence store. Export omission selection is [MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal). SRC-1: `src/storage/schema.rs`, `src/cli/commands/gate.rs`, `src/sync/mod.rs`; supporting passages in [MEM-OBJ-event](#mem-obj-event) and [MEM-OBJ-gate-result](#mem-obj-gate-result).

#### On [RT-RTE-triage-prompt](runtime.md#rt-rte-triage-prompt)

Memory consumers receive projected issue state, not the whole issue rationale. This is requested prompt context with code-chosen fields/row counts, not proactive independent push or host-window eviction. Its alternative prompt consumers are [MEM-RTE-guided-context](#mem-rte-guided-context). SRC-1: `src/mcp/prompts.rs`; supplied record contains selection and delivery evidence.

## Write side

The main acquisition and mutation controls remain those in supplied create/claim/close/import records. Caller authorship and human approval cannot be inferred from an actor string. Software enforces permitted structure and workflow rather than the truth of task descriptions. Separate operative parts explain why the same write can change both reader knowledge and software selection ([MEM-OBJ-issue](#mem-obj-issue), [MEM-OBJ-dependency](#mem-obj-dependency)). CLI agent-context normalization is a syntax gate, not semantic trust; clearing/removing ancestry withdraws future delivery but not already copied host text.

Automatic mutation events are raw traces. Audit coordination produces normalized incident evidence from supplied snapshots and retains a source hash; optional labels append review metadata. No inspected path transforms those traces into retained agent methods and then supplies those methods to a later reasoning consumer. The exact semantic consumer remains unresolved locally rather than being generalized into a system-wide absence of learning ([MEM-RTE-audit-record](#mem-rte-audit-record)). Gate reporting is a different chain: caller verdict → scoped local evidence → later software admission. It can directly change future permitted actions, without proving improved capability or task correctness ([MEM-RTE-gate-report](#mem-rte-gate-report)).

Lint renders missing-section warnings and exit status; the inspected handler does not itself revise descriptions. Polish proposes curation to a later external agent; updates/dependency tools can persist resulting edits. Evidence therefore supports a guided edit affordance, not exercised quality improvement. Reasons can survive in prose/comments/notes, but bounded prompt projections often omit them; detailed issue reads are the established reload path ([MEM-RTE-guided-context](#mem-rte-guided-context), [MEM-RTE-state-read](#mem-rte-state-read); SRC-1: `src/cli/commands/lint.rs`).

Maintenance copies, deduplicates and prunes data rather than summarizing its meaning. Backup history is not a guaranteed per-edit log, and protected pre-salvage bytes differ from ordinary rotating snapshots. Tombstone, purge and export omission have different effects and consumers. Physical compaction and dormant candidate retention must not be reported as conversation summarization ([MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal), [MEM-CLM-compaction-scope](#mem-clm-compaction-scope)).

## Read-back

All established state-content deliveries here begin with caller CLI/MCP requests. Ancestor enrichment automatically selects additional retained content within that request; it is not an independently scheduled injection. Ordinary detail retrieval returns requested content, saved query reads reuse retained filters, ready/scheduler select eligible work, and prompts precompute bounded model-visible subsets. The selection rules are software; the host/model interprets prose and decides work. Only symbolic readiness/gate consumers have demonstrated source-level decision dependencies within br itself.

Working-context control is therefore field/row exclusion before delivery plus targeted reload. An omitted description or intermediate ancestor remains externally reachable; it is not a live reference inside the model window. There is no inspected per-task frame whose pop returns only a result, nor a demonstrated eviction/tail-summary strategy in br. Host compaction is a motivating external condition for re-delivery, not part of this implementation. Limits are row/block budgets, not a universal host token budget. Static installed blurb loading remains an external host affordance ([RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions)); the changing instruction-file artifact is retained across sessions, but the shipped static string itself is not experience-derived memory.

## Integration issues

- **Added operative route, not correction of an asserted absence:** runtime leaves memory scope open; ancestor re-delivery is material beyond its selected routes. Reconciliation should connect [MEM-OBJ-agent-context](#mem-obj-agent-context), [MEM-RTE-inherited-context](#mem-rte-inherited-context) and [MEM-BAP-inherited-guidance](#mem-bap-inherited-guidance) to supplied claim/show behavior, without replacing [RT-OBJ-agent-blurb](runtime.md#rt-obj-agent-blurb). SRC-1: `src/inheritance.rs`, `src/cli/commands/update.rs`, `src/cli/commands/show.rs`.
- **Important non-equivalence:** text update emits inherited context; structured update does not use that branch, while structured show explicitly attaches it. MCP detail projection does not establish ancestor enrichment. Prevents a universal claim-time governance guarantee ([MEM-RTE-inherited-context](#mem-rte-inherited-context), [MEM-RTE-state-read](#mem-rte-state-read); SRC-1: `src/cli/commands/update.rs`, `src/cli/commands/show.rs`, `src/mcp/tools.rs`).
- **Supplied finding retained:** skill's never-automatic sync wording remains in tension with automatic export code. Nothing here repairs that conflict; export/reconstruction must not inherit the stronger promise of complete local-memory portability ([RT-CLM-explicit-sync](runtime.md#rt-clm-explicit-sync), [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import), [MEM-OBJ-event](#mem-obj-event), [MEM-OBJ-gate-result](#mem-obj-gate-result)).
- **Source label corrections:** status_report period is guidance rather than a filtered historical activity acquisition; polish completeness samples/proxies cannot establish semantic completeness; compaction labels do not establish trace summarization or candidate activation ([MEM-RTE-guided-context](#mem-rte-guided-context), [MEM-CLM-compaction-scope](#mem-clm-compaction-scope)). These qualify source-native labels, not supplied runtime facts.
- **Unresolved:** interaction log's later semantic consumer, full auxiliary capacity/acceptance provenance and recovery roundtrips, and non-agents-update instruction distribution variants remain uninspected as named in coverage. Prevents a complete trace-learning, local-evidence portability or uniform installation-admission conclusion. Existing positive routes remain supported; missing facts do not nullify them.
- **Duplicate comparison:** new detail retrieval overlaps ready/MCP lifecycle infrastructure but denotes different selection endpoints; new guided prompt route excludes supplied triage; gate retention precedes supplied close admission; withdrawal is not import. No new declaration is proposed as an alias or replacement of a supplied referent.

## Limitations and checks

This is static implementation/doctrine analysis, not observed host use. It establishes retained stores, selection/delivery and some software decision dependencies; it does not establish compliance, semantic retrieval quality, successful recovery, improved capacity or causal benefit. Uninspected available maintenance/distribution/auxiliary branches are not access gaps or absences. There is no model-provider payload in the inspected br routes to classify as a br-owned numerical memory.

Source identity was rechecked against checkout HEAD and every added anchor stays within SRC-1. Required prompt, types, collection, worker rules, runtime and record-contract reads were completed, including recovery of bounded-read tails. Search errors for nonexistent guessed module paths were inspected and replaced with actual module-directory paths; no target execution followed. Supplied analysis methods were used without authoring skills, prior-analysis reads, delegation or edits to source/run metadata. Deterministic validation: `commonplace-run validate-output` passed for this invocation. It reported: "Member content check passes; invocation residue not checked. This is not job acceptance or claim support." This establishes neither semantic correctness nor acceptance.
