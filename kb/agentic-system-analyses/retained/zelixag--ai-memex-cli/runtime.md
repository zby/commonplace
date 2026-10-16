---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of ai-memex-cli: delegated knowledge maintenance, deterministic feedback, and later-session context delivery at the frozen revision"
run-id: AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01
reviewed-boundary: 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f
---

# ai-memex-cli runtime report

## Runtime account

### Work and evidence boundary

ai-memex-cli maintains a Markdown wiki by combining deterministic commands with instructions for an external coding agent. Its consequential work is capture, semantic integration, repair, and later reuse of knowledge. It does not enclose the external agent's inference or tool runtime. The [boundary](boundary.md) fixes SRC-1 and its whole-system scope. All source findings below use SRC-1 at the reviewed commit; implementation and doctrine are distinguished. No supplied execution trace, real vault or model result establishes activation, successful maintenance or benefit.

The package exposes `memex` at `dist/cli.js`, distributes `dist/` and `templates/`, and builds TypeScript with `tsc` (SRC-1, `package.json`). The driver registers capture (`fetch`, `distill`), maintenance (`ingest`, `watch`, `lint`), read/use (`search`, `inject`, `glob`), setup/integration (`init`, `onboard`, `install-hooks`, `context`), direct page/log operations and migration/update entry paths (SRC-1, `src/cli.ts`). Installed slash prompts are another caller, not an independent deterministic semantic engine: Claude/Codex prompts instruct the outer agent to choose a skill workflow, while OpenCode/Gemini prompts present shell invocations (SRC-1, `src/commands/install-hooks.ts`).

> This skill makes the agent the main interface for maintaining an LLM wiki. Use the `memex` CLI as a deterministic toolbox, not as the source of semantic judgment.
> --- `templates/skills/ai-memex/SKILL.md`

The ordinary trace is [RT-RTE-ingest-write](#rt-rte-ingest-write). Material alternates are [RT-RTE-capture-source](#rt-rte-capture-source), [RT-RTE-session-distill](#rt-rte-session-distill), [RT-RTE-semantic-lint](#rt-rte-semantic-lint), [RT-RTE-watch-repair](#rt-rte-watch-repair), [RT-RTE-context-delivery](#rt-rte-context-delivery), and [RT-RTE-install-update](#rt-rte-install-update). These separate input admission, model-controlled writes, mechanical feedback, and host instruction installation; they do not assign memory-revision findings to runtime.

### Ordinary invocation, end to end

For `memex ingest <target>`, the CLI caller supplies the target, optional agent and vault. The driver ensures a vault and agent, then calls the ingest implementation. `--fix-lint` first obtains a mechanical report; `--loop` instead transfers control to the repeated ingest/lint controller (SRC-1, `src/cli.ts`). Vault and agent identities are operational paths/profile IDs, not authenticated roles or tenant identities.

`ingestCommand` resolves the global vault, merges configuration, selects an agent by flag, configured ingest agent or binary discovery, and reads a live vault schema plus `index.md`. The schema basename follows the configured agent with Markdown alternatives. The target is a hint, not a validated input-file boundary. The assembled natural-language prompt contains target, schema, current index and optional previous lint issues. The external agent owns file discovery, semantic decisions and writes (SRC-1, `src/commands/ingest.ts`, `src/core/config.ts`, `src/core/agent-adapter.ts`). The numerical inference component is [RT-CMP-coding-agent](#rt-cmp-coding-agent); no model name or immutable model revision is supplied by these calls.

The CLI prepares argv, sometimes spilling a long flag-mode prompt to a temporary Markdown file and passing a read-and-follow wrapper. It spawns the selected executable with `cwd=vault`, streams stdout, buffers stderr and records command/profile/cwd, prompt size and a truncated prompt preview. The child receives inherited environment; the streamed subprocess has stdin ignored. On child exit it reports completion/failure and removes a spilled prompt file in `finally` (SRC-1, `src/commands/ingest.ts`, `src/core/agent-adapter.ts`, `src/utils/exec.ts`). Zero exit is process success, not proof of required file changes: ingest does not validate a returned artifact. Child errors are caught and logged rather than rethrown by this command.

The requested durable effects are wiki-page edits plus index/log updates, with raw preservation. Later ingest reloads schema and index; later query/search/inject reads retained content. There is no CLI transaction enclosing the agent's individual edits in this inspected path, and its catch/finally handles reporting and temporary prompt cleanup, not restoration of wiki files. These conclusions concern the visible caller; external-agent recovery remains opaque (SRC-1, `src/commands/ingest.ts`).

Management delegation is a working-context boundary: the CLI selects schema/index/target/report for a new child invocation rather than copying the foreground conversation. Intermediate discovery and tool activity can remain in the child context; stdout and filesystem effects cross back. This resembles a task frame only at the caller boundary. Child history, compaction, provider persistence and context eviction are not implemented or inspectable here. Distillation explicitly reimports session material, and query reloads wiki content; neither demonstrates that the enclosing host discarded earlier context (SRC-1, `templates/skills/ai-memex/SKILL.md`, `src/commands/ingest.ts`, `src/commands/distill.ts`).

### Four forcing cases and control strength

**1. Raw preservation is a scoped instruction, not a filesystem invariant.** Ingest and semantic lint say not to mutate raw files. Claude's profile nevertheless passes Bash and write/edit tools; `cwd` selects a directory but does not impose a read-only mount or path sandbox in the spawn call. Alternate fetch and mechanical distill paths intentionally write raw destinations, and direct fetch writes the URL-derived destination again without the existence guard used by `new`. Thus preservation applies to maintenance behavior as a policy request, not every shipped writer (SRC-1, `src/commands/ingest.ts`, `src/commands/lint.ts`, `src/core/agent-adapter.ts`, `src/utils/exec.ts`, `src/commands/fetch.ts`, `src/commands/distill.ts`, `src/commands/new.ts`).

> extraArgs: ['--allowedTools', 'Bash,Read,Write,Edit,Glob,Grep,WebFetch'],
> --- `src/core/agent-adapter.ts`

> const destPath = join(rawDir, `${stem}.md`);
> const markdown = resultToMarkdown(result);
> await writeFileUtf8(destPath, markdown);
> --- `src/commands/fetch.ts`

Owner: prompt author/external agent. Enforcement point: interpreted maintenance prompt. Guarantee strength: policy. Covered paths: ingest and semantic-lint requests; alternates: deterministic capture, mechanical session conversion and foreground file tools. External contract: host tool permission enforcement and model compliance. Policy implementation conclusion status: wired. Preservation operation conclusion status: uninspected. The deployed grant set and isolation envelope are not supplied; the quoted adapter flag is a requested capability surface, not proof of actual provider/host authorization.

**2. Collaborative admission is not a CLI approval gate.** The shipped vault schema says to discuss takeaways before writes; the skill asks confirmation for destructive/ambiguous work. In contrast the management CLI launches a headless child, ignores stdin in streamed execution and provides no per-content approval callback. Aider uses `--yes --no-git`; Codex requests `auto-edit`. These are alternative invocation controls, not equivalent guarantees about approval semantics (SRC-1, `templates/AGENTS.md`, `templates/skills/ai-memex/SKILL.md`, `src/core/agent-adapter.ts`, `src/utils/exec.ts`).

> 2. **Discuss the key takeaways with the user before writing anything** — confirm what is worth integrating, what is duplicative, and what should be skipped. Ingest is collaborative, not auto-pilot.
> --- `templates/AGENTS.md`

> stdio: ['ignore', 'pipe', 'pipe'],
> --- `src/utils/exec.ts`

Owner: outer agent/user under doctrine; child agent during CLI maintenance. Enforcement point: natural-language instructions only within this caller. Guarantee strength: protocol. Covered paths: instructed skill/schema workflows; alternates: direct CLI, watcher, mechanical writes, external host tools. External contract: an agent must implement discussion/consent despite noninteractive launch. Approval protocol implementation conclusion status: wired. Human approval operation conclusion status: uninspected. Initiating a command does not establish human approval of every resulting claim or edit. The tension remains explicit rather than being resolved in favor of either instruction.

**3. Clean lint neither verifies factual content nor implies bounded cost.** The loop's mechanical checks are orphans, broken links and frontmatter. Semantic lint is opt-in as a separate child invocation; the watcher calls `runLint`, not the semantic pass. The loop defaults to three iterations when called directly, but watch defaults to unlimited. `--force` bypasses the repeated-issue-set stop. Ingest failure can still be followed by lint, including a clean report on unchanged files. The repeated-issue key omits frontmatter error details, so it is not an exact comparison of report content (SRC-1, `src/commands/lint.ts`, `src/core/ingest-lint-loop.ts`, `src/commands/watch.ts`, `src/cli.ts`).

> const rawMax = opts.maxIter ?? 3;
> const max =
>   !Number.isFinite(rawMax) || rawMax <= 0 ? Number.POSITIVE_INFINITY : Math.floor(rawMax);
> --- `src/core/ingest-lint-loop.ts`

> if (!opts.disableNoChangeGuard && lastReport && sameIssueSet(lastReport, report)) {
> --- `src/core/ingest-lint-loop.ts`

Owner: deterministic loop. Enforcement points: lint issue count, normalized iteration cap and optional no-change predicate. Guarantee strength: invariant for these code predicates on this route, not convergence or factual truth. Covered paths: loop callers; alternates: one-shot ingest, optional semantic lint, unlimited/force watch. External contract: child termination and correct filesystem/helper behavior; no child timeout or spend budget is passed in the inspected subprocess wrappers. Predicate implementation conclusion status: wired. Convergence operation conclusion status: uninspected.

**4. Task-labelled injection is not implemented task selection.** The bootstrap recommends `memex inject --task ...`, and the CLI parses task/token options. The injection implementation selects schema includes and, only if supplied, keyword-scored pages. It does not use `task` or `maxTokens`. Markdown output includes the schema body; JSON returns selected file contents without that body. This prevents treating the bootstrap's task wording as a relevance or token-budget guarantee. Search is another route: it returns capped paths/snippets, not a completed answer or all relevant evidence (SRC-1, `src/core/context-block.ts`, `src/cli.ts`, `src/commands/inject.ts`, `src/core/globber.ts`, `src/commands/search.ts`).

> // If keywords are provided, also search wiki for relevant pages
> if (options.keywords) {
> --- `src/commands/inject.ts`

Owner: injector for selection, outer host for consumption. Enforcement point: include resolution and optional keyword scoring. Guarantee strength: no claimed guarantee for implemented task relevance or token cap. Covered paths: inject; alternates: search, full page reads, installed digest and local projection. External contract: host explicitly reads/uses emitted text. Delivery implementation conclusion status: wired. Activation operation conclusion status: uninspected.

### Additional source coverage and remaining limits

Beyond the boundary's initial reads, this member inspected complete implementations of the adapter, subprocess wrappers, ingest/lint loop, CLI, ingest, semantic lint, distill, fetch, watch, context, hook installation, update, init, new, migration, inject, search, glob and keyword scorer; configuration and context-rendering helpers; package metadata, shipped schema, main skill and query reference. These add implementation and doctrine/design coverage under SRC-1, not a new evidence source. Source-level tests were not executed, nor was the target or its services.

The materially different control paths are enumerated above: deterministic network capture, agent web/Bash capture in the caller cwd, mechanical/agent session processing, agent wiki maintenance in vault cwd, foreground read/synthesis, autonomous watch dispatch, integration file writes, schema migration and package update. The inspected memex adapters invoke executables; provider-native tools, nested delegation, remote workers and host manual graph control remain external-agent internals, not established alternate memex APIs. Live provider permissions, current model identity, installations, user vaults and host automatic loading remain unobserved. Fine-grained session parsing, network extraction, schema/link helper correctness and onboarding interaction were not exhaustively audited; those limits prevent comprehensive format/security/compatibility claims, not the bounded control-flow account.

## Shared records

### Components

#### RT-CMP-coding-agent
Label: External coding agent and inference endpoint

Source-native identity: profiles `claude-code`, `codex`, `opencode`, `gemini-cli`, `aider`, `generic`, with additional registered Cursor/Continue profiles. The executable identity resolves from PATH and alternatives; it is not a model identity. Representational form: inference depends on distributed-parametric model state; profile/argv configuration is symbolic. Storage substrate: executable and model/provider storage outside this repository; actual parameters and provider state are uninspected. In the inspected memex routes no parameter-update operation is requested; whether provider parameters change during operation is uninspected. Exact model version is not pinned by the invocation. Mutable executable/configured provider resolution can select a different model; its actual endpoint mapping is uninspected. This does not preclude learning via retained wiki content.

Evidence: SRC-1, `src/core/agent-adapter.ts`, `src/commands/ingest.ts`, `src/commands/distill.ts`, `src/commands/lint.ts`, `src/commands/fetch.ts` (implementation).

> const priority: AgentId[] = ['claude-code', 'codex', 'opencode', 'gemini-cli', 'aider', 'generic'];
> --- `src/core/agent-adapter.ts`

### Operative objects

#### RT-OBJ-agent-profiles
Label: Agent profiles and merged configuration

Source-native identity: `AGENT_PROFILES` and `VaultConfig`. Representational form: symbolic registry, argv arrays and JSON fields consumed by fixed selection/merge rules. Storage substrate: shipped TypeScript/compiled module, global `~/.llmwiki/config.json`, and vault `.llmwiki/config.json`. Defaults are overlaid by global then local config; a top-level agent populates unset ingest/distill agents. CLI overrides remain route-specific. Deprecated command fields derive known agent identities rather than installing arbitrary new registry entries (SRC-1, `src/core/config.ts`, `src/core/agent-adapter.ts`, implementation).

> // Propagate top-level agent to sub-configs
> if (config.agent) {
> --- `src/core/config.ts`

#### RT-OBJ-ingest-prompt
Label: Ingest invocation prompt

Source-native identity: `buildIngestPrompt` output. Representational form: natural-language task and instructions with embedded schema/index/report; a report's JSON/issue fields become interpreted guidance at this consumer. Storage substrate: process string or temporary UTF-8 Markdown file. Prompt delivery is argv or a wrapper directing the child to read the file. Cleanup deletes the temporary directory after execution, not durable wiki edits. The prompt's target is deliberately a hint and can refer outside raw (SRC-1, `src/commands/ingest.ts`, `src/core/agent-adapter.ts`, implementation).

> // We pass the raw target string as a HINT to the agent.
> // The agent uses its own file search tools to find the actual files.
> --- `src/commands/ingest.ts`

### Routes

#### RT-RTE-ingest-write
Label: Agent ingestion into wiki

Endpoints/progression: CLI or outer skill caller → live schema/index/target prompt → selected child agent in vault cwd → requested wiki/index/log writes → terminal report. CLI owns dispatch; child model proposes and admits semantic edits through its tools. Guidance asks for source-based pages, cross-links and raw preservation. Starting the workflow is not per-content human approval. Human discussion is requested by schema, but no CLI pre-write veto gate or artifact transaction is wired. Mode: open target-driven maintenance, not a benchmark/curriculum. Answer oracle: none supplied; schema is a writing contract, not an expected factual answer. Recovery: child errors logged, prompt temp files cleaned; restoration of partial wiki edits is not performed by this function. Direct `new` is an alternate deterministic writer with type/name validation and existing-file refusal; `migrate` explicitly converts valid legacy summary subtypes, skips destination conflicts and supports dry-run, without making model decisions (SRC-1, `src/commands/ingest.ts`, `src/commands/new.ts`, `src/commands/migrate.ts`, `templates/AGENTS.md`).

- Immediate return: stdout/stderr and completion/failure logging; dry-run prints the prompt instead of launching the child.
- Later read-back: subsequent ingest reloads schema/index; search/inject/outer page reads can consume changed wiki files.
- Delegated visibility: live schema and index are inlined; target is a search hint; child file tools discover source/page content, not a copied foreground conversation.
- Selection predicate: explicit target normalized as hint; default all files under vault raw; agent decides actual file/page selection.
- Invalidation or expiry: each call reloads schema/index; spilled prompt file removed in finally; no wiki expiry is set here.
- Activation or effect: process invocation is wired; wiki/index/log writes are requested and delegated, not verified by this function.
- Evidence limits: no child transcript, approved edit set or resulting vault supplied; compliance and semantic success unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 2. Create or update wiki pages following the schema above.
> 3. Never modify or delete raw source files.
> 4. After writing pages, update ${vault}/index.md and ${vault}/log.md as instructed in the schema.
> --- `src/commands/ingest.ts`

#### RT-RTE-capture-source
Label: Web material capture

Endpoints/progression: URL/keywords → direct network/search helpers or explicitly selected agent → Markdown under raw scene. Direct keyword mode lets a human choose result indices, all or none; `--yes` selects all returned results. Direct URL/sitemap/crawl modes select through supplied limits and URL rules. The agent branch runs in the caller cwd, not necessarily vault cwd, and prompts WebFetch/Bash retrieval. Admission is direct code I/O or model tool writes, not factual verification. Mode: open capture request. Proposer: user/query and search service; decider: user result selection or code/model; veto: interactive selection/cancel before direct keyword fetch, dry-run, external-agent permissions. No answer oracle. Recovery: skips/logs failed pages and retains successful writes; this command supplies no batch rollback. Source-selection guidance is operational preference for official/recent sources, not proven source quality (SRC-1, `src/commands/fetch.ts`, implementation).

- Immediate return: written-page counts/failures and next-ingest suggestion; child output on agent paths.
- Later read-back: raw Markdown is reachable by subsequent ingestion and search.
- Delegated visibility: agent gets query/URL, output directory and formatting/quality instructions; it uses its own web/file tools.
- Selection predicate: URL detection or keyword results; interactive indices/all, top limit, crawl/sitemap bounds, or model choice on delegated branch.
- Invalidation or expiry: no TTL; repeated direct fetch can write the same derived destination; no preservation guarantee across capture calls.
- Activation or effect: direct branch writes returned Markdown; agent branch requests raw files and summaries.
- Evidence limits: network helper internals and live responses not established here; model capture results unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (options.yes) {
>   // Auto mode: fetch all results
>   selectedIndices = results.map((_, i) => i);
> --- `src/commands/fetch.ts`

#### RT-RTE-session-distill
Label: Session capture and delegated distillation

Endpoints/progression: session files or hint → mechanical parse/render or model extraction → raw session Markdown; agent branch also requests appending learnings to the schema file. The no-argument default is mechanical current/latest conversion, not model summarization. Explicit `--no-llm` with an input is also mechanical; `--latest`/input/output combinations can select delegated mode. Code chooses current Codex thread when matched, otherwise latest mtime among discovered files. Model branch receives role, input hint, schema and index and runs in vault cwd. Mode: open session capture, no oracle or expected answer. Proposer: session content plus extraction instructions; decider/admitter: parser/code or external model. Caller chooses mode/input; no per-extracted-claim human gate. Model guidance requests decisions, practices, rationale and no credentials; privacy compliance is not verified. Recovery logs errors; no automatic content rollback in command. This establishes a requested instruction-change path as well as raw capture, not that learnings improved later behavior (SRC-1, `src/commands/distill.ts`, implementation).

- Immediate return: destination/source messages for mechanical mode; child output and next-ingest advice for delegated mode.
- Later read-back: subsequent ingest can read session Markdown; a later management invocation reloads schema notes if the agent appended them.
- Delegated visibility: model receives path/search hint, role, live schema and index; mechanical mode launches no model.
- Selection predicate: explicit input; no-argument configured/current agent session root, extension/depth discovery, thread-ID match or latest mtime; model latest mode uses a search instruction.
- Invalidation or expiry: default conversion skips destinations whose mtime is at least source mtime; explicit mechanical/model output paths have different write behavior; no general TTL.
- Activation or effect: mechanical branch writes parsed/rendered Markdown; model branch requests extraction and schema append, without verifying either output.
- Evidence limits: exact parser fidelity and provider session formats not exhaustively audited; no actual transcript conversion or downstream activation supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> After writing the file, also update ${vault}/${contextFile} if it exists, appending a brief note about this session's key learnings.
> --- `src/commands/distill.ts`

#### RT-RTE-semantic-lint
Label: Delegated semantic diagnosis and repair

Endpoints/progression: mechanical report → live schema/index/report prompt → child semantic scan → requested direct fixes or durable findings page and log. Trigger: `lint --with-semantic`; plain lint only reports mechanical checks. The external model proposes, judges safety/ambiguity and writes; schema directs seven categories, including contradictions and duplicates. The prompt routes ambiguous/large findings to a page for human/agent review, but the CLI does not enforce a diff approval boundary. Mode: open diagnosis/repair. Answer oracle: no reference truth supplied; mechanical report is structural evidence, not semantic ground truth. Recovery is failure logging and temp-prompt cleanup, not wiki rollback (SRC-1, `src/commands/lint.ts`, `templates/AGENTS.md`, implementation and doctrine).

- Immediate return: mechanical findings and streamed child output/completion; dry-run prints semantic prompt.
- Later read-back: requested report page, repairs and log persist for later readers; caller does not automatically rerun semantic validation afterwards.
- Delegated visibility: full live schema/current index and JSON mechanical report; model must scan wiki files through tools.
- Selection predicate: schema semantic categories; model chooses relevant pages and safe fixes versus unresolved findings.
- Invalidation or expiry: prompt rebuilt from live files per invocation; report filename date-based; no automatic report retirement specified here.
- Activation or effect: semantic scan and edits are requested; actual fixes, reviewer decisions and correctness unobserved.
- Evidence limits: no model trace or findings artifact; category coverage cannot be inferred from successful process exit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 3. Apply safe, unambiguous fixes directly (broken-link suggestions, frontmatter corrections, obvious cross-reference additions, page-merge stubs when the duplicate is unambiguous).
> --- `src/commands/lint.ts`

#### RT-RTE-watch-repair
Label: Repeated ingest and mechanical lint

Endpoints/progression: CLI loop/once, startup file scan, debounced add/change or periodic dirty health check → ingest/lint iterations → clean/stalled/capped/error state → best-effort context refresh on clean. Within one watcher `busy` serializes batches; changed filenames are status/batch metadata, while `runLoopSafe` supplies the whole watch path as ingest target. Health checks skip an initial ingest and feed lint to a later iteration. Code determines stopping and report propagation; model determines repairs and writes. This is an open maintenance mode with structural feedback, not a semantic oracle, expected-answer curriculum or proof of convergence. Human can choose caps/force, stop watcher or alter files; ordinary iterations do not seek individual content approval. Previous lint issues shape subsequent prompts, at most 200 issue descriptions; instructions prioritize wiki repair without raw mutation. The resulting pages are model-admitted before the next lint, not staged behind a rejection gate. No-change/cap stops leave existing writes in place (SRC-1, `src/commands/watch.ts`, `src/core/ingest-lint-loop.ts`, `src/commands/ingest.ts`, `src/commands/lint.ts`).

- Immediate return: one-shot result includes iterations, stop reason and final report; continuous watch exposes phase/status and logs; daemon parent returns PID/log instructions.
- Later read-back: changed wiki files feed later lint/ingest; prior issue report enters the next prompt within a loop; clean runs refresh registered host context from wiki.
- Delegated visibility: each ingest child gets schema/index/target and previous bounded issue list, not the watcher's complete event history.
- Selection predicate: watched extensions, startup scan, add/change debounce or dirty periodic lint; default target whole watch path; no unlink listener in inspected watcher registration.
- Invalidation or expiry: issue report replaced each round; temporary prompt removed; status/PID removed on cleanup; daemon log remains; no wiki rollback on stall.
- Activation or effect: dispatcher, feedback and stop predicates wired; model compliance, convergence and later host activation not observed.
- Evidence limits: concurrency protection is local to one watcher, not a demonstrated multi-process vault lock; process signaling does not establish cancellation of external agent descendants.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> target: state.watchPath,
> --- `src/commands/watch.ts`

> // fall through to lint so the caller still gets a report
> --- `src/core/ingest-lint-loop.ts`

No formulated explanatory theory is established by this report's mechanical feedback account. It forwards localized defects and requests repairs. Model-internal criticism is opaque; successful theory criticism, learning and improvement are not inferred from issue counts or recurrence. Semantic meaning/revision assessments remain for the specialists.

#### RT-RTE-context-delivery
Label: Retained content delivery to outer agents

Endpoints/progression: outer query → search paths/snippets → foreground page reads/synthesis; or inject → included/keyword page bodies; or glob → local copied subset and generated includes; or context install/refresh → project host bootstrap. These are distinct consumers, not identical selection semantics. Search chooses ripgrep/qmd/hybrid from flag/config, falls back when qmd is missing, filters scene/type after backend limiting, deduplicates and caps. Errors can become empty results. Glob scores metadata by supplied/project-derived keywords, copies matched files with force and regenerates local includes; this implementation does not clear unmatched old local files. Inject includes can resolve absolute/home/relative paths; keyword scoring is optional and task/token flags do not affect selection. Bootstrap digest lists up to five indexed pages per scene by existing order, plus optional bound scene triggers; it is not a task ranker (SRC-1, `src/commands/search.ts`, `src/commands/inject.ts`, `src/core/injector.ts`, `src/commands/glob.ts`, `src/core/globber.ts`, `src/core/context-block.ts`).

Admission subroute: context install/refresh reads pages and scene manifests, renders instructions/digest and writes marker-bounded Markdown or a full Cursor rule, registering target hosts. Automatic after-clean refresh iterates registered hosts best-effort. Code selects/render-writes content; human chooses initial installation/scene binding or invokes uninstall. No per-refresh human gate. Rejection/recovery: dry-run, unsupported-host skip, per-host caught refresh errors, block uninstall; no snapshot rollback is implemented by context command. Guidance is the renderer's instruction to consult knowledge and use CLI commands. Mode: open integration/use; no answer oracle (SRC-1, `src/commands/context.ts`, `src/core/context-block.ts`, `src/core/ingest-lint-loop.ts`).

- Immediate return: search paths/snippets or JSON, inject bodies/JSON, copied local projection, or host-file write/status messages; outer model returns the actual answer.
- Later read-back: later invocations read changed wiki/source files, copied local files or installed host bootstrap. Static renderer/skill text alone is not accumulated memory.
- Delegated visibility: query foreground model gets only results and pages it reads; inject Markdown also outputs schema body; JSON contains selected file objects only; host bootstrap carries digest/paths/instructions, not full wiki.
- Selection predicate: backend query/filter/cap, include directives, metadata keyword scoring, or per-scene ordered digest slice depending on subroute.
- Invalidation or expiry: explicit refresh/reprojection needed for derived files; clean loop refresh is best effort; uninstall removes context blocks/registry entries; no universal stale-content TTL.
- Activation or effect: deterministic delivery/file writes wired; host autoload and model use depend on external runtime contracts and are unobserved.
- Evidence limits: neither snippet delivery nor a bootstrap instruction proves complete retrieval, answering accuracy or behavioral change; qmd internals uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Read the most relevant wiki pages.
> --- `templates/skills/ai-memex/references/query-workflow.md`

> const top = list.slice(0, topPerScene);
> --- `src/core/context-block.ts`

#### RT-RTE-install-update
Label: Integration and product change admission

Two related but independently controlled surfaces: hook installation installs shipped workflow text into host command/skill locations; package update replaces the executable/template distribution. The CLI caller triggers both. Hook generation is deterministic, writes/prunes managed files and appends a generic/Codex instructions section unless already present; Claude and Codex receive copied skill references. User-level Codex prompt paths can be used even from a project install. `install-hooks` also attempts context install unless disabled/user-scope. This is instruction/capability exposure, not proof that a host discovered or granted it (SRC-1, `src/commands/install-hooks.ts`, `src/cli.ts`).

For product replacement, caller chooses source or installation detection chooses npm/git. npm admission is latest package availability followed by global install; Git admission is pull/rebase followed by dependency install, build and link. npm-unavailable fallback installs from GitHub. Upstream maintainers supply changes; code admits them through package manager/Git outcomes. No model selects a successor and no semantic quality oracle is supplied. Mode: explicit open upgrade, not an autonomous optimization loop. Veto/recovery: `--check`, dry-run for hook writes, source choice and logged/manual recovery on update failure; update does not implement an automatic rollback transaction or run a test suite before accepting replacement. Shell/package-manager contracts remain external (SRC-1, `src/commands/update.ts`, `src/commands/install-hooks.ts`, `package.json`).

- Immediate return: created/pruned paths and usage hints, update version/status or failure/manual instructions.
- Later read-back: host may load installed commands/skills; subsequent memex invocation uses replaced executable/templates.
- Delegated visibility: integration text tells outer agent what workflow/CLI to use; package tools receive source/package commands, not a wiki knowledge prompt.
- Selection predicate: caller agent/scope, shipped registry/template set, install-method detection or source override and upstream latest/current branch.
- Invalidation or expiry: managed files overwritten/pruned on reinstall, existing generic section can be skipped; update follows mutable upstream; no TTL or built-in version rollback.
- Activation or effect: installation and update calls wired; host recognition, successful build/runtime replacement and usefulness unobserved.
- Evidence limits: no live registry/Git results or host integration run; shipped updater is not evidence of self-directed product improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await runCommand('git', ['pull', '--rebase'], { cwd: projectRoot });
> --- `src/commands/update.ts`

> const { stdout, stderr } = await runCommand('npm', ['install', '-g', 'ai-memex-cli@latest'], {});
> --- `src/commands/update.ts`

### Claims

#### RT-CLM-management-use
Label: Management versus use separation

Claimed operation: maintenance runs in a CLI-spawned child with live schema; use answers in the current user session. This is shipped doctrine, with supporting ingestion/semantic-lint wiring but not universal control over foreground file tools. The schema's query section requests filing durable answers back; the installed query reference instead says not to write unless asked. Those are different guidance paths, not a single mechanically enforced read-only guarantee (SRC-1, `templates/skills/ai-memex/SKILL.md`, `templates/skills/ai-memex/references/query-workflow.md`, `templates/AGENTS.md`).

> Practical rule: if a workflow modifies wiki pages, prefer the CLI command that spawns a sub-agent. If it only reads or summarizes, do it in the current session.
> --- `templates/skills/ai-memex/SKILL.md`

> Do not write files unless the user asks to save or archive the answer.
> --- `templates/skills/ai-memex/references/query-workflow.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-schema-prompt
Label: Vault schema to maintenance decisions

Consumer: external ingestion/semantic-lint/distillation agent. Channel: live schema inlined into invocation prompt, with schema/index loaded afresh; distillation can request adding session learnings to that schema. Force: natural-language guidance, interpreted by the model, not memex-enforced authorization. Horizon: one invocation's prompt; a changed durable schema can reach later invocations across sessions. Actual schema changes and downstream causal use unobserved. Evidence: SRC-1, `src/commands/ingest.ts`, `src/commands/lint.ts`, `src/commands/distill.ts`; see [RT-RTE-ingest-write](#rt-rte-ingest-write) and [RT-RTE-session-distill](#rt-rte-session-distill).

> ## Wiki Schema
> 
> ${agentsContent}
> --- `src/commands/ingest.ts`

#### RT-BAP-host-bootstrap
Label: Project bootstrap to outer session

Consumer: host coding agent in a project session. Channel: installed CLAUDE/AGENTS/GEMINI Markdown or Cursor rule, containing wiki digest/paths and consultation instructions. Force: requested host-autoloaded instructions; Cursor renderer requests `alwaysApply: true`. No host-runtime enforcement or observed compliance is supplied. Horizon: later project sessions until refresh/uninstall/replacement; after-clean refresh can update the projection from retained pages. Evidence: SRC-1, `src/commands/context.ts`, `src/core/context-block.ts`, `src/core/ingest-lint-loop.ts`; see [RT-RTE-context-delivery](#rt-rte-context-delivery).

> globs: ["**/*"]
> alwaysApply: true
> --- `src/core/context-block.ts`

## Annotations

none
