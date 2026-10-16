---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Sparks runtime baseline: external-agent semantic work, CLI/MCP maintenance, persistence and later consumption at the frozen revision."
run-id: AAS-2026-10-15-sparks-563865f8b26f-01
reviewed-boundary: "49abddc848ea55f78518bfbbbe04c3d37a5f2705"
---

# Sparks runtime report

## Runtime account

### Responsibility and evidence

Sparks supplies deterministic vault operations and an agent-facing writing protocol. It does not schedule the semantic agent or implement its model calls. A human captures material; an external agent decides which pages to create or revise; the binary parses, indexes, archives and optionally commits files. The [boundary](boundary.md) fixes SRC-1 and the whole-product scope, excluding the enclosing harness implementation. The semantic component is [RT-CMP-agent](#rt-cmp-agent); the claimed division of work is [RT-CLM-work-split](#rt-clm-work-split).

All findings below concern inspected implementation or shipped doctrine at SRC-1. No target commands, tests, providers or services were executed. There is no supplied observed-run or causal-experiment source. Thus wiring and requested behavior can be established, but actual model compliance, production recovery, semantic correctness and benefit remain unobserved. Additional inspection within the same frozen source covered full ingest/CLI adapters, manifest ingest lifecycle/schema, task admission/matching, archive/clear, collection dispatcher, index regeneration, instruction installation, Git execution, query filtering, brief selection, viewer HTTP handling, Makefile and CI. These are implementation evidence, with embedded prose and configuration comments treated as doctrine. They add coverage, not a new source.

### Ordinary invocation: capture to archive to later answer

1. **Trigger and identity.** A human asks an agent to process `inbox.md`. The source-native principal split is human capture / agent semantic writing / CLI mechanical mutation. The filesystem process identity, not a Sparks user identity, determines actual write access. `sparks init [path] --agent X` can create the vault, SQLite manifest and a harness-conventional instruction file. Supported filename identities are Claude, Codex, Gemini and generic; the content is identical. The mapping is not a model selection or provider credential mechanism (SRC-1, `cmd/sparks/init.go`, `internal/core/init.go`, `internal/contract/contract.go`). See [RT-RTE-contract-install](#rt-rte-contract-install).
2. **Prepare.** `sparks ingest --prepare` opens the vault/manifest and calls `PrepareIngest`. It reads the current inbox, splits entries with capture dates and deterministic hints, returns all entries and conservative affected-collection names, and opens an `in_progress` row if nonempty. The default output is JSON. An existing row returns its ingest ID and `already_in_progress`, rather than a new batch. This is a workflow interlock, not a filesystem lock. The CLI deliberately converts the already-in-progress result into readable output; callers must inspect that field (SRC-1, `cmd/sparks/ingest.go`, `internal/core/ingest.go`, `internal/manifest/ingests.go`).
3. **Semantic step.** The external agent owns the next decision. Its context is the human request, instruction prose, returned entry contents/hints, and whatever existing pages it reads. It is instructed to check aliases, prefer updates, preserve conflicting sources in a Revision section, write wiki pages/index/log, and add tasks. These are natural-language policies; the Go program does not run a model or validate that those decisions occurred. The agent's page writes are ordinary host filesystem effects, not submissions to a Sparks content-approval API. The contract recommends at most 10–15 entries per session, but prepare returns the complete parsed list (SRC-1, `internal/contract/contract.md`, `internal/core/ingest.go`).
4. **Finalize.** The agent calls `sparks ingest --finalize`. `FinalizeIngest` requires an active row but no caller-supplied ingest ID or entry receipt. It rereads the live inbox, archives that current content by capture date, clears the inbox after its header, scans the vault, optionally stages/commits through system Git, and completes the row. It does not check that every archived entry produced a page, nor that the batch matches the earlier prepare output. The durable result is files plus manifest/session state; stdout reports counts and commit/skip information. See [RT-RTE-ingest-cycle](#rt-rte-ingest-cycle).
5. **Return and later use.** On a later question, the agent requests structured lookup, receives page metadata, reads selected page files itself, and is instructed to synthesize an answer with wikilinks. For a weekly brief, Sparks selects recent log blocks, raw-file metadata, updated-page metadata, revisit signals and up to five open-task previews; the agent synthesizes to stdout and is told not to save unless asked. The viewer is another consumer: it reads Markdown bodies directly and re-queries the manifest for navigation/backlinks. These paths reach different projections of the same persisted vault; a query or brief result is not the full source content (SRC-1, `internal/manifest/queries.go`, `internal/core/brief.go`, `internal/view/server.go`, `internal/contract/contract.md`). See [RT-RTE-vault-consume](#rt-rte-vault-consume).

### Alternate paths and forcing cases

**Case 1 — a partial semantic batch is not a partial finalize.** The instruction budget of 10–15 entries does not limit finalization. Finalize reparses the live inbox and archives/clears all parsed entries. A newly appended entry between prepare and finalize can also enter that set. No snapshot comparison occurs in these functions. Thus completion of the mechanical ingest is not evidence of semantic completeness, and concurrent capture requires external coordination (SRC-1, `internal/core/ingest.go`, `internal/core/ingest_finalize.go`, `internal/inbox/archive.go`).

**Case 2 — alternate adapters share effects but not identical returns.** `sparks serve` offers stdio MCP tools for prepare, finalize, scan, query, brief, index, lint and tasks. Each resolves the vault from server working directory and invokes the same core/manifest implementation. MCP errors can retain partial results; CLI finalize returns an error before printing its summary. The MCP registry does not expose collection regeneration or abort in the inspected revision, although CLI exposes them. Neither adapter adds per-content human approval. Read-only-looking use through an agent tool protocol does not make the registered mutation tools read-only (SRC-1, `internal/mcp/serve.go`, `cmd/sparks/main.go`, `cmd/sparks/ingest.go`). See [RT-RTE-mcp-tools](#rt-rte-mcp-tools).

**Case 3 — scan and lint are not an admission barrier.** A scan with unchanged size and mtime skips hashing/reparsing; same-size content edits preserving mtime therefore do not necessarily refresh frontmatter. Individual scan failures accumulate in `ScanResult.Errors` while `Scan` can return a nil error; finalize discards that result and proceeds if the error return is nil. Missing frontmatter is tolerated during scan. Separately invoked `fmt` and `lint` report violations rather than gate finalize. Lint text output returns an error for issues, while JSON output returns after serialization without that issue-count error. The contract's proposed `lint --fix` is not a registered flag in the inspected CLI. These qualify [RT-CLM-mechanical-integrity](#rt-clm-mechanical-integrity), not an assertion that scans always fail or are useless (SRC-1, `internal/core/scan.go`, `internal/core/ingest_finalize.go`, `cmd/sparks/lint.go`, `cmd/sparks/fmt.go`, `internal/contract/contract.md`).

**Case 4 — Git and direct writes exceed the ingest row's scope.** Auto-commit calls `git add -A` and commits the dirty tree, not only files attributable to the prepared entries. Configured Git hooks/signing can participate through system Git. Direct editor/agent filesystem writes, `tasks add`, `done`, collection regeneration and index regeneration need no ingest row. The manifest's OpenIngest sequence checks for a row and then inserts; the schema has a nonunique status index, not a uniqueness constraint for the active status. It supports sequential blocking but does not establish race-free exclusion between simultaneous prepares. No deployed isolation or harness shell grant set is supplied (SRC-1, `internal/git/git.go`, `internal/core/tasks.go`, `internal/core/index.go`, `internal/collections/collections.go`, `internal/manifest/ingests.go`, `internal/manifest/migrations/0001_init.sql`).

### Guarantees, controls and recovery

| Claimed guarantee / owner | Enforcement point and strength | Covered paths, alternatives and external contract | Separate conclusions |
|---|---|---|---|
| Raw stability, no agent commits, alias dedup, Revision sections / human and agent | Embedded contract delivered as prose; **protocol** | Applies as instructions to cooperating agents. Direct host writes and shell commands are not intercepted by Sparks. Requires harness loading and agent/human compliance. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Only one prepared ingest / manifest layer | Current-row check before insert; **best effort** under concurrency | Shared by CLI and MCP prepare. Does not cover ordinary file writes, tasks, scan, regeneration or atomic concurrent admission. Requires callers to honor active-row results and external serialization where needed. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Mechanically indexed vault / scan and validators | Incremental metadata checks, parsing, graph rebuild and explicit diagnostic commands; **best effort** | CLI/MCP scan share implementation. Direct writes require a later scan; per-file errors and unchanged metadata weaken completeness; diagnostics are not finalize prerequisites. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Recoverable finalization / core plus operator | Archive → clear → scan → optional commit → complete; **best effort** | CLI/MCP share this order. Pre-clear crashes may duplicate archived entries on retry; post-clear failures need inspection/manual commit; active-row recovery is CLI abort. Filesystem and Git durability are external contracts. No cross-filesystem/SQLite/Git transaction or automatic content rollback is established. | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence and minimum passages for these rows are in [RT-RTE-ingest-cycle](#rt-rte-ingest-cycle), [RT-RTE-maintenance-write](#rt-rte-maintenance-write), [RT-BAP-agent-contract](#rt-bap-agent-contract) and [RT-CLM-mechanical-integrity](#rt-clm-mechanical-integrity). Guarantee strengths classify the enforcement actually inspected, not the contract's use of the word invariant.

The **capability surface** includes deterministic file/SQLite writes, task completion, Git subprocesses, a stdio tool server and an HTTP viewer. The **current grant set** of an enclosing agent is uninspected: instructions name tool usage but do not show allowed shell commands, provider-native tools, callbacks, remote workers or a session's permissions. The **deployed isolation envelope** is also uninspected. Viewer defaults to loopback and registers GET routes, but that does not constrain an external agent's direct filesystem access. No claim is made about unavailable provider internals or a particular deployment (SRC-1, `internal/mcp/serve.go`, `internal/git/git.go`, `internal/view/server.go`, `internal/contract/contract.md`).

Working-context control is modest and source-native: prepare structures the inbox, query selects metadata, brief filters signals and caps previews, and doctrine requests a session processing budget. These reduce or organize material offered to an external agent, but Sparks does not implement a model window, compaction, isolated sub-agent frame, eviction or reload scheduler in the inspected routes. Page reads are requested external retrieval; subsequent context inclusion belongs to the harness. Nothing in these source paths establishes provider-native tool policy, model-response approval, delegated agent visibility, model parameter updates, or successful activation of the supplied prose. The bounded positive mechanisms are detailed below rather than generalized into a universal absence claim.

### Change admission

There are three distinct change planes. Knowledge and task changes are agent/human filesystem edits or deterministic requested writes, with no per-content human approval requirement in the inspected core ([RT-RTE-ingest-cycle](#rt-rte-ingest-cycle), [RT-RTE-maintenance-write](#rt-rte-maintenance-write)). Instruction changes enter a vault through the embedded-contract installer; existing files are preserved unless explicitly forced ([RT-RTE-contract-install](#rt-rte-contract-install)). Product/capability/machinery changes are source changes followed by ordinary build/test/install workflows, not a running plugin loader or model-authored self-update loop ([RT-RTE-product-build](#rt-rte-product-build)). These routes establish admission mechanisms, not improved capacity. Semantic criticism/revision obligations belong to shipped doctrine; observed knowledge revisions and their epistemic merit are left to specialist analysis.

## Shared records

### Components

#### RT-CMP-agent
Label: External semantic agent

Source-native identity: the agent using Sparks, including named Claude Code, Codex CLI or Gemini-style integrations. Representational form: the model computation depends on distributed-parametric model state; instructions/results crossing Sparks are separately natural-language or symbolic material. Storage substrate: provider/harness model state outside the repository, unresolved by this source. Exact model version is not pinned by Sparks' harness-name mapping; whether an endpoint can resolve to another model and whether parameters change during operation are **uninspected**, because the provider and harness are outside the frozen implementation boundary. Mapping a filename to a harness does not fix its model. Evidence: SRC-1, `internal/contract/contract.go`, `internal/contract/contract.md`. This record identifies an external dependency, not a model shipped in the binary.

> Agents do content work; Sparks does plumbing.
> --- `internal/contract/contract.md`

### Operative objects

#### RT-OBJ-contract
Label: Embedded runtime contract

Source-native identity: `contractMarkdown`, embedded from the canonical contract and optionally copied to a vault instruction file. Representational form: natural-language operational instructions, interpreted by an agent/human. Storage substrate: compiled-in text plus ordinary Markdown files. The Go embedding/filename mapping is symbolic machinery, not the semantic force of the prose. Consumer and admission path: [RT-RTE-contract-install](#rt-rte-contract-install), [RT-BAP-agent-contract](#rt-bap-agent-contract). Evidence: SRC-1, `internal/contract/contract.go`, `internal/core/agent.go`.

> //go:embed contract.md
> var contractMarkdown string
> --- `internal/contract/contract.go`

#### RT-OBJ-ingests
Label: Manifest ingest lifecycle

Source-native identity: SQLite `ingests` rows with integer ID, timestamps, status, entry count and commit SHA. Representational form: symbolic state, consumed by fixed SQL and Go rules. Storage substrate: vault `sparks.db`. It records sessions, not prepared entry snapshots or a semantic completion receipt. Its active state blocks a sequential prepare; completed and aborted rows preserve history. Evidence: SRC-1, `internal/manifest/ingests.go`, `internal/manifest/migrations/0001_init.sql`.

> CREATE INDEX IF NOT EXISTS idx_ingests_status ON ingests(status);
> --- `internal/manifest/migrations/0001_init.sql`

### Routes

#### RT-RTE-ingest-cycle
Label: Two-phase inbox ingest

Endpoints/progression: human inbox capture → CLI prepare or equivalent MCP request → external agent page/index/log/task work → finalize → raw inbox archive, cleared inbox, scanned manifest, optional Git commit and completed ingest row. Owner: agent schedules calls, core owns mechanical effects, manifest owns row transitions. Decision policy: code parses/classifies; natural-language contract guides semantic choices. State includes live inbox, filesystem, SQLite and Git; there is no transaction spanning them. Evidence: SRC-1, `cmd/sparks/ingest.go`, `internal/core/ingest.go`, `internal/core/ingest_finalize.go`, `internal/inbox/archive.go`, `internal/manifest/ingests.go`, `internal/git/git.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: PrepareResult JSON with ID, entries, total and affected collections; finalize CLI count/commit summary or error, MCP structured result/partial error.
- Later read-back: Archived entries, persisted wiki/index/log/task edits and manifest projections can reach later queries, briefs and page reads through [RT-RTE-vault-consume](#rt-rte-vault-consume).
- Delegated visibility: External harness receives results; no Sparks agent-delegation mechanism in this path. Visibility beyond the caller is uninspected because harness behavior is external.
- Selection predicate: Prepare parses every current inbox entry; affected collections use deterministic hints. Finalize separately reparses all current entries, not a prepared subset.
- Invalidation or expiry: Finalize clears inbox content after the header and completes the active row; abort marks a row aborted. No automatic timeout or prepared-entry snapshot in the inspected lifecycle.
- Activation or effect: Wired archive append, inbox rewrite, scan, optional Git effects and lifecycle transition; successful semantic writing or influence on a later answer is unobserved.
- Evidence limits: Implementation and requested agent protocol only; no run demonstrates batch completeness, safe concurrent capture or crash recovery.

Admission: an open human request triggers work; the agent proposes and directly writes semantic changes under the contract. No expected-answer oracle or per-page approval/veto is built into prepare/finalize. Humans can review/edit externally, but invocation is not proof of per-content approval. Code can reject missing active state, I/O or Git failures; it does not veto a semantic contradiction. Recovery: abort unlocks future prepare without reverting files; manual inspection/commit is prescribed after interrupted finalization. Git configuration can disable commits; not-a-repository is reported as a skip. Guidance persists as contract and page/log content; the exact semantics of actual revisions remain unobserved. Operating mode: open-ended maintenance, not a bounded model experiment or curriculum.

> data, err := os.ReadFile(v.InboxPath())
> if err != nil {
> return FinalizeResult{}, fmt.Errorf("read inbox: %w", err)
> }
> today := time.Now().UTC().Format("2006-01-02")
> entries := inbox.Split(string(data), inbox.SplitOptions{Today: today})
> --- `internal/core/ingest_finalize.go`

> **Process no more than 10–15 inbox entries per session** to stay within reasonable token budgets. If more remain, the agent should stop and say so; the human re-runs.
> --- `internal/contract/contract.md`

The budget phrase above is part of an emphasized sentence, not a batch-limit implementation. Prepare's entry list and finalize's current-inbox selection are the counterexamples to interpreting it as enforced truncation.

#### RT-RTE-mcp-tools
Label: Stdio MCP adapter

Endpoints/progression: external MCP client → stdio server → registered handler → vault/manifest opened at working directory → core/manifest call → marshalled JSON or tool error. Owner: external caller chooses the next operation; server performs deterministic dispatch. No semantic agent executor is embedded. Evidence: SRC-1, `internal/mcp/serve.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tool text containing JSON, contract text for describe, or an error; jsonOrError can preserve a partial typed result alongside the error.
- Later read-back: Mutating tools persist the same files/manifest used by later invocations; read-only query/brief results alone are not retained memory.
- Delegated visibility: Tool results go to the calling MCP client; sharing with other agents is uninspected because Sparks supplies no enclosing delegation runtime here.
- Selection predicate: Explicit registered tool name and arguments; vault selected by server working directory. Query filters and brief days pass through to their consumers.
- Invalidation or expiry: Handler cleanup closes the manifest; durable writes survive. Server ends on client disconnect; no content expiry is added by the adapter.
- Activation or effect: Calls shared core mutations or structured reads. It does not make generated content trusted or approve model actions.
- Evidence limits: No protocol session was supplied or run. MCP library/provider internals and deployed client permissions remain outside inspection.

Admission/mode: external requests select operations; no independent human per-call approval is visible in this adapter. The common core supplies each write's rejection/recovery rules. No expected-answer oracle is used. Tools include task mutation and ingest, not collection regeneration or abort in this registry. Direct CLI remains an alternate administrative route.

> // disconnects. Every tool resolves the vault from the working directory
> // the server was launched in — same convention as the CLI.
> --- `internal/mcp/serve.go`

> "error":   err.Error(),
> "partial": res,
> --- `internal/mcp/serve.go`

#### RT-RTE-vault-consume
Label: Structured lookup and later synthesis

Endpoints/progression: external question → CLI/MCP query → manifest page metadata → external agent reads page bodies and synthesizes; weekly brief instead gathers selected activity signals; browser viewer reads Markdown plus manifest navigation. Owner: user/agent chooses query and body reads; Go rules select metadata/signals; agent owns semantic output. Evidence: SRC-1, `internal/manifest/queries.go`, `internal/core/brief.go`, `internal/mcp/serve.go`, `internal/view/server.go`, `internal/contract/contract.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Query page metadata; brief structured log blocks/file-page metadata/revisit paths/task count and preview; viewer HTML. Semantic answers and briefs are requested external agent outputs.
- Later read-back: Later invocations can read files written by ingest/direct maintenance and manifest metadata populated by scan. Contract says briefs stay on stdout unless a human requests saving; saving is not implemented by Brief itself.
- Delegated visibility: Caller/browser receives only the selected projection; external sharing or delegated model context is uninspected.
- Selection predicate: Query combines implemented nonempty filters with AND; exact case-insensitive title/alias/tag, type/maturity, graph and stale/orphan checks. Thin exists in QueryFilter but is not consumed by Query. Brief selects by dates/mtime and deterministic revisit signals, excludes raw/inbox and raw/archive from new-raw, and caps open-task preview at five. Viewer URL chooses the Markdown body.
- Invalidation or expiry: Query relies on manifest state until another scan; brief recomputes windows per call without deleting older files. Viewer rereads bodies and DB per request, not an automatic filesystem-to-manifest refresh.
- Activation or effect: Delivers metadata, selected retained log/task text or rendered bodies; delivery is wired, changed model behavior and improved answers are unobserved.
- Evidence limits: No actual vault/question/answer trace; metadata matching cannot establish semantic relevance, completeness or faithful synthesis.

Answer oracle: none in these inspected paths; there is no reference answer or model grader. Operating mode: open user lookup or time-window snapshot, not controlled evaluation. Working-context mechanism: selective external retrieval and capped previews, not compaction of an existing conversation. Raw content, body content and metadata are not interchangeable consumer inputs.

> 1. `sparks query` for structured lookup (by title, tag, type, link graph).
> 2. Read the matching wiki pages.
> 3. Synthesize the answer with `[[wikilink]]` citations.
> --- `internal/contract/contract.md`

> if len(t.First) < briefTasksPreview {
> text := strings.TrimSpace(strings.TrimPrefix(line, "- [ ]"))
> t.First = append(t.First, text)
> }
> --- `internal/core/brief.go`

#### RT-RTE-maintenance-write
Label: Direct deterministic maintenance writes

Endpoints/progression: caller requests scan, tasks add/done, collections regen or index → deterministic selection/transformation → SQLite or Markdown write → result/diagnostics. Owner: caller picks operation; Go code applies fixed rules. These operations do not require an active ingest. Task, collection and index writes have different source/selection rules, stated here rather than treating all wiki files as regenerated. Evidence: SRC-1, `internal/core/scan.go`, `internal/core/tasks.go`, `internal/collections/collections.go`, `cmd/sparks/collections.go`, `internal/core/index.go`, `cmd/sparks/lint.go`, `cmd/sparks/fmt.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Scan metrics/error list, task selected text/line or ambiguity candidates, per-collection result array, index counts and preserved-description counts, or diagnostic issues.
- Later read-back: Task mutations feed later task matching and brief previews; regenerated Markdown is available to page readers; index rebuild preserves matching existing descriptions; scan feeds later metadata/graph consumers.
- Delegated visibility: Return to CLI caller or corresponding MCP handler where registered; downstream sharing is uninspected.
- Selection predicate: Scan skips specified noisy dirs and manifest files, uses size+mtime before hash/parse, then rebuilds links. TasksAdd always appends under a matched/created heading. TaskDone prefers a unique substring match, then a sole or sufficiently separated fuzzy winner; ambiguous candidates are returned. Collections use registry names, extractors and configured/default globs; Tasks is excluded. Index groups manifest pages by type and matches descriptions by path/title keys.
- Invalidation or expiry: Regeneration overwrites generated collection files; task done changes an open marker; scan marks disappeared files deleted and replaces link edges; index overwrites its file while preserving matched descriptions. No common expiry or automatic semantic rollback is implemented here.
- Activation or effect: Deterministic file/manifest writes on admitted requests; diagnostic commands only report. Actual subsequent model use is unobserved.
- Evidence limits: Source-level wiring only. Extractor-specific semantic quality and concurrent-write safety are not established by the dispatcher; no observed success or recovery claim.

Admission: requested operation and its fixed rules determine acceptance. TaskDone rejects missing/ambiguous matches, but can choose a fuzzy winner without a second approval. TasksAdd checks nonempty fields, not duplicates. Collections dry-run avoids writes; unknown/extractor failures can be recorded per result, while file-write errors return. Index has a dry-run branch. Human authorship of a request does not prove review of its generated content. No reference-answer oracle is used. Operating mode is open maintenance. Recovery is user inspection/editing/Git where available, not a transaction across these operations. Despite contract/config comments claiming a collections-regeneration commit, neither inspected CLI caller nor dispatcher invokes Git or post-write Scan; those later steps cannot be assumed.

> // normalize it — pass whatever the agent decided. Duplicate-suppression
> // is the agent's concern: TasksAdd always appends.
> --- `internal/core/tasks.go`

> if err := os.WriteFile(path, []byte(body), 0o644); err != nil {
> return results, fmt.Errorf("write %s: %w", path, err)
> }
> --- `internal/collections/collections.go`

#### RT-RTE-contract-install
Label: Agent instruction installation

Endpoints/progression: caller invokes init with harness name and optional force → vault initialization → WriteAgentFile selects conventional filename → writes embedded contract unless existing file is preserved → later harness may load it, or agent can request describe directly. Owner: caller selects installation/overwrite; core enforces name/existence rules. Context/state: harness-name map, force flag and existing file; persisted payload is natural-language protocol. Evidence: SRC-1, `cmd/sparks/init.go`, `internal/core/agent.go`, `internal/contract/contract.go`, `internal/mcp/serve.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Wrote/skipped filename and initialization summary; describe returns embedded contract text without installation.
- Later read-back: Persisted instruction file can be loaded in later harness invocations; direct describe supplies compiled-in text. Static contract delivery is not accumulated operational memory.
- Delegated visibility: External harness convention determines instruction loading and precedence; not implemented by Sparks.
- Selection predicate: Known harness name maps to CLAUDE.md, AGENTS.md or GEMINI.md; identical embedded payload for every name.
- Invalidation or expiry: Existing files survive default init; force permits overwrite. Replacing a binary alone does not refresh an existing copied file.
- Activation or effect: File creation/replacement is wired; actual harness loading, instruction authority and compliance remain unobserved.
- Evidence limits: No harness session verifies loading or precedence; embedded-text delivery does not prove parity between prose promises and all implementation paths.

Admission: caller proposes installation by selecting name/force; software rejects unknown names and preserves existing files unless forced. Human review of the precise content is not required or established. No semantic oracle. Operating mode: explicit setup/update, not automatic improvement. Recovery is manual restoration/reinstallation; installer has no revision history or rollback mechanism. The guidance itself persists as the copied contract, and can therefore shape later agent behavior only through an external loader/interpreter.

> if !force {
> if _, err := os.Stat(target); err == nil {
> return false, filename, nil
> }
> }
> --- `internal/core/agent.go`

#### RT-RTE-product-build
Label: Source and contract build admission

Endpoints/progression: developer edits Go/contract/workflow sources → optional Makefile sync/check/build/install or CI on main pushes/pull requests → tests/vet/build → distributable/installed binary when separately deployed. Owner: developer controls proposals; CI runs fixed checks, while repository merge/deployment authority is not shown in inspected configuration. Representational form: code/workflow rules symbolic; contract content natural language; output executable/embedded prose. Evidence: SRC-1, `Makefile`, `.github/workflows/ci.yml`, `internal/contract/contract.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Build/test/check/install process results; no run evidence is supplied.
- Later read-back: A separately installed binary can supply revised rules/contract on future calls; actual installation/deployment of a candidate change is unobserved.
- Delegated visibility: CI results for repository workflows; developer/reviewer visibility depends on external repository permissions not established here.
- Selection predicate: Workflow triggers main push/PR; OS matrix runs vet, race tests and build, and Unix checks contract-copy equality. Make targets are explicit caller selections.
- Invalidation or expiry: Rebuild/reinstall can replace a binary; sync copies root contract to embedded path. Runtime copied instruction files need separate explicit refresh. Product rollback policy is uninspected because deployment is not in these files.
- Activation or effect: Can produce changed executable/embedded instructions; no model-mediated source editing, live plugin admission or automatic rollout is established by these build paths.
- Evidence limits: Test definitions and CI YAML are not passing results, required branch protection, code review or deployment evidence; excluded release-packaging provenance remains outside this assessment.

Admission: developer proposes source changes; fixed checks may fail, but whether they veto merge is unresolved without repository policy. Human/computational contribution to actual edits is uninspected. Test assertions supply program-specific expected outcomes where authored, not an answer oracle for semantic wiki revisions. Operating mode: development testing/building, separate from ordinary agent-driven ingest. No evidence-responsive runtime self-update loop or improvement result is claimed.

> sync-contract:
> cp sparks-contracts.md internal/contract/contract.md
> --- `Makefile`

> - name: Test
> shell: bash
> run: go test -race -coverprofile=cover.out ./...
> --- `.github/workflows/ci.yml`

### Claims

#### RT-CLM-work-split
Label: Semantic versus mechanical responsibility

Claimed operation: agents decide/write/synthesize, while Sparks mechanizes bookkeeping. Source: SRC-1, `internal/contract/contract.md`. The inspected CLI/core and retrieval adapters support the separation architecturally. This does not show that an agent followed the protocol, that every prose promise is enforced, or that the split improves quality/performance.

> Semantic search, keyword search over content, and synthesis are **agent work**. The CLI does not understand content.
> --- `internal/contract/contract.md`

#### RT-CLM-mechanical-integrity
Label: Mechanical integrity and preserved invariants

Claimed operation: append-only raw, revision blocks, identity dedup, stable timestamps and other preserved behaviors are load-bearing invariants. Source: SRC-1, `internal/contract/contract.md`. Assessment: code supplies selected deterministic mechanisms, while semantic/raw ownership duties are protocol-level and validation is not a comprehensive admission barrier. Enforcement points and counterexamples are in the runtime account and [RT-RTE-ingest-cycle](#rt-rte-ingest-cycle), [RT-RTE-maintenance-write](#rt-rte-maintenance-write).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> These are not implementation details — they are load-bearing invariants. Any reimplementation of Sparks must preserve them.
> --- `internal/contract/contract.md`

> // No frontmatter on a wiki page is allowed during scan; lint will
> // flag it. We still want a row so queries by path succeed.
> --- `internal/core/scan.go`

> if _, err := Scan(v, db); err != nil {
> return result, fmt.Errorf("post-finalize scan: %w", err)
> }
> --- `internal/core/ingest_finalize.go`

The last passage checks only Scan's error return, not its per-file Errors list. A mechanically completed ingest is therefore weaker than a validated, semantically complete vault revision.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-contract
Label: Contract guidance into external agent behavior

Consumer: external semantic agent/harness. Channel: copied harness-conventional instruction file, CLI describe stdout or MCP describe tool result. Force: natural-language protocol, dependent on external loading/precedence and model compliance, not a permission-enforcing reference monitor. Horizon: potentially later sessions through persisted instruction files; direct describe lasts in the receiving context according to the harness. Evidence: SRC-1, `internal/contract/contract.go`, `internal/core/agent.go`, `internal/contract/contract.md`, `internal/mcp/serve.go`. Linked route: [RT-RTE-contract-install](#rt-rte-contract-install).

> - Never edit `raw/` (except the human writing into `inbox.md`).
> - Never edit `sparks.db`.
> - Never edit a regenerated collection page (everything except Tasks).
> - Never make git commits — Sparks handles them on `ingest --finalize`.
> - Never delete notes; move to `raw/archive/` instead.
> --- `internal/contract/contract.md`

These prohibitions establish requested boundaries. They do not establish actual tool grants, filesystem isolation or obedience. Direct write and Git paths remain outside their mechanical enforcement.

## Annotations

none
