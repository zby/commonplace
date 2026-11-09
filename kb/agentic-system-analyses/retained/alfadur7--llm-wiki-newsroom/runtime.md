---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "llm-wiki-newsroom runtime baseline: host-driven newsroom roles, deterministic tools, publication controls and instruction-change admission."
run-id: AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01
reviewed-boundary: "8e209cab483da544852d7213f0e25291d06d8a88"
---

# llm-wiki-newsroom runtime report

## Runtime account

### What runs, and what the repository supplies

This is a coding-agent-operated wiki, not an enclosing model runtime. Natural-language requests and nine slash commands enter an Editor-in-Chief routing procedure. Reporter and Columnist author content; Copy Editor runs quantitative checks; Desk reviews qualitative defects. Python tools build, inspect and export files. The external host executes model calls, supplies tool schemas and permissions, and implements agent contexts. These responsibilities must not be confused with the repository's role instructions. SRC-1: `CLAUDE.md`, `.claude/agents/editor-in-chief.md`, `.claude/agents/README.md`, `tools/build.py`.

> When the user makes a request in natural language or runs a slash command, these instructions route the work to the appropriate one of the five roles.
> --- `CLAUDE.md`

The implemented Python call paths below are source-inspected wiring. Role orchestration is a specified protocol interpreted by the host's models, not a Python scheduler in this repository. No target execution was performed. No supplied invocation trace was inspected for these paths. Activation, reliable compliance and resulting quality remain unobserved here. The boundary registers experiment artifacts, but this report does not turn their availability into evidence of runtime operation.

Additional SRC-1 coverage in this member comprises the role execution/model-routing sections, role frontmatter, query/news/export procedures, staleness runbook, build/lint/query/export dispatch and selected consumers, ingest prefilter, defect-record admission, and hook dispatch/chain detection. These supply implementation or doctrine/design evidence, not new sources or execution evidence.

### Ordinary invocation: ingest one source

[RT-RTE-source-ingest](#rt-rte-source-ingest) traces `/wiki-ingest <file>` from an operator's file argument to retained source/hub content and a completion report. Empty arguments stop with usage. The Editor-in-Chief owns routing and shared context, not content authorship. The Reporter reads the raw body and index/overview, matches URL first and path second against the generated source map, then authors or updates the source and eligible stubs. The model interprets natural-language layer rules; code consumes frontmatter, links and schema fields symbolically. The effect boundary is the shared repository filesystem, not a transactional draft store. Pages are written before final review and commit approval. SRC-1: `.claude/commands/wiki-ingest.md`, `tools/_ingest/prefilter_ingest.py`.

The author runs source lint; hub checks follow. Rebuild regenerates graph, clusters, contradictions, index and dependencies. Desk is mandatory for changed L2-2 targets and conditional for sources with at least seven `[fact]` claims and three citations. Defects return to the author, with escalation on the third same-cause failure. Contradiction consolidation follows Desk edits because claim IDs depend on claim text. The final batch rebuild/lint, log and defect-batch recording precede the completion report. This is the specified successful path; it is not evidence that every invocation follows it. SRC-1: `.claude/commands/wiki-ingest.md`, `.claude/agents/README.md`.

### Delegation and context boundaries

[RT-RTE-role-delegation](#rt-rte-role-delegation) is the ordinary scheduling protocol. Each anonymous role invocation has a fresh context and returns final text automatically, according to the target's host-facing account. Reviewers must read the shared filesystem and original grounding themselves. For three or more genuinely new sources, ingestion fans out one source per Reporter, then serializes shared hub/index/log changes. This isolates model contexts, not filesystem authority: source slugs are writer-owned by procedure, not by an inspected lock manager. Resuming by agent ID is a separate mode retaining context and is forbidden where freshness is required. SRC-1: `.claude/agents/README.md`, `.claude/commands/wiki-ingest.md`.

[RT-RTE-faction-authoring](#rt-rte-faction-authoring) is a material alternative: persistent named advocates, explicit messaging, transcript recovery and a fresh synthesizer. It is not ordinary parallel ingestion. The role frontmatter does not enforce tool bans for this mechanism, by the project's own account. Its context isolation depends on not reusing camp-framed teammates outside that task. The principal host contract is therefore consequential and unverified, rather than a deployed isolation guarantee.

### Controls challenged against alternate routes

| Control and owner | Enforcement point and strength | Covered path; forcing case; external contract | Conclusions |
|---|---|---|---|
| Preserve generated state/raw originals; repository hook author | `run_pre` in `.claude/hooks/dispatch.py`, registered for Write/Edit; invariant only for matching inputs under the host hook contract | Protected exact/glob paths and raw-path test reject with code 2. New raw Write with a `source: http...` line is allowed for fetch fallback; queue files are exceptions. CLI/shell writes do not enter this path. This is not filesystem immutability. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Separate role capabilities; role authors and caller | Role `disallowedTools` plus prose X-lists; policy with host-dependent named-tool enforcement | Anonymous role definitions declare bans; named teammates do not enforce them; Editor-in-Chief normally runs as main without frontmatter restriction; Bash can reach the same effects. Not a capability sandbox. | declaration conclusion status: claimed; operation conclusion status: uninspected |
| Complete review before publication; Editor-in-Chief/operator | Lint return codes plus instructed Copy Editor/Desk/publish sequence; protocol | Direct `build.py` and `export.py` do not check review approval. Legacy AGENTS/GEMINI mode requires lint but does not reproduce the full five-role chain. Staleness runbook exempts low-risk timeline/trail re-grounding from full Desk review. A universal Desk-before-every-write claim is false. | protocol conclusion status: claimed; operation conclusion status: uninspected |
| Finish opted-in repair chains; hook author/foreground agent | PostToolUse command/output marker detection and feedback code 2; best effort beyond detection | Detector requires a lint path plus `--yes` or `--fix` and a known stdout marker. It emits instructions after command execution, not an independent durable work queue. Commit ladder hook is advisory and may reach context after commit. | implementation conclusion status: wired; completion conclusion status: uninspected |

Evidence is SRC-1: `.claude/settings.json`, `.claude/hooks/dispatch.py`, `.claude/hooks/lint_chain_guard.py`, `.claude/agents/README.md`, `tools/build.py`, `tools/export.py`, `AGENTS.md`, `GEMINI.md`, `.claude/operations/staleness-reground-runbook.md`.

Minimum passages grounding the control limits:

> build.py reach these through the CLI (not Write|Edit), so they are unaffected.
> --- `.claude/hooks/dispatch.py`

> if (tool_name == "Write" and not Path(path).exists()
>                 and re.search(r"^source:\s*['\"]?https?://", content, re.MULTILINE)):
>             return None
> --- `.claude/hooks/dispatch.py`

> **Name-blocking is not a seal** — `disallowedTools` blocks the named tool, not the capability (a role could still reach the same effect via Bash).
> --- `.claude/agents/README.md`

> Advisory, never a block: the hook cannot observe whether the ladder already ran,
>     and blocking would stop the compliant commit along with the careless one.
> --- `.claude/hooks/dispatch.py`

Four selected forcing comparisons bound this account: anonymous versus named agents; Write/Edit versus shell/CLI writes; ordinary query versus optional save and no-QMD fallback; full build with a dry-run flag versus the contradictions-only branch. The last matters because `--dry-run` is not global no-write protection: the dispatcher passes it only to contradictions while other full-pipeline phases still run. All are source cases, not experimentally demonstrated bypasses. Provider-native tool internals, host permission prompts, deployed grants, remote execution and compaction remain uninspected external behavior. No claim of their absence is made.

### Consumption, maintenance and change admission

[RT-RTE-wiki-query](#rt-rte-wiki-query) distinguishes simple answers from approved saved syntheses. Graph CLI consumes persisted JSON, not raw originals. The optional QMD CLI subprocess forwards query/settings and streams results; the agent path instead requests structured MCP queries and retrieves page bodies. If QMD is absent, the procedure falls back to graph neighbors plus direct page reads. Optional hosted export intentionally omits source/entity/concept bodies; [RT-RTE-wiki-export](#rt-rte-wiki-export) specifies the separate reader channel and its uncertainty. SRC-1: `.claude/commands/wiki-query.md`, `tools/query.py`, `tools/_query/qmd.py`, `tools/_query/graph.py`, `tools/export.py`.

[RT-RTE-build-lint](#rt-rte-build-lint) explains the deterministic half of the cycle. Staleness re-grounding is a separately triggered runbook, not an automatic consequence of an advisory lint result: Columnist rewrites against current upstream context; high-risk narratives receive Desk review; timeline/trail use deterministic lint and main-session spot review. Root publication, large rewrites and external commits still require the operator. The runbook says staleness clears on commit because it uses git body-edit dates. This distinction prevents interpreting an advisory surface as completed maintenance. SRC-1: `.claude/operations/staleness-reground-runbook.md`.

> It is advisory (exit 0), so it only surfaces — it never blocks. Re-grounding is triggered separately by this batch (staleness has no `--fix`).
> --- `.claude/operations/staleness-reground-runbook.md`

News acquisition supplies an earlier alternate entry: interactive Reporter searches recommend items and wait for the operator; `--gap` asks a crawler to append candidates without per-query approval, but ingestion remains a separate explicit `/wiki-ingest inbox`. Inbox fetching retains failures for retry, then invokes ingest on landed raw files; WebFetch fallback is limited to short-content failures. Therefore queued, fetched, admitted and published are distinct stages. SRC-1: `.claude/commands/wiki-news.md`, `.claude/commands/wiki-ingest.md`.

[RT-RTE-guideline-change](#rt-rte-guideline-change) is the admitted route for changing the instructions and checker/skill surfaces that govern later work. It proposes and measures changes rather than establishing autonomous adoption. Tools persist structured evidence; the Editor-in-Chief and operator perform the interpreted selection/gates. This baseline leaves detailed memory transformations and epistemic property judgments to the specialist members. No exercised self-improvement or quality gain is inferred from the existence of the loop.

## Shared records

### Components

#### RT-CMP-opus
Label: opus authoring models

Source-native identity: `model: opus` in Reporter and Columnist role frontmatter. Representational form: distributed-parametric model supplied by the host; parameters reside outside the repository. The repository supplies prompts, not weights. No parameter-update operation is established by these inspected role routes; provider-side mutation is uninspected. Exact version is not pinned: the alias deliberately tracks a family generation and can resolve to another model. SRC-1: `.claude/agents/reporter.md`, `.claude/agents/columnist.md`, `.claude/agents/README.md`.

> Use family aliases, never version ids — an alias tracks its family's current generation instead of freezing the role on one.
> --- `.claude/agents/README.md`

#### RT-CMP-fable
Label: fable Desk model

Source-native identity: Desk frontmatter `model: fable`. Distributed-parametric, external host/provider storage. Exact version unpinned; alias can resolve to another model. Inspected review instructions do not update parameters; provider-internal changes are uninspected. Different-family review is an explicit design hypothesis, not measured benefit in this report. SRC-1: `.claude/agents/desk.md`, `.claude/agents/README.md`.

> That is unmeasured — the one run behind it had no same-family control, so the effect is not separable from "any fresh reviewer"; do not cite it as evidence the family mattered.
> --- `.claude/agents/README.md`

#### RT-CMP-sonnet
Label: sonnet Copy Editor model

Source-native identity: `model: sonnet` in Copy Editor. Distributed-parametric model externally stored; exact version is not pinned and alias resolution can change. No parameter-changing operation is specified on this route; provider internals remain uninspected. Its prescribed verdict source is deterministic lint, not independent model adjudication. SRC-1: `.claude/agents/copyeditor.md`, `.claude/agents/README.md`.

> The Copy Editor is pinned down-family (`sonnet`) because its verdict is `lint.py`'s exit code, not the model's judgment.
> --- `.claude/agents/README.md`

#### RT-CMP-session-model
Label: Editor-in-Chief session model

Source-native identity: Editor-in-Chief's inherited session model, not a repository-defined exact endpoint. Distributed-parametric component stored in the external host/provider. Version pinning and parameter changes during operation are uninspected; no training step is specified in the inspected orchestration procedure. Resolution can change with operator session configuration. SRC-1: `.claude/agents/editor-in-chief.md`, `.claude/agents/README.md`.

> **The Editor-in-Chief carries no `model`** — the orchestrator must follow whatever the operator is running, in both the main-thread and sub-Agent modes of Tool permissions exception 2 above.
> --- `.claude/agents/README.md`

#### RT-CMP-qmd
Label: QMD search backend

Source-native identity: external QMD binary/MCP service. This wrapper is symbolic Python on disk; vector and hybrid search name an opaque distributed-parametric dependency, whose individual models, storage, parameter mutation and version pinning are uninspected. Installed binary/MCP configuration, not this repository, resolves that dependency and may change independently. BM25 `search` is explicitly the no-LLM alternative. Do not attribute the authoring models' fixity to search models. SRC-1: `tools/_query/qmd.py`, `.claude/commands/wiki-query.md`.

> search   Full-text BM25 keywords (no LLM)
>   vsearch  Vector similarity only
> --- `tools/_query/qmd.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-source-ingest
Label: Source ingest and publication

Endpoints/progression: operator file/folder/inbox → Editor-in-Chief → Reporter authoring → deterministic checks and build → applicable Desk review/author ADAPT → final rebuild/lint/log → completion report. Shared Markdown files and generated JSON persist on disk. Operator supplies the request and gated approvals; models propose authored content and judge qualitative defects; software supplies dedup/schema/check results. Operating mode is open source-ingest requests, not a curriculum. Raw content supplies evidence, not an expected-answer oracle. Operator can reject gated publication; lint/Desk defects send work back; third same-cause failure escalates. Recovery is revision/re-lint or holding for the operator, not an inspected atomic rollback of all writes. Guidance is source/hub layer contracts; pages, links, log and defect records persist. SRC-1: `.claude/commands/wiki-ingest.md`.

> Race avoidance: two sub-agents never write to the same file simultaneously. `wiki/sources/<slug>.md` is isolated per slug. `wiki/entities/`·`wiki/concepts/`·`wiki/overview.md`·`log.md` are updated serially by main.
> --- `.claude/commands/wiki-ingest.md`

- Immediate return: completion report names page changes, contradictions, verification and cluster impact.
- Later read-back: retained source/hub pages and rebuilt indices enter later query and authoring contexts.
- Delegated visibility: each Reporter reads its raw and wiki context; main collects proposals/links/contradictions; reviewers read relevant files.
- Selection predicate: genuine-new prefilter for batches; URL match first, normalized path fallback; source Desk trigger and changed-L2-2 roster select reviews.
- Invalidation or expiry: body-changing updates revise dates; rebuild regenerates derived state; duplicate match updates existing content rather than guaranteeing no revisions.
- Activation or effect: prescribed writes and code rebuild capacity; subsequent behavior and content quality not observed.
- Evidence limits: orchestration is doctrine/design; prefilter/build code is implementation; raw originals and invocation traces unavailable here.
- protocol conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-role-delegation
Label: Anonymous role invocation

Endpoints: Editor-in-Chief to anonymous role agent and automatic final-text return. Owner chooses role, original grounding, prior output and relevant guide. Model routing decisions interpret prose; the external host owns actual scheduling and context construction. Each fresh role frame keeps its internal processing out of the caller context; report plus shared file effects cross back. This resembles selected inputs and a return value, but shared filesystem writes escape the frame and there is no inspected frame allocator. Resumed `agentId` carries context instead. Host compaction/eviction is uninspected. SRC-1: `.claude/agents/README.md`, `.claude/agents/editor-in-chief.md`.

> fresh per invocation; each ADAPT is a re-invocation that re-reads its GROUND.
> --- `.claude/agents/README.md`

- Immediate return: anonymous sub-agent final text reaches the caller according to the host-facing contract.
- Later read-back: inapplicable — this record concerns invocation frames; persistent file effects belong to authoring routes.
- Delegated visibility: selected original grounding, guide and predecessor output; reviewer also reads shared filesystem.
- Selection predicate: command traversal and layer/cycle ownership; ambiguous entry asks the operator once.
- Invalidation or expiry: fresh reinvocation replaces the task frame; resume retains it and must not be used for fresh-eye review.
- Activation or effect: role instructions request bounded author/reviewer behavior; effective host enforcement is not demonstrated.
- Evidence limits: host implementation, deployed grants and context isolation are outside SRC-1.
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### RT-RTE-faction-authoring
Label: Adversarial faction authoring

Endpoints: recurring contested-draft defect → Columnist eligibility judgment → Editor-in-Chief activation → two named camp authors → fresh anonymous Columnist synthesis → Desk → ordinary publication chain. The operator/Desk retain ordinary gate/rejection roles; no new answer oracle appears. Operating mode is a conditional open authoring workflow, not an experiment. Camp sources shape advocacy proposals; both cases and full grounding shape synthesis. Defects return to standard ADAPT. Named teammates persist until session end and must not be reused for neutral work; a missing message is recovered from transcript rather than replaced by self-review. SRC-1: `.claude/agents/README.md`.

> **Desk VERIFY₂ on the synthesis — non-waivable.** The faction procedure changes who authors, not what gets verified; it does not substitute for the qualitative gate.
> --- `.claude/agents/README.md`

- Immediate return: explicit `SendMessage(to: "main")` after ToolSearch preload; final text alone yields only an idle notification.
- Later read-back: shared drafts/synthesis can be read in later review; reuse of the camp agent for unrelated work is forbidden by procedure.
- Delegated visibility: disjoint advocacy-source sets, shared factual background allowed; synthesizer gets both cases and full grounding.
- Selection predicate: incompatible camps with at least two independent sources each and recurring bias/argument defect after at least one ADAPT; Columnist judges and Editor-in-Chief activates.
- Invalidation or expiry: teammates persist until session end; no shutdown tool in the target's stated contract.
- Activation or effect: persistent advocacy contexts feed fresh synthesis by protocol; benefit is not demonstrated.
- Evidence limits: named-agent tool bans are not enforced according to the target; brief compliance and host message delivery remain unobserved.
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### RT-RTE-wiki-query
Label: Wiki query and optional synthesis save

Endpoints: question → model classification into six types → graph/MCP/direct page reads → Reporter answer; explicit operator approval optionally starts Columnist synthesis → Copy Editor → Desk → publish gate/log. The operator chooses saving, not every sentence; models select and synthesize content. No fixed answer oracle is specified. Operating mode is open questions. The external QMD subprocess returns its own exit code; MCP query/get is an alternative, not the same adapter. Saved-content rejection/recovery uses author ADAPT and operator gates. SRC-1: `.claude/commands/wiki-query.md`, `tools/_query/qmd.py`, `tools/_query/graph.py`.

> If unstated·declined, end the turn — output only the answer, no save
> --- `.claude/commands/wiki-query.md`

> Search results (snippets·docids) are **only a lead** — pull the body via `mcp__qmd__get`/`multi_get` for facts·quotes·nuance before answering. Read the top ≤10 pages
> --- `.claude/commands/wiki-query.md`

- Immediate return: cited answer ending with Sources; optional save proposal.
- Later read-back: only approved saved synthesis is prescribed to enter retained wiki state; ordinary no-save answer is not a wiki write.
- Delegated visibility: Reporter receives question and retrieved pages; Columnist receives simple-answer material plus own additional reads on save.
- Selection predicate: question type, model-authored intent/lex/vec, optional edge filter and retrieval ranking; fallback is graph neighbors plus direct reads when QMD is not installed.
- Invalidation or expiry: uninspected — query does not itself establish a freshness/expiry check over all returned facts.
- Activation or effect: delivery into answer synthesis is requested; retrieval correctness and answer use are unobserved.
- Evidence limits: graph filters operate on persisted typed edges, not independent fact verification; QMD internals and source completeness are outside this inspected adapter.
- implementation conclusion status: wired
- protocol conclusion status: claimed
- operation conclusion status: uninspected

#### RT-RTE-build-lint
Label: Deterministic rebuild and repair surfaces

Endpoints: CLI/main agent → build phase dispatch or lint group dispatcher → generated files, diagnostics and optional repairs/rewrite instructions. Python code owns phase order and return-code aggregation, not model authoring. File-based symbolic fields/links feed generated JSON/Markdown. Full build order is graph, clusters, contradictions, index, dependencies. Lint's `--fix` is not one admission rule: some branches repair mechanical fields, others emit instructions for a model. `all --fix` deliberately disables explicit-only contradiction-theme regeneration. Returned chain status does not execute the chain. SRC-1: `tools/build.py`, `tools/lint.py`, `tools/_lint/hub_schema.py`.

> EXPLICIT_FIX_ONLY: set[tuple[str, str]] = {("contradiction", "theme")}
> --- `tools/lint.py`

> if name == "contradictions":
>             PHASES[name](dry_run=args.dry_run)
>         elif name == "clusters":
>             PHASES[name](cold=args.cold)
>         else:
>             PHASES[name]()
> --- `tools/build.py`

Mechanical admission is software-controlled once invoked; e.g. hub schema fix infers type/date but does not invent semantic tags/title/sources. Model rewrite blocks propose content subject to the ordinary role/operator gates; deterministic check results are criteria, not a reference answer to the substantive question. Recovery is rerun after correcting inputs or completing the indicated chain. No whole-pipeline atomic recovery is established by this dispatcher. Operating modes are diagnosis, mechanical repair and explicit authoring-chain entry.

- Immediate return: phase/check stdout and exit status; rewrite blocks/chain markers where needed.
- Later read-back: generated graph/index/dependency files feed subsequent retrieval and checks; semantic revisions use the authoring route.
- Delegated visibility: main invokes most tools directly; deliberate `/wiki-lint` report cycle uses Copy Editor per role protocol.
- Selection predicate: parser's phase/group/subcommand, accepted argument forwarding, explicit-only fix policy; edge-query filters are separate consumers.
- Invalidation or expiry: rebuild replaces derived artifacts; full `--dry-run` does not prevent non-contradiction phases from writing.
- Activation or effect: code writes derived artifacts/allowed repairs and returns diagnostics; emitted prose requires a later model consumer.
- Evidence limits: implementation inspected, no passing target test/run claimed; an rc=0 reflects selected check scope, not all semantic properties.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-wiki-export
Label: Exported reader context

Endpoints: Editor-in-Chief or direct CLI → `export.py` → merged Markdown, source locator, generated README and staged graph assets → operator upload/paste → external Claude.ai reader. Software selects folders and strips comments/rewrites links; the operator controls upload and instruction installation. Code does not invoke a hosted answerer or require publication approval internally. This is a distribution route, not per-answer admission or an answer oracle. SRC-1: `tools/export.py`, `.claude/commands/wiki-export.md`.

> Source bodies are not exported — they live in the graph
>     (reachable via #q=<slug>), and this index lets the LLM resolve a claim to the
>     right source slug for a deep link.
> --- `tools/export.py`

> **Paste this entire document into the Claude.ai project instruction field.**
> --- `.claude/commands/wiki-export.md`

- Immediate return: generated files, size/budget diagnostics and staging report.
- Later read-back: uploaded synthesis/directory content and pasted instruction document are intended for later hosted questions; graph links expose omitted details to readers.
- Delegated visibility: exported answerer receives only uploaded selections, not the local role runtime or complete wiki; operator must install instructions separately.
- Selection predicate: root meta plus five synthesis-related folder merges, underscore exclusion, cluster-assigned source locator; Core/Optional recommendations use priority-greedy estimated token budget.
- Invalidation or expiry: stale export Markdown is pruned against files produced this run; upload/paste refresh is an operator action, not automatic invalidation at the hosted consumer.
- Activation or effect: code produces/stages bundles; hosted installation, context loading and compliance remain unobserved.
- Evidence limits: omitted source/hub bodies cannot substantiate an export-completeness guarantee; claimed hosted context behavior is design text, not inspected provider implementation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-guideline-change
Label: Guideline change admission

Endpoints: operator feedback plus verifier-grounded defect corpus → Editor-in-Chief diagnosis/proposal → responsible instruction/checker/skill edit → verification ladder and applicable measurement → operator adoption/transition record → next cycle reading new guidance. The programmatic part validates and appends defect/transition records; it does not enforce substantive measurement or approval by merely accepting an `accept` value. SRC-1: `.claude/agents/editor-in-chief.md`, `tools/log_defect.py`.

> **Adoption always passes the operator gate** — the loop proposes and measures; it never self-adopts.
> --- `CLAUDE.md`

> if rec["decision"] == "accept" and rec.get("treatment") not in TREATMENTS:
> --- `tools/log_defect.py`

Trigger/proposed change: recurring failures or feedback prompt the Editor-in-Chief to identify an addressable mechanism and edit existing guidance by default. It must consult rejected directions, read touched files and compare alternatives under pruning/minimality criteria. The operator can veto policy/matrix/rubric changes before update and adoption at the gate. Blind reviewers classify hunks and defects; severe findings cause revision, with a three-rotation cap. Measurement-obligated substantive changes need a recorded accept before commit. If not accepted, hold commit and revert/isolate the edit before measurement; the operator decides extensions/reversion after non-convergence. Proposed capability and production-machinery changes expressed as skills/checks/hooks share these procedures; deployed tool grant changes are not established by editing their prose.

Operating modes: open feedback review plus type-specific bounded comparisons (deterministic before/after, blind rewrite/review, behavioral probes). Selection rule is at least one motivating improvement and no regression across motivating/fresh/fixed held-in/out slices. Fixed pages and sampled tasks are comparison material; qualitative model judgments are not a demonstrated expected-answer oracle. Guidance says what to measure; hidden provider processing and effectiveness of this admission regime remain uninspected. SRC-1: `.claude/agents/editor-in-chief.md`.

- Immediate return: proposal, review/measurement findings and accept/reject/defer decision records by procedure.
- Later read-back: revised instruction SoTs are required GROUND in a next cycle; transition corpus and rejected-direction notes inform future proposals.
- Delegated visibility: fresh blind reviewer gets diff without author deliberation, and later re-passes retain prior findings; type-specific measurement contexts follow the selected procedure.
- Selection predicate: addressability, recurrence/support prioritization, minimal-edit/blind-review ladder and applicable improvement/non-regression gates.
- Invalidation or expiry: rejection records discourage re-proposal; failed edits are isolated/reverted or held for operator decision; no automatic global rollback proved.
- Activation or effect: persisted instruction text can shape future model work if read and followed; exercised causal self-change or improved capacity is not established here.
- Evidence limits: instructions establish requested admission behavior; log writer establishes schema admission only, not truth of claimed deltas or actual operator approval.
- implementation conclusion status: wired
- protocol conclusion status: claimed
- operation conclusion status: uninspected

### Claims

#### RT-CLM-human-supervision
Label: Automated production with human supervision

Claimed operation: humans mainly set direction, rubric/threshold trade-offs and final acceptance; automated roles write and review prose. This is design doctrine, not a finding that every produced artifact was independently approved. SRC-1: `.claude/agents/README.md`.

> **Production is automated, supervision is human**. The human reviewer's work concentrates on adjusting guidance·conventions, not detailed proofreading.
> --- `.claude/agents/README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-role-guidance
Label: Role guidance to host agent

Consumer: host model running a named role definition or main-thread Editor-in-Chief. Channel: role system prompt, command procedure, explicit grounding reads and handoff. Force: natural-language policy interpreted by a model, with limited named-tool restrictions supplied by the host; not equivalent to OS isolation. Horizon: one invocation for fresh agents, session for named teammates, later invocations when revised SoTs are re-read. SRC-1: `.claude/agents/editor-in-chief.md`, `.claude/agents/README.md`.

> the role SoT loads as the system prompt.
> --- `.claude/agents/editor-in-chief.md`

#### RT-BAP-hook-feedback
Label: Hook feedback to foreground agent

Consumer: host's foreground model/tool executor. Channel: configured pre/post tool commands, stderr code 2 or JSON additional context. Force: selected tool-input blocking for `run_pre`; post-command chain feedback and commit/authoring advisories require model action. Horizon: the next continuation of the current session; no durable pending-task enforcement established by these hooks. SRC-1: `.claude/settings.json`, `.claude/hooks/dispatch.py`, `.claude/hooks/lint_chain_guard.py`.

> if not LINT_RE.search(command) or not MARKER_RE.search(stdout):
>         return 0
>     print(MSG_YES if YES_RE.search(command) else MSG_NO_YES, file=sys.stderr)
>     return 2
> --- `.claude/hooks/lint_chain_guard.py`

## Annotations

none
