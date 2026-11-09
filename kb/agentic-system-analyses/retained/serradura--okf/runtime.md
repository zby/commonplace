---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OKF runtime baseline: skill-led knowledge work, retrieval surfaces, guarded Pro writes and governance installation."
run-id: AAS-2026-11-08-okf-8bc42addf404-01
reviewed-boundary: "cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c"
---

# OKF runtime report

## Runtime account

### Responsibility and evidence

OKF delegates semantic work to an external agent or human. It ships instructions, Ruby commands, retrieval servers, a terminal browser and optional host hooks; it does not supply the enclosing model conversation loop. The ordinary skill-led invocation is a user task in a project carrying a bundle: the agent orients, retrieves selected concepts, performs the task and records durable discoveries. Code computes structure and checks; the agent judges meaning. This division is explicit in SRC-1, `skills/okf/SKILL.md` and `skills/okf/playbooks/consume.md`, retained in [RT-RTE-skill-work](#rt-rte-skill-work). The agent's model implementation is outside the frozen source, as described in [RT-CMP-agent](#rt-cmp-agent).

All findings below use SRC-1 at the boundary's frozen revision. Source text establishes implementation wiring or authored requests, not exercised operation. No target, test, example, model provider or service was executed. No supplied run evidence establishes activation, reliability, benefit or host compliance. Additional inspected coverage beyond the boundary's initial trace includes the CLI search consumer, SafeRead, MCP resource reads and output cuts, MCP residency/fallback code, Pro event parsing, target/root scoping, shell and text guards, writer planning/conservation, closing and scaffold implementations, browser registry mutation, and TUI workspace registry operations. These supply implementation evidence. The refine and instruction-restructuring playbooks supply doctrine/design evidence, not executed optimization.

### Ordinary invocation, return and persistence

The task's principal is the requesting user; the next-step owner is the external agent. Bundle identities are directories or registry slugs (`@slug`), while a concept id is resolved through the parsed bundle rather than blindly treated as an OS path. Skill intent routing chooses consume/search/maintain and other playbooks. Natural-language instructions guide that choice; symbolic Ruby code dispatches actual commands. The ordinary task has no OKF-owned model sampling policy, conversation checkpoint, retry budget or terminal-answer evaluator (SRC-1, `skills/okf/SKILL.md`, `gems/okf/lib/okf/cli.rb`, `gems/okf/lib/okf/bundle/folder.rb`). These responsibilities remain with the host, not with the deterministic command.

The consume procedure starts with `dirs`, descends through `index`, checks the log, then follows only relevant concepts. A pointed question switches to search. A shell invocation enters CLI dispatch, loads the folder through Reader, queries symbolic search/filter rules, and returns rows or JSON; the agent then reads selected bodies and produces its own answer. `@all` and group searches can span several bundles. File reads eagerly parse visible Markdown; unusable files are recorded separately rather than aborting the whole read. Hidden paths are excluded by the reader's glob. These distinctions bound what a zero-match result can mean (SRC-1, `gems/okf/lib/okf/cli/search.rb`, `gems/okf/lib/okf/bundle/reader.rb`).

The terminal output of this ordinary workflow is an agent answer and, when the agent follows the write-back instruction, edited concept/index/log files. The write-back decision and prose are not produced by the search command. Host Write/Edit/shell actions can change disk directly; a library caller can instead use Folder.save and Writer. The latter validates a temporary bundle before promotion under a lock, refuses an existing target unless overwrite is enabled, and attempts backup restoration if overwrite promotion fails. That guarantee belongs to Writer, not to every way an agent can edit Markdown (SRC-1, `gems/okf/lib/okf/bundle/folder.rb`, `gems/okf/lib/okf/bundle/writer.rb`; [RT-RTE-publish-bundle](#rt-rte-publish-bundle)). Memory revisions, provenance and retained-content transformations are left to the memory analyst; these paths identify their executors and admission boundaries.

### Material alternate surfaces

| Surface | Trigger, identities and owner | Execution, state, return and recovery |
|---|---|---|
| MCP tools/resources/prompts | An external host sends a request to a stdio process or shared HTTP server; served bundle slugs identify the corpus. The host or model chooses tool calls; the host can also attach a resource without a model retrieval decision. | Shared Server definition routes to registry, backend and Folder. Search returns selected rows, read_concept returns full original Markdown, resources return root index or exact concept text. Domain errors become tool errors or resource errors. Residency refresh occurs between requests; body reads are live through containment guards. See [RT-RTE-mcp-retrieve](#rt-rte-mcp-retrieve). |
| Browser and TUI | Human navigation or query; selected registry entries and concept ids. | Browser App serves GET views with a boot-time structural snapshot and live concept/log reads. TUI Workspace searches a held corpus and can reload. Both have registry-management paths, not just bundle browsing. Browser Hub mutations require writable mode, a registry, host-matching Origin/Referer and a boot token; TUI uses registry methods directly. See [RT-RTE-registry-manage](#rt-rte-registry-manage). |
| Base plugin post-edit hook | Host PostToolUse after Write/Edit/MultiEdit; file_path and session_id select bundle and feedback. | Runs validate/lint subprocesses, emits at most twelve finding lines plus a remainder notice as additionalContext, and exits zero. Environment and file-marker opt-outs exist; malformed CLI JSON becomes empty reports. It is feedback, not rollback or write prevention. See [RT-RTE-curation-feedback](#rt-rte-curation-feedback). |
| Pro operating profile | User installs scaffold and host loads seeded settings plus generated hook wrapper. | Pre-edit guards can ask/refuse, post-edit checks can report/refuse at their hook phase, Stop checks completed state, and SessionStart supplies a computed banner. Git and CI provide distinct later doors. The host protocol decides what exit 2 and permissionDecision mean. See [RT-RTE-pro-gates](#rt-rte-pro-gates). |
| Pro mechanical writers | Caller requests capture/promote/demote/journal-open/close. | Deterministic transforms declare a delta, conserve it, then atomically replace each affected file. These are a supported Bash path that need not contain a shell mutator token. They have construction-time restrictions rather than relying on text guards. See [RT-RTE-pro-writes](#rt-rte-pro-writes). |
| Runtime capability/governance installation | Operator installs an extension, invokes scaffold/upgrade, or requests instruction restructuring. | Ruby requires discovered plugin code; scaffold rewrites gem-owned machinery while preserving seeded adopter content. Refine produces a proposal before approved execution. See [RT-RTE-extension-load](#rt-rte-extension-load), [RT-RTE-governance-install](#rt-rte-governance-install), and [RT-RTE-refine-proposal](#rt-rte-refine-proposal). |

Sources for this table are SRC-1: `gems/okf-mcp/lib/okf/mcp/server.rb`, `gems/okf-mcp/lib/okf/mcp/resources.rb`, `gems/okf-mcp/lib/okf/mcp/cli.rb`, `gems/okf/lib/okf/server/app.rb`, `gems/okf/lib/okf/server/hub.rb`, `gems/okf-tui/lib/okf/tui/workspace.rb`, `plugin/hooks/scripts/curate.rb`, `gems/okf-pro/lib/okf/pro/cli.rb`, `gems/okf-pro/lib/okf/pro/writes.rb`, `gems/okf-pro/lib/okf/pro/scaffold.rb`, `gems/okf/lib/okf/cli.rb`, and `skills/okf/playbooks/refine.md`.

### Four forcing cases and guarantee limits

1. **A direct edit is not a validated publication.** Writer checks its temporary tree before rename, but the supplied skill explicitly uses general Read/Write/Edit/Bash tools and asks for validation after edits. Pro's direct tool guard examines event-added text; its specialized writers instead constrain their own transformations. Therefore Writer's conformance invariant and Pro's conservation check cannot be generalized to arbitrary file changes. The base curation hook cannot undo an already completed edit (SRC-1, `skills/okf/SKILL.md`, `gems/okf/lib/okf/bundle/writer.rb`, `gems/okf-pro/lib/okf/pro/writes.rb`, `plugin/hooks/scripts/curate.rb`).
2. **Guarded text and shell are different channels.** Pro checks both new_string/new_str and arrays of edits, and detects block/flow spellings of verified. But an empty JSON object parses successfully and supplies no target, and guards then return no findings. That is not evidence that the actual host sends such a malformed edit event. ShellGuard separately asks on recognized bundle-writing command shapes; it is a heuristic, not a shell interpreter. A supported `okf pro capture` command has no shell mutator pattern and is governed by its writer instead. External editors, custom host tools, arbitrary extension Ruby and other subprocess interfaces are not enclosed by the named Claude tool matchers. Later commit/CI checks cover other state questions, not an authenticated proof that every verified field was human-approved (SRC-1, `gems/okf-pro/lib/okf/pro/event.rb`, `gems/okf-pro/lib/okf/pro/guards.rb`, `gems/okf-pro/lib/okf/pro/shell_guard.rb`, `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json`). No complete attestation-exclusion claim is warranted.
3. **A log with one enormous or unrecognized heading remains byte-bounded on MCP.** bounded_log's blank, bare-title, unsplittable and normal date-group branches all reach sized_log. It cuts supplied content to LOG_BUDGET times max(limit,1), scrubs a split UTF-8 tail, recounts surviving headings and announces truncation. The bound is per file's content, not the whole JSON envelope, number of files, all resource reads, or read_concept. Larger limits request larger content budgets; full concept reads are deliberately not such a bound. This is an implemented output control, not evidence of token savings in a model run (SRC-1, `gems/okf-mcp/lib/okf/mcp/server.rb`).
4. **Live bytes and fresh selection metadata can disagree.** MCP's folder cache fingerprints Markdown path/mtime/size, memoized for a request; equal-size changes preserving mtime can escape invalidation. read_concept/resources still read live bytes at a known cached id/path. Folder.log_entries can fall back to the loaded reserved snapshot after a vanished or escaping live file. Browser index/graph/search structure is a boot snapshot. Thus the stated live-read intention does not establish universal fresh search, graph or id mappings. SafeRead rejects resolved symlink escapes but explicitly leaves hardlinks and a resolve/open race outside its guarantee (SRC-1, `gems/okf-mcp/lib/okf/mcp/memory_backend.rb`, `gems/okf/lib/okf/bundle/folder.rb`, `gems/okf/lib/okf/server/app.rb`, `gems/okf/lib/okf/safe_read.rb`).

### Controls, context and isolation

Capability, grant and isolation differ here. The general skill advertises Read/Write/Edit/Grep/Glob/Bash; MCP exposes retrieval handlers; Pro supplies a particular hook installation. None proves the current grants of an external host. MCP defaults to loopback HTTP or host-owned stdio. A non-loopback bind warns that all served bundles are readable without authentication: the Host allowlist is a DNS-rebinding defense, not a user authorization boundary (SRC-1, `skills/okf/SKILL.md`, `gems/okf-mcp/lib/okf/mcp/cli.rb`, `gems/okf-mcp/lib/okf/mcp/http.rb`). Installed Ruby extensions run in the command process, not in a demonstrated sandbox.

The inspected working-context controls are selective supply, not conversation compaction: agent-directed index-first retrieval, MCP row limits/projection, log byte cuts, host-attached resources, post-edit feedback filtering, and a SessionStart state banner that replaces repeated file discovery with computed state. They neither remove old conversation turns nor create a demonstrated isolated sub-agent frame. The external host decides whether to follow the routing and what stays in its window. A stack-frame analogy does not establish an OKF-owned frame/pop operation here; Ruby cache eviction affects implementation residency, not previously delivered model context. Reload routes are subsequent search/read calls, TUI reload, or a new server snapshot, not references the context automatically follows (SRC-1, `skills/okf/SKILL.md`, `gems/okf-mcp/lib/okf/mcp/server.rb`, `gems/okf-mcp/lib/okf/mcp/resources.rb`, `gems/okf-pro/lib/okf/pro/closing.rb`, `gems/okf-tui/lib/okf/tui/workspace.rb`).

Load-bearing controls have different strengths:

| Owner / enforcement point | Strength and covered paths | Required external contract / limits | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|
| Writer.call before promote | invariant — validated materialized bundle through Writer only | Ruby filesystem/rename/lock behavior; excludes direct edits | wired | uninspected |
| Pro wrapper around recognized hook checker | protocol — missing checker/marker and unexpected status normalize to exit 2 | Host must invoke wrapper and honor blocking phase/status/ask; marker is identification, not cryptographic authentication | wired | uninspected |
| Pro Conserve before planned writes | invariant — declared line-multiset delta through mechanical writers | Does not prove semantic correctness, ordering, concurrent-update safety or multi-file transactionality | wired | uninspected |
| Base plugin feedback | best effort — recognized post-edit file events | Can be disabled; exits zero; host must consume feedback | wired | uninspected |
| MCP handlers plus SafeRead | protocol — registered served roots and guarded file reads | Optional backend internals and host isolation uninspected; no HTTP user authentication guarantee | wired | uninspected |
| Refine approval instruction | policy — compliant skill-following execution | Agent/user must preserve proposal/approval separation; no executable approval gate shown | claimed | uninspected |

The supporting route records below retain the evidence and decision roles. No measured performance claim follows from cache design, authored benchmark comments or test presence.

## Shared records

### Components

#### RT-CMP-agent
Label: External agent consuming the OKF skill

The source-native role is the OKF expert addressed as “you” by the skill. Its instruction content is natural language stored in Markdown; its external model computation is distributed-parametric, with parameter storage outside SRC-1. The inspected route does not identify a model/provider/version or update protocol. Whether parameters change during operation is uninspected; exact version pinning and whether a mutable endpoint can resolve to another model are uninspected because no endpoint is selected here. This prevents model-fixity or provider-internal-learning conclusions, not the skill's file-based behavioral path. SRC-1, `skills/okf/SKILL.md`:

> All the power lives in *conventions* and *judgment*, not in
> enforcement. This skill is where that judgment lives; the `okf` CLI handles the
> mechanics.
> --- `skills/okf/SKILL.md`

#### RT-CMP-cli
Label: OKF CLI and deterministic bundle kernel

Source-native Ruby command registry, Folder/Reader/Writer and pure bundle analyzers; symbolic code stored as Ruby package files, with parsed concepts and derived maps in process memory. Not a distributed-parametric component. The same CLI can load extension code; package installation and load-path provenance remain external. SRC-1, `gems/okf/lib/okf/cli.rb`, `gems/okf/lib/okf/bundle/folder.rb`, `gems/okf/lib/okf/bundle/reader.rb`:

> command.new(out: @out, err: @err, runner: @runner, input: @input).call(argv)
> --- `gems/okf/lib/okf/cli.rb`

### Operative objects

#### RT-OBJ-skill
Label: Shipped OKF skill and routed playbooks

Natural-language procedural guidance in Markdown files, consumed by an external agent. Frontmatter includes symbolic host metadata, including the declared tools; it is not proof of an actual grant. Runtime relevance is instruction supply and semantic decision ownership, not a second declaration of bundle memory. SRC-1, `skills/okf/SKILL.md`:

> allowed-tools: Read Write Edit Grep Glob Bash
> --- `skills/okf/SKILL.md`

#### RT-OBJ-settings
Label: Pro hook registrations and executable wrapper

Symbolic JSON registrations and Bash wrapper stored in scaffold templates and copied into adopter projects. The JSON selects host phases/tool names; the script maps checker identity and status to host protocol output. This is behavior-determining machinery, not semantic knowledge. SRC-1, `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json`, `gems/okf-pro/lib/okf/pro/template/gem/.claude/hooks/run`:

> MARKER='okf-pro-enforcer v1'
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/hooks/run`

### Routes

#### RT-RTE-skill-work
Label: Skill-led consume and maintain work

User task → external agent intent routing → CLI orientation/search → selected bodies → task answer; durable discoveries can trigger agent-authored file edits and structural checks. Principal is the user; semantic proposer/decider is the agent, subject to host/user permissions. Natural-language playbooks guide open task work; symbolic commands compute map/search/check outputs. There is no expected-answer oracle in this procedure: search results and lint findings are evidence, not reference answers. Per-content human approval is not required by the general maintain playbook; the separate Pro profile can add targeted asks.

- Immediate return: CLI rows/JSON, selected Markdown and ultimately an agent-authored task answer.
- Later read-back: Edited concept/index/log files are available to later bundle readers; semantic revision details belong to the memory analysis.
- Delegated visibility: uninspected — external host delegation/context sharing is not specified by this route.
- Selection predicate: Agent task judgment chooses branches/bodies; CLI search ANDs terms and applies requested filters, with explicit scan/index/fuzzy/regexp alternatives.
- Invalidation or expiry: New CLI invocations reload folders; knowledge correction is requested through maintain, not automatically warranted by file age.
- Activation or effect: Instruction delivery and command execution are afforded; actual host compliance or changed task behavior is unobserved.
- Evidence limits: Implementation of deterministic reads and authored workflow only; no agent session trace or outcome oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `skills/okf/playbooks/consume.md`, `skills/okf/playbooks/maintain.md`, `gems/okf/lib/okf/cli/search.rb`, `gems/okf/lib/okf/bundle/reader.rb`:

> 3. **Write-back reflex:** if you learn something durable while working — a fact the
>    bundle lacks, a link it is missing, a concept that no longer matches reality —
>    switch to [maintain](maintain.md) and record it. That reflex is what keeps the
>    bundle alive.
> --- `skills/okf/playbooks/consume.md`

> 5. Run `validate`, then `lint` to catch the curation drift the change introduced —
>    new orphans, broken sources, dangling index entries, footnotes that lost
>    their source.
> --- `skills/okf/playbooks/maintain.md`

#### RT-RTE-mcp-retrieve
Label: MCP retrieval and host attachment

Host request → Server definition → served registry root → selected backend/Folder → tool/resource response. CLI boot selects stdio or HTTP and detects optional backend; memory backend serves fallback and always supplies live file reads. Decisions about tool choice and interpretation belong to host/model; Ruby owns deterministic selection. Prompts are returned as user-role messages. Tools reject domain/argument failures through readable error responses; optional backend failure during detection falls back, not necessarily failures during every later query.

- Immediate return: JSON text plus structuredContent for structured tools, raw Markdown for read_concept, resource TextContents, or a domain error.
- Later read-back: Reads existing bundle files; no retained write is performed by inspected shipped retrieval handlers. Backend cache is process-local; optional backend disk behavior is uninspected.
- Delegated visibility: Resource attachment permits host-supplied context without a model deciding to fetch it; visibility to other agents is host-owned and uninspected.
- Selection predicate: Served slug allowlist; omitted search bundle searches served set, group expands members; requested filters/projection/limit then select output. Resource ids resolve by map, not arbitrary filesystem paths.
- Invalidation or expiry: Per-request path/mtime/size fingerprints refresh cached folders; served-root changes prune residency and corpora; four prepared corpora retained by LRU. Same-size/mtime edits can evade refresh. Live concept reads recheck containment.
- Activation or effect: Bounded data supply is wired, including log content byte cuts and truncation signaling; semantic use and benefit remain unobserved.
- Evidence limits: Optional okf-sqlite3 implementation and MCP SDK internals are external. No whole-response byte bound or authentication claim; no host execution trace.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `gems/okf-mcp/lib/okf/mcp/server.rb`, `gems/okf-mcp/lib/okf/mcp/resources.rb`, `gems/okf-mcp/lib/okf/mcp/backend.rb`, `gems/okf-mcp/lib/okf/mcp/memory_backend.rb`, `gems/okf-mcp/lib/okf/mcp/http.rb`:

> text = id ? concept_text(context, slug, id, uri) : root_index_text(root)
> --- `gems/okf-mcp/lib/okf/mcp/resources.rb`

> return row unless content.bytesize > budget
> --- `gems/okf-mcp/lib/okf/mcp/server.rb`

> kept = content.byteslice(0, budget).scrub("")
> --- `gems/okf-mcp/lib/okf/mcp/server.rb`

> [ path, stat.mtime.to_f, stat.size ]
> --- `gems/okf-mcp/lib/okf/mcp/memory_backend.rb`

> A same-second edit that also
>       # preserves the byte count is still invisible; catching that needs a
>       # content hash on every call, which is the whole cost this cache exists
>       # to avoid.
> --- `gems/okf-mcp/lib/okf/mcp/memory_backend.rb`

#### RT-RTE-publish-bundle
Label: Validated library publication

Folder.save → Writer.call → temporary materialization → Validator over Reader result → rename promotion under an exclusive lock. Caller proposes bundle contents and chooses overwrite; code admits structurally valid materialization or raises. Validation supplies a structural acceptance predicate, not a semantic answer oracle. Operating mode is a caller-requested publication, not an autonomous improvement loop. Direct agent edits do not use this gate.

- Immediate return: true from Writer, Folder from save, or exception/refusal before publication.
- Later read-back: Promoted directory becomes the bundle for subsequent loads.
- Delegated visibility: inapplicable — no worker dispatch in this publication mechanism.
- Selection predicate: Caller-supplied concepts, index_files and log_files; Markdown-relative path validation and §11 conformance precede promotion.
- Invalidation or expiry: overwrite replaces the directory; no semantic expiry is decided here.
- Activation or effect: Filesystem publication is wired, with existing-target refusal unless overwrite is enabled.
- Evidence limits: Lock covers this writer's cooperating invocations; direct editors do not acquire it. Filesystem crash behavior and concurrent external edits unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection: Ruby validator can veto malformed output; human participation is caller-dependent, not an enforced per-content approval. Recovery: temporary tree cleanup in ensure; overwrite renames old bundle aside and attempts to restore it after failed promotion. No general version-history rollback is supplied by this call. Guidance is conformance code; the persisted result is bundle files. SRC-1, `gems/okf/lib/okf/bundle/writer.rb`:

> result = Validator.call(Reader.read(temp_path))
>             raise ValidationErrorFromResult.new(result), "materialized bundle is invalid" unless result.valid?
>
>             promote(temp_path)
> --- `gems/okf/lib/okf/bundle/writer.rb`

#### RT-RTE-curation-feedback
Label: Advisory post-edit curation

Host PostToolUse → edited Markdown path → upward bundle detection → validate/lint subprocesses → filtered findings as additionalContext. Ruby decides which evidence to present; the agent decides whether to act. This is feedback after mutation, not an admission gate or semantic oracle.

- Immediate return: Optional host JSON context, always exit zero at script boundary.
- Later read-back: inapplicable — findings do not themselves revise knowledge; a temporary per-session marker only suppresses repeated missing-CLI notices.
- Delegated visibility: uninspected — additionalContext delivery beyond the invoking host is unspecified.
- Selection predicate: Markdown file_path; opt-out environment/file marker; all validation errors plus edited-file warnings and relevant lint membership findings; first twelve lines plus remainder notice.
- Invalidation or expiry: Reports recomputed after eligible edit; session marker persists in temporary storage for notification suppression.
- Activation or effect: Context emission wired; repair is a requested agent response, not enforced or observed.
- Evidence limits: CLI status is not a hard gate; malformed report JSON becomes an empty report and top-level StandardError is silenced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `plugin/hooks/scripts/curate.rb`:

> out, _err, _status = Open3.capture3("okf", verb, root, "--json")
>         out
> --- `plugin/hooks/scripts/curate.rb`

> exit 0
> --- `plugin/hooks/scripts/curate.rb:246-246`

#### RT-RTE-pro-gates
Label: Pro host, commit and CI gates

Seeded settings select tool phases → wrapper buffers event and invokes `okf pro hook CHECK` → CLI validates check/event → text/shell/state checker → empty/pass, ask JSON or block. The checker owns deterministic detection; owner approval decides attestation and recognized risky shell writes. CLI cannot verify whether a person actually read the source. Guidance is the Pro rules; structural checker outputs are not expected semantic answers. Open project work, not a fixed experiment/curriculum.

- Immediate return: Wrapper forwards protocol stdout/stderr; statuses other than recognized 0/2 normalize to 2. CLI returns ask JSON for owner decisions or blocking messages.
- Later read-back: SessionStart reads board/log/project state and prior snapshot into a banner. Stop independently recomputes checks after dirty Markdown work; no automatic knowledge correction.
- Delegated visibility: uninspected — registered hooks govern matched host events, not a specified remote-worker or custom-tool protocol.
- Selection predicate: Edit/Write/MultiEdit added text and Target scoping; Bash mutator/path heuristic; Stop skips recursive stop_hook_active and clean sessions. Git pre-commit materializes staged tree, checks record changes and audits it; CI validates/lints/audits checked-out state.
- Invalidation or expiry: Checks read current event/state; banner labels prior snapshot as not live and instructs state refresh after writes. Seeded settings do not automatically track upgrades.
- Activation or effect: Requests for host ask/block decisions and later Git/CI refusals are wired, conditional on configured and honored integration. No universal write exclusion follows.
- Evidence limits: Host protocol/permission grants external; empty or incomplete object events can supply no target without JSON parse failure. Shell patterns are not complete shell semantics. Git hooks require per-clone setup, CI protection policy is external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: agent supplies edit text; code can reject recognized cases; owner can approve/deny an ask. Existing past journal edits are denied by journal_guard, creation of missing past days asks. Rejection occurs before matched tools only at the pre-tool phase; post-edit/Stop/commit checks are later checks, not rollback. Recovery requires explicit correction of state or environment and retry. The wrapper can retry after restoring Bundler environment unless disabled. Its marker proves a recognizable checker was reached under its own protocol, not protection against malicious local code. No human per-content approval is required for ordinary unverified concept edits. SRC-1, `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json`, `gems/okf-pro/lib/okf/pro/template/gem/.claude/hooks/run`, `gems/okf-pro/lib/okf/pro/cli.rb`, `gems/okf-pro/lib/okf/pro/event.rb`, `gems/okf-pro/lib/okf/pro/guards.rb`, `gems/okf-pro/lib/okf/pro/shell_guard.rb`, `gems/okf-pro/lib/okf/pro/closing.rb`, `gems/okf-pro/lib/okf/pro/template/gem/.githooks/pre-commit`, `gems/okf-pro/lib/okf/pro/template/gem/.github/workflows/okf-pro.yml`:

> return [] if Target.for(event).nil?
>         return [] unless attests?(event.added_text)
> --- `gems/okf-pro/lib/okf/pro/guards.rb`

An empty event file_path reaches a specific early return in BundleRoot.containing, called by Target.for. This establishes the branch behavior, not real-host reachability. SRC-1, `gems/okf-pro/lib/okf/pro/target.rb`, `gems/okf-pro/lib/okf/pro/bundle_root.rb`:

> def containing(path)
>         return nil if path.to_s.empty?
> --- `gems/okf-pro/lib/okf/pro/bundle_root.rb`

> return [] if command.empty?
>         return [] unless MUTATORS.any? { |m| command.match?(m) }
> --- `gems/okf-pro/lib/okf/pro/shell_guard.rb`

> 0) exit 0 ;;
>   2) exit 2 ;;
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/hooks/run`

> return [] if event.stop_hook_active?
> --- `gems/okf-pro/lib/okf/pro/closing.rb`

#### RT-RTE-pro-writes
Label: Targeted mechanical Pro writers

Caller request → CLI selection/arguments → Writes pure Board/Log transform → declared-delta Conserve check → Scaffold atomic file replacement. Software decides the mechanical change and can veto ambiguity, cap excess or invalid shape. Caller identity does not establish human authorship/approval. No expected-answer oracle; structural predicates constrain transformation rather than judge task truth. Open operational requests, with cap from the board rather than an immutable numeric policy.

- Immediate return: Success description or refused result/CLI exit 2; promote and close explicitly state remaining semantic/journal/extraction obligations.
- Later read-back: Changed board, journal index/day, project closure index and log are read by state, snapshot, audit, later agents and users.
- Delegated visibility: inapplicable — writers do not launch or return from delegated computation.
- Selection predicate: Named verb and keyed selector; capture rejects blank/multiline input, promote checks declared cap, close restricts project to one segment and heading-shaped first line; rewritten existing files are checked for escaping symlinks.
- Invalidation or expiry: Latest file text supplies transform input. No separate learned policy or per-content expiry is generated.
- Activation or effect: Selected filesystem changes wired after conservation check; journal-open and close have per-file, not set-wide, atomicity.
- Evidence limits: Line multiset conservation does not validate prose truth or line placement by itself. No concurrent compare-and-swap or group transaction demonstrated; execution/crash outcomes unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal/admission: user or agent requests action; Ruby constructs candidate texts from prior file contents, declares additions/removals/moves, refuses mismatched deltas before writes. This admits operational knowledge/work-state changes, not arbitrary generated frontmatter. Guidance resides in symbolic grammar and Pro operational rules. Recovery: journal-open checks file/index separately so rerun repairs a half-pair; close computes all plans before writing, but an interrupted sequence can leave a pairing failure for audit. No automatic full rollback. SRC-1, `gems/okf-pro/lib/okf/pro/writes.rb`, `gems/okf-pro/lib/okf/pro/conserve.rb`, `gems/okf-pro/lib/okf/pro/scaffold.rb`:

> findings = Conserve.check(before, after, added: added, removed: removed, moved: moved)
>         return [ nil, refuse(conservation_refusal(verb, path, findings)) ] unless findings.empty?
> --- `gems/okf-pro/lib/okf/pro/writes.rb`

> plans.each { |plan| Scaffold.write_atomically(plan.path, plan.text, false) }
> --- `gems/okf-pro/lib/okf/pro/writes.rb`

> Scaffold.write_atomically(entry_path, journal_entry(day), false) unless exists
>         Scaffold.write_atomically(index_path, after, false) unless indexed
> --- `gems/okf-pro/lib/okf/pro/writes.rb`

#### RT-RTE-registry-manage
Label: Browser and TUI registry management

Human UI action → Hub registry mutation or TUI Workspace registry method → on-disk registry change → reload selected bundles/corpus. This changes subsequent selection, not concept prose. Code decides structural validity; UI caller selects the action. No model oracle or improvement experiment is part of the route. Browser CLI enables writes only for loopback and without read-only; direct Hub construction has its own writable parameter.

- Immediate return: Hub JSON success/error or TUI status-line message with refreshed workspace.
- Later read-back: Registry entries/default/groups affect later discovery and served sets.
- Delegated visibility: uninspected — other clients can observe later registry state, but no worker propagation protocol is shown.
- Selection predicate: Named slug/path/action; browser checks recognized write verb, writable flag, registry existence, host comparison and boot token. TUI requires registry-backed mode.
- Invalidation or expiry: Hub rebuilds apps and clears search corpus/count/health after writes; TUI reload preserves active/scope where still resolvable.
- Activation or effect: Registry configuration changes are wired. Removal explicitly leaves the bundle folder untouched.
- Evidence limits: Browser same_origin? compares parsed host, not full scheme/port origin equality. UI code is not an authorization claim for external deployment; actual UI use unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection/recovery: caller proposes; registry/core constraints and browser request checks can refuse; returned errors prompt retry. No automatic rollback beyond underlying registry behavior is established here. Guidance is fixed symbolic UI routing; registry changes persist, not model parameters. SRC-1, `gems/okf/lib/okf/server/hub.rb`, `gems/okf/lib/okf/cli/server.rb`, `gems/okf-tui/lib/okf/tui/workspace.rb`:

> return deny(403, "That request did not come from this page. Reload and try again.") unless authentic?(request)
> --- `gems/okf/lib/okf/server/hub.rb`

> URI.parse(source).host == request.host
> --- `gems/okf/lib/okf/server/hub.rb`

> !options[:read_only] && loopback?(options[:bind])
> --- `gems/okf/lib/okf/cli/server.rb`

#### RT-RTE-extension-load
Label: Ruby CLI extension admission

Missing CLI verb or help → RubyGems plugin-path discovery → owning-gem-name check → require code → command registration → dispatch. Operator/package installation supplies capability code; code applies naming/registration checks. No content review, semantic oracle or experiment occurs at discovery. General Ruby code runs in-process; registration limits are not a sandbox.

- Immediate return: Newly available command, unknown-command error, or stderr load/refusal notes. Built-in dispatch need not load plugins.
- Later read-back: Installed plugin files are loaded by later CLI processes; registration is process-local and load-latched.
- Delegated visibility: inapplicable — plugin loading is not worker delegation.
- Selection predicate: Discovered okf/plugin.rb paths; installed gem names beginning okf- pass, no-owning-gem load-path entries pass, unknown ownership fails. Duplicate command ids cannot replace prior registrations through register.
- Invalidation or expiry: Process restart reloads installed state; no content hash, signature or exact dependency version pin is imposed here.
- Activation or effect: Ruby require executes accepted code and may register new capabilities; arbitrary side effects are not contained by command registration.
- Evidence limits: Local dependency/load-path trust is external; a malicious accepted plugin could modify Ruby behavior outside the public registration method. No universal non-displacement/security guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission trigger is discovery after operator installation/load-path provision; naming and duplicate-id checks can reject, but a prefix is not substantive approval. LoadError/StandardError failures are collected and reported; require need not undo partial side effects. Recovery is package/environment correction or restart, not transactional plugin rollback. SRC-1, `gems/okf/lib/okf/cli.rb`:

> require path
>             @loaded_plugins << path
> --- `gems/okf/lib/okf/cli.rb`

> return true if name.nil?
>         return false if name.equal?(UNKNOWN_GEM)
>
>         name.start_with?(PLUGIN_GEM_PREFIX)
> --- `gems/okf/lib/okf/cli.rb`

#### RT-RTE-governance-install
Label: Pro scaffold and governance upgrade

Caller invokes setup/upgrade/skill → template-tree enumeration → per-file copy/collision policy → atomic rename → written/staged/kept report. Caller selects installation; Ruby decides files, overwrite and collisions. This admits instruction and production-control changes from packaged templates without model content judgment or a fixed-answer oracle. Installation is operator-requested, not trace-triggered self-modification.

- Immediate return: Counts and paths written/staged/kept, with merge instructions or refusal.
- Later read-back: Copied skill/guides are read by agents; hook wrapper, Git hook and CI workflow are executed by their respective external runtimes. Seeded settings must be merged/configured where needed.
- Delegated visibility: inapplicable — installer does not launch workers.
- Selection predicate: Gem-owned template tree is rewritten on upgrade; seeded tree is completed but existing bundle files are kept, other differing seeded collisions become .okf-pro-new. Skill-only install copies whole skill tree.
- Invalidation or expiry: Upgrade refreshes gem-owned content, not existing seeded settings. Installed versions therefore can differ by ownership class.
- Activation or effect: Files copied and executable modes set; actual host discovery, hook enabling and CI enforcement depend on adopter setup and remain unobserved.
- Evidence limits: Atomic per file, not across tree; no rollback history or package authenticity guarantee. Running installer is not separate human approval of each copied instruction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposed change comes from packaged templates, guided by ownership policy. Code can reject incompatible setup layout; users can decline/merge staged collisions. Recovery is rerunnable setup/upgrade, with no set transaction. SRC-1, `gems/okf-pro/lib/okf/pro/scaffold.rb`:

> report(out, write_tree(GEM_DIR, dest, overwrite: true) + write_tree(SEED_DIR, dest), dest, "upgrade")
> --- `gems/okf-pro/lib/okf/pro/scaffold.rb`

> File.binwrite(tmp, content)
>         File.chmod(executable ? 0o755 : 0o644, tmp)
>         File.rename(tmp, target)
> --- `gems/okf-pro/lib/okf/pro/scaffold.rb`

#### RT-RTE-refine-proposal
Label: Proposed structural and instruction refinement

User request → external agent inventory/measurement → content-sensitive diagnosis under shipped principles → proposal → user approval → requested edits and before/after checks. Refine concerns bundle arrangement, not factual correction; okf-principles separately restructures instruction artifacts by question boundaries and keyed references. These are natural-language workflows, not Ruby CLI verbs that independently perform semantic restructuring. Agent proposes/diagnoses, human can veto refine execution, and tools compute structural evidence. The measurements are not an expected semantic-answer oracle. okf-principles requests a fixed question set for worst-case loading assessment, whereas refine serves an open user request with before/after structural evidence.

- Immediate return: Refine report, declines and ready-to-run execution prompt; instruction restructuring requests inventory/index/rule-key changes and question-set verification.
- Later read-back: Approved structure and authored pointers/keys can shape later retrieval; declines are requested to prevent repeated proposals. Their actual later consumption is unobserved.
- Delegated visibility: uninspected — no isolated worker protocol specified by these playbooks.
- Selection predicate: Agent judges cohesion, hub origin, duplication and churn for refine; instruction splitting uses question families, excludes splitting foreign/generated files, and measures worst-case questions rather than mean bytes.
- Invalidation or expiry: New observed misfit/task request can trigger another pass; source supplies no automatic scheduler or expiry.
- Activation or effect: Approval separation and restructuring behavior are requested; no execution trace establishes application or benefit.
- Evidence limits: Policy depends on agent/user compliance. Fixed question set/provider of expected answers is not concretely supplied; diagnosis quality and task accuracy remain unobserved.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission: refine requires approval before execution; agent chooses changes under retained principles and do-nothing comparison. Users can reject proposals. Recovery requests closeout checks and pointers at moved seams; no executable rollback protocol. The instruction-restructuring skill does not itself impose refine's explicit approval step, so the two are not one approval guarantee. SRC-1, `skills/okf/playbooks/refine.md`, `skills/okf-principles/SKILL.md`:

> 5. **Propose — never auto-apply.** Refine's output is a short report (the
>    evidence, the tiers, the declines) plus a ready-to-run execution prompt the
>    user can hand back later: a scope line, the governing principles above, the
>    explicit prohibitions, the closeout gate as acceptance.
> --- `skills/okf/playbooks/refine.md`

> The frame that governs every move: the directory tree is a **lossy projection
> of the link graph**. A tree gives each concept one parent, so the tree encodes
> only the single dominant decomposition; every genuinely many-to-many
> relationship rides links and tags, never new directories.
> --- `skills/okf/playbooks/refine.md`

> 6. Verify against the anti-goal with a fixed question set, judging the
>    worst question rather than the mean (rule ss-measure-worst-case): one
>    that loads more files or bytes than before names the boundary to
>    merge back.
> --- `skills/okf-principles/SKILL.md`

Theory account: the projection explanation and explicit scope exceptions are localized guidance applied to structural diagnosis, not necessarily themselves revised. The request criticizes bundle arrangement under unchanged principles; this alone does not establish content-directed criticism of those principles. Persisted outputs requested are proposal/declines, changed layout, pointers and before/after evidence, not model weights.

- theory-builder conditions 1–4: assessed separately below, for the shipped structural principles and their proposed use, not the whole external agent.
- Condition 1 conclusion status: wired
  - Whole localized natural-language units exist, including the projection explanation quoted above.
- Condition 2 conclusion status: claimed
  - The playbook explicitly makes the frame govern moves; actual model decisions depending on its content are unobserved.
- Condition 3 conclusion status: uninspected
  - No supplied execution shows criticism naming a challenged principle, blame and resultant revision/reliance. Requested diagnosis of an artifact under a fixed principle is not that evidence.
- Condition 4 conclusion status: uninspected
  - Retaining declines and later reruns is requested, but no demonstrated criticism/result-to-next-round chain for the principles is supplied.
- Addressability: individual named rules and bounded exceptions are inspectable/revisable text; actual revision use is unobserved.
- Persistence: principles ship across sessions; proposals/declines and approved edits can persist in user files, but attained later-use horizon is unobserved.
- learning: no improved future capacity or component attribution is established by these instructions alone.
- Reflection: the instruction-restructuring target can be an agent's instructions, but both causal directions for a bounded self-representation are unestablished in supplied evidence.
- Reflective theory builder: uninspected — no evidenced criticism of method text against records of its own operation.
- Autonomous theory builder: uninspected — host internals and actual role execution are not frozen, and refine explicitly reserves execution approval to a user.
- Self-improvement: no exercised pathway is attributed. Instruction files could affect an agent's later behavior, but a retained, evidence-shaped update entering and causally changing subsequent operation is not shown. Bundle arrangement improvement is not automatically change to OKF's own organization.

### Claims

#### RT-CLM-live-bodies
Label: MCP current-file promise

SRC-1, `gems/okf-mcp/lib/okf/mcp/server.rb` claims live bodies and current results:

> Bodies are read
>         live from disk, so results always reflect the current files.
> --- `gems/okf-mcp/lib/okf/mcp/server.rb`

[RT-RTE-mcp-retrieve](#rt-rte-mcp-retrieve) narrows this to actual live byte reads plus fingerprint-dependent selection state. Equal-size/mtime changes, cached identity maps, and reserved-log fallback prevent a universal result-freshness conclusion. This is not a demonstrated stale execution, only an implementation limit.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Skill guidance to agent decisions

Consumer: external agent. Channel: skill/playbook Markdown, CLI output and optionally MCP prompts/tool descriptions. Force: requested natural-language behavioral guidance, not enforced semantic compliance. Horizon: current task and later sessions that reload installed text. Relevant route: [RT-RTE-skill-work](#rt-rte-skill-work). SRC-1, `skills/okf/SKILL.md`, `gems/okf-mcp/lib/okf/mcp/server.rb`:

> Read the referenced playbook before executing — it *is* the procedure.
> --- `skills/okf/SKILL.md`

#### RT-BAP-hook-protocol
Label: Installed hook machinery to host admission

Consumer: Claude host hook dispatcher, then Git or GitHub Actions at later doors. Channel: installed JSON registrations, executable wrapper and checker outputs, pre-commit script and CI workflow. Force: software rejection/ask requests conditional on configured host protocol and deployment controls; no universal filesystem sandbox. Horizon: installed project operation until files/configuration change. [RT-RTE-pro-gates](#rt-rte-pro-gates) and [RT-RTE-governance-install](#rt-rte-governance-install) distinguish shipping, installation and actual enforcement. SRC-1, `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json`, `gems/okf-pro/lib/okf/pro/template/gem/.claude/hooks/run`:

> cat "$work/out"
> --- `gems/okf-pro/lib/okf/pro/template/gem/.claude/hooks/run`

## Annotations

none
