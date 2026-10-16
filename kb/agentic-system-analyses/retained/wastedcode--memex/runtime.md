---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Memex runtime baseline tracing Unix-socket admission, per-wiki jobs, delegated Claude work and control limits at the frozen commit."
run-id: AAS-2026-10-14-memex-42ecde52cc05-01
reviewed-boundary: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
---

# Memex runtime report

## Runtime account

Memex ships a Node CLI and exported Unix-socket client backed by a privileged daemon. Its consequential work is asking Claude Code to integrate sources into persistent markdown, answer from that wiki and maintain its structure. The daemon schedules and records work; the external Claude process chooses reads, synthesis and edits. The runtime does not itself implement semantic retrieval or validate the resulting wiki. This is an implementation account of SRC-1 at the [frozen boundary](boundary.md), not supplied execution evidence. Operation, prompt compliance, quality and benefit remain uninspected.

### Ordinary invocation and ownership

The package binary points to `dist/index.js`; `src/index.ts` registers `serve`, lifecycle/configuration, authentication, ingest/query/lint and monitoring commands. The exported `./client` supplies `MemexClient`. `serve` initializes SQLite, resets stale jobs, checks mount capability, creates the namespace target, starts the socket server and drains pending queues (SRC-1, `package.json`, `src/index.ts`, `src/daemon.ts`). This inspection covers these shipped entry paths, not published package bytes.

For an ordinary `memex ingest <wiki> <files...>`, the client checks local file existence, uploads each file as base64, receives stored filenames, then submits an ingest payload. The caller is a local process identified by the kernel socket UID, not by a claimed JSON identity. Creation stores that UID as `owner_uid`; wiki-specific routes require equality. Wiki ID and job ID are separate identities: queue jobs carry `wiki_id`, and job lookup checks that association. Root has an explicit ownership-transfer exception but no general exception in `requireWiki`. The UID does not establish whether the principal is a human or automation (SRC-1, `src/cli/commands/ingest.ts`, `src/cli/client.ts`, `src/daemon/server.ts`, `src/daemon/routes.ts`, `src/daemon/peercred.c`).

The upload writes directly through the daemon, outside the job queue. Submission creates a durable pending row and notifies an in-memory per-wiki drain loop. That loop claims the oldest pending job atomically and awaits its runner. Distinct wikis can drain concurrently; one drain loop serializes jobs for a wiki within that daemon. The runner builds a natural-language task, resolves credentials and current tools/model, mounts the wiki, then spawns fresh `claude -p`. No conversation-resume/session identifier is passed. Ingest asks Claude to read sources, schema, index and related pages, make edits, update connections and reflect on conventions. File tools execute the effects; the daemon neither stages a proposed patch nor waits for human per-edit approval. See [RT-RTE-ingest-job](#rt-rte-ingest-job).

The terminal runner result is stdout transformed from Claude's JSON envelope when parsable, with raw-text fallback. Exit code zero determines success, not valid operation JSON, completed file writes, citations or link correctness. The queue persists the result and a coarse audit action. CLI polling then prints `output`, or reports failure. Asynchronous CLI invocation instead returns the job ID; API wait mode polls for up to ten minutes and can return a still-active job. CLI polling has no corresponding deadline (SRC-1, `src/daemon/runner.ts`, `src/daemon/queue.ts`, `src/daemon/routes.ts`, `src/cli/client.ts`).

> success: code === 0,
> --- `src/daemon/runner.ts`

A material path inconsistency prevents treating this source trace as evidence of a successful ingest: the mount wrapper changes to the wiki root `/workspace`, while scaffolded content is in `/workspace/wiki/`. Task prompts use `raw/`, `_schema.md` and `_index.md` relative to the current directory. Memex does not add a subsequent `cd wiki`. Claude may discover and compensate for the layout, but that is unobserved; literal prompt execution would not reach the scaffolded paths (SRC-1, `src/daemon/namespace.ts`, `src/daemon/scaffold.ts`, `src/lib/prompts/ingest.ts`, `src/lib/prompts/query.ts`).

> `cd ${shellEscape(WORKSPACE_MOUNT)}`,
> --- `src/daemon/namespace.ts`

> writeFileSync(join(base, 'wiki', '_schema.md'), DEFAULT_SCHEMA_MD);
> --- `src/daemon/scaffold.ts`

> 2. Read _schema.md for current conventions (create it if it doesn't exist — this is a new knowledge base).
> --- `src/lib/prompts/ingest.ts`

### Alternate and forcing cases

Four source-level forcing cases qualify stronger product claims; none was executed.

1. **Direct socket client versus ordinary CLI.** A caller can submit jobs without the CLI's file-upload sequence, provide query history or use server wait mode. `submitJob` checks the job type and outer object, not a typed payload schema. Malformed ingest payloads can fail during prompt construction. File browsing and raw upload use host-side scaffold methods, not Claude's tool restrictions. Most wiki operations check ownership, but `POST /auth/token` has no caller-UID authorization: any connected local principal can replace the global fallback token. This is not a bypass of `requireWiki`; it is a separate admission path (SRC-1, `src/cli/client.ts`, `src/daemon/routes.ts`, `src/daemon/auth.ts`).

2. **Absolute filesystem access versus instructed relative paths.** `unshare -m` changes mount namespace, not filesystem root. The script binds the wiki and a read-only raw mount, but does not remove host mounts, chroot or pivot root. The original wiki host path remains a distinct access path not made read-only by the raw bind remount. This invalidates an unconditional claim that only `/workspace` is visible or that raw bytes cannot be changed by any process with sufficient host permissions. The shipped service supplies `CAP_SYS_ADMIN`, has `NoNewPrivileges=no`, specifies no `User`, and lacks the `ProtectSystem=strict` documented in operations. The deployed UID, filesystem permissions and any additional service hardening are not supplied (SRC-1, `src/daemon/namespace.ts`, `systemd/memex.service`, `docs/operations.md`). See [RT-CLM-workspace-isolation](#rt-clm-workspace-isolation).

3. **Extra tools and MCP versus base file tools.** The actual base grant is Read/Write/Edit/Glob/Grep; opt-in extras are NotebookEdit/WebFetch/WebSearch. Bash in the README example is discarded by `resolveTools`. Both `--tools` and `--allowedTools` receive the filtered grant; enforcement is external Claude Code's contract. If `.tools/mcp.json` exists, it is passed as MCP configuration without Memex validation or inspection of its commands/services. That configuration can describe subprocess or remote capabilities; whether Claude exposes or permits them with the supplied flags is uninspected. Memex does not supply an independent remote-effects guard. No separate direct provider-call branch is present in the inspected runner; all three job types share this delegation path (SRC-1, `src/daemon/runner.ts`, `src/lib/constants.ts`, `README.md`). See [RT-RTE-config-change](#rt-rte-config-change).

4. **Daemon restart versus exactly-once file effects.** Startup requeues every running row and increments retries, but does not roll back markdown effects already performed by the prior child. A job can be replayed after partial or completed edits if result recording was interrupted. Serialization is not a filesystem transaction and does not cover uploads, local editors or external processes. The timeout sends SIGTERM to the tracked child; its SIGKILL branch tests `child.killed`, which reports signal sending rather than confirmed exit. There is no explicit process-group termination or guarantee for MCP descendants. These are implementation limits, not observed failures (SRC-1, `src/daemon.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts`). See [RT-RTE-job-recovery](#rt-rte-job-recovery).

### Guarantees and their limits

| Load-bearing guarantee | Owner and enforcement point | Strength and covered paths | Alternate path / external contract | Conclusion statuses |
|---|---|---|---|---|
| Wiki API ownership | Daemon; kernel peer credential extraction and route `requireWiki` | invariant for inspected wiki-specific handlers requiring equality; chown has explicit owner/root rule | Global-token route lacks this gate; direct filesystem edits and Claude effects are outside it. Requires Linux SO_PEERCRED and working native addon. | implementation conclusion status: wired; operation conclusion status: uninspected |
| One queued job per wiki in a daemon | QueueManager active flag, awaited runner and atomic SQL claim | protocol for that daemon's job drain | Uploads/config/editor writes are not serialized here; multiple daemons/deployments unobserved. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Restricted tool grant | Runner builds `--tools` and `--allowedTools`; whitelist filters extras | policy delegated to Claude Code for job tools | MCP semantics, tool implementation and host filesystem access need external enforcement; not a deployed sandbox guarantee. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Read-only raw mount | NamespaceManager's bind remount before exec | deployment guarantee conditional on Linux mount success and use of that mount path | Uploads deliberately write the archive; original host-path alias and privileged child access are not eliminated. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Grounded answers, maintained index and links | Claude; appended system and task instructions | policy, not daemon-checked invariant | Same file-write grant for queries; optional web tools and MCP can enlarge inputs. Requires model compliance. | implementation conclusion status: wired; operation conclusion status: uninspected |

The table describes enforcement scope, not verified security. The strongest source-native visibility claim is retained as a claim record rather than adopted as an invariant.

### Context, admission and observability

Each job gets its own spawned process, a freshly built task and the same appended wiki system text. The selected wiki's files remain accessible for model-directed reads; credentials are remapped under `/workspace/.claude`, HOME is `/workspace`, and only PATH/LANG/LC_ALL/TERM/NODE_ENV plus resolved credentials are copied. This is per-job working-context isolation at the invocation boundary, not evidence of how Claude internally trims or summarizes its context. The subprocess frame returns stdout/stderr and durable file side effects, not its full working conversation. Query payload history is copied verbatim when supplied; the shipped CLI does not supply history. Memex implements no own token-based trimming or compaction in this path (SRC-1, `src/daemon/runner.ts`, `src/lib/prompts/query.ts`, `src/cli/commands/query.ts`).

Ingest and lint admit retained file changes directly through the model's pre-approved tools. Query also receives Write/Edit and the system instruction to append an activity log; it is not a read-only execution mode. Model directives about confidence or human judgment do not create an approval callback. The query prompt suggests that new synthesis *could* be saved; it does not implement a distinct save-answer workflow. Memory revision and semantic warrant assessments belong to the later specialists; the routes below establish who can propose/admit changes and what the runtime enforces.

Capability/configuration changes can be admitted by an owner API request for tools/model, by local editing of `.claude.md`, or by writing `.tools/mcp.json` on disk. The latter files are within the writable wiki root and not separately mounted read-only; protection from model writes is not established. The runner reads tool/MCP state again per job. Core product prompt changes instead require source edits and rebuild/redeployment; `docs/prompts.md` supplies qualitative sequential evaluation guidance, not a tested automated release gate. No target execution or evaluation results were supplied (SRC-1, `src/cli/commands/config.ts`, `src/daemon/routes.ts`, `src/daemon/runner.ts`, `src/daemon/scaffold.ts`, `package.json`, `docs/prompts.md`).

SQLite stores queue payloads, statuses, results and audit entries. Audits record submission/completion/failure IDs and coarse timing/errors; operation reasons stay in returned output, not parsed per-edit audit records. The runner buffers all stdout/stderr, logs the first 500 stderr characters and has no semantic verifier before success admission. In-memory ingest counters reset on daemon restart, so automatic lint is after ten successful ingests counted in that queue state, not a persistent lifetime total (SRC-1, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts`).

All added inspection stays within SRC-1 and the frozen commit: entry/client, server/native identity, routes/scaffold/auth, queue/database/startup, runner/namespace/constants, all four prompts, CLI ingest/query/config, package, service, README and prompt/operations docs. These supply implementation and doctrine/design only. External model parameters, Claude tool semantics and live deployment remain uninspected.

## Shared records

### Components

#### RT-CMP-claude-model
Label: Claude model behind delegated jobs

Source-native identity: Claude selected by the per-wiki `default_model`, falling back to `sonnet`. Representational form: distributed-parametric. Storage substrate: external provider/model infrastructure, not the Memex wiki or SQLite. Each inspected job delegates to the Claude Code executable. Parameters changing during operation are uninspected: Memex supplies no parameter-update operation, but provider internals are outside the boundary. Exact model version is not pinned by the shipped default alias. A mutable provider alias or operator model configuration can resolve to another model; endpoint resolution and exact weights are uninspected (SRC-1, `src/daemon/runner.ts`, `src/lib/constants.ts`, `src/daemon/db.ts`).

> const model = wiki?.default_model ?? DEFAULT_MODEL;
> --- `src/daemon/runner.ts`

> export const DEFAULT_MODEL = 'sonnet';
> --- `src/lib/constants.ts`

### Operative objects

#### RT-OBJ-queue-jobs
Label: Durable queue and result rows

Source-native identity: SQLite `queue_jobs`. Representational form: symbolic columns and JSON envelopes consumed by fixed scheduler/status rules; natural-language task content and answer text are embedded payload/result parts interpreted by Claude or users. Storage substrate: `memex.db`, WAL-enabled. Job ID/wiki ID/status govern claiming and result access, not truth admission. Payload and results survive daemon restart and are polled by clients. Audit rows are a separate coarse event history, not model tool traces (SRC-1, `src/daemon/db.ts`, `src/daemon/routes.ts`, `src/cli/client.ts`).

> payload TEXT NOT NULL,
>         status TEXT NOT NULL DEFAULT 'pending',
> --- `src/daemon/db.ts`

#### RT-OBJ-wiki-prompts
Label: Shipped wiki and job instructions

Source-native identity: `getWikiSystemPrompt`, `buildIngestPrompt`, `buildQueryPrompt`, `buildLintPrompt`. Representational form: natural-language policy with illustrative page formats and requested output forms. Storage substrate: TypeScript template strings bundled/compiled into the installed program, then command arguments. These are static shipped guidance, not use-accumulated read-back. Mutable wiki-specific `.claude.md` is a distinct on-disk customization whose auto-discovery is attributed to Claude Code, not performed by this runner (SRC-1, `src/lib/prompts/wiki.ts`, `src/lib/prompts/ingest.ts`, `src/lib/prompts/query.ts`, `src/lib/prompts/lint.ts`, `src/daemon/runner.ts`, `src/daemon/scaffold.ts`).

> const systemPrompt = getWikiSystemPrompt();
>     args.push('--append-system-prompt', systemPrompt);
> --- `src/daemon/runner.ts`

### Routes

#### RT-RTE-ingest-job
Label: Source upload and model integration

Endpoints/progression: caller files → host-side raw upload → stored filename list → SQLite job → per-wiki queue → ClaudeRunner → Claude file effects and output → persisted result → caller. Owner: caller selects source input; daemon owns admission/scheduling; Claude proposes and executes content edits. State/effects: archive bytes are written before enqueue; wiki changes happen in the delegated process, not a database transaction. Operating mode: open supplied sources, not bounded curriculum. Answer oracle: none supplied by the runtime; source text is evidence input, not a known expected output. Human contribution is source supply when the caller is human, not per-content approval. Model can decline content in its output; daemon rejects unauthorized/invalid outer requests or reports execution failure, but has no semantic veto or rollback of edits (SRC-1, `src/cli/commands/ingest.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts`, `src/lib/prompts/ingest.ts`).

- Immediate return: upload filename then accepted job row; blocking CLI later prints the stored output.
- Later read-back: surviving wiki files, schema/index/log are reachable by later ingest/query/lint invocations; task instructions request their use.
- Delegated visibility: task filenames, appended system instructions, mounted wiki and resolved credentials/tool grant; actual file reads and custom instruction discovery are uninspected.
- Selection predicate: caller-provided source list; existing-page search/selection is requested of Claude using names, topics and themes.
- Invalidation or expiry: wiki deletion or file overwrite/removal; no per-job semantic invalidation or transactional edit rollback.
- Activation or effect: upload, queue and delegation are wired; desired integration/schema changes are requested, not observed.
- Evidence limits: no output wiki or trace supplied; relative paths mismatch the scaffolded `wiki/` directory; semantic compliance and benefit uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 5. For each source document:
>    a. Extract key facts, concepts, entities, and relationships.
>    b. Determine which existing pages should be updated and which new pages should be created.
>    c. Create or update wiki pages with the extracted information.
> --- `src/lib/prompts/ingest.ts`

Theory account, scoped to requested schema maintenance: guidance says conventions should evolve from encountered filing patterns, drift and vocabulary; it asks Claude to retain revisions in `_schema.md` for a future session. This is a requested language-level method, not evidence of executed theory revision. Theory-builder conditions 1–4: (1) claimed — localized conventions are requested, but no generated schema supplied; (2) claimed — future filing dependence is requested, not demonstrated; (3) claimed — drift questions request comparison and revision, but no criticism with blame assignment supplied; (4) claimed — retaining conventions for future use is requested, not an observed next round. Addressability of generated rules is uninspected; persistence is afforded across sessions through files. Learning/improved future capacity is uninspected; persistence is not improvement evidence. Reflection is claimed by the requested comparison of filing behavior with schema, while both realized causal directions are uninspected. Autonomous or reflective theory-building execution is uninspected. No exercised self-improvement attribution is made. These limits do not deny the wired content-update opportunity.

> - Has my filing behavior drifted from what the schema says? Update the schema to match reality.
> --- `src/lib/prompts/ingest.ts`

#### RT-RTE-query-job
Label: Question to wiki-backed answer

Endpoints/progression: caller question and optional API history → queue → fresh Claude process → markdown answer → durable job result → polling client. Owner: daemon schedules; Claude decides search and synthesis under natural-language grounding rules. Context/effects: same model/tools/mount path as ingest, including Write/Edit; system prompt also requests a log append. This is open question answering, not an evaluation mode; no expected-answer oracle or formal admission of newly synthesized claims. The prompt suggests saving synthesis but ships no distinct save endpoint (SRC-1, `src/cli/commands/query.ts`, `src/lib/prompts/query.ts`, `src/lib/prompts/wiki.ts`, `src/daemon/runner.ts`).

- Immediate return: accepted job row or wait-mode current/terminal row; blocking CLI prints output after terminal status.
- Later read-back: requested reads of retained index/pages; query-written log or other surviving files remain reachable, but actual writes uninspected. Prior job answers are not automatically inserted into later questions.
- Delegated visibility: question and supplied history text plus system prompt and accessible wiki; history supplied by API is copied, not loaded by daemon from older jobs.
- Selection predicate: Claude is instructed to read index then grep/glob for relevant files; no daemon relevance scorer.
- Invalidation or expiry: changes/deletion of wiki files or registry; no automatic expiration of stored answers or freshness check.
- Activation or effect: grounded answer and citation behavior requested; exit-code result admission wired; evidence-grounded correctness unobserved.
- Evidence limits: no question/answer trace; tools permit writes and optional web/MCP inputs; path mismatch and external Claude behavior prevent assurance of successful grounding.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 1. ONLY reference information that exists in the wiki files. Never use training data for facts.
> --- `src/lib/prompts/query.ts`

> 6. If your answer synthesizes multiple pages into new insight, mention it could be saved to the wiki as a new page.
> --- `src/lib/prompts/query.ts`

#### RT-RTE-lint-job
Label: Manual or counter-triggered maintenance

Endpoints/progression: caller lint request or queue counter → durable lint job → same runner → direct edits plus markdown report → result consumer. Owner: code chooses automatic trigger after ten successful ingests in current queue state, suppressing an already-pending lint; Claude diagnoses/selects fixes. Guidance: eight checks including contradictions, stale claims, index and schema drift. Admission: confident structural fixes are requested directly; contradictions/merges/stale facts are requested to remain report-only. Human judgment is requested for flagged issues, but no approval handler forces it before writes. Operating mode: open maintenance against existing wiki, not bounded testing. Answer oracle: none; the wiki/schema are comparison material, not externally validated expected outcomes. Rollback: no built-in restoration of model edits; external backup is operator guidance (SRC-1, `src/daemon/queue.ts`, `src/lib/prompts/lint.ts`, `docs/operations.md`).

- Immediate return: manual job acceptance followed by report on completion; automatic lint has no initiating human client.
- Later read-back: surviving fixes/schema/log can reach subsequent jobs; report persists in job result for clients, not automatically injected into later model work.
- Delegated visibility: date, lint instructions, appended wiki policy and filesystem access; no supplied curated evaluation answers.
- Selection predicate: requested glob of all markdown excluding raw; Claude selects issues and classifies confidence.
- Invalidation or expiry: overwrite/deletion of files; in-memory counter resets on daemon restart; no retained pending-review lifecycle.
- Activation or effect: automatic scheduling and delegation wired; confident fixes/flags requested, not observed.
- Evidence limits: no maintenance trace or before/after files; confidence and human-review partition are model policies, not effect guards.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> For issues requiring human judgment (contradictions, merges, stale facts), note them in your report but do NOT change the files.
> --- `src/lib/prompts/lint.ts`

> if (job.type === 'ingest' && result.success) {
>             state.ingestCount++;
> --- `src/daemon/queue.ts`

Schema drift comparison requests revision under static method guidance. Theory-builder conditions 1–4 are claimed at the request layer for localized schema, its use, drift-directed criticism and persistence into later work; generated localized content, actual decision dependence, explicit blame assignment and next-round dependence remain uninspected. Addressability and learning of generated conventions are uninspected; cross-session file persistence is afforded. Requested schema self-comparison is not observed reflection or autonomous theory building. No exercised self-improvement is established.

#### RT-RTE-config-change
Label: Capability and instruction configuration admission

Endpoints/progression: owner API/CLI config → validated extra-tool file or SQLite model; local editor → `.claude.md`; local filesystem configuration → `.tools/mcp.json`; next runner resolves current files/model. Owner: caller chooses API changes, route checks ownership and allowed names; local editing requires host permissions. The actual human/automation split is unresolved for API callers. Claude has file tools in the same root: this source adds no separate configuration write barrier. External Claude determines custom instruction discovery and MCP operation. Operating mode: direct configuration, not experimental successor selection. Answer oracle: none. Rejection: API rejects extras outside whitelist, but local MCP/custom text lacks an equivalent semantic admission check. Rollback: reconfigure/re-edit or external backup; no versioned rollback. Core shipped prompt/code edits require maintainer source editing and rebuild/redeployment, with proposed sequential prompt checks but no enforced evaluation gate (SRC-1, `src/cli/commands/config.ts`, `src/daemon/routes.ts`, `src/daemon/runner.ts`, `src/daemon/scaffold.ts`, `package.json`, `docs/prompts.md`).

- Immediate return: API updated wiki/acknowledgment or editor completion; no model call needed for configuration admission.
- Later read-back: runner reloads allowed-tools/MCP presence and model per job; `.claude.md` consumption depends on external discovery.
- Delegated visibility: deduplicated base plus allowed extras as both tool flags; MCP config path supplied if present; customization text delivery uninspected.
- Selection predicate: owner-selected wiki and config fields; allowed-tool membership filters extras; model string selected from current registry.
- Invalidation or expiry: overwrite/reconfiguration or wiki deletion; no installed-config revision pin.
- Activation or effect: tool/model/MCP argument changes wired; actual external grant enforcement and custom instruction activation uninspected.
- Evidence limits: operator config and live services absent; local writable configuration can bypass API authoring procedure but runner still filters tool names.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> .filter(l => l && !l.startsWith('#') && ALLOWED_TOOLS_WHITELIST.has(l));
> --- `src/daemon/runner.ts`

> args.push('--mcp-config', `${WORKSPACE_MOUNT}/.tools/mcp.json`);
> --- `src/daemon/runner.ts`

> execFileSync(editor, [claudeMdPath], { stdio: 'inherit' });
> --- `src/cli/commands/config.ts`

#### RT-RTE-job-recovery
Label: Restart requeue and terminal result recording

Endpoints/progression: daemon startup → running rows reset pending → queue startup → replayed runner → completion/failure row and client read. Owner: fixed SQL/code rules, not model successor judgment. Job effects are direct filesystem writes outside SQLite result transactions; the job ID is reused with increased retry count. Time/turn controls belong to the runner/external CLI contract; graceful queue shutdown waits thirty seconds before signalling tracked children (SRC-1, `src/daemon.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts`, `src/lib/constants.ts`).

- Immediate return: startup continues into listening/draining; terminal result is available after later completion/failure.
- Later read-back: retained pending payload is consumed on replay; partial wiki effects remain available to the next invocation without reconstruction from a clean snapshot.
- Delegated visibility: rebuilt prompt and current configuration, not preserved model working conversation.
- Selection predicate: all rows with status running at reset; then pending jobs by ascending ID per wiki.
- Invalidation or expiry: completion/failure ends automatic pending eligibility; reset has no retry cap or semantic deduplication check.
- Activation or effect: persisted work can be replayed; exactly-once markdown effects are not enforced.
- Evidence limits: no crash or timeout trace; signal delivery, child exit and descendant cleanup unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> SET status = 'pending', retry_count = retry_count + 1
>       WHERE status = 'running'
> --- `src/daemon/db.ts`

> if (!child.killed) {
>             console.warn(`[runner] Job #${job.id} did not exit after SIGTERM grace period, sending SIGKILL`);
>             child.kill('SIGKILL');
> --- `src/daemon/runner.ts`

### Claims

#### RT-CLM-workspace-isolation
Label: Workspace-only visibility claim

Claimed operation: README says a wiki namespace exposes only workspace, not host filesystem or other wikis. Source: SRC-1, `README.md`. Implemented wrapper instead bind-mounts within the inherited filesystem view and changes working directory; it does not hide other mounts (SRC-1, `src/daemon/namespace.ts`). The raw read-only mount covers its namespace path, not the original host-path alias. Thus mount setup is wired, but unconditional filesystem confinement is not established. Capability grant, credentials and model tool policy are separate controls, not substitutes for root isolation.

> **Safe by default.** Each wiki runs in its own Linux mount namespace — Claude can only see `/workspace`, not your home directory, not other wikis, not the host filesystem. No Docker required. Tool access is restricted to file operations (Read, Write, Edit, Glob, Grep) unless you explicitly opt in to more.
> --- `README.md`

> args: ['-m', '--propagation', 'private', '--', 'sh', '-c', script],
> --- `src/daemon/namespace.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-wiki-instructions
Label: Appended wiki policy authority

Consumer: external Claude Code/model. Channel: `--append-system-prompt` on every job and `-p` task argument. Force: natural-language instructions interpreted by model, distinct from tool flags and mount rules; requested index/source/link/log disciplines are not verified. Horizon: all delegated jobs under that installed product version. Evidence: SRC-1, `src/daemon/runner.ts`, `src/lib/prompts/wiki.ts`; [RT-OBJ-wiki-prompts](#rt-obj-wiki-prompts) supplies explicit append wiring. Wiki-generated schema can become later filing guidance through requested reads in [RT-RTE-ingest-job](#rt-rte-ingest-job), but actual behavioral activation is uninspected.

> You own the schema. It is not a static config file — it is a living document that evolves with every ingest. The schema captures what you've learned about how THIS knowledge base works: what categories exist, how pages in each category are structured, what naming and filing patterns have emerged, what domain vocabulary matters.
> --- `src/lib/prompts/wiki.ts`

## Annotations

none
