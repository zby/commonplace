---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AREX-Skill's DisCo session, skill-delivery and change-admission runtime at the frozen partial-loop boundary."
run-id: AAS-2026-10-19-arex-skill-089a5ed7476f-01
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
---

# AREX-Skill runtime report

## Runtime account

AREX-Skill ships both operating guidance and the DisCo application that consumes it. This account retains the [boundary](boundary.md)'s complete-artifact, partial-loop scope. All implementation findings below use SRC-1 at the frozen commit. New inspection extends to the session-services adapter, print consumer, RPC bash branch, project-trust resolver, local shell executor and model-runtime request methods. These add implementation evidence, not observed operation. No target code, tests, examples or providers were executed; supplied example exports were not inspected. Activation, reliability and benefit remain unobserved.

### Ordinary invocation and next-step ownership

An ordinary `disco -p` request enters the package's `dist/cli.js`, then `main`. Main creates services and a session runtime, prepares the initial message (including piped input outside RPC), and selects print, interactive or RPC consumption. `createAgentSessionFromServices` forwards services and tool options into the SDK. The SDK resolves working directory and agent directory, validates Creator/Researcher mode consistency, loads resources when no loader was supplied, restores the selected session context, and selects a model from explicit input, restored identity or defaults. Provider/model IDs, thinking level and session ID are distinct identities; none identifies exact model weights. SRC-1: `cli/package.json`, `cli/packages/coding-agent/src/main.ts`, `cli/packages/coding-agent/src/core/agent-session-services.ts`, `cli/packages/coding-agent/src/core/sdk.ts`.

[RT-RTE-session-prompt](#rt-rte-session-prompt) follows the foreground request through extension interception, skill/template expansion, authentication, pre-prompt compaction, user-message construction and the agent call. The external agent-core owns the internal model/tool turn schedule; this checkout supplies context transforms, tool hooks and the provider-stream closure. The model proposes next actions, symbolic runtime dispatch invokes registered tools, and the OS or custom executor realizes their effects. That is a division of responsibility, not evidence that the model obeys the instructions.

The default active grant is `read`, `bash`, `edit`, `write`; the broader tool registry and extension registration are capability surfaces, not necessarily current grants. [RT-RTE-tool-grants](#rt-rte-tool-grants) describes their name-based filtering. Model calls receive converted session messages and a base or extension-modified system prompt. An extension can handle input without a model request, replace text/images, supply extra messages or override the system prompt. Provider controls include transport, timeout, WebSocket timeout, retry limits, attribution/header transforms, payload interception and response notification. These are client controls, not guarantees about remote inference. The model component is [RT-CMP-model-runtime](#rt-cmp-model-runtime). SRC-1: `cli/packages/coding-agent/src/core/sdk.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`.

Print mode subscribes to session events, awaits the initial prompt and each remaining prompt, then prints final assistant text, or JSON events in JSON mode. An assistant error/abort in text mode or a thrown error produces failure status. The persistent message-end subscriber appends ordinary user, assistant and tool-result messages; custom messages have their own entries. SDK restoration builds context from the session manager rather than simply concatenating every stored event. Detailed memory semantics and revisions are left to the memory analyst. SRC-1: `cli/packages/coding-agent/src/modes/print-mode.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`.

### Selected forcing routes and guarantees

Four source-level forcing cases bound consequential claims:

1. **A hidden skill is explicitly invoked.** `disable-model-invocation` removes its description from implicit prompt selection but leaves the registered skill available to `/skill:name` and router-directed reads. Expansion reads and strips frontmatter, inserts the body into user text, and returns the original command if lookup or reading fails. Role filtering precedes collision resolution, but is not a filesystem access boundary. [RT-RTE-skill-delivery](#rt-rte-skill-delivery).
2. **Tools are disabled but a caller requests shell execution.** `noTools: "all"` creates an empty allowlist; a truthy other `noTools` value empties initial activation without creating that allowlist. Registry filtering covers builtin, custom and extension tools by name. It does not cover `session.executeBash`; the shipped RPC `bash` command reaches that method, or accepts an extension-supplied result/operations. Thus an empty model-tool grant is not a universal no-execution guarantee. This is a supported caller path, not merely a public type possibility. [RT-RTE-tool-grants](#rt-rte-tool-grants), [RT-RTE-user-bash](#rt-rte-user-bash).
3. **Compaction is canceled or supplied by an extension.** Overflow/threshold logic does not force the default summarizer in every case: a handler can cancel or provide compaction content. Accepted content is appended and reconstructed into model context; failure emits an event and returns false. [RT-RTE-context-compaction](#rt-rte-context-compaction).
4. **A skill is overwritten or the router update fails.** The repository importer requires `--overwrite` for a collision and tries rollback after mutation failure. That flag is not authenticated evidence of separate human approval. The official-library manager is a separate admission path with force/conflict, no-op and staged-swap branches. Neither gate covers direct shell/file writes. [RT-RTE-repo-import](#rt-rte-repo-import), [RT-RTE-library-update](#rt-rte-library-update).

The runtime owns name filtering at registry refresh; its strength is an **invariant over that registry construction**, requiring agent-core to dispatch only registered tools for model calls. It is not a deployment guarantee: local shell execution uses an OS child process and environment, and custom operations may execute elsewhere. No deployed container, OS permission set or remote executor isolation was supplied. Shell authority can implement writes or subprocesses outside the specialized import path. Native provider tools, independent extension model calls, manually manipulated agent state and remote backends were not exhaustively traced; universal coverage across them is not established. SRC-1: `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/tools/bash.ts`, `cli/packages/coding-agent/src/core/model-runtime.ts`.

Project trust is a separate resource-admission decision, not per-tool approval. The CLI resolver permits explicit overrides, extension decisions, saved decisions, defaults, then UI choice; without UI an unresolved ask returns false. Loader bootstrap forces untrusted project settings before obtaining that decision. This establishes wiring of a trust decision, not exhaustive proof about every resource consumer. Its declared scope includes project settings/resources, package installation and project extension execution. SRC-1: `cli/packages/coding-agent/src/core/project-trust.ts`, `cli/packages/coding-agent/src/core/resource-loader.ts`.

> This allows DisCo to load ${CONFIG_DIR_NAME} settings and resources, install missing project packages, and execute project extensions.
> --- `cli/packages/coding-agent/src/core/project-trust.ts`

### Construction and change admission

Creator guidance asks the agent to scope, ground, construct and verify a graph for a later Researcher. It separates project/managed destination choice, requests import approval and instructs Creator not to execute the downstream task. These are natural-language policies, not code-enforced role confinement. They reach behavior through [RT-BAP-creator-guidance](#rt-bap-creator-guidance). Installed skills reach subsequent model interpretation through [RT-BAP-skill-guidance](#rt-bap-skill-guidance). The importer and library manager admit durable instruction/capability changes; they do not change model weights. Dynamic extension registrations can change tools, prompt hooks and providers in the current runtime; the inspected registry refresh preserves name filtering on that route. Exhaustive extension installation, software-release admission and specialized workflow verification remain uninspected. SRC-1: `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`, `cli/packages/coding-agent/src/core/agent-session.ts`.

These mechanisms support an implemented path from constructed or installed guidance to later requests. They do not establish exercised self-improvement or improved scientific work. In particular, installation and prompt delivery do not show a later decision causally depending on an evidence-responsive change. Theory-builder or learning conclusions require the specialists' content and outcome evidence, not the runtime's graph labels.

## Shared records

### Components

#### RT-CMP-model-runtime
Label: ModelRuntime and selected provider model

The source-native ModelRuntime is a symbolic TypeScript request adapter in the checkout; the selected inference model is the distributed-parametric component behind its provider. Provider/model descriptors and auth/configuration reside in runtime configuration and session entries; parameter storage and provider internals are external and uninspected. The adapter calls the prepared provider with the selected model and context. SRC-1: `cli/packages/coding-agent/src/core/model-runtime.ts`, `cli/packages/coding-agent/src/core/sdk.ts`.

> return prepared.provider.streamSimple(prepared.model, context, prepared.options as SimpleStreamOptions);
> --- `cli/packages/coding-agent/src/core/model-runtime.ts`

Parameters changing during operation: uninspected — no provider internals or weight-update evidence. Exact parameter version pinned: not established; restored provider/model IDs and settings do not pin weights. Mutable endpoint resolving to another model: uninspected at the provider; local selection is demonstrably mutable through restoration/default fallback and runtime provider registration. Fixed weights, even if supplied externally, would not exclude adaptation through retained instructions. Implementation conclusion status: wired. Operation conclusion status: uninspected.

### Operative objects

none declared in this member

### Routes

#### RT-RTE-session-prompt
Label: Foreground session prompt

A CLI, RPC or SDK principal supplies text/images to AgentSession; session identity and mode select context. The owner is AgentSession until it calls external agent-core, which owns model/tool scheduling. Natural-language messages, symbolic tool schemas/settings and distributed-parametric inference cooperate. Extensions may consume or transform input before expansion and may override system context. Authentication failure rejects before the ordinary request. SRC-1: `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/sdk.ts`, `cli/packages/coding-agent/src/modes/print-mode.ts`.

> await this._runAgentPrompt(messages);
> --- `cli/packages/coding-agent/src/core/agent-session.ts`

- Immediate return: asynchronous completion to the caller; print mode emits final text or streamed JSON events and returns status.
- Later read-back: message-end persistence feeds SessionManager context restored by the SDK; branch/compaction projection determines what returns.
- Delegated visibility: provider receives converted context; extensions receive their event inputs; independent worker delegation is uninspected.
- Selection predicate: explicit model, eligible restored model with configured auth, then defaults; session branch supplies messages.
- Invalidation or expiry: abort, compaction, branch changes and model selection alter subsequent context; provider retention is uninspected.
- Activation or effect: source wires requests and tool execution; model compliance and resulting project effects are unobserved.
- Evidence limits: implementation only; external agent-core/provider internals and supplied execution traces were not inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Open-request mode; the caller supplies the problem, model proposes actions, code dispatches, extensions can intercept, and the user can abort. No answer oracle is established for ordinary conversational completion. Guarantee owner: session code. Enforcement: auth/model checks and prompt assembly. Guarantee strength: best effort for completion, not a correctness guarantee; remote services and agent-core must honor their APIs.

#### RT-RTE-tool-grants
Label: Tool registry grant filtering

SDK options initialize allow/exclude sets; AgentSession refresh filters builtin, SDK-custom and registered extension tool definitions and their active names before handing tools to the agent. This symbolic policy controls named model tools, not all host capabilities. SRC-1: `cli/packages/coding-agent/src/core/sdk.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`.

> const allowedToolNames = options.tools ?? (options.noTools === "all" ? [] : undefined);
> --- `cli/packages/coding-agent/src/core/sdk.ts`

> const isAllowedTool = (name: string): boolean =>
> (!allowedToolNames || allowedToolNames.has(name)) && !excludedToolNames?.has(name);
> --- `cli/packages/coding-agent/src/core/agent-session.ts`

- Immediate return: refreshed registry and active tool list, rather than a task answer.
- Later read-back: inapplicable — this is current-runtime configuration, not an accumulated retained artifact.
- Delegated visibility: selected schemas/executors are supplied to agent-core; registered extension tools use the same name predicate.
- Selection predicate: explicit allowlist if present, minus exclusions; default active tools otherwise include read/bash/edit/write.
- Invalidation or expiry: refresh/reload rebuilds registries; initial active selection and durable allowlist are distinct.
- Activation or effect: only allowed registry names are activated by this path; actual invocations are unobserved.
- Evidence limits: name filtering is not code identity verification or OS isolation; direct shell, extension-side effects and provider-native behavior are outside this enforcement point.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guarantee owner: AgentSession. Enforcement point: `_refreshToolRegistry`. Guarantee strength: invariant over the constructed registry. Required external contract: agent-core uses the installed registry for model tool dispatch. Runtime tool hooks emit `tool_call` only when handlers exist; without handlers they return undefined, so this is not universal approval. Dynamic tool admission is computational registration plus the predicate; a caller configures names, no per-definition human review is demonstrated. A same-name extension definition can replace a builtin definition in the registry. Recovery is rebuilding/reloading grants, not rollback of already executed effects. Operating mode: runtime configuration; answer oracle inapplicable, since no expected task answer is used.

#### RT-RTE-user-bash
Label: User and RPC bash execution

A supported RPC `bash` command emits `user_bash`. An extension can return a result directly, supply operations, or leave the default executor to run. AgentSession executes with cwd, configured shell prefix and cancellation, then records the result. Default operations spawn a local shell with environment and stream stdout/stderr; custom operations permit another executor. SRC-1: `cli/packages/coding-agent/src/modes/rpc/rpc-mode.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/tools/bash.ts`.

> operations: eventResult?.operations,
> --- `cli/packages/coding-agent/src/modes/rpc/rpc-mode.ts`

- Immediate return: BashResult to RPC caller, including output/status; events can stream updates.
- Later read-back: recorded bash messages enter session history; excludeFromContext can suppress their model-facing use.
- Delegated visibility: supplied operations receive command/cwd and execution controls; default shell gets its environment.
- Selection predicate: explicit caller bash request; extension result takes precedence over execution.
- Invalidation or expiry: cancellation aborts tracked executions; process effects need independent undo.
- Activation or effect: wired OS subprocess or custom executor; no deployed effect observed.
- Evidence limits: this method does not consult the model-tool allowlist; custom executor permissions and remote isolation remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guarantee owner: caller/extension chooses backend; local executor implements abort and optional tool timeout. Guarantee strength: no claimed guarantee of sandboxing. This is not a bypass of a claimed OS sandbox; it is evidence that tool grants do not define the entire execution envelope. Command mode is open-ended; caller proposes command, extension can intercept, shell supplies exit status but not a general answer oracle or correctness judgment.

#### RT-RTE-skill-delivery
Label: Skill selection and body delivery

The loader filters role-ineligible skills before name collisions; prompt formatting emits visible names, descriptions and locations. Explicit invocation searches the registered skills and reads a selected body into user-message text. Router-guided tool reads are another delivery route, not an enforced access boundary. SRC-1: `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`.

> Hidden skills remain registered for explicit invocation and router-directed reads.
> --- `cli/packages/coding-agent/src/core/skills.ts`

> const body = stripFrontmatter(content).trim();
> --- `cli/packages/coding-agent/src/core/agent-session.ts`

- Immediate return: XML-like description catalog in the system prompt, or expanded skill body and arguments in user text.
- Later read-back: accumulated installed skill changes can reach later sessions through loading and body reads; static shipped files alone are not read-back.
- Delegated visibility: model receives catalog or body; no independent subagent frame is established by this expansion.
- Selection predicate: role eligibility, collision resolution and visibility for catalog; explicit skill name for expansion; model interpretation for implicit relevance.
- Invalidation or expiry: reload/session reconstruction can change discovery; an unreadable or unknown explicit skill passes original text through.
- Activation or effect: delivery is wired; following the guidance is not observed or guaranteed.
- Evidence limits: role and visibility filters govern discovery, not arbitrary read/bash filesystem access; router internals were not exhaustively retraced here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guarantee owner: loader/formatter. Enforcement point: eligibility predicate and visible-skill filter. Guarantee strength: invariant for those outputs, policy for model use. Required external contract: a model interprets the supplied guidance. The model selects implicit relevance; explicit caller selection overrides implicit hiding, not role filtering of the registered set. No expected-answer oracle is involved. Open task requests remain open after expansion.

#### RT-RTE-context-compaction
Label: Session context compaction

Enabled settings plus same-model overflow or token threshold trigger code-owned preparation. An extension may cancel or provide the summary and kept-entry marker; otherwise the summarizer is called with model/auth/stream function. Appending compaction and rebuilding session context replaces active messages. SRC-1: `cli/packages/coding-agent/src/core/agent-session.ts`, `cli/packages/coding-agent/src/core/session-manager.ts`.

> this.sessionManager.appendCompaction(summary, firstKeptEntryId, tokensBefore, details, fromExtension, usage);
> --- `cli/packages/coding-agent/src/core/agent-session.ts:2153-2153`

- Immediate return: recovery decision plus compaction events, not a user task answer.
- Later read-back: stored summary and kept tail are projected into later requests and restored sessions; older summarized entries remain in session storage, not normal active context.
- Delegated visibility: summarizer or extension sees prepared history; foreground later sees the summary and kept entries.
- Selection predicate: enabled settings, overflow/threshold checks, branch preparation and firstKeptEntryId; extension cancellation/content precedes default summarization.
- Invalidation or expiry: newer compaction supersedes active projection; abort or failure leaves no successful new compaction from this attempt.
- Activation or effect: code replaces agent messages with rebuilt context; semantic preservation and improved performance remain unobserved.
- Evidence limits: preparation's exact token/tail partition and summarizer prompt internals were not inspected, preventing exact preferential-removal or fidelity claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Working-context control is history removal plus a retained summary/tail, not an isolated task frame: the summary can carry content across the boundary. Code triggers, extension vetoes or substitutes, and otherwise a runtime model produces prose. No reference answer checks preservation. Overflow recovery is bounded by one compact-and-retry attempt; a successful response over the window compacts without retry. Threshold compaction ordinarily waits for user continuation, while queued messages can cause continuation. Guarantee strength: best effort; owner: AgentSession; enforcement: compaction branches, append and rebuild. External model summarization must preserve needed meaning, which this source path does not certify.

#### RT-RTE-repo-import
Label: Repository skill import

Creator or another caller proposes a staged graph outside live roots. The Node importer validates portable files, skill metadata, license evidence, routing metadata and links; validates again after copying and installation; updates router/index through a subprocess. Endpoints are the external staged directory and managed repository skill/router/index paths. SRC-1: `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`.

> if (pathExists(targetDir) && !args.overwrite) throw new ImportError(`live repo skill already exists: ${targetDir}. Obtain separate overwrite approval, then rerun with --overwrite`);
> --- `cli/packages/coding-agent/src/disco/skills/verify-repo-skill/scripts/import_repo_skill.mjs`

- Immediate return: success text or error status; success advises a new Researcher session, not proof one occurred.
- Later read-back: installed graph and router/index can be loaded by later Researcher sessions through skill discovery/read paths.
- Delegated visibility: router updater subprocess receives library/template/routing arguments; downstream model receives selected guidance, not necessarily construction evidence in full.
- Selection predicate: staged skill identity plus metadata/routing checks; existing target requires overwrite flag; reserved library/router IDs reject.
- Invalidation or expiry: explicit later overwrite/update; mutation errors trigger restoration attempts for skill, router and index.
- Activation or effect: durable instruction admission is wired; later guidance use is unobserved.
- Evidence limits: structural/provenance checks do not prove task success or human authorization; all validator helper semantics and manual-unrouted alternatives were not fully inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission trigger: explicit import call. Proposal guidance: Creator scope/ground/construct/verify contract and its approval requests. Software rejects invalid inputs and unapproved-by-flag collisions; caller controls the flag, so the mechanism cannot authenticate separate approval. A lock helper serializes the ordinary entry; `--already-locked` checks an environment marker, not an adversarial security credential. Recovery backs up affected paths and retains transaction artifacts if rollback fails. Guarantee owner: importer; enforcement: validation/staging/catch branches; guarantee strength: best effort for multi-path recovery, not crash-atomic deployment. Required external contracts: functioning filesystem, lock helper and router updater. Operating mode: explicit construction/admission; no task answer oracle is established by license/link/routing checks. No weight changes occur on this route.

#### RT-RTE-library-update
Label: Official library install and update

The manager obtains a source snapshot, inventories it, enters a live lock, detects conflicts, stages skill trees/router/state and swaps them. Update requires existing managed state; install can no-op when state already exists. Same snapshot and unchanged digest conditions can return without swapping. SRC-1: `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`.

> if (conflicts.length > 0 && !force) throw new RepoSkillsLibraryConflictError(conflicts);
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

> if (actual.digest !== expected.digest) {
> throw new RepoSkillsLibraryError(`Staged official skill changed during validation: ${skillId}`);
> }
> --- `cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`

- Immediate return: install/update counts, source commit, no-op flag, issues and optional backup path.
- Later read-back: installed graph/router and durable management state govern later discovery and update decisions.
- Delegated visibility: router updater receives staged tree; downstream session sees loaded eligible skills, not the entire source snapshot.
- Selection predicate: inventory and previous management state; conflicts reject unless force; unchanged same-commit/digest conditions no-op.
- Invalidation or expiry: explicit update replaces managed content; local routing rows are merged and disabled router visibility is preserved.
- Activation or effect: staged content and management state are installed by sequential renames; runtime use remains unobserved.
- Evidence limits: snapshot acquisition/trust, every inventory helper and concurrent external direct writes were not exhaustively traced; no release authenticity or universal atomicity conclusion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software-driven after explicit caller request. Snapshot/inventory propose content; conflict code can reject, and caller force can override conflicts without a separate human approval check. Hash equality is a reference for integrity relative to inventory, not an answer oracle for scientific or operating correctness. Symbolic management state persists source/digest bookkeeping; natural-language skills persist as guidance. Recovery removes installed paths and restores backups on caught swap errors; restoration itself can fail, preserving recovery artifacts. Guarantee owner: manager; enforcement: lock/stage/digest/swap/catch; guarantee strength: best effort. Sequential renames do not establish process-crash atomicity. Operating mode: maintenance, not an automatic trace-fed improvement experiment.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Installed skill to model guidance

Consumer: later Creator/Researcher model request. Channel: catalog in system context, explicit expanded body in user content, or tool-read body. Force: natural-language instruction interpreted by the model, not runtime enforcement of every procedure. Horizon: current request and later sessions after installed material is reloaded. Source and evidence are [RT-RTE-skill-delivery](#rt-rte-skill-delivery), [RT-RTE-repo-import](#rt-rte-repo-import) and [RT-RTE-library-update](#rt-rte-library-update). SRC-1: `cli/packages/coding-agent/src/core/skills.ts`, `cli/packages/coding-agent/src/core/agent-session.ts`.

> Use the read tool to load a skill's file when the task matches its description.
> --- `cli/packages/coding-agent/src/core/skills.ts`

Installation changes available guidance; this establishes a live delivery capability, not observed activation or a causal benefit.

#### RT-BAP-creator-guidance
Label: Creator construction and deployment guidance

Consumer: Creator model during skill distillation. Channel: loaded `distill-ml-knowledge` body and linked procedures. Force: natural-language policy to scope/ground/construct/verify, obtain approvals, choose scope and hand off without performing downstream work. Horizon: construction run; resulting installed graph can govern later Researcher sessions through [RT-BAP-skill-guidance](#rt-bap-skill-guidance). SRC-1: `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`.

> Keep every root and sub-skill in one scope, show exact destinations and
> collisions, obtain import approval, and invoke the selected specialized or
> generic locked importer once with all top-level roots.
> --- `cli/packages/coding-agent/src/disco/skills/distill-ml-knowledge/SKILL.md`

The prose assigns proposal/verification work to Creator and approval to the user. This is doctrine/design, not evidence of compliance, an observed criticism/revision cycle, or authenticated per-content human admission in the importer. Detailed theory content and its criticism are not assessed here.

## Annotations

none
