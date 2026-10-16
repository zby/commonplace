---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Binder memory: graph-backed journal distillation, task contracts, selected read-back and recoverable file projections."
run-id: AAS-2026-10-15-binder-a35c41531d40-01
source-identity: "https://github.com/mpazik/binder"
reviewed-boundary: e4066d750ac5c6918706f44b12daa261b261106e
---

# Binder memory report

## Boundary and evidence

Binder retains typed graph state for later people, scripts and agent hosts. This report includes record content, config-controlled admission/rendering, transaction recovery, file projections, CLI/MCP/HTTP/library read surfaces, and shipped journal and task procedures. It does not attribute the external agent host's context window, provider memory or model weights to Binder. The source and functional boundary remain those of [boundary](boundary.md), SRC-1 at e4066d750ac5c6918706f44b12daa261b261106e. HEAD was rechecked against that revision. No target code, tests, examples or model calls were executed.

The runtime records below are supplied findings, not observations of operation. Direct source inspection added the complete journal skill set, journal schema/views/sample data, journal initializer and add-log script, task capture/refinement and investigation/design guides, read/search and MCP tool registration, HTTP routes, CLI dispatch, transaction CLI, journal command gates, undo commands, docs plugin/render orchestration and snapshot implementation. The graph's search/update/rollback portion and delete-cleanup portions were inspected as bounded implementation excerpts/searches. All added paths belong to SRC-1. Executable source supplies implementation evidence; prompts/schema examples supply doctrine/design. Sample journal records are examples, not observed user histories.

### Coverage inventory

| Entry or operation | Source paths in SRC-1 | Coverage and limits |
|---|---|---|
| CLI dispatch and generic writes | `packages/cli/src/index.ts`, `packages/cli/src/commands/delete.ts`, `packages/cli/src/commands/transaction.ts` | Direct reads; [RT-RTE-graph-update](runtime.md#rt-rte-graph-update), [MEM-RTE-history-maintenance](#mem-rte-history-maintenance). Create/update handler internals otherwise supplied through runtime. |
| CLI fetch/search, library graph operations | `packages/cli/src/commands/read.ts`, `packages/cli/src/commands/search.ts`, `packages/repo/src/knowledge-graph.ts`, `packages/cli/src/cli/options.ts` | Direct reads/excerpts; [MEM-RTE-selected-read](#mem-rte-selected-read). Library opening supplied by [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph); arbitrary downstream library callers are not inferred. |
| Registered MCP tools | `packages/cli/src/mcp/tools/index.ts`, `packages/cli/src/mcp/tools/search.ts` | Direct reads: schema/search/transact, not a separate registered read tool. Transact admission supplied by [RT-RTE-graph-update](runtime.md#rt-rte-graph-update). |
| HTTP read/write and browser delivery | `packages/cli/src/http/server.ts` | Direct read; built-in schema/config/record fetch/search and transaction routes included in [MEM-RTE-selected-read](#mem-rte-selected-read). Browser frontend details not inspected; no claim about UI selection completeness. |
| Disk/editor admission and file projection | `packages/cli/src/plugins/docs/index.ts`, `packages/cli/src/document/repository.ts`, `packages/cli/src/lib/snapshot.ts` | Direct reads; [MEM-OBJ-snapshot-metadata](#mem-obj-snapshot-metadata), [MEM-RTE-document-projection](#mem-rte-document-projection). Extraction and LSP entry supplied by [RT-RTE-document-sync](runtime.md#rt-rte-document-sync); full slot/extraction grammar not audited. |
| Log reconciliation, undo/redo, history import/export/squash | `packages/cli/src/plugins/journal/index.ts`, `packages/cli/src/plugins/journal/commands.ts`, `packages/cli/src/plugins/undo/commands.ts`, `packages/cli/src/commands/transaction.ts` | Direct reads; [MEM-RTE-history-maintenance](#mem-rte-history-maintenance). Lower-level repair supplied by [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair). Exact squash-field merging and rehash algorithms not inspected; prevents claims of preservation of every provenance field. |
| Journal capture, initialization, summary and future planning | `examples/journal/journal.ts`, `examples/journal/add-log.ts`, `examples/journal/journal.yaml`, `examples/journal/skills/`, `examples/journal/agents/journal.md` | Direct reads of all eight skill bodies; [MEM-RTE-journal-curation](#mem-rte-journal-curation). Extra data-sync injection is named by prompts but its producer implementation is not present in these paths; provenance and filtering of actual injected calendar/health/activity data remain unresolved. |
| Model-assisted Git ingestion and completion helper | `examples/journal/git-import-logs.ts`, `packages/cli/src/lib/llm.ts` | Supplied [RT-RTE-git-import](runtime.md#rt-rte-git-import), [RT-RTE-llm-call](runtime.md#rt-rte-llm-call); not reclassified as persistence. Provider state remains opaque. |
| Task capture, refinement and later guidance | `examples/workflow/skills/capture-task/SKILL.md`, `examples/workflow/skills/refine-backlog/SKILL.md`, `examples/workflow/skills/implement-task/guides/investigate.md`, `examples/workflow/skills/implement-task/guides/design.md` | Direct reads; [MEM-RTE-task-curation](#mem-rte-task-curation), supplied [RT-RTE-task-guide](runtime.md#rt-rte-task-guide). Discuss/write-tests/old skill details remain uninspected: no exhaustive claim about all task transformation policies. |
| External-source import and schema/template editing | `skills/binder-import/SKILL.md`, `skills/binder-modeling/SKILL.md` | Direct complete reads; write-side account and annotation of [RT-RTE-graph-update](runtime.md#rt-rte-graph-update). Import mapping references and app-building skill details not read; no exhaustive account of all app-specific admission or mapping recipes. |
| Hooks, plugins, scripts and custom servers | `packages/repo/src/local/plugin-loader.ts`, `packages/cli/src/lib/scripts.ts`, `packages/cli/src/http/serverModule.ts` | Supplied [RT-RTE-extension-load](runtime.md#rt-rte-extension-load); dispatch checked directly. Unshipped extension contents and deployed configuration unknown; no universal memory gate or consumer inventory beyond shipped wiring. |
| Evaluators | `packages/cli/tests/doc-sync.test.ts`, `packages/cli/tests/workspace-script.test.ts`, `packages/repo/src/knowledge-graph.test.ts` | Supplied boundary test excerpts and additional declaration searches: round trips, field includes, pagination, rollback and bad-input checks. No test execution or measured semantic-summary/retrieval quality. |

## Core ideas

1. **Persistence and authority are separate.** Graph rules interpret schema, references and transaction operations symbolically. Journal prose and task specifications affect behavior only through interpreting people/models. A retained specification can be an implementation contract without becoming an executable permission boundary. See [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) and the parts below.
2. **The shipped journal has a raw-to-derived-to-later-use chain.** Day logs feed confirmed day summaries; child activity feeds period achievements, learnings and summaries; later briefings, period updates and planning select these fields. This is an explicit prompt-mediated distillation path, not an automatic database summarizer. The `learnings` label establishes neither improved capacity nor correct generalization. [MEM-RTE-journal-curation](#mem-rte-journal-curation).
3. **Context is selected by queries and field projection, not demonstrated semantic memory ranking.** Date/period keys, status filters, relation expansion and field includes control delivery. Search row limits bound records, not tokens. Skill-time command substitutions request preloading; they do not establish an always-on unsolicited memory injector. [MEM-RTE-selected-read](#mem-rte-selected-read).
4. **Maintenance can change what survives.** Rendered Markdown is a selected display and editable projection; snapshot hashes are synchronization metadata, not content summaries. Undo/replay restores state; squash replaces transaction history. These paths must not be mistaken for model context compaction or criticism-based learning. [MEM-RTE-document-projection](#mem-rte-document-projection), [MEM-RTE-history-maintenance](#mem-rte-history-maintenance).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-journal-log
Label: Journal log and captured observations

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: JournalDay `log`, associated `events` and `healthData` fields. Representational form: natural-language observations in symbolic typed/list containers; dates, keys and score integers have fixed structural consumers. Storage substrate: record fields in graph SQLite, with selected Markdown projections. Lineage: user messages through day-log/add-log, conversations through day-start/day-update, and possibly imported external health summaries. The live inputs and original third-party health records are not captured. `log` is relatively raw activity capture, not necessarily a verbatim conversation transcript; day-update explicitly compresses conversation to a sentence. Events can also be model-derived and user-confirmed. These are parts of the runtime graph container, not another graph implementation. SRC-1, `examples/journal/journal.yaml`, `examples/journal/add-log.ts`, `examples/journal/skills/day-log/SKILL.md`, `examples/journal/skills/day-update/SKILL.md`.

> - Append to `log`: `HH:MM - Mid-day update. [1-sentence capture of what came up or was discussed.]`
> --- `examples/journal/skills/day-update/SKILL.md`

Later consumers are day-summary, day-start and period-summary. Their authority is evidence/background for interpretation, not authenticated event truth. Retroactive log additions weaken inference from timestamps, explicitly recognized by day-summary. Write agency and confirmation differ by capture route; see [MEM-RTE-journal-curation](#mem-rte-journal-curation).

#### MEM-OBJ-journal-summary
Label: Journal achievements, learnings and summaries

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: day/period `summary`, `achievements`, period `learnings`, and aggregate scores. Storage substrate: graph records and their rendered views. Representational form: natural-language distilled content, alongside symbolic integer scores. Lineage: logs, prior captures, child summaries, user corrections and sometimes external-source information. These are derived memory rather than raw logs. They do not replace all source fields: summary procedures preserve plans; logs remain separately addressable. SRC-1, `examples/journal/journal.yaml`, `examples/journal/skills/day-summary/SKILL.md`, `examples/journal/skills/period-summary/SKILL.md`.

> Propose `learnings` based on actual period activity (children logs, achievements, events, and summaries), then merge with any learning lines already captured on the target period entry. Keep it concrete. Learnings are composed of personal insights and information from external sources like articles.
> --- `examples/journal/skills/period-summary/SKILL.md`

Later day-start reads summaries and scores for briefing/calibration; period-summary reads children for another aggregation; period-update reads current learnings and parent learnings. The consumer treats them as contextual evidence. No required per-learning source pointer, derivation record or retained full discussion is specified by these output contracts. Reasons may survive in prose, but reliable reconstruction of every inference is not established. The selected field list, not the mere presence of graph data, determines which reasons reach a later consumer. Distinct part from [MEM-OBJ-journal-log](#mem-obj-journal-log): derived content and later selections differ.

#### MEM-OBJ-journal-plan
Label: Journal goal and plan

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: journal `goal` and `plan` fields across day/week/month/quarter/year. Representational form: natural-language desired outcomes and work lists, stored in graph richtext arrays and rendered documents. Lineage: initial user/sample inputs, parent goals, unfinished earlier items, and user-agreed planning changes. Actual initial live-workspace authorship is unknown. Later consumers are briefings and planning/check-in skills; force is user-intent guidance, not execution enforcement. These differ from descriptive summaries because they prescribe future work and have separate edit ownership. SRC-1, `examples/journal/journal.yaml`, `examples/journal/skills/day-next-plan/SKILL.md`, `examples/journal/skills/period-next-plan/SKILL.md`.

> **Flag zombie tasks** — anything that's been unfinished for 3+ consecutive days:
> --- `examples/journal/skills/day-next-plan/SKILL.md`

> Force a decision. No silent rolling.
> --- `examples/journal/skills/day-next-plan/SKILL.md`

Carry-forwards require interpreting completion evidence and human dispositions; database state alone does not mechanically identify a zombie item. Drop means omit from the new plan, not erase prior history. See [MEM-RTE-journal-curation](#mem-rte-journal-curation).

#### MEM-OBJ-task-findings
Label: Retained task descriptions and investigation findings

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: Task descriptive/capture fields and `rootCause`, `stepsToReproduce`, `sourceFiles`, `potentialSolution`. Storage: graph records, potentially rendered files. Form: natural-language descriptions/diagnoses with symbolic status, links and filepath lists. Capture separates user-provided from inferred fields; investigation derives findings from reproduction, tracing, code and history. Initial live task content is not captured. Later implement-task reads these fields to select guides and orient product work; the diagnosis is proposed explanatory content, not a verified runtime invariant. SRC-1, `examples/workflow/skills/capture-task/SKILL.md`, `examples/workflow/skills/implement-task/guides/investigate.md`.

> For `rootCause`, explain **why** the bug happens, not just where. For `sourceFiles`, list all files involved — not just the entry point.
> --- `examples/workflow/skills/implement-task/guides/investigate.md`

This part retains a requested causal explanation, unlike a timestamp-only trace; reproduction commands/results or full investigation rationale need not all persist in the specified fields. Its generic downstream route is already [RT-RTE-task-guide](runtime.md#rt-rte-task-guide); no duplicate route is declared here.

#### MEM-OBJ-task-specification
Label: Task specification and acceptance constraints

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: Task `specification`, `acceptanceCriteria`, `constraints`, `outOfScope`. Storage: graph fields and optional file projections. Form: natural-language contract and criteria, not executable tests themselves. Lineage: user-approved capture/refinement, design discussion, source inspection and linked records. Later implementation is instructed to follow specification, subordinate to passing existing tests as described by [RT-RTE-task-guide](runtime.md#rt-rte-task-guide). Different authority and admission from descriptive task findings warrant this separate part. SRC-1, `examples/workflow/skills/implement-task/guides/design.md`, `examples/workflow/skills/capture-task/SKILL.md`, `examples/workflow/skills/refine-backlog/SKILL.md`.

> This is a collaborative guide — propose the design and discuss with the user before writing it.
> --- `examples/workflow/skills/implement-task/guides/design.md`

> - `specification` has Approach, Contracts, File Plan, Validation, and Steps sections
> - The user has agreed to the design
> --- `examples/workflow/skills/implement-task/guides/design.md`

Rejected design alternatives are discussed briefly, not required as durable criticism records. Reasons can survive in Approach/File Plan, but the output format does not require the full deliberation. This establishes a retained contract affordance, not demonstrated theory revision or learning.

#### MEM-OBJ-config-views
Label: Schema, views and navigation config

Part of: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Source-native identity: config Field/Type/View/Navigation entities. Storage: graph config tables and projected config files; process-local schema/view/navigation caches are separate transient copies. Operative parts: symbolic datatype/constraint/query/path/slot rules consumed by parser/admission/render code, and natural-language template headings/descriptions displayed to people/models. Editing a template is not a model-weight update. Lineage: built-ins plus imported or edited workspace configs; live initialization choices unknown. Config changes govern later structural admission and what selected content appears in documents, not factual correctness. SRC-1, `skills/binder-modeling/SKILL.md`, `packages/cli/src/plugins/docs/index.ts`, `examples/journal/journal.yaml`; preparation evidence is supplied by [RT-RTE-graph-update](runtime.md#rt-rte-graph-update).

> Schema is stored as data — types and fields are config entities that evolve through transactions.
> --- `skills/binder-modeling/SKILL.md`

> if (configsChanged) ctx.invalidateCaches?.();
> --- `packages/cli/src/plugins/docs/index.ts`

The journal views deliberately render child summaries at parent levels rather than the full child log. Thus a Markdown consumer can receive less evidence than a field-expanded CLI consumer. This is configuration-directed projection, not proof of semantic summarization by the renderer.

#### MEM-OBJ-snapshot-metadata
Label: Snapshot content and synchronization metadata

Source-native identity: rendered snapshot files and `SnapshotMetadata` / `cliSnapshotMetadataTable`. Storage: filesystem content plus CLI database metadata. Form: file content is selected natural-language text and symbolic preamble; path, transaction ID, entity UID, mtime, size and SHA-256 are symbolic access/synchronization metadata, not a readable content summary or an embedding. Lineage: renderer-selected graph entities/config/templates; metadata tracks writes or refreshes. Actual document consumers are people/editors and later docs sync, while metadata is consumed by sync/render change detection. SRC-1, `packages/cli/src/lib/snapshot.ts`, `packages/cli/src/document/repository.ts`.

> export type SnapshotMetadata = {
>   id?: number;
>   path: string;
>   txId: TransactionId;
>   entityUid: EntityUid | null;
>   mtime: number;
>   size: number;
>   hash: string;
> };
> --- `packages/cli/src/lib/snapshot.ts`

Distinct from the graph container: these are derived disk projections and CLI metadata, not another name for all graph records. Closest supplied [RT-RTE-document-sync](runtime.md#rt-rte-document-sync) is an ingress route, not this object. Per-document field projection differs from both a complete graph backup and a host context checkpoint.

### Routes

#### MEM-RTE-selected-read
Label: Requested graph selection and delivery

Endpoints/progression: CLI read/search, MCP search, HTTP record/config/schema request or graph fetch/search call → schema-aware selection → includes/relations where exposed → serialization/reference formatting → requesting consumer. Owner: caller chooses query/reference/fields; deterministic code selects stored rows and serializes them. State: current graph/schema and query; no model ranking step is established in these handlers. These are access capabilities; actual named agent consumers are the journal/task routes below, not an invented generic caller. Distinct from [RT-RTE-graph-update](runtime.md#rt-rte-graph-update): selection/delivery, not admission. SRC-1, `packages/cli/src/commands/read.ts`, `packages/cli/src/commands/search.ts`, `packages/cli/src/mcp/tools/index.ts`, `packages/cli/src/mcp/tools/search.ts`, `packages/cli/src/http/server.ts`, `packages/repo/src/knowledge-graph.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected entity/list/schema, pagination and optionally formatted relation references; CLI/MCP/HTTP shapes differ.
- Later read-back: retrieves records/config changed in earlier invocations; a bare API alone establishes capability, while shipped journal/task prompts establish intended later consumers.
- Delegated visibility: command output/tool structured data/HTTP JSON goes to requester; no automatic injection into every agent window is established.
- Selection predicate: reference or filters, namespace, optional ordering/cursors and includes; graph default search limit is 50. CLI argv --limit trims returned items after graph search, whereas stdin pagination can set the graph limit. MCP exposes filters/limit/cursors but not CLI field-includes; HTTP built-ins do not expose that same nested includes contract.
- Invalidation or expiry: later mutations/deletion/rollback change subsequent results; prior delivered copies are not recalled by these handlers.
- Activation or effect: code returns selected data; whether a human/model follows or relies on it is unobserved.
- Evidence limits: row budgets are not token budgets; relation expansion and long text can enlarge payloads. No measured completeness/relevance or deployed caller access controls.

> const limit = pagination?.limit ?? DEFAULT_SEARCH_LIMIT;
> --- `packages/repo/src/knowledge-graph.ts`

> const items = applySelection(result.data.items, { limit: args.limit });
> --- `packages/cli/src/commands/search.ts`

The second passage challenges the inference that a large CLI argv limit necessarily retrieves that many rows: that branch builds no graph pagination parameter. A seven-day lower date bound is similarly not a hard seven-record or upper-date cap. Neither selector guarantees exhaustive duplicate search without pagination.

#### MEM-RTE-journal-curation
Label: Journal capture, distillation and later planning

Endpoints/progression: invoked journal skill/date offset and conversation → selected retained entries → agent proposal/capture → user decisions where requested → Binder update → later briefing, summary, check-in or planning invocation. `journal.ts` creates missing date/parent entities before printing a key/path; it stops scanning missing ancestors at an existing entity and adds previous links when found. The code controls initialization; the foreground model/human owns semantic changes under prompt policy. Closest supplied [RT-RTE-git-import](runtime.md#rt-rte-git-import) is only a proposed log producer; this route adds actual instructed graph writes and named later consumers, not a duplicate importer. SRC-1, `examples/journal/journal.ts`, `examples/journal/skills/day-log/SKILL.md`, `examples/journal/skills/day-start/SKILL.md`, `examples/journal/skills/day-update/SKILL.md`, `examples/journal/skills/day-summary/SKILL.md`, `examples/journal/skills/day-next-plan/SKILL.md`, `examples/journal/skills/period-summary/SKILL.md`, `examples/journal/skills/period-update/SKILL.md`, `examples/journal/skills/period-next-plan/SKILL.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: instructed capture confirmation, briefing, proposal, scored reflection or plan; initializer itself prints key/path or fails.
- Later read-back: day-start selects recent summaries/scores; period-summary selects child logs and derived fields for aggregation; period-update includes current/parent learnings; next planning reads prior achievements/summary and parent/sibling plans.
- Delegated visibility: host skill command substitutions request YAML context preloading; follow-up Binder reads provide missing context; update persists chosen fields through graph admission.
- Selection predicate: granularity/date offset, period key, parent/children links and explicit field lists; recent days use a seven-day lower bound. Output-size instructions bound prose/items (for example 3–7 learnings), not model input tokens.
- Invalidation or expiry: append/replace updates and explicit planning decisions revise retained content; summary does not erase logs. Dropped items are not carried forward. No automatic time-to-live in these prompts.
- Activation or effect: prompts instruct calibration, reflection and concrete future planning from stored context; implementation of the host loading contract and semantic compliance are unobserved.
- Evidence limits: no live journal, dialogue, confirmed write or later model response; named external data-sync injection has opaque inputs/selection. Requested deduplication and groundedness are not verified semantic guarantees.

Admission differs by mechanism. Day-log accepts the supplied message without a second confirmation; day-start writes after user answers rather than waiting for a separate write request; day-update writes a compact log when conversation closes. Day-summary waits for corrections/score adjustments and confirmation before final fields; it forbids plan edits and assigns carry-forward writes to day-next-plan. Day-next-plan explicitly asks move/schedule/drop and writes agreed target/future plans after reading existing future plans. Period-summary proposes aggregation/learnings, accepts user correction/defaults, preserves the source plan and carries confirmed next items; period-next-plan writes agreed goal/plan and may defer items to a parent backlog; period-update confirms before replacing plan or editing learnings/events/achievements. Human semantic veto is prompt policy in these named paths, not a graph-wide gate. Structural parsing/schema rejection remains software-owned. Open personal planning is the operating mode; activity records and self-scores are inputs, not an independently supplied answer oracle. Recovery uses explicit edits/undo, not automatic reversal of a mistaken interpretation.

> Reuse context already present in the conversation when available (source day entry, target day entry, week context, recent days). Only run binder context commands for missing pieces.
> --- `examples/journal/skills/day-summary/SKILL.md`

> 4. **`learnings`**: final deduplicated learning lines for the period (distilled from activity, merged from children + period-level captures) — list of strings
> --- `examples/journal/skills/period-summary/SKILL.md`

This is trace-fed derived memory with a requested later consumer through period-update/parent aggregation, but not a fully automatic trace-fed write: the foreground agent and user participate. The record supports a durable summary/planning pathway without demonstrating improved future capacity or source-correct distillation. Initial external provenance remains unknown without suppressing this known downstream transformation.

#### MEM-RTE-task-curation
Label: Task admission and retained design refinement

Endpoints/progression: user description → capture with inferred fields marked → duplicate check/user approval → draft or approved pending Task → refinement/investigation/design → stored task findings/contract → existing task-guide consumer. Owner: foreground agent proposes, user approves capture/refinement/design; investigation guide itself asks the agent to write findings after reproduction/tracing, without a separate explicit confirmation clause. Context/effects: task state, linked records, code and tests; accepted field changes persist in graph. Distinct from supplied [RT-RTE-task-guide](runtime.md#rt-rte-task-guide): this is its producer/admission side. SRC-1, `examples/workflow/skills/capture-task/SKILL.md`, `examples/workflow/skills/refine-backlog/SKILL.md`, `examples/workflow/skills/implement-task/guides/investigate.md`, `examples/workflow/skills/implement-task/guides/design.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed record/changes and instructed persistence; exact duplicates may stop creation, vague tasks cause clarification.
- Later read-back: implement-task rereads retained fields to select guides; implementation consumes specification/criteria and sourceFiles through [RT-RTE-task-guide](runtime.md#rt-rte-task-guide).
- Delegated visibility: draft/existing/cancelled lists and schema are requested through skill commands; full task/linked records are pulled as needed; stored fields cross invocations, not necessarily the whole discussion.
- Selection predicate: named tasks or draft list; status/type/size determine required fields; retained cancelled tasks participate in duplicate rejection and terminal task status prevents implementation.
- Invalidation or expiry: refinement may merge unique content, cancel duplicate drafts, split children or replace fields; cancelled records remain searchable. No timed expiry specified.
- Activation or effect: intended later guide selection and contract-following; prompt compliance and actual product effect unobserved.
- Evidence limits: duplicate checks operate on selected query results; no exhaustive semantic duplicate oracle or independent correctness check of rootCause/design is supplied.

> - **Partial overlap** → merge the unique parts into the existing task, cancel the draft
> --- `examples/workflow/skills/refine-backlog/SKILL.md`

> - Propose changes to the user and wait for approval before executing
> --- `examples/workflow/skills/refine-backlog/SKILL.md`

Admission guidance is source-specific: retain what the user said, mark inferences, do not silently invent acceptance criteria, inspect links before pending, and reach agreement on design. User refusal can leave a draft partly filled. The graph enforces structure, not the Definition of Ready or user approval as a universal invariant. Open task work is the mode. Reproduction and project tests inform findings; no independent oracle for all diagnosis/design outcomes is established. Edits/cancellation and generic undo supply recovery, not an autonomous revision evaluator. This route retains explanations/contracts; it does not establish formulated content-directed criticism and iteration merely because the guide is named investigate or design.

#### MEM-RTE-document-projection
Label: Graph projection and orphan withdrawal

Endpoints/progression: originating commit/rollback or explicit render → config cache invalidation → navigation/view selection and rendering → saveSnapshot and orphan cleanup → filesystem/editor readers and later file-to-graph sync. Owner: docs plugin and deterministic render/snapshot code. Context: current graph, views, navigation, paths and tracked metadata. Distinct from [RT-RTE-document-sync](runtime.md#rt-rte-document-sync): outward projection/withdrawal, rather than disk extraction/admission. SRC-1, `packages/cli/src/plugins/docs/index.ts`, `packages/cli/src/document/repository.ts`, `packages/cli/src/lib/snapshot.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: modified/diverged path lists or error, with optional LSP file notifications; post-commit failure does not undo graph state.
- Later read-back: filesystem readers see selected views; docs sync/LSP use retained files plus metadata as later edit input. No automatic model consumer is established by writing a file.
- Delegated visibility: Markdown/YAML content on disk, plus notifications to connected editor; a view may omit raw fields or substitute child summaries.
- Selection predicate: Navigation query/path and View slots; save mode fast/verify/force controls unchanged/diverged files; cleanup compares tracked paths with rendered paths by namespace.
- Invalidation or expiry: config changes invalidate view/navigation caches; orphan cleanup deletes tracked files and metadata not in the rendered set. Force can overwrite diverged files; verify can preserve them and report divergence.
- Activation or effect: rendering changes files/readable display, cleanup withdraws tracked projections; it does not retract already-copied text from agents or external files.
- Evidence limits: no execution or exhaustive extraction/render proof; generated files are not necessarily complete graph backups, and filesystem effects remain best effort after commit.

> if (mode === "verify") return ok("skipped-diverged");
> --- `packages/cli/src/lib/snapshot.ts`

> if (renderedSet.has(metadata.path)) continue;
> --- `packages/cli/src/lib/snapshot.ts`

Write admission for projected content is software-controlled by config and graph state; a person can author the originating data/config or choose force, but no per-file semantic approval is inserted. Disk edits flow through the separate supplied ingress route. Cleanup is deterministic lifecycle maintenance, not evaluation of whether a claim is true or useful. A model context checkpoint or learned representation is not produced here.

#### MEM-RTE-history-maintenance
Label: History import, undo and replacement

Endpoints/progression: transaction import/preview, undo/redo, rollback/squash or journal verify/repair caller → parse/select/history checks and command-specific confirmation → update, rollback, prepared apply or log reconciliation → persisted graph/history/log/redo state → later graph readers or recovery calls. Owner: CLI and graph code; caller chooses operation/input. This groups deterministic history lifecycle under explicit operation-specific admission rules, not one universal gate. Overlap with [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair) is the repair leg, and with [RT-RTE-graph-update](runtime.md#rt-rte-graph-update) the fresh import leg; the distinct referent is their caller-facing lifecycle including undo/redo and squash. SRC-1, `packages/cli/src/commands/transaction.ts`, `packages/cli/src/plugins/undo/commands.ts`, `packages/cli/src/plugins/journal/commands.ts`, `packages/cli/src/plugins/journal/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: previews, selected transaction data/log/export, maintenance success or error; a preview can report individual failures and still finish without applying.
- Later read-back: graph state after rollback/replay is used by future queries; redo reads staged undo JSONL; verify/repair reads transaction log and DB history. Export emits TransactionInput for a possible later import, not automatic read-back by itself.
- Delegated visibility: transaction displays/JSON/YAML/JSONL reach caller; repair can write backups; logs are retained change/recovery traces, not semantic summaries or model lessons.
- Selection predicate: transaction counts/IDs/hash head, author/log display filters, explicit input files/stdin, repair direction and divergence; tx log defaults to 10 fetched entries, range export fetches up to 10000 before filtering.
- Invalidation or expiry: undo rolls back suffixes, new commits clear redo staging through plugin behavior, redo requires matching predecessor; squash replaces a suffix with a merged transaction. Repair can replace divergent log/DB history under selected authority.
- Activation or effect: changes retained content and/or recovery history; later reads can reflect restored state. No measured repair success, semantic truth adjudication or beneficial learning.
- Evidence limits: multiple update/replay operations are not established as one atomic batch; exact squash-field aggregation, all backup-restoration procedures and arbitrary extension side effects are not established.

> // Rollback + apply: both plugins react via their subscriptions.
> --- `packages/cli/src/commands/transaction.ts`

> "Cannot redo: repository state has changed since undo",
> --- `packages/cli/src/plugins/undo/commands.ts`

Fresh file/stdin import parses and calls update for each input; preview calls process without applying. Neither physical import nor dry-run establishes per-content human approval. The import skill separately requires mapping approval and then approval after batch dry-run (SRC-1, `skills/binder-import/SKILL.md`). Undo/redo apply directly after checks; protected rollback/squash call confirmProtected (TTY confirmation or explicit --yes; non-TTY otherwise refuses). Journal verify diagnoses integrity/sync and does not curate factual content. Repair defaults to DB authority; log-authoritative repair confirms when discarding DB-only transactions; forced log overwrite confirms when discarding log-only transactions; rehash requests protected confirmation and backup, then repairs DB from the rehashed log. Caller decisions can veto through these gates, but --yes is authorization of the operation rather than evidence of reviewing each transaction. Hash/version checks are recovery references, not answer oracles. Explicit maintenance is the operating mode. Rejection returns errors/no-op on refusal; backups and redo provide bounded recovery, not universal reversal.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-journal-guidance
Label: Journal memory to briefing and future-plan choices

Consumer: foreground agent interpreting journal skills and interacting user. Channel: selected Binder command outputs requested by skill template, additional reads, then natural-language instructions. Force: evidence/background from logs and summaries; goal/plan fields express user commitments; scores calibrate proposed ratings, not an enforced reward function. Horizon: later day/period invocations and potentially sessions, when stored content is selected; actual recurrent use is unobserved. SRC-1, `examples/journal/skills/day-start/SKILL.md`, `examples/journal/skills/period-update/SKILL.md`, `examples/journal/skills/day-next-plan/SKILL.md`, `examples/journal/skills/period-next-plan/SKILL.md`. Distinct from [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance): different records, consumers' tasks and authority. Route: [MEM-RTE-journal-curation](#mem-rte-journal-curation).

> If `healthData` contains sleep data, **propose a sleep score in the briefing** — don't ask about sleep. Use recent days' sleep data and scores as calibration (e.g. if 8.3h scored 8, and today is 7.0h with low deep sleep, propose 6). Show your reasoning briefly:
> --- `examples/journal/skills/day-start/SKILL.md`

The prompt makes retained material relevant to a later decision. It does not establish compliance, calibration accuracy, improved capacity or causal benefit.

## Annotations

#### On [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph)

Memory consumers differ by part: schema/config have fixed structural authority at admission/rendering; text fields have interpretive authority only at actual people/model consumers. Journal raw/derived/planning and task findings/contracts are separately declared above. Transaction history stores symbolic changes and author/time/source/message metadata for read/export/recovery, not necessarily the rationale behind a content claim. Source annotations are provenance labels, not authentication or epistemic validation. SRC-1, `packages/cli/src/commands/transaction.ts`, `packages/cli/src/cli/options.ts`; the graph container's storage evidence is supplied by the cited record.

#### On [RT-RTE-graph-update](runtime.md#rt-rte-graph-update)

Import adds another fresh-input path using the same semantic admission: file/stdin parsing → per-input update. Imported YAML may contain both config and records. The binder-import prompt requires sampling, schema gap resolution, approved mapping, duplicate treatment and approval after dry-run; this is not an enforced property of tx import. Stable-key upsert does not prove semantic duplicate resolution when keys differ. Schema/modeling changes can alter later admission and file presentation, while the modeling prompt itself warns dry-run can be lenient for dataType validity. That warning is doctrine, not an independently demonstrated runtime failure here. SRC-1, `packages/cli/src/commands/transaction.ts`, `skills/binder-import/SKILL.md`, `skills/binder-modeling/SKILL.md`.

> Only after user approval:
> --- `skills/binder-import/SKILL.md`

#### On [RT-RTE-git-import](runtime.md#rt-rte-git-import)

Retained prior/current logs are context and deduplication evidence for this model call, but printed parsed entries have no admitted later consumer inside the script. This is a trace-to-proposal transformation, not an automatic durable trace-learning path. The supplied record's output quote and parsing caveat support this distinction. Opaque external model/agent state remains outside inspected memory.

#### On [RT-RTE-llm-call](runtime.md#rt-rte-llm-call)

Working-context control is a fresh one-user-message completion with selected system/user text and optional response schema. It neither reloads prior conversation here nor establishes a separate subagent/fork/pop protocol. Returned extracted data/usage escapes to the caller, not a whole persisted model conversation; usage/failure JSONL lacks an established later behavior-shaping reader. Provider-side retained state and host compaction are uninspected. The supplied record supplies source and quote. Fresh-context construction is local scope control, not evidence that the provider forgets.

#### On [RT-RTE-extension-load](runtime.md#rt-rte-extension-load)

Configured hooks receive transaction JSON and execute automatically after subscribed events. This is push delivery to extension code, distinct from requested journal context loading. No retained summary or later agent-memory consumer is established merely by the loader. Extensions can implement independent persistence through repo/DB/filesystem capabilities, so built-in admission and expiry conclusions cannot be generalized to arbitrary workspace code. The supplied record supplies implementation evidence.

#### On [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance)

The relevant durable inputs are task findings and task specification/criteria, not the static guide itself. User-approved design contracts and generated diagnoses have different lineage and approval rules. Later guide rereads can select a different procedure after fields change; they do not prove content criticism or improved capacity. The task record may retain a reason in rootCause/Approach, while the prescribed design record need not preserve rejected alternatives. SRC-1, `examples/workflow/skills/implement-task/guides/investigate.md`, `examples/workflow/skills/implement-task/guides/design.md`; consumer authority is supplied by the cited record.

## Write side

The graph admits symbolic changes, not truth. Fresh update routes converge on schema preparation; prepared replay bypasses that fresh preparation. Text author, physical writer and admission decision are different: an agent may propose a summary, a person approve it under a skill, the CLI submit it, and graph software reject malformed data. No generic author string establishes human review. [RT-RTE-graph-update](runtime.md#rt-rte-graph-update), [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair).

The journal chain keeps raw-ish captures, derived summaries and future intentions separate. Capture can be a direct user message, a compact conversation log or initializer-created structural entry. Day-summary retains user-confirmed scores/achievements/summary; period-summary merges lower-level activity and proposes 3–7 learning lines; period-update can append, reshape or remove confirmed learning lines. Later read-back is explicitly named in [MEM-RTE-journal-curation](#mem-rte-journal-curation). These operations can change meaning through model/human interpretation, but the engine does not itself perform semantic distillation. Rationale retention is partial: raw logs remain separately reachable, while selected later summaries may omit them. External article/health/calendar provenance is not necessarily retained at source-record granularity. Source trust is conversational and procedural, not cryptographically authenticated factual warrant.

Task capture/refinement labels inferences, rejects duplicates and keeps cancelled records available to avoid recreating deliberately cancelled work. Investigation requests causal explanation; design retains an implementation contract. These are different authority-bearing products, not one universal task-memory class. User approval is explicit for capture/refinement/design, not a mandatory extra step in the investigation guide or graph handler. [MEM-RTE-task-curation](#mem-rte-task-curation).

Import and modeling provide material-edit/adoption surfaces for records, schema and templates. The import prompt samples sources rather than loading entire large inputs, asks mapping approval, prefers stable-key upserts, stages batches (default 50 records, 30 with relations), dry-runs and asks approval before applying. These are working-context and curation instructions, not executable guarantees or a model context-token manager. Unknown live initialization choices coexist with these known subsequent edit paths. SRC-1, `skills/binder-import/SKILL.md`, `skills/binder-modeling/SKILL.md`; [RT-RTE-graph-update](runtime.md#rt-rte-graph-update).

Withdrawal has several scopes. Duplicate cancellation/drop changes selection/reliance while preserving earlier records. CLI delete submits a graph deletion, and delete preparation expands incoming-reference cleanup; the bounded inspection did not prove cleanup of every arbitrary text reference. Document cleanup removes tracked orphan projections, not all copies of the assertion. Undo/rollback/replay changes current graph history; squash reduces transaction granularity and can replace author metadata with the newest author. Protected confirmations and redo/version checks are maintenance safeguards, not evaluation of claim quality. SRC-1, `packages/cli/src/commands/delete.ts`, `packages/repo/src/changeset-processor.ts`, `packages/cli/src/commands/transaction.ts`; [MEM-RTE-document-projection](#mem-rte-document-projection), [MEM-RTE-history-maintenance](#mem-rte-history-maintenance).

Authored storage/round-trip tests evaluate persistence, serialization and rejection paths. No supplied observed run demonstrates their passing, and those checks do not establish factual correctness of a journal summary or root-cause diagnosis. The output of verify is a report of hash/sync consistency; its later consumer is the operator choosing repair. It is not retained criticism that autonomously revises journal knowledge. SRC-1, `packages/cli/src/plugins/journal/commands.ts`; boundary evaluator inventory and [RT-CLM-transaction-boundary](runtime.md#rt-clm-transaction-boundary).

## Read-back

Read-back is request-driven in the inspected built-ins: a reference/query chooses rows and fields, and the requesting process/host receives formatted values. A file path is a location, not evidence that someone read it. The named shipped consumers are journal skill commands and task guide reads; the database library alone provides a capability. [MEM-RTE-selected-read](#mem-rte-selected-read).

Journal invocation requests preloaded target/parent/recent entries, sometimes child records or siblings. Period-summary reads rich child activity; period-next-plan reads selected parent/child goals, achievements and summary, not every raw log or learning line. Period-update explicitly includes learnings. Thus retained reasons can be available in the graph yet omitted from one planning prompt. Static guides are context supply but not use-derived memory; stored plan/summary/rootCause/specification fields are use-derived inputs when selected later. [MEM-OBJ-config-views](#mem-obj-config-views), [MEM-RTE-journal-curation](#mem-rte-journal-curation), [RT-RTE-task-guide](runtime.md#rt-rte-task-guide).

Budgets have distinct units: graph search defaults to 50 rows, includes select fields/relations, skill sampling limits source rows/files, and prompt output caps constrain prose. None establishes a shared input-token allocator, trimming algorithm or automatic host compaction. Day-summary's reuse instruction avoids fetching already-present context, but may reuse older in-window values; freshness under concurrent edits is not guaranteed by that instruction. The completion helper uses a fresh call context; the Git importer sends selected commit/log text to an external executable and parses a reduced return. No Binder-managed subagent frame isolation, verbatim-tail retention, summary checkpoint reload or eviction/reload protocol was established in these inspected routes; external host behavior remains uninspected rather than absent. [RT-RTE-llm-call](runtime.md#rt-rte-llm-call), [RT-RTE-git-import](runtime.md#rt-rte-git-import), [MEM-RTE-journal-curation](#mem-rte-journal-curation).

In stack-frame terms, the completion helper exposes a bounded call/return shape, but it does not define the external host's conversational frame lifetime. Graph keys point to externally retrievable material; they do not create automatically followed references inside a model window. This limits the memory-management analogy without implying a missing implementation defect.

## Integration issues

- **Qualification, not a correction of declared runtime status:** [RT-RTE-graph-update](runtime.md#rt-rte-graph-update) mentions pagination generally; [MEM-RTE-selected-read](#mem-rte-selected-read) distinguishes actual surfaces. CLI argv --limit is post-search trimming and cannot be assumed to enlarge graph retrieval; stdin pagination can. MCP lacks the CLI includes interface. Evidence: SRC-1, `packages/cli/src/commands/search.ts`, `packages/cli/src/mcp/tools/search.ts`. Consequence: do not infer exhaustive duplicate/context coverage from the CLI query examples or a large displayed limit.
- **Route overlap:** [MEM-RTE-history-maintenance](#mem-rte-history-maintenance) includes the repair leg of [RT-RTE-journal-repair](runtime.md#rt-rte-journal-repair) and fresh-input import through [RT-RTE-graph-update](runtime.md#rt-rte-graph-update). It is a broader caller-facing lifecycle account, not a replacement identity. If reconciliation needs operation-level separation, preserve repair's supplied identity and attribute undo/squash/gates to this additional record. Evidence: SRC-1, `packages/cli/src/commands/transaction.ts`, `packages/cli/src/plugins/journal/commands.ts`, `packages/cli/src/plugins/undo/commands.ts`.
- **Projection versus ingress:** [MEM-RTE-document-projection](#mem-rte-document-projection) and [RT-RTE-document-sync](runtime.md#rt-rte-document-sync) share graph/files but opposite producers and effects. Do not supersede one with the other. [MEM-OBJ-snapshot-metadata](#mem-obj-snapshot-metadata) is separate metadata/projection, not a second [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph). Evidence: SRC-1, `packages/cli/src/lib/snapshot.ts`, `packages/cli/src/plugins/docs/index.ts`.
- **Opaque journal inputs:** [MEM-RTE-journal-curation](#mem-rte-journal-curation) preserves known log/summary transformations while calendar/health/activity injection and actual original-source lineage remain unresolved. Prompt declarations are the evidence; no data-sync implementation was inspected or separately registered. Prevents attributing filtering, trust or model-window budgets to that extension.
- **Add-log comment exceeds visible behavior:** `examples/journal/add-log.ts` says it creates missing day/parents, but its body only submits an update against today's reference. It does not invoke the structural initializer. [MEM-OBJ-journal-log](#mem-obj-journal-log) therefore does not attribute ancestor initialization to this script; that responsibility is established in `examples/journal/journal.ts` under [MEM-RTE-journal-curation](#mem-rte-journal-curation). No runtime failure was executed; possible external/workspace behavior is unresolved.
- **Exact history retention is bounded:** [MEM-RTE-history-maintenance](#mem-rte-history-maintenance) establishes squash/replay and protected gates, not exact preservation of every transaction metadata/rationale field. Merge/rehash internals and full backup restoration remain uninspected. The conceptual append-only label in modeling doctrine must not override these explicit history-replacement surfaces. Evidence: SRC-1, `packages/cli/src/commands/transaction.ts`, `packages/cli/src/plugins/journal/commands.ts`.
- **No other possible duplicate declaration identified:** journal/task/config object records explicitly partition the supplied graph container through Part of fields; task-curation is upstream of [RT-RTE-task-guide](runtime.md#rt-rte-task-guide), and [MEM-BAP-journal-guidance](#mem-bap-journal-guidance) is distinct from [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance). Remaining guide/app/browser/extraction details and unshipped extension consumers are the coverage limits named above, not evidence of absence.

## Limitations and checks

The source identity, HEAD and supplied member run/revision were rechecked; this report adds no source or external evidence. All conclusions are source-grounded implementation or prompt-policy findings, not observed activation or demonstrated benefit. Method identity is this invocation's supplied memory type, worker rules and records contract; no unrelated authoring workflow or prior analysis was used. `learning` as improved future capacity, reliable semantic curation and exercised self-improvement are not established by retaining fields named learnings, summaries or specification. The positive retained-content/consumer paths stand independently of those unestablished claims.

Available but uninspected details are not access gaps. In particular full relation/slot extraction, squash/rehash algorithms, all workflow guides and custom app behavior prevent exhaustive correctness or whole-loop consumer completeness claims. External provider/host state prevents a complete model-memory or context-management account. No source execution was authorized or performed.

Validation: required validate-output completed successfully (exit 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Form/quotation validation does not establish semantic correctness or coordinator acceptance.
