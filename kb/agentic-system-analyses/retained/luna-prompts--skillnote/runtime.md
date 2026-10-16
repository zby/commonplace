---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SkillNote runtime baseline: skill admission, host delivery, context hooks and feedback at the frozen source revision."
run-id: AAS-2026-10-14-skillnote-0ccfe85cda4a-01
reviewed-boundary: "7ea2fc7a8435af64d1c080d8765c0eabba1121ea"
---

# SkillNote runtime report

## Runtime account

SkillNote moves reusable instruction text between a registry and external agents. It does not own the enclosing task-execution loop. The server executes database, archive and HTTP operations; a host model decides whether and how to apply the delivered prose. The principal distinction is between distributing instructions and enforcing their application. All findings below use SRC-1 at the boundary's frozen commit. They are implementation or doctrine/design findings, not observed runs. No target execution, service contact, supplied transcript or causal experiment supports activation or benefit.

### Ordinary invocation and ownership

An ordinary Claude Code path starts with a user or authoring agent creating a registry skill through POST `/v1/skills`. The backend validates the request, assigns the skill UUID, stores the slug, name, description, Markdown and collections, snapshots a content version, notifies MCP listeners and commits. PATCH edits the current row and snapshots another version. The browser store calls these APIs but also retains local state on failure; browser success is therefore not necessarily registry admission. See [RT-RTE-registry-write](#rt-rte-registry-write).

The user chooses project collections in `.skillnote.json`. The shipped Claude Code hook manifest invokes sync on session startup, resume and compact, and on configuration changes; UserPromptSubmit also invokes an asynchronous auto-sync handler. The inspected sync handler resolves the registry base URL, requests `include=content` with optional collection filtering, reconstructs frontmatter, substitutes API/web URL placeholders and writes `.claude/skills/skillnote-<slug>/SKILL.md`. A manifest tracks managed directories. Missing configuration or an empty collection choice prevents this sync; network failure preserves cached files. On a normal complete response, stale prefixed directories can be deleted. The immediate terminal result is local skill files and a human-facing sync summary, not a completed user task. Host discovery, subsequent model selection and task effects are external contracts. See [RT-RTE-project-sync](#rt-rte-project-sync) and [RT-BAP-host-instructions](#rt-bap-host-instructions).

The host may later invoke a skill. SkillNote's PostToolUse hook produces a JSON `additionalContext` instruction asking for a rating after task completion. The request is not a mandatory postcondition on the task executor. The MCP alternative similarly returns skill prose plus an optional `complete_skill` hint, and its completion tool saves a caller-supplied rating after range and skill checks. See [RT-RTE-feedback-report](#rt-rte-feedback-report). Neither route checks the task's expected answer.

### Material alternate routes

- **MCP:** the provider fetches current skill rows for list/get requests, maps descriptions to tool metadata, and returns a title and body when called. The provider's inspected filter parser reads an environment variable; its URL-filter docstring does not itself implement connection-specific selection. The source does not justify treating a query-string collection label as an authorization boundary. See [RT-RTE-mcp-delivery](#rt-rte-mcp-delivery).
- **CLI archives:** `add` selects an active published bundle or, only if there are no published versions, a generated current-content bundle. It checks a supplied checksum, validates archive entries through the system `unzip` interface, copies files through agent adapters and records an installation manifest. A published ZIP is a distinct product from the current Markdown row: publishing records archive metadata but does not copy its body into the existing row. See [RT-RTE-bundle-install](#rt-rte-bundle-install).
- **Codex:** the corresponding sync implementation writes host skill files, but has a project-scoped single-writer lock and stale-lock reap. Its hook mode deliberately avoids stdout context injection. These controls are specific to that handler, not implied for the Claude Code handler. See [RT-RTE-project-sync](#rt-rte-project-sync).
- **OpenClaw:** the shipped prompt instructs description-first selection, at most three ordinary matches, a maximum of five full skill loads, and user resolution of conflicting advice. Sync populates user-level `sn-*` files and a sidecar. A one-time user-confirmed include connects that sidecar to the host's AGENTS file. The sync script also has a daily version-mismatch update path, distinct from ordinary instruction sync. See [RT-RTE-openclaw-use](#rt-rte-openclaw-use) and [RT-RTE-adapter-update](#rt-rte-adapter-update).
- **Browser connector:** a paired extension consumes queued operations, uses the browser's claude.ai session to upload/update/delete skills or replace collection plugin groups, reports completion, and can discover and import previously unknown remote skills. It is an asynchronous delivery/admission path, not a direct model call. See [RT-RTE-browser-sync](#rt-rte-browser-sync).
- **Git import:** selected inspected skills can be inserted, renamed, skipped or replaced. A same-source non-forked conflict takes a special branch that can update metadata without replacing the body. Refresh preview computes a diff, but the refresh apply endpoint returns zero rather than applying it. See [RT-RTE-source-import](#rt-rte-source-import).

### Guarantees and forcing cases

1. **Author approval is a prompt policy, not an API invariant.** Owner: the authoring agent and user. Enforcement point: `skill-push`'s confirmation and final-review instructions. Guarantee strength: policy. Covered path: an agent following that prompt. Alternate paths: direct POST/PATCH, browser editing, import, ZIP publish and connector reverse import. Required external contract: host instruction following and a real user approval exchange. Implementation conclusion status: wired (the prompt and API endpoints are shipped). Operation conclusion status: uninspected. A direct API caller is the forcing case: `create_skill` and `update_skill` accept payload plus database dependency, without a per-content approval artifact. Accordingly, universal human approval is not established. Evidence: [RT-RTE-registry-write](#rt-rte-registry-write), [RT-RTE-source-import](#rt-rte-source-import), [RT-RTE-bundle-install](#rt-rte-bundle-install).
2. **Withdrawal covers download routes, not all delivery.** Owner: backend download handlers and CLI selector. Enforcement point: disabled-version rejection; current-download rejects a published skill with no active version. Guarantee strength: invariant, restricted to those handler branches. Covered paths: versioned/current archive downloads and CLI add's selection. Alternate paths: REST list with content, project/OpenClaw sync, MCP current-row delivery and already cached files. Required external contract: consumers use the controlled endpoint and stop using earlier copies. Implementation conclusion status: wired. Operation conclusion status: uninspected. Comparing download checks with the current-row MCP query defeats a system-wide revocation inference. Even the generated-current check is stricter than its error wording: it tests lack of active versions, not that every version literally has status `disabled`. See [RT-RTE-bundle-install](#rt-rte-bundle-install) and [RT-RTE-mcp-delivery](#rt-rte-mcp-delivery).
3. **Offline continuity trades away prompt revocation.** Owner: each sync handler. Enforcement point: fetch failure, empty/bodyless response guards and manifest deletion. Guarantee strength: best effort. Covered paths: inspected handler branches. Required external contract: existing files remain readable and hosts continue discovering them. Implementation conclusion status: wired. Operation conclusion status: uninspected. A filtered empty response with cached Claude Code skills deliberately keeps them, so absence on the server need not remove local instructions. Codex/OpenClaw implement their own related guards; no uniform freshness deadline follows. See [RT-RTE-project-sync](#rt-rte-project-sync).
4. **Synchronization is not uniformly atomic or complete.** Owner: backend and connector workers. Enforcement points: database transactions, adapter locks, operation acknowledgments. Guarantee strength: best effort across network/filesystem boundaries. Required external contracts: working Postgres notifications, filesystem operations, browser permissions and remote API compatibility. Implementation conclusion status: wired. Operation conclusion status: uninspected. Forcing cases are refresh `apply` returning zero, browser group retirement errors being logged without necessarily failing the operation, and browser-local save surviving an API error. These prevent interpreting UI success, an operation acknowledgment or a drift preview as proof of all consumers sharing current content. See [RT-RTE-source-import](#rt-rte-source-import), [RT-RTE-browser-sync](#rt-rte-browser-sync) and [RT-RTE-registry-write](#rt-rte-registry-write).

### Authority, context and model boundary

Capability surfaces include arbitrary retained instruction bodies, archive files delivered to host skill directories, shell-based sync, the browser's authenticated remote operations and an OpenClaw adapter updater. Current grants depend on local registry address, selected collections, adapter destinations, integration pairing and browser session. No deployed grant set or isolation envelope is supplied. These mechanisms must not be treated as a sandbox for the task-performing agent. Backend CORS and conditional production HTTPS checks constrain some HTTP access; they do not implement per-content approval or constrain actions an external host takes after reading a skill. The connector bearer guard is real but narrower than the UI/control plane: its own source says the pairing/settings side remains auth-less. SRC-1, `backend/app/main.py`, `backend/app/api/claude_ai.py`.

> The frontend's pairing
>     and settings endpoints DON'T use this — they are user-session based
>     (currently auth-less, see CLAUDE.md, until ACL lands).
> --- `backend/app/api/claude_ai.py`

Working-context controls are delivery and selection controls, not SkillNote-owned window compaction. Collection filters exclude skills before host discovery. OpenClaw's prose asks a foreground agent to inspect descriptions before loading selected bodies; the hard cap is requested, not mechanically enforced. The OpenClaw context-bundle endpoint contains deterministic candidate truncation and usage/rating ordering but does not itself execute semantic ranking. Its docstring describes a resolver subagent; the inspected shipped OpenClaw prompt instead describes foreground v1 picking and a future resolver. Resolver execution and any isolated-frame return are therefore not established by this evidence.

Claude Code's SubagentStart handler supplies the collection name and command pointers, not full instruction bodies. PostCompact fetches slugs and emits a reminder, not a retained summary of task reasoning. It treats empty and wildcard selections alike when fetching, unlike normal sync's empty-selection no-op. Moreover, PostCompact prints plain text while the inspected PostToolUse handler explicitly uses JSON for model-visible context; actual PostCompact reinjection is not established. SkillNote does not implement the host's compaction decision, what tail survives or the subagent's isolation. These mechanisms are recorded in [RT-RTE-context-hooks](#rt-rte-context-hooks).

The external host model is the distributed-parametric decision maker [RT-CMP-host-model](#rt-cmp-host-model). Inspected routes do not expose its weights, exact version or update policy. Model choice, provider-native tools, shell grants and actual model compliance belong to the external hosts. This is not an inference that those capabilities are absent. SkillNote's task-selection prose and rating requests are natural-language policies; its filters, status checks and transactions are symbolic code rules. No source-supported claim of weight learning, task benefit or reliable autonomous improvement is made here.

### Inspection extent

In addition to the boundary's initial coverage, this report inspected SRC-1 implementation in `backend/app/api/downloads.py`, relevant portions of `backend/app/api/skills.py`, `backend/app/api/imports.py`, `backend/app/api/openclaw.py`, `backend/app/api/claude_ai.py`, `backend/app/main.py`, `backend/mcp_server.py`, `backend/app/services/imports/importer.py`, `cli/src/commands/add.ts`, `cli/src/util/zip.ts`, `src/lib/skills-store.ts`, the context hooks, Codex locking code and the browser connector's operation switch. Shipped prompt sections in `plugin/skills/skill-push/SKILL.md` and `plugin-openclaw/skillnote/SKILL.md` supply doctrine/design evidence. This is selective control-path tracing, not an exhaustive security audit. Connector server conflict-resolution internals, watcher parsing, CLI update/remove internals, import inspection/token expiry and release machinery were not fully traced; their end-to-end reliability remains uninspected. These are available-code coverage limits, not source access gaps. Memory/version semantics beyond the runtime distinctions above belong to the memory analyst.

## Shared records

### Components

#### RT-CMP-host-model
Label: External host model

The model interpreting skill descriptions, bodies and completion instructions lives in Claude Code, Codex, OpenClaw or claude.ai, outside the frozen implementation. Representational form: distributed-parametric. Storage substrate: external host/provider weights, uninspected. Parameter changes during operation: uninspected. Exact version pinned: not established by these prompts/adapters. Mutable endpoint substitution: uninspected; SkillNote does not establish the host's model resolution contract. SRC-1, `plugin-openclaw/skillnote/SKILL.md`, asks the host to select and apply skills, rather than implementing a local model call.

> 2. **Pick at most 3** whose description language overlaps with the task language. Be conservative: 0 is a valid answer.
> 3. **Read the full `SKILL.md`** of those 1-3 selected skills.
> 4. **Apply their guidance** to the task.
> --- `plugin-openclaw/skillnote/SKILL.md`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-registry-write
Label: Registry authoring and direct write

User/editor or host agent → POST/PATCH → current skill row and content-version snapshot. The agent-prompt path proposes repeated persistent conventions, shows a draft, asks for a collection and requests final approval; the user can reject. The API path accepts caller content subject to structural checks, not a semantic oracle or approval receipt. Open-request authoring mode; triggers are explicit requests, repeated instructions or retrospective review. Description trigger quality and short actionable content guide the proposal. Rollback is partly afforded by content-version restore/set-latest; inspected restore copies title/description/body/collections and makes a new snapshot, whereas set-latest reselects an existing one. This is not proof that every field or alternate write path shares the same history semantics. Browser localStorage is a separate failure-surviving state, not registry acceptance. SRC-1, `backend/app/api/skills.py`, `src/lib/skills-store.ts`, `plugin/skills/skill-push/SKILL.md`.

- Immediate return: API skill detail/version on commit; browser can instead return a locally added or locally edited skill after API failure.
- Later read-back: committed registry current content reaches list/detail, sync and MCP; local browser content reaches later browser reads, not necessarily other clients.
- Delegated visibility: authors can distribute through selected host integrations; user approval behavior is only prescribed to the authoring agent.
- Selection predicate: slug for edit; payload fields and collections for new admission; browser chooses the skill under edit.
- Invalidation or expiry: PATCH changes current content; explicit version selection/restore and delete can change future reads; browser failures can leave divergence.
- Activation or effect: database and browser state changes are wired; later model adherence and task changes are unobserved.
- Evidence limits: no observed approval exchange or successful save; local fallback is not a cross-client sync guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Show complete skill preview. Emphasize: "Does the description have good trigger keywords?" Wait for approval.
> --- `plugin/skills/skill-push/SKILL.md`

>     # Auto-create a new content version on every save
>     _create_content_version(db, skill_row)
> --- `backend/app/api/skills.py`

>     (updated as Skill & { _savedLocally?: boolean })._savedLocally = true
> --- `src/lib/skills-store.ts`

#### RT-RTE-project-sync
Label: Project skill synchronization

Claude Code host hook → collection-filtered REST list → project skill files/manifest → external host discovery. Codex has a parallel handler with project locking and different stdout behavior. Code owns fetching, frontmatter reconstruction, placeholder replacement, comparison and stale-file removal; host/user owns configuration and later invocation. The installer admits newer instruction bytes without a per-update content approval gate. The operator can change collections or stop sync; offline cached content is the recovery mechanism. SRC-1, `plugin/hooks/hooks.json`, `plugin/hooks-handlers/sync.sh`, `plugin-codex/hooks/handlers/sync.sh`.

- Immediate return: files and manifest plus a Claude Code sync summary; Codex hook mode suppresses stdout.
- Later read-back: a later host invocation can read the installed SKILL.md files, including older cached versions after fetch failure.
- Delegated visibility: project host skill discovery; no claim that child agents inherit complete skill bodies.
- Selection predicate: configured collections or wildcard; special plugin-provided commands are skipped in the Claude Code handler; empty bodies are protected rather than written.
- Invalidation or expiry: normal successful response deletes stale managed/prefixed directories; filtered empty or degraded bodyless responses retain caches; no universal expiry.
- Activation or effect: file replacement and deletion are implemented; discovery and semantic application depend on hosts.
- Evidence limits: no live hook trace; filesystem operations are not an end-to-end atomic deployment; Codex lock coverage does not cover Claude Code.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>     echo "SkillNote: offline (using cached skills)"
> --- `plugin/hooks-handlers/sync.sh`

> if not skills and has_filter and old_managed:
>     print('SkillNote: collection not found on server (keeping cached skills)')
>     sys.exit(0)
> --- `plugin/hooks-handlers/sync.sh`

> LOCK="${MANIFEST_DIR}/.skillnote-sync.lock"
> --- `plugin-codex/hooks/handlers/sync.sh`

#### RT-RTE-mcp-delivery
Label: MCP skill delivery

MCP client list/get/call → provider's current-row query → named tool description and instruction result. Code builds tools and performs query/placeholder substitution; client/model chooses a tool. It does not execute the skill's task. SRC-1, `backend/mcp_server.py`.

- Immediate return: tool metadata or title/body plus optional completion hint.
- Later read-back: later list/get requests query current registry content rather than a fixed published archive.
- Delegated visibility: uninspected — enclosing MCP client decides where tool results travel.
- Selection predicate: requested slug and optional environment collection overlap; special authoring/completion tools respect settings; URL-specific filtering is not established by the inspected parser.
- Invalidation or expiry: future provider reads reflect current rows; already delivered results remain under external client control.
- Activation or effect: returned prose can guide an external agent; actual behavior change is unobserved.
- Evidence limits: tool delivery is not task execution, per-content approval or published-version withdrawal enforcement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         filter_collections = os.environ.get("SKILLNOTE_MCP_FILTER_COLLECTIONS", "")
> --- `backend/mcp_server.py`

>             f"SELECT slug, name, description, content_md, collections, extra_frontmatter "
>             f"FROM skills {where} ORDER BY name"
> --- `backend/mcp_server.py`

>         content = f"# {self.skill_name}\n\n{self.content_md}"
> --- `backend/mcp_server.py`

#### RT-RTE-bundle-install
Label: Publish and install archives

Caller ZIP/version → `/v1/publish` → bundle file and SkillVersion row; CLI `add` → version/current download → archive validation → adapter destinations and installation manifest. The caller proposes bytes and release status. Server metadata/archive/size/version checks can reject; no task-answer oracle or semantic quality gate is shown. Open-request release/install mode. Admission is code validation and caller selection, not required human review. Database failure after file creation removes the published archive; installation errors return failure, but no transactional rollback across all adapter destinations is established. SRC-1, `backend/app/api/publish.py`, `backend/app/api/downloads.py`, `cli/src/commands/add.ts`, `cli/src/util/zip.ts`.

- Immediate return: publish metadata/checksum, or CLI installation success/failure and manifest.
- Later read-back: installed archive content can be consumed in later host sessions; future downloads use stored published bytes or generated current content.
- Delegated visibility: adapter destinations determine project/user scope; fallback universal adapter writes `.agents/skills/`.
- Selection predicate: requested slug or all skills, detected/explicit agents, first active returned published version; current fallback only for no published versions.
- Invalidation or expiry: disabled versions block versioned download; no active published version blocks current download; cached installations are not revoked by these checks.
- Activation or effect: local file copies and manifest are wired; host execution and archive semantic safety are not demonstrated.
- Evidence limits: checksum agreement is not trusted authorship or correctness; archive-entry validation is narrower than general execution isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>   if (!latest && versions.length > 0) {
>     spin.stop()
>     ui.fail(`${slug}: no active version (all published versions are disabled)`)
>     return false
>   }
> --- `cli/src/commands/add.ts`

>     if version_row.status == "disabled":
>         raise api_error(403, "VERSION_DISABLED", "Version is disabled")
> --- `backend/app/api/downloads.py`

>         if not has_active:
>             raise api_error(
>                 403,
>                 "SKILL_WITHDRAWN",
>                 "Every published version of this skill is disabled",
>             )
> --- `backend/app/api/downloads.py`

#### RT-RTE-source-import
Label: Import and refresh

Inspected source result and caller selection → import applier → skill/source/collection rows. Caller chooses conflict policy; code validates names/paths and decides branch outcomes. Proposed knowledge/instruction changes come from repository content, not a task oracle. Open-request import mode. `skip` rejects conflicting candidates; `rename` preserves another slug; `replace` overwrites and repoints origin. Same-source non-forked records take a different branch: changed hashes update description/hash/SHA but not body here. Therefore re-import is not uniformly body refresh. Refresh preview probes and computes drift; apply is a stub. Recovery beyond explicit conflict policy and subsequent registry operations is not fully traced. SRC-1, `backend/app/services/imports/importer.py`, `backend/app/api/imports.py`.

- Immediate return: imported/skipped summaries or preview diff; refresh apply returns zero.
- Later read-back: imported rows reach current-content consumers; imported source/hash metadata persists for subsequent source handling.
- Delegated visibility: collection membership exposes imported instructions to downstream integrations.
- Selection predicate: selected skill names, target collection and conflict policy; validation can skip individual candidates or reject an all-invalid result.
- Invalidation or expiry: replacement changes current row; fork flag and source identity alter conflict handling; preview does not invalidate installed content.
- Activation or effect: database admissions are wired; automatic successful refresh of instruction bodies is not established by the apply endpoint.
- Evidence limits: source inspectors and refresh diff internals not fully traced here; remote repository contents are outside the frozen corpus.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>             if existing.import_source_id == src.id and not existing.forked_from_source:
>                 if existing.source_content_hash != skill_meta.get("content_hash"):
>                     existing.description = skill_meta.get("description", existing.description)
>                     existing.source_content_hash = skill_meta.get("content_hash")
>                     existing.source_sha = inspect_result.resolved_sha
> --- `backend/app/services/imports/importer.py`

>         # "apply" — Literal validation guarantees mode is preview or apply.
>         # v1 stub — full diff-apply arrives in v1.1.
> --- `backend/app/api/imports.py`

>         return {"applied": 0}
> --- `backend/app/api/imports.py`

#### RT-RTE-openclaw-use
Label: OpenClaw instruction selection

Sync script → local `sn-*` skills/sidecar → external foreground agent → selected instruction reads and task. Setup prompt requires user consent for the AGENTS include, with a `grafted: false` opt-out. Thereafter selection and loading caps are prompt policies. The script also emits a usage/rating protocol in the sidecar. The context-bundle endpoint supplies an alternative candidate catalog: optional collection filter, alphabetic prelimit at four times requested size, usage/rating sorting, requested-size truncation and body/comment/staleness fields. This is implemented preprocessing, not observed resolver selection. SRC-1, `plugin-openclaw/skillnote/SKILL.md`, `plugin-openclaw/skillnote/sync.sh`, `backend/app/api/openclaw.py`.

- Immediate return: local files and sidecar; context-bundle requests return candidate metadata and content.
- Later read-back: later host tasks may read synced descriptions, selected bodies and usage/rating-informed candidates.
- Delegated visibility: uninspected — a resolver is described in the endpoint docstring but the inspected shipped prompt specifies foreground v1 selection, not an executed subagent route.
- Selection predicate: task-language overlap, conservative ordinary maximum three, requested maximum five bodies; endpoint selection first truncates alphabetically then sorts usage/rating.
- Invalidation or expiry: sync replaces/removes managed skills on accepted responses; cache-preserving guards can delay removal; sidecar inclusion is separately user-controlled.
- Activation or effect: distribution and ranking preprocessing are wired; host selection/application is requested and unobserved.
- Evidence limits: no host transcript, frame-isolation evidence or benefit measurement; endpoint candidate ranking is not semantic task matching.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 5. **Hard cap: never load more than 5 sn-* SKILL.md files into context for a single task.** If 5+ seem relevant, you've over-matched — re-read the task and tighten.
> --- `plugin-openclaw/skillnote/SKILL.md`

>     stmt = stmt.order_by(Skill.name).limit(req.max_skills * 4)
> --- `backend/app/api/openclaw.py`

#### RT-RTE-adapter-update
Label: OpenClaw adapter self-update

An OpenClaw sync invocation checks the daily timer, fetches `/v1/openclaw-skill`, and compares remote/local version strings. Any nonempty mismatch, not demonstrated semantic version advancement, triggers installation. If `clawhub` is available the script invokes installation with `--yes`; otherwise the actual fallback writes the returned skill body and VERSION file. Its comment mentions sync.sh replacement, but that fallback body does not perform it. Proposed change: adapter skill/package. Admission: code version comparison and installer success/body presence; server/package author supplies bytes, not a per-update human veto. User can stop/configure the integration; local rollback is not shown in this branch. No independent answer oracle or performance objective gates admission. Routine package-update mode, not an improvement experiment. SRC-1, `plugin-openclaw/skillnote/sync.sh`.

- Immediate return: update message and local package/instruction changes if branch succeeds.
- Later read-back: subsequent host sessions can consume the changed adapter instructions; package manager path may also replace machinery outside inspected fallback bytes.
- Delegated visibility: external package manager and OpenClaw host receive the installed product.
- Selection predicate: configured host, elapsed daily interval and unequal nonempty version strings.
- Invalidation or expiry: VERSION and check timestamp suppress repeated checks; no content-specific rollback is shown.
- Activation or effect: update invocation/file overwrite is wired; successful deployment and later behavior change are unobserved.
- Evidence limits: remote server response and clawhub package bytes are not frozen; no authenticity or compatibility conclusion from the version comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         if [ -n "$REMOTE_VER" ] && [ "$REMOTE_VER" != "$LOCAL_VER" ]; then
> --- `plugin-openclaw/skillnote/sync.sh`

>                 clawhub install "skillnote@$REMOTE_VER" --yes >/dev/null 2>&1 && \
>                     echo "SkillNote updated to v$REMOTE_VER — restart your session to apply."
> --- `plugin-openclaw/skillnote/sync.sh`

#### RT-RTE-browser-sync
Label: Browser connector queue execution

Backend queue → paired browser extension → remote claude.ai operations → completion acknowledgment. For upload/update the worker fetches a versioned bundle; publish_group fetches desired groups and replaces each whole bundle, re-enables uploaded plugins, then attempts to disable undesired groups. Reverse `list` imports previously unknown remote IDs. Code and selected integration state admit distribution changes; remote skills propose inbound content. The extension route has bearer identity checks; remote mutation additionally uses the browser's logged-in org/session. No per-skill human approval or answer oracle appears in the inspected worker switch. Operating mode: asynchronous synchronization. Rejection/recovery includes per-operation failure, auth-expired/permanent flags and later retry; complete server-side inbound collision admission remains outside this report's inspected details. SRC-1, `extensions/claude-ai/src/background.ts`, `backend/app/api/claude_ai.py`.

- Immediate return: per-operation completion/failure plus local activity entries, not a synchronous completed user task.
- Later read-back: uploaded remote skills/groups can reach later host use; imported registry rows can reach other clients, subject to server-side admission not fully traced here.
- Delegated visibility: browser worker receives bundles; claude.ai org receives uploaded skills/plugins; server receives import and acknowledgment data.
- Selection predicate: queued operation kind, desired groups, supplied skill/version IDs and unknown remote IDs.
- Invalidation or expiry: delete and group retirement attempt removal/disable; retirement errors are best effort; bearer revocation prevents subsequent guarded calls, not already delivered content.
- Activation or effect: remote mutation requests are wired; actual remote acceptance, discovery and model use are unobserved.
- Evidence limits: remote API implementation/session semantics and complete conflict handling are uninspected; successful group acknowledgment can coexist with retirement errors.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>           console.warn("publish_group: uninstall-removed pass failed", e);
> --- `extensions/claude-ai/src/background.ts`

>             await client.importSkill({
>               claude_ai_skill_id: skill.id,
>               claude_ai_version: skill.version,
>               name: skill.name,
>               description: skill.description ?? "",
>               bundle,
>             });
> --- `extensions/claude-ai/src/background.ts`

#### RT-RTE-feedback-report
Label: Skill completion feedback

Host tool-use event → rating instruction in context; MCP caller completion → rating validation/current-version lookup → database rating. The host/model supplies the score and outcome; code validates score range and resolves identifiers. This is open task feedback, not an expected-answer oracle, and not a skill-content revision mechanism by itself. SRC-1, `plugin/hooks-handlers/skill-used-context.sh`, `backend/mcp_server.py`.

- Immediate return: additionalContext rating request or completion success/error text.
- Later read-back: stored feedback is available to later reporting consumers; OpenClaw's separate comment/usage aggregates can influence its candidate bundle, but this does not establish that MCP ratings and comment averages are the same data path.
- Delegated visibility: external host receives the requested curl/completion action; database receives caller-provided outcome and session attribution.
- Selection predicate: invoked skill name normalized from prefix, or explicit completion slug; score must be integer 1–5 in the inspected MCP implementation.
- Invalidation or expiry: inapplicable — this route reports feedback rather than replacing instructions; broader feedback-retention policy is uninspected.
- Activation or effect: rating insertion/request is implemented; actual host rating behavior, correctness and causal improvement are unobserved.
- Evidence limits: task execution is not verified before accepting a rating; self-report is not measured skill benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         if not isinstance(rating, int) or rating < 1 or rating > 5:
>             return ToolResult(content="Error: rating must be an integer between 1 and 5.")
> --- `backend/mcp_server.py`

#### RT-RTE-context-hooks
Label: Context reminders across host events

Claude Code SubagentStart and PostCompact events → handler output. The subagent handler constructs JSON with collection name and command pointers; PostCompact fetches selected slugs and prints a reminder. Host owns the fork/compaction decision, actual window contents and delivery interpretation. SkillNote does not return a subtask answer or restore task reasoning. SRC-1, `plugin/hooks/hooks.json`, `plugin/hooks-handlers/subagent-context.sh`, `plugin/hooks-handlers/compact-context.sh`, `plugin/hooks-handlers/skill-used-context.sh`.

- Immediate return: collection/command JSON for child context, or plain-text compact reminder.
- Later read-back: inapplicable — event output is current invocation context, not accumulated material written through this route; the handlers reload separately retained configuration/catalog state.
- Delegated visibility: collection label and available command names, not full skill contents, are sent toward the child host context.
- Selection predicate: project configuration; compact handler fetches all slugs on empty/wildcard selection, unlike the sync no-op for empty choice.
- Invalidation or expiry: current context lifetime is controlled by the host; remote-fetch failure produces no reminder.
- Activation or effect: output production is wired; PostCompact model visibility is unresolved because it prints plain text rather than the explicit JSON channel used elsewhere.
- Evidence limits: no host hook trace or compaction survivor evidence; no established isolated-frame return or semantic recovery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> ctx = 'SkillNote: this project uses the ${COLLECTIONS} skill collection. Available commands: /skillnote:collection (change), /skillnote:skill-push (create).'
> --- `plugin/hooks-handlers/subagent-context.sh`

> # Plain text stdout is shown to user only, NOT injected into Claude's context.
> --- `plugin/hooks-handlers/skill-used-context.sh`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-instructions
Label: Delivered skill prose to external agents

Consumer: external task-performing host model. Channel: installed SKILL.md body or MCP tool result; description metadata first influences selection. Force: natural-language instruction interpreted under the external host's instruction hierarchy, not a SkillNote enforcement invariant. Horizon: later tasks/sessions while installed or served, with already delivered copies remaining outside registry control. SRC-1, `plugin/hooks-handlers/sync.sh`, `backend/mcp_server.py`, `plugin-openclaw/skillnote/SKILL.md`; the quoted selection and delivery passages in [RT-CMP-host-model](#rt-cmp-host-model) and [RT-RTE-mcp-delivery](#rt-rte-mcp-delivery) establish the requested channel. They do not establish actual compliance. The updater in [RT-RTE-adapter-update](#rt-rte-adapter-update) can change the shipped adapter instructions along this path, but exercised self-improvement is not inferred from update/install wiring.

## Annotations

none
