---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SkillNote memory: instruction rows, independent archives, local copies, inbound staging and feedback-conditioned candidate delivery."
run-id: AAS-2026-10-14-skillnote-0ccfe85cda4a-01
source-identity: "https://github.com/luna-prompts/SkillNote"
reviewed-boundary: "7ea2fc7a8435af64d1c080d8765c0eabba1121ea"
---

# SkillNote memory report

## Boundary and evidence

This report covers reusable skill instructions, their content history and published archives, installed copies, browser-local fallback, connector staging and feedback consumed by later selection. It inherits the whole-system boundary and SRC-1 from [boundary](boundary.md#source-register), at commit `7ea2fc7a8435af64d1c080d8765c0eabba1121ea`. External host weights, context windows, user corpora and remote-origin bytes remain outside the available evidence. No run or experiment establishes successful use or benefit.

The supplied runtime is a provisional source-grounded baseline, not evidence of execution. Direct reads below add implementation evidence from SRC-1, with prompt contracts supplied by the runtime providing doctrine/design evidence. Paths in the table are commit-relative. Remaining available-but-uninspected code is not an access gap.

| Entry point / operation | Source path | Coverage and limit |
| --- | --- | --- |
| POST/PATCH, history, set-latest, restore | `backend/app/api/skills.py`; `backend/app/db/models/skill.py`, `skill_content_version.py` | Direct history/schema reads; [MEM-OBJ-skill](#mem-obj-skill), [MEM-OBJ-content-version](#mem-obj-content-version); supplied [RT-RTE-registry-write](runtime.md#rt-rte-registry-write) for ordinary authoring |
| UI authoring and failure fallback | `src/lib/skills-store.ts`; `plugin/skills/skill-push/SKILL.md` | Supplied [RT-RTE-registry-write](runtime.md#rt-rte-registry-write); browser persistence annotated below; actual approval and cross-client admission unobserved |
| Git admission and refresh | `backend/app/services/imports/importer.py`; `backend/app/api/imports.py` | Supplied [RT-RTE-source-import](runtime.md#rt-rte-source-import); inspector provenance, expiry and all fork behaviors not directly re-audited; prevents universal provenance/history guarantee |
| ZIP publish/download, CLI add | `backend/app/api/publish.py`, `downloads.py`; `cli/src/commands/add.ts` | Supplied [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install); direct release schema [MEM-OBJ-skill-version](#mem-obj-skill-version) |
| CLI dispatch/update/remove | `cli/src/index.ts`; `cli/src/commands/update.ts`, `remove.ts` | Direct dispatch search and maintenance-body reads; [MEM-RTE-install-maintenance](#mem-rte-install-maintenance); shared-install registry internals not fully inspected |
| Claude Code and Codex sync, context hooks | `plugin/hooks/hooks.json`; `plugin/hooks-handlers/sync.sh`, `compact-context.sh`, `subagent-context.sh`; `plugin-codex/hooks/handlers/sync.sh` | Supplied [RT-RTE-project-sync](runtime.md#rt-rte-project-sync), [RT-RTE-context-hooks](runtime.md#rt-rte-context-hooks); no host reinjection or compaction-survivor evidence |
| MCP list/get/call/completion | `backend/mcp_server.py` | Supplied [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery), [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report); current-row route, not release-status revocation |
| OpenClaw prompt/sync/updater | `plugin-openclaw/skillnote/SKILL.md`, `sync.sh` | Supplied [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use), [RT-RTE-adapter-update](runtime.md#rt-rte-adapter-update); selection caps are requested, not enforced by host code here |
| Context bundle, usage admission, comments | `backend/app/api/openclaw.py`, `comments.py`; `backend/app/db/models/comment.py`, `skill_usage_event.py` | Direct reads; [MEM-RTE-feedback-catalog](#mem-rte-feedback-catalog), [MEM-OBJ-comment](#mem-obj-comment), [MEM-OBJ-usage-event](#mem-obj-usage-event) |
| Watcher and hook trace admission | `plugin-openclaw/skillnote/log-watcher.py`; `backend/app/api/hooks.py` | Direct reads; [MEM-RTE-trace-reporting](#mem-rte-trace-reporting); read detection is not application evidence |
| Browser upload/group retirement | `extensions/claude-ai/src/background.ts`; `backend/app/api/claude_ai.py` | Supplied [RT-RTE-browser-sync](runtime.md#rt-rte-browser-sync); remote acceptance not observed |
| Browser reverse import/conflict resolution | `backend/app/api/claude_ai.py` | Direct inbound and resolution branches; [MEM-RTE-inbound-resolution](#mem-rte-inbound-resolution); divergence detector and all ZIP parsing guards not fully re-audited |
| Evaluation, analytics and cleanup | `backend/app/api/hooks.py`, `comments.py`, `openclaw.py`; CLI removal above | Direct evaluation storage and comment deletion; analytics UI/query internals beyond supplied feedback findings remain uninspected; prevents complete retention-policy and evaluation-effect conclusions |

## Core ideas

SkillNote retains procedures rather than owning the task-solving agent. A description helps an external model select a skill; the body supplies natural-language guidance. Collections, hashes, pointers and release statuses have symbolic consumers. Their control differs from the authority of the prose itself. See [MEM-OBJ-skill](#mem-obj-skill) and [RT-BAP-host-instructions](runtime.md#rt-bap-host-instructions).

There is no single canonical version for all consumers. Current rows, historical content snapshots, published ZIPs, local installed copies and staged remote versions have distinct admission and withdrawal semantics. A content snapshot does not prove an identical published archive. A rejected staged body can be physically deleted while its rejection remains in an audit record. See [MEM-OBJ-content-version](#mem-obj-content-version), [MEM-OBJ-skill-version](#mem-obj-skill-version), [MEM-RTE-inbound-resolution](#mem-rte-inbound-resolution).

Feedback can change a later candidate payload without revising any skill text. OpenClaw usage counts, comment ratings and deprecation comments influence candidate order and staleness metadata. The server delivers only the first 200 characters of the latest comment, not a synthesized explanation or a complete criticism history. This supports feedback-conditioned delivery capacity, not demonstrated improvement. See [MEM-RTE-feedback-catalog](#mem-rte-feedback-catalog).

Context budgeting is mostly host-side policy: description-first selection and limits on loaded bodies. The bundle's deterministic prelimit is a server control, but not a token budget or semantic ranker. Host compaction and subagent isolation are opaque external responsibilities; reminder hooks do not retain a task-reasoning checkpoint. See [RT-RTE-context-hooks](runtime.md#rt-rte-context-hooks) and [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-skill
Label: Skill instruction and access fields

SRC-1, `backend/app/db/models/skill.py`: the `skills` table holds `description` and `content_md`, natural-language material interpreted by authors and later external agents. SQL text is the substrate, not the representational form. Separately, UUID, slug, collections, current-version counter, source SHA/hash/path, fork flag and connector opt-in are symbolic access, lineage and selection state. `extra_frontmatter` is retained text whose downstream interpretation depends on the adapter/host; arbitrary keys cannot be classified uniformly from its storage column. Initial body authorship is caller-supplied and can be human, agent or imported; caller identity does not establish human approval.

Closest supplied records are [RT-RTE-registry-write](runtime.md#rt-rte-registry-write), [RT-RTE-source-import](runtime.md#rt-rte-source-import) and [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery): this declares their shared retained object, not a duplicate route. Later list/detail, sync and MCP read current content; collections constrain discovery, while prose has policy authority only at the external interpreting agent.

>     description: Mapped[str] = mapped_column(Text, nullable=False)
>     content_md: Mapped[str] = mapped_column(Text, nullable=True, default="")
> --- `backend/app/db/models/skill.py`

#### MEM-OBJ-content-version
Label: SkillContentVersion history and staged bodies

SRC-1, `backend/app/db/models/skill_content_version.py`, `backend/app/api/skills.py`, `backend/app/api/claude_ai.py`: Postgres `skill_content_versions` retains natural-language title/description/body plus symbolic version, collections and `is_latest`. Ordinary save derives a snapshot from the current row. History endpoints, restore/set-latest and connector delivery consume these snapshots. The schema does not snapshot `extra_frontmatter` or source lineage fields; restoration cannot be inferred to rewind those fields. Reasons for an edit are not required snapshot fields. An arbitrary body could retain reasons, but their presence and later consumption are corpus-dependent.

Closest supplied record: [RT-RTE-registry-write](runtime.md#rt-rte-registry-write); distinct operative object rather than duplicated authoring. Staged inbound snapshots share this table but have different admission and cleanup in [MEM-RTE-inbound-resolution](#mem-rte-inbound-resolution). A version number is not always the active-content pointer: staging advances the counter without replacing the local current body.

>         title=skill.name,
>         description=skill.description,
>         content_md=skill.content_md or "",
>         collections=skill.collections or [],
>         is_latest=True,
> --- `backend/app/api/skills.py`

#### MEM-OBJ-skill-version
Label: SkillVersion published archive reference

SRC-1, `backend/app/db/models/skill_version.py`: release metadata lives in Postgres `skill_versions`; `bundle_storage_key` points to separately stored archive bytes. Version, checksum, channel and status are symbolic. Release notes are natural-language descriptions, not necessarily a rationale for the procedure. Archive payloads may contain Markdown, scripts and assets; opaque bundled files cannot be classified by the display name or checksum. Archive consumers install files; actual executable effects depend on their contents and external hosts.

Closest supplied [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install) provides publication/storage/delivery evidence. This object is distinct from [MEM-OBJ-content-version](#mem-obj-content-version), which snapshots current Markdown rather than arbitrary published files. Disabling a release changes download eligibility, not local copies or current-row MCP delivery.

>     bundle_storage_key: Mapped[str] = mapped_column(Text, nullable=False)
> --- `backend/app/db/models/skill_version.py`

#### MEM-OBJ-comment
Label: Comment text and rating fields

SRC-1, `backend/app/db/models/comment.py`, `backend/app/api/comments.py`: Postgres `comments` retains natural-language body and author label, plus symbolic skill ID, author type, comment type, optional rating and linked usage ID. Provenance is caller assertion with referential checks, not verified task evidence. Human and agent authors can submit comments; agent comments require a type. Optional usage linkage checks event existence and, for a nonempty agent event, skill membership. This does not authenticate an outcome.

Closest supplied [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report) discusses adjacent rating feedback; comments are a distinct store and admission endpoint, not the MCP completion row. Rated agent comments fan out into `skill_ratings`, connecting the stores without making them identical. Later context-bundle consumes comment ratings, deprecation type and a latest-body prefix; reporting consumers can retrieve comments. Editing here changes the body only. Deleting removes the comment; this handler does not delete its previously emitted rating row.

>     if payload.author_type == "agent" and payload.rating is not None:
>         db.add(SkillRating(
> --- `backend/app/api/comments.py`

#### MEM-OBJ-usage-event
Label: SkillUsageEvent reported task record

SRC-1, `backend/app/db/models/skill_usage_event.py`, `backend/app/api/openclaw.py`: Postgres stores a natural-language `task_summary` alongside symbolic JSONB skill IDs, outcome/risk/channel labels, resolver confidence and metadata. Metadata payload interpretation is uninspected; numerical confidence is a localized scalar, not distributed-parametric memory. Reports originate from caller-provided agent activity, not an authenticated transcript. Summary admission rejects more than 1000 characters, checks explicit UUIDs and collection identity, resolves slugs and silently drops unknown slugs. The summary is already a caller-produced derivative; raw task dialogue is not retained by this endpoint.

Closest supplied [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use) names usage-informed selection. This declares its input store, not a second selection route. The context bundle counts IDs over 30 days but does not forward task summaries or outcomes in its returned skill records. Dashboard fan-out writes ordinary call events too, so overlap in analytics is deliberate rather than identity of underlying stores.

>         task_summary=payload.task_summary,
>         collection_id=payload.collection_id,
> --- `backend/app/api/openclaw.py`

#### MEM-OBJ-watcher-state
Label: Watcher cursor and deduplication state

SRC-1, `plugin-openclaw/skillnote/log-watcher.py`: local JSON state contains per-file inode, offset, session ID and seen slugs. Representational form: symbolic; later daemon scans use it to suppress replay and resume reading. It is recovery/access state, not learned procedural content. Raw host JSONL stays a separate external trace substrate. The watcher extracts read-tool path matches, not task reasoning or success. Closest supplied [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use) concerns foreground selection, not this parser; no supplied watcher-state counterpart.

>         {"inode": None, "offset": 0, "session_id": "", "seen_slugs": []},
> --- `plugin-openclaw/skillnote/log-watcher.py`

### Routes

#### MEM-RTE-feedback-catalog
Label: Feedback-conditioned catalog delivery
Part of: [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use)

The context-bundle operation is a material alternative within the supplied OpenClaw route, not evidence that its claimed resolver runs. An HTTP caller requests the bundle; code uses retained usage and comments to select current skill rows and compute delivery metadata. SRC-1, `backend/app/api/openclaw.py`. Feedback admission is separate: caller authors summaries/comments, software checks structure/references, and rated agent comments fan out as above. There is no task-answer oracle or objective-based admission gate. Operating mode: open requests and reporting, not controlled comparison. No skill body is rewritten in this operation; aggregates are recomputed from persistent inputs, not stored as a new procedure.

- Immediate return: candidate rows containing description/body, usage count, average comment rating, staleness label and latest comment prefix, plus collections.
- Later read-back: later HTTP requests receive ordering and metadata derived from retained prior usage/comment submissions; an external agent may consume that payload. A deployed foreground/resolver caller is not established.
- Delegated visibility: documented resolver role is afforded the payload; actual subagent wiring remains uninspected.
- Selection predicate: optional collection membership; name-ordered candidate window of max_skills times four; descending 30-day usage, then comment rating, then name; truncation to max_skills. No task summary enters this server selector.
- Invalidation or expiry: counts use a rolling 30-day boundary; comment ratings have no analogous time filter here; latest comment replaces the displayed prefix; any deprecation comment marks needs_review rather than removing the skill.
- Activation or effect: code changes later delivered candidate order/metadata; actual model selection/application and benefit unobserved.
- Evidence limits: request-driven preprocessing is not an unsolicited injection, semantic match or enforced token budget; reasons in older or longer comments may be omitted.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         row.skill_id: row.body[:200] if row.body else None
> --- `backend/app/api/openclaw.py`

>         .where(Comment.comment_type == "agent_deprecation_warning")
> --- `backend/app/api/openclaw.py`

#### MEM-RTE-inbound-resolution
Label: Inbound staging and resolution
Part of: [RT-RTE-browser-sync](runtime.md#rt-rte-browser-sync)

SRC-1, `backend/app/api/claude_ai.py`: reverse import proposes remote body/metadata for registry admission. Server conflict policy and explicit resolution determine adoption, not a quality oracle. Mode: synchronization with policy arbitration. Unlinked existing-slug collisions reject. Local-wins discards incoming content and queues local output. Ask stages a non-latest snapshot, preserving local content; repeated staging can delete the previous non-latest staged row. Normal remote-wins/no-conflict adoption updates current content and creates a latest snapshot. The human UI resolution is an available decision surface, not mandatory for automatic policies or proof of an observed human decision.

- Immediate return: import identity/created flag, rejection or resolution acknowledgment; audit and link state persist alongside content.
- Later read-back: accepted current rows reach registry consumers; staged content is available for later conflict display/resolution rather than normal current-row consumption; keep_skillnote queues the selected local snapshot for the extension.
- Delegated visibility: browser extension obtains outbound content; current-row clients obtain admitted content; conflict UI has a separate staged/local display surface.
- Selection predicate: integration/remote link identity, pre-import latest snapshot and conflict policy; resolution uses explicit staged_version_id, not newest non-latest heuristics.
- Invalidation or expiry: keep_skillnote deletes staged inbound and records its ID in audit; keep_claude_ai promotes staged body; skip clears the staged pointer without changing content; no inferred universal deletion/expiry of historical snapshots.
- Activation or effect: persistent body/pointer changes and outbound queueing are implemented; external acceptance and behavior change unobserved.
- Evidence limits: inspected branches establish adoption/rejection distinctions, not exhaustive detector correctness, remote authorship trust or complete conflict-recovery reliability.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>             is_latest=False,  # staged — user resolves via /resolve
> --- `backend/app/api/claude_ai.py`

>         if staged_inbound is not None:
>             audit_detail["discarded_staged_version_id"] = str(staged_inbound.id)
>             db.delete(staged_inbound)
> --- `backend/app/api/claude_ai.py`

The rejection audit preserves an event and identifier, not necessarily the rejected procedure or its reasons. Subsequent conflict checks consume the re-anchored baseline. No claim that the task-performing host reads rejection rationale follows.

#### MEM-RTE-trace-reporting
Label: Watcher and hook trace reporting

SRC-1, `plugin-openclaw/skillnote/log-watcher.py`, `backend/app/api/hooks.py`: daemon scans host JSONL, selects read-tool paths ending in sn-* SKILL.md, deduplicates by session, posts skill-used, and persists cursor state. This is automatic trace extraction and analytics admission, distinct from [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report)'s rating requests. The hook API also accepts externally generated session evaluation prose and stores at most 500 characters in the call-event agent_name slot. This unconventional field placement does not turn evaluation text into a revised instruction. Proposer: host trace or evaluation caller; selector/admitter: code; no per-event human approval or expected-answer oracle. Mode: ongoing reporting. Failure/recovery is best effort, not an experiment or demonstrated learning.

- Immediate return: accepted/ignored API response, analytics event, and saved local watcher cursor; network failures can be silently ignored.
- Later read-back: subsequent scans read cursor/seen-slug state; analytics reads retained events as described by the supplied runtime's reporting account. This watcher does not write SkillUsageEvent, so its events alone do not increment the context bundle's usage query.
- Delegated visibility: backend receives slug/session/agent identifiers, not the whole JSONL or extracted reasoning; evaluation endpoint receives caller evaluation text.
- Selection predicate: message toolCall named read and matching skill-file path, first unseen slug within a session; pre-existing unseen files with older modification times can start at EOF.
- Invalidation or expiry: inode change resets tracking; malformed/missing state recovers to empty; saved offsets and seen slugs suppress replay; no durable retry queue is established.
- Activation or effect: analytics writes and scanner recovery behavior are implemented, not skill-text revision or verified application.
- Evidence limits: a file read is not proof of use or success; best-effort delivery and heuristic replay suppression prevent complete analytics inference; evaluation generation/quality remains uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         pass  # fire-and-forget — network errors are silently ignored
> --- `plugin-openclaw/skillnote/log-watcher.py`

>             "eval": payload.evaluation[:500],
> --- `backend/app/api/hooks.py`

#### MEM-RTE-install-maintenance
Label: Installed archive update and removal

SRC-1, `cli/src/index.ts`, `cli/src/commands/update.ts`, `cli/src/commands/remove.ts`: explicit CLI update selects installed manifest entries, downloads active release/current archive, verifies supplied checksum and extraction, replaces adapter files and updates manifest. Remove deletes installed files, except user-global shared installs can retain them for another project. Closest supplied [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install) covers add/publish; distinct maintenance invocations act on previously installed state. Caller requests update/removal; code admits bytes by release selection/checks, without per-update semantic/human approval. No answer oracle or measured objective. Operating mode: routine maintenance. Previous destination is removed before copy, so atomic rollback is not established.

- Immediate return: updated/skipped/failed result and manifest change, or removal result and possible shared-files-kept notice.
- Later read-back: host sessions can read replaced or retained installed instructions; later CLI operations read version/checksum/agent manifest fields.
- Delegated visibility: adapter directories expose archive files at project or user scope; exact host discovery/compliance is external.
- Selection predicate: explicit slug or installed entries, first active release; current-mode checksum comparison for never-published content; adapter identities from manifest or detection.
- Invalidation or expiry: update replaces destination and removes legacy project Codex copy; no-active-release skips update rather than deleting installation; remove preserves global files until last project release.
- Activation or effect: file/manifest replacement and deletion are implemented; actual host reload and behavior unobserved.
- Evidence limits: no global-registry implementation audit, transactional multi-adapter rollback or complete withdrawal guarantee; published-version equality skips redownload.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>       if (!releaseGlobalInstall(agentName, skill, projectDir)) {
>         shared.push(adapter.displayName)
>         continue
>       }
> --- `cli/src/commands/remove.ts`

>       if (fs.existsSync(dest)) fs.rmSync(dest, { recursive: true })
>       fs.mkdirSync(dest, { recursive: true })
>       copyDirSync(tmpDir, dest)
> --- `cli/src/commands/update.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-registry-write](runtime.md#rt-rte-registry-write)

Memory parts: current text and snapshots are classified in [MEM-OBJ-skill](#mem-obj-skill) and [MEM-OBJ-content-version](#mem-obj-content-version). SRC-1, `backend/app/api/skills.py`, directly inspected restore/set-latest copies name, description, body and collections; this leaves extra frontmatter and origin outside the snapshot. Restoration uses caller-chosen prior content, not automatically evaluated quality. Supplied SRC-1 `src/lib/skills-store.ts` evidence in the runtime establishes browser localStorage as independent persistence: a locally saved skill can feed later browser reads without registry admission. Local browser text has author/editor authority there, not confirmed cross-client availability.

#### On [RT-RTE-project-sync](runtime.md#rt-rte-project-sync)

SRC-1, `plugin/hooks-handlers/sync.sh`, supplied runtime evidence: project SKILL.md copies carry natural-language instructions plus adapter-generated symbolic frontmatter. Managed manifests are symbolic access/deletion state, not procedural memory. Automatic hook-triggered reload selects collections before delivery; it is push toward host discovery, not proof of unsolicited body injection into a model window. Cached copies retain later-session authority as interpreted host instructions even after some empty/failure responses. Codex cache/lock behavior belongs to its separately inspected handler, not a general registry invariant.

#### On [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery)

SRC-1, `backend/mcp_server.py`, supplied passages: request-selected slug yields current Markdown and optional completion advice in tool-result text. Description metadata controls discovery while returned prose carries policy guidance. The caller pull and provider delivery are separate operations; no index query or semantic ranking follows from slug lookup. Already returned bodies remain external-client context; later list/get reloads current rows rather than revoking earlier text.

#### On [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use)

SRC-1, `plugin-openclaw/skillnote/SKILL.md`, `sync.sh`, supplied passages: synced sn-* files and sidecar survive host sessions. User consent attaches the sidecar to AGENTS; subsequent body selection is foreground-agent description/task overlap policy. Ordinary three-match and five-body caps limit requested loading, not token volume. Unselected bodies stay on disk and can be read later. There is no established isolated resolver frame/return here; the alternative candidate operation is separately declared in [MEM-RTE-feedback-catalog](#mem-rte-feedback-catalog).

#### On [RT-RTE-context-hooks](runtime.md#rt-rte-context-hooks)

SRC-1, `plugin/hooks-handlers/subagent-context.sh`, `compact-context.sh`, supplied runtime evidence: child context receives collection/command pointers rather than full bodies; post-compaction reload requests slugs as reminder material. Raw task traces are not transformed into a retained summary by these handlers. The external host decides preferential eviction, surviving tail/summary and frame isolation. Consequently the stack-frame lens cannot establish any SkillNote-owned frame pop or returned subtask result; only the shipped input reminders are inspectable. Plain-text PostCompact output has unresolved model delivery, not confirmed memory reinjection.

#### On [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report)

SRC-1, `backend/mcp_server.py`, supplied evidence: score/outcome/session fields are persistent feedback, not automatically rewritten procedural content. Direct SRC-1 `backend/app/api/comments.py` adds a connection: agent comment ratings fan out into the rating store, but MCP ratings do not thereby become Comment rows. Thus analytics and OpenClaw candidate averages can share some reports while differing on others. This narrows a possible inference of either total independence or complete unification, without correcting the runtime's stated uncertainty.

## Write side

Acquisition has distinct controls. Human editing and approval-following skill-push are afforded authoring paths, whereas structural POST/PATCH checks admit arbitrary callers' bodies without an approval artifact. Browser fallback persists an editor result independently. Git imports admit selected upstream content under conflict rules; same-source metadata-only updates and stub refresh apply prevent a universal body-refresh claim. These are supplied [RT-RTE-registry-write](runtime.md#rt-rte-registry-write) and [RT-RTE-source-import](runtime.md#rt-rte-source-import), not observed approval or refresh exchanges.

Automatic transformations include content snapshots, frontmatter reconstruction and URL substitutions for installed copies, current-content archive generation, connector staging/adoption and feedback aggregation. Each has different later consumers. ZIP publishing independently admits caller archive bytes, leaving archive payload provenance distinct from current Markdown. Restoring an old snapshot creates a new snapshot; set-latest chooses an existing one. Neither restores fields not included in history. SRC-1, `backend/app/api/skills.py`, and [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install).

The trace chains must remain separate. Host JSONL → watcher read-path event → skill_call_events serves analytics and deduplication, not the bundle's SkillUsageEvent counter. Caller task summary/skill IDs → SkillUsageEvent → later 30-day aggregate changes candidate delivery. Caller comment → Comment and optional SkillRating fan-out → later average/deprecation/latest-prefix selection. These are [MEM-RTE-trace-reporting](#mem-rte-trace-reporting) and [MEM-RTE-feedback-catalog](#mem-rte-feedback-catalog). The latter is automatic trace-fed selection from retained reports, but no durable derived procedure is written. A derived payload is recomputed; raw reports persist. No skill-revision learning or causal capacity improvement is established by these writes.

Maintenance and rejection do not imply universal forgetting. Comment deletion removes a bundle input without retracting its prior rating fan-out. Connector local-wins can delete staged instruction bytes but preserves an audit identity; skip only clears the marker. Disabled releases gate downloads; current-row consumers and cached files can still expose instructions. CLI no-active-version leaves installations untouched; explicit removal can keep shared files. See [MEM-RTE-inbound-resolution](#mem-rte-inbound-resolution), [MEM-RTE-install-maintenance](#mem-rte-install-maintenance), [MEM-OBJ-comment](#mem-obj-comment) and [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install).

Reasons are not a required history field. Comments can carry rationale, but bundle delivery truncates the latest body and omits older discussion; a task-summary record is not sent as selection rationale. Release notes and skill bodies may encode reasons if authors choose, but the frozen source supplies no user corpus establishing that. This distinguishes retained events and display summaries from preserved explanations at a later agent consumer.

## Read-back

Current-row consumers are wired in list/detail, project sync and MCP; archive consumers instead select releases or generated current bundles. Filesystem copies are the eventual external-host surface, with symbolic manifests controlling installation/deletion rather than interpreting the procedure. Browser localStorage supports later editor reads, not guaranteed remote availability. Supplied [RT-RTE-registry-write](runtime.md#rt-rte-registry-write), [RT-RTE-project-sync](runtime.md#rt-rte-project-sync), [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery) and [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install) establish these channels.

The principal automatic push is event-triggered adapter synchronization: hook/configuration triggers select collection-filtered current content and persist files for later host discovery. The foreground host chooses loaded bodies; actual inclusion is external. OpenClaw has description-first instructions and a body-count policy, while MCP is a requested named-tool return. These are different selection operations, not one generic retrieval algorithm. The context-bundle is request-driven feedback preprocessing with a documented external resolver consumer, not confirmed deployed routing or task-conditioned server search.

Direct [MEM-RTE-inbound-resolution](#mem-rte-inbound-resolution) establishes a further consumer: conflict resolution reads staged retained bodies and explicit link pointers, deciding which content can become current or be re-uploaded. The rejected branch's audit ID is not a pointer by which the host can reconstruct deleted text. Direct [MEM-RTE-install-maintenance](#mem-rte-install-maintenance) establishes manifest-guided later refresh/removal. A store API alone would not establish these consumer routes; the inspected caller branches do.

Context preservation remains bounded. Collection filtering keeps irrelevant skills out of discovery; policy body caps keep most bodies unloaded and reloadable from disk. Hooks add pointers or catalog reminders without implementing trimming or summarization. What the external host preferentially evicts, what compacted tail survives and what children return are uninspected. SkillNote's installed files are external retained material, not references whose model-window liveness the registry tracks.

## Integration issues

- No supported correction to a supplied factual assertion is required. The runtime deliberately leaves full reverse-import conflict admission unresolved; [MEM-RTE-inbound-resolution](#mem-rte-inbound-resolution) supplies staging, deletion and promotion detail from SRC-1 `backend/app/api/claude_ai.py`. Its containment is explicit; it does not duplicate the encompassing browser queue route.
- [MEM-RTE-feedback-catalog](#mem-rte-feedback-catalog) is the candidate-endpoint part of [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use), not a second overall selection route. It clarifies latest-comment truncation, 30-day usage scope and warning-as-metadata. A deployed resolver caller remains unestablished, preventing claims of autonomous semantic selection or isolated-frame memory control.
- [MEM-OBJ-comment](#mem-obj-comment) and the annotation on [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report) connect agent comment ratings to SkillRating, while context-bundle averages read Comment. The supplied statement that these are not proven identical is retained; deleting a comment does not retract fan-out in the inspected handler. Reconciliation should not merge the stores or infer common invalidation.
- [MEM-RTE-trace-reporting](#mem-rte-trace-reporting) and [MEM-RTE-feedback-catalog](#mem-rte-feedback-catalog) have different event stores. A watcher read does not automatically contribute to the 30-day bundle count. Supplied feedback reporting is rating admission, not this parser; no duplicate after comparison.
- [MEM-RTE-install-maintenance](#mem-rte-install-maintenance) supplements rather than replaces [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install). Shared global-registry ownership internals remain uninspected, preventing a complete cross-project cleanup guarantee. Update's skip on withdrawal is affirmative code behavior, not automatic revocation.
- Current-row, history, release and staged objects are separately declared because their consumers and rollback differ. No supplied operative-object counterpart exists. Unknown imported body rationale, archive payload contents, arbitrary extra frontmatter and metadata semantics remain local limits; reconciliation must not infer a uniform representational form or provenance from a SKILL.md label.
- Session-eval production and analytics query/display internals remain uninspected beyond stored truncation and supplied reporting claims. [MEM-RTE-trace-reporting](#mem-rte-trace-reporting) therefore does not establish evaluation-driven content updates. Available code could narrow that limit in a correction round; missing execution evidence independently prevents exercised-learning conclusions.

## Limitations and checks

HEAD was rechecked and equals the boundary commit. All added evidence uses SRC-1 at that revision; no additional source identity or evidence layer was introduced. Inspection was static and selective, without executing target code, tests or services. Prompt behavior remains requested behavior; delivered bytes, actual compliance and causal benefit remain separate. No user corpus establishes the content of procedural reasons, model weights or exact host context state.

Deterministic output validation passed using the invocation's prepared `commonplace-run validate-output` command. This checks structure, identity and quote occurrence, not analytical correctness or acceptance.
