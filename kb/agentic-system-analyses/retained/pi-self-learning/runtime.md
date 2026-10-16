---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "pi-self-learning runtime baseline: host-triggered reflection, memory admission, maintenance and future-turn injection at the frozen extension revision."
run-id: AAS-2026-10-15-pi-self-learning-1a318610d4b1-01
reviewed-boundary: e0d76a93195b11b688ca71da8a8b5700c6541542
---

# pi-self-learning runtime report

## Runtime account

### Boundary and ordinary invocation

This report traces the complete extension package, not the enclosing pi agent. Evidence is inspected implementation and declared design in SRC-1, principally `extensions/self-learning.ts`, with packaging in `package.json` and operator claims in `README.md`. All of the extension was read, along with the README, package metadata, agent guidance and example settings. These are already registered paths; no source was added. The supplied [boundary](boundary.md) contains no execution traces or experiments. Operation, model compliance and prevention benefit remain unobserved throughout.

The consequential claimed work is mistake prevention through retained session reflections, not weight training. Package metadata loads one TypeScript extension. Its default export registers `agent_end`, `before_agent_start` and nine commands. Installation, copying the extension and settings-based loading all reach that same registration function; they are not separate agent loops (SRC-1, `package.json`, `README.md`, `extensions/self-learning.ts`).

An ordinary implemented invocation proceeds as follows ([RT-RTE-task-reflection](#rt-rte-task-reflection), [RT-RTE-context-injection](#rt-rte-context-injection)):

1. The host finishes an agent task and invokes `agent_end` with messages and an extension context. The host, not this package, owns the foreground agent, tools, session identities and task completion event.
2. Code reloads global and project settings, consults a branch custom-entry toggle, and checks automatic-reflection enablement, latest assistant `stopReason === "stop"`, and the module-wide redistill suppression deadline. This is a stop-reason predicate, not independent verification that the user's task succeeded.
3. `reflectNow` reloads settings, filters user-abort messages from the current branch and takes the last configured number, default eight. It converts and serializes them through host functions. A separate bounded scan extracts up to eight error-tool permission/blocking signals, excluding user cancellations.
4. Code chooses a model/auth pair. The configured model wins when found and authenticated; otherwise it tries `ctx.model`. It sends a separate user-message-only completion request with the embedded mistake/fix prompt, selected conversation and constraint signals. The reflection call does not receive the whole foreground context, injected memory policy or a tool schema.
5. Text output is parsed directly or by extracting a JSON object; one repair completion is attempted if parsing fails. A nonempty mistakes or fixes list suffices. Code appends a dated Markdown entry, updates the canonical scored index, renders core and long-term files, attempts Git commits and retains a short process-local note. No per-content human approval or correctness oracle intervenes.
6. The hook may display the daily path; automatic exceptions are swallowed. On a later `before_agent_start`, the enabled extension returns hidden custom-message content from recent notes and selected files, and appends a memory consultation policy to the existing system prompt. The host owns consumption and subsequent actions. Delivery is wired; changed foreground behavior is not observed.

Settings handling has a material limit: global and project objects are deep-merged with each other, but `DEFAULT_CONFIG` is only the fallback when the entire `selfLearning` value is missing. A partial `selfLearning` object is not deep-merged with defaults; missing nested fields can therefore fail at dereference. The full example configuration does not demonstrate safe partial configuration (SRC-1, `extensions/self-learning.ts`, `docs/example-settings.json`).

> async function reflectNow(turnLabel: string, ctx: ExtensionContext): Promise<ReflectNowResult> {
>   const settings = loadMergedSettings(ctx.cwd);
>   const config = getSetting(settings, "selfLearning", DEFAULT_CONFIG) as SelfLearningConfig;
> --- `extensions/self-learning.ts`

Persistent identity is a resolved project/global filesystem root, dated files and normalized text keys, not a per-agent memory namespace. Project roots prefer the nearest ancestor `.pi/settings.json`, then `.git`; a global root can span repositories. Branch entries control enablement, but disk memory and module-level notes are not branch-partitioned. There is no extension-level queue or lock around synchronous filesystem writes separated by asynchronous model calls. Host callback concurrency and cross-process coordination are external/unobserved (SRC-1, `extensions/self-learning.ts`).

### Material alternate routes and forcing cases

Four source-inspected cases qualify the apparent guarantees. They are code-path analyses, not executed tests.

**Completed-turn gate versus manual reflection.** The automatic hook checks stop reason and a five-minute redistill suppression window. `/learning-now` calls `reflectNow` directly and therefore bypasses both gates and automatic enablement, though it still checks the branch/config enabled flag and filters user-abort messages. Filtering does not prove every retained assistant message is complete: `isUserAbortMessage` specifically recognizes aborted assistants and cancellation tool results. Completed-turn-only language is justified for the automatic hook's predicate, not all manual or historical input (SRC-1, `extensions/self-learning.ts`; [RT-RTE-task-reflection](#rt-rte-task-reflection)).

**Strict mode versus actual enforcement.** `instructionMode: strict` constructs a MUST instruction; it neither intercepts answers nor verifies file reads. `off` removes the policy but does not disable bundled memory. `context.enabled: false` prevents file bundling and policy, yet recent process-local notes can still be injected while learning remains enabled. Thus neither "strict enforces consultation" nor "context disabled removes all memory delivery" is a hard runtime guarantee (SRC-1, `extensions/self-learning.ts`; [RT-BAP-memory-policy](#rt-bap-memory-policy), [RT-RTE-context-injection](#rt-rte-context-injection)).

**Model override versus selected model.** `/learning-model` validates and appends a branch model entry, but reflection and redistill pickers read configured settings/current model, not that entry. Status explicitly reports the branch override as ignored. `/learning-model-global` actually rewrites global settings, subject to project override. Redistill constructs at most one authenticated candidate: if the configured candidate is usable it returns immediately. A later failed completion does not trigger current-model fallback. Fallback is selection-time missing-model/auth recovery, not general request-failure recovery (SRC-1, `extensions/self-learning.ts`; [RT-RTE-runtime-controls](#rt-rte-runtime-controls), [RT-CMP-reflection-model](#rt-cmp-reflection-model)).

**Disablement and preview versus maintenance.** Monthly summary and redistill commands do not check `isLearningEnabled`; the toggle is not a universal maintenance veto. Redistill requires global mode, prompts for coarse confirmation only above 200 entries without `--yes`, and accepts automatic model rewrites thereafter. `--dry-run` skips the final rewrite/commit block but calls `loadCoreIndex` first; migration/default loading can create a missing core file. Its "without writing files" description is therefore narrower in code. An invocation sets the suppression deadline even before argument validation or cancellation (SRC-1, `extensions/self-learning.ts`; [RT-RTE-core-redistill](#rt-rte-core-redistill), [RT-RTE-month-summary](#rt-rte-month-summary)).

### Guarantees, authority and isolation

| Scoped guarantee | Owner and enforcement point | Strength and coverage | External contract and limits | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|---|
| Automatic reflection follows a stop-ended event | Extension `agent_end` guard | invariant for this automatic path; manual command bypasses it | Host must supply truthful messages/stop reasons; task success is not checked | wired | uninspected |
| Accepted reflection contains nonempty string content | Extension `parseReflection` and repair admission | invariant at reflection admission; either array may be empty; older keys accepted | JSON parsing is local; factuality, maximum array length and prevention quality are model requests, not validated properties | wired | uninspected |
| Historical consultation in strict mode | Extension constructs policy; foreground model interprets it | policy; covers returned system-prompt instructions, not tool/answer interception | Host must apply returned prompt; model must comply; direct completions use their own prompts | wired | uninspected |
| Automatic reflection errors do not propagate from the protected body | Extension hook `try/catch/finally` | best effort, not universal non-blocking operation | Pre-try config access, working-message cleanup, synchronous I/O and host behavior remain outside a blanket guarantee; awaited work can delay callback return | wired | uninspected |
| Memory is Git-backed | Extension `ensureGitRepo`/`gitCommit` | best effort and configurable; daily/core/monthly/redistill call sites attempt commits | Git executable, writable paths, identity and successful commits required; initialization/commit results often ignored; writes are not a transaction | wired | uninspected |

Evidence for these qualifications is retained in the route and authority records below and in these enforcement passages (SRC-1, `extensions/self-learning.ts`).

> if (!isLearningEnabled(config, ctx) || !isAutoReflectionEnabled(config)) return;
> if (!didCompleteFullTurn(event.messages)) return;
> if (Date.now() < skipAutoReflectionUntil) return;
> --- `extensions/self-learning.ts`

> } catch {
>   // Never break normal flow
> } finally {
> --- `extensions/self-learning.ts`

> runGit(root, ["commit", "-m", message], GIT_COMMIT_TIMEOUT_MS);
> --- `extensions/self-learning.ts`

The capability surface is extension-level filesystem access, direct completion calls through registry credentials, host custom-entry writes, UI access and synchronous Git subprocesses. Current configured grants, actual credential scopes and deployed process isolation are not supplied. Permission-denial text is training input, not an approval mechanism. The reflection requests offer no tools; the enclosing agent's shell/provider-native tools and other extensions remain host responsibilities. This package does not sandbox those alternate paths. Git is invoked directly from extension code rather than through an enclosing model's tool approval UI. No new capability plugin, product-code update or production-machinery installation is admitted by the inspected extension; its model-generated changes target memory. Manual installation of a new package revision is outside the retained-memory loop (SRC-1, `extensions/self-learning.ts`, `package.json`, `README.md`).

Recovery is local and uneven: malformed reflection gets extraction/one repair; invalid results are skipped; manual commands report diagnostics; automatic skips are mostly silent. Model waits have explicit timeout races, but no abort signal is passed to `complete`, so timeout is not proven provider cancellation. Redistill stages chunk rewrites in memory before final multi-file writes; it has no automatic rollback after partial filesystem failure. Git history can afford manual recovery if commits succeeded, but no restore command is shipped. No evaluator or supplied run establishes accuracy, successful integration or improved capacity (SRC-1, `extensions/self-learning.ts`, `AGENTS.md`, `package.json`).

## Shared records

### Components

#### RT-CMP-reflection-model
Label: Reflection and maintenance completion model

Source-native identity: selected `model` from `pickReflectionModel` or `buildRedistillModelCandidates`. Representational form: distributed-parametric model behind an external completion API; storage substrate: provider/service, inaccessible in SRC-1. The extension stores symbolic provider/id references in settings and branch entries, not weights. Parameters are not updated by any inspected extension route; provider-side mutation is uninspected. Exact version is not pinned by the package: configured/current model references may select different models over time, and whether an endpoint aliases changing weights is unresolved externally. Reflection, repair, monthly summary and redistill use this component. No embedding model is called (SRC-1, `extensions/self-learning.ts`).

> const configured = registry.find?.(fromConfig.provider, fromConfig.id) ?? getModel(fromConfig.provider, fromConfig.id);
> --- `extensions/self-learning.ts`

> diagnostics.push(`selected=current:${ctx.model.provider}/${ctx.model.id}`);
> return { model: ctx.model, auth: auth.auth, diagnostics };
> --- `extensions/self-learning.ts`

The configured/current fallback is model/auth selection, not evidence of multiple candidate answers or independent evaluation. Host registry/provider internals are uninspected.

### Operative objects

#### RT-OBJ-runtime-notes
Label: Process-local recent reflection notes

Source-native identity: `RUNTIME_NOTES`, a module-level string array in Node process memory. Form: natural-language note content with symbolic FIFO selection. It stores the first mistake or fix, at most 180 characters, after successful reflection writes; it retains at most 30 notes. Before-start selects the last `injectLastN` (default five). There is no root/branch key, durable reload or explicit clear on branch change. These notes are distinct from canonical disk memory and can reach context even with file context disabled. This is implementation, not evidence of actual cross-branch leakage in a deployment (SRC-1, `extensions/self-learning.ts`).

> const shortNote = (parsed.mistakes[0] || parsed.fixes[0] || "").slice(0, 180);
> if (shortNote) {
>   RUNTIME_NOTES.push(shortNote);
>   if (RUNTIME_NOTES.length > 30) RUNTIME_NOTES.splice(0, RUNTIME_NOTES.length - 30);
> }
> --- `extensions/self-learning.ts`

### Routes

#### RT-RTE-task-reflection
Label: Automatic and manual task reflection admission

Endpoints/progression: host event or `/learning-now` → selected branch transcript → completion/optional repair → parsed mistakes/fixes → daily append and scored-index/render updates → optional Git → runtime note/path. Extension code owns next-step dispatch and admission; model proposes content; filesystem performs effects. Ordinary mode is open session reflection, not a bounded curriculum/experiment. Trigger and guidance are the completed-task event/manual request and the shipped mistake-prevention instructions. No human decides each item and no independent expected-answer oracle is provided. Code can reject empty/unparseable output, missing model/auth and disabled/empty inputs. It cannot veto a plausible but false string on semantic grounds. Recovery is extraction/one repair or skip/error, without transactional rollback (SRC-1, `extensions/self-learning.ts`).

- Immediate return: `ReflectNowResult` gives daily path or skip reason/diagnostics; automatic hook mostly suppresses failures, manual command reports them.
- Later read-back: updated core/daily files can enter future-turn context; long-term path can be consulted by the host agent; short note is separately injected.
- Delegated visibility: completion receives only serialized selected messages and bounded execution signals plus embedded instructions, not the full host prompt, disk memory or tool interface; repair receives compacted raw output.
- Selection predicate: enabled branch/config; automatic path additionally requires auto setting, last assistant stop and elapsed suppression deadline; branch messages exclude recognized aborts, then take configured tail.
- Invalidation or expiry: runtime notes evict older entries; disk writes have no automatic expiry here; future render ranking can exclude items from core without deleting index history.
- Activation or effect: local append/update/render and context delivery are wired; prevention behavior and benefit are unobserved.
- Evidence limits: source implementation and embedded doctrine only; neither model factuality nor successful writes/commits are observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "You are a coding session mistake-prevention reflection engine.",
> "Focus on what went wrong and how it was fixed.",
> "Do NOT summarize accomplishments or completed tasks.",
> --- `extensions/self-learning.ts`

> if (normalizedMistakes.length === 0 && normalizedFixes.length === 0) return undefined;
> --- `extensions/self-learning.ts`

> const dailyFile = appendDailyEntry(root, now, entry);
> const coreFiles = updateCoreFromReflection(root, parsed, Math.max(1, config.maxCoreItems || 20));
> --- `extensions/self-learning.ts`

Theory account: requested output is localized mistake/prevention text; particular formulated theories in actual outputs are uninspected. The prompt asks what went wrong/how fixed, but does not itself establish claim-directed criticism with explicit blame or model compliance. It does not revise its own shipped reflection method. What persists is daily reflection text, derived rules/watch-outs, scores/timestamps, optional Git history and a short runtime note; later readers are context builder and host agent. Theory-builder conditions 1–4: condition 1 conclusion status: afforded — string items can carry whole localized rules, actual output content uninspected; condition 2 conclusion status: uninspected — delivery does not show content-dependent foreground decisions; condition 3 conclusion status: uninspected — no supplied criticism/output trace; condition 4 conclusion status: uninspected — repeated writes alone do not show retained criticism shaping later theory revision. Addressability: array items and normalized index records expose individual text units, but finer assumption/scope structure depends on generated prose. Persistence horizon is potentially cross-session on disk, process lifetime for notes. Learning: improved future capacity and attribution are unestablished; no outcome evidence. Reflection: session traces can update self-representation of mistakes and that representation has a wired later instruction/context path; actual reciprocal behavioral effect is unobserved. Reflective theory builder and autonomous theory builder are not established; computation owns implemented proposal/parse/write steps, but autonomous performance of every theory-builder operation is not demonstrated. Self-improvement attribution is limited to a dispositional, improvement-directed memory-change pathway within the extension/host-context interface, across sessions, objective preventing repeated mistakes. Trace evidence is wired to proposal determination, retained output is wired to later delivery, but live subsequent decisions causally depending on changed organization (link 4) and successful improvement lack evidence. This does not establish exercised self-improvement.

#### RT-RTE-context-injection
Label: Future-turn context delivery and consultation request

Endpoints/progression: host `before_agent_start` → enabled check → recent notes plus selected file bundle → custom hidden message and augmented system prompt → external host agent. Extension code decides inclusion, not semantic relevance; host/model owns the next work step. This is context shaping, not host transcript compaction (SRC-1, `extensions/self-learning.ts`).

- Immediate return: optional `self-learning-context` message with `display: false`, plus original or policy-augmented system prompt.
- Later read-back: prior reflection notes and selected core/daily/monthly text reach a later foreground invocation; long-term memory is referenced by path, not automatically bundled.
- Delegated visibility: host gets bounded by-value text and path instructions; no child worker is spawned. Actual host application is external.
- Selection predicate: learning enabled; notes use a tail count; files require context enabled and include flags, with lexically latest dated daily/monthly filenames; no user-query matching.
- Invalidation or expiry: rereads files at hook time; per-file prefix truncation and aggregate prefix truncation can omit later sections; notes evict by count. Missing files are omitted.
- Activation or effect: returned context and policy are wired; actual consultation, adherence and answer changes remain unobserved.
- Evidence limits: no enclosing host implementation or execution trace; character limits are not token budgets and truncation marker adds characters beyond a nominal prefix limit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const maxChars = Math.max(2000, config.context.maxChars || 12000);
> const maxPerFile = Math.max(1000, Math.floor(maxChars / 4));
> --- `extensions/self-learning.ts`

> systemPrompt: instruction ? `${event.systemPrompt}\n\n${instruction}` : event.systemPrompt,
> --- `extensions/self-learning.ts`

Core precedes ascending selected daily files, then monthly; later sections can disappear under the aggregate cap. Recent notes are outside this bundle cap. The window receives values, not automatically dereferenceable pointers; policy supplies paths that an externally equipped agent may read. Separate reflection calls resemble isolated frames with selected transcript input and only parsed output escaping; this package does not remove foreground accumulated turns or provide reference-count/liveness management. Context shaping is a code rule; on-demand file consultation is a request to the foreground model, not an implemented extension reload tool (SRC-1, `extensions/self-learning.ts`). Authority: [RT-BAP-memory-policy](#rt-bap-memory-policy).

#### RT-RTE-month-summary
Label: Manual monthly summary admission

Endpoint/progression: `/learning-month [YYYY-MM]` → regex/default month → matching daily files sorted and concatenated, prefix-compacted to 180000 characters → selected completion model → any nonempty text → overwrite monthly Markdown and optional Git. Human selects month/starts the operation; model proposes summary; extension admits nonempty output without semantic review, section validation or expected-answer oracle. Guidance asks Wins, Recurring issues and Most important learnings; ordinary mode is open summarization, not an experiment. Enabled toggle is not checked. Rejection/recovery: no files, no model/auth or empty text prevents a new summary; exceptions report failure; no automatic rollback or revision comparison (SRC-1, `extensions/self-learning.ts`).

- Immediate return: UI reports file path, missing inputs/model result or error.
- Later read-back: latest monthly file is optionally bundled on later turns, or referenced by the consultation policy.
- Delegated visibility: model receives only bounded assembled month journal and summary instructions, not the foreground transcript/system prompt.
- Selection predicate: filename prefix matching requested month and `.md` suffix; latest monthly consumption is lexicographic and separately configurable.
- Invalidation or expiry: regenerating the same month overwrites it; no automatic expiry or reconciliation with later-edited dailies.
- Activation or effect: summary overwrite and optional commit are wired, benefit/usage unobserved.
- Evidence limits: summary faithfulness and preserved facts are uninspected; no supplied outputs.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!summary) return { dailyCount: files.length };
> --- `extensions/self-learning.ts`

> writeFileSync(file, content, "utf-8");
> return file;
> }
> 
> function ensureCoreFile(root: string): string {
> --- `extensions/self-learning.ts`

This quote anchors monthly writer overwrite semantics; substantive memory lineage and curation judgments are left to the memory analyst.

#### RT-RTE-core-redistill
Label: Global core redistillation admission

Endpoints/progression: manual command → global-mode/count/optional confirmation checks → scored selection → chunks of eight → separate model completion/optional repair per chunk → ID mapping and prefix normalization → merge equal keys → final core/long-term/index rewrites and optional Git. Computation proposes and admits each rewrite; human selects scope, can cancel coarse confirmation, choose dry-run or avoid invocation, but does not approve individual content. No answer oracle verifies preserved meaning or generality. Guidance asks cross-project imperative rules preserving intent; mode is an open transformation, not a measured improvement trial. Candidate model selection is configured-then-current only while resolving availability/auth. Error after an authenticated configured candidate is chosen has no second candidate (SRC-1, `extensions/self-learning.ts`).

- Immediate return: progress, counts, sample rewrites and model diagnostics via UI; errors include smaller-limit/model-switch hints.
- Later read-back: write mode changes the same rendered files later delivered to the agent; dry-run returns preview statistics without final rewrite, though index migration/default may create core.
- Delegated visibility: each completion gets current chunk's id/kind/text; repair also receives input items and compacted raw output. Other chunks and full session history stay out.
- Selection predicate: global mode; top scored keys bounded by optional positive limit; targets then follow index order; chunks processed sequentially.
- Invalidation or expiry: successful rewrite replaces selected text/keys and merges collisions; no expiry. Missing response IDs retain original text, not reject the entire chunk.
- Activation or effect: final memory rewrites are wired; no proof of semantic preservation, generality or later improvement.
- Evidence limits: no outputs/runs; final writes are multiple synchronous operations without transaction/rollback; dry-run is not evidence of no side effects in initialization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const candidate = normalizeLearningText(parsed.get(id) || original.text);
> --- `extensions/self-learning.ts`

> if (!dryRun && !assumeYes && targetCount > 200) {
> --- `extensions/self-learning.ts`

> "- Preserve each item's original meaning and prevention intent.",
> --- `extensions/self-learning.ts`

Recovery rejects unparseable chunks after repair and avoids final writes before all chunks finish; previously created migration files and provider requests are not undone. Optional Git gives only conditional manual recovery. These rewrites generalize requested wording under unchanged guidance, not evidenced content-directed criticism of a challenged theory; actual theories/criticisms in generated output remain uninspected. No theory-builder or learning benefit is inferred from rewrite counts (SRC-1, `extensions/self-learning.ts`).

#### RT-RTE-runtime-controls
Label: Branch and global control admission

Endpoints/progression: user command → symbolic toggle/model entry or global JSON update → later branch enabled resolution/settings reload; status reports effective state. `/learning-daily` only reports today's path. Code validates model references/existence, sometimes warns rather than rejects missing auth; global/project settings determine actual picker inputs. Humans choose values; extension performs persistence, not autonomous capability discovery. Operating mode is explicit configuration, with no answer oracle or per-output approval (SRC-1, `extensions/self-learning.ts`).

- Immediate return: UI acknowledgment, selector result, status fields, path or validation warning.
- Later read-back: toggle entries are scanned along current branch; global model settings reload on later reflection/maintenance requests; branch model entries are read for status but ignored by completion pickers.
- Delegated visibility: host session manager receives custom-entry data; global settings changes are plain JSON. No worker launch or model request is needed merely to set a value.
- Selection predicate: latest matching branch toggle; configured model from merged global/project settings then current host model; branch model entries do not control selection.
- Invalidation or expiry: toggle reverses prior branch state; model reset clears branch entry effect or deletes global setting; project settings can override global; no automatic expiry.
- Activation or effect: toggle gates automatic/manual reflection and injection, not monthly/redistill maintenance; global model changes can change later selected completion model.
- Evidence limits: current grant set and deployed settings are not supplied; branch model acknowledgment is not proof of selected-model effect.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> pi.appendEntry(TOGGLE_ENTRY, { enabled: next, ts: Date.now() });
> --- `extensions/self-learning.ts`

> `selfLearning.modelResolutionOrder=configured model -> current session model${runtimeModel ? " (runtime /learning-model override is currently ignored for reflection)" : ""}`,
> --- `extensions/self-learning.ts`

Rollback/recovery is explicit toggle/reset or external settings edit; these change control references rather than provider weights. Global setting writes are not transactional and do not install new executable capabilities.

### Claims

#### RT-CLM-strict-consultation
Label: Strict mode consultation claim

The README describes strict mode as enforcement, while implementation supplies imperative natural-language policy without a read-checking gate. The implementation supports a request, not guaranteed adherence. Its authoritative downstream path is [RT-BAP-memory-policy](#rt-bap-memory-policy); operation is uninspected (SRC-1, `README.md`, `extensions/self-learning.ts`).

> - `strict`: enforce checking memory logs for history-related questions
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-memory-policy
Label: Memory context and consultation policy authority

Consumer: external foreground pi agent/model. Channel: returned hidden custom message containing historical text and returned system prompt containing appended static memory policy. Force: historical evidence plus advisory/imperative model-interpreted instruction, not deterministic action restriction. Horizon: subsequent turns; disk content can survive sessions, notes only process lifetime. Update consumers differ: reflection parsing/index/render code admits content without a foreground decision, whereas the later agent interprets delivered text (SRC-1, `extensions/self-learning.ts`).

> ? "You MUST consult self-learning memory when the user asks about history, prior decisions, patterns, regressions, or follow-up work."
> : "Consult self-learning memory when relevant to history and prior decisions.";
> --- `extensions/self-learning.ts`

> "Use this as historical evidence.",
> --- `extensions/self-learning.ts`

The host must honor the returned fields and the model must follow the instruction. The extension does not verify either, supply an answer oracle or inspect resulting decisions. Long-term memory has a referenced-path consultation route, not automatic file-text delivery. Direct reflection/maintenance completions receive separate embedded instructions and are not constrained by this returned foreground policy (SRC-1, `extensions/self-learning.ts`).

## Annotations

none
