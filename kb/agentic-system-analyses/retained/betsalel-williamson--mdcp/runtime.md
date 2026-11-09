---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MDCP runtime baseline: host-interpreted documentation workflows, deterministic compile/check routes, extension and maintainer admission paths."
run-id: AAS-2026-11-08-mdcp-1e4e8314c1e4-01
reviewed-boundary: "1a198715a4da72dd89bad93f84cf5d4b3ab56b01"
---

# MDCP runtime report

## Runtime account

MDCP ships a documentation skill and a Node CLI, not an enclosing inference runtime. The ordinary consequential work is an agent finding a small source shard, changing intent before implementation, compiling derivatives, and checking the resulting documentation. The skill gives natural-language decision policy; host tools perform searches, reads, writes, shell calls and Git operations. The CLI gives deterministic transformation and diagnostic policy. These are different enforcement layers, not interchangeable guarantees. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`, `packages/mdcp-cli/src/cli.ts`.

### Ordinary feature invocation

A user supplies a feature or bugfix request to an external agent host. Host skill discovery exposes MDCP; the foreground agent interprets the task and selects one workflow. It takes the work item and delivery-location conventions from the request/repository, discovers relevant shards by host search or an index, and reads the selected workflow and needed shards. Its identities are task/work item, branch, guide and file paths, not MDCP-managed session or worker IDs. It plans numbered commit groups, creates a branch, edits audience-appropriate shards and indexes first, implements/tests against that contract, revises documentation to as-built behavior, validates and submits for review. Human approval is conditional: when nobody can answer, the skill directs reasonable defaults and continuation, stopping for destructive/irreversible work, real scope changes or exclusively human input. Therefore “docs first” is a protocol for the host agent, not a CLI-enforced ordering constraint. Decision roles, mode and admission limits are retained in [RT-RTE-feature-work](#rt-rte-feature-work).

Context reduction is requested rather than implemented by a window manager. The skill asks for one shard at a time and only the selected workflow; it does not physically remove prior turns or prohibit host tools from reading compiled output. Optional workflow isolation is explicitly host-dependent. A fork resembles a task frame only insofar as selected inputs enter a separate host context; MDCP specifies no child return schema, token budget, eviction algorithm, reload handle or enforced visibility boundary. Source files remain available to search/read later. Compiled documents are a publication path and a last-resort broader agent read, not the prescribed ordinary context payload. SRC-1, `skills/mdcp/SKILL.md`; [RT-BAP-skill-host](#rt-bap-skill-host).

> Hosts that can fork work (Task tool, `context: fork`, and similar) may run the
> chosen workflow in an isolated agent; otherwise follow it in the main session.
> --- `skills/mdcp/SKILL.md`

When the agent runs `mdcp compile`, the packaged executable parses flags, resolves config against the invocation directory, parses JSON through the schema, and builds a compile workspace. Guide order, configured guide paths and manifest links select source content. A shared shard cache/link index feeds per-output assembly. Assembly adjusts headings, applies named hooks, rewrites intra/cross-guide and publish-relative links, adds optional source tags, and assembles per-guide and eligible monolith copies. The copies are assembled for their actual output locations rather than blindly copied with identical links. Output writing and refs generation precede built-in link-lint failure. The terminal result is written Markdown/JSON plus console diagnostics and a process exit status, not an agent answer. SRC-1, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-cli/src/compile-workspace.ts`, `packages/mdcp-core/src/config/load.ts`, `packages/mdcp-core/src/compile/assemble.ts`; [RT-RTE-compile-check](#rt-rte-compile-check).

`mdcp check` is not read-only admission. Orphans stop it before compilation; otherwise it writes outputs, regenerates refs and checks that registry against the same computed data. It then combines built-in links, configured Markdown peers, optional HTTP-link peer, Vale unless skipped, optional path probes and coverage. It accumulates several failures for diagnostic reporting, but some failures exit immediately. A failed late check does not roll back already-written output. Existing compiled output can optionally be moved to backup before overwrite; this is not a transaction or automatic recovery. Correct source/config and rerun, or use external Git/backup recovery. SRC-1, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-core/src/compile/write-output.ts`, `packages/mdcp-core/src/refs/registry.ts`.

### Forcing cases and guarantees

The following four cases challenge universal interpretations of the shipped rules. They are source traces, not executed experiments.

| Forcing case | Supported route and result | Guarantee boundary |
| --- | --- | --- |
| Broken links with permissive options | `--warn-broken-links` resolves severity to warn; `lint.links.enabled: false` returns an empty built-in issue list. Compile has already written outputs and refs before its link decision. | Built-in link failure is conditional on enabled checking and error severity. These are supported CLI/config inputs, not hypothetical malformed calls. |
| Missing peers, skipped Vale and non-strict coverage | `runPeer` returns exit 0 when a missing binary is not required. `check --skip-vale` bypasses Vale even when the require flag is also supplied; Markdown checks require configured paths/configs. Coverage gaps fail only with `scan.strict`. | “check passed” means the selected gate completed, not that every possible peer or semantic check ran. Root dogfood scripts strengthen this with require flags; they do not change bare CLI defaults. |
| Direct library calls and registered callbacks | Core exports assembly, writers and validators separately. Callers can assemble/write without the CLI check action. Registered hook functions can transform bodies; an explicit hook array replaces defaults and unknown names are skipped. | The CLI gate does not wrap every API caller or callback. Hook registration is process-local executable authority, not a new sandboxed plugin principal. |
| Host tools and mechanical shard import | Agent source edits and reads happen through host tools. Separately, `shard` invokes md-tree and replaces guide directories, then asks the caller to compile. | Skill prose is not a filesystem interceptor or per-content approval gate. The deterministic import route need not pass the feature/doc-review decision process. |

Evidence for the first two cases is in SRC-1, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-cli/src/compile-workspace.ts`, `packages/mdcp-core/src/peers/resolve.ts`, `packages/mdcp-core/src/config/schema.ts`, `package.json`; for the latter two, SRC-1, `packages/mdcp-core/src/index.ts`, `packages/mdcp-core/src/compile/hooks.ts`, `packages/mdcp-core/src/config/resolve-compile-hooks.ts`, `packages/mdcp-core/src/shard/orchestrator.ts` and `skills/mdcp/SKILL.md`. Supporting passages are retained in the route records below.

Load-bearing guarantee ownership is thus local:

- **Shard discipline and docs-first ordering:** owner is the host agent following the skill; enforcement point is interpreted instruction before/while editing; guarantee strength: protocol. Covered path is compliant skill-mediated work. Direct host filesystem/shell operations and `shard` are materially different paths. Required external contract is host instruction following and tool permissions. Implementation conclusion status: claimed. Operation conclusion status: uninspected.
- **Mechanical validation failure:** owner is the CLI check action and configured peers; enforcement point is process failure for selected diagnostics; guarantee strength: invariant within the inspected enabled branches, not a universal documentation-correctness guarantee. Direct core calls, disabled/warn checks and absent optional peers do not have equivalent coverage. Required external contract is filesystem access and installed peer behavior. Implementation conclusion status: wired. Operation conclusion status: uninspected.
- **Repository integration gate:** owner is the CI workflow; enforcement point is ordered skill/docs validation and `git diff --exit-code`; guarantee strength: policy. This can reject changed generated outputs in that workflow, but does not prove deployed branch protection, PR approval or semantic truth. Required external contract is GitHub execution and merge policy outside this evidence. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `.github/workflows/ci.yml`, `package.json`; [RT-RTE-release-admission](#rt-rte-release-admission).

### Maintenance, publication and model boundary

`mdcp review` computes sprawl warnings, not replacements. A separate agent-interpreted doc-review workflow chooses merge, split, move, reword, link, delete or leave, applies groups and checks again. Repeated findings can prompt changes to thresholds, glossary entries or Vale rules. That is a route for admitting durable guidance/checking changes, with no measured improvement established here; [RT-RTE-doc-review](#rt-rte-doc-review).

The repository also ships a site consumer: it reads the refs registry, compiled outputs and source shards, derives slug ownership from source tags/headings, builds pages, rewrites links and writes navigation. This is not evidence that an agent received or obeyed those pages. Root `site:prepare` builds and compiles first. Source tags and compiled registry content can therefore affect a later deterministic publication consumer, independently of ordinary host shard reads. SRC-1, `packages/mdcp-site/scripts/sync-content.mjs`, `package.json`; [RT-RTE-compile-check](#rt-rte-compile-check).

The optional maintainer evaluation plane is materially different from production: with/without-skill fixtures, human feedback and model grading are prescribed; a vendored trigger optimizer actually wires repeated Claude subprocess evaluations and model-proposed descriptions into bounded candidate selection. It returns a best-description result; installing that result into skill frontmatter is a further author action. Neither production CLI inference nor autonomous production self-modification follows from this tooling. [RT-RTE-skill-evaluation](#rt-rte-skill-evaluation) names its oracle, state, stopping and admission boundary; [RT-CMP-claude](#rt-cmp-claude) names the unpinned distributed-parametric dependency.

The capability surface includes host file/shell/Git tools, CLI output writes, peer subprocesses, programmatic hook callbacks, and optional evaluator subprocesses. The current grant set is whatever the external host/process/CI credentials permit; MDCP does not establish the actual deployment's grants. The inspected session hook installs dependencies, builds and installs the checkout skill only for a Claude remote session. Its host configuration is not an isolation envelope. CI declares read access for its Check job and audit-mode egress logging; the manual release job has write/OIDC permissions. No inspected deployment or model run establishes actual isolation, activation, latency, cost or benefit. SRC-1, `.claude/settings.json`, `.claude/hooks/session-start.sh`, `.github/workflows/ci.yml`, `.github/workflows/release.yml`.

### Evidence basis and added coverage

All findings use SRC-1 at the boundary's frozen commit. The local HEAD was checked against that pin. This report adds implementation inspection of core hook resolution/registration, peer resolution/spawning, output backup writing, section selection, config parsing/schema, shard orchestration, relevant site consumer ranges, and vendored trigger evaluation/optimization/proposal code; it adds doctrine inspection of the feature/doc-review workflows and live-eval contracts, plus release workflow wiring. These are additional paths within the registered repository, not new sources. No target, test, fixture, provider call, benchmark or evaluator was executed. Remaining included archetype/bootstrap/UX details and evaluator helper internals are not exhaustively characterized here. None of the source traces establishes observed compliance, successful published output, learning benefit or causal improvement.

## Shared records

### Components

#### RT-CMP-host-model
Label: Host inference dependency

MDCP's ordinary skill is interpreted by an external agent host. Its model is distributed-parametric numerical state in provider/local model storage, not weights shipped in this repository. Provider internals, parameter changes during operation and exact version are uninspected; MDCP does not pin them in `skills/mdcp/SKILL.md`. A host-selected mutable endpoint may resolve to another model; host/provider configuration is outside the captured source. This component's identity is the opaque foreground inference role, not the deterministic CLI. SRC-1, `skills/mdcp/SKILL.md` permits multiple hosts and host-dependent forks. Its natural-language policy object is [RT-OBJ-mdcp](#rt-obj-mdcp).

> Host-agnostic **documentation system** Agent Skill for MDCP. Prefer this over
> IDE extensions when you want durable, sharded docs that agents and humans can
> maintain as ideas keep coming.
> --- `skills/mdcp/SKILL.md`

#### RT-CMP-claude
Label: Claude evaluation and proposal inference

The vendored evaluator/proposer calls the external `claude` executable, optionally with `--model`. This is a separately inspectable use role from the arbitrary production host above; it may resolve to the same provider in a deployment, but no identity of actual endpoints is established. Representational form: distributed-parametric inference; storage substrate: external model/provider storage, uninspected. No parameter-update API is inspected in these scripts; parameter changes at the provider remain uninspected. Exact weight version is not pinned; a model string or user's configuration can select a mutable alias/default and resolve differently later. SRC-1, `.agents/skills/skill-creator/scripts/run_eval.py`, `.agents/skills/skill-creator/scripts/improve_description.py`.

> if model:
>     cmd.extend(["--model", model])
> --- `.agents/skills/skill-creator/scripts/improve_description.py`

### Operative objects

#### RT-OBJ-mdcp
Label: MDCP skill policy

Source-native identity: `skills/mdcp/SKILL.md` and its selected workflow references. Representational form: natural-language instructions and decision tables interpreted by a host agent. Storage substrate: versioned Markdown files, installed into a host-discovered skills directory by an external installer. The vendor-managed skill, repository-specific normative shards and complementary skills have different intended ownership; arbitrary repo-specific hand-edits to the installed vendor skill are forbidden by policy, not prevented by a file guard. SRC-1, `skills/mdcp/SKILL.md`.

> - **NEVER** hand-edit files in a vendor-managed install under your agent’s skills
>   directory (for example `.agents/skills/` in Cursor/Amp) for repo-specific
>   guidance — use complementary skills, `docs/extensions/`, or normative shards.
> --- `skills/mdcp/SKILL.md`

#### RT-OBJ-config
Label: Compile and check configuration

Source-native identity: `mdcp.config.json`, parsed as `MdcpConfigSchema`. Representational form: symbolic JSON keys, values and lists consumed by fixed rules; storage substrate: caller repository file and process-local parsed object. It controls guide/path/order selection, hook names, outputs, backup and validation policy. Human or software editing this file can change the gate; schema validity is not approval of policy strength. SRC-1, `packages/mdcp-core/src/config/load.ts`, `packages/mdcp-core/src/config/schema.ts`.

> const raw = JSON.parse(readFileSync(abs, 'utf-8'));
> return MdcpConfigSchema.parse(raw);
> --- `packages/mdcp-core/src/config/load.ts`

### Routes

#### RT-RTE-feature-work
Label: Skill-mediated feature work

Endpoints: request/repository → foreground host agent → selected shards/indexes → code/tests → validation and review submission. The agent owns next steps; natural-language skill/workflow policy guides its choices, and host tools execute effects. State is the current host context plus repository branch/files. Source-native guidance persists as edited Markdown and code, not as a model-weight update. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Host reply/plan and final review submission are prescribed; no MDCP-specific response protocol is implemented.
- Later read-back: Future tasks are instructed to discover and open durable shards through search/indexes; no successful later consumption is observed.
- Delegated visibility: Optional isolated host workflow; input/return scope is not specified by MDCP.
- Selection predicate: Agent interprets task against workflow table; relevant shards are found by host search or guide index.
- Invalidation or expiry: Superseded current documentation is to be deleted/replaced; Git keeps history. There is no MDCP context-expiry timer.
- Activation or effect: Instructions request docs-first branch edits, implementation/tests and validation; actual adherence is unobserved.
- Evidence limits: Workflow prose establishes requested operation, not a runtime-enforced sequence or exercised improvement.

Proposal/decision/veto: the user/repository supplies scope and acceptance; the agent proposes plans/content and implements. Human review can approve or reject when available, but starting work is not per-content human approval. Headless defaults allow continuation. Operating mode: open work requests narrowed to one focused work item, not a fixed experimental curriculum. Answer oracle: task acceptance/tests may constrain a feature, but no universal expected-answer oracle is supplied by this workflow. Trigger: feature/bugfix task. Proposed change: shards, indexes, tests and product code. Admission: agent edits and validates, then submits for repository review. Rejection/recovery: stop conditions and review apply; branch/Git reversibility is the stated fallback, not automatic rollback. Guidance says place intent/contracts by audience before code and reconcile with as-built behavior.

> Before writing shards, apply the `mdcp` skill's **What belongs where** placement test. Place by **audience and job**, not by topic keyword (the same subject can span tiers).
> --- `skills/mdcp/references/workflows/feature-level.md`

> Put the plan, with its commit groups, in your reply, then carry on with the
> edits. Edits on a branch are reversible.
> --- `skills/mdcp/SKILL.md`

#### RT-RTE-compile-check
Label: Compile, validate and publish derived documentation

Endpoints: CLI arguments/config/source files → compile workspace → output Markdown/refs → diagnostics/status; later registry reads and site generation consume derivatives. CLI/core own symbolic progression. SRC-1, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-cli/src/compile-workspace.ts`, `packages/mdcp-core/src/compile/assemble.ts`, `packages/mdcp-core/src/refs/registry.ts`, `packages/mdcp-site/scripts/sync-content.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Compile/check write derived files and log paths/issues; refs-list returns JSON or tabular headings. Review is a separate command.
- Later read-back: refs-list reads stored JSON; site sync reads registry, compiled output and source shards for pages/navigation. These are deterministic later consumers, not observed agent activation.
- Delegated visibility: Peer binaries receive configured paths/arguments and docs-root cwd; they inherit process authority. No model worker is launched by these commands.
- Selection predicate: Config compileOrder/guide paths and manifest-linked sections, transitive in-scope Markdown links, with directory fallback when no manifest paths resolve. Site walks the selected published guide trees, rather than assuming exactly the compile file list.
- Invalidation or expiry: Recompile regenerates derived outputs/refs; refs-check independently compares against fresh compilation. No expiry schedule or automatic source watcher is established.
- Activation or effect: Synchronous writes and configured checks are wired; site content/links/navigation derive from consumed files. Successful generation is unobserved.
- Evidence limits: A pass reflects enabled checks; outputs can already exist after failure. Semantic truth, host compliance, peer correctness and deployed publication remain unestablished.

Check authority is deterministic accept/reject for configured mechanical criteria, not an answer oracle for prose truth. Mode: caller-invoked batch validation. No model proposes these diagnostics. A caller controls permissiveness; CI can veto within its own job. The check action regenerates refs before checking, whereas refs-check does not write them. Thus a check pass alone is not evidence that a prior on-disk registry was already fresh. Backups move existing output before writing; absent backup, overwrite is direct, and refs writes have their own plain JSON write path. No automatic all-output rollback is inspected.

> if (warnBrokenLinks) return 'warn';
> return config.lint?.links?.severity ?? 'error';
> --- `packages/mdcp-cli/src/compile-workspace.ts`

> if (config.lint?.links?.enabled === false) return [];
> --- `packages/mdcp-cli/src/compile-workspace.ts`

> console.info(`→ ${msg}`);
> return { ran: false, skipped: true, exitCode: 0 };
> --- `packages/mdcp-core/src/peers/resolve.ts`

> genRefs(workspace, refsPath, refsOutputs);
> const refsResult = checkRefs(workspace, refsPath, refsOutputs);
> --- `packages/mdcp-cli/src/cli.ts`

> if (!opts.skipVale) {
> --- `packages/mdcp-cli/src/cli.ts`

> if (hooks === undefined) {
>     return [...DEFAULT_COMPILE_HOOKS];
> }
> --- `packages/mdcp-core/src/config/resolve-compile-hooks.ts`

The last passage also matters to the separate hook route: defaults are conditional, not intrinsic properties of all compiled output. The `sectionFiles` fallback and explicit selection precede assembly; loading one shard as an agent policy is not equivalent to the compiler's potentially transitive traversal. SRC-1, `packages/mdcp-core/src/compile/section-manifest.ts`.

#### RT-RTE-doc-review
Label: Sprawl diagnosis and documentation revision

Endpoints: requested review/sprawl trigger → mechanical findings → host-agent interpretation → revised shards/indexes or leave decision → checks/review again. The CLI reports warnings; the agent owns semantic decisions and host tools own edits. SRC-1, `packages/mdcp-core/src/validate/review.ts`, `packages/mdcp-cli/src/cli.ts`, `skills/mdcp/references/workflows/doc-review.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: CLI emits warning findings as text/JSON; strict mode sets failure on any finding. The workflow calls for one-line action rationales.
- Later read-back: Edited shards/indexes and optionally tuned review thresholds, glossary or Vale rules are available to later agent/check invocations.
- Delegated visibility: inapplicable — the review workflow assigns four lenses to one review pass, not four implemented workers.
- Selection predicate: Guide index first, shards indicated by signals next, then sample the rest; optional guide filter retains cross-guide duplicates involving that guide.
- Invalidation or expiry: Workflow removes superseded paragraphs and updates links after moves/renames; default CLI review does not mutate or expire content.
- Activation or effect: Signals invite merge/split/move/reword/link/delete/leave; only subsequent agent edits admit revisions.
- Evidence limits: Mechanical signal implementation and decision instructions are inspected; no trace establishes revisions, criticism quality or improved documentation.

Trigger: explicit cleanup, session sprawl, or externally scheduled weekly review for actively changing projects. Proposer/decider: host agent interprets multiple reviewer lenses; human review follows local delivery conventions and can reject. CLI does not choose semantic replacements. Operating mode: open maintenance with configured mechanical thresholds, not a fixed answer curriculum. Answer oracle: no expected correct prose; duplication/size/title rules are diagnostics, not truth references. Proposed changes include guidance and validation policy. Rejection: leave is explicitly valid. Recovery: atomic groups, rerun compile/check/review and external Git history; no automatic semantic rollback.

> When the same finding keeps coming back, make it mechanical so the next review
> does not depend on someone reading closely: tune the `review` thresholds in
> `mdcp.config.json`, add a glossary entry for the term that keeps drifting, or add
> a Vale rule for the wording. Narrow a rule that flags the wrong thing; do not
> switch it off wholesale.
> --- `skills/mdcp/references/workflows/doc-review.md`

If treating this as a theory route, guidance says one audience/job per shard and one canonical owner per rule, with repetition explained as drift risk. Theory-builder conditions 1–4: condition 1 claimed (localized prose rules); condition 2 claimed (the agent is directed to decide using their content, not demonstrated consuming them); condition 3 uninspected (instructions to critique do not supply a completed content-directed criticism with blame/revision); condition 4 uninspected (the loop requests continued use, but no retained criticism and next-round trace is supplied). Addressability: source paragraphs/rules and individual files are inspectable/editable. Persistence: repository horizons can span sessions; attained use is unobserved. Learning: no capacity-improvement evidence. Reflection: recurrence can motivate changes to the review machinery, but both causal directions are not observed. Reflective/autonomous theory building and exercised self-improvement are not established by this route's prescription alone.

#### RT-RTE-hook-extension
Label: Programmatic compile-hook extension

Endpoints: importing core caller registers a function/name → assembly resolves configured names → callback returns replacement text. Symbolic JavaScript/TypeScript functions execute in the caller's Node process; natural-language shard content is transformed, not interpreted by an LLM here. SRC-1, `packages/mdcp-core/src/index.ts`, `packages/mdcp-core/src/compile/hooks.ts`, `packages/mdcp-core/src/config/resolve-compile-hooks.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Each resolved callback receives context/body and returns the next body string; absent hooks leave body unchanged.
- Later read-back: Generated text can persist through output writing; callback registration itself is a process-local Map, not durable learned state.
- Delegated visibility: Callback receives config, source/output paths and shared per-guide state; no sandbox or separate worker is created at this call site.
- Selection predicate: Omitted hooks use defaults; arrays replace defaults; object form filters default hooks; unresolved registered names are skipped.
- Invalidation or expiry: New registration under the same name overwrites the Map entry; lifetime otherwise follows the importing process.
- Activation or effect: Arbitrary supplied callback code can alter body before later link passes and output; a CLI JSON name does not itself import arbitrary code.
- Evidence limits: Public API capacity is inspected; no external caller's hook installation, current grant or successful execution is supplied.

Admission trigger: library caller registers a hook and selects its name. Proposer/decider: caller code/author; no MDCP approval/veto or answer oracle at registration. Mode: programmatic extension. Proposed change: transformation capability for this process, not a persisted skill update. Guidance is callback/context API plus selected hook pipeline. Recovery: caller can re-register/remove selection or restart; no versioned hook rollback is implemented in the inspected Map API.

> export function registerCompileHook(name: string, hook: CompileHook): void {
>   builtinHooks.set(name, hook);
> }
> --- `packages/mdcp-core/src/compile/hooks.ts`

> const hook = builtinHooks.get(name);
> if (hook) {
>   out = hook({ ...ctx, body: out });
> }
> --- `packages/mdcp-core/src/compile/hooks.ts`

#### RT-RTE-shard-import
Label: Mechanical source-to-shard import

Endpoints: `mdcp shard` config/source → md-tree extract/explode or directory copy → guide directories and compile-order file. CLI maps configured source variants; orchestrator owns deterministic effects and subprocess invocation. SRC-1, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-core/src/shard/orchestrator.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Files/directories are replaced; CLI says to edit shards and compile.
- Later read-back: Created shards are available for later compile/agent reads; content correctness and successful import are unobserved.
- Delegated visibility: npx md-tree gets source/output paths and inherited execution authority; it is an external parser, not an isolated agent.
- Selection predicate: Config chooses directory, H1 extraction or merged H1 indices and split levels; source is required at CLI entry.
- Invalidation or expiry: Orchestrator removes destination directories recursively before reconstruction; temporary working directory is cleaned in finally.
- Activation or effect: Text extraction/preamble promotion/copy/explode populates source documentation, without content-specific human approval in this code path.
- Evidence limits: Static orchestration only; dependency resolution/parser behavior and successful executable packaging are not established by this trace.

Admission: caller invoking the command supplies the source and mappings; software admits resulting text mechanically, not via semantic review or an answer oracle. Rejection: missing source/config/mapping/extraction throws or exits; no per-shard approval. Mode: deterministic migration/import. Recovery: temporary cleanup is wired but not destination rollback; external backups/Git are needed after destructive partial effects. Guidance is mapping/split configuration; what persists is imported Markdown and order text.

> execFileSync('npx', ['--yes', '@kayvan/markdown-tree-parser', ...args], {
>   stdio: 'inherit',
> });
> --- `packages/mdcp-core/src/shard/orchestrator.ts`

> rmSync(dest, { recursive: true, force: true });
> mkdirSync(dest, { recursive: true });
> runMdTree(['explode', srcPath, dest, splitLevel]);
> --- `packages/mdcp-core/src/shard/orchestrator.ts`

#### RT-RTE-skill-evaluation
Label: Maintainer evaluation and description optimization

Endpoints: maintainer-selected fixtures/prompts/assertions → host with/without-skill runs and grading/feedback → candidate skill edits; the vendored automated trigger subroute maps labeled queries/current description → repeated Claude calls → proposed description → repeated evaluation → best-description JSON. This is an included maintainer plane, not the production CLI loop. SRC-1, `docs/developer/live-skill-evals.md`, `tests/skills/mdcp/evals/README.md`, `.agents/skills/skill-creator/SKILL.md`, `.agents/skills/skill-creator/scripts/run_loop.py`, `.agents/skills/skill-creator/scripts/run_eval.py`, `.agents/skills/skill-creator/scripts/improve_description.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Trigger evaluator returns whether the temporary skill was invoked; optimizer returns best/final descriptions, score/history and exit reason. Broader live-eval workflow requests grading files/viewer feedback.
- Later read-back: Optimizer keeps prior descriptions/scores in history for next proposal calls; optional proposal logs persist prompts/responses. Skill installation requires updating frontmatter after selecting the returned candidate.
- Delegated visibility: Trigger calls run as Claude subprocesses in project root with environment inherited except CLAUDECODE; proposal calls receive skill content, failures and blinded history. Separate calls isolate conversation by invocation but not filesystem permissions.
- Selection predicate: Labeled query fixtures define trigger expectations; train failures guide proposals; with holdout, best candidate is selected by test passed count, otherwise train passed count.
- Invalidation or expiry: Temporary command file is deleted in finally; running trigger process is killed/waited on exit if still alive. History spans bounded iterations; stopping is zero train failures or max iterations.
- Activation or effect: New description becomes current_description in subsequent evaluations; returned best description does not itself overwrite the installed skill in run_loop.
- Evidence limits: No runs/results supplied. Trigger detection is not successful task execution; held-out selection is not an independent final untouched-test estimate. General skill-body revisions remain a prescribed human/agent workflow.

Proposal/decision/veto: computation proposes descriptions through Claude; deterministic train/test scoring selects an iteration; maintainer/user decides whether to edit/install it. Expected `should_trigger` labels are a real answer oracle for trigger behavior, supplied by eval data, not model judgment. Broader suites provide expected outputs/assertions; expected-workflow reads are transcript checks, not delegated truth judgments. Mode: bounded fixture experiments, distinct from open production tasks. Trigger: maintainer requests evaluation/optimization. Change: skill description or manually revised policy text. Admission: candidate selection inside optimizer, then explicit frontmatter edit and repository checks; there is no automatic production replacement here. Recovery: prior descriptions/history permit choosing an earlier candidate; published rollback is external.

> if train_summary["failed"] == 0:
> --- `.agents/skills/skill-creator/scripts/run_loop.py`

> blinded_history = [
>     {k: v for k, v in h.items() if not k.startswith("test_")}
>     for h in history
> ]
> --- `.agents/skills/skill-creator/scripts/run_loop.py`

> best = max(history, key=lambda h: h["test_passed"] or 0)
> --- `.agents/skills/skill-creator/scripts/run_loop.py`

> Take `best_description` from the JSON output and update the skill's SKILL.md frontmatter. Show the user before/after and report the scores.
> --- `.agents/skills/skill-creator/SKILL.md`

The proposer is guided to generalize failures rather than enumerate cases; the supplied skill text describes intended scope. What persists is candidate description text, scores, optional transcripts and ultimately authored skill policy, not updated weights. Theory-builder conditions 1–4: condition 1 afforded (localized candidate policy descriptions); condition 2 wired for delivering that description to skill-trigger evaluation, while semantic compliance remains unobserved; condition 3 uninspected (scores and a request for revisions do not establish formulated content-directed criticism and blame); condition 4 wired for feeding prior candidates/results into the next proposal, but criticism-driven theory iteration remains unestablished. Addressability: whole description replacement and editable prose; no automatic fine-grained assumption model. Persistence: in-memory rounds plus optional logs/output files and subsequent author-applied frontmatter. Learning: improved general capacity unestablished without results/attribution. Reflection: evaluator represents trigger outcomes and feeds changes affecting its next evaluated description, a wired bounded feedback capacity, not demonstrated reflection in production. Autonomous theory building is not established. For self-improvement, the bounded optimizer changes its next evaluated description, but installation into production and subsequent production behavior causally depending on it are unobserved; no exercised production self-improvement is attributed.

#### RT-RTE-release-admission
Label: Repository gate and manual release admission

Endpoints: repository change/PR → CI checks → maintainer merge/release dispatch → release plan and conditional publish job. Repository CI and release orchestration own progression, with external GitHub/npm services executing publication. SRC-1, `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `package.json`, `scripts/release-build.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CI logs/status and generated-output diff status; release planning summarizes changesets and detects missing releases before the conditional publish job.
- Later read-back: Changed packages/skill files and released artifacts can affect future installs; actual publication and consumer upgrade are unobserved.
- Delegated visibility: GitHub jobs receive declared permissions; release job uses release environment, write/OIDC permissions and required release token. Environment reviewer configuration is not frozen here.
- Selection predicate: Check runs on listed push/PR events; archived release workflow is manual dispatch, then changesets/missing-release outputs govern its release job.
- Invalidation or expiry: CI cancels stale concurrent checks; release preserves in-progress publishing and cancels superseded waiting/queued release runs in its plan.
- Activation or effect: Ordered static/docs checks and output diff can reject a CI run; release entry point can version/publish after its gates. Deployed merge enforcement is not established.
- Evidence limits: YAML/script wiring is not a successful run, verified protection setting, npm release result or security guarantee.

Trigger/proposal: repository authors propose changes to product, instructions or machinery; manual dispatch starts release. Admission: configured checks and external maintainer/GitHub decisions; rejection can occur through failing checks or withholding configured environment authorization, but actual reviewers and mandatory merge policies remain unknown. Mode: repository integration/release, not answer-oracle learning. Oracle: tests/configured checks provide bounded expected outcomes, not semantic truth of docs. Recovery: rerun/repair and missing-release detection are visible; inner publish-script recovery and package rollback are not assessed here. Release-build is a separate maintainer version-bump path: it edits selected manifests/skill metadata before running skill validation, and supports dry run, so validation is not universal pre-write authorization.

> - run: pnpm run skill:validate
> - run: pnpm run prepare:docs
> - run: pnpm run docs:check
> - run: pnpm run docs:compile
> - name: Ensure documentation outputs are up-to-date
>   run: git diff --exit-code
> --- `.github/workflows/ci.yml`

> on:
>   workflow_dispatch:
> --- `.github/workflows/release.yml`

### Claims

#### RT-CLM-context-discipline
Label: Small-context source-shard discipline

Claimed operation: agents should discover source shards rather than load compiled monoliths. This is natural-language policy, not an implemented context-size cap; direct host reads remain possible. SRC-1, `skills/mdcp/SKILL.md`; its consumer path is [RT-BAP-skill-host](#rt-bap-skill-host).

> - **NEVER** dump whole compiled output (a compiled guide or the monolith) into
>   context. Discover with host search (`rg`, IDE search), then read **one shard**
>   at a time.
> --- `skills/mdcp/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-host
Label: Installed skill to host-agent decisions

Consumer: foreground host inference, or optional isolated host agent. Channel: host skill discovery then Markdown reads of the skill/workflow and task-selected source shards. Force: interpreted instructions/contracts, not an API interception layer; host instruction precedence and permissions are external. Horizon: current work item and later sessions that reload the installed skill/repository docs. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`; [RT-RTE-feature-work](#rt-rte-feature-work). Presence/delivery does not establish compliance or benefit.

> Each kind of work has its own workflow file. Pick **one** for the current
> `WORK_ITEM` (one focused batch per branch), read that file, and follow its
> Process. Do not load the others.
> --- `skills/mdcp/SKILL.md`

## Annotations

none
