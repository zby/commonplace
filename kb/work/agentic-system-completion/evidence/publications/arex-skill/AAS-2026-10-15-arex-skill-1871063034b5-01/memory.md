---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AREX-Skill memory: installed guidance, session summaries, workflow replay and saved orchestration within the partial-loop boundary."
run-id: AAS-2026-10-15-arex-skill-1871063034b5-01
source-identity: https://github.com/VectorSpaceLab/AREX-Skill
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill memory report

## Boundary and evidence

The subject is DisCo's retained operating context and its later consumers, not just the published Markdown library. The frozen boundary and source identity are those of [boundary](boundary.md), SRC-1 at ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6. Its **complete artifact, partial loop** classification remains appropriate. Included memory surfaces are installed skill graphs and their discovery metadata, persisted session branches and summaries, workflow result journals, compact diagnostic histories, saved executable workflows, and filesystem instruction loading. Static shipped skills count as initial context, not use-derived read-back. Imported or updated content can become read-back in later sessions. Provider weights remain outside the captured implementation; [RT-CMP-model-runtime](runtime.md#rt-cmp-model-runtime) supplies their separate uncertainty account.

Direct reads added implementation coverage of `cli/packages/coding-agent/src/core/compaction/compaction.ts`, `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts`, `cli/packages/coding-agent/src/core/compaction/utils.ts`, selected ranges of `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/messages.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/resource-loader.ts`, `cli/packages/coding-agent/src/core/system-prompt.ts`, and the workflow and collection paths below. Direct doctrine inspection includes `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`. All are SRC-1. Runtime findings supply the importer, foreground persistence, role filtering, explicit skill expansion and child-session construction accounts where not independently reread. No runtime trace, example artifact, test, provider call or experiment was executed or treated as observed operation.

### Coverage inventory

Paths in this table are commit-relative SRC-1 anchors. “Supplied” means the finding comes from runtime rather than a new direct file read. Available but uninspected paths are not access failures.

| Operation or part | Source path and inspection | Covering records or local limit |
| --- | --- | --- |
| Ordinary CLI/session persistence and SDK reconstruction | Supplied: `cli/packages/coding-agent/src/main.ts`, `cli/packages/coding-agent/src/core/sdk.ts`; direct selected reconstruction in `cli/packages/coding-agent/src/core/session-manager.ts` | [RT-RTE-foreground-task](runtime.md#rt-rte-foreground-task), [RT-OBJ-session-context](runtime.md#rt-obj-session-context); annotations below |
| Registry versus full skill body; explicit versus semantic selection | Supplied: `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `skills/repositories/repo-skills-router/SKILL.md` | [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry); no body-selection accuracy conclusion |
| Creator drafting, verification and generic installation | Direct doctrine: `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`; supplied importer inspection: `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs` | [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission), [RT-OBJ-operating-graph](runtime.md#rt-obj-operating-graph); semantic quality is not a validator result |
| Collection install/update/status/router disable | Direct CLI and selected manager ranges: `cli/packages/coding-agent/src/cli/repo-skills.ts`, `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`; dispatch symbol checked in `cli/packages/coding-agent/src/main.ts` | [RT-RTE-library-update](runtime.md#rt-rte-library-update), [MEM-OBJ-library-state](#mem-obj-library-state); router disable is not deletion |
| Manual/automatic compaction, split-turn and incremental summary | Direct selected ranges: `cli/packages/coding-agent/src/core/compaction/compaction.ts`, `cli/packages/coding-agent/src/core/compaction/utils.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`; supplied trigger/hook account | [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction), [MEM-OBJ-compaction](#mem-obj-compaction) |
| Branch navigation, optional summary, extension cancellation/replacement | Direct: `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts` | [MEM-RTE-branch-summary](#mem-rte-branch-summary), [MEM-OBJ-branch-summary](#mem-obj-branch-summary) |
| Child context separation and structured result | Supplied: `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`; direct history and workflow consumer paths | [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent), [MEM-OBJ-agent-history](#mem-obj-agent-history) |
| Workflow journal, checkpoints, resume and cleanup | Direct selected ranges: `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/run-persistence.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-paths.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-commands.ts` | [MEM-RTE-journal-replay](#mem-rte-journal-replay), [MEM-OBJ-journal](#mem-obj-journal) |
| Reusable workflow save, load, command registration and named nesting | Direct: `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-saved.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/saved-commands.ts`, selected `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-ui.ts` and command ranges; registration/tool wiring symbol checked in `cli/packages/coding-agent/src/disco/dynamic-workflows/extension-factory.ts` and `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-tool.ts` | [MEM-RTE-saved-workflow](#mem-rte-saved-workflow), [MEM-OBJ-saved-workflow](#mem-obj-saved-workflow) |
| Project/global instructions and prompt overrides | Direct selected ranges: `cli/packages/coding-agent/src/core/resource-loader.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/system-prompt.ts`, `cli/packages/coding-agent/src/core/messages.ts`; supplied extension/trust account | [MEM-OBJ-context-files](#mem-obj-context-files); arbitrary extensions' actual transformations uninspected |
| Specialized repository/meta import, paper recovery/verification and cross-agent export | Supplied partial inventory; symbol search only in `cli/packages/coding-agent/src/disco/skills/import-repo-skills-to-agent/scripts/export_repo_skills_to_agent.mjs` | Separate transactional paths remain untraced; no complete admission, recovery or external-host consumption conclusion. Do not extend generic-import guarantees to these paths. |
| Individual repository graphs, task-oriented FrontierCS/PaperBench/PassNet, examples and release/home-reset scripts | Included, not substantively inspected beyond supplied boundary inventory | Content lineage, evaluator-to-retained-skill changes, destructive cleanup and deployed efficacy remain uninspected. No system-wide trace-learning or completeness claim. |

External destination agents, providers, live installed files and later upstream revisions are not frozen. Their actual context, compliance and parameter behavior cannot be established here. Excluding those deployments does not exclude the shipped exporters or drivers from the inventory.

## Core ideas

1. **The library is a retained instruction surface, but discovery is not ingestion of every body.** Registry descriptions and paths support model-selected reads; explicit commands inject a body. The router's progressively narrowed reads are prompt policy. Installing a graph creates a future delivery opportunity, not evidence that the model selected it or changed behavior. See [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) and [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance).
2. **Session memory substitutes a derived checkpoint for selected history.** The stored event tree is richer than the reconstructed model window. Compaction, split-turn summaries and branch summaries all change what later invocations see; their serialization can truncate original tool evidence. Requested retention of decisions and reasons is not a semantic preservation guarantee. See [MEM-OBJ-compaction](#mem-obj-compaction), [MEM-RTE-branch-summary](#mem-rte-branch-summary).
3. **Replay and reusable orchestration are distinct retained products.** A journal reuses a prior result without rerunning the child; a saved workflow reruns retained JavaScript. Diagnostic history is neither of those. These have different consumers, invalidation and behavioral force. See [MEM-RTE-journal-replay](#mem-rte-journal-replay), [MEM-RTE-saved-workflow](#mem-rte-saved-workflow), [MEM-OBJ-agent-history](#mem-obj-agent-history).
4. **Access metadata is not scientific warrant.** Commit/digest state controls conflicts and drift; role metadata controls eligible discovery; summary metadata tracks file operations. None certifies the truth of guidance or the adequacy of the evidence omitted from a later window. See [MEM-OBJ-library-state](#mem-obj-library-state), [RT-CLM-mode-contract](runtime.md#rt-clm-mode-contract).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-compaction
Label: Compaction checkpoint

Part of: [RT-OBJ-session-context](runtime.md#rt-obj-session-context)

Source-native identity: `CompactionEntry` summary, first-kept boundary and optional details/usage. Storage: retained session entry, or in-memory session store. Form: natural-language summary; symbolic boundary, usage and file-list metadata. This is a derived part of the supplied session container, not a second declaration of that container. Evidence: SRC-1, `cli/packages/coding-agent/src/core/compaction/compaction.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`.

Lineage: older branch messages, previous compaction summary, and optionally a split-turn prefix produce one merged checkpoint. Original input mixes user messages, assistant text/thinking/tool calls and tool-result text; this is trace-fed derivation, not merely raw logging. Before summarization, conversion and serialization lose nontext detail and cap each textual tool result at 2,000 characters. Default recent-tail/reserve settings are 20,000/16,384 tokens; the cut walks backwards through estimated sizes and avoids cutting at a tool result. The normal summary output allowance is min(0.8 × reserve, positive model maxTokens). These are selection/output budgets, not exact end-to-end context bounds.

> const TOOL_RESULT_MAX_CHARS = 2000;
> --- `cli/packages/coding-agent/src/core/compaction/utils.ts`

> previousSummary = prevCompaction.summary;
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

> summary = `${historyText}\n\n---\n\n**Turn Context (split turn):**\n\n${turnPrefixResult.text}`;
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

Curation/admission: code selects history; current model writes a summary under continuation-checkpoint instructions; optional custom instructions and extension replacement affect content. The host admits the completed result without a semantic equivalence test. The prompt requests decisions with brief rationale and permits removal of no-longer-relevant information. Thus reasons are requested in retained prose, not guaranteed complete. File operation lists are appended to readable text and also retained as metadata. A later compactor reads previous summary and file-tracking details; a later foreground model receives summary text plus kept tail, not the whole original history or arbitrary details. [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction) supplies admission cancellation, persistence and activation limits.

> ## Key Decisions
> - **[Decision]**: [Brief rationale] (preserve all previous, add new)
> --- `cli/packages/coding-agent/src/core/compaction/compaction.ts`

#### MEM-OBJ-branch-summary
Label: Branch exploration summary

Part of: [RT-OBJ-session-context](runtime.md#rt-obj-session-context)

Source-native identity: `BranchSummaryEntry` attached at the navigation destination. Storage: session event tree. Form: natural-language exploration summary and symbolic origin/details. Lineage: abandoned branch entries up to their common ancestor, selected under a model-window-minus-reserve budget, or an extension-provided replacement. It differs from [MEM-OBJ-compaction](#mem-obj-compaction): the trigger is navigation and the result is attached to another branch, not a first-kept compaction boundary. SRC-1, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts`.

> const tokenBudget = contextWindow - reserveTokens;
> --- `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts`

> const requestOptions: SimpleStreamOptions = { apiKey, headers, env, signal, maxTokens: 2048 };
> --- `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts`

The selector favors recent branch material and can include an over-budget summary near the boundary; serialization again truncates tool-result text. The model prompt requests goal, constraints, progress, blockers, decisions/rationale and next steps. It receives serialized selected text, not every abandoned event. File lists are appended; extension details may remain opaque to this analysis. Later reconstruction emits readable summary as model-facing context; reasons have only the authority of interpreted continuation guidance, not a validated record of events. See [MEM-RTE-branch-summary](#mem-rte-branch-summary).

#### MEM-OBJ-journal
Label: Workflow result journal

Source-native identity: persisted `journal` entries `{index, hash, result}` in workflow run state. Storage: JSON files under `~/.disco/workflows/projects/<cwd-derived-key>/runs/`, with primary, temporary and backup forms. Form: symbolic index/hash structure; result payload may be text or arbitrary schema-shaped data. The schema's semantics are not established by its JSON representation. It is distinct from [RT-OBJ-session-context](runtime.md#rt-obj-session-context): it stores returned values, not the child's event tree. Closest supplied route is [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent).

Lineage and admission: a successfully returned child result, or a checkpoint reply/default, is journaled automatically after abort/empty-result checks. No separate human content approval is required for child results. Checkpoint reply origin is human only when a confirmation callback supplies it; headless operation can retain a declared default or `true`. Run state separately retains script, args, attempts, status, errors and history; the replay consumer selects only a matching journal value. A result may lack the reasoning that produced it; replay does not reconstruct those reasons.

Evidence: SRC-1, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/run-persistence.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-paths.ts`.

> options.onAgentJournal?.({ index: callIndex, hash: callHash, result });
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

> reply = checkpointOptions.default ?? true;
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

#### MEM-OBJ-agent-history
Label: Compact child diagnostic history

Source-native identity: `AgentHistoryEntry[]` generated by `compactAgentHistory`. Storage: callback snapshots and persisted workflow agent state. Form: symbolic role/kind/tool flags and truncated natural-language text or JSON-displayed tool arguments. This is distinct from the replay payload in [MEM-OBJ-journal](#mem-obj-journal) and from the child's full messages in [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent). SRC-1, `cli/packages/coding-agent/src/disco/dynamic-workflows/agent-history.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/run-persistence.ts`; callback wiring symbol checked in `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts` and manager.

> const DEFAULT_MAX_ENTRIES = 40;
> const DEFAULT_MAX_TEXT_CHARS = 2000;
> const DEFAULT_MAX_TOTAL_CHARS = 20000;
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent-history.ts`

Code extracts text/tool calls/results/errors, omits thinking and nontext payloads, keeps a recent bounded tail, and truncates text. Authorship comes from mixed session events; admission/curation is automatic formatting, not human review or a new verified claim. Manager persistence retains snapshots for diagnostics. The inspected replay route reads `journal`, not this display history. No model read-back or behavior-shaping learning route from this history was established; complete UI rendering and other external consumers remain uninspected. Do not equate a short readable diagnostic with an opaque full tool result.

#### MEM-OBJ-saved-workflow
Label: Saved reusable workflow

Source-native identity: `SavedWorkflow` JSON with script, name, description, optional parameters, location and savedAt. Storage: project-namespaced `saved/` under workflow home or user `~/.disco/workflows/saved/`. Form: executable symbolic JavaScript script; natural-language description; symbolic parameter/default metadata. It is not a skill graph or a journal. Closest supplied counterpart is [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent), which executes children rather than naming the retained orchestration product. SRC-1, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-saved.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-paths.ts`.

> writeFileSync(path, JSON.stringify(saved, null, 2));
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-saved.ts`

The command/UI save path copies a selected run's script and workflow name, not its execution journal, verification rationale or run arguments. Generic API callers can supply scripts directly. A safe filename check controls storage admission; existing names are overwritten by this API without an independent semantic approval gate or backup protocol. Human command/UI selection is a content-selection act, but authorship of the original script may be model or caller; it is not inferred from who saves. A later command or nested-workflow resolver consumes executable script, not just its description. See [MEM-RTE-saved-workflow](#mem-rte-saved-workflow).

#### MEM-OBJ-library-state
Label: Managed library access state

Source-native identity: `RepoSkillsLibraryState` in `<agentDir>/repo-skills-library.json`, plus router invocation metadata in its installed SKILL.md. Storage: filesystem JSON and frontmatter, staged/swapped alongside managed collection changes. Form: symbolic source metadata, per-tree digests, inventory, timestamps and visibility flags. This is admission/access metadata, not the natural-language instructions in [RT-OBJ-operating-graph](runtime.md#rt-obj-operating-graph) or the transient eligible registry in [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry). Related route: [RT-RTE-library-update](runtime.md#rt-rte-library-update). SRC-1, `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`.

> return join(this.agentDir, "repo-skills-library.json");
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

> parsed.document.set("disable-model-invocation", true);
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

Lineage: manager derives state from source inventory and installed bytes; router toggle edits invocation metadata under lock. Consumers are update/conflict/status logic and subsequent resource discovery. Software admits metadata after structural/digest checks; caller invocation or force is not proof of per-content human review. Digests support drift detection, not evidential warrant. Router disable removes automatic listing eligibility, not content or explicit invocation. The CLI requests a new Researcher session; existing prompt copies do not retroactively disappear.

#### MEM-OBJ-context-files
Label: Loaded filesystem context files

Source-native identity: resource loader's `agentsFiles` and resolved system/append-system input strings. Storage: global/ancestor filesystem instruction files and in-memory prompt copies. Form: natural-language instructions with symbolic source paths. This is distinct from the listed skill registry in [RT-OBJ-skill-registry](runtime.md#rt-obj-skill-registry), although both enter prompt construction. SRC-1, `cli/packages/coding-agent/src/core/resource-loader.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/system-prompt.ts`.

> result += `<project_instructions path="${filePath}">\n${content}\n</project_instructions>\n\n`;
> --- `cli/packages/coding-agent/src/core/system-prompt.ts`

The loader resolves global and ancestor AGENTS/CLAUDE context; `noContextFiles` can omit it and API overrides can replace it. Prompt rebuilding inserts the selected bodies in project-context blocks. System/append overrides and mode defaults are additional channels. These are push-style invocation context selection, not automatically demonstrated use-derived memory. Initial authorship, human editing/approval, deployed trust and any use-driven write-back are uninspected. Physical file loading alone establishes no content-admission decision. If files change and are reloaded, later prompt construction can consume the new bytes; no observed update/read-back pair was supplied. Runtime's trust qualification remains necessary: extension-package pre-trust filtering is not a universal rejection of project text.

### Routes

#### MEM-RTE-branch-summary
Label: Branch summary transfer

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: navigateTree returns cancellation/abort state, optional editor text and the new summary entry.
- Later read-back: reconstructed destination-branch messages carry the derived exploration summary to later model invocations; the session tree can retain it across resumption.
- Delegated visibility: session_before_tree receives preparation and can cancel or supply summary/details or change focus; it is an extension, not necessarily a human reviewer.
- Selection predicate: caller selects a target and summarize option; code collects old-branch entries to the common ancestor and the summarizer budgets recent material.
- Invalidation or expiry: selecting another leaf changes active context; navigation without a summary transfers no derived summary. No time expiry was established.
- Activation or effect: host rebuilds Agent messages after switching leaf; model reliance or improved continuation is unobserved.
- Evidence limits: implementation trace only; no test of preservation, branch navigation or extension behavior was performed.

Distinct from [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction): target-branch attachment and user-message editor restoration are not first-kept compaction. It adds a separate context-control path to [RT-OBJ-session-context](runtime.md#rt-obj-session-context). Owner/progression: client request → AgentSession preparation → extension cancel/replacement or current-model summarization → SessionManager.branchWithSummary at destination → reconstruction. Payload: [MEM-OBJ-branch-summary](#mem-obj-branch-summary). Admission is software acceptance after model completion/abort/error handling, not semantic evaluation; custom instructions guide the proposal. There is no task-answer oracle. The human/client can decline summarization; extension cancellation vetoes navigation. No explicit per-summary human approval is established. Raw branch entries remain reachable in the event tree; navigating away is window removal, not deletion.

Evidence: SRC-1, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/compaction/branch-summarization.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`.

> if (result?.cancel) {
> 	return { cancelled: true };
> }
> --- `cli/packages/coding-agent/src/core/agent-session.ts:2960-2990`

> const summaryId = this.sessionManager.branchWithSummary(
> 	newLeafId,
> 	summaryText,
> 	summaryDetails,
> 	fromExtension,
> 	summaryUsage,
> );
> --- `cli/packages/coding-agent/src/core/agent-session.ts`

#### MEM-RTE-journal-replay
Label: Workflow journal replay

Part of: [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resume returns a boolean and launches background execution; a matching child/checkpoint call returns the cached result directly.
- Later read-back: persisted journal values become workflow-code inputs on resumed invocation, replacing a fresh child execution or confirmation callback.
- Delegated visibility: replay does not restore a child's entire transcript or run a new child for that hit; nested workflows explicitly discard the parent's resume journal.
- Selection predicate: deterministic lexical call index, stored hash equality and position before first miss; empty textual child outputs are not replayed.
- Invalidation or expiry: changed/new/missing calls terminate the replayable prefix; completed/aborted runs are refused by resume. Manual deletion can remove run files and sidecars; no time expiry was established.
- Activation or effect: workflow control receives a prior value without spending a fresh child call's tokens; actual semantic dependence in an executed workflow is unobserved.
- Evidence limits: hashes cover enumerated fields, not all environmental state; persistence is best effort and replay does not revalidate every prior result against the current world.

This is the retained-value subroute of the supplied child/workflow route, not an alternative identity for its full execution loop. Owner/progression: manager loads saved script/args/limits/journal → workflow assigns index/hash → match returns stored value, otherwise live child/checkpoint → journal callback → manager persistence. [MEM-OBJ-journal](#mem-obj-journal) records storage and provenance. Child model proposes results; schema/empty/abort gates can reject them; checkpoint may use human confirmation or a headless default. Open workflow tasks have no universal reference-answer oracle. A resumed run is not a new per-content approval.

Countercheck to an overly broad invalidation claim: hashAgentCall includes prompt, model spec, tier, phase, subSkill, agentType, environment, resolved agent-definition identity and schema. It does not hash current filesystem bytes or provider weights. hashCheckpoint covers promptText, kind and choices, but not the headless default. Therefore “anything changes” in a comment is not a complete dependency guarantee. A modified default alone need not invalidate a prior checkpoint reply. This qualifies cache safety without denying the implemented prefix check.

Evidence: SRC-1, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/run-persistence.ts`.

> if (hashMatches && !cachedEmptyOutput && callIndex < state.firstMiss) {
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

> const identity = JSON.stringify({
> 	promptText,
> 	kind: options.kind ?? "confirm",
> 	choices: options.choices ?? null,
> });
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

> if (!persisted?.script || persisted.status === "completed" || persisted.status === "aborted") return false;
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`

#### MEM-RTE-saved-workflow
Label: Saved workflow reuse

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: save returns a saved record and registers a slash command; command execution returns a report/custom message, while nested workflow execution returns child.result.
- Later read-back: a subsequent command registration/invocation or named nested workflow consumes retained script from project/user storage.
- Delegated visibility: script controls child calls; ordinary child context isolation still applies. Nested workflow shares counters/budget but not the parent's resume journal.
- Selection predicate: human command/UI save chooses a run/name; API save accepts caller content. Load prefers project over user by name; registration skips already registered command names.
- Invalidation or expiry: delete removes selected stored files; startup registers only listed workflows. Already registered handlers capture saved content and use an existence predicate, not a content-version check; replacement may require reload to update that handler.
- Activation or effect: retained symbolic script directly controls VM orchestration when invoked; its description alone does not. No exercised reuse or capacity improvement was observed.
- Evidence limits: generic storage methods are capabilities, but shipped command and named-nesting consumers establish wiring. No complete editor, parser or security audit is claimed.

No supplied record has this exact retained-script referent; it complements [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent). Trigger/change: save a run script as [MEM-OBJ-saved-workflow](#mem-obj-saved-workflow), or supply script through the storage API. Human selection of a particular run is separate from automatic file writing and from authorship. The save command/UI does not require successful completion or a scientific evaluation result; the storage API checks safe names, not a task answer. Save overwrites by name; no rollback or per-content confirmation is visible in this path. Malformed JSON/unsafe names are rejected on load, and the execution path applies its own parser. Guidance shaping the retained script comes from its original author; reasons/evidence are not automatically extracted from the run. The horizon is cross-invocation/project or user reuse, with no demonstrated benefit.

Evidence: SRC-1, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-commands.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-ui.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-saved.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/saved-commands.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`.

> script: run.script,
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-commands.ts`

> const { runId, promise } = manager.startInBackground(wf.script, parseCommandArgs(args, wf.parameters));
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/saved-commands.ts`

> const resolved = options.loadSavedWorkflow?.(String(nameOrScript));
> const childScript = resolved ?? String(nameOrScript);
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-summary-context
Label: Summary continuation authority

Consumer: subsequent foreground/child model invocation on the reconstructed branch. Channel: persisted compaction or branch summary → sessionEntryToContextMessages → convertToLlm → user-role summary text. Force: interpreted continuation context, not a tool policy or semantic truth gate. Horizon: later turns and resumed sessions while the selected branch retains the entry. This differs from [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance), which delivers installed skill guidance rather than conversation-derived checkpoints. It covers [MEM-OBJ-compaction](#mem-obj-compaction) and [MEM-OBJ-branch-summary](#mem-obj-branch-summary); neither delivery nor a key-decisions heading proves behavioral activation.

Evidence: SRC-1, `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/messages.ts`.

> return [createCompactionSummaryMessage(entry.summary, entry.tokensBefore, entry.timestamp)];
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

> case "branchSummary":
> 	return {
> 		role: "user",
> 		content: [{ type: "text" as const, text: BRANCH_SUMMARY_PREFIX + m.summary + BRANCH_SUMMARY_SUFFIX }],
> 		timestamp: m.timestamp,
> 	};
> --- `cli/packages/coding-agent/src/core/messages.ts`

## Annotations

#### On [RT-OBJ-operating-graph](runtime.md#rt-obj-operating-graph)

Lineage/curation: Creator doctrine requests source/task grounding, retained provenance, conflicts and assumptions before constructing operating instructions. Representative/source/executable checks and repairs shape proposed content. This is a requested transformation, not observed successful distillation of any particular graph. Import admits graph files; construction record and researcher-handoff remain requested outside live roots. Thus the model may later receive selected root/subskill guidance without receiving all construction reasons. Source: SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`; importer enforcement limits and minimum passages are supplied by [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission).

> Write `researcher-handoff.md` outside live skill roots with the anchor kind,
> distillation form, `Q` summary, `X` provenance scope, accepted or unverified
> `G`, `R` path, construction strategy, selected scope, exact imported paths,
> entry point, verification evidence, and unresolved limits. Do not load the
> resulting operating graph or execute the downstream task in this Creator run.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`

#### On [RT-RTE-library-update](runtime.md#rt-rte-library-update)

Memory-specific withdrawal: applyInventoryToStage removes previously managed skill IDs/root files missing from the new inventory, then replaces current official content; conflict checks can block removal of modified managed content unless forced. This reaches future discovery via the staged/live swap, not retroactive removal from existing session messages. State metadata and router visibility have separate consumers in [MEM-OBJ-library-state](#mem-obj-library-state). The CLI's disable command explicitly preserves explicit invocation. SRC-1, `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`, `cli/packages/coding-agent/src/cli/repo-skills.ts`.

> for (const skillId of Object.keys(state?.managedSkills ?? {})) {
> 	if (!inventory.managedSkills.has(skillId)) {
> 		rmSync(join(stagedRepoSkills, skillId), { recursive: true, force: true });
> 	}
> }
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

#### On [RT-OBJ-session-context](runtime.md#rt-obj-session-context)

Raw versus derived: active context uses latest compaction plus kept entries and later entries on the leaf path; other historical entries remain in the store. Projection admits message/custom-message/summary content but omits plain custom state entries and generic metadata. `details` can hold extension-specific structures without being delivered as readable summary; later extension consumers remain extension-specific. Subsequent compaction can consume file-tracking metadata even though the normal model projection does not. The derived parts are separately declared above. SRC-1, `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/messages.ts`.

> if (entry.type === "branch_summary" && entry.summary) {
> 	return [createBranchSummaryMessage(entry.summary, entry.fromId, entry.timestamp)];
> }
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

#### On [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction)

Read-back/selection: direct summarizer inspection extends the supplied trigger account with incremental previous-summary updates, split-turn prefix/history merging, character-capped tool text, and approximate retained-tail selection. [MEM-OBJ-compaction](#mem-obj-compaction) carries those facts and passages. This is automatic trace-fed retained context consumed by later model invocations; it is not published-skill learning or demonstrated improvement. Window removal is not physical deletion; the existing session tree remains an alternative source, without a proved automatic complete rehydration route.

#### On [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent)

Working-context control: fresh child context keeps the parent's accumulated conversation out; the return value crosses back, while disposal discards the child session's live frame. Filesystem writes, diagnostic history and journal persistence escape independently, so the stack-frame analogy is limited to context delivery, not effects or filesystem isolation. [MEM-OBJ-agent-history](#mem-obj-agent-history) distinguishes the truncated diagnostic from [MEM-OBJ-journal](#mem-obj-journal)'s replay result. A later replay hands a value to workflow code, not the internal transcript to another model. Detailed child input/tool construction and schema repair remain supplied runtime findings, not newly audited here.

## Write side

**Instruction construction and installation.** [RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission) separates model drafting/verification from requested human construction/import approval and executable structural validation. The anchor can be external source or task material; origin is not necessarily agent experience. No particular graph's transformation or reasons were inspected, so a system-wide trace-fed skill-update conclusion is unwarranted. Generic imports, specialized importers, library updates, direct writes and export are not one universal admission mechanism.

**Maintenance and rejection.** [RT-RTE-library-update](runtime.md#rt-rte-library-update) and its annotation distinguish upstream withdrawal, local conflicts, force, backups and staged replacement. Structural/digest rejection prevents intended helper admission; it does not prevent a separately authorized shell write. Router disabling affects automatic discovery only. Requested verification and construction records can retain reasons outside live roots, but the later minimal selected-body route does not automatically read those records.

**Trace summarization.** [MEM-OBJ-compaction](#mem-obj-compaction) and [MEM-RTE-branch-summary](#mem-rte-branch-summary) trace raw messages → selected/truncated serialization → model/extension checkpoint → session persistence → later summary-bearing context. Both can retain decision rationale in prose; neither proves faithful preservation. Extension override is a distinct writer; caller custom focus is not authorship of every output sentence. Cancellation or summary errors can prevent admission. Unknown extension payload provenance does not erase the known default transformation.

**Workflow traces and machinery.** [MEM-RTE-journal-replay](#mem-rte-journal-replay) is automatic result/checkpoint retention for replay; diagnostics are independently truncated, not validated knowledge. Run persistence writes temporary JSON then renames primary and attempts backup; manager persistence errors warn without necessarily failing the live run. Deletion best-effort removes primary and sidecars. [MEM-RTE-saved-workflow](#mem-rte-saved-workflow) is a different admission: explicit save selects retained executable orchestration from a run, without automatically retaining its evaluation evidence or journal. It is not an automatic evidence-responsive improvement algorithm.

## Read-back

| Route | Trigger and selector | Delivered retained part and consumer | Budget/authority/limit |
| --- | --- | --- | --- |
| Installed guidance | Later session discovery, then task/description matching or explicit name; [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) | Listing then selected file body to model; explicit command injects body | Router requests minimal relevant reads, not a measured hard token budget; guidance rather than assured obedience |
| Session resume | Caller chooses saved session/branch; [RT-RTE-foreground-task](runtime.md#rt-rte-foreground-task) | Reconstructed branch messages, including latest summary/tail, to Agent | Path projection, not entire stored tree; ordinary raw persistence alone is not derived learning |
| Compaction continuation | Manual call or auto threshold/overflow; [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction) | Derived checkpoint and retained tail to next model invocation | Code budget/cut plus model summarization; reasons and semantics may be lost |
| Branch transfer | Target plus optional summary; [MEM-RTE-branch-summary](#mem-rte-branch-summary) | Selected old-branch summary to destination's later model calls | Model-window reserve and 2,048-token summary request; extension may replace/cancel |
| Workflow replay | Explicit resume then index/hash/prefix selection; [MEM-RTE-journal-replay](#mem-rte-journal-replay) | Stored result or reply/default to workflow code | No semantic retrieval ranking or fresh child computation; dependency coverage is finite |
| Saved orchestration | Command name or nested workflow name; [MEM-RTE-saved-workflow](#mem-rte-saved-workflow) | Stored JavaScript to workflow executor | Exact-name/project precedence selection; executable control, not natural-language advice |
| Filesystem instructions | Loader/rebuild and configured overrides; [MEM-OBJ-context-files](#mem-obj-context-files) | Selected global/ancestor instruction bodies to system context | No new token budget established; initial files alone are static context, not use-derived memory |

These chains contain both pull and push steps. A requested skill read is not unsolicited retrieval just because descriptions were supplied automatically. Conversely, code-triggered compaction supplies a summary on a later call without the model requesting that particular retained passage. Exact name, call index and path are addressing inputs, not evidence of semantic relevance selection. No embedding/vector retrieval route was established by these reads; uninspected paths prevent a system-wide absence claim.

## Integration issues

- **Runtime extension, not a correction:** [RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction) explicitly left full prompts and branch alternatives uninspected. [MEM-OBJ-compaction](#mem-obj-compaction) adds checked prompt/serialization/budget details; [MEM-RTE-branch-summary](#mem-rte-branch-summary) supplies the independent branch path. Preserve the latter's destination attachment rather than merging it into compaction's first-kept semantics.
- **Replay safety qualification:** [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent) left invalidation uninspected. [MEM-RTE-journal-replay](#mem-rte-journal-replay) establishes a finite hash and prefix policy, including the checkpoint-default omission. Do not promote source comments about “anything changes” into a full environmental dependency guarantee. No supplied positive fact is contradicted.
- **Additional retained machinery:** [MEM-RTE-saved-workflow](#mem-rte-saved-workflow) extends the supplied account's uninspected saved-workflow surface. A saved command captures content at registration; existence checks do not prove refreshed content after replacement. Consequence: deletion and update behavior differ from fresh named storage loads.
- **Identity comparison:** summary objects are explicit parts of [RT-OBJ-session-context](runtime.md#rt-obj-session-context); replay is a part of [RT-RTE-workflow-agent](runtime.md#rt-rte-workflow-agent). Library-state, diagnostic-history, journal, saved-workflow and context-file objects have different stored referents/consumers from supplied containers as stated in their declarations. [MEM-BAP-summary-context](#mem-bap-summary-context) is a different source/channel from [RT-BAP-operating-guidance](runtime.md#rt-bap-operating-guidance). No possible duplicate remains after these comparisons; no supersession proposed.
- **Unresolved included surfaces:** specialized importer/exporter recovery, paper recovery/evaluation, individual graphs, task-oriented benchmark loops, full extension transformations and destructive release/reset cleanup remain uninspected as named in the coverage inventory. They prevent complete enumeration of admission, trace-fed learning, rationale retention and withdrawal across the shipped artifact. Actual external-agent consumption, live installed state and providers remain outside captured evidence. These limits coexist with the concrete local routes; they are not evidence of absence.

## Limitations and checks

The source checkout HEAD matched the registered commit and was clean at initial inspection and final recheck; the Commonplace worktree had no tracked diff. Evidence identity is SRC-1's repository and reviewed revision, not the local checkout path. Governing method inputs were read completely, including the bounded runtime and records-contract ranges; no authoring skill, prior analysis or other worker state was used. This report uses source text and supplied records, not execution evidence. Delivery, replay capability and instruction replacement do not establish activated reliance, exercised learning, reflection, theory criticism or improved future performance. No general claim of their absence is made.

Deterministic validation: the invocation-specific `commonplace-run validate-output` command passed with “Member content check passes; invocation residue not checked.” This is not job acceptance or claim support. The check concerns member form and quotation occurrence, not causal support or complete source coverage.
