---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Hermes Agent memory: bounded notes, skill revision, session recovery, local and opaque compaction, and optional provider recall."
run-id: AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01
source-identity: https://github.com/nousresearch/hermes-agent
reviewed-boundary: "0e427d788d253630d38a3a51cd76849e73cd6925"
---

# Hermes Agent memory report

## Boundary and evidence

Hermes retains several different things: notes and a user profile, reusable skill packages, conversation rows, derived context handoffs, and optional provider-owned memory. They have different selectors and admission controls. This report extends the supplied runtime baseline within the [boundary](boundary.md), which remains a complete artifact with partial loop inspection. All added evidence is SRC-1 implementation or explicitly identified prompt/design text at the frozen commit. No runtime, tests, examples, service requests or experiments were executed.

The memory scope follows the ordinary turn, review, delegation and Codex routes of [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn), [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff), [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation) and [RT-RTE-codex-turn](runtime.md#rt-rte-codex-turn). Static shipped skill text is not itself read-back from use; agent-authored or revised packages are. User configuration and actual retained contents are not supplied. External provider implementations and Codex internals remain excluded; repository-side adapters remain included.

The following inventory distinguishes direct reads from supplied findings. An unresolved included surface is not an evidenced absence. Source paths in this table are SRC-1 commit-relative anchors.

| Entry or operation | Evidence and coverage | Records or unresolved limit |
|---|---|---|
| Agent initialization; system prompt | Direct bounded reads/searches of `agent/agent_init.py`, `agent/system_prompt.py`, `tools/memory_tool_store.py` | Notes/profile load; frozen prompt; compaction refresh: [MEM-RTE-notes-cycle](#mem-rte-notes-cycle). Resume can reuse stored prompt bytes; frontend refresh equivalence is not established. |
| Registered built-in memory tool | Direct `tools/memory_tool.py`, `tools/memory_tool_store.py` | Add/patch/remove/batch, admission and unattended staging: [MEM-RTE-notes-cycle](#mem-rte-notes-cycle). Whole store implementation was not audited for OS durability. |
| Approval and rejection | Direct `tools/write_approval.py`, `hermes_cli/write_approval_commands.py` | Pending payloads, content-pinned memory targets, apply/reject: [MEM-RTE-pending-review](#mem-rte-pending-review). Full gateway authorization is uninspected. |
| Skill tools, catalog and prompt index | Direct `tools/skills_tool.py`, `tools/skill_manager_tool.py`, `tools/skill_manager_guards.py`; searched `agent/prompt_builder.py`, `agent/system_prompt.py` | [MEM-RTE-skill-cycle](#mem-rte-skill-cycle). Plugin-supplied bodies, inline-shell preprocessing, auto-load and slash/preload are alternative delivery paths; full transformations/budgets remain uninspected. |
| Background review | Direct bounded reads of `agent/background_review.py`; supplied finalizer predicate | [MEM-RTE-review-write](#mem-rte-review-write); annotation on [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff). Same-model/full-history and routed/digest alternatives are separate input forms. |
| Idle curator; CLI curator | Direct `agent/curator.py`, `tools/skill_usage.py`; searched `hermes_cli/curator.py` | [MEM-RTE-skill-curation](#mem-rte-skill-curation). Automatic transitions traced; optional consolidation, backup restoration, purge and cron-reference rewrite are named but not end-to-end verified. |
| Session persistence, resume, search and rewind | Direct bounded `hermes_state_messages.py`, `tools/session_search_tool.py`; supplied one-shot resume | [MEM-OBJ-session-content](#mem-obj-session-content), [MEM-RTE-session-recall](#mem-rte-session-recall). Full schema/FTS repair, retention policy, gateway/ACP reload remain uninspected. |
| Local automatic/manual compression, prune and micro-compaction | Direct bounded `agent/context_compressor.py`, `agent/conversation_compression.py`; supplied preflight/finalizer seams | [MEM-RTE-local-compaction](#mem-rte-local-compaction). Manual `here N`, rotation and in-place forms located; micro rolling-summary exact selector and commit semantics remain incompletely inspected. |
| Native Responses checkpoints | Direct `agent/native_compaction.py`; searched adapter wiring in `agent/codex_responses_adapter.py`, `agent/chat_completion_helpers.py` | [MEM-OBJ-native-checkpoint](#mem-obj-native-checkpoint). Opaque payload distinct from text handoff; adapter end-to-end replay remains a limit. |
| Memory hooks/provider services | Direct bounded `agent/memory_manager.py`, `agent/memory_provider.py`, `plugins/memory/retaindb/__init__.py`, `plugins/memory/byterover/__init__.py` | [MEM-RTE-provider-cycle](#mem-rte-provider-cycle). Optional catalog providers are not frozen implementations; exact remote extraction, embedding provenance and deletion semantics are unknown. |
| CLI external-memory setup/off/reset | Direct parser `hermes_cli/subcommands/memory.py` | Exposed reset/off operations located, handlers not traced. Cannot conclude reset removes external state or all cached/persisted copies. Parser's “always active” label is qualified by built-in enable flags. |
| Child frame isolation and async result delivery | Supplied runtime findings, not independently re-traced | [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation). Selected input/return result is not full-parent-history sharing; full async retained completion consumer remains uninspected. |
| Codex app-server history/thread | Supplied runtime findings | [RT-RTE-codex-turn](runtime.md#rt-rte-codex-turn). Thread binding and projection differ from opaque Responses sidecars; external native context is unknown. |
| Result spill, persistent Python kernel, approvals, plugins | Supplied runtime records | [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch), [RT-RTE-code-execution](runtime.md#rt-rte-code-execution), [RT-RTE-command-approval](runtime.md#rt-rte-command-approval), [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission). Retained effects/capabilities exist; full spill reload, approval revocation and kernel cleanup not re-traced. |
| Context files, todo snapshots, external context engines, scheduler/evaluation | Located in `agent/prompt_builder.py`, `agent/system_prompt.py`, `agent/conversation_compression.py`; supplied runtime coverage | Included unresolved parts: editable context-file lineage/admission, todo rehydration and context-engine opaque transformations need fuller tracing. Scheduler recall and evaluation outcomes cannot be inferred from hooks or prompt assertions. |

## Core ideas

1. **Write visibility is delayed, not absent.** Built-in notes and profile have a load-time prompt snapshot and live disk state. A mid-turn write returns current entries without replacing the cached system prefix. An admitted local compaction reloads memory and rebuilds the prompt. Thus “only at session start” is too strong; “immediately influences every future request” is also too strong ([MEM-RTE-notes-cycle](#mem-rte-notes-cycle)).
2. **Procedure memory is selectively loaded.** A skill index exposes names/descriptions; the model or caller selects a body and optional support files. Fresh tool reads can return modified content. A previously loaded body can later become a pruning marker, which requires reload rather than treating a summary of the skill as the full procedure ([MEM-RTE-skill-cycle](#mem-rte-skill-cycle), [MEM-RTE-local-compaction](#mem-rte-local-compaction)).
3. **Review is a second write principal.** A fork interprets a completed trace and writes through restricted tools. It is detached from the real session DB, but deliberately shares the built-in store. Read-before-write and destructive-operation guards enforce narrower rules than the aspirational review prompt. Configured extra tools can broaden dispatch ([MEM-RTE-review-write](#mem-rte-review-write)).
4. **Removal from context need not destroy evidence.** Local compaction can archive raw rows and insert derived handoffs, while on-demand search returns archived material. Rewind rows use a different flag from summarized rows. Native server checkpoints are opaque and cannot be classified as equivalent to readable handoffs ([MEM-RTE-local-compaction](#mem-rte-local-compaction), [MEM-RTE-session-recall](#mem-rte-session-recall), [MEM-OBJ-native-checkpoint](#mem-obj-native-checkpoint)).
5. **Trust is a consumer instruction, not validation of truth.** External recalled text is labelled authoritative reference data in a model-facing fence. Sanitizing fence syntax and redacting egress do not establish the factual warrant of retrieved content ([MEM-RTE-provider-cycle](#mem-rte-provider-cycle), [MEM-BAP-retained-text](#mem-bap-retained-text)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory
Label: Built-in agent notes

Source-native identity: profile-scoped `memories/MEMORY.md` entries, live `MemoryStore.memory_entries` and the corresponding frozen prompt block. Form: natural-language notes interpreted by the model; delimiter and target fields are symbolic storage/dispatch structure. Substrate: UTF-8 file and process snapshot. Lineage: existing file authorship is unknown; foreground tools, approved pending writes and review additions can change it. No mandatory retained rationale field was established. Distinct from [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages): this is a separately bounded cross-session store, not the transcript envelope. SRC-1 `tools/memory_tool_store.py`, `tools/memory_tool.py`.

> ``_system_prompt_snapshot`` is frozen at load time (prefix-cache stable);
> ``memory_entries`` / ``user_entries`` are live state persisted to disk.
> --- `tools/memory_tool_store.py`

#### MEM-OBJ-user
Label: Built-in user profile

Source-native identity: `memories/USER.md`, `user_entries` and its frozen prompt block. Form: natural-language user descriptions/preferences; symbolic target and entry separation. Substrate: UTF-8 file plus process snapshot. Lineage/admission: same mechanisms as notes, but separately enabled and budgeted. Intended subject is the user rather than task procedure. Distinct from [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages) and [MEM-OBJ-memory](#mem-obj-memory): different file, budget, enable flag and prompt header. SRC-1 `tools/memory_tool_store.py`, `agent/prompt_builder.py`.

> self.memory_char_limit, self.user_char_limit = memory_char_limit, user_char_limit
> self.memory_enabled, self.user_profile_enabled = memory_enabled, user_profile_enabled
> --- `tools/memory_tool_store.py`

#### MEM-OBJ-skill-package
Label: Retained skill package

Source-native identity: skill directory containing `SKILL.md` and optional references/templates/scripts. Substrate: project/profile/configured external trees or plugin registry; index caches additionally store descriptions and manifest signatures. Operative parts differ: prose rules/references are natural-language model input; names, platform/dependency fields and lookup paths are symbolic selection/control metadata; scripts and inline-shell templates can have executable symbolic force. Their exact downstream executor/rewrite envelope is not established by reading a body. Lineage can be bundled, hub-installed, hand-authored or agent-created/revised; user state is not captured. Distinct from [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission): a package supplies task instruction/support content, not necessarily a registered handler. SRC-1 `tools/skills_tool.py`, `tools/skill_manager_tool.py`, `agent/prompt_builder.py`.

> "description": "List available skills (name + description). Use skill_view(name) to load full content.",
> --- `tools/skills_tool.py`

#### MEM-OBJ-pending-write
Label: Pending retained-content proposal

Source-native identity: `<HERMES_HOME>/pending/{memory,skills}/<id>.json`. Substrate: JSON file. Symbolic operative payload contains replay kwargs; natural-language content/diff is an editable proposal for human interpretation, not yet adopted memory. Summary/origin/time are access/audit metadata, not a substitute for payload content. Memory destructive proposals can pin the full matched entry; skill proposals can expose diffs. Distinct from [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call): deferred content admission rather than an immediately dispatched call. SRC-1 `tools/write_approval.py`, `hermes_cli/write_approval_commands.py`, `tools/memory_tool.py`.

> "id": pid, "subsystem": subsystem, "action": payload.get("action", ""),
> "summary": (summary or "").strip(), "origin": origin or "foreground",
> "created_at": time.time(), "payload": payload,
> --- `tools/write_approval.py`

#### MEM-OBJ-session-content
Label: Retained session content and sidecars
Part of: [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages)

This part owns the retained content rather than the supplied record's coordination envelope. Substrate: SQLite message rows plus process copies. Natural-language user/assistant/tool text is raw trace content; local handoff text is derived content. `api_content` stores model-facing injected bytes separately from display text. Active/compacted flags, IDs and lineage are symbolic access metadata. Reasoning/media sidecars have different consumers and can contain opaque checkpoint payloads; see [MEM-OBJ-native-checkpoint](#mem-obj-native-checkpoint). Source origin is mixed: user, model, tools, plugins/providers and synthetic handoff code. Persistence alone is not trace-fed learning. SRC-1 `hermes_state_messages.py`, `agent/turn_context.py`.

> return "" if include_inactive else (_DISPLAY_ACTIVE_CLAUSE if include_compacted else " AND active = 1")
> --- `hermes_state_messages.py`

#### MEM-OBJ-native-checkpoint
Label: Opaque native compaction checkpoint
Part of: [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages)

Source-native identity: Responses `type: compaction` items carrying `encrypted_content` in `codex_reasoning_items`. Substrate: response/transcript sidecar and serialized session row. The item's type/position is symbolic replay control; encrypted content is opaque to this inspection. Its internal representational form, extraction rationale and summarization fidelity are uninspected, not assumed natural-language or numerical. A readable local summary carried beside it is a separate object part, not its plaintext display. Provider-derived lineage follows earlier context; exact server transformation is excluded. Distinct from [RT-RTE-codex-turn](runtime.md#rt-rte-codex-turn): this is Responses-side checkpoint replay, not an app-server thread binding. SRC-1 `agent/native_compaction.py`, `hermes_state_messages.py`.

> _is_compaction_item(item)
> and isinstance(item.get("encrypted_content"), str)
> and bool(item["encrypted_content"].strip())
> --- `agent/native_compaction.py`

#### MEM-OBJ-provider-state
Label: Optional provider memory alternatives

Source-native parts: RetainDB local `retaindb_queue.db`, remote stored messages/facts/files/profile and returned context/dialectic/agent-model displays; ByteRover CLI-owned persistent tree and optional cloud state. Local queue envelopes and API fields are symbolic. Returned prose is natural-language model input. Service embeddings, inferred profiles and internal synthesis state are opaque; exact numerical provenance and storage cannot be established from adapter names. Raw transcript ingress is distinct from any remotely derived fact. Initial store content is unknown. Distinct from [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission): this is provider-retained material, not loader admission. SRC-1 `plugins/memory/retaindb/__init__.py`, `plugins/memory/byterover/__init__.py`.

> self._queue = _WriteQueue(self._client, home / "retaindb_queue.db")
> --- `plugins/memory/retaindb/__init__.py`

> return ("# ByteRover Memory\nActive. Persistent knowledge tree with hierarchical context.\n"
>         "Use brv_query to search past knowledge, brv_curate to store important facts, brv_status to check state.")
> --- `plugins/memory/byterover/__init__.py`

### Routes

#### MEM-RTE-notes-cycle
Label: Built-in notes retention and reload

Endpoint/progression: model tool proposal → validation/approval or staging → locked disk reread → mutation → file/store result → later load-time snapshot → system prompt. Owner: foreground/review model proposes content; tool/store software enforces operation and capacity checks; optional human decision admits or vetoes a specific write. Generic caller identity does not establish human authorship of existing files. Defaults are 2200 note and 1375 profile characters, configurable. External edits can exceed limits: load warns but does not truncate. Add/patch scan content; load replaces threat hits in the prompt snapshot while keeping raw entries removable. Unique-match, stale pinned-entry and drift checks constrain destructive operations. A batch checks final budget rather than requiring capacity before each constituent action. SRC-1 `tools/memory_tool.py`, `tools/memory_tool_store.py`, `agent/system_prompt.py`, `agent/conversation_compression.py`.

Proposal guidance routes stable notes/profile versus procedures in `agent/prompt_builder.py`; it is model instruction, not a semantic admission oracle. Open heuristic retention; no expected factual answer/reference outcome. Rejection leaves content uncommitted; drift can retain a backup. Remove/patch withdraw disk content but do not retroactively erase cached prompts, old tool results, transcripts or provider mirrors. Unattended review destructive ops are staged even when ordinary write approval is off. Compaction reload is a counterexample to the module's simplified session-start-only description. Distinct route from [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch): scoped store admission and later prompt consumer, not generic effect dispatch.

- Immediate return: JSON success/error, current entries and usage; staged success is not a store update.
- Later read-back: whole enabled notes/profile snapshots enter system prompt on load; ordinary cached requests retain old bytes until a refresh boundary. Local admitted compaction reloads/rebuilds; seeded detached compression can deliberately retain old prompt bytes.
- Delegated visibility: ordinary delegation skips memory by supplied [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation); review rebinds the parent's store.
- Selection predicate: enabled target; no query ranking for built-in prompt blocks; writes require valid operation, matching target and capacity/security/admission checks.
- Invalidation or expiry: explicit patch/remove/reset surfaces; no age TTL established. Cached/transcript copies have separate lifetimes.
- Activation or effect: wired disk update and model-input delivery, not observed changed behavior or factual correctness.
- Evidence limits: external file authorship, configuration, actual updates and frontend refresh equivalence are unobserved; reset handler and provider withdrawal semantics remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if agent._memory_store:
>     agent._memory_store.load_from_disk()
> --- `agent/system_prompt.py`

#### MEM-RTE-pending-review
Label: Pending proposal approval or rejection

Endpoint/progression: gated memory/skill tool payload → pending JSON → list/diff → approve/reject → subsystem replay → remove successful pending record or retain failure. Owner: software stages/displays/replays; human-facing command chooses the proposal to apply or reject. Default approval off permits direct writes; gate on stages skills/background writes and can prompt foreground memory inline. Missing/invalid config disables this optional gate, and the built-in memory tool's import failure is fail-open. This is not a universal human veto on file/tool effects. Open content-admission mode, no answer oracle. The proposal text persists separately from its display summary. Failed staging can return a record although disk write was lost, so pending existence is not guaranteed by a returned ID. SRC-1 `tools/write_approval.py`, `tools/memory_tool.py`, `hermes_cli/write_approval_commands.py`.

Distinct from [RT-RTE-command-approval](runtime.md#rt-rte-command-approval): per-content memory/skill replay, not terminal-command authorization. Approval revalidates via subsystem appliers; memory target pinning prevents matching a changed entry. Rejection deletes the proposal, not already adopted content. Recovery retains failed pending records; successful replay deletes them. Full authenticated transport and skill target race behavior remain uninspected.

- Immediate return: staged ID or gate denial; command returns pending list/diff or apply/reject counts and changed-entry text.
- Later read-back: commands load exact pending payload; adopted output reaches the notes/skill consumers, not the model merely by being pending.
- Delegated visibility: background origin is metadata; command's complete payload, not fork conversation, is replayed.
- Selection predicate: subsystem/config/origin/interactive availability, then exact ID or explicit all; content pinning for destructive memory writes.
- Invalidation or expiry: reject removes JSON; successful apply discards it; stale target/application error retains it. No pending TTL inspected.
- Activation or effect: wired replay/withdrawal; staging alone has no live memory authority.
- Evidence limits: returned stage success does not prove durable pending file; commands being human-facing do not establish deployed gateway authorization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if ok:
>     wa.discard_pending(subsystem, rec["id"])
>     applied += 1
> --- `hermes_cli/write_approval_commands.py`

#### MEM-RTE-skill-cycle
Label: Skill content mutation and selective load

Endpoint/progression: model/caller proposes skill change → optional pending gate → validation and origin guards → atomic file write/security scan → scan rollback or result/metadata → catalog/index and requested body/file load → later model. Owner: model authors/revises; code admits by shape/size/path/read marks and security policy; optional human gate approves content. Initial authorship remains mixed/unknown. The inspectable manager supports create/edit/patch/delete/support-file operations; advisory lint is not a hard quality evaluator. A blocked security scan restores original content or removes a new target. Open task-procedure retention, not a bounded experiment or answer oracle. SRC-1 `tools/skill_manager_tool.py`, `tools/skill_manager_guards.py`, `tools/skills_tool.py`, `agent/prompt_builder.py`, `agent/system_prompt.py`.

Bodies can retain reasons in prose, but no required historical-rationale field or separately verified rationale consumer was established. Scripts/templates are materially different support parts: tool viewing is not proof of their later execution. Closest supplied record [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) covers call execution; this route adds retained package editing and selection. Index/preload/plugin routes overlap [RT-BAP-task-prompt](runtime.md#rt-bap-task-prompt) only at model-input authority.

- Immediate return: JSON mutation status, previews/advisory lint; body view returns content, linked-file inventory, readiness and path metadata.
- Later read-back: prompt index advertises eligible names/descriptions; foreground model requests body/support file by name/path. Auto-load and slash/preload can deliver bodies without a `skill_view` proposal; their exact rendering is incompletely traced.
- Delegated visibility: skip-context child construction prevents assuming inherited parent file/body context; explicit selected task text can carry it. Review fresh reads count separately from quoted transcript content.
- Selection predicate: search-root priority, name/path, platform, disabled status, tool availability and caller request; body preprocessing can alter returned text.
- Invalidation or expiry: edits replace content; scan rollback restores pre-write target; foreground deletion can remove package; curator archives have a different reversible path. Existing model context is not automatically erased.
- Activation or effect: wired file mutation and selective model delivery; dependency metadata may invoke package ensure on view. Reliable procedure compliance is unobserved.
- Evidence limits: full batch atomicity, hub admission/audits, inline shell execution policy and transformed auto-load/plugin content remain uninspected; no skill-quality benefit measured.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> atomic_write_text(target, content, preserve_mode=True, create_mode=0o644)
> scan_error = _security_scan_skill(skill_dir)
> if not scan_error:
>     return None
> if original is not None:
>     atomic_write_text(target, original, preserve_mode=True)
> else:
>     target.unlink(missing_ok=True)
> --- `tools/skill_manager_tool.py`

#### MEM-RTE-review-write
Label: Trace-fed review retention

Endpoint/progression: supplied completed-turn handoff → detached fork → full snapshot or routed digest → review guidance/model decisions → whitelisted reads and memory/skill tools → accepted stores or pending proposals → later notes/skill consumer. Owner: finalizer chooses trigger; fork model selects content; store/skill guards decide admissibility; human can veto gated/staged content. Distinct continuation of [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff), whose referent ends at scheduling, not a duplicate declaration. SRC-1 `agent/background_review.py`, `tools/memory_tool.py`, `tools/skill_manager_guards.py`.

The fork shares the built-in store but has no session DB and persistence disabled. Same-model path inherits cached prompt/tool schema; different-model path can use a digest. Dispatch whitelist is distinct from advertised schemas, includes file reads and optional configured extra tools. The prompt asks for class-level lessons, updates to loaded skills, user corrections, and no reliable-workflow claims from unresolved failures. Read-before-write is code-enforced for existing skill targets. Memory adds can proceed; unattended patch/remove is staged. An explicit attended refine fork changes that destructive-operation gate, not every other policy. Cancellation prioritizes foreground and bounded waiting, but does not roll back prior store writes. Open heuristic review; model judgment supplies no answer oracle. Trace source is mixed user/model/tool conversation, not independent verified outcomes.

- Immediate return: best-effort background execution/cleanup; fork reply is not the foreground answer, and can be discarded while writes survive.
- Later read-back: accepted notes/profile load into later prompts and skill changes into later indexes/views; pending changes require approval first. Reasons persist only if authored into accepted content or audit evidence, not automatically as the whole review conversation in real session history.
- Delegated visibility: fork sees selected snapshot or compact digest; it does not publish its harness conversation into the parent DB; shares store and may have broader configured tools.
- Selection predicate: supplied interval/availability trigger, review-memory flag, auxiliary routing/input budget, model-selected lesson and per-tool admission.
- Invalidation or expiry: cancellation/supersession, 16-iteration review cap and aggregate input-token budget; no transaction rolls back earlier accepted content when the fork is interrupted.
- Activation or effect: wired automatic trace-fed pathway to durable behavior-shaping prose; no exercised retention or changed later behavior observed.
- Evidence limits: exact trace-selected lesson correctness, retention rationale and reliable compliance are unestablished. Unobserved writes do not negate architectural trace-fed capacity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> review_agent._memory_store = agent._memory_store
> --- `agent/background_review.py`

> review_agent._skip_mcp_refresh = review_agent._persist_disabled = review_agent.suppress_status_output = True
> review_agent._end_session_on_close = False
> review_agent._session_db = None
> review_agent.session_id = agent.session_id
> --- `agent/background_review.py`

#### MEM-RTE-skill-curation
Label: Activity-driven skill withdrawal

Endpoint/progression: idle/interval or manual curator → usage/provenance selection → active/stale/archived state → archive move/suppression → later catalog changes or restore. Owner: deterministic rules select aging; optional consolidation fork selects content changes; human/config can pause, pin or opt in. Default consolidation is off, unlike enabled deterministic transitions. This route is distinct from post-turn [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff): idle lifecycle maintenance, not immediate completed-turn lesson review. SRC-1 `agent/curator.py`, `tools/skill_usage.py`, `tools/skill_manager_guards.py`.

Admission uses provenance, pinning, activity times and cron references, not a correctness oracle. Unknown first sight seeds the clock rather than expiring immediately. Default stale/archive thresholds are 14/30 days. Archiving physically relocates package to `.archive`, updates lifecycle state and can suppress bundled reseeding. Restore refuses collisions and restores to flat layout; it does not reconstruct original nesting. Foreground delete differs from autonomous archive. Optional model consolidation uses different content guidance and backups/reports; complete rollback and cron rewrite are not settled here. Usage metadata is symbolic access/maintenance state, not retained knowledge or evidence that the procedure is correct.

- Immediate return: transition counts/status, archive/restore status and curator reports; optional content changes use manager tools.
- Later read-back: later catalog/index/body lookup sees current tree/suppression state; restore can re-admit a package. Already cached instructions can remain until a reload boundary.
- Delegated visibility: optional curator fork inspects selected library state rather than the full live user transcript; exact fork input remains incompletely inspected.
- Selection predicate: enabled/not paused/elapsed interval and idle caller; curator eligibility, pinned/cron protection, last activity or creation clock; optional consolidation configuration.
- Invalidation or expiry: stale transition then archive move; restore/collision guards; manual purge and full rollback handlers are uninspected.
- Activation or effect: wired autonomous metadata changes and package withdrawal; reduced prompt availability is conditional on later rebuild/lookup.
- Evidence limits: actual curator scheduling, optional consolidation quality, complete backup/rollback and purge are not observed or end-to-end traced; aging is not a quality judgment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if row.get("pinned") or name in protected:
>     continue
> --- `agent/curator.py`

> _toggle_suppressed_name(skill_name, add=archiving)
> set_state(skill_name, STATE_ARCHIVED if archiving else STATE_ACTIVE)
> --- `tools/skill_usage.py`

#### MEM-RTE-local-compaction
Label: Local transcript compaction and recovery

Endpoint/progression: preflight/post-tool/manual/post-turn pressure trigger → optional provider checkpoint → tool/media pruning and head/tail selection → summary model or deterministic fallback → growth/failure/lease checks → in-place archive-and-insert or rotation → subsequent model request and archive recall. Owner: code decides trigger/budgets/rejection; summary model proposes prose; code commits; human manual focus shapes selection but is not per-summary approval. Distinct from [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn): the retained raw-to-derived transformation rather than enclosing turn. SRC-1 `agent/context_compressor.py`, `agent/conversation_compression.py`, `hermes_state_messages.py`.

Default lean mode uses a small bounded recency tail; legacy mode uses a larger token-ratio tail. Tool results are preferentially stubbed/deduplicated, stale media removed and recent skill bodies protected or marked pruned; tool-call argument control is not equated with prose result pruning. Summary input can itself be sampled/elided. Output preserves selected user/task anchors, structured handoff and recovery pointers, not a lossless transcript. Empty/truncated/access/network failures can abort; other configured failure paths insert deterministic incomplete handoff rather than guaranteeing a model summary. Grown candidates can be refused. Required checkpoint v2 capability/success gates local compaction; ByteRover's asynchronous v1 flush does not satisfy it. Admission is structural/resource/recovery policy, not truth evaluation or an answer oracle. No universal retention of reasons follows from the summary prompt.

- Immediate return: compacted working messages/prompt or unchanged input on refusal/abort; deterministic fallback is separately signalled.
- Later read-back: next model invocation consumes handoff plus protected material; active session rows permit resume; raw summarized rows remain archived and recoverable via [MEM-RTE-session-recall](#mem-rte-session-recall). Skill markers instruct reload rather than replace full skill content.
- Delegated visibility: child context is already isolated; detached review compression is persistence-isolated. Manual `here N` can retain an explicit verbatim tail; alternative rotation carries a continuation session.
- Selection predicate: request pressure, tail mode/budgets, tool grouping, recent user/reply anchors, optional manual focus, provider checkpoint and growth/lease checks; summary source is mixed conversation trace.
- Invalidation or expiry: new handoff replaces live middle, not archived evidence; summaries iteratively merge. Failure/cancellation before commit preserves input; commit failure prevents treating the candidate as durable. Full micro-summary lifecycle remains incompletely inspected.
- Activation or effect: wired trace-fed context reduction and later model input; no causal benefit or semantic completeness observed.
- Evidence limits: sampled summary input and partial inspection prevent lossless-retention claims; plugin context-engine alternatives, micro selector and all rotation recovery cases are not fully traced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not summary:
>     summary = self._fallback_summary_for_window(
>         telemetry, turns_to_summarize, compress_end - compress_start, feasibility_skip,
>     )
> # Phase 4: Assemble compressed message list
> compressed = self._assemble_compressed(messages, compress_start, compress_end, scan, summary)
> --- `agent/context_compressor.py`

> agent._session_db.archive_and_compact(
>     agent.session_id, persisted, model_config_patch={PROACTIVE_PRUNE_REARM_MODEL_CONFIG_KEY: None},
> --- `agent/conversation_compression.py`

#### MEM-RTE-session-recall
Label: On-demand retained session recall

Endpoint/progression: model `session_search` request → browse/search/read/scroll dispatch → SQLite/FTS and lineage filtering → bounded hydrated message results → tool result → later model. Owner: foreground model requests content; code ranks/filters/shapes; optional explicit profile chooses another store. Default discovery searches user/assistant text, deduplicates lineages, demotes cron and hydrates only the highest-ranked result fully in adaptive mode. It does not indiscriminately push entire history. Distinct from [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn): requested archive retrieval rather than caller-selected resume. SRC-1 `tools/session_search_tool.py`, `hermes_state_messages.py`.

- Immediate return: JSON snippets/bookends, session metadata/link and IDs for scroll, or bounded read result/error.
- Later read-back: raw archived or previous session content returns by tool channel; resume separately loads active working projection, not every display/audit row.
- Delegated visibility: live current-lineage/delegation hits are excluded unless content left context; no assumption that parent sees every child transcript.
- Selection predicate: query/FTS, optional role/time/exclusion/profile, lineage/live-context flags; explicit session ID or around-message anchor selects read/scroll. Identifier lookup is not semantic targeting by itself.
- Invalidation or expiry: compaction archives remain eligible; rewind/undo rows use inactive non-compacted flags and are excluded from ordinary display/live projections, though audit reads can include them.
- Activation or effect: wired re-access to retained evidence; snippets can inform decisions but are not reliable compliance or truth certificates.
- Evidence limits: full FTS repair/inactive search policy and data deletion horizons uninspected; actual retrieval quality and model use unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if current_session_id and raw_sid == current_session_id and not is_compacted_hit:
>     continue
> --- `tools/session_search_tool.py`

#### MEM-RTE-provider-cycle
Label: Optional provider write and recall

Endpoint/progression: hooks/tool calls → egress redaction → provider queue/CLI/API ingress → opaque retained transformations → prefetch or explicit query → manager sanitization/dedup/spill → fenced `api_content` → model. Owner: manager schedules and fences; provider selects/transforms retained material; model interprets returned prose. Human/config chooses provider/auto extraction, not necessarily approves each retained fact. Supplied [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) concerns tools; this route additionally covers unsolicited hook writes and automatic recall. SRC-1 `agent/memory_manager.py`, `agent/turn_context.py`, `plugins/memory/retaindb/__init__.py`, `plugins/memory/byterover/__init__.py`.

RetainDB queues user/assistant pairs and turn-end prefetches context, user synthesis and agent self-model; next-turn `prefetch` consumes caches rather than issuing a fresh query with that turn's argument. ByteRover runs a current-query CLI recall and can asynchronously curate truncated turn pairs (2000 characters each), add/replace memory mirrors and the last ten pre-compression messages (500 characters each). It does not mirror every patch/remove. Thus local withdrawal cannot be presumed to withdraw external copies. Manager can handle successful memory-tool mirrors and delegation hooks, but complete provider-specific deletion/trace retention is not established. Remote fact extraction/embedding rationale and storage are opaque. No source-supported answer oracle or factual admission evaluator is established at the adapter. Provider tool schemas include more than automatic recall; explicit stored-file read/ingest/delete in RetainDB have distinct remote effects and unknown service enforcement.

- Immediate return: query/tool result or scheduled async sync; hook success does not prove derived content persisted or was later selected.
- Later read-back: nontrivial user turn triggers automatic prefetch before first model request; recall enters fenced API content and can replay in persisted sidecars. Explicit provider tools deliver selected query/read results. RetainDB cache selector uses prior queued query; ByteRover uses current query.
- Delegated visibility: manager exposes delegation hook input; exact deployed provider use is unknown. Review initialization skips external provider lifecycle, with configured extra-tool exceptions requiring separate inspection.
- Selection predicate: configured provider/tool gates, nontrivial query and skill-scaffolding stripping, provider-specific filters/ranking/cache; external timeout defaults to eight seconds and optional spill limits output. Remote ranking/budget unknown.
- Invalidation or expiry: prefetch caches consume/reset; timed-out provider skipped while thread lives; bounded sync drain/shutdown is best effort. ByteRover delete mirroring is not implemented by its inspected add/replace hook; complete service deletion unknown.
- Activation or effect: wired repository-side write/recall delivery conditional on provider configuration; remote transformation is opaque and actual behavior unobserved.
- Evidence limits: service/CLI internals, exact derived content, embedding lineage and successful durable sync are excluded/unobserved; recalled “authoritative” label establishes requested reliance only.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "NOT new user input. Treat as authoritative reference data — "
> "this is the agent's persistent memory and should inform all responses.]\n\n"
> --- `agent/memory_manager.py`

> if self._auto_extract_enabled("memory mirror") and action in {"add", "replace"} and content:
> --- `plugins/memory/byterover/__init__.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-text
Label: Retained text model-input authority

Consumer: foreground model or review model at a later invocation. Channels: whole notes/profile system blocks, skill index/body/support text, local context handoff and recalled API-content fence. Force: natural-language guidance/reference interpreted by the numerical component [RT-CMP-inference-model](runtime.md#rt-cmp-inference-model); delivery does not prove compliance, correctness or benefit. Horizon: requests in a session and later sessions conditional on store reload/selection. Executable scripts, plugin handlers and opaque provider checkpoints are not asserted to share this force. This spans several retained inputs and overlaps [RT-BAP-task-prompt](runtime.md#rt-bap-task-prompt), but specifies retained-content paths, not all caller instructions. SRC-1 `agent/system_prompt.py`, `agent/turn_context.py`, `tools/skills_tool.py`, `agent/context_compressor.py`.

> volatile_parts: list[str] = [skills_prompt, *_memory_parts(agent)]
> --- `agent/system_prompt.py`

## Annotations

#### On [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff)

Memory-specific continuation is [MEM-RTE-review-write](#mem-rte-review-write). Snapshot or routed digest supplies mixed raw trace to the review model; shared notes/skill stores supply durable write results. Persistence isolation applies to fork transcript/real session DB, not to those stores. Subsequent notes load and skill view/index are wired consumers, not evidence that any update improved behavior. SRC-1 `agent/background_review.py`, `tools/memory_tool.py`, `tools/skill_manager_guards.py`; supporting passages are in that continuation record.

## Write side

The built-in stores separate physical I/O, authorship and admission. Model-authored text is scanned/budgeted and optionally human-gated; externally authored existing file text is unknown in origin and can bypass write-time capacity. Load-time sanitization changes the prompt projection while retaining removable raw material ([MEM-RTE-notes-cycle](#mem-rte-notes-cycle)).

Skills use different admission: shape/path/size checks, optional pending approval, read marks for review overwrites and rollback on blocked security scan. Advisory lint reports convention violations after successful writes; it does not validate the procedure's effectiveness ([MEM-RTE-skill-cycle](#mem-rte-skill-cycle)). Pending payloads are neither adopted content nor proof of durable proposal existence. Apply/reject commands consume them; successful apply removes proposal JSON, failed replay retains it ([MEM-RTE-pending-review](#mem-rte-pending-review)).

Automatic review is a trace-fed content transformation: mixed conversation → model-selected lesson → guarded accepted notes/procedure → later prompt/view. The prompt requests encoding user corrections and warns against turning unresolved failed attempts into reliable guidance. Those requests are not observed formulated criticism or reliable lesson formation. No mandatory reasons field preserves the justification for every adopted rule. The whole fork conversation is intentionally not a real-session transcript ([MEM-RTE-review-write](#mem-rte-review-write)).

Curator age transitions curate availability rather than truth. Usage/provenance/pinning are control metadata. Archive/restore is distinct from hard deletion and from review content patches; pinning does not universally prevent editing a pinned skill ([MEM-RTE-skill-curation](#mem-rte-skill-curation)). Optional consolidation, reports, backup and purge are unresolved maintenance parts, not collapsed into “all curation is reversible.”

Compaction has three result families: readable model-generated handoff, deterministic incomplete handoff and opaque server checkpoint. Local raw trace can survive in SQLite while the active projection is replaced. Reasons and omitted detail are not guaranteed to survive in the handoff. Summary-input sampling is another lossy stage before output generation. Micro-compaction uses rolling-summary bookkeeping and is a named incompletely traced alternative, not silently assumed to share batch selector/commit behavior ([MEM-RTE-local-compaction](#mem-rte-local-compaction)).

Provider ingress is also potentially trace-fed, but retaining raw pairs in a queue is not proof of a derived behavior-shaping update. ByteRover's explicit curate request supplies truncated trace; its actual tree transformation is external. RetainDB returned profile/synthesis/self-model has opaque derivation. The corresponding later adapters are present without demonstrated benefit ([MEM-RTE-provider-cycle](#mem-rte-provider-cycle)).

## Read-back

Built-in notes/profile are automatically supplied wholesale on reload, not targeted by a request query. Prompt caching delays adoption of new disk text. Skill index is automatic supply of eligible descriptions; body/support-file selection is normally model- or caller-requested. Automatic skill loading, slash/preload and plugin bodies are alternate admission channels requiring fuller transformation inspection ([MEM-RTE-notes-cycle](#mem-rte-notes-cycle), [MEM-RTE-skill-cycle](#mem-rte-skill-cycle)).

Local handoff is code-selected automatic supply to later model calls, with head/tail/recovery stubs and archived original evidence. Native Responses selection additionally sends the latest checkpoint run plus budgeted plaintext user messages/local summaries: 64,000 and 32,000 token budgets respectively in SRC-1 `agent/native_compaction.py`. Newest-first selection can truncate a boundary user string and drops other pre-checkpoint material. Checkpoint-required configuration suppresses server-side native compaction so the local pre-checkpoint hook can run first. The adapter wiring was located, but exact full replay was not re-traced; the encrypted payload's actual contents remain unknown ([MEM-OBJ-native-checkpoint](#mem-obj-native-checkpoint)).

> if getattr(agent, "compression_checkpoint_required", False) is True:
>     _warn_native_compaction_suppressed_by_checkpoint_gate()
>     return None
> --- `agent/native_compaction.py`

Session search is a request → search/read selector → bounded tool result chain. It brings removed evidence back, not the whole original window. Resume is a separate caller action using active model projection. Rewind inactive rows are not equivalent to compaction-archived rows ([MEM-RTE-session-recall](#mem-rte-session-recall)).

External prefetch is automatic recall initiated by code at turn start; explicit provider tools are requested recall. RetainDB's queued prior-query cache and ByteRover's current-query selector must not be merged into one synchronous semantic retrieval story. Recalled prose's consumer authority is a model instruction, not a fixed-rule correctness guarantee ([MEM-RTE-provider-cycle](#mem-rte-provider-cycle)).

Child contexts resemble a separate frame: selected inputs enter and return values cross back. The analogy stops at shared filesystem effects and retained child sessions; dropping a child result does not free those effects. Local eviction differs: the window retains a derived handoff/stub rather than a dereferenceable pointer, though session-search IDs can request archived text. A pointer in text has no automatic liveness/reload semantics ([RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation), [MEM-RTE-local-compaction](#mem-rte-local-compaction)).

## Integration issues

- **Boundary wording qualification:** the background-review module description says writes go straight to stores. Optional approval and unconditional unattended destructive-memory staging can instead retain a proposal. SRC-1 `tools/memory_tool.py`, `tools/write_approval.py` support [MEM-RTE-pending-review](#mem-rte-pending-review), [MEM-RTE-review-write](#mem-rte-review-write). This qualifies design prose, not the boundary identity.
- **Snapshot horizon:** the memory module's session-start-only description is incomplete: compaction reloads/rebuilds; seeded detached compression can retain old bytes. Do not infer either immediate refresh or permanent session freezing from [RT-BAP-task-prompt](runtime.md#rt-bap-task-prompt). See [MEM-RTE-notes-cycle](#mem-rte-notes-cycle), SRC-1 `agent/system_prompt.py`, `agent/conversation_compression.py`.
- **Possible authority overlap:** [MEM-BAP-retained-text](#mem-bap-retained-text) overlaps [RT-BAP-task-prompt](runtime.md#rt-bap-task-prompt) at model-input delivery but narrows to retained material. Reconciliation should keep distinct scope or establish container identity, not duplicate the force claim. The session-content and native-checkpoint declarations are explicit parts of [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages), not replacement containers.
- **Handoff versus downstream route:** [MEM-RTE-review-write](#mem-rte-review-write) continues [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff). They share a trigger seam but have different endpoints. No supplied fact needs correction beyond interpreting “uninspected” downstream fields as now supported by the continuation.
- **Incomplete alternatives:** native checkpoint replay, micro rolling-summary selector, opaque context engines, todo rehydration, spill reload and editable context-file admission remain named unresolved parts. SRC-1 anchors and missing conclusions are in the coverage table; [MEM-RTE-local-compaction](#mem-rte-local-compaction), [MEM-OBJ-native-checkpoint](#mem-obj-native-checkpoint) cannot warrant a unified lossless memory policy.
- **Maintenance and frontend gaps:** full optional curator consolidation/rollback/purge/cron rewrite, skill hub acquisition/audit, slash/auto-load preprocessing, CLI memory reset and gateway/ACP lifecycle/authorization remain partially inspected. These prevent exhaustive admission/recovery and cross-frontend equivalence claims; see [MEM-RTE-skill-curation](#mem-rte-skill-curation), [MEM-RTE-skill-cycle](#mem-rte-skill-cycle), [MEM-RTE-pending-review](#mem-rte-pending-review).
- **Provider withdrawal:** ByteRover's inspected mirror accepts add/replace, not patch/remove; remote deletion and archive provenance are unknown. A local delete therefore cannot establish system-wide forgetting. See [MEM-RTE-provider-cycle](#mem-rte-provider-cycle), SRC-1 `plugins/memory/byterover/__init__.py`.
- **Independent epistemic assessment:** [RT-CLM-product-work](runtime.md#rt-clm-product-work) requests a learning account. This report establishes memory pathways only. Formulated criticism, improved capacity and exercised self-improvement require independent evidence; no observed run closes retained-update → changed-later-behavior attribution.

## Limitations and checks

Source identity was rechecked with Git: HEAD equals the full reviewed commit. The supplied invocation, member types, collection, worker rules, boundary, runtime and record contract were read completely. Added coverage remains bounded source inspection at SRC-1; source paths are not evidence of exercised behavior. No new source identity or boundary was introduced. No numerical component was duplicated: [RT-CMP-inference-model](runtime.md#rt-cmp-inference-model) supplies provider/model mutability limits; summary and review routing need not share one numerical checkpoint.

Strong claims were challenged against alternate paths: compaction refutes session-start-only visibility; pending writes refute unconditional direct-store retention; provider mirrors refute universal withdrawal; deterministic and opaque handoffs refute a single lossless summary ontology; fresh skill reads and read marks refute treating quoted prior context as sufficient write evidence. Supported architectural trace-fed retention coexists with unobserved activation and benefit.

Deterministic output validation passed through the required invocation check after correcting two miscopied code quotations against freshly reread source. No finding was narrowed or withdrawn. The check establishes form and quote occurrence, not analytical acceptance or observed effectiveness.
