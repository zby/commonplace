---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "beads_rust runtime baseline: CLI issue lifecycle, MCP requests, JSONL admission, instruction installation and executable replacement at the frozen commit."
run-id: AAS-2026-10-16-beads-rust-e82d5506d2ff-01
reviewed-boundary: 53f7a3d30aca8cab3c3e4abdefeade459e8a3089
---

# beads_rust runtime report

## Runtime account

### Work and evidence basis

beads_rust retains and queries project work; the external agent or human still chooses and performs the work. Its shipped loop is retrieve ready issues, mark work in progress, implement elsewhere, close, and export. The tracker does not itself execute the issue's implementation task. The instruction is a request to a downstream reader, not evidence of compliance ([RT-CLM-work-cycle](#rt-clm-work-cycle), [RT-BAP-agent-instructions](#rt-bap-agent-instructions)). The boundary and SRC-1 register are in [boundary.md](boundary.md#source-register).

All findings below use SRC-1 at the reviewed commit. Added implementation coverage beyond the boundary's initial trace includes claim construction and transactional assignment checks, close bypass and auxiliary audit handling, MCP close validation, prompt selection and message construction, JSONL import transaction and row writers, agent-file update confirmation and backup, and upgrade checksum/replacement. Doctrine coverage includes the official skill's sync wording. No program, tests or providers were executed. Operation and benefit remain unobserved; the implementation conclusions describe wiring, not successful runs.

The shipped entry paths inspected are the CLI dispatcher, the optional feature-gated stdio MCP server, and public storage/sync library functions. The CLI also has JSONL-only operation. They are materially different: a command-level check is not automatically a library invariant, an issue commit is not an export commit, and a displayed recommendation is not an agent action. The core is a symbolic executable, not a distributed-parametric component ([RT-CMP-beads-rust](#rt-cmp-beads-rust)). An external host may use a model, but model version, mutability, context isolation and provider behavior are outside this source boundary; none is attributed to br.

### Ordinary invocation, then the next work decision

For an ordinary initialized-workspace `br create --title ... --description ... --json`, the caller supplies issue content and initiates the invocation. `main` parses flags, initializes output/logging and startup configuration, resolves actor attribution, determines automatic import/export eligibility, and arranges storage/write authority. Automatic import is conditional on command, stale-data controls and configuration, not an unconditional precondition of every read. Dispatch passes the preopened storage context into create. Create resolves configuration defaults and provenance, checks the workflow entry policy, captures description input once for recovery retry, constructs and writes the issue, obtains the stored export-shaped issue for structured output, and attempts auto-flush. See [RT-RTE-create-issue](#rt-rte-create-issue); SRC-1: `src/main.rs`, `src/cli/commands/create.rs`.

The immediate return is an issue or error, not completed project work. The next-step owner is the caller. A later `br ready` reads current stored state, selects eligible statuses and dependency readiness, applies assignee/label/type/priority/defer/parent filters, sorts, checks external blockers and limits the delivered result. JSON output uses a `ReadyIssue` projection, not the complete retained issue. This is a working-context selection mechanism: the caller requests a subset, code excludes other issues, and the omitted material remains available through further queries. It neither trims a host conversation nor creates a separate model context ([RT-RTE-ready-query](#rt-rte-ready-query)).

The shipped blurb calls `--status=in_progress` a claim. The stronger `--claim` path additionally sets the actor as assignee and asks storage to require an eligible assignment state. This difference matters for coordination: fetching a ready list reserves nothing, and merely changing status is not the same claim operation. A competing claimant or a later close/deferral can invalidate a saved selection ([RT-RTE-claim-issue](#rt-rte-claim-issue)).

Closing is another caller request. CLI close evaluates configured closure gates and uses atomic issue updates, but can admit an explicit reasoned policy bypass when allowed. Optional close-metadata persistence happens after the close and may fail without undoing it. MCP close uses its own validation and passes a non-bypass update to storage ([RT-RTE-close-issue](#rt-rte-close-issue)). The caller performs any repository commit/push prescribed by the blurb; that instruction must not be confused with an effect of the create or close operation.

### Alternate and forcing routes

Four forcing cases bound the important guarantees:

1. **Two claims after one ready result.** Transactional eligibility and assignment checks constrain `--claim`; they do not make the ready result a lease or make an actor string an authenticated principal. Same-actor reclaims can be idempotent unless exclusive claiming is configured ([RT-RTE-claim-issue](#rt-rte-claim-issue)).
2. **Mutation commits but export fails.** CLI create can print the stored issue and return through a best-effort auto-flush failure report. MCP instead acquires sync authority before mutation and can return a structured error after commit with `retry_mutation=false`. Neither path supports “every error means no write” or a universal DB-plus-JSONL atomicity claim ([RT-RTE-create-issue](#rt-rte-create-issue), [RT-RTE-mcp-request](#rt-rte-mcp-request)).
3. **Close gate fails or is bypassed.** Caller-supplied evidence and configured gates decide admission; CLI explicit bypass and best-effort auxiliary auditing defeat a universal “all closures satisfy policy and have complete audit metadata” claim. Storage transition enforcement is stronger than CLI-only preflight, but deliberately honors its bypass field ([RT-RTE-close-issue](#rt-rte-close-issue)).
4. **Retained state arrives through JSONL rather than create/update.** Import snapshots, validates, resolves collisions and writes through dedicated import row methods. It is not a replay of every interactive command's admission checks. JSONL-only operation also imports into a private empty database each invocation. Thus interactive checks cannot be generalized to every retained-state admission ([RT-RTE-jsonl-import](#rt-rte-jsonl-import)).

These are source-level countercases, not induced failures or concurrency experiments. The inspected locks and transactions require cooperating processes, working filesystem locking and the database engine's transaction contract. Direct external database/file edits and arbitrary code with the same OS privileges are not contained by these mechanisms. The capability surface comprises registered MCP tools and CLI/library operations; no supplied deployment specifies a current host tool grant set, authenticated caller set or OS isolation envelope. MCP is a local stdio integration, not evidence of a deployed sandbox or remote delegation system. No inspected route executes shell commands from issue text; the downstream host's shell access remains outside br's control boundary. This is not a repository-wide security certification.

### Instructions, context delivery and machinery changes

MCP is a second shipped driver, not just CLI formatting. It opens storage for each request, refreshes workflow policy under write authority for mutations, checks pending sync-merge state and coordinates export. Its registered resources and four prompts are read/context paths; its seven tools include issue mutations. The triage prompt fetches data, projects selected fields, caps some lists, and returns two user-role messages: data and guidance. The model host owns subsequent interpretation and tool calls. See [RT-RTE-mcp-request](#rt-rte-mcp-request), [RT-RTE-triage-prompt](#rt-rte-triage-prompt), [RT-BAP-triage-guidance](#rt-bap-triage-guidance); SRC-1: `src/mcp/mod.rs`, `src/mcp/prompts.rs`.

Retained instructions can change through `br agents` file management. The inspected update route detects a legacy/older blurb, constructs the shipped replacement, permits preview or refusal, and writes after confirmation or force. It persists instructions, not a learned method derived from session traces. A separate feature-gated upgrade command downloads release assets, compares the archive checksum with the release checksum asset and replaces the executable. This changes future machinery but relies on the release publisher and transport; matching a checksum from the same release is not independent approval of the code's semantics ([RT-RTE-agents-update](#rt-rte-agents-update), [RT-RTE-upgrade-binary](#rt-rte-upgrade-binary)). Build-time feature admission, including MCP, is also a capability choice made outside the running request; SRC-1: `Cargo.toml`, `src/main.rs`.

These mechanisms establish ways to admit state, instructions and executable successors. They do not establish autonomous improvement, exercised learning or theory criticism. Issue-content revision, retention, compaction and memory quality are left to the memory analyst. Available recovery/merge/doctor branches and developer release evaluators were not exhaustively audited here; no claim is made that the selected routes enumerate every maintenance guarantee. Host model calls, remote workers, provider-native tools and manual graph control are not hidden alternate br executors in the inspected paths: downstream choice remains at the external caller. That boundary does not establish their absence from a deployment.

## Shared records

### Components

#### RT-CMP-beads-rust
Label: beads_rust executable and library

Source-native identity: package `beads_rust`, CLI driver `br`, storage/sync library and optional MCP driver. Representational form: symbolic Rust code with fixed dispatch and validation rules. Storage substrate: shipped source/compiled executable; operational state is SQLite-family files and JSONL, not executable parameters. SRC-1: `Cargo.toml`, `src/main.rs`, `src/storage/sqlite.rs`, `src/mcp/mod.rs`. The frozen source version is pinned; whether any deployed binary matches it is unobserved. No distributed-parametric component is used by the inspected br routes; external model weights/version remain uninspected rather than classified as fixed.

> mcp = ["dep:fastmcp-rust"]
> --- `Cargo.toml`

### Operative objects

#### RT-OBJ-agent-blurb
Label: AGENT_BLURB

Source-native identity: the version-marked `AGENT_BLURB` installed into an agent instruction file. Representational form: natural-language workflow guidance with illustrative commands; consumed through host/agent interpretation, not executed as a script. Storage substrate: embedded Rust string, then project Markdown (`AGENTS.md`/`CLAUDE.md` variants). Its version markers support replacement/removal. Evidence: SRC-1, `src/cli/commands/agents.rs`; admission and authority are [RT-RTE-agents-update](#rt-rte-agents-update) and [RT-BAP-agent-instructions](#rt-bap-agent-instructions).

> pub const SUPPORTED_AGENT_FILES: &[&str] = &["AGENTS.md", "CLAUDE.md", "agents.md", "claude.md"];
> --- `src/cli/commands/agents.rs`

### Routes

#### RT-RTE-create-issue
Label: CLI create admission and return

Caller content/flags → startup/configuration → create implementation → storage transaction → structured issue output → attempted export. Owner: caller chooses the proposed issue; CLI and storage code decide admission. Actor attribution is configured/resolved, not proof of a human identity. Context includes defaults, workflow policy, optional parent/dependency provenance and one captured description input. The executor changes issue state, not project implementation files. SRC-1: `src/main.rs`, `src/cli/commands/create.rs`, `src/storage/sqlite.rs`.

- Immediate return: ID, stored export-shaped issue in JSON/TOON, human confirmation, dry-run preview or error.
- Later read-back: Stored issue fields are available to show/list/ready and export consumers in later invocations; export may still be pending.
- Delegated visibility: Returned content can cross to the invoking agent through its host; no worker is launched.
- Selection predicate: Create arguments/defaults and generated/resolved identity; dry-run and file-import branches differ from the ordinary single-issue write.
- Invalidation or expiry: Later issue edits/deletion can supersede content; no expiry of the ordinary create return is enforced in the host.
- Activation or effect: Storage validates and inserts issue state under its mutation path; downstream agent use of the returned issue is unobserved.
- Evidence limits: Ordinary initialized-workspace path traced; batch create/import and all recovery retries were not exhaustively audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes text and fields; validation/workflow/capacity code can reject. Human per-content approval is unresolved because the caller can be a program or human. Operating mode: open user/tool request, not a bounded learning experiment. Answer oracle: none identified for truth of issue content; validation checks permitted structure and workflow. Recovery includes JSONL-recovery retry around mutation; description is captured once. Later edits and sync/history mechanisms can change or restore state, but no automatic semantic undo is established.

Guarantee owner/enforcement: `SqliteStorage::create_issue`, with status/entry/capacity admission in the write transaction. Strength: invariant for the installed policy on this create path; it is not a universal issue-import or authenticated-access guarantee. Required external contract: engine transaction and filesystem/write-authority behavior. CLI policy preflight alone is not the guarantee.

> workflow_policy.validate_status(issue.status.as_str())?;
> --- `src/storage/sqlite.rs:7110-7135`

> auto_flush_after_create(&mut storage_ctx, ctx);
>     Ok(())
> --- `src/cli/commands/create.rs:235-245`

**Runtime return versus export.**

The command obtains the stored full issue before emission; export is a subsequent attempt. This makes a successful issue return weaker than “JSONL is already durably exported.” The CLI post-dispatch flush also reports failures without rolling back an issue write (SRC-1: `src/main.rs`). The official skill's “never automatic” wording is not an accurate universal description of this code path ([RT-CLM-explicit-sync](#rt-clm-explicit-sync)).

#### RT-RTE-ready-query
Label: Ready work selection

Caller → ready command → storage readiness query → external-blocker filtering → projected output. Owner: caller chooses query; symbolic filters and sort rules choose returned candidates; caller owns the next work decision. State includes workflow ready-status group, dependencies, deferrals and external project mappings. SRC-1: `src/cli/commands/ready.rs`, `src/storage/sqlite.rs`, `src/mcp/mod.rs`.

- Immediate return: Filtered/sorted/limited issue projection or human table; quiet mode can suppress output.
- Later read-back: The route reads retained state but does not itself create a new retained result; subsequent invocations query current state anew.
- Delegated visibility: CLI output or MCP ready-resource/prompt delivery can reach the host; there is no automatic assignment/delegation.
- Selection predicate: Configured ready statuses, local blocker exclusion, defer and caller filters; CLI checks external blockers before visible truncation, then hydrates labels for structured output.
- Invalidation or expiry: A result is a snapshot, not a lease; concurrent issue/dependency changes can make it stale immediately.
- Activation or effect: Delivers eligible work candidates; actual choice and task execution remain with the caller.
- Evidence limits: No measured retrieval quality, host context reduction or cross-project freshness result; MCP helper and CLI have different refresh plumbing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: software selects by policy/query; caller decides what to work on and can ignore the list. Answer oracle: readiness predicate is the operational reference, not an oracle of task value or correctness. Operating mode: open retrieval request. Guarantee owner: command/storage query, strength: policy; covers the queried state, not future eligibility or successful claim. External database mappings and reachable state bound external-blocker results.

> ready_issues.retain(|issue| !external_blockers.contains_key(&issue.id));
> --- `src/cli/commands/ready.rs`

> let total_before_truncation = ready_issues.len();
>     let truncated = args.limit > 0 && ready_issues.len() > args.limit;
>     if truncated {
>         ready_issues.truncate(args.limit);
>     }
> --- `src/cli/commands/ready.rs`

#### RT-RTE-claim-issue
Label: Claim-time coordination

Caller-selected ID → CLI update `--claim` → `IssueUpdate` with actor/assignment precondition → transactional eligibility and assignment check → issue update. SRC-1: `src/cli/commands/update.rs`, `src/storage/sqlite.rs`. Owner: caller proposes starting work; code decides whether current state permits that claim.

- Immediate return: Updated issue/coordination information or a claim conflict/validation error.
- Later read-back: Assignee/status persist for later queries and other callers.
- Delegated visibility: Other processes can see committed assignment on subsequent reads; there is no host-worker scheduling handoff.
- Selection predicate: Requested ID, current eligibility/assignee, claim exclusivity configuration and optional unchanged-time precondition.
- Invalidation or expiry: Close/deferral/assignment changes can invalidate a previous selection; `--claim` is not an indefinite authenticated lock on work.
- Activation or effect: Sets in-progress status and actor assignee only through admitted mutation; same-actor reclaim may be idempotent.
- Evidence limits: Concurrency correctness is source-grounded, not stress-tested here; configured actor identity is not verified identity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: software rejects invalid/conflicting claims; caller may reload and choose another task. Human participation is not determined by the CLI principal. Operating mode: open mutation request. Answer oracle: current database preconditions, not independent proof that the claimant will perform the work. Recovery: reload before retry after preconditions change; later explicit updates can change assignment/status. Guarantee owner: storage transaction/preconditioned update; strength: invariant on updates carrying `expect_unassigned`, subject to engine/cooperating-writer contracts. Plain `--status=in_progress`, direct assignee edits, imports and external DB edits do not inherit this claim-specific guarantee.

> expect_unassigned: args.claim,
>         claim_exclusive: args.claim && claim_exclusive,
> --- `src/cli/commands/update.rs`

> Some(current) if !updates.claim_exclusive && current == claim_actor => {
>                     /* same actor re-claim, idempotent */
>                 }
> --- `src/storage/sqlite.rs`

> format!(
>                             "claim preconditions changed for issue {id}; reload it before claiming"
>                         )
> --- `src/storage/sqlite.rs`

#### RT-RTE-close-issue
Label: Closure policy and override

Caller close request → closure gate evaluation → atomic status updates → auxiliary close metadata → output/export. CLI owner: close command and storage; MCP has a separate `validate_mcp_close` consumer before calling storage. SRC-1: `src/cli/commands/close.rs`, `src/storage/sqlite.rs`, `src/mcp/tools.rs`.

- Immediate return: Closed/skipped outcomes or validation error; optional metadata failure can be reported after the close committed.
- Later read-back: Closed status, reason, transition events and successfully recorded auxiliary metadata can reach later queries/audits.
- Delegated visibility: Other clients observe stored closure; the external agent may then choose new work.
- Selection predicate: Caller IDs, blockers/children, configured gates/required fields and transition policy; CLI permits an explicit bypass reason if policy allows.
- Invalidation or expiry: Later reopen/edit/import can change state; a close does not establish permanent correctness of the task.
- Activation or effect: Marks issues closed through atomic issue updates; optional auxiliary metadata is not in that same all-or-nothing effect.
- Evidence limits: No evidence that acceptance criteria actually held beyond supplied fields/gates; every helper and close variant was not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes closure and evidence, gate code decides, configured CLI override can veto the ordinary rejection. `allow_bypass: false` rejects that CLI override. MCP close rejects policy violations and constructs an update without the bypass field. Direct storage callers can supply `workflow_policy_bypass_reason`; storage checks that it is nonempty and deliberately skips transition enforcement. Therefore the guarantee is conditional on entry path and installed policy, not an authorization boundary against same-privilege code. Answer oracle: configured closure evidence checks, not independent task verification. Operating mode: open mutation request. Recovery: issue state can later be reopened; metadata failure does not roll back closure. Guarantee owner: storage transition preflight (invariant for non-bypass updates), CLI/MCP gate consumers (policy), auxiliary metadata (best effort). Required external contract: engine transactions and correctly installed policy.

> if args.bypass_policy && !policy_doc.allow_bypass {
> --- `src/cli/commands/close.rs`

> if let Some(reason) = update.workflow_policy_bypass_reason.as_deref() {
>                 if reason.trim().is_empty() {
>                     return Err(BeadsError::validation(
>                         "bypass_reason",
>                         format!("issue {id}: workflow-policy bypass reason must not be empty"),
>                     ));
>                 }
>                 continue;
>             }
> --- `src/storage/sqlite.rs`

> "failed to record closure-time policy metadata; close already committed"
> --- `src/cli/commands/close.rs`

#### RT-RTE-mcp-request
Label: MCP request mutation lifecycle

External MCP host → optional `br serve` stdio driver → registered handler → per-request `BeadsState::with_mutation` → storage → export → serialized result/error. `run_serve` registers seven tools, twelve resources and four prompts. Owner: host requests; handler/storage code decides execution. SRC-1: `src/mcp/mod.rs`, `src/mcp/tools.rs`.

- Immediate return: Serialized tool result or structured MCP error, potentially retaining a committed result and export-pending information.
- Later read-back: Mutated issues are retained; the server's optional read snapshot cache is cleared before mutation and guarded by file-state witnesses on reads.
- Delegated visibility: Host receives tool responses/resources; no model provider or remote worker is invoked by this lifecycle.
- Selection predicate: Tool registration/schema and arguments choose handler/IDs; mutation acquires DB-family and sync authority and checks pending-merge state before the closure.
- Invalidation or expiry: Request-local storage ends with the request; policy reload/cache invalidation handles later changes, without proving host-visible freshness under arbitrary external edits.
- Activation or effect: Runs the mutation closure, then flushes; a later export error need not mean mutation rollback.
- Evidence limits: FastMCP transport and database internals/deployed grants are outside inspection; no service invocation was observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: external caller proposes tool arguments; handlers and refreshed policy reject malformed/forbidden changes. Human per-change approval is not shown by the handler. Operating mode: open tool requests, no answer oracle for issue truth. Recovery: structured errors distinguish committed/pending outcomes so the host can sync/reload rather than duplicate the mutation; an unreadable commit witness produces an unknown-outcome error. Guarantee owner: `with_mutation` and `finish_mutation`; strength: protocol for structured outcome handling and cooperating lock acquisition, not atomicity of database plus export. The registered mutations use this wrapper; direct storage/sync/library writes and CLI paths are separate coverage. Required external contracts: lock semantics, engine commit behavior and host interpretation of returned errors.

> let policy = crate::close_policy::load_for_beads_dir(&self.beads_dir).map_err(to_mcp)?;
> --- `src/mcp/mod.rs`

> data["mutation_committed"] = json!(changed);
>                     data["previous_sync_pending"] = json!(previous_sync_pending);
>                     data["sync_pending"] = json!(true);
>                     data["retry_mutation"] = json!(false);
> --- `src/mcp/mod.rs`

#### RT-RTE-triage-prompt
Label: Data-bearing triage prompt

Host prompt request → focus validation → read storage → projected backlog context → two user-role messages. Owner: code chooses data by focus; host/model decides subsequent recommendations and any tool requests. SRC-1: `src/mcp/prompts.rs`, `src/mcp/mod.rs`.

- Immediate return: Current-state text and triage guidance, not a revised backlog.
- Later read-back: Reads accumulated issue state; no triage findings are persisted automatically by this prompt getter.
- Delegated visibility: Selected issue fields reach the external host as prompt messages; which model receives them is unobserved.
- Selection predicate: Focus defaults/validation and category queries; unassigned fetch limit 50/display 15, ready display 10, deferred fetch 50/display 15. Blocked context uses its own query/projection.
- Invalidation or expiry: Messages describe the read snapshot; future issue mutations require a new read to refresh them.
- Activation or effect: Constructs guidance asking the consumer to review ownership, blockers and priorities; actual reasoning/actions remain unobserved.
- Evidence limits: Prompt delivery is not evidence of compliance, improved planning or a host compaction mechanism.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: code selects and supplies; external agent proposes recommendations, caller/other tools would admit edits. Answer oracle: none supplied for good triage; operating mode is an open guided request. The instruction and issue summaries are natural-language consumer input even though JSON fields are embedded in the text. This working-context control excludes unselected issues and fields before delivery; it does not remove existing turns or isolate a sub-agent. Retained issues remain reloadable by show/list. Authority path: [RT-BAP-triage-guidance](#rt-bap-triage-guidance).

> content: Content::text(triage_instruction(focus).to_string()),
> --- `src/mcp/prompts.rs`

> const UNASSIGNED_FETCH_LIMIT: usize = 50;
> const UNASSIGNED_DISPLAY_LIMIT: usize = 15;
> const READY_DISPLAY_LIMIT: usize = 10;
> --- `src/mcp/prompts.rs`

#### RT-RTE-jsonl-import
Label: JSONL state admission

Explicit sync/automatic stale import/JSONL-only open → source snapshot → validation and collision planning → dedicated transactional row/relation writes → metadata/witnesses → foreign-key restoration and result. Owner: caller/config chooses input; import code decides structural/collision handling. SRC-1: `src/sync/mod.rs`, `src/storage/sqlite.rs`.

- Immediate return: Import counts/outcomes or error; explicit sync and automatic-startup callers have different outward output.
- Later read-back: Admitted issue fields/relations reach subsequent CLI/MCP queries; import witnesses support later stale-source decisions.
- Delegated visibility: Exported/shared JSONL can be consumed by another cooperating workspace; Git transport is not established by importing.
- Selection predicate: Snapshot parsing/normalization/validation, expected prefix, identity/collision action and import configuration; insert/update/skip outcomes differ.
- Invalidation or expiry: New imports/edits can supersede rows; source witnesses and retention cutoffs bound reconciliation rather than establishing permanent semantic truth.
- Activation or effect: Inserts or upserts rows and synchronizes labels, dependencies and comments; this is not replay of create/claim/close commands.
- Evidence limits: Full merge/reconcile/repair variants and every import admission rule were not audited; foreign-key restoration is performed after the apply transaction, so no universal error-implies-rollback claim is made.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: upstream author supplies JSONL, caller/config selects it, deterministic code validates and resolves actions. Human authorship/approval is unresolved. Operating mode: explicit or configured synchronization/reconstruction, not a curriculum. Answer oracle: schema/source/state consistency checks, not external validation of issue assertions. Recovery: snapshot/witness-based processing and separate repair/reconciliation facilities exist; no blanket automatic rollback guarantee is inferred. Path safety is conditional on supplied `ImportConfig` and its `beads_dir`/external-path settings. Ordinary insert/update uses import-specific writers, not interactive workflow admission; that limits the create/claim/closure guarantees above. Strength: protocol for this import pipeline, with engine and filesystem contracts required.

> storage.upsert_issue_for_import_in_tx(issue)?;
>                 sync_issue_relations(storage, issue)?;
> --- `src/sync/mod.rs:16315-16365`

> let apply_result = storage.with_write_transaction(|storage| -> Result<ImportResult> {
> --- `src/sync/mod.rs`

> let validate_foreign_keys = apply_result.is_ok();
>     let fk_restore_result = restore_foreign_keys_after_import(storage, validate_foreign_keys);
> --- `src/sync/mod.rs:16279-16280`

The source explicitly identifies the durable variant: JSONL-only opens reconstruct current state into a private database on each invocation. This is a different substrate lifecycle, not an agent-context fork.

> // relation rows first: for a fresh replacement that is the reviewed
>         // contract, and for a JSONL-only (`--no-db`) open, which imports the
>         // whole JSONL into a private empty database on every invocation, it
> --- `src/sync/mod.rs`

#### RT-RTE-agents-update
Label: Agent instruction replacement

Caller `br agents --update` → file/version detection → replacement construction from shipped blurb → preview/confirmation/force → backup attempt → atomic file write. Owner: operator/calling program initiates and may veto; software determines version eligibility and replacement content. SRC-1: `src/cli/commands/agents.rs`.

- Immediate return: Preview, already-current result, abort, performed update or error.
- Later read-back: Installed Markdown remains for a later agent-host instruction load; actual host loading is unobserved.
- Delegated visibility: Supported project instruction files can reach multiple future agents; no agent is launched by this operation.
- Selection predicate: Detected supported file, readable content and legacy/older blurb detection; current-version content is not automatically rewritten merely because text differs.
- Invalidation or expiry: Remove/update/manual editing can replace the section; no host-side cache invalidation is demonstrated.
- Activation or effect: Changes instruction-file bytes; host interpretation, compliance and improvement are separate unobserved effects.
- Evidence limits: The update branch was inspected; all installer/plugin/migration write variants were not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposed change: replace recognized old guidance with [RT-OBJ-agent-blurb](#rt-obj-agent-blurb), whose guidance prescribes ready/work/close/sync. Admission/rejection: dry run changes nothing; interactive refusal aborts; force bypasses confirmation, including machine-driven operation. Therefore initiation is not necessarily per-content human approval. Backup is attempted to `.md.bak` and can fail with warning; successful backup supports manual recovery but is not a universal rollback guarantee. Answer oracle: blurb/version recognition, no outcome oracle. Operating mode: explicit maintenance request. This is instruction distribution, not criticism of a theory against task evidence.

> require_force_for_json_action(force, ctx)?;
> --- `src/cli/commands/agents.rs:1330-1380`

> let backup_path = backup_agent_file(file_path, ctx);
> 
>     write_agent_file_atomically(file_path, new_content.as_bytes())?;
> --- `src/cli/commands/agents.rs:1365-1385`

#### RT-RTE-upgrade-binary
Label: Executable successor admission

Caller upgrade request → release selection → target archive/checksum assets → temporary download → checksum verification → extraction → executable replacement → version result. Owner: release publisher proposes executable; caller selects version/force; update code admits compatible assets/checksum. SRC-1: `src/cli/commands/upgrade.rs`, `Cargo.toml`, `src/main.rs`.

- Immediate return: Update/check/dry-run outcome or error; successful actual update reports successor version.
- Later read-back: Later program invocations can execute the replaced binary; this does not mutate the running source snapshot used for this analysis.
- Delegated visibility: No worker delegation; effects are on the installed executable and future users of it.
- Selection predicate: Feature-gated command, requested/latest release, target asset, version-newer or force decision, required checksum asset.
- Invalidation or expiry: A subsequent install/update can replace the binary; no general automatic post-install rollback was established.
- Activation or effect: Checksum-gated extraction and self-replacement/move change installed machinery; execution of the successor is unobserved.
- Evidence limits: Network/release authenticity, dependency replacement internals and deployed feature set are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection: missing asset/checksum or mismatch rejects before replacement. Human semantic review is not implied; updater construction disables dependency-level confirmation. Guidance is target/version/package compatibility, not retained operational criticism. Operating mode: explicit maintenance request, with check/dry-run alternatives. Answer oracle: published checksum and version comparison, not proof of program correctness or improvement. Recovery is bounded to download/extract/replace error handling and later explicit reinstall/version choice; rollback was not audited. Guarantee owner: `update_with_checksum`; strength: protocol. Covered path is this command, not arbitrary installer/release pipelines; external trust in publisher and transport is required.

> let expected_sha256 =
>         download_expected_sha256(checksum_asset, target_asset.name(), updater.auth_token())?;
>     verify_sha256(&tmp_archive_path, &expected_sha256)?;
> --- `src/cli/commands/upgrade.rs`

> self_replace::self_replace(new_exe).map_err(|err| BeadsError::upgrade(err.to_string()))?;
> --- `src/cli/commands/upgrade.rs`

### Claims

#### RT-CLM-work-cycle
Label: Shipped work lifecycle

Claimed operation: agents should retrieve, mark in progress, implement, close and export. SRC-1: `src/cli/commands/agents.rs`. This is doctrine, with tracker mechanisms wired but external work/compliance unobserved. The blurb's ordinary status update is weaker coordination than [RT-RTE-claim-issue](#rt-rte-claim-issue).

> 1. **Start**: Run `br ready` to find actionable work
> 2. **Claim**: Use `br update <id> --status=in_progress`
> 3. **Work**: Implement the task
> 4. **Complete**: Use `br close <id>`
> 5. **Sync**: Always run `br sync --flush-only` at session end
> --- `src/cli/commands/agents.rs`

#### RT-CLM-explicit-sync
Label: Explicit sync instruction versus automatic export

Claimed operation: the shipped skill describes sync as never automatic. SRC-1: `.claude/skills/br/SKILL.md`. That wording conflicts with the inspected auto-flush calls and conditional auto-import startup. It can serve as a conservative operator instruction to explicitly export, but not as a universal implementation claim. Automatic export is also not automatic Git commit. This discrepancy is retained rather than silently selecting one doctrine surface.

> ### Sync (EXPLICIT -- never automatic)
> --- `.claude/skills/br/SKILL.md`

Implementation counterevidence is in [RT-RTE-create-issue](#rt-rte-create-issue) and [RT-RTE-mcp-request](#rt-rte-mcp-request).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-instructions
Label: Project instruction authority

Consumer: future coding agent/human and its instruction-loading host. Channel: installed supported Markdown instruction file containing [RT-OBJ-agent-blurb](#rt-obj-agent-blurb). Force: natural-language workflow request; binding priority and compliance depend on the external host, not a br enforcement point. Horizon: later sessions while the file remains installed. Source: SRC-1, `src/cli/commands/agents.rs`; write mechanism [RT-RTE-agents-update](#rt-rte-agents-update). No observed host load or exercised behavioral change is supplied.

> - Check `br ready` at session start to find available work
> - Update status as you work (in_progress → closed)
> - Create new issues with `br create` when you discover tasks
> --- `src/cli/commands/agents.rs`

#### RT-BAP-triage-guidance
Label: MCP triage guidance authority

Consumer: external host/model receiving prompt messages. Channel: user-role text delivered by [RT-RTE-triage-prompt](#rt-rte-triage-prompt), combining projected retained issue data with static instructions. Force: advisory model input, not tool execution or a storage invariant. Horizon: the host's receiving conversation and any later action it chooses; no persisted triage result is automatic. Source: SRC-1, `src/mcp/prompts.rs`. The prompt requests judgment and recommendations but does not prove they occurred.

> "Review the blocked issues above. For each one:\n\
>              1. Check what's blocking it (use show_issue on the blockers)\n\
>              2. Determine if the blocker can be resolved or if the dependency should be removed\n\
>              3. Suggest concrete next steps to unblock progress"
> --- `src/mcp/prompts.rs`

## Annotations

none
