---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Claude Code dynamic workflows runtime baseline: documented script orchestration, launch controls, worker effects and session-scoped replay."
run-id: AAS-2026-10-14-workflows-f9c2f80a3a94-01
reviewed-boundary: "workflows-2026-10-14"
---

# Claude Code dynamic workflows runtime report

## Runtime account

This report traces the workflow subsystem in the single frozen documentation capture, SRC-1. All positive runtime findings below are declared contracts, not inspected implementation or observed execution. The [boundary](boundary.md) excludes linked API specifications, actual workflow files, provider internals and enclosing permission implementation. The full capture was inspected. No execution evidence establishes activation, quality, cost savings or reliability.

### Ordinary invocation and decision ownership

A user asks Claude to audit route handlers with a workflow. The foreground Claude writes a JavaScript script, rather than deciding each subsequent worker assignment in conversation. The script is recorded under the session directory. Launch then passes through the enclosing session's permission path, whose human involvement depends on mode. The ordinary manual CLI route displays phases, offers raw-script inspection or an editor, and lets the user approve or cancel. The named-command route can instead load a bundled, project, personal or plugin script. [RT-RTE-workflow-launch](#rt-rte-workflow-launch) records these principals and alternatives.

Once admitted, the isolated runtime executes JavaScript control flow. In the page's example, a discovery worker returns structured file names; `pipeline()` calls an audit worker for each file; the body returns the truthy results. The script owns next-step selection and branching, while workers make model-mediated judgments and tool choices. Intermediate outputs reside in script variables rather than the foreground model context. This is orchestration isolation, not evidence that worker filesystem changes are isolated: agents can read, write and run commands. [RT-RTE-agent-orchestration](#rt-rte-agent-orchestration) records this loop and the distinction between worker outputs and external effects.

The foreground session stays responsive. `/workflows` lists runs or opens the sole run; phases expose counts, worker prompts, recent tool calls, results and any worker task list. Expanding a detail shows full prompt and result, but only the start of each listed tool result. The human can pause/resume, stop an agent or run, restart an agent, and save a script. The final workflow answer returns to the session. The bundled `/deep-research` contract adds search, fetching, cross-checking, voting and a cited report, but its executable script was not supplied. Its quality claim is separately retained in [RT-CLM-research-report](#rt-clm-research-report).

Recovery is consequential to both results and effects. A stalled worker restarts with its original prompt and without its previous transcript, but edits and spent tokens remain. A stopped or failed run can be relaunched using order-sensitive saved results; this is not a transactional undo or general exactly-once execution guarantee. [RT-RTE-agent-recovery](#rt-rte-agent-recovery) and [RT-RTE-run-replay](#rt-rte-run-replay) identify the different recovery decisions. Saving or editing a script admits reusable orchestration changes through [RT-RTE-script-admission](#rt-rte-script-admission). Memory-specific interpretation of retained results is left to the memory analyst.

### Material routes and forcing cases

Four documentation-supported cases challenge easy overgeneralizations:

1. **No universal human launch review.** Bypass mode starts immediately; auto mode prompts only on first launch, and not even then with ultracode enabled. Headless and SDK launches have no interactive prompt and can be approved by permission rules, a classifier, a hook or a host callback. Keyword provenance restrictions are not a ban on headless workflows. Before v2.1.210, even relayed keyword text could trigger a workflow. See [RT-RTE-workflow-launch](#rt-rte-workflow-launch).
2. **Script isolation is not effect isolation.** Direct shell/filesystem access and module loading are barred in the script, but its agents perform those tasks. A stalled retry retains prior edits while losing the transcript. The migration prompt's request for an isolated copy is not a universal runtime worktree guarantee. See [RT-RTE-agent-orchestration](#rt-rte-agent-orchestration) and [RT-RTE-agent-recovery](#rt-rte-agent-recovery).
3. **Failure is not necessarily a failed whole run.** `parallel()` and `pipeline()` continue with a `null` result, whereas an awaited direct stalled-agent call ends the run with an error. The example filters null entries, so a returned list need not account for every discovered file. Replay can rerun already completed later agents after an earlier failure. See [RT-RTE-agent-recovery](#rt-rte-agent-recovery) and [RT-RTE-run-replay](#rt-rte-run-replay).
4. **Advice and disable settings are not universal stop controls.** Size guidelines are model advice; the large-run warning is advisory and suppressed by ultracode. Runtime agent/list caps are separate. Disabling workflows removes launch surfaces but an existing run continues. See [RT-CLM-runtime-limits](#rt-clm-runtime-limits) and [RT-RTE-workflow-launch](#rt-rte-workflow-launch).

These are forcing cases in the declared contract, not experimental tests. Direct provider calls, undisclosed host or worker bypass paths, full SDK hook semantics and actual bundled/plugin bodies remain uninspected outside this capture. No universal security or failure-recovery conclusion extends to them.

### Controls, grants and guarantee coverage

The **capability surface** consists of JavaScript coordination, model-backed agents and agents' tools. The **current grant set** is supplied by session permissions and available tools; `/deep-research` requires WebSearch, and a script's read permission is required to launch it. The **deployed isolation envelope** is only described as an isolated script environment plus session tool checks and sandboxing. Concrete sandbox configuration, grants and enforcement code are not supplied (SRC-1, `Ask for a workflow in your prompt`, `Approve the plan before it runs`, `How a workflow runs`, `Behavior and limits`).

| Load-bearing contract | Owner and claimed enforcement point | Strength and coverage | Alternate path / external dependency | Conclusion statuses |
| --- | --- | --- | --- | --- |
| Launch permission | Enclosing Claude Code; Workflow call evaluation and mode-dependent UI | policy; applies to Workflow launch, not per-result correctness or per-edit human review | Auto, bypass, hooks and host callbacks can approve without that UI; exact permission semantics external | doctrine conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected |
| Script access and isolation | Claude Code launch read check; workflow runtime environment | invariant; permitted script-file reads, no script filesystem/shell or `import()` | Agents retain tool access under session permissions; actual sandbox internals external | doctrine conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected |
| Resource ceilings | Workflow runtime at scheduling/list admission | invariant; 4,096 items per fan-out call, 1,000 total agents, configurable concurrency | Guidelines and warnings are not ceilings; ultracode's removal of the session Agent-tool concurrency limit is a different path | doctrine conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected |
| Replay and duplicate-run exclusion | Claude Code result tracker and relaunch check | protocol; same-session replay and refusal while stopped-run agents have not exited | Background/cloud/session resume have distinct persistence contracts; missing saved results causes error, fresh session starts over | doctrine conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected |
| Save-path protection | Claude Code save-location symlink check | invariant; project checks `.claude`, workflow directory and target; personal checks only target | Personal ancestor symlinks intentionally allowed; before v2.1.216 links were followed | doctrine conclusion status: claimed; implementation conclusion status: uninspected; operation conclusion status: uninspected |

Evidence for these contracts and their countercases is retained in the corresponding records below. None establishes a deployment guarantee across arbitrary host configurations.

### Models, coordination and bounded performance claims

[RT-CMP-claude-model](#rt-cmp-claude-model) separates model mediation from the symbolic next-step owner. Agents may use a stage-specific model; otherwise model selection falls back to session configuration according to external subagent rules. Organization allowlists can substitute a model, so a script's requested name does not pin the executing model.

SRC-1, `Prompt caching in a fan-out`, describes matching on model, effort, agent type, tools, schema and working directory to share the tools/system-prefix cache. Matching siblings may be held until the first response begins, with a 5,000 ms default maximum hold and a zero setting to disable it. Cache TTL defaults to five minutes, optionally one hour with higher API write rates. These are coordination and billing contracts, not measured speedups. The cache prefix is not shared task progress or a shared worker transcript. Token usage is displayed per agent; paid-plan/API and host availability, rate limits and model services remain external dependencies. No performance or monetary bound follows from an agent-count cap alone.

## Shared records

### Components

#### RT-CMP-claude-model
Label: Claude model mediation

Source-native identity: foreground Claude authoring the workflow and Claude models used by workflow subagents. Representational form: distributed-parametric model behavior; prompt and returned text/JSON are separate representations. Storage substrate: provider-held parameters, opaque in SRC-1. Foreground exact model and provider parameter details are uninspected.

Parameters changing during operation: uninspected; the page describes orchestration, not training or parameter updates. Exact version pinned: uninspected; no immutable model revision is supplied. Mutable endpoint resolution: uninspected at provider level; configuration can change selection and organization policy can substitute a requested model, so requested identity is not a fixed execution identity. No fixed-weight or no-learning conclusion follows.

Evidence: SRC-1, `Cost`:

> When your organization's [`availableModels` allowlist](/docs/en/model-config#restrict-model-selection) blocks a model the script requests for an agent, that agent runs on a substituted model instead, following the same [substitution rules as subagents](/docs/en/sub-agents#choose-a-model).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Operative objects

#### RT-OBJ-workflow-script
Label: Workflow script

Source-native identity: the generated run script and saved `.js` workflow. Representational form: symbolic JavaScript body and literal `meta` object consumed by loader/runtime. Embedded natural-language worker prompts are separately interpreted by models, as described in [RT-RTE-agent-orchestration](#rt-rte-agent-orchestration); storing prompts inside JavaScript does not make their task meaning fixed-rule code.

Storage substrate: run file under the session's `~/.claude/projects/` directory; reusable copies under project or personal `.claude/workflows/`, or plugin workflow directories. Actual filenames, storage format beyond `.js`, loader code and shipped scripts are uninspected. The script determines order, branching, fan-out and final return; permissions still determine available effects.

Evidence: SRC-1, `How a workflow runs`:

> Every run writes its script to a file under your session's directory in `~/.claude/projects/`. Claude receives the path when the run starts, so you can ask for it. You can open that file to read the orchestration Claude wrote, diff it against a previous run's script, or edit it and ask Claude to relaunch from the edited version.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### RT-OBJ-agent-results
Label: Agent results

Source-native identity: intermediate agent results and saved run results. Representational form: prose or schema-constrained JSON returned by workers, JavaScript values during orchestration, plus opaque persistence encoding. Storage substrate: script variables during execution; session directory for local saved results; cloud conversation history for cloud results. Transcript persistence and serialization internals are uninspected.

Consumer: the script obtains worker return values; relaunch can deliver saved values instead of executing a worker; the terminal script output returns to the foreground session. This record identifies runtime state without assigning memory-revision properties.

Evidence: SRC-1, `How a workflow runs` and `Resume after you leave the session`:

> The runtime tracks each agent's result as the run progresses, which is what makes a run [resumable](#resume-after-a-pause) within the same session.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> In a [cloud session](/docs/en/claude-code-on-the-web), Claude Code also saves the run's results with the session's conversation history, which survives when the session's VM is reclaimed. When you [reopen such a session](/docs/en/claude-code-on-the-web#environment-expired) and ask Claude to relaunch the workflow, completed agents still return their saved results.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Routes

#### RT-RTE-workflow-launch
Label: Workflow launch

Endpoints and progression: human or host task input → foreground Claude script generation or named-script loading → Workflow permission evaluation → background runtime. Owner: Claude proposes orchestration; enclosing Claude Code or its configured host admits launch; in manual CLI mode the human can veto. Operating mode: open task requests, not a specified experimental curriculum. Answer oracle: inapplicable — launch consent evaluates permission, not expected task correctness.

Entry routes include direct requests, human-origin keyword prompts, session ultracode, `/deep-research`, saved commands and plugin commands. The keyword can operate in CLI, IDE, Remote Control and SDK input stamped `{ kind: "human" }`; it does not opt in via `-p`, unstamped SDK input, scheduled tasks or relayed webhook/PR text on versions from v2.1.210. The page does not thereby forbid those surfaces from making Workflow calls. Automatic ultracode can plan several successive workflows for one request and is substantive-task dependent. Project saved commands shadow personal names; nested project selection prefers the closest working-directory ancestor. Plugins use namespaced commands.

Runtime-client controls: review script and phases, approve/cancel, reusable named consent, permission rules, host/hook approval, disable settings. The read-permission condition applies to script files, including an external directory needing `/add-dir` or a Read allow rule. Starting a workflow is not per-content or per-edit approval. Disabling removes commands and opt-in controls but does not stop an existing run.

- Immediate return: launch starts a background run, publishes progress and gives Claude the run-script path; eventual terminal answer returns to the session.
- Later read-back: named script and persisted named/auto consent can govern later launches; saved-script route details are in [RT-RTE-script-admission](#rt-rte-script-admission).
- Delegated visibility: workers receive script-computed prompts and tools under session rules, not the launcher's identity as an automatic authorization for every action.
- Selection predicate: explicit command/request, human-origin keyword, or foreground Claude's substantive-task decision with ultracode; named loading follows scope/namespace precedence.
- Invalidation or expiry: session ultracode ends with the session unless settings persist it; consent and disabled settings have described longer horizons, but complete revocation semantics are uninspected.
- Activation or effect: claimed launch of orchestration; child tool actions are separately permission-evaluated, with selected subagent modes determined by external rules.
- Evidence limits: doc-grounded; full permission evaluator, hooks, host callbacks, loader and mode inheritance are outside SRC-1.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Approve the plan before it runs`:

> | Auto | First launch only. Any **Yes** records consent in your user settings, and later launches start without prompting. Skipped entirely when ultracode is on |
> | Manual, accept edits | Every run, unless you've selected **Yes, and don't ask again** for that workflow in this project |
> | Bypass permissions | Claude Code doesn't prompt you. The run starts immediately |
> | `claude -p`, Agent SDK | Claude Code doesn't prompt you |
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> In `claude -p` and the Agent SDK, Claude Code never shows this prompt. It runs the Workflow tool call through the same [permission evaluation](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) as the rest of the session, so deny rules, ask rules, and `dontAsk` mode apply to the launch as they apply to every tool call.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### RT-RTE-agent-orchestration
Label: Agent orchestration

Endpoints and progression: JavaScript `agent()` prompt/options → subagent model and tools → prose/JSON value → script variables, branching and terminal return. `pipeline()` fans out by item; `parallel()` waits for a set of tasks. Owner: runtime executes script order and concurrency; model-backed worker owns its task judgments. Representations: symbolic orchestration and schemas; natural-language task prompts and prose; distributed-parametric models in [RT-CMP-claude-model](#rt-cmp-claude-model). Each schema is checked before launch for provable contradictions; contradictory calls fail without starting a worker. Invalid structured outputs have five attempts by default, adjustable via `MAX_STRUCTURED_OUTPUT_RETRIES`; failure includes the last validation error. Shape checking does not establish factual validity.

Working-context control: runtime keeps intermediate results in variables in a separate environment rather than sending each into foreground context. Worker task frames expose prompts/results through progress UI; final return crosses back. Exact worker context construction, inherited instructions and whether additional summaries reach the foreground are uninspected. The stack-frame analogy fits selected input and returned value; it breaks at persistent file effects, UI access and saved results, which outlive a worker frame. Generated prompt text is marked script-computed, not a human request in auto classification.

- Immediate return: `agent()` returns a result value; pipeline/parallel collect outputs; workflow returns its script-selected terminal value to the foreground.
- Later read-back: saved worker values may reenter script execution through [RT-RTE-run-replay](#rt-rte-run-replay); ordinary same-run variable use is not retained read-back by itself.
- Delegated visibility: workers receive their computed prompt and selected options; sibling prompt-prefix caching does not establish sibling result visibility unless the script passes results onward.
- Selection predicate: JavaScript control flow and input list determine workers; explicit schema, label, model and other options parameterize calls.
- Invalidation or expiry: current-run variables have runtime scope; saved-result invalidation follows replay ordering and prompt divergence.
- Activation or effect: claimed worker reasoning/tool actions plus script-selected return; filesystem/shell effects occur via workers, not direct script access.
- Evidence limits: example and documented APIs only; no actual audit, code or complete subagent/API specification supplied.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `How a workflow runs`, `Behavior and limits`, `What the saved script looks like`:

> The workflow runtime executes the script in an isolated environment, separate from your conversation. Intermediate results stay in script variables instead of landing in Claude's context.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> | No direct filesystem or shell access from the workflow itself | Agents read, write, and run commands. The script coordinates the agents |
> | No module loading: a script that contains `import()` fails before the run starts | The script body is plain JavaScript. Put work that needs a library in an agent's task |
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> In [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode), the prompt your script passes to `agent()` doesn't count as a request from you when the classifier reviews that subagent's actions, because Claude Code marks it as text the script computed.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### RT-RTE-agent-recovery
Label: Agent recovery

Endpoints and progression: runtime detects stalled output or human requests restart → fresh attempt with same prompt → result, null or error. Owner: runtime retry logic; human can restart or stop. Retry decisions are liveness control, not criticism of task content. Separate usage-limit policy pauses interactive subscription runs only when auto-continue is enabled, reset is within 24 hours and the run has not already waited twice; background, Remote Control, team teammate, headless and SDK runs fail the affected agent instead. This wait behavior requires v2.1.271; earlier versions fail. A paused run admits no new agents and resumes after reset.

- Immediate return: ongoing progress/retry detail; successful value, null in fan-out failure handling, or error terminating a directly awaited stalled call.
- Later read-back: external file changes survive retry; saved result handling on relaunch is recorded in [RT-RTE-run-replay](#rt-rte-run-replay).
- Delegated visibility: restarted worker receives original prompt but no stalled-attempt transcript; persistent edited files can still be accessible via tools.
- Selection predicate: no-output stall threshold excludes time spent waiting on tools or usage reset; `r` also restarts; usage waiting uses the distinct eligibility conditions above.
- Invalidation or expiry: maximum five restarts including manual restarts, six attempts total; per-call `stallMs` or environment controls window; streaming idle timeout is a distinct possible cause.
- Activation or effect: retry can repeat work against files already changed; no rollback of tokens or edits is claimed.
- Evidence limits: timeout enforcement, API error interactions and side-effect idempotence uninspected; source's general null description and specific direct-await stalled error behavior are retained without inventing full exception semantics.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `When an agent stalls and restarts`:

> The new attempt starts without the stalled attempt's transcript. Files the stalled attempt already changed stay changed, and the tokens it spent stay in the run's total.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> * **Inside [`parallel()` or `pipeline()`](#what-the-saved-script-looks-like)**: the run carries on with `null` in place of the agent's result
> * **Awaited directly**: the run ends with the error
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### RT-RTE-run-replay
Label: Run replay

Endpoints and progression: paused-run resume or Claude relaunch of stopped/edited run → runtime replay in original start order → cached earlier values or fresh worker calls → terminal output. Owner: Claude Code result tracker. Human requests relaunch; Claude issues it. The first changed prompt or failed prior agent invalidates that slot and all later-started agents, even completed ones. Still-running agents restart; whole-run stop does not count them failed, whereas stopping one agent does. Changed ordering also creates prompt divergence. This selection is recovery logic, not semantic candidate comparison; answer oracle is inapplicable because no expected task answer is used.

No duplicate copy is admitted while stopped agents remain alive. Stop re-signals processes on a second stop. Backgrounding and move-to-background exit replay and continue; ordinary exit stops tasks. Resuming the same local session permits saved results to replay; fresh sessions start new runs. Cloud results survive VM reclaim in conversation history. Missing saved results cause `nothing to resume`, not silent restart. Replay is session-associated, not proof of deterministic tool effects or complete crash consistency.

- Immediate return: completed valid prefix returns saved values; fresh suffix executes again, eventually returning a new terminal output or error.
- Later read-back: stored [RT-OBJ-agent-results](#rt-obj-agent-results) reach script invocations in the same or resumed session, including cloud reopening.
- Delegated visibility: a cached slot does not run a worker; a rerun receives the current prompt and tool-accessible state, not an established rollback snapshot.
- Selection predicate: ordered prior agent starts, completion/failure state and first prompt mismatch determine prefix reuse and suffix recomputation.
- Invalidation or expiry: failed or differing slot invalidates suffix; missing storage blocks relaunch; retained-result lifetime beyond session persistence is uninspected.
- Activation or effect: saved values can drive later branches; rerun workers can repeat external effects. Exercised dependency is unobserved.
- Evidence limits: prompt matching internals, option/model-change invalidation and atomic persistence are not specified in the capture.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Which agents run again`:

> * **Completed**: returns its saved result. The first agent whose prompt differs from the previous run, because you edited the script or an earlier agent returned something different, runs again, and so does every agent after it, even ones that completed.
> * **Still running when you stopped**: starts over. Stopping the whole run doesn't count any agent as failed.
> * **Failed**: runs again, and so does every agent that started after it, even ones that completed. Stopping one agent alone, by selecting it in [`/workflows`](#watch-the-run) and pressing `x`, counts as failing.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### RT-RTE-script-admission
Label: Script admission

Endpoints and progression: generated script → human save action or human/Claude edit → filesystem workflow artifact → reload/named invocation or edited-run relaunch. Owner: human chooses save location and can author edits; Claude can author on request; Claude Code checks location, metadata and syntax and resolves command scope. Proposed change: reusable orchestration, embedded tasks and invocation inputs, not necessarily an update to the enclosing runtime machinery.

Admission and veto: save dialog commits the chosen copy; direct file edits need no documented separate per-content approval; subsequent launch follows [RT-RTE-workflow-launch](#rt-rte-workflow-launch). Loader demands first-statement plain literal `meta` with name/description; nonliteral metadata drops autocomplete, while body syntax errors are reported on invocation. Save protection refuses project ancestor/target symlinks but allows personal ancestor symlinks. Rollback/recovery: human can edit back and reload or edit a run and relaunch; no versioned automatic rollback is described. Plugin distribution puts workflow scripts under plugin `workflows/` or a manifest-selected path; its separate installation/admission internals are uninspected.

Guidance: page recommends loading `/workflow-authoring` before edits, available from v2.1.248, and `/reload-skills` to run edited saved copies in the current session. The full authoring reference is outside the capture. Size guideline is advisory input to Claude's proposal, not a file constraint. Script and metadata persist; whether rationale or criticism persists is uninspected. Operating mode: open user requests and reusable commands; no mandatory comparison experiment. Answer oracle: inapplicable — structural loader checks and user consent are not expected task outcomes.

- Immediate return: saved command becomes invocable; edits take effect through reload or edited-run relaunch, subject to loader/runtime checks.
- Later read-back: project commands reach future project sessions and clones; personal commands reach future projects for that user; plugin commands reach installed consumers. `args` supplies structured per-invocation input without modifying saved code.
- Delegated visibility: script authors determine prompts and data forwarded to workers; plugin distribution shares symbolic orchestration rather than guaranteeing identical model behavior.
- Selection predicate: named command, nearest project directory, project-over-personal precedence and plugin namespace select reusable script; user selects save location.
- Invalidation or expiry: reload rereads directories; modified prompt/order changes replay reuse; exact command retirement and plugin update semantics are uninspected.
- Activation or effect: admitted script can control later worker orchestration; loading or saving alone does not establish exercised behavior or improvement.
- Evidence limits: doc-grounded checks; actual saved files, authoring reference, plugin machinery and file-edit permissions uninspected. No formulated theory criticism or autonomous self-improvement is inferred from editability.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Save the workflow for reuse`, `Edit a saved script`:

> * Project location: Claude Code refuses if `.claude`, `.claude/workflows`, or the target file is a symlink.
> * Personal location: Claude Code refuses only if the target file itself is a symlink, so a `~/.claude` directory managed by a dotfiles tool still works.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> To run the edited version in the current session, run [`/reload-skills`](/docs/en/commands#all-commands) to re-read the workflow directories, then run `/<name>` again.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> * **Timestamps and randomness**: Claude Code makes `Date.now()`, `Math.random()`, and a no-argument `new Date()` throw inside the script, so that a [relaunched run](#resume-after-a-pause) repeats the same `agent()` calls. Pass a timestamp in through `args` instead.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Claims

#### RT-CLM-runtime-limits
Label: Runtime limits

Claimed operation: runtime rejects lists over 4,096 per `parallel()`/`pipeline()` call, limits total spawned agents to 1,000 and defaults to up to 16 concurrent agents, reduced with available CPUs. A 1–256 environment setting changes concurrency from v2.1.269. These local limits are distinct from the session Agent-tool concurrency limit removed by ultracode. No precise wall-clock or money ceiling is established. Advisory size guidelines and large-run warnings cannot enforce a workload bound.

Source: SRC-1, `Behavior and limits`, `Set a size guideline`, `Cost`. Guarantee owner: workflow runtime; strength: invariant for explicit resource caps, policy for authoring advice; actual enforcement uninspected.

> | Up to 4,096 items in a single `parallel()` or `pipeline()` call: the runtime rejects a longer list with an error | A silent cap would drop part of the workload without telling the script |
> | 1,000 agents total per run | Prevents runaway loops |
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

> A size guideline tells Claude how many agents to aim for when it writes a dynamic workflow. Claude Code sends the guideline to Claude as advice, not a cap, so a prompt that calls for a different scale still overrides it.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### RT-CLM-research-report
Label: Research report

Claimed operation: explicitly invoked `/deep-research` fans out searches, fetches and cross-checks sources, votes on claims and returns a cited report with failed cross-check claims filtered. Uncheckable claims after rate limits/API errors are marked unverified rather than refuted. Source: SRC-1, `Bundled workflows`, `Read the report`. Required external contract: WebSearch availability. Owner: bundled script and model-backed workers, whose actual identities, thresholds and prompts are uninspected. Guarantee strength: best effort for cross-checking as described, not an invariant of factual correctness.

The page's general claim of a more trustworthy result than a single pass is a design assertion with no comparative run evidence. Neither voting nor citations establish an independent answer oracle. Detailed diagnosis/admission roles and epistemic warrants require the actual script or specialist interpretation; this claim does not stand in for those missing internals.

> When the verifier agents can't check a claim, such as after a rate limit or API error, the report lists that claim as unverified instead of counting it as refuted.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-script-control
Label: Script control

Consumer: workflow runtime and named-command loader. Channel: session-run JavaScript file or saved/plugin script selected at invocation. Force: symbolic execution determines calls, branching, accumulation and returned value under runtime restrictions; embedded task text has model-mediated force at the separate worker consumer. Horizon: current run, replay rounds, or future sessions consuming saved scripts. Evidence: SRC-1, `When to use a workflow`, and [RT-OBJ-workflow-script](#rt-obj-workflow-script), [RT-RTE-script-admission](#rt-rte-script-admission).

> A workflow moves the plan into code. With subagents, skills, and agent teams, Claude is the orchestrator: it decides turn by turn what to spawn or assign next, and every result goes into a context window. A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### RT-BAP-agent-prompts
Label: Agent prompts

Consumer: workflow subagent model, including [RT-CMP-claude-model](#rt-cmp-claude-model). Channel: script-computed `agent()` prompt and passed input. Force: natural-language interpreted task guidance; not direct human authorization in auto mode and not proof of compliance. Horizon: worker attempt, repeat attempts from the same prompt, and future invocations if prompts persist in a saved script. Evidence: SRC-1, `What the saved script looks like`, retained at [RT-RTE-agent-orchestration](#rt-rte-agent-orchestration). External effects still depend on tool permissions. Delivery is documented; exercised task obedience is unobserved.

## Annotations

none
