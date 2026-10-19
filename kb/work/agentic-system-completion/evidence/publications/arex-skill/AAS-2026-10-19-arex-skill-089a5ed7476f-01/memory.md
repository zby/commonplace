---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AREX-Skill memory: managed guidance, session projections, branch checkpoints and workflow replay at a partial-loop boundary."
run-id: AAS-2026-10-19-arex-skill-089a5ed7476f-01
source-identity: https://github.com/VectorSpaceLab/AREX-Skill
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill memory report

## Boundary and evidence

This report uses SRC-1 in the [boundary](boundary.md#source-register), at ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6. The checkout HEAD was rechecked against that identity. It preserves the complete-artifact, partial-loop boundary. It includes installed repository guidance, routing and management metadata, session logs and their model-facing projections, compaction, branch summaries, extension payload alternatives, project instructions, and selected dynamic-workflow state and isolated consumers. Code supplies implementation evidence; verification and routing procedures supply doctrine/design. No target was executed, no example run was inspected, and no observed activation or benefit is established.

Direct reads extend the supplied runtime at the paths below. The registered source is unchanged. Shipped static skills establish available guidance, not accumulated experience by themselves. Importing, revising or installing them creates a possible later read-back path. External provider state, external host implementations and upstream scientific repositories remain excluded as in the boundary; that prevents claims about their retention, enforcement or validity. Task-oriented evaluators, specialized paper recovery, export internals and several workflow-authoring paths remain included but unresolved, not absent.

| Entry point or operation | Source path, all SRC-1 | Coverage and conclusion limit |
| --- | --- | --- |
| Prompt, print and SDK restoration | `cli/packages/coding-agent/src/core/sdk.ts`, `cli/packages/coding-agent/src/modes/print-mode.ts` | Supplied [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt); not independently retraced end to end. |
| Append, JSONL reload and active projection | `cli/packages/coding-agent/src/core/session-manager.ts`; `cli/packages/coding-agent/src/core/messages.ts` | Direct bounded reads; [MEM-OBJ-session-messages](#mem-obj-session-messages), [MEM-OBJ-session-metadata](#mem-obj-session-metadata), [MEM-RTE-session-retention](#mem-rte-session-retention). |
| Automatic and explicit compaction, extension replacement/cancel | `cli/packages/coding-agent/src/core/agent-session.ts`; `cli/packages/coding-agent/src/core/compaction/compaction.ts` | Runtime route plus direct preparation/summary reads; [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction), [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary). |
| Tree navigation and optional branch checkpoint | `cli/packages/coding-agent/src/core/agent-session.ts`; `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts` | Direct reads; [MEM-RTE-branch-navigation](#mem-rte-branch-navigation). Interactive and RPC bindings located by search, not all UI transitions inspected. |
| Bash exclusion and custom-message alternatives | `cli/packages/coding-agent/src/core/messages.ts`; `cli/packages/coding-agent/src/core/session-manager.ts` | Direct reads; [RT-RTE-user-bash](runtime.md#rt-rte-user-bash), [MEM-OBJ-custom-entry](#mem-obj-custom-entry). Hidden display is not context exclusion. |
| Skill discovery, role/visibility and explicit body reads | `cli/packages/coding-agent/src/core/skills.ts`; `cli/packages/coding-agent/src/core/agent-session.ts` | Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery); direct router procedure read adds model selection policy, not a deployed retrieval trace. |
| Managed graph import, overwrite, manual-unrouted alternative, rollback | `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs` | Direct metadata/validation/mutation reads; annotation on [RT-RTE-repo-import](runtime.md#rt-rte-repo-import). Router generator internals remain uninspected; exact evidence projection into each generated index is unresolved. |
| Official library install/update, conflicts, upstream removals, router toggle | `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`; `cli/packages/coding-agent/src/cli/repo-skills.ts` | Supplied [RT-RTE-library-update](runtime.md#rt-rte-library-update), supplemented by bounded searches. Exact deletion set and every state field not independently traced; no general revocation guarantee. |
| Verification and revision artifacts | `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md` | Direct bounded procedure read; [MEM-RTE-verification-revision](#mem-rte-verification-revision). Referenced evaluator helpers, refresh/extend internals and actual outcomes uninspected. |
| Global/ancestor instruction selection and delivery | `cli/packages/coding-agent/src/core/resource-loader.ts`; `cli/packages/coding-agent/src/core/system-prompt.ts` | Direct selector/assembler reads; [MEM-OBJ-project-context](#mem-obj-project-context). Complete trust gating across all loaders not established. |
| Dynamic-workflow registered tool, independent sessions, background return | `cli/packages/coding-agent/src/disco/dynamic-workflows/extension-factory.ts`; `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`; `cli/packages/coding-agent/src/disco/dynamic-workflows/task-panel.ts` | Direct bounded reads, resource-loader registration search; [MEM-RTE-workflow-context](#mem-rte-workflow-context). All agent-definition and prompt construction inputs not inspected. |
| Workflow disk save/load, result journal and checkpoint replay | `cli/packages/coding-agent/src/disco/dynamic-workflows/run-persistence.ts`; `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`; `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`; `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-paths.ts` | Direct bounded reads; [MEM-OBJ-workflow-journal](#mem-obj-workflow-journal), [MEM-RTE-workflow-resume](#mem-rte-workflow-resume). Full hash coverage, recovery and concurrency semantics unresolved. |
| Workflow diagnostic history and display | `cli/packages/coding-agent/src/disco/dynamic-workflows/agent-history.ts`; `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-ui.ts` | History transformer read completely, UI consumer located by search; [MEM-OBJ-agent-history](#mem-obj-agent-history). No route from these diagnostic snippets back into worker prompts established. |
| Saved workflow script adoption | `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-commands.ts`; `cli/packages/coding-agent/src/disco/dynamic-workflows/extension-factory.ts` | Direct save-command and named-loader wiring reads; script save/reuse exists. Storage validation, replacement control, provenance of initial authored scripts and nested workflow consumers remain uninspected; prevents a complete machinery-admission assessment. |
| Export to external agents | `cli/packages/coding-agent/src/disco/skills/import-repo-skills-to-agent/SKILL.md`; `cli/packages/coding-agent/src/disco/skills/import-repo-skills-to-agent/scripts/export_repo_skills_to_agent.mjs` | Procedure mentions located by search; helper not read. Export approval, subset withdrawal, backup recovery and exact external payload remain unresolved; external-host ingestion not established. |
| Specialized recovery/task graphs | `cli/packages/coding-agent/src/disco/skills/recover-paper-result/SKILL.md`; `skills/task-oriented/PassNet/skills/passnet-skill/SKILL.md`; `skills/task-oriented/FrontierCS`; `skills/task-oriented/PaperBench` | Search plus supplied boundary inventory only. Retained evaluation results and later task-specific consumers not traced; prevents collection-wide trace-learning or cleanup claims. |

## Core ideas

1. **Guidance and its admission evidence have different destinations.** The managed runtime tree contains instructions, references and scripts. Verification cases/reports belong outside it; runtime routing metadata is a minimal projection without rationale. The importer consumes a richer external classification handoff, while a later Researcher can see selected operating text without the complete verification record. This is not evidence-free admission, but neither is it automatic delivery of all reasons to the model. See [MEM-OBJ-repo-skills](#mem-obj-repo-skills), [MEM-RTE-verification-revision](#mem-rte-verification-revision) and the import annotation.
2. **Session storage is not the context window.** JSONL retains a tree; branch selection and the latest compaction determine active messages. Derived summaries are model-facing user content, whereas arbitrary extension details are not. A branch can be left without summarization, or its selected history can cross into the new branch as prose. See [MEM-RTE-session-retention](#mem-rte-session-retention), [MEM-RTE-branch-navigation](#mem-rte-branch-navigation).
3. **Two different operations called compaction have different consumers.** Session compaction generates behavior-shaping prose for later model requests. `compactAgentHistory` truncates diagnostics for workflow history/display; it is not evidence of semantic learning or automatic worker-context restoration. See [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary), [MEM-OBJ-agent-history](#mem-obj-agent-history).
4. **Workflow resume reuses results, not hidden worker conversations.** Workers get independent in-memory sessions; a journal can substitute an unchanged-prefix result on resume. That symbolic substitution can change control flow without a model rereading raw traces. A checkpoint reply can come from a human callback or a headless default; its label does not authenticate human approval. See [MEM-RTE-workflow-context](#mem-rte-workflow-context), [MEM-RTE-workflow-resume](#mem-rte-workflow-resume).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-repo-skills
Label: Managed repository skill graph

Natural-language `SKILL.md` bodies and reference prose live in filesystem trees, including installed `~/.disco/agent/skills/repositories/repo-skills/<skill-id>/`. Bundled scripts are separate symbolic executable parts, not prose interpreted by the model. Provenance and routing JSON are metadata parts with different consumers. Initial shipped graph authorship is not established by this inspection. Creator-directed construction and revisions are documented; filesystem import is implemented. Later consumers are role-eligible sessions, explicit skill expansion and tool-directed reads through [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery); code execution of every bundled script is not established. Guidance has instruction force only when interpreted; installation is not compliance.

Closest supplied records are [RT-RTE-repo-import](runtime.md#rt-rte-repo-import), [RT-RTE-library-update](runtime.md#rt-rte-library-update) and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance): this object is the retained payload, not those routes or authority relation. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`.

> The importer copies only the runtime tree,
> recursively validates its role and visibility contract,
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`

#### MEM-OBJ-routing-metadata
Label: Repository routing metadata and indexes

Symbolic runtime `references/repo-routing-metadata.json` stores identity, taxonomy hash, status and exact assignments; it is not an embedding. The richer external `classification.json` includes source identity/commit, content digest, assignment rationale and repository evidence. Natural-language area/family pages guide model selection; generated machine-readable indexes are the router's declared maintenance source of truth. These parts share repository lineage but not authority: importer validates metadata/handoff; model interprets pages; updater maintains indexes. Complete preservation of external evidence in generated indexes is uninspected. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`, `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`, `skills/repositories/repo-skills-router/SKILL.md`.

> Do not store evidence or
> rationale in that runtime JSON.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`

> The machine-readable files under `references/index/` are the generated routing source of truth.
> --- `skills/repositories/repo-skills-router/SKILL.md`

Closest supplied record: [RT-RTE-repo-import](runtime.md#rt-rte-repo-import); this declares its metadata payload, not another import route. Official manager source/digest state is a different symbolic bookkeeping part described on [RT-RTE-library-update](runtime.md#rt-rte-library-update), not evidence that routing judgments are correct.

#### MEM-OBJ-session-messages
Label: Session message entries

Filesystem JSONL stores raw user/assistant/tool-result messages and bash messages in an append-only tree; memory-only SessionManager is also supported. Message content is natural language or tool/media payload; role, tool-call structure, parent IDs and timestamps are symbolic structure, not semantic warrant. Inputs include user requests, model responses, executed tool results and extension contributions; external payload truth and media internals are not established. Later active model context is a branch/compaction projection, not a full event replay. Conversion can exclude a retained bash result by `excludeFromContext`. Closest supplied record [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) is a consuming route, not this retained object. SRC-1: `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/messages.ts`.

> Manages conversation sessions as append-only trees stored in JSONL files.
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

#### MEM-OBJ-session-metadata
Label: Session context selection metadata

Symbolic entry IDs/parents and selected leaf determine the branch. Model/thinking-change entries and assistant provider/model identity determine restored settings; they do not pin model parameters. Labels and session-info entries support navigation/display rather than contributing conversation text. JSONL and in-memory indexes store these parts. Default session directories are cwd-derived under the agent directory. Their authority is fixed code interpretation at reconstruction, not instruction prose. Different from [MEM-OBJ-session-messages](#mem-obj-session-messages); closest supplied [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) consumes the reconstructed context. SRC-1: `cli/packages/coding-agent/src/core/session-manager.ts`.

> const { thinkingLevel, model } = getSessionContextSettings(path);
> const messages = buildContextEntries(entries, leafId, byId).flatMap(sessionEntryToContextMessages);
> return { messages, thinkingLevel, model };
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

#### MEM-OBJ-compaction-summary
Label: Compaction summary and retained boundary

Natural-language `summary` and symbolic `firstKeptEntryId`, token count, usage and optional `details` live in compaction entries in the same session storage. Default generation transforms older messages and possibly an existing summary; split turns get a separately generated prefix summary merged with history. File lists are derived from tool-call records and appended to summary text, with structured lists in details. Extension-supplied content and opaque details are alternatives, not necessarily the same schema or provenance. Only summary text and its message wrapper reach the ordinary model conversion; details are not automatically injected. No fidelity or preservation of all reasons is established. The default requested format includes key decisions and brief rationale, so absence of all rationale would also be unsupported. SRC-1: `cli/packages/coding-agent/src/core/compaction/compaction.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/messages.ts`.

> summary += formatFileOperations(readFiles, modifiedFiles);
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

Closest supplied [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction) is the transformation route, not the retained checkpoint. Its metadata does not confer independent truth authority; the later model receives a user-role summary.

#### MEM-OBJ-custom-entry
Label: Extension state and injected message parts

`CustomEntry.data` and summary `details` can hold arbitrary extension-specific payloads in JSONL/in-memory state. Their form and initial lineage are opaque beyond the symbolic envelope. A documented extension reload role may scan custom entries to reconstruct internal state; a particular deployed reader was not traced. Plain custom entries do not enter normal model context. `CustomMessageEntry.content` is a distinct model-facing part: text/media is converted to user content, while details remain metadata. `display` controls TUI visibility, not whether the content reaches the model. SRC-1: `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/messages.ts`.

> Does NOT participate in LLM context (ignored by buildSessionContext).
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

> * display controls TUI rendering:
> * - false: hidden entirely
> * - true: rendered with distinct styling (different from user messages)
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

Closest supplied [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) mentions extension messages; these are the distinct retained payload and state parts, not a second prompt route. No automatic learning authority is assigned to opaque data with an unspecified reader.

#### MEM-OBJ-project-context
Label: Project instruction files

Natural-language files on disk, selected from the agent directory and cwd ancestors, become `<project_instructions>` in system context. Selector canonicalization avoids duplicates and a shadowed linked-worktree context file. This is code-owned selection by directory ancestry, not semantic query or trace-derived summarization. Authors, content approval and editing history are unresolved; load capability does not establish that the runtime writes these files. Static input is not read-back; edited retained instructions can reach a later reload, but no automatic trace-to-edit path is established. Closest supplied [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) covers the assembled request, not these files. SRC-1: `cli/packages/coding-agent/src/core/resource-loader.ts`, `cli/packages/coding-agent/src/core/system-prompt.ts`.

> result += `<project_instructions path="${filePath}">\n${content}\n</project_instructions>\n\n`;
> --- `cli/packages/coding-agent/src/core/system-prompt.ts`

#### MEM-OBJ-workflow-journal
Label: Workflow run result journal

Symbolic `{index, hash, result}` entries are persisted with the actual script, args, limits, status, recovery lineage, agent snapshots and final result. Results are opaque arbitrary JSON values or natural-language outputs depending on the worker; a readable preview is not the full value. Files live under cwd-namespaced `~/.disco/workflows/projects/<key>/runs`, with `.tmp` and `.bak` companions. The manager writes after journal callbacks; load tries primary and backup. Hash/index matches permit the workflow interpreter to return the cached result instead of invoking a worker. This gives retained output control-flow authority independent of a model reading prose. Initial scripts/args may be caller supplied; live result lineage includes model/tool work, while checkpoint entries can hold human responses or software defaults. SRC-1: `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-paths.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/run-persistence.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`.

> managed.journal = managed.journal.filter((e) => e.index !== entry.index);
> managed.journal.push(entry);
> this.persistRun(managed);
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`

No counterpart after comparison with supplied routes: [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) is a foreground session route, not workflow replay storage.

#### MEM-OBJ-agent-history
Label: Compact agent diagnostic history

Derived display/diagnostic entries contain user/assistant text, tool-call argument JSON, tool-result text and errors, not the complete worker conversation or opaque result. The default transformer keeps at most 40 recent entries, 2,000 characters per entry and 20,000 total, truncating from text beginnings and favoring newest entries. Agent callbacks feed history to manager snapshots; persisted agent state carries it, and workflow UI can render it. These are trace-fed writes, but the inspected consumer is diagnostic display, not automatic knowledge revision or worker replay. Storage is JSON within persisted run snapshots; natural-language snippets and symbolic role/kind/tool fields have distinct presentation roles. SRC-1: `cli/packages/coding-agent/src/disco/dynamic-workflows/agent-history.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-ui.ts`.

> const DEFAULT_MAX_ENTRIES = 40;
> const DEFAULT_MAX_TEXT_CHARS = 2000;
> const DEFAULT_MAX_TOTAL_CHARS = 20000;
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent-history.ts`

> body.push(...wrap(`${historyLabel(entry)}: ${entry.text}`, width));
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-ui.ts`

No supplied counterpart; distinct from the result cache in [MEM-OBJ-workflow-journal](#mem-obj-workflow-journal).

### Routes

#### MEM-RTE-session-retention
Label: Session retention and reload

Part of: [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt)

This isolates the foreground route's persistence/reconstruction segment. Message-end handling supplies entries; SessionManager appends to its current tree and SDK restoration consumes the projection. Physical disk persistence is conditional: `_persist` exits for memory-only sessions, and a fresh unflushed session defers file creation until an assistant entry exists. Thus ordinary append wiring is not a guarantee every user input is already durable. SRC-1: `cli/packages/coding-agent/src/core/session-manager.ts`; supplied message-end/SDK evidence in the parent route.

> if (!this.persist || !this.sessionFile) return;
> --- `cli/packages/coding-agent/src/core/session-manager.ts:1043-1043`

- Immediate return: append ID and updated leaf; later caller obtains reconstructed messages/settings.
- Later read-back: branch-selected message entries and derived summaries reach later prompts and reopened sessions; older branches remain outside the selected projection.
- Delegated visibility: provider receives converted context; arbitrary custom data and display-only metadata are not universally forwarded.
- Selection predicate: leaf ancestry, latest compaction and first-kept marker, then message conversion; bash exclusion can suppress retained output.
- Invalidation or expiry: navigation and newer compaction change active projection without deleting old tree content; disk deletion/retention policies not exhaustively inspected.
- Activation or effect: reconstruction assigns model context; semantic influence and improved future capacity remain unobserved.
- Evidence limits: source implementation plus supplied foreground wiring, not a crash-recovery experiment or provider-retention account.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Raw acquisition is event-driven software admission, not per-entry human review. User input authorship is distinct from model/tool authorship and from the runtime's physical append. No answer oracle is used for ordinary persistence.

#### MEM-RTE-branch-navigation
Label: Branch navigation checkpoint

AgentSession owns tree navigation. A caller chooses target and whether to summarize the abandoned path. `session_before_tree` may cancel, supply a summary, or modify instructions/label; otherwise a runtime model summarizes when requested. The summary is attached at the destination position, not left only on the abandoned branch. This is an alternative to compaction, not a duplicate of [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction). SRC-1: `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/messages.ts`.

> // Summary is attached at the navigation target position (newLeafId), not the old branch
> --- `cli/packages/coding-agent/src/core/agent-session.ts`

- Immediate return: cancellation/abort or selected branch and optional summary entry; selected user text can return to the editor.
- Later read-back: stored branch summary is converted to a user-role message in later destination-branch requests; without summary, abandoned history is not injected by this mechanism.
- Delegated visibility: summarizer sees budget-selected entries; foreground model sees summary text, not summary details or the complete abandoned path.
- Selection predicate: caller target and summarize option, common-ancestor path, then newest-first message selection under model window minus reserved tokens. An over-budget summary entry can still fit via a special allowance below 90% of budget.
- Invalidation or expiry: subsequent branch selection/compaction changes active context; original entries remain reachable through the tree rather than being physically withdrawn.
- Activation or effect: code rebuilds agent messages at the destination; observed reliance or faithful preservation is uninspected.
- Evidence limits: UI and RPC binding searches identify supported callers; all caller option defaults and branch-selection preparation internals were not exhaustively read.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Default branch summarization uses reserveTokens (fallback 16,384) and a 2,048-token response cap. It requests goals, constraints, progress, decisions/rationale and next steps; file-operation tracking can incorporate older summary details even when those entries do not fit the message budget. The model proposes summary text; code admits it after error/abort checks and extensions can veto or replace. No expected-answer oracle checks fidelity. Human initiation of navigation is not per-summary approval. Summary details may be opaque on the extension alternative. This is working-context removal with a prose return, not an isolated subagent frame.

#### MEM-RTE-verification-revision
Label: Verification-driven skill revision

This procedure precedes but is distinct from [RT-RTE-repo-import](runtime.md#rt-rte-repo-import): it concerns constructing and revising the runtime graph, not admitting a directory to the managed collection. Creator/verification guidance calls for assertion-backed synthetic and native cases, content self-refine, backend-aware runtime checks and saved reports outside the runtime tree. Failures can guide edits before final static checks and import readiness. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`.

> Use failures or gaps to revise the runtime skill before
> static verification when the generated skill is wrong or thin.
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/SKILL.md`

- Immediate return: requested verified draft, coverage/test reports, routing handoff and readiness report.
- Later read-back: revised runtime graph can reach a later Researcher through managed import and skill delivery; reports remain construction/review evidence, not automatically injected operating context.
- Delegated visibility: verifier/Creator receives native results and assertion-backed cases; the Researcher receives selected installed content, not necessarily the check-only artifacts.
- Selection predicate: confirmed scope, capability/backend plan and representative safe native cases plus generated difficult cases; full executable selector implementation uninspected.
- Invalidation or expiry: instructed revisions replace draft guidance; refresh/extend and exact report retention/deletion policies remain uninspected.
- Activation or effect: instructions request evidence-responsive curation and gate auto-import on unresolved failures; actual revisions and causal improvement are not observed.
- Evidence limits: doctrine/design only for this revision chain; no cases run and referenced evaluator implementations not audited.
- design conclusion status: claimed
- operation conclusion status: uninspected

Proposer/editor: instructed agent; requested vetoes include required-backend blocks and unresolved high/critical failures. Users may authorize auto-import up front; partial backend evidence instead requires a new informed manual decision. This is not universal per-content human approval. Assertions provide specified checks but their actual expected values, providers and correctness were not inspected. It is an open construction request with bounded chosen verification cases, not an established scientific answer oracle. What persists differs: revised operating guidance enters the runtime tree; criticisms/results reside in external cases/reports. A later model is not shown reading the reasons for every edit. No theory-builder or successful learning conclusion follows merely from the self-refine label.

#### MEM-RTE-workflow-context
Label: Isolated workflow worker and return

Dynamic-workflow extension registers `workflow`; resource-loader includes the default extension when configured. Each live worker creates an in-memory SessionManager independent of the foreground session, after stripping caller-supplied resourceLoader/sessionManager overrides. Prompt construction, shared settings, selected model and tools supply the worker; the parent conversation is not copied wholesale by the inspected constructor. The worker returns last assistant text or a structured result, with compact history emitted separately. Closest supplied [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt) describes session execution, not the orchestration/return route. SRC-1: `cli/packages/coding-agent/src/core/resource-loader.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/extension-factory.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/task-panel.ts`.

> sessionManager: SessionManager.inMemory(runCwd, { discoMode: this.discoMode }),
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`

- Immediate return: live worker text or validated structured result to workflow script; synchronous workflow result or background run ID to the foreground caller.
- Later read-back: journaled results support resumed interpretation; background completion injects a selected report into a later foreground turn, retained through custom-message machinery.
- Delegated visibility: worker sees its built prompt and independently loaded resources; parent receives return value or report projection, while compact diagnostics go to history callbacks.
- Selection predicate: workflow script assigns prompts, model/agent options and result composition; automatic completion selector prefers verdict/report/summary string fields, then bare string, else JSON truncated after 400 characters.
- Invalidation or expiry: worker disposal ends its context; abort can terminate it; retained journal/history and foreground result message survive separately when persistence succeeds.
- Activation or effect: registered completion sends a custom workflow-result with triggerTurn and followUp delivery; real activation is unobserved and send failures are swallowed.
- Evidence limits: full role-prompt/agent-definition/resource construction and every failure/recovery return not inspected; this is context isolation, not proof of filesystem isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> { customType: "workflow-result", content, display: true },
> { triggerTurn: true, deliverAs: "followUp" },
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/task-panel.ts`

The stack-frame analogy fits separate message state with a bounded return, but breaks at shared filesystem/resources and independently retained journal/history. A result is passed by value; pointers in returned prose do not automatically reload files. Background completion is a push selector: completion/incomplete events supply the run, code selects report content and delivery starts/queues the next model turn. It is not an unsolicited semantic search through the whole store. Partial results include missing-ID recovery guidance rather than a blanket success assertion.

#### MEM-RTE-workflow-resume
Label: Workflow journal replay

Manager resume loads a run, rejects running/completed/aborted cases as applicable, obtains a lease, restores script/args/limits and builds an index map for interpreter replay. Live results replace entries with the same call index through callbacks and trigger persistence. Checkpoint replies use the same journal but can originate in `confirm`, a headless default, or rejection when headless policy is abort. This recovery route is distinct from all supplied session routes. SRC-1: `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/run-persistence.ts`.

> if (hashMatches && !cachedEmptyOutput && callIndex < state.firstMiss) {
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

> reply = checkpointOptions.default ?? true;
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

- Immediate return: resume boolean and background execution, or cached per-call result during interpretation.
- Later read-back: persisted matching-prefix outputs and checkpoint replies substitute for later worker/callback invocations.
- Delegated visibility: interpreter receives full cached value; later workers receive only what the script uses in their prompts, not automatically journal rationale or diagnostic history.
- Selection predicate: run ID, resumable status and lease, then deterministic call index/hash and first-miss boundary; empty text agent result causes a live rerun.
- Invalidation or expiry: changed/missing call ends the replayable prefix; later calls run live. Delete operation attempts primary/sidecar removal; precise UI deletion authorization and every environment dependency in hashes are unresolved.
- Activation or effect: cached value returns directly without worker inference; this establishes symbolic control-flow reuse, not measured benefit or environmental freshness.
- Evidence limits: source wiring only; full hash dependencies, concurrent edits, filesystem crash guarantees and all recovery-round branches uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Software admits live outputs into the journal; no human per-output review is shown. A checkpoint callback can request human judgment, but default `true` proves that the label alone cannot establish it. Hash equality is an identity/cache check, not an answer oracle. Mode is pause/resume maintenance. The code can reject missing/nonresumable state or rerun from the first miss; filesystem persistence uses tmp-to-primary rename and best-effort backup, not a demonstrated crash-proof transaction. Retention of outputs affects future execution without changing model weights or necessarily revising an explanatory claim.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction)

The default selector walks newest to oldest accumulating estimated tokens, keeps approximately `keepRecentTokens`, and chooses legal user/assistant boundaries rather than cutting at tool results. Older history is preferentially summarized, not exclusively tool output or skill text. Preparation includes previous summary, older messages and optional split-turn prefix; generation merges history/prefix summaries and appends file lists. New compaction plus kept tail reaches later requests; original JSONL entries remain available outside active context. SRC-1: `cli/packages/coding-agent/src/core/compaction/compaction.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`.

> * Algorithm: Walk backwards from newest, accumulating estimated message sizes.
> * Stop when we've accumulated >= keepRecentTokens. Cut at that point.
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

The default format requests brief decision rationale. Repeated compaction passes previous summary for updating, but semantic fidelity is uninspected. Extension-produced summary/details need not follow that format; default file-tracking metadata does not establish semantics of opaque extension payloads. Summary becomes user-role content through `convertToLlm`, not new system policy. [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary) names its retained parts. This extends the runtime's explicitly uninspected preparation internals; it does not contradict its supplied route.

#### On [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery)

The router's natural-language selector uses task capability, workflow, data/model format and runtime intent, then area/family comparisons and selected root/sub-skills. Its stated budget is one or two likely area pages and the smallest useful repository set, not a numerical token cap or embedding search. A foreground model's tool reads are demand-driven; catalog loading is a separate automatic resource-selection operation. SRC-1: `skills/repositories/repo-skills-router/SKILL.md`.

> Read only the one or two most likely area pages below.
> --- `skills/repositories/repo-skills-router/SKILL.md`

Raw installed files remain reachable after discovery filters; role/visibility are not filesystem confinement. Router disable changes automatic selection availability, not explicit invocation or deletion. Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) already establishes hidden explicit invocation; CLI help additionally distinguishes router toggle semantics. SRC-1: `cli/packages/coding-agent/src/cli/repo-skills.ts`.

#### On [RT-RTE-repo-import](runtime.md#rt-rte-repo-import)

Direct source inspection adds an alternative admission path: `--manual-unrouted` permits explicit unclassified import without an external routing handoff, while runtime metadata remains required. Normal handoffs are digest-bound to the portable skill tree and require assignment rationale/evidence; unknown runtime metadata keys reject. Therefore not every admitted graph has classified routing or a preserved complete critique. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`.

> if (manualUnrouted && data.routing_status !== "unclassified") throw new ImportError("--manual-unrouted requires runtime metadata with routing_status unclassified");
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`

Runtime tree and router/index backup/restore are separate from the construction reports. Import catch restores prior affected live paths when possible, and transaction cleanup removes staging/backups unless rollback failed. This preserves recovery artifacts on failed restoration, not a permanent history of every rejected candidate. No universal withdrawal of already loaded model context follows from filesystem overwrite or rollback. The updater's exact retained evidence projection remains unresolved.

#### On [RT-RTE-library-update](runtime.md#rt-rte-library-update)

The durable management state is symbolic source/digest bookkeeping with the library updater/status checker as consumer, not model-facing scientific knowledge. Conflict searches distinguish locally modified managed content and upstream removal. Router visibility is normalized separately from graph content digests and can be preserved across updates. This is maintenance relative to a source inventory, not automatic trace-based skill improvement. Initial snapshot authenticity and all helper consumers remain uninspected as the supplied record states. SRC-1: `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`.

## Write side

The write mechanisms differ in admission, not just authorship:

| Mechanism | Producer/editor and physical write | Admission, rejection and retained result |
| --- | --- | --- |
| Managed graph construction/revision | Instructed Creator/verification agent; source-native filesystem tools | Procedure requests test/review-based edits; reports/cases remain outside runtime graph. Backend failures block automatic import by policy; actual compliance unobserved. [MEM-RTE-verification-revision](#mem-rte-verification-revision). |
| Repository import | Caller supplies directory/flags; importer copies, validates, swaps and updates router | Structural/license/routing checks and overwrite flag; manual-unrouted alternative; rollback attempts, cleanup and failure artifact preservation. Separate human approval is not authenticated by a flag. [RT-RTE-repo-import](runtime.md#rt-rte-repo-import) annotation. |
| Official library install/update | Snapshot/inventory plus manager filesystem swaps | Conflict/force, digest and state checks; no-op branches; source/digest bookkeeping affects later updates. [RT-RTE-library-update](runtime.md#rt-rte-library-update). |
| Session acquisition | Users/models/tools/extensions author different inputs; event subscriber and SessionManager append | Software append, conditional flush, no per-entry truth or human gate. Raw traces alone are not learned guidance. [MEM-RTE-session-retention](#mem-rte-session-retention). |
| Session compaction / branch checkpoint | Runtime summarizer or extension supplies prose; SessionManager stores checkpoint | Code triggers/caller target, extension cancel/replace, error/abort checks; retained summary affects later requests without content approval. [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction), [MEM-RTE-branch-navigation](#mem-rte-branch-navigation). |
| Workflow journal/history | Worker results, checkpoint callback/defaults and diagnostic transformer; manager saves JSON | Latest per-index output replaces cache entry; matching-prefix code decides reuse. Diagnostics have a different display consumer. [MEM-RTE-workflow-resume](#mem-rte-workflow-resume), [MEM-OBJ-agent-history](#mem-obj-agent-history). |
| Project instructions, arbitrary extension payloads and saved scripts | Initial author/approval unresolved; loader reads do not establish writes | Known subsequent selection/injection is retained without inventing content-level human control. Saved-script command exists but full admission/storage checks uninspected. [MEM-OBJ-project-context](#mem-obj-project-context), [MEM-OBJ-custom-entry](#mem-obj-custom-entry), coverage table. |

The qualifying automatic raw-to-derived-to-later-model chain is session history → generated compaction/branch summary → later model invocation. It can preserve reasons by requested format, but only generated prose reaches that reader and no semantic preservation oracle was found on the inspected route. Workflow history truncation is also automatic and trace-fed, but its established consumer is display. Journal replay retains outcome values and substitutes them in resumed execution, not a newly formulated rule. Verification doctrine asks results to shape revisions, but that trace-to-guidance update is not shown exercised. The distinctions prevent treating all persistence or all transformations as one learning mechanism.

Rejection and withdrawal have different horizons. Failed import can restore filesystem paths; router disable only suppresses automatic discoverability; branch/compaction omits old entries from active context without erasing logs; workflow first-miss invalidates cache reuse and disk delete attempts remove run files. None automatically retracts prose already sent to a provider. Specialized export withdrawal and task-evaluation cleanup remain uninspected. Sources and supporting records are the table above and [MEM-RTE-workflow-resume](#mem-rte-workflow-resume).

## Read-back

- **Installed guidance:** loader/catalog selection, explicit `/skill:` and model-directed router/file reads are distinct steps. A selected path is a pointer until a read/expansion supplies its content. Static shipped bodies are ordinary resources; installed/revised content becomes read-back when a later session receives it. Instructions have natural-language force, not proof of compliance. [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) and annotation.
- **Session retention:** current selected branch and latest summary/tail are automatically projected when building later context; metadata and excluded bash output do not all become text. This selector is based on tree/entry state, not task semantic similarity. Compaction removes older accumulated content while leaving a summary and verbatim tail. [MEM-RTE-session-retention](#mem-rte-session-retention), [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction).
- **Branch alternatives:** navigation can carry no abandoned context, a default generated summary, or an extension substitute; arbitrary details are not the readable summary. Old path storage remains reachable by selecting another branch rather than automatic resurrection. [MEM-RTE-branch-navigation](#mem-rte-branch-navigation).
- **Workflow contexts:** independent worker sessions resemble separate frames; only chosen output/history channels cross back. Background completion pushes a report projection with automatic follow-up turn; replay instead requests a run/index and returns full cached value to symbolic interpretation. These are neither the same delivery direction nor the same payload. [MEM-RTE-workflow-context](#mem-rte-workflow-context), [MEM-RTE-workflow-resume](#mem-rte-workflow-resume).
- **Unspecified readers:** extension custom-state scanning is documented as an afforded role, not a traced deployed model consumer. Saved scripts have a named loader/command path, but full replacement and later execution semantics remain unresolved. External agents have an export affordance, not established ingestion. These limits prevent promoting storage APIs or display snippets into universal knowledge-retrieval routes. [MEM-OBJ-custom-entry](#mem-obj-custom-entry), coverage table.

## Integration issues

1. **Runtime coverage extension, not a contradicted fact:** [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction) leaves partition/prompt internals uninspected. The annotation and [MEM-OBJ-compaction-summary](#mem-obj-compaction-summary) now establish recent-tail selection, split-turn alternatives, rationale request and details/text separation. Reconciliation should retain the narrower runtime inspection limit as historical scope, not infer that these internals remain entirely unknown across the set.
2. **Import qualification:** [RT-RTE-repo-import](runtime.md#rt-rte-repo-import) explicitly left manual-unrouted alternatives uninspected. Its annotation establishes that route and blocks a universal external-classification-handoff claim. [MEM-OBJ-routing-metadata](#mem-obj-routing-metadata) separates minimal runtime metadata from richer input rationale. Exact updater/index evidence preservation remains unresolved at `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/update_repo_skills_router.mjs` (SRC-1); prevents claiming every later reader receives admission reasons.
3. **New route parts versus duplicates:** [MEM-RTE-session-retention](#mem-rte-session-retention) is explicitly part of [RT-RTE-session-prompt](runtime.md#rt-rte-session-prompt). Other new objects are payloads/metadata, not duplicate route referents. [MEM-RTE-branch-navigation](#mem-rte-branch-navigation) is a separate checkpoint operation, not synonymous with compaction; workflow routes are separate orchestration and replay. No unresolved possible-duplicate identity remains after these distinctions.
4. **Additional shipped orchestration:** [MEM-RTE-workflow-context](#mem-rte-workflow-context), [MEM-RTE-workflow-resume](#mem-rte-workflow-resume) add independent sessions and completion/replay consumers beyond the runtime's selected routes. SRC-1 dynamic-workflow paths in those records support wiring, but full worker prompt composition, hash coverage, saved-script replacement, recovery rounds and nested workflow inputs remain uninspected. Prevents complete delegation isolation, environmental freshness or universal machinery-admission conclusions.
5. **Remaining partial loop:** export helper, refresh/extend internals, paper recovery and task-oriented evaluator/result-consumer paths named in the coverage table remain unresolved. Their existence is not evidence of an automatic log-to-library-learning cycle, nor evidence that one is absent. This limits system-wide learning, trace provenance, test-oracle and withdrawal claims. Initial project-file authorship, opaque extension payload lineage and external provider memory likewise remain local unknowns; known selection/transformation positives are retained.
6. **Checks versus observed effects:** no operation or experiment supports reliable compliance, summary fidelity, improved capacity or successful self-improvement. The result-cache substitution and summary delivery mechanisms are implemented; their successful effects are not inferred from naming or installation. This is an evidence-layer limit, not a correction to supported implementation findings.

## Limitations and checks

The source revision was checked with Git; direct reads/searches stayed within SRC-1. The supplied invocation, types, collection, worker rules and record contract were read, including continued ranges. Runtime observations remain supplied findings where marked; direct source inspection adds only implementation and doctrine/design evidence. No new source was registered, target executed, provider called or example treated as an experiment. Available uninspected files are coverage limits, not access gaps or evidenced absences. Counterexample checks included explicit hidden-skill invocation, manual-unrouted import, memory-only/deferred disk persistence, extension replacement, branch navigation without summary, truncated workflow reports, and headless checkpoint defaults.

Deterministic validation: passed with the invocation's prepared `commonplace-run validate-output` command after quotation-attribution repairs. Form and quotation occurrence checks do not certify analytical completeness or successful operation.
