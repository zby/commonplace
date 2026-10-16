---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memex memory mechanisms: raw archive, derived wiki, evolving schema, result history and later file-directed consumers."
run-id: AAS-2026-10-14-memex-42ecde52cc05-01
source-identity: "https://github.com/wastedcode/memex"
reviewed-boundary: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
---

# Memex memory report

## Boundary and evidence

Memex retains a filesystem wiki between fresh Claude Code jobs. This report covers acquisition, derived pages, schema, index, logs, result persistence, configuration read-back, maintenance, file browsing and withdrawal within the [boundary](boundary.md). SRC-1 supplies implementation and doctrine/design only. No populated wiki, execution trace or evaluation result was supplied. The external Claude context manager, instruction discovery, provider state and configured MCP services remain opaque; their absence is not inferred.

Direct reads covered `src/index.ts`, `package.json`, `src/cli/client.ts`, `src/cli/commands/ingest.ts`, `src/cli/commands/query.ts`, `src/cli/commands/config.ts`, `src/cli/commands/status.ts`, `src/cli/commands/logs.ts`, `src/daemon/scaffold.ts`, `src/daemon/routes.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts`, `src/daemon/namespace.ts`, `src/daemon/auth.ts`, `src/lib/constants.ts`, all four `src/lib/prompts/` files, `docs/prompts.md` and `docs/operations.md`. Correction-round direct reads additionally traced `src/cli/commands/destroy.ts`, the full client and server transport in `src/cli/client.ts` and `src/daemon/server.ts`, route registration/deletion in `src/daemon/routes.ts`, scaffold deletion, database cascades and the documented destroy options. Startup recovery and other CLI/security details are supplied runtime findings, not new direct inspection. CLI dispatch, the complete route registry, exported client methods and runner dispatch were checked for alternate memory entry points: job types are ingest/query/lint, with separate upload, browsing, configuration, history/status and deletion operations. No target was executed.

| Entry point or operation | SRC-1 source path | Coverage and conclusion limit |
|---|---|---|
| Create and upload | `src/daemon/scaffold.ts`, `src/daemon/routes.ts`, `src/cli/commands/ingest.ts` | [MEM-OBJ-raw](#mem-obj-raw), [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job); owner submission admits bytes, not their truth. |
| Ingest extraction, merging and provenance | `src/lib/prompts/ingest.ts`, `src/lib/prompts/wiki.ts` | [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job); requested transformations, no generated pages. |
| Schema revision and later filing | `src/lib/prompts/ingest.ts`, `src/lib/prompts/lint.ts` | [MEM-OBJ-schema](#mem-obj-schema), [MEM-BAP-schema-guidance](#mem-bap-schema-guidance); requested read-dependent decisions, not demonstrated activation. |
| Index-based retrieval | `src/lib/prompts/query.ts`, `src/lib/prompts/wiki.ts` | [MEM-OBJ-index](#mem-obj-index), [RT-RTE-query-job](runtime.md#rt-rte-query-job); selector is Claude, no source-defined token/page budget. |
| Activity and coarse audit histories | `src/lib/prompts/wiki.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts` | [MEM-OBJ-log](#mem-obj-log), [MEM-OBJ-audit-log](#mem-obj-audit-log); raw event histories, not an implemented trace-to-rule pipeline. |
| Manual/automatic lint | `src/daemon/queue.ts`, `src/lib/prompts/lint.ts` | [RT-RTE-lint-job](runtime.md#rt-rte-lint-job); automatic scheduling is wired, issue diagnosis/fixes requested, no review lifecycle. |
| Job history and reasons | `src/daemon/runner.ts`, `src/daemon/db.ts`, `src/cli/commands/status.ts` | Annotation on [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs), [MEM-CLM-reason-audit](#mem-clm-reason-audit); result read by client, not automatically later model input. |
| Restart and partial effects | `src/daemon/db.ts`, `src/daemon/queue.ts` | [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery); replay consumes payload and surviving files, no clean checkpoint or full working conversation. |
| Browser/API and local files | `src/cli/client.ts`, `src/daemon/routes.ts`, `docs/operations.md` | [MEM-RTE-file-browse](#mem-rte-file-browse); external reader role documented/afforded, client-server file delivery wired. |
| Config and custom instructions | `src/daemon/runner.ts`, `src/daemon/scaffold.ts`, `src/cli/commands/config.ts` | Annotation on [RT-RTE-config-change](runtime.md#rt-rte-config-change); tool/model config reload wired, `.claude.md` discovery uninspected. |
| Credentials/opaque host state | `src/daemon/auth.ts`, `src/daemon/runner.ts` | Access metadata retained on disk and passed as environment/config directory; not wiki knowledge. Claude's other directory state and provider context policies uninspected. |
| Withdrawal and backup | `src/cli/commands/destroy.ts`, `src/cli/client.ts`, `src/daemon/server.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`, `src/daemon/db.ts`, `docs/operations.md` | [MEM-RTE-wiki-withdrawal](#mem-rte-wiki-withdrawal); DELETE body is not parsed, so the shipped keep-data option does not prevent directory deletion; scaffold preservation is an isolated capability, not an operable API choice. |
| Prompt evaluation | `docs/prompts.md`, `package.json` | [MEM-RTE-prompt-evaluation](#mem-rte-prompt-evaluation); proposed human procedure, no results or automatic release gate. |

The supplied runtime's scaffold/mount mismatch applies to every intended relative read: the model starts at `/workspace`, but seeded files and archive are under `/workspace/wiki/`. We retain requested consumers without claiming successful delivery through those literal paths. See [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job). Host filesystem aliases also qualify archive immutability and confinement; see [RT-CLM-workspace-isolation](runtime.md#rt-clm-workspace-isolation).

## Core ideas

The primary reusable result is edited text, not a vector index or a resumed conversation. Raw input, derived assertions, retrieval summaries and filing guidance have different roles and different consumers. Pages supply answer evidence; the index directs search; the schema is requested to govern future filing. Their shared markdown substrate does not give them equal authority. These distinctions are declared separately below.

Read-back is chiefly task-requested, model-directed filesystem search. The daemon selects a wiki and constructs a task; it does not calculate semantic relevance or inject selected page contents. Automatic lint is unsolicited maintenance scheduling, not unsolicited delivery of memory into an already-running foreground model. Its file selection remains requested of a fresh Claude job ([RT-RTE-query-job](runtime.md#rt-rte-query-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)).

Source links and quote preservation are requested provenance, not verification. A caller can supply misleading material; Memex checks ownership and upload shape, not source trust. Query grounding is a language instruction, while optional web/MCP capabilities can expose other inputs. No evidence here establishes reliable resistance to source instructions or correct contradiction resolution (SRC-1, `src/daemon/routes.ts`, `src/lib/prompts/wiki.ts`, `src/lib/prompts/query.ts`, `src/daemon/runner.ts`; [RT-BAP-wiki-instructions](runtime.md#rt-bap-wiki-instructions)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw source archive

Source-native identity: `wiki/raw/`. Representational form: source bytes, potentially natural-language documents, images or opaque PDF payloads; Memex stores bytes without parsing or embedding them. Storage substrate: timestamp-prefixed files under the wiki directory. Lineage: caller local file → base64 transport → decoded bytes → file. It is distinct from derived wiki pages and from the SQLite payload filename list in [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs); the closest supplied route is [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), not an object counterpart. Admission: owner upload request, daemon physical write; human versus automated supply unresolved. Later ingest is asked to read listed files, and page references afford later inspection. Sources have evidentiary authority only through model/reader interpretation, no privileged truth status. A timestamp prefix is not a content digest or provenance authentication. Source: SRC-1, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`, `src/lib/prompts/ingest.ts`.

> const buffer = Buffer.from(content, 'base64');
>     const stored = this.scaffold.writeRawFile(wikiId, filename, buffer);
> --- `src/daemon/routes.ts`

The namespace remount protects `/workspace/wiki/raw` for the intended job path, not every host alias. Archive rejection/removal is not a semantic approval workflow; model refusal does not remove uploaded bytes. Actual source handling by external Claude is uninspected.

#### MEM-OBJ-wiki-pages
Label: Derived wiki pages and connections

Source-native identity: wiki pages organized by entity and topic, with `## Related` sections and raw references. Representational form: natural-language assertions, quotes, synthesis and labeled links interpreted by Claude or readers; link syntax alone does not make semantic connection selection symbolic. Storage substrate: markdown files in `wiki/`. Lineage: requested extraction and integration of source material with existing pages. Claude is instructed to prefer updates, resolve or flag contradictions and add reciprocal links. The daemon admits direct Write/Edit effects without checking warrant or per-edit human approval. Later ingest/query/lint are requested consumers; external browsing is another consumer. Actual generated content and completeness of retained reasons are uninspected. Distinct from static [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts), and file products of [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), not duplicate route identity. Evidence: SRC-1, `src/lib/prompts/wiki.ts`, `src/lib/prompts/ingest.ts`.

> - Preserve key quotes verbatim with attribution and date
> - Include source references
> --- `src/lib/prompts/wiki.ts`

> Each wiki page should reference its raw sources: \`*Source: [raw/filename.md](raw/filename.md)*\`
> --- `src/lib/prompts/wiki.ts`

Links and preserved quotes could expose reasons/evidence to later readers, but no route requires rereading all raw support or edit reasons before using a page. They do not establish truth or measured improvement.

#### MEM-OBJ-schema
Label: Evolving filing schema

Source-native identity: `_schema.md`. Representational form: natural-language conventions, categories, vocabulary, page templates and heuristics. Storage substrate: seeded markdown at `wiki/_schema.md`. Lineage: minimal shipped placeholder followed by requested model revision against encountered material and filing patterns; initialization is known, realized content is not. It differs from static [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts) and their instruction to maintain it. [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) already assesses the revision route; this record identifies its retained product. Evidence: SRC-1, `src/daemon/scaffold.ts`, `src/lib/prompts/ingest.ts`, `src/lib/prompts/wiki.ts`, `src/lib/prompts/lint.ts`.

> writeFileSync(join(base, 'wiki', '_schema.md'), DEFAULT_SCHEMA_MD);
> --- `src/daemon/scaffold.ts`

> The schema is your institutional memory. If you learned something from this ingest — a new convention, a refinement, a pattern — write it down. Vocabulary, heuristics, page templates, lifecycle stages, things to ignore. The schema should get richer with every ingest, not just when new categories appear.
> --- `src/lib/prompts/ingest.ts`

Authorship/curation is delegated to Claude; tool effects admit revisions directly. A human starting ingest is not approving each convention. Subsequent ingest is asked to read this schema and lint to compare actual patterns against it. Persistence across sessions is afforded by files. The prompt calls it institutional memory but does not establish improved capacity, actual content-directed criticism or consumer dependence. Reasons for conventions are not a required schema field; ingest reasons are a separate output. Addressability of generated content is uninspected. Theory-builder conditions 1–4 remain claimed at the instruction layer as scoped in the supplied ingest/lint routes, not observed here; learning and realized reflection remain uninspected independently.

#### MEM-OBJ-index
Label: Semantic page index

Source-native identity: `_index.md`. Representational form: natural-language one-line summaries plus paths and connection counts. Storage substrate: seeded then model-maintained markdown at `wiki/_index.md`. Lineage: summaries derived from affected pages under ingest and corrected under lint. Consumer: later query and ingest are asked to orient from it; lint checks accuracy. Authority: search/navigation guidance to a model or reader, not answer validation. Counts and paths are displayed text; no Memex scorer consumes them. Separate from [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts) and distinct from the schema's filing guidance. Source: SRC-1, `src/daemon/scaffold.ts`, `src/lib/prompts/wiki.ts`, `src/lib/prompts/query.ts`, `src/lib/prompts/lint.ts`.

> ALWAYS keep _index.md current. Every wiki page gets a one-line summary: what it contains, how many connections, what matters most. Organize by category. A reader should understand the shape of the entire knowledge base by reading only the index.
> --- `src/lib/prompts/wiki.ts`

The index is a requested compressed retrieval map, not a replacement checkpoint for the model's working context. No maximum index length, automatic eviction or complete delivery assurance is specified.

#### MEM-OBJ-log
Label: Wiki activity log

Source-native identity: `_log.md`. Representational form: natural-language dated operation summaries. Storage substrate: seeded `wiki/_log.md`, appended by requested Claude writes. Lineage: requested ingest/lint/query descriptions, not captured tool events. Later consumers: lint's all-markdown read request and optional filesystem/API readers; ingest/query do not explicitly require prior-log reading. Authority: historical evidence to readers, not a fixed admission or filing rule. It is distinct from daemon audit rows and from the returned result in [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs). Evidence: SRC-1, `src/daemon/scaffold.ts`, `src/lib/prompts/wiki.ts`, `src/lib/prompts/lint.ts`.

> After completing any operation, append an entry to _log.md:
> --- `src/lib/prompts/wiki.ts`

This is a requested durable trace summary, not an implemented trace-fed schema update. The ingest instruction instead asks reflection on current filing patterns; it does not explicitly transform earlier log entries into rules.

#### MEM-OBJ-audit-log
Label: Daemon audit events

Source-native identity: SQLite `audit_log`. Representational form: symbolic IDs, timestamps and action names consumed by fixed display/order rules, with text detail interpreted by readers. Storage substrate: `memex.db`. Lineage: fixed route/queue event writes. Consumers: API logs and CLI display, not the model prompt builder. No approval/warrant authority is carried by an audit event. Distinct from queue rows in [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs), whose record mentions but does not include audit rows, and from the wiki log. Evidence: SRC-1, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon/routes.ts`, `src/cli/commands/logs.ts`.

> this.db.logAudit(wikiId, `job.${job.type}.completed`, `job #${job.id} (${result.duration_ms}ms)`);
> --- `src/daemon/queue.ts`

This records lifecycle success determined by exit code, not per-edit reasons, tool traces or verified content changes. API retrieval defaults to fifty events; the logs handler does not forward the client's `limit` query to the database. CLI reverses received entries for chronological presentation; neither display nor that reorder curates knowledge.

### Routes

#### MEM-RTE-file-browse
Label: Retained file browsing

Endpoints/progression: owner client request → wiki ownership gate → directory listing or UTF-8 file read → JSON response → client reader. Owner: caller chooses wiki/prefix/path, fixed daemon code delivers; external human/automation interpretation uninspected. State effects: no file write in these handlers. Unlike [RT-RTE-query-job](runtime.md#rt-rte-query-job), this route delivers retained content without model synthesis. It exposes storage through a shipped client/server pair; actual third-party client usage remains unobserved. SRC-1, `src/cli/client.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`, `docs/operations.md`.

- Immediate return: file/directory entries or requested file content in response.
- Later read-back: existing wiki files, including raw archive paths, can be read in later client requests; local operator file viewing is also documented.
- Delegated visibility: inapplicable — no Claude delegation by these handlers.
- Selection predicate: caller-selected exact path or directory prefix, not semantic relevance selection; listings skip dot-prefixed names and sort directories first then alphabetically.
- Invalidation or expiry: overwrite/removal changes returned bytes; successful shipped deletion removes registration and the directory even when keep-data is requested, preventing normal API read-back and deleting retained file inputs.
- Activation or effect: wired content delivery; changed reader behavior uninspected.
- Evidence limits: no external reader trace; UTF-8 decoding is not faithful interpretation of every binary source format, and path checking is not a demonstrated security guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const content = this.scaffold.readWikiFile(wikiId, filePath);
>     return { status: 200, body: { ok: true, data: { path: filePath, content } } };
> --- `src/daemon/routes.ts`

#### MEM-RTE-wiki-withdrawal
Label: Wiki deletion and retained-data withdrawal

Endpoints/progression: CLI keep-data selection → client DELETE with JSON body → server omits DELETE body parsing → ownership-gated handler receives undefined body and selects keepData=false → scaffold directory removal → registry deletion and foreign-key cascades → acknowledgment. Owner: caller requests whole-wiki withdrawal, daemon admits authorized request and executes; the caller's preservation choice does not reach the handler. Human identity unresolved; this is not content criticism or candidate comparison. Proposed change: remove registration/history and, unless keep-data is selected, files; actual shipped route selects file deletion regardless of that option. Rejection: ownership check; rollback: external backup/reconstruction, no built-in version restore. Guidance: lifecycle options and backup instructions, not an answer oracle. Operating mode: direct administrative request. Distinct from job replay in [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery), and from configuration replacement in [RT-RTE-config-change](runtime.md#rt-rte-config-change). SRC-1, `src/index.ts`, `src/cli/commands/destroy.ts`, `src/cli/client.ts`, `src/daemon/server.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`, `src/daemon/db.ts`, `docs/operations.md`.

- Immediate return: successful deletion acknowledgment after scaffold/DB operations; CLI prints data preserved when its local keep-data option is set, without checking preservation.
- Later read-back: normal job/file API read-back ceases with registry deletion; successful shipped deletion also removes the wiki directory, so keep-data does not retain files for local readers or recovery. External backups remain separate.
- Delegated visibility: inapplicable — no model delegated by the delete handler.
- Selection predicate: caller's wiki ID; handler keepData defaults false because server passes no DELETE body, not the caller's requested boolean. No claim-specific expiry or semantic retraction.
- Invalidation or expiry: directory deletion removes retained files/configuration even with the shipped keep-data option; subsequent registry deletion cascades queue/audit rows.
- Activation or effect: wired destructive removal, not wired keep-data preservation; no coordinated cancellation of already-active Claude work in this handler.
- Evidence limits: source-level transport defect, not an observed deletion run; no concurrent deletion trace, transactional filesystem rollback or verified revocation of content already read by a child. Filesystem errors can interrupt this progression before registry deletion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> this.scaffold.destroy(wikiId, keepData);
>     this.db.deleteWiki(wikiId);
> --- `src/daemon/routes.ts`

> return this.request('DELETE', `/wikis/${id}`, { keepData });
> --- `src/cli/client.ts`

> let body: unknown = undefined;
> if (method === 'POST' || method === 'PUT') {
>   body = await readBody(req);
> }
> --- `src/daemon/server.ts`

> const keepData = body && typeof body === 'object' && 'keepData' in body
>   ? Boolean((body as { keepData: unknown }).keepData)
>   : false;
> --- `src/daemon/routes.ts`

> if (keepData) return;
> --- `src/daemon/scaffold.ts`

The last passage establishes only a scaffold capability when directly supplied true. The registered HTTP route is DELETE, and the server passes its unparsed body onward; neither a custom HTTP caller sending a body nor a query parameter delivers keepData to this handler. No alternate preservation endpoint appears in the inspected route registry. The CLI's confirmation and terminal message nevertheless describe preservation from its local option:

> console.log(`Destroyed wiki '${wikiId}'${opts.keepData ? ' (data preserved)' : ''}`);
> --- `src/cli/commands/destroy.ts`

This can mislead an operator about destructive data loss; the isolated scaffold branch does not support an affirmative shipped preservation finding.

#### MEM-RTE-prompt-evaluation
Label: Sequential prompt evaluation procedure

Endpoints/progression: maintainer-selected sources → proposed sequential ingests → qualitative per-source checks and final wiki inspection → possible prompt tuning and iteration documentation. Owner/proposer/admitter: maintainer, not a wired automated evaluator. Trigger: prompt development/use; proposed change: source prompt text. Human judgments can decline changes in practice, but no enforced release veto is shipped. Rollback: source editing or external backup, not a workflow operation here. Operating mode: bounded proposed corpus of five to ten sources. Answer oracle: qualitative expectations listed in the document, no exact expected-answer corpus supplied. Distinct from runtime [RT-RTE-lint-job](runtime.md#rt-rte-lint-job); it concerns product prompt development, not automated wiki maintenance. Closest overlap is the source-prompt-development passage of [RT-RTE-config-change](runtime.md#rt-rte-config-change), not the per-wiki config operation. Source: SRC-1, `docs/prompts.md`, `package.json`.

- Immediate return: inapplicable — documentation procedure, not an implemented callable evaluator.
- Later read-back: sequential sources are supposed to encounter earlier pages/schema; document iterations alongside wiki for possible future maintainers.
- Delegated visibility: proposed ordinary ingest inputs and retained wiki; no special evaluation context wired.
- Selection predicate: maintainer chooses varied new/returning/contradictory/vague sources and assesses the listed structural/readability expectations.
- Invalidation or expiry: uninspected — no implemented evaluation artifact or acceptance lifecycle.
- Activation or effect: requested prompt tuning, not demonstrated adoption or benefit.
- Evidence limits: no evaluation corpus/results, automatic test entry point or documented live successor comparison supplied.
- procedure conclusion status: claimed
- operation conclusion status: uninspected

> **Sequential processing.** Process sources in order, building up the knowledge base. Does the 5th source correctly reference pages created by the 1st?
> --- `docs/prompts.md`

> Document iterations alongside your wiki. The prompt is the product.
> --- `docs/prompts.md`

### Claims

#### MEM-CLM-reason-audit
Label: Edit reasons entering audit history

Claimed operation: prompt documentation says structured ingest reasons flow into audit log and explain wiki evolution. Source: SRC-1, `docs/prompts.md`. The inspected implementation retains model result text in job results but writes only coarse lifecycle details to SQLite audit. The wiki log is separately requested to summarize activity and affected pages, not guaranteed to retain each reason. This distinguishes reason-bearing content from lifecycle metadata in [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs) and [MEM-OBJ-audit-log](#mem-obj-audit-log). No supplied claim record has this referent.

> These reasons flow into the audit log and become a narrative of how the knowledge base evolved.
> --- `docs/prompts.md`

The counter-witness is the completion audit quote in [MEM-OBJ-audit-log](#mem-obj-audit-log) and direct result persistence in `src/daemon/db.ts`. Reasons may survive in a successfully generated ingest output, available through status, without becoming parsed per-operation audit records or future model input. This qualifies the documentation rather than denying reason retention capability.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-schema-guidance
Label: Retained schema guiding later filing

Consumer: Claude in a later ingest, and maintenance Claude comparing current files to conventions. Channel: requested file reads under task instructions, not daemon-injected schema contents. Force: natural-language filing guidance interpreted by the model; not a fixed validator or admission invariant. Horizon: files can persist across jobs and sessions until overwritten/deleted. Distinct from static system/task authority in [RT-BAP-wiki-instructions](runtime.md#rt-bap-wiki-instructions); retained product is [MEM-OBJ-schema](#mem-obj-schema). Source: SRC-1, `src/lib/prompts/ingest.ts`, `src/lib/prompts/lint.ts`.

> 2. Read _schema.md for current conventions (create it if it doesn't exist — this is a new knowledge base).
> --- `src/lib/prompts/ingest.ts`

The request establishes a behavior-shaping opportunity for retained conventions. Actual file delivery, decision dependence and improvement are uninspected, especially given the working-directory mismatch. No exercised self-improvement attribution follows from the label institutional memory.

## Annotations

#### On [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs)

Memory parts: payload includes filename lists or question/history text; result can include an ingest operation array with reasons, a query answer, lint criticisms/fixes or error text. SQLite preserves the outer result envelope; the runner first extracts Claude's `result` text and may normalize valid inner JSON. Other Claude envelope fields are not intentionally copied into the successful result. This is not a full tool/conversation trace. Source: SRC-1, `src/daemon/runner.ts`, `src/daemon/db.ts`, `src/lib/prompts/ingest.ts`.

> const text = envelope.result ?? '';
> --- `src/daemon/runner.ts`

> output = JSON.stringify(JSON.parse(text));
> --- `src/daemon/runner.ts`

Later consumers: status prints stored output/error, clients poll rows, restart replay consumes pending payload. The model prompt builder does not fetch earlier completed results; later history is caller-supplied instead. Thus model-written reasons and unresolved lint criticisms are retained for API/CLI readers without an automatic later-model route. Source: SRC-1, `src/cli/commands/status.ts`, `src/cli/client.ts`, `src/daemon/runner.ts`, `src/lib/prompts/query.ts`.

#### On [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)

Read-back selection inputs: source filename list, requested schema/index reads, names/topics/themes searched across existing pages. Selected retained content: raw source bytes, conventions, navigation summaries and model-selected existing pages. Persistence: direct edits survive process exit irrespective of later success recording. Delivery: filesystem tools, not a daemon assembled context packet. Budget: twenty-five turns and five-minute runner timeout; these are work limits, not token-level context or selected-page budgets (SRC-1, `src/lib/constants.ts`, `src/daemon/runner.ts`). Requested curation includes extraction, page integration and reciprocal links. Schema revision is requested from source and current filing experience, not an explicit historic-log summarizer. Raw-to-derived-to-next-consumer chain is archive → model-produced pages/index/schema → later query/ingest/lint read requests. The source prompt and supplied route preserve the defining passages; actual execution remains uninspected.

#### On [RT-RTE-query-job](runtime.md#rt-rte-query-job)

Selection is task-requested index → grep/glob → chosen pages → synthesized answer. Retained input is not pushed independently by an automatic relevance selector. Authority at consumer is evidence for answers plus explicit grounding rules; no truth-enforcing constraint. Budget: fifteen turns, two minutes; no token/page budget or history trimming defined by Memex. API history is appended verbatim, CLI supplies only question, and job results are not automatically recovered as conversation history. A query may append a log and has Write/Edit access, but the saving suggestion is not a wired answer-adoption transaction. SRC-1, `src/lib/prompts/query.ts`, `src/cli/commands/query.ts`, `src/lib/constants.ts`, `src/daemon/runner.ts`.

#### On [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)

Requested selection: all markdown excluding raw; selector Claude diagnoses with pages/schema and current date. Automatic trigger inputs are in-memory successful-ingest count, not semantic quality or retained issue reports. Budget: thirty turns/ten minutes; no maximum wiki size or guaranteed complete scan. Direct changes to index/links/schema persist and can influence later jobs. Contradiction/merge/stale-fact criticisms persist in returned report for readers; no automatic injection of that report or approve-and-apply API is shipped. Policy asks model not to edit human-judgment issues; identical file-write tools do not enforce that partition. SRC-1, `src/daemon/queue.ts`, `src/lib/constants.ts`, `src/lib/prompts/lint.ts`, `src/daemon/runner.ts`.

#### On [RT-RTE-config-change](runtime.md#rt-rte-config-change)

Retained parts have different consumers: natural-language `.claude.md` intended for Claude discovery, symbolic allowed-tool lines filtered by runner, SQLite model string consumed as invocation argument, and JSON MCP configuration passed by path to external Claude. Scaffold supplies the known default customization text; actual edits and MCP contents are absent. CLI editing lets a caller replace content through an editor, not an approval of model-generated edits. Tool/model config reload is wired; custom instruction read-back and MCP capabilities are uninspected externally. No explicit runner call to `readClaudeMd` injects that file. SRC-1, `src/daemon/scaffold.ts`, `src/cli/commands/config.ts`, `src/daemon/runner.ts`, `src/daemon/routes.ts`.

Credential tokens and JSON files in `.claude/` are symbolic access metadata. They authorize external services, not wiki assertions. Per-wiki token → credential-file presence → global token defines precedence. Provider-managed auxiliary state under the config directory has unresolved format, provenance and later consumers; a configured directory alone does not establish conversation compaction or knowledge learning (SRC-1, `src/daemon/auth.ts`, `src/daemon/runner.ts`).

#### On [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery)

Replay receives retained task payload, current config and surviving files, not the prior working context or a reasoned checkpoint. The prior result, if any, is not an input to prompt construction. No file-effect transaction ties restored pending state to a clean wiki. Alternative checkpoint forms are therefore limited to existing payload/files and opaque external host state, whose checkpoint semantics are uninspected. SRC-1, `src/daemon/db.ts`, `src/daemon/runner.ts`; supplied route establishes reset and recovery wiring.

## Write side

Acquisition and semantic admission are separate. The upload endpoint admits owner-supplied bytes and writes them before an ingest job. Claude then authors/adopts derived content with pre-approved file tools; the daemon gates request ownership and job type but does not verify page contents or approve each change. The archive may remain even if ingestion fails or the model chooses not to incorporate it ([MEM-OBJ-raw](#mem-obj-raw), [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)).

Source integration requests extraction, contradiction handling, merging into existing pages and provenance references. These are model-curation instructions, not observed transformations. Pages and links retain evidence and relationships when the model follows them; operation reasons are requested as JSON output and survive through job results when produced. Nothing requires each schema rule to retain its historical reason or a later agent to consume that reason ([MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-OBJ-schema](#mem-obj-schema), [MEM-CLM-reason-audit](#mem-clm-reason-audit)).

Maintenance has two materially different outputs: direct structural edits become later filesystem inputs, while unresolved criticisms become a returned report. Automatic lint scheduling is code-wired after ten exit-success ingests in current queue state, reset at restart; it does not prove ten successful integrations. The report's human-review request is not a retained approval lifecycle. No semantic rejection/rollback guard covers already-made edits. Documentation proposes qualitative prompt evaluation rather than delivering evaluation evidence ([RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [MEM-RTE-prompt-evaluation](#mem-rte-prompt-evaluation)).

Requested schema evolution is a trace-related behavior-shaping update based on newly processed content and filing patterns. The original inputs are mixed supplied sources and current wiki organization; no instrumented trace-to-schema transformer is implemented. Logs retained alone do not establish this update. File-based persistence affords future use of the result, but execution, criticism, learning and improvement are separate unresolved properties ([MEM-OBJ-schema](#mem-obj-schema), [MEM-OBJ-log](#mem-obj-log), [MEM-BAP-schema-guidance](#mem-bap-schema-guidance)).

Withdrawal is whole-wiki deletion or local file editing, not a shipped claim-by-claim retract-and-propagate mechanism. The shipped keep-data choice is lost between client and handler because DELETE bodies are not parsed. On successful deletion, files are removed and queue/audit history cascades away; scaffold's direct keepData=true preservation branch is not an operable client/API option. Concurrent children are not cancelled by the handler. External backups are suggested, not an automatic revision journal ([MEM-RTE-wiki-withdrawal](#mem-rte-wiki-withdrawal), [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery)).

## Read-back

The daemon chooses the wiki/task frame and Claude is requested to choose files. Ingest selects by source list and related terms; query by question/index/search; lint asks for all non-raw markdown. There is no source-defined relevance-score threshold, token budget or compaction policy in the inspected prompt builder/runner. Turn limits/timeouts bound work, not retrieval completeness. Delivery of file content and its activation remain external-model dependent ([RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-query-job](runtime.md#rt-rte-query-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)).

Every job spawns a fresh process without passing a resume identifier. Prior model turns/tool results are kept out of the newly constructed Memex invocation; selected task text, supplied API history, static policy and accessible files cross in. At return, normalized answer/result and filesystem effects escape, not a full working conversation. This resembles a per-task frame with a restricted return value, but differs because filesystem side effects outlive it and external Claude can manage opaque state. No Memex reference-count/liveness mechanism determines which retained files matter; they remain reachable until edited/deleted. Internal Claude trimming, summarization and reloading remain uninspected (SRC-1, `src/daemon/runner.ts`, `src/lib/prompts/query.ts`; [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery)).

Clients can later read file contents or job output; documented operators can browse disk directly. These are separate external-reader routes, not hypothetical model consumers inferred from a storage method. Job history, error text and lint reports influence later model work only if a caller manually supplies them or writes relevant files; that transfer is not wired here ([MEM-RTE-file-browse](#mem-rte-file-browse), annotation on [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs)).

Configuration uses a fixed runner selector on each job for tool names and model, with MCP delivery by path. Custom convention discovery is declared by Memex but not implemented by its runner. Access metadata must not be mistaken for knowledge content. Page facts have answer-evidence authority; schema has requested filing authority; tool configuration has computational grant-selection authority. Delivery does not establish reliable model compliance ([MEM-BAP-schema-guidance](#mem-bap-schema-guidance), [RT-RTE-config-change](runtime.md#rt-rte-config-change), [RT-BAP-wiki-instructions](runtime.md#rt-bap-wiki-instructions)).

## Integration issues

1. Documentation correction: edit reasons do not flow into SQLite audit through the inspected queue path. They can persist in job output, while wiki activity log summaries are requested separately. This is a source-document discrepancy consistent with runtime's coarse-audit finding, not a correction to runtime. Consequence: no automatic reason-to-rule or per-edit audit lineage should be inferred. Evidence and records: [MEM-CLM-reason-audit](#mem-clm-reason-audit), [MEM-OBJ-audit-log](#mem-obj-audit-log), [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs).
2. Potential overlap: [MEM-RTE-prompt-evaluation](#mem-rte-prompt-evaluation) expands the prompt-development portion of [RT-RTE-config-change](runtime.md#rt-rte-config-change). It concerns a separate proposed evaluation procedure, not per-wiki configuration; reconciliation should preserve that scope distinction. Other new objects/authority paths have distinct identities stated beside their closest supplied records; no other possible duplicate was found.
3. Relative-path mismatch is unresolved at execution: no evidence establishes whether Claude discovers `wiki/` and compensates or creates parallel root-level files. Consequence: do not upgrade requested wiki/schema read-back to observed activation. [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-query-job](runtime.md#rt-rte-query-job), [MEM-BAP-schema-guidance](#mem-bap-schema-guidance).
4. `.claude.md` discovery, configured MCP behavior and external host checkpoints remain uninspected. Consequence: configuration delivery is not full instruction activation/context-management evidence. [RT-RTE-config-change](runtime.md#rt-rte-config-change), [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery).
5. Lint report criticism has no automatic later-model consumer or approval workflow, and schema reasons are not required fields. Consequence: retain requested revision/persistence separately from demonstrated criticism iteration or learning. [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [MEM-OBJ-schema](#mem-obj-schema), [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs).
6. Withdrawal correction: the previous memory report incorrectly described keep-data as an operable preservation choice. Direct caller-to-handler inspection shows the client sends a DELETE body, the server parses only POST/PUT bodies, and the handler therefore selects false before scaffold deletion. Coverage, route progression, read-back, invalidation and Write side now reflect destructive deletion even with keep-data. The CLI's preservation message and operations documentation are misleading; scaffold's true branch is only an isolated capability. See [MEM-RTE-wiki-withdrawal](#mem-rte-wiki-withdrawal) for SRC-1 paths and passages. This corrects this member, not a supplied runtime record.
7. Archive immutability and deletion withdrawal are path/lifecycle qualified, not verified universal revocation: host aliases survive namespace setup and deletion does not cancel active children. [RT-CLM-workspace-isolation](runtime.md#rt-clm-workspace-isolation), [MEM-OBJ-raw](#mem-obj-raw), [MEM-RTE-wiki-withdrawal](#mem-rte-wiki-withdrawal).

No supplied runtime record requires factual correction on the inspected memory mechanisms. The keep-data correction repairs this member's previous preservation finding; the other issues remain bounded unknowns/source-claim qualifications, not a changed frozen boundary.

## Limitations and checks

Git HEAD was rechecked as `1e223b6045be31b70b1ab9e4b28dd403150d29e7` and status was clean. Source identity agrees with the supplied boundary; the supplied method/type/worker/records files were read completely, recovering trailing ranges. All added evidence remains SRC-1 at that commit. No prohibited prior analysis, target execution, external service or additional source was used.

This account establishes source wiring and requested model behaviors, not successful ingestion, trustworthiness, improved retrieval, complete context scans, reliable recovery or exercised self-improvement. No full model working-context or generated wiki was available. Deterministic validation is recorded after running the invocation's output validator; its pass establishes form, source quotation occurrence and invocation consistency, not semantic acceptance.

Validation: passed using the supplied `commonplace-run validate-output` invocation.
