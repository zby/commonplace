---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Binder runtime baseline: graph transactions, alternate admission paths and shipped agent callers at e4066d750ac5c6918706f44b12daa261b261106e."
run-id: AAS-2026-10-15-binder-a35c41531d40-01
reviewed-boundary: e4066d750ac5c6918706f44b12daa261b261106e
---

# Binder runtime report

## Runtime account

### Work and evidence basis

Binder performs deterministic graph storage, schema-based admission, querying and document synchronization. It exposes these capabilities to people and agent hosts rather than owning a general autonomous agent loop. Shipped prompts and an executable journal importer add model-mediated workflows inside the selected system boundary. Their scheduling and model execution still depend on external hosts. The [boundary](boundary.md) supplies SRC-1 and the frozen revision. All findings below are implementation or doctrine/design evidence from SRC-1; no execution trace, passing test result or causal experiment was supplied or produced.

This inspection extends the boundary's initial coverage to the transaction application and asynchronous SQLite wrapper, plugin loading, script execution, custom HTTP module loading, journal replay/repair, the full model helper and journal importer, and the task implementation guide. Exact paths appear in the records. Other source files remain available; this is not a complete security or synchronization audit. Memory transformation details and the remaining journal/workflow skills are left to the specialists, not classified as absent.

### Ordinary invocation: update, persist, return, read

Consider a caller invoking `binder update <ref> field=value`. CLI dispatch selects `UpdateCommand`; `runtimeWithDb` discovers the workspace, loads configuration and logging, opens the SQLite-backed repo and installs journal, undo and docs plugins. `--cwd` can first change the process working directory. The caller supplies the reference and patches; code, not a model, owns the next step. The command obtains the namespace schema, parses patches and stamps transaction metadata, including the configured author. The alternate piped-input branch rejects simultaneous positional input and parses an array of updates. Both call `kg.update`. SRC-1, `packages/cli/src/index.ts`, `packages/cli/src/runtime.ts`, `packages/cli/src/commands/update.ts`.

Inside the graph, `update` reserves an immediate write transaction and reloads the record schema inside it, rather than trusting an earlier process-local cache. The processor resolves configuration edits first, computes the resulting record schema, and processes record changes against that schema. Changeset preparation resolves upserts and relations, builds changesets, aggregates errors and expands delete cleanup/inverse relations. The application step checks transaction sequence and predecessor hash, applies config changes before records, and saves the transaction. The async database wrapper holds the SQL transaction until its callback settles, rolling back error results and thrown failures. These symbolic operations admit data and schema changes; they do not adjudicate factual truth. See [RT-RTE-graph-update](#rt-rte-graph-update) and [RT-CLM-transaction-boundary](#rt-clm-transaction-boundary).

After database success, originating `onCommit` subscribers run, then `afterCommit`, then general `onTransaction` subscribers. The CLI runtime registers journal before undo before docs. Journal reconciliation takes another writer lock; docs rendering invalidates navigation/view caches on config changes and can notify the LSP about changed files. Subscriber errors are reported without aborting the committed graph transaction. Thus a successful database write is not an atomic promise of successful file rendering, journal repair or arbitrary hooks. The command prints the resulting transaction and closes its runtime. A subsequent process can reopen the database and fetch/search retained state, with optional relation expansion and pagination. [RT-OBJ-knowledge-graph](#rt-obj-knowledge-graph) distinguishes stored state from immediate command output.

### Alternate entry paths and four forcing cases

MCP `transact` and HTTP `POST /api/transactions` parse their own envelopes and converge on `kg.update`; neither adds a mandatory per-content human confirmation step in the inspected handler. MCP returns text, transaction metadata and structured transaction data. HTTP returns the transaction with status 201. MCP transport is newline JSON-RPC over stdio. HTTP defaults to `127.0.0.1` but accepts host configuration. HTTP's default author is spread before the request body, so it is a fallback, not authenticated authorship. The bundled `openWorkspace` library opens the full runtime and optionally stamps a validated client ID as default provenance; a raw repo open need not install CLI plugins. SRC-1, `packages/cli/src/commands/mcp.ts`, `packages/cli/src/mcp/index.ts`, `packages/cli/src/mcp/tools/transact.ts`, `packages/cli/src/commands/http.ts`, `packages/cli/src/http/server.ts`, `packages/cli/src/workspace.ts`, `packages/repo/src/local/open.ts`.

The following forcing cases challenge broader readings of the ordinary route:

1. **Prepared replay is not fresh schema admission.** `kg.apply` enters the common application wrapper with an already formed transaction, bypassing `processTransactionInput`. Journal repair actually uses this route after comparing logs and database history and potentially rolling back a divergent suffix. The sequence/predecessor check remains, but the `update` preparation claim does not extend to every write. [RT-RTE-journal-repair](#rt-rte-journal-repair).
2. **Disk saves are writes without an interactive CLI patch.** `docs sync` extracts modified files then calls `update`; LSP saves extract the latest on-disk document and call `update` too. Per-URI coalescing prevents overlapping save work in that handler, not a global distributed edit guarantee. A file outside known snapshot roots is skipped. [RT-RTE-document-sync](#rt-rte-document-sync).
3. **Extensions cross the graph's effect boundary.** Workspace plugins are dynamically imported and receive the repo, including its database. Inline hooks spawn shell commands with transaction JSON on stdin. Workspace scripts execute Node/Bun/sh subprocesses, and custom HTTP modules are imported and receive graph, config, filesystem and logger. Graph validation does not mediate all effects those programs can cause. [RT-RTE-extension-load](#rt-rte-extension-load).
4. **A model-produced changeset need not be persisted.** The journal importer reads retained logs, calls an external agent executable, parses its text and prints JSON. It does not call the write command on that output. Moreover its prompt permits an empty list when everything is already covered, while its parser treats zero extracted entries as failure. Neither the output label nor the prompt establishes successful deduplication, temporal accuracy or retained learning. [RT-RTE-git-import](#rt-rte-git-import).

These cases are source-supported, not experiments. Direct `callLlm` is a further model-call affordance, not a discovered core command consumer: a bounded search in `packages/cli/src` found only its definition and comments. It constructs a fresh context for one completion and validates a returned `respond` tool call if a schema was requested; this is not execution of arbitrary model tools. [RT-RTE-llm-call](#rt-rte-llm-call). Provider-native tools or agent subprocess internals, remote-worker isolation and host context compaction remain uninspected; their absence is not established.

### Authority, guarantees and human gates

The capability surface includes record and schema mutation, replay/rollback, filesystem synchronization, arbitrary imported code and shell/subprocess execution. The current grant set of a deployed host, enabled workspace plugins, actual credentials and OS/network containment are not captured. A loopback default is not an authentication or sandbox guarantee. In the inspected built-in HTTP handlers and MCP dispatcher, input parsing and graph admission are the operative checks; host authorization and deployment isolation require external contracts. A client ID or author string supplies provenance, not proof of principal identity. SRC-1, `packages/cli/src/http/server.ts`, `packages/cli/src/mcp/index.ts`, `packages/cli/src/workspace.ts`, `packages/repo/src/local/plugin-loader.ts`.

The database guarantee belongs to the repo graph and DB wrapper and covers graph-managed transactions under SQLite/adapter semantics. Derived files are best-effort post-commit effects, and raw database access or arbitrary extension I/O is outside this guarantee. [RT-CLM-transaction-boundary](#rt-clm-transaction-boundary) and [RT-CLM-derived-effects](#rt-clm-derived-effects) state separate implementation and operation conclusions.

Human confirmation does exist as a shipped prompt policy, rather than a universal write guard. Day-summary requests discussion, a scored proposal and confirmation before `binder update`; it prohibits modifying the day's plan or writing carry-forwards. By contrast, the HTTP/MCP handlers accept valid requests directly, and the importer merely emits a proposal. SRC-1, `examples/journal/skills/day-summary/SKILL.md`:

> I respond with final corrections, score adjustments, and carry-forward decisions.
> --- `examples/journal/skills/day-summary/SKILL.md`

The task skill selects guides from retained task fields and asks the agent to reread after each guide. Its implementation guide gives existing passing tests priority over specification, acceptance criteria and potential solution, then asks for verification before completion. The runtime does not mechanically implement that ordering or a commit/release gate. This product-change pathway, its decision roles and limited oracle are recorded in [RT-RTE-task-guide](#rt-rte-task-guide); the skill's natural-language authority is [RT-BAP-task-guidance](#rt-bap-task-guidance). No model obedience, autonomous completion, benefit or self-improvement is inferred from these instructions.

## Shared records

### Components

#### RT-CMP-journal-model
Label: Journal importer model behind external CLI

Source-native identity: `LLM_PROVIDER` selects `claude` (default) or `opencode`, each invoked with `--print`. Representational form: distributed-parametric computation, mediated by a natural-language prompt and textual response. Storage substrate: external provider/agent installation; weights and provider state are not in this checkout. Used by [RT-RTE-git-import](#rt-rte-git-import). Parameters changing during operation: uninspected — subprocess/provider internals are outside captured evidence. Exact version pinned: no model/version argument in this caller. Mutable endpoint resolving to another model: possible through external CLI configuration; actual resolution uninspected. SRC-1, `examples/journal/git-import-logs.ts`.

> const LLM_PROVIDER = process.env.LLM_PROVIDER || "claude";
> --- `examples/journal/git-import-logs.ts`

#### RT-CMP-llm-model
Label: Configured model for callLlm

Source-native identity: provider and model ID resolved per operation from `ctx.config.llm`. Representational form: distributed-parametric; symbolic provider/model selectors and natural-language inputs are separate from numerical weights. Storage substrate: remote provider accessed through pi-ai, not the graph database. Used by [RT-RTE-llm-call](#rt-rte-llm-call). Parameter mutation during operation: uninspected — no weight-update operation in this helper, provider internals uninspected. Exact weight/version pinned: not established by a configurable model ID. A mutable endpoint can resolve differently; the wrapper provides no immutable weight digest. SRC-1, `packages/cli/src/lib/llm.ts`.

> const { provider, model: modelId } = resolved;
> --- `packages/cli/src/lib/llm.ts`

### Operative objects

#### RT-OBJ-knowledge-graph
Label: KnowledgeGraph transaction and entity state

Source-native identity: `KnowledgeGraph`, its record/config tables and transaction history. Representational form: symbolic fields, entity references, changesets, schema and transaction metadata consumed by fixed graph rules. Free-text field contents can separately reach interpreting humans/models; that consumption does not make the SQL schema natural-language policy. Storage substrate: SQLite opened at the workspace data path; schemas and derived navigation/view state also have process-local caches. Evidence: SRC-1, `packages/repo/src/local/open.ts`, `packages/repo/src/knowledge-graph.ts`, `packages/repo/src/transaction-processor.ts`.

> const dbPath = join(paths.data, DB_FILE);
> --- `packages/repo/src/local/open.ts:251-255`

The graph exposes fetch/search after later opens, not only the previous command's printed output. Writes and schema cache invalidation are covered by [RT-RTE-graph-update](#rt-rte-graph-update). This record identifies the runtime container; memory transformations and authority of individual retained text parts are not collapsed into one finding.

### Routes

#### RT-RTE-graph-update
Label: Caller input to graph update and return

Endpoints/progression: CLI patches or piped arrays, MCP transact, HTTP transaction body or workspace library input → graph update → transaction processing/application → subscribers → caller. Owner: command/tool/HTTP code owns control flow; the invoking person, script or agent supplies content. Context/state/effects: namespace schema, configured author and metadata, existing graph version and entity state determine symbolic admission; accepted record/config changes persist in SQLite. `openWorkspace` adds full CLI plugins and optional default source, unlike bare repo use. SRC-1, `packages/cli/src/commands/update.ts`, `packages/cli/src/mcp/tools/transact.ts`, `packages/cli/src/http/server.ts`, `packages/cli/src/workspace.ts`, `packages/repo/src/knowledge-graph.ts`, `packages/repo/src/transaction-processor.ts`, `packages/repo/src/changeset-processor.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI prints transaction; HTTP returns transaction JSON; MCP returns metadata, textual count and structured transaction.
- Later read-back: accepted entities/config can be fetched or searched on subsequent graph opens; schema changes govern later input processing.
- Delegated visibility: returned data reaches the requesting host/client; graph access permits other workspace clients to read committed state, not automatic prompt injection.
- Selection predicate: caller-selected namespace/reference/patches or transaction input; schema/version and changeset rules select admissible mutations.
- Invalidation or expiry: config writes clear schema cache; update reloads schema inside its reserved transaction; explicit deletion/rollback can remove state, with no expiry inferred.
- Activation or effect: code applies accepted graph mutations and invokes subscribers; model behavioral activation remains unobserved.
- Evidence limits: implementation only; no authenticated caller identity, deployment permissions, factual validation or observed run established.

Admission: open caller requests, not a curriculum or bounded experiment. Caller proposes; parser/processor and optional before-transaction/before-commit callbacks can reject; no mandatory human veto in these handlers. A human may supply or edit input, but generic caller identity does not establish human control of each admitted content item. Schema is a structural constraint, not an answer oracle. Guidance consists of command/tool contracts and current schema; accepted field/schema changes and transaction metadata persist. Recovery is error rollback before commit and explicit graph rollback afterwards; it does not undo arbitrary external effects.

> const updatedSchema = applyConfigChangesetToSchema(
>     recordSchema,
>     configsResult.data,
>   );
> --- `packages/repo/src/transaction-processor.ts`

#### RT-RTE-document-sync
Label: Modified document or editor save to graph

Endpoints/progression: `docs sync` path/all modified files, or LSP file save → extraction using navigation/schema/views → `kg.update` → committed graph and render subscribers. Owner: command code or LSP save handler; a human or program authored the disk content. Context: disk state, snapshot identity, navigation and current schema; executor: local process filesystem and graph. SRC-1, `packages/cli/src/plugins/docs/commands.ts`, `packages/cli/src/lsp/handlers/save-handler.ts`, `packages/cli/src/plugins/docs/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: sync prints transaction/success or no-change; LSP sends save count or error notification asynchronously.
- Later read-back: accepted fields become graph state available to future read/search and document rendering.
- Delegated visibility: editor receives notifications; other clients can read committed state through graph entry paths.
- Selection predicate: requested sync scope or saved file URI within recognized snapshot roots, then extracted changes; LSP skips non-file/outside-workspace paths and empty diffs.
- Invalidation or expiry: subsequent saves/updates replace fields; graph config changes invalidate rendering caches; no time expiry established.
- Activation or effect: handler calls update; post-commit rendering may update disk and notify clients; no agent compliance observed.
- Evidence limits: extraction internals were not exhaustively audited; save coalescing is per URI in this process, not proof of conflict-free distributed editing.

Admission: disk changes propose content; extraction and common graph admission decide acceptance. No per-save human confirmation is added by this handler. Operating mode is ordinary editor/CLI work; answer oracle is inapplicable to file-to-field synchronization. Guidance is current schema/navigation/views; field changes persist. Failures notify/log; retries can occur on later saves, with pending saves coalesced to a latest-disk resync. Recovery after commit inherits the graph's rollback limits.

> // At most one sync runs per URI at a time. Saves arriving while a sync is
> // in-flight set a pending flag; when the current sync finishes, a single
> // re-sync runs with the latest disk content, preventing duplicate transactions.
> --- `packages/cli/src/lsp/handlers/save-handler.ts`

#### RT-RTE-journal-repair
Label: Transaction log repair and prepared replay

Endpoints/progression: repair caller → log verification and DB/log history comparison → backup divergent DB transactions → graph rollback → apply log-only transactions. Owner: repair code under caller invocation. Context/state: hashes, version IDs, transaction log and database; executor: graph plus filesystem. It is a different admission path from fresh update processing. SRC-1, `packages/cli/src/plugins/journal/sync.ts`, `packages/repo/src/knowledge-graph.ts`, `packages/repo/src/transaction-applier.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: repair result includes optional backup path or error.
- Later read-back: repaired database state is consumed by later graph opens; logs and backups support later recovery rather than proving improved decisions.
- Delegated visibility: graph subscribers react to rollback/replay; subsequent clients can query the resulting graph.
- Selection predicate: verified log, DB/log hash comparison and last common transaction identify divergent suffixes; apply checks next ID and predecessor hash.
- Invalidation or expiry: rollback deletes a selected transaction suffix and clears schema cache; restored history supersedes divergent state.
- Activation or effect: implementation rolls back and reapplies prepared transactions; actual repair and derived-file success unobserved.
- Evidence limits: inspected repair and apply paths do not constitute a complete proof of log integrity or all journal operations.

Admission: caller elects log-authoritative repair; software determines suffixes and can reject verification/version/application failures. There is no per-transaction human content approval here. Operating mode is explicit repair, not model evaluation; the reference is the verified log, not an answer oracle for factual content. Proposed changes are previously formed transactions. Backup and early-error returns provide bounded recovery; the whole multi-transaction repair is not shown as one atomic operation. No model guidance or instruction revision is established.

> apply: (transaction: Transaction) =>
>       prepareApplyAndNotify(() => ok(transaction)),
> --- `packages/repo/src/knowledge-graph.ts`

#### RT-RTE-extension-load
Label: Workspace code and shell effect routes

Endpoints/progression: configured plugin spec → dynamic import → register with repo; configured hook → transaction subscription → shell command; workspace script → runner subprocess; HTTP user static directory → server module import → route factory. Owners: workspace/config author selects code; imported code or subprocess owns its subsequent effects. Substrate: modules/scripts/config on disk, process memory and child processes. These are grouped as host-code admission, not asserted to share graph validation. SRC-1, `packages/repo/src/local/plugin-loader.ts`, `packages/repo/src/local/open.ts`, `packages/cli/src/lib/scripts.ts`, `packages/cli/src/index.ts`, `packages/cli/src/http/server.ts`, `packages/cli/src/http/serverModule.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: plugin registration completes or throws; script runner returns exit code; server loader returns a Hono app or load/shape error; hook completion waits on child exit.
- Later read-back: inapplicable — the loader itself does not retain a use-derived knowledge result; extension code may independently write persistent state.
- Delegated visibility: plugin receives repo including DB; HTTP factory receives kg/log/config/fs; hook receives transaction JSON; script receives caller-supplied cwd/env and inherited stdio.
- Selection predicate: enabled plugin specs, configured hooks, discovered supported script extensions/names, or first matching server.ts/server.mjs/server.js in user web directory.
- Invalidation or expiry: plugin disposal runs in reverse order at repo close; script exits end child work; no general unloading, revocation or durable rollback of external effects established.
- Activation or effect: imported modules and spawned processes execute with host capabilities; no sandbox enforcement appears in these loaders.
- Evidence limits: enabled grants and unshipped code are unknown; no arbitrary extension safety, isolation, correctness or completion guarantee.

Admission: workspace author supplies/changes executable code and config, software applies enable flags and loader/shape checks. HTTP factory must return a Hono-like app; this is not a safety oracle. Operating mode is extension execution, not experimental improvement. No universal approval/rejection gate is established beyond loading checks; a human operator can choose files/config but per-content review is unresolved. Guidance is plugin/factory/runner contracts; files persist as capabilities until changed. Disable/remove or restart can stop future loading; reversing prior filesystem/network effects is not supplied by these loaders.

> const mod = await import(name);
> --- `packages/repo/src/local/plugin-loader.ts`

> const child = spawn(hook.command, {
>               shell: true,
>               stdio: ["pipe", "inherit", "inherit"],
>             });
> --- `packages/repo/src/local/plugin-loader.ts`

#### RT-RTE-git-import
Label: Git commits and journal context to proposed log entries

Endpoints/progression: caller date/env/default day → Git log and per-commit stat calls → prior/current journal reads through Binder subprocesses → prompt → claude/opencode subprocess → line parser → time-position insert mutations → printed changeset. Owner: code sequences the workflow, model proposes descriptions. Context: filtered commits plus retained logs; model component is [RT-CMP-journal-model](#rt-cmp-journal-model). SRC-1, `examples/journal/git-import-logs.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON changeset on stdout, dry-run prompt, no-commits message, or failure.
- Later read-back: prior/current logs are read into this invocation; newly generated output has no write/read-back path inside this script and requires a separate application step.
- Delegated visibility: assembled prompt reaches external CLI via a temporary stdin file; returned stdout is parsed locally, stderr is reported on nonzero exit.
- Selection predicate: target date, wip/typo/merge exclusions, journal keys for target and previous day; response lines must start with '- ' to be extracted.
- Invalidation or expiry: prompt file is removed after the subprocess; current-log comparison is requested in prose, not enforced as semantic deduplication; printed proposal has no automatic expiry.
- Activation or effect: external completion is requested and parsed; output is printed, not applied to graph by main.
- Evidence limits: no model run or factual outcome; Git failures are not robustly surfaced by the Git helper; empty model output list becomes an error despite being permitted by the prompt.

Admission: model proposes entries under grouping, concision and nonduplication instructions; code extracts lines and orders insert positions using parsed time. No human per-content approval occurs inside the script, but neither does durable admission. Operator or another caller must decide whether/how to apply the printed changeset through graph admission. Operating mode: open date-based summarization, not an experiment/curriculum. Git records are evidence input, not a reference answer proving summary correctness; no answer oracle. Recovery: nonzero model exit fails; existing journal read failures become missing context; no internal retry or persisted proposal recovery. Retained result from this script alone: none established.

> console.log(JSON.stringify(changeset, null, 2));
> --- `examples/journal/git-import-logs.ts`

#### RT-RTE-llm-call
Label: One configured completion with optional structured response

Endpoints/progression: `callLlm(ctx, operation, params)` → provider/model config and API-key checks → pi-ai completion → text extraction or first matching respond call validation → result plus usage and JSONL log. Owner: helper code controls one request; external model supplies response. State/context: supplied system/user prompt, one user message and optional single tool schema, not accumulated dialogue. Component: [RT-CMP-llm-model](#rt-cmp-llm-model). SRC-1, `packages/cli/src/lib/llm.ts`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: data, usage, provider and model or a typed error.
- Later read-back: uninspected — helper writes usage/failure logs but no later behavioral consumer was established; no conversation state is reloaded here.
- Delegated visibility: provider receives constructed context; caller receives extracted text/validated arguments, not the whole response object.
- Selection predicate: operation-resolved provider/model and optional schema select response handling; first matching respond call is used.
- Invalidation or expiry: context is freshly constructed per call; caller/host controls any retained result and model-config changes.
- Activation or effect: callable code requests a completion, checks schema when supplied and returns arguments; it does not execute the respond tool as an external action.
- Evidence limits: bounded search for callLlm in packages/cli/src found definition/comments only, not a core consumer; actual endpoint behavior and strict one-call obedience unobserved.

The prompt requests exactly one tool call, but code checks existence and validates the selected call, not the count of all tool calls. Structural schema checking is not an answer oracle. No product/knowledge change is admitted by this helper alone; downstream persistence and human control are caller responsibilities. Its fresh-context design bounds what this wrapper sends, not what a provider retains. No host compaction, sub-agent frame or reload policy is established by this helper.

> "Submit the structured response. Always call this tool exactly once."
> --- `packages/cli/src/lib/llm.ts`

#### RT-RTE-task-guide
Label: Retained task state to guided product work

Endpoints/progression: user task request/key or task-list choice → read Task → status check → first matching guide → reread Task after guide → next guide/implementation. Owner: foreground agent interprets prompt; user can direct guide choice. Context: requested task fields, sourceFiles, tests and guide text; executor: external host agent with Binder and development tools. SRC-1, `examples/workflow/skills/implement-task/SKILL.md`, `examples/workflow/skills/implement-task/guides/implement.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: intended code changes and report of completion/issues; draft/complete/cancelled tasks instead produce a stop message.
- Later read-back: skill explicitly requests task reread after guide completion; recorded task fields select subsequent guidance, without proving any particular historical update occurred.
- Delegated visibility: guide text and task data are delivered to the agent through host skill/command facilities; no separate worker context or return channel is specified in these two files.
- Selection predicate: key or active/pending lists; task status; missing rootCause/specification, linked Problem and test need select guide in listed order, unless user directs otherwise.
- Invalidation or expiry: mutable task fields and new reads can change selected guide; no host skill-version pin or context eviction specified.
- Activation or effect: prompt requests code implementation and verification; actual host obedience, writes and test execution unobserved.
- Evidence limits: doctrine/design only; these files do not implement tool permissions, automatic release, merging, human approval or a durable autonomous scheduler.

Admission: user supplies problem/direction, agent proposes and edits product under task guidance. Passing tests and acceptance criteria are requested completion checks; existing tests serve as a conditional expected-behavior reference supplied by the project, not an independently validated universal oracle. Agent is instructed to fix failures, but no runtime veto enforces this. Operating mode is open task work, not a benchmark or curriculum. Guidance prioritizes tests, specification, acceptanceCriteria and potentialSolution. Task data may persist through Binder; production code persists through filesystem tools owned by the host. Rollback/commit/release policy is not specified in these files. No claim of theory criticism, learning or self-improvement follows from rereading task state.

> 3. **Verify.** Run the tests. If `acceptanceCriteria` exist, verify each one. Fix failures before considering the work done.
> --- `examples/workflow/skills/implement-task/guides/implement.md`

### Claims

#### RT-CLM-transaction-boundary
Label: Graph-managed transaction consistency

Claimed operation: fresh `update` prepares schema-aware mutations inside a reserved SQL write transaction; both update and prepared apply check sequence/predecessor before application/save. Owner/enforcement: `KnowledgeGraph` and async SQLite wrapper. Guarantee strength: invariant, conditional on inspected graph entry and SQLite/adapter transaction semantics. Covered: graph update/apply/rollback SQL work. Alternatives: prepared apply skips fresh-input processing; direct DB access and external filesystem/shell effects are not covered. Separate schema preparation from version consistency; neither is factual truth checking. SRC-1, `packages/repo/src/knowledge-graph.ts`, `packages/repo/src/db.ts`, `packages/repo/src/transaction-applier.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> sqlite.exec(isErrResult(result) ? "ROLLBACK" : "COMMIT");
> --- `packages/repo/src/db.ts`

> transaction.id !== expectedId ||
>     transaction.previous !== versionResult.data.hash
> --- `packages/repo/src/transaction-applier.ts`

#### RT-CLM-derived-effects
Label: Post-commit side effects are not database atomicity

Claimed operation: originating commit subscribers maintain journal/undo/docs; subscriber failures are reported and do not abort the committed DB operation. Owner/enforcement: graph notification wrapper and CLI plugin registration. Guarantee strength: best effort for derived effects, not deployment guarantee. Covered: registered handler errors returned or thrown through notification wrapper. Alternatives/limits: afterCommit callbacks are awaited separately; hook/subprocess behavior and externally written files are not transactionally reversed. Required external contract: working filesystem, process completion, and trustworthy extension code. SRC-1, `packages/repo/src/knowledge-graph.ts`, `packages/cli/src/runtime.ts`, `packages/cli/src/plugins/docs/index.ts`, `packages/cli/src/plugins/journal/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Subscriber failures cannot abort the already committed DB operation.
> --- `packages/cli/src/plugins/journal/index.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-task-guidance
Label: Task fields and guide text to agent decisions

Consumer: external foreground agent running the shipped task skill. Channel: skill body plus Binder reads/searches and loaded guide files. Force: natural-language instruction and task-specific design contract; not a runtime-enforced permission boundary. Horizon: current task episode with explicitly requested rereads, potentially across sessions when task state is retained and the skill is invoked again; actual recurrent activation unobserved. Static guide text is not itself use-derived memory. SRC-1, `examples/workflow/skills/implement-task/SKILL.md`, `examples/workflow/skills/implement-task/guides/implement.md`. Route: [RT-RTE-task-guide](#rt-rte-task-guide).

> If `specification` is filled, that is the design contract — follow it.
> --- `examples/workflow/skills/implement-task/guides/implement.md`

## Annotations

none
