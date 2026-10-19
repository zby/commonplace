---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AREX-Skill runtime baseline: DisCo invocation, skill delivery, delegated execution and bounded change admission at the frozen commit."
run-id: AAS-2026-10-15-arex-skill-1871063034b5-01
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill runtime report

## Runtime account

### Work and evidence boundary

DisCo encloses a coding-agent session and also supplies the machinery and instructions for constructing its future operating context. The Researcher is asked to execute downstream ML/software tasks; the Creator is asked to produce operating skill graphs, verification evidence and a handoff instead. These are instructions, not two separately confined operating systems. [RT-CLM-mode-contract](#rt-clm-mode-contract) preserves that distinction. Published repository guidance can also be exported to other agents, whose execution is outside this boundary.

This account uses SRC-1 at the exact reviewed commit in [the boundary](boundary.md). Added implementation inspection covers `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/resource-loader.ts`, `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/system-prompt.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`, `cli/packages/coding-agent/src/core/model-runtime.ts`, `cli/packages/coding-agent/src/core/tools/bash.ts`, `cli/packages/coding-agent/src/modes/print-mode.ts`, `cli/packages/coding-agent/src/cli/repo-skills.ts`, selected transaction ranges in `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`, and the dynamic-workflow and generic operating-graph importer paths cited below. Added doctrine inspection covers the mode prompts, distillation instructions and published router. These remain implementation and doctrine/design evidence, not observed runs. No target program, test, example or model was executed. Activation, successful task completion and benefit remain unobserved.

### Ordinary invocation: one foreground Researcher request

The selected ordinary path is `disco -p "task"`, with a configured provider and default Researcher mode. The print entry explicitly documents this use (SRC-1, `cli/packages/coding-agent/src/modes/print-mode.ts`); `cli/packages/coding-agent/src/disco/modes/types.ts` sets the default to `researcher`. The identities relevant to the loop are cwd, agent directory, session ID/branch, DisCo mode and provider/model ID. They are not independent security principals. The initiating principal is the CLI caller; the model chooses ordinary next actions within the session tool surface, and the host executes them. See [RT-RTE-foreground-task](#rt-rte-foreground-task).

`main.ts` prepares session services, settings and resource loading, resolves trust, CLI tool/model overrides and authentication, constructs the session runtime, prepares input and dispatches interactive, RPC or print mode. Print mode binds extensions and sends each supplied prompt serially. `AgentSession.prompt` first offers slash commands and input interception to extensions, then expands skill/template syntax. It validates the model/auth configuration, checks compaction, constructs a user message and pending context, lets extensions add messages or replace the system prompt, then calls the Agent. The SDK's stream callback routes the request through ModelRuntime with timeout/retry settings and header/payload hooks. These are code rules and symbolic API values surrounding natural-language model decisions, not proof of provider-internal control. [RT-CMP-model-runtime](#rt-cmp-model-runtime) bounds the numerical component.

The shipped default active coding tools are read, bash, edit and write. SDK/CLI allow/exclude settings can narrow the registry; extensions and SDK custom tools can add or replace definitions by name. Tool-call and tool-result hooks mediate ordinary Agent tool execution. Bash's default executor spawns a local shell with cwd and environment, streams output, and optionally kills its process tree on timeout/abort. That is an effect boundary at the process's filesystem/network/credential authority, not a filesystem jail. The capability surface includes shell subprocesses and extension code; the current grant set depends on caller options and loaded extensions; the actual deployed isolation envelope is not supplied.

The session subscribes to messages and persists ordinary user/assistant/tool-result events; session creation can reconstruct existing messages. AgentSession continues after retryable errors, compaction recovery or queued messages. Print mode outputs final assistant text or JSON events, reports error/aborted final answers as failure in text mode, and disposes the runtime. Interactive and RPC are alternative clients of this session runtime, not evidence that every client command has identical policy coverage. Their complete command surfaces were not audited.

### Skill delivery and working context

Skill discovery first creates an eligible registry. The model normally receives names, descriptions and file locations, not all skill bodies. A natural-language matching instruction asks it to read the relevant file. The repository router further asks for area → family → selected repository root → relevant references/scripts, and permits no exact match. An explicit `/skill:name` is a materially different entry: host code reads the registered file, strips frontmatter and inserts its body into the user message. [RT-RTE-skill-delivery](#rt-rte-skill-delivery) distinguishes these routes. Delivery is not proof of compliance or correct selection.

The other inspected working-context controls are: extension replacement/transformation of input/context/system prompt; manual/automatic compaction with summary plus retained tail; and separate in-memory workflow-agent sessions. Compaction can retain a summary for a later invocation, whereas a child session excludes its entire internal conversation from the parent's ordinary return. [RT-RTE-context-compaction](#rt-rte-context-compaction) and [RT-RTE-workflow-agent](#rt-rte-workflow-agent) state the different escape paths. The stack-frame analogy fits the child session's selected inputs and return value, but filesystem writes, diagnostic history and journals can escape the frame, and neither context window has pointer-following liveness semantics. This is not an isolation guarantee for side effects.

### Three forcing cases and guarantee coverage

1. **Role filtering versus direct file/shell access.** Resource loading filters the eligible registry by mode. Shared skills are visible to both; absent role metadata defaults to operating. This enforces a registry predicate, while the Creator/Researcher prohibition on other work is prompt policy. Direct reads, bash and extension code are materially different paths not shown to be blocked by that predicate. Thus “Researcher cannot modify skills” would overstate the implementation. Owner: resource loader for registry filtering, agent for following the mode prompt. Enforcement: `isSkillEligibleForDiscoMode` and the post-load filter. Guarantee strength: invariant for this registry transformation; policy for task/role compliance. Required external contract: downstream tool/runtime and model behavior must respect any stronger restriction a deployment wants. implementation conclusion status: wired. operation conclusion status: uninspected. Evidence: [RT-CLM-mode-contract](#rt-clm-mode-contract), [RT-RTE-skill-delivery](#rt-rte-skill-delivery).

2. **Structured return versus prose-only failure.** Workflow agents get a schema tool and repair prompts, but the implementation can also accept schema-valid converted JSON extracted from prose. Therefore “all accepted results come from a final tool call” is false. Owner/enforcement: WorkflowAgent's `resolveStructuredOutput`; guarantee strength: invariant for its final schema gate, best effort for tool-call compliance. The external contract is schema-checker correctness and actual meaning of the supplied schema; schema validity supplies no answer oracle. Ordinary string-return agents, foreground responses and direct provider calls do not pass this gate. implementation conclusion status: wired. operation conclusion status: uninspected. See [RT-RTE-workflow-agent](#rt-rte-workflow-agent).

3. **Validated import versus arbitrary writes and process failure.** The generic importer rejects malformed roles/names/links and existing targets without an overwrite flag; managed library installation stages content, detects conflicts, checks official digests and attempts rollback on caught swap errors. These mechanisms do not certify the scientific truth or task efficacy of a skill. Sequential renames and fallible rollback are not an all-reader atomicity or power-loss guarantee. Owners/enforcement: importer validation and rename/rollback routines; library manager's locked staging/swap path. Guarantee strength: protocol. Required external contract: cooperating writers, functioning filesystem operations and use of the intended helper. Alternate paths include normal file tools, shell writes, specialized repository import/export helpers and upstream publication; they do not inherit this generic helper's checks. implementation conclusion status: wired. operation conclusion status: uninspected. See [RT-RTE-graph-admission](#rt-rte-graph-admission) and [RT-RTE-library-update](#rt-rte-library-update).

Project trust also has narrower coverage than a shell sandbox: the resource loader's pre-trust pass excludes project-local extensions/packages but still loads user/global and temporary CLI extensions. Project SYSTEM/APPEND_SYSTEM discovery checks trusted state. The same reload separately loads project context files. No blanket claim that all untrusted project text is excluded follows (SRC-1, `cli/packages/coding-agent/src/core/resource-loader.ts`). Tool allowlists apply to the session registry, not arbitrary code inside an extension, a shell command or a remote provider. Direct ModelRuntime calls also bypass AgentSession prompt/tool interception (SRC-1, `cli/packages/coding-agent/src/core/model-runtime.ts`). Dependency-internal provider-native tools and remote workers remain uninspected, not proved absent.

### Change-admission coverage and limits

The Creator protocol proposes and verifies instruction changes, then asks for scope/destination and import approval. The generic importer and managed published-library updater supply distinct executable admission paths. They are not equivalent to per-content human review: flags encode a caller's choice, while the helper does not independently identify a human approver. These paths retain instructions that a later Researcher can read; [RT-BAP-operating-guidance](#rt-bap-operating-guidance) records the authority channel.

Other included change mechanisms remain only partly inspected: specialized repository and meta-skill importers, paper distillation/recovery validators, saved workflow authoring and cross-agent export. A symbol-level inspection of `cli/packages/coding-agent/src/disco/skills/import-repo-skills-to-agent/scripts/export_repo_skills_to_agent.mjs` found selected-ID and overwrite-ID arguments, staging/validation routines and persisted transaction fields; its recovery semantics were not traced. No generic-import guarantee is attributed to it. Existing source-build/release scripts, production deployment, task-oriented FrontierCS/PaperBench/PassNet loops and individual repository graphs remain uninspected here. This preserves the boundary's partial-loop classification rather than silently excluding them. Ordinary tools can modify product files or production machinery when granted sufficient OS authority, but no general product acceptance/release gate was established. The account makes no exercised self-improvement or learning claim: creation, installation and instruction delivery alone do not establish later behavior causally depending on the change, much less improved capacity.

## Shared records

### Components

#### RT-CMP-model-runtime
Label: Provider-backed language models

Source-native identity: foreground Agent model and WorkflowAgent-resolved provider/model instances, mediated by ModelRuntime. Representational form: distributed-parametric model computation; provider/model identifiers, settings and requests are symbolic configuration, not the parameters. Storage substrate: provider-hosted parameters are outside the captured checkout; runtime keeps model/config/auth objects, and session entries can record provider/model IDs. Evidence: SRC-1, `cli/packages/coding-agent/src/core/sdk.ts`, `cli/packages/coding-agent/src/core/model-runtime.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`.

Parameter changes during operation: uninspected inside providers; inspected request code exposes inference routing, not a weight-update procedure. Exact version pinned: no exact weight revision established for either foreground or child models; saved provider/model names and package version pins do not pin weight bytes. Mutable endpoint resolution: afforded through provider/auth base URL and registry configuration; whether a deployed endpoint changes backing models is uninspected. Workers can choose explicit model, tier, configured medium tier or session default; an unresolved requested model warns and falls back. The compaction route uses the current session model or extension-supplied result, not a separately established learned component.

> model: resolution.auth.baseUrl ? { ...model, baseUrl: resolution.auth.baseUrl } : model,
> --- `cli/packages/coding-agent/src/core/model-runtime.ts`

> return prepared.provider.streamSimple(prepared.model, context, prepared.options as SimpleStreamOptions);
> --- `cli/packages/coding-agent/src/core/model-runtime.ts`

### Operative objects

#### RT-OBJ-skill-registry
Label: Eligible skill registry

Source-native identity: ResourceLoader's loaded `skills` collection. Representational form: symbolic names, paths, roles and visibility flags, with natural-language descriptions consumed by the model. Storage substrate: in-process array derived from skill files; prompt rendering copies selected fields into text. Distinct from a candidate graph or its admission record. The full skill bodies are consumed along [RT-RTE-skill-delivery](#rt-rte-skill-delivery), not encoded in the discovery listing. Evidence: SRC-1, `cli/packages/coding-agent/src/core/resource-loader.ts`, `cli/packages/coding-agent/src/core/skills.ts`.

> .filter((skill) => isSkillEligibleForDiscoMode(skill.discoRole ?? "operating", this.discoMode))
> --- `cli/packages/coding-agent/src/core/resource-loader.ts`

> lines.push(`    <location>${escapeXml(skill.filePath)}</location>`);
> --- `cli/packages/coding-agent/src/core/skills.ts`

#### RT-OBJ-operating-graph
Label: Operating skill graph files

Source-native identity: imported top-level operating-skill roots with SKILL.md files, links, references and optional scripts. Representational forms split by consumer: natural-language operating guidance for a model; symbolic frontmatter/link structure for validators; executable script text for interpreters. Storage substrate: project `.agents/skills/` or managed agent `skills/` filesystem directories. This record names the artifact container, not an assertion that every part shares epistemic warrant. The generic importer rejects repository-routing metadata, which belongs to a specialized path. Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`.

> if (role !== "operating") {
> 		throw new ImportError(`${skillFile} metadata.disco-role must be operating`);
> 	}
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`

#### RT-OBJ-session-context
Label: Session branch and reconstructed messages

Source-native identity: SessionManager entries, active branch and Agent messages. Representational form: symbolic event tree, IDs, model settings and entry types containing natural-language messages and summaries. Storage substrate: session files under agent sessions directories, or in-memory SessionManager for workflow children. `buildSessionContext` reconstructs messages on the selected path; compaction substitutes summary plus kept entries, not destruction of all historical entries. Evidence: SRC-1, `cli/packages/coding-agent/src/core/session-manager.ts` and `cli/packages/coding-agent/src/core/sdk.ts`.

> const messages = buildContextEntries(entries, leafId, byId).flatMap(sessionEntryToContextMessages);
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

### Routes

#### RT-RTE-foreground-task
Label: Foreground task execution

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI print client receives final assistant text, or serialized events in JSON mode; error/aborted final assistant messages set failure in text mode.
- Later read-back: session creation rebuilds saved messages and restores them when present; specific retention transformations belong to the memory account.
- Delegated visibility: extensions can intercept input/context, add custom messages or replace system prompt; workflow children do not automatically inherit the full foreground transcript.
- Selection predicate: caller chooses app mode and optional model/tools; default Researcher handles a user task, with the model selecting ordinary next actions from the active registry.
- Invalidation or expiry: runtime disposal ends live state; resumption reconstructs a saved branch and may fall back if a saved model cannot be restored. Expiry of saved files is uninspected.
- Activation or effect: wired model calls and tool execution can affect local files/processes and network through granted tools; actual compliance, task success and side effects in a run are unobserved.
- Evidence limits: source trace only; Agent dependency internals, deployed permissions and the complete interactive/RPC command surface are uninspected.

Owner/progression: caller → main/services/runtime → print client → AgentSession.prompt → Agent/provider → tool executor/results → AgentSession continuation → client. Inputs comprise user text/images, system guidance, selected skills/context, current branch, model and auth settings. The default four tools are a grant default, not all possible capabilities. Allowed/excluded names filter built-ins, extension tools and SDK custom tools in `_refreshToolRegistry`; custom definitions may replace same-name built-ins. `beforeToolCall` delegates policy blocking to extension handlers when installed, and does nothing when no handler exists. Bash uses a local shell with optional timeout/abort process-tree kill; no deployed container or per-file authorization policy was supplied. Recovery: provider timeout/retry configuration, session-level retry/compaction continuation, abort/disposal. Admission/oracle: open-request task mode; the caller supplies the objective, model proposes actions, code executes, and no universal reference answer is wired at this entry.

Evidence: SRC-1, `cli/packages/coding-agent/src/main.ts`, `cli/packages/coding-agent/src/core/sdk.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/tools/bash.ts`, `cli/packages/coding-agent/src/modes/print-mode.ts`.

> const defaultActiveToolNames: ToolName[] = ["read", "bash", "edit", "write"];
> --- `cli/packages/coding-agent/src/core/sdk.ts`

> await this.agent.prompt(messages);
> 			while (await this._handlePostAgentRun()) {
> 				await this.agent.continue();
> 			}
> --- `cli/packages/coding-agent/src/core/agent-session.ts`

> const child = spawn(shellConfig.shell, commandFromStdin ? shellConfig.args : [...shellConfig.args, command], {
> 				cwd,
> 				detached: process.platform !== "win32",
> 				env: env ?? getShellEnv(),
> --- `cli/packages/coding-agent/src/core/tools/bash.ts`

#### RT-RTE-skill-delivery
Label: Registry selection and skill-body delivery

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normal discovery yields name/description/location prompt entries; explicit `/skill:name` yields a frontmatter-stripped body inside a skill block, with arguments appended.
- Later read-back: a later session can discover files admitted to the same project or managed scope; source does not establish which newly authored graph was subsequently used.
- Delegated visibility: child sessions construct their own resource loader in the inherited DisCo mode; parent context is not the source of that registry.
- Selection predicate: loader applies role eligibility; model-visible listing also respects disableModelInvocation; normal semantic matching is delegated to the model, while explicit command lookup compares skill names exactly.
- Invalidation or expiry: reload rediscovers skills; file read failure emits an error and returns the original command text. Updating a file is not proof that an already supplied prompt body changes.
- Activation or effect: model receives guidance by listing/read result or expanded user text; changed downstream behavior remains unobserved.
- Evidence limits: no routing accuracy, prompt compliance or individual graph correctness established; arbitrary direct reads are outside the registry filter.

Owner/progression: resource loader → registry → prompt formatter → model-selected read/router branch, or command expander → user message. Current task and descriptions inform semantic choice; router doctrine requests only one or two likely areas, relevant families and minimal roots. Its no-match branch is a supported alternative to forced selection. Decision roles: human may name a skill, model proposes normal matching, loader vetoes registry eligibility, formatter omits disabled automatic invocation entries. Answer oracle: inapplicable — description matching and router judgment have no expected-answer service here. Operating mode: open tasks, not a fixed routing benchmark. Evidence: SRC-1, `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/disco/modes/skill-policy.ts`, `skills/repositories/repo-skills-router/SKILL.md`.

> "Use the read tool to load a skill's file when the task matches its description.",
> --- `cli/packages/coding-agent/src/core/skills.ts`

> const body = stripFrontmatter(content).trim();
> 			const skillBlock = `<skill name="${skill.name}" location="${skill.filePath}">\nReferences are relative to ${skill.baseDir}.\n\n${body}\n</skill>`;
> --- `cli/packages/coding-agent/src/core/agent-session.ts`

> 5. If no exact family fits, do not force a repository match; continue with the general task context or report that the managed collection has no exact route.
> --- `skills/repositories/repo-skills-router/SKILL.md`

#### RT-RTE-graph-admission
Label: Creator construction and generic graph import

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: importer prints installed root IDs/destinations and instructions to start a Researcher session; Creator doctrine asks for accepted graph, construction record and external handoff, or explicit verification blockers.
- Later read-back: installed graph roots enter subsequent eligible skill discovery/read paths; actual later consumption is unobserved.
- Delegated visibility: Creator instructions permit selected workflow delegation; generic import writes shared project/managed files rather than transferring chat context.
- Selection predicate: source/task anchor, scoped capabilities, evidence and construction strategy choose candidate roots; importer checks canonical identities, explicit operating role, graph-local existing links and collisions.
- Invalidation or expiry: replacement requires overwrite flag for existing targets; role and managed-namespace collision checks can still reject. No time expiry established.
- Activation or effect: helper stages, validates, renames roots into live scope and revalidates; intended future model guidance is delivered through the separate skill route, not proven activated by import.
- Evidence limits: semantic verification and human approvals are procedural requests; the helper's structural checks do not prove them or identify a human approver. Specialized importers differ and are not covered by this record's transaction finding.

Trigger/proposed change: a source/task distillation request leads the Creator model to draft natural-language operating guidance and associated files. Guidance: scope capabilities, ground in evidence, construct graph, verify through static/source/executable/link and applicable representative-use checks; direct strategy requires exact-spec approval after grounding. The model proposes and repairs, requested human approval can veto construction/import, and the importer deterministically rejects structural defects or conflicts. Operating modes: task-agnostic representative workflows and task-oriented verification with task data/evaluator/goal; no universal answer oracle, and actual task-level reference outcome/provider remains anchor-specific and uninspected.

Admission/recovery: scope is project `.agents/skills` or managed agent `skills`; drafts must lie outside live scope. Import validates draft and staged graphs, checks collisions again, backs up replaced roots, renames staged roots and validates live targets. On caught failure before commit it attempts rollback; rollback errors are surfaced. The script's shared-lock wrapper is present, but lock implementation was not audited here. Ordinary write/bash bypasses this helper, so its rejection rules are not a global write policy. What persists: graph files; the construction record and handoff are requested outputs outside live roots, not structurally enforced by this importer. Improvement trigger is a requested capability gap or source anchor, not automatic evidence of improved future capacity. The inspected procedure does not itself identify a formulated explanatory theory inside any particular graph; theory-builder status for a graph's content is uninspected rather than inferred from packaging.

Evidence: SRC-1, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`.

> **Verify** the candidate graph with static, source-support, executable,
>    graph/link, and applicable task-level or representative-use checks. Exercise
>    failure recovery and repair affected skills, links, evidence mappings, or
>    fixtures.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`

> if (conflicts.length > 0 && !args.overwrite) {
> 		throw new ImportError(
> 			`live target(s) already exist: ${conflicts.join(", ")}. Obtain separate overwrite approval, then rerun with --overwrite`,
> 		);
> 	}
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`

> validateGraph(targets);
> 		committed = true;
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/scripts/import_operating_skill_graph.mjs`

#### RT-RTE-library-update
Label: Published repository collection installation and update

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: install/update result includes source commit, counts, router visibility, noop/issues and possible backup path; CLI asks for a new Researcher session.
- Later read-back: subsequent Researcher loading can consume the replaced managed collection and router; no run showing a particular update reaching decisions was inspected.
- Delegated visibility: filesystem collection is shared with later eligible sessions; cross-agent export is a separate mechanism whose full semantics remain uninspected.
- Selection predicate: caller chooses install/update and force; source inventory distinguishes managed official skills from local content, checks conflicts and detects unchanged snapshots/digests.
- Invalidation or expiry: update replaces managed inventory through staging; local conflicts reject unless forced, and router disabled state is preserved. Explicit router invocation remains available under the CLI's stated contract.
- Activation or effect: manager stages collection/router/state, rebuilds routing, checks official staged digests and swaps live paths; this is admission to the store, not demonstrated model activation.
- Evidence limits: acquired live source, filesystem durability and runtime exercise unobserved; source acquisition and complete conflict classification were not audited end to end.

Owner/endpoints: CLI caller → RepoSkillsLibraryManager → source inventory → locked staged collection/router/state → live files → future session. Operating mode is operator-initiated collection maintenance, with updates driven by a selected source snapshot, not a scored learning curriculum. Upstream content authors propose the official content; software chooses inventory transformations; caller can withhold invocation or force replacement; no per-content human semantic approval is established. Answer oracle: inapplicable — digests and structural routing checks compare artifacts, not task answers. Persisted source commit and digests support later drift/conflict detection. `swapLiveTree` backs up old paths and tracks installed ones, attempts reverse restoration after caught errors, and preserves recovery artifacts when rollback fails. Forced conflicts can preserve a backup. Guidance shaping the instructions is upstream publication, not reconstructed by the installer; the manager admits bytes without proving their epistemic quality. No production release gate follows from this local-library protocol.

Evidence: SRC-1, `cli/packages/coding-agent/src/cli/repo-skills.ts`, `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`.

> if (conflicts.length > 0 && !force) throw new RepoSkillsLibraryConflictError(conflicts);
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

> if (actual.digest !== expected.digest) {
> 						throw new RepoSkillsLibraryError(`Staged official skill changed during validation: ${skillId}`);
> 					}
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

> `${error instanceof Error ? error.message : String(error)}; rollback failed:\n${rollbackErrors.join("\n")}\nRecovery artifacts remain at ${transactionRoot}`,
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

#### RT-RTE-workflow-agent
Label: Dynamic workflow child execution and structured return

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: child run returns last assistant text or a schema-validated captured/recovered value; empty text or exhausted schema repair raises a typed workflow error.
- Later read-back: manager journals agent results and persists run state for recovery/resume; semantic replay guarantees and all journal invalidation cases remain uninspected.
- Delegated visibility: fresh in-memory session receives task/instructions/label and its own resources in inherited mode, not the parent's accumulated messages. Filesystem writes, compact diagnostic histories and usage callbacks can escape separately from the return.
- Selection predicate: workflow code chooses calls and options; child model resolution uses explicit model/tier/default rules; tool policy filters constructed tools and adds structured_output for schema tasks.
- Invalidation or expiry: session is disposed in finally; abort is propagated. Saved journals have separate persistence; complete cache/replay expiry policy was not audited.
- Activation or effect: child can execute granted tools against its cwd, optionally a worktree, and return a result used by workflow code; no observed delegation or causal benefit supplied.
- Evidence limits: context separation is not OS isolation; provider internals and every workflow recovery, worktree and budget edge case remain uninspected.

Trigger/owner: dynamic workflow script calls the injected `agent` function; WorkflowManager owns run lifecycle, concurrency/agent/retry/timeout/token/recovery limits and persistence callbacks, while WorkflowAgent owns the child session. Workflow source runs as an async body in a Node VM context exposing agent/parallel/pipeline/gate/checkpoint and other helpers. This is programmed orchestration with model decisions inside calls, not one foreground model autonomously selecting every graph edge. The child inherits Creator/Researcher mode; supplied session overrides for resourceLoader/sessionManager/mode are deleted before fresh session creation. Built-in tool policies therefore do not imply that the foreground session's particular current grants are inherited.

Decision/validation policy: schema provider is the workflow author; TypeBox validation is an output-shape gate, not an answer oracle. Model produces output, host checks, repair prompts can request another output, and final failure vetoes return. A positive schema alone cannot establish truth. `resolveStructuredOutput` first accepts tool capture, then retries with only structured_output requested, then tries parsed/coerced schema-valid prose, else throws. Operating modes include ordinary open subtask requests and author-programmed comparisons/gates; scoring, if selected, remains model judgment rather than a reference answer. Optional human checkpoints and supplied validators are workflow-specific, not a universal approval requirement. A script's `gate` can feed feedback into another attempt, but that affordance alone is not evidence of content-directed theory criticism or learning. Worktree creation/teardown and persisted recovery are separate effect paths, not covered by schema validity.

Evidence: SRC-1, `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`, `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow-manager.ts`.

> sessionManager: SessionManager.inMemory(runCwd, { discoMode: this.discoMode }),
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`

> const extracted = extractValidated<T>(lastText(session.messages), schema);
> 	if (extracted !== undefined) {
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/agent.ts`

> const result = await new vm.Script(wrapped, { filename: `${meta.name || "workflow"}.js` }).runInContext(context);
> --- `cli/packages/coding-agent/src/disco/dynamic-workflows/workflow.ts`

#### RT-RTE-context-compaction
Label: Compaction and context reconstruction

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: manual compact returns summary/first-kept-entry/token estimates and emits events; automatic path can compact at threshold or compact and retry after overflow.
- Later read-back: compaction entry persists summary and retention boundary; reconstruction supplies it plus kept branch entries to later model invocations.
- Delegated visibility: extension session_before_compact receives preparation/branch entries and may cancel or supply replacement content; provider summarization receives prepared content, not a proved complete historical transcript.
- Selection predicate: explicit compact call or enabled auto threshold/overflow check; preparation and configured retention select removed history and kept tail. Detailed cut-point heuristics are uninspected.
- Invalidation or expiry: latest compaction on active branch determines reconstruction; stale pre-compaction usage is ignored for auto checks; superseded raw history remains outside the active model window.
- Activation or effect: code replaces Agent messages with reconstructed context; semantic preservation or changed decisions have no execution evidence.
- Evidence limits: manual path and automatic trigger logic inspected; full summarizer prompts, branch-summary alternatives and automatic retry internals are not audited here.

Owner/progression: human/client explicit request or code threshold → preparation → extension override/cancel or current model summary → appendCompaction → buildSessionContext → Agent state. Representation: natural-language summary within symbolic entry and firstKeptEntryId. The summary changes later context without being a new published operating graph. Human custom instructions may shape a summary; extension or model supplies content and host admits it after completion/abort checks, not a semantic correctness oracle. Rejection/recovery: too-small/already-compacted input and cancellation fail; overflow recovery allows one compact/retry before reporting failure. This preserves a window by replacing old material with a summary and tail rather than merely accumulating turns. Historical files and on-demand skill reads offer other access paths, but an automatic complete rehydration of summarized text is not established.

Evidence: SRC-1, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`.

> this.sessionManager.appendCompaction(summary, firstKeptEntryId, tokensBefore, details, fromExtension, usage);
> 			const newEntries = this.sessionManager.getEntries();
> 			const sessionContext = this.sessionManager.buildSessionContext();
> 			this.agent.state.messages = sessionContext.messages;
> --- `cli/packages/coding-agent/src/core/agent-session.ts:1872-1875`

> if (entry.id === compaction.firstKeptEntryId) {
> 			foundFirstKept = true;
> 		}
> 		if (foundFirstKept) {
> 			contextEntries.push(entry);
> 		}
> --- `cli/packages/coding-agent/src/core/session-manager.ts`

### Claims

#### RT-CLM-mode-contract
Label: Creator and Researcher separation

Claimed operation: Creator constructs operating context without executing downstream work; Researcher executes tasks without constructing the library. Source: SRC-1, `cli/packages/coding-agent/src/disco/modes/prompts.ts`. Strength differs by mechanism: natural-language policy governs task behavior, symbolic role eligibility governs only loaded registry membership. Implementation evidence: `cli/packages/coding-agent/src/disco/modes/skill-policy.ts` and `cli/packages/coding-agent/src/core/resource-loader.ts`.

> "You are DisCo's skill-powered research agent. Under the fixed coding-agent harness, solve the downstream ML research or software task by loading only task-relevant operating skills as operating context. You use those skills to inform execution; you do not construct the skill library.",
> --- `cli/packages/coding-agent/src/disco/modes/prompts.ts`

> export function isSkillEligibleForDiscoMode(role: DiscoSkillRole, mode: DiscoAgentMode): boolean {
> 	if (role === "shared") return true;
> 	return mode === "creator" ? role === "meta" : role === "operating";
> }
> --- `cli/packages/coding-agent/src/disco/modes/skill-policy.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-operating-guidance
Label: Installed operating guidance to later model decisions

Consumer: later eligible Researcher model invocation. Channel: filesystem skill graph → registry description/location → selected read result or explicit expanded skill block. Force: natural-language task guidance interpreted by the model; registry eligibility and command expansion are executable rules, not guarantees of model obedience. Horizon: across sessions when the files remain installed in the same discovered scope; actual recurrence unobserved. Direct Creator import and published-library update can feed this path, but admission consumers differ from the downstream model. Retained scripts have a distinct executable effect only when invoked through a tool/interpreter; their mere presence is not execution.

Evidence: SRC-1, `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`; minimum passages are retained in [RT-RTE-skill-delivery](#rt-rte-skill-delivery) and [RT-RTE-graph-admission](#rt-rte-graph-admission). This is a wired delivery/authority path, not observed activation or evidence of exercised self-improvement.

## Annotations

none
