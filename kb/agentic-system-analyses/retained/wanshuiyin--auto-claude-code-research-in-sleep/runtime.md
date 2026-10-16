---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of Auto-claude-code-research-in-sleep: host-driven research stages, reviewer transports, acceptance/resume controls and harness-patch admission at the frozen partial-loop boundary."
run-id: AAS-2026-10-15-auto-claude-code-research-in-sleep-a8abf5f80cbb-01
reviewed-boundary: 26b95cfa0d8747078e9e43b42e20952709e561b8
---

# Auto-claude-code-research-in-sleep runtime report

## Runtime account

### Scope and evidence

ARIS supplies host-interpreted research workflows plus executable helpers, not the enclosing agent scheduler or model service. The [boundary](boundary.md) remains `complete artifact, partial loop`. All evidence below is SRC-1 at the frozen commit. Python control-flow findings are implementation evidence; skill and setup instructions are doctrine/design. No target code, tests, examples or providers were executed. Operation, compliance with prompts, quality improvement and performance benefit remain unobserved.

Additional inspection covers the complete Codex bridge, phase helper and review transition helper; the model-family classifier and provenance write/authorization functions; the complete corpus-write hook and reviewer-independence protocol; the pipeline and setup; experiment-bridge sanity/deployment instructions; review-loop nightmare, memory and stop-gate instructions; the Codex pipeline's provisional-state instructions; and the complete meta-optimize/meta-apply skills. These extend SRC-1 inspection without introducing another source. Queue internals, native Copilot evidence validation internals, wiki maintenance, paper audits, installers/update scripts, monitoring and most platform-specific paths remain uninspected here. Their availability is not an access failure or evidence of absent behavior. This baseline does not establish equivalent guarantees across them.

### Ordinary invocation and ownership

The plugin advertises research skills; `/aris:setup` instructs the host to check Codex installation/login, register the `codex` MCP key to the shipped Python bridge, establish `~/.aris/repo` if needed, and restart the host. Setup leaves the reviewer model in external Codex configuration and documents plugin updates through `claude plugin update aris@aris` (SRC-1, `.claude-plugin/plugin.json`, `commands/setup.md`). The executable host installation, MCP registration and plugin update mechanisms are external contracts, not ARIS-enforced deployment guarantees. Standalone skill calls are also material entry paths: entering the full pipeline is not a prerequisite to invoking a child skill.

An ordinary `/research-pipeline "direction"` is an open research request. The user supplies the direction and any project brief. The foreground host model reads natural-language skill instructions, resolves flags and decides subsequent tool/skill calls. Its current task context, project artifacts and downstream returns are the working state. The pipeline orders idea discovery, experiment implementation/deployment, iterative review, summary and optional paper production. It requests phase JSON persistence through a CLI but continues with a warning if the helper cannot be found. Thus state tracking is not a mandatory wrapper around all work (SRC-1, `skills/research-pipeline/SKILL.md`; [RT-RTE-research-pipeline](#rt-rte-research-pipeline)).

Default `AUTO_PROCEED=true` makes selection updates nonblocking; `false` ends the turn awaiting explicit human confirmation. This is not automatic per-content human approval. `HUMAN_CHECKPOINT`, deployment checkpoints and an explicitly selected interactive Feishu gate can introduce additional human decisions. The host executes effects through its own Bash, file, web and skill tools; GPU jobs and provider calls cross external execution boundaries. The skill's allowed-tools declaration names capability requests, not the current deployed permission set or proof of isolation (SRC-1, `skills/research-pipeline/SKILL.md`, `skills/experiment-bridge/SKILL.md`).

The experiment bridge reads the plan, generates code, requests optional code review, runs sanity, deploys milestones and parses results. The downstream instruction is more precise than the pipeline summary: sanity allows two patch attempts plus two clean reimplements, not the summary's three attempts. A milestone with at least ten jobs or teacher/student dependencies goes to the queue; the explicit otherwise rule sends other cases, including six to nine jobs, to `/run-experiment`. Queue reliability is a downstream claim, not inspected implementation here. Critically, unavailable Codex code review is explicitly skipped. Cross-model code review is therefore not an invariant prerequisite to experiment effects (SRC-1, `skills/experiment-bridge/SKILL.md`; [RT-RTE-research-pipeline](#rt-rte-research-pipeline)).

Review then proposes fixes, requests new experiments and repeats up to four rounds. Positive review requires score at least six AND verdict `ready` or `almost`; exhaustion reports unresolved issues rather than authorizing infinite retries. The terminal normal artifact is `NARRATIVE_REPORT.md` plus the pipeline report. Paper writing is off by default; if selected but venue or manual figures are missing, the instruction defers it rather than guessing. Optional HTML rendering is nonblocking. Successful optional writing returns LaTeX/PDF and improvement logs, but its audit implementation was not inspected (SRC-1, `skills/research-pipeline/SKILL.md`; [RT-RTE-review-transition](#rt-rte-review-transition)).

### Delegated reviewer and working context

The ordinary reviewer tool sends a prompt to an external Codex CLI subprocess through the shipped MCP bridge. The bridge sends JSON events/progress to the host and returns the last agent message plus thread ID; it does not return a complete transcript as the normal text result. Calls are serviced serially by its dispatcher, while a ticker answers pings and cancellation and defers other requests. Cancellation terminates the child; no hard runtime deadline or kill escalation is implemented in the inspected bridge. A completed event clears recoverable intermediate errors; `turn.failed` remains terminal. These are transport/result rules, not a guarantee of a correct review (SRC-1, `mcp-servers/codex-exec/server.py`; [RT-RTE-codex-call](#rt-rte-codex-call)).

The reviewer starts with selected task instructions and file pointers, rather than automatically inheriting the foreground window. ARIS's independence protocol prohibits executor paraphrases and leading findings, with an exception for the reviewer's own earlier feedback in the same thread. This is prompt discipline, not a filter enforced by the bridge. The bridge accepts arbitrary prompt text. A same-thread reply reloads saved model/config/sandbox/cwd options and delegates conversation continuity to `codex exec resume`; missing or unreadable option files silently produce empty options, allowing external defaults. Reapplying a model string does not pin weights or preserve an immutable provider endpoint (SRC-1, `skills/shared-references/reviewer-independence.md`, `mcp-servers/codex-exec/server.py`).

This delegation resembles a separate task frame: selected inputs enter another model context and a final response returns, while detailed tool activity is also streamed as events. It is not strict frame isolation: the reviewer can read shared files according to CLI permissions, its thread can persist, and notifications expose more than the final return. Host compaction itself is outside the inspected implementation. The pipeline's `COMPACT` option requests summary files for later session recovery; it does not implement context eviction. The review instruction requests verbatim reviewer-memory append before stop evaluation, and supplies that material to later rounds; revisions and retention semantics belong to the memory analysis (SRC-1, `skills/research-pipeline/SKILL.md`, `skills/auto-review-loop/SKILL.md`).

### Forcing cases and guarantee limits

Four source-selected challenges bound the ordinary account:

1. **Direct CLI instead of MCP.** Nightmare review explicitly bypasses MCP and invokes `codex exec` from Bash. It requests independent repository reading but does not pass explicit model, effort or sandbox flags in that command. MCP option replay and event conversion do not cover it. Neither direct CLI nor arbitrary host Bash is fenced by the ARIS bridge (SRC-1, `skills/auto-review-loop/SKILL.md`; [RT-RTE-codex-call](#rt-rte-codex-call)).
2. **Different stop paths.** Compatibility Copilot positives cannot stop directly; they escalate to a finalizer. Native Copilot instead requires host-event evidence and may stop directly after helper checks. Default Codex/Oracle/Agy positive-stop paths do not require independently attested model identity. A blanket statement that every successful review is verified cross-family would be false (SRC-1, `tools/review_gate.py`; [RT-RTE-review-transition](#rt-rte-review-transition)). Native evidence-helper internals and alternative reviewer transports remain uninspected.
3. **Durable provisional progress.** Mainline resume skips accepted/skipped phases; the shipped Codex pipeline deliberately enables provisional advancement. This is not acceptance. `--force` relaxes the completed-phase precondition, and `set skipped` can also advance resume. Neither API verifies a referenced verdict artifact or executes a deterministic verifier. The phase helper enforces label/provenance structure on its API, not authentic independent acquittal across filesystem writes (SRC-1, `tools/run_state.py`, `tools/provenance.py`, `skills/skills-codex/research-pipeline/SKILL.md`; [RT-RTE-phase-resume](#rt-rte-phase-resume)).
4. **Corpus-write alternate paths.** The optional hook denies recognizable Bash corpus writes, but permits Write/Edit, fails open on malformed input and is not a filesystem sandbox. The producer explicitly acknowledges uncaught `git apply`, variables, absolute paths and language APIs. Meta-apply supplies a fresh jury plus human landing protocol; the hook cannot enforce that protocol for Write/Edit. The producer also states that the intended pre-push integrity detector is not yet built (SRC-1, `templates/claude-hooks/corpus_write_guard.py`, `skills/meta-optimize/SKILL.md`, `skills/meta-apply/SKILL.md`; [RT-RTE-meta-landing](#rt-rte-meta-landing)).

The load-bearing guarantees are consequently local. The host/model owns following natural-language stage and landing rules: strength **protocol**, design conclusion **claimed**, operation conclusion **uninspected**. `evaluate_transition` owns deterministic stop decisions: strength **invariant** for returned decisions given its inputs, implementation conclusion **wired**, operation conclusion **uninspected**; a cooperating host must actually call and obey it. `run_state` owns allowed status transitions and persisted resume selection: strength **invariant** for those API paths, implementation conclusion **wired**, operation conclusion **uninspected**; file integrity, truthful caller identities and single-writer coordination remain external contracts. Its POSIX lock is advisory, and unavailable `fcntl` means no lock; same-directory atomic replace protects individual saves, not arbitrary writers. The optional Bash guard owns only matched command denial: strength **best effort**, implementation conclusion **wired**, deployment conclusion **uninspected**, operation conclusion **uninspected**. CLI sandbox behavior belongs to the external CLI, not this repository. None of these establishes successful unattended research.

### Change admission

Research-product changes are proposed and implemented by the foreground model under plan, sanity, review and optional human-checkpoint instructions; reviewers can request changes but are not answer oracles. Empirical results and sanity expectations are task evidence, not a supplied universal reference answer. The phase helper records claimed acceptance separately from execution completion. Harness changes use a distinct log-analysis → patch staging → human-invoked fresh jury → Write/Edit landing → provenance receipt path. The downstream consumer is a later host invocation of the edited skill, not model-parameter training. The mechanism is improvement-directed but exercised self-improvement is unestablished: no supplied trace closes evidence→update→live consumption→dependent later behavior. Knowledge-maintenance paths and broader installation/update variants are not assessed here (SRC-1, `skills/meta-optimize/SKILL.md`, `skills/meta-apply/SKILL.md`; [RT-RTE-meta-landing](#rt-rte-meta-landing), [RT-BAP-skill-instructions](#rt-bap-skill-instructions)).

## Shared records

### Components

#### RT-CMP-claude
Label: Foreground host model

Source-native identity: Claude executor in the mainline skills. Form: distributed-parametric model behind an external host/service, not stored in this repository. Storage substrate and provider internals are uninspected. The skill supplies natural-language procedures consumed by this component; host tool execution is distinct from inference. No inspected ARIS code updates its parameters during a run; actual provider parameter mutability is uninspected. Exact model version is not pinned by the pipeline; a mutable host endpoint/configuration can select another model, with resolution outside the repository. Evidence: SRC-1, `skills/research-pipeline/SKILL.md`, `tools/run_state.py` (default executor label `claude` is provenance, not a weight pin).

#### RT-CMP-codex
Label: External Codex reviewer model

Source-native identity: Codex/GPT reviewer, commonly requested as `gpt-6-astra`. Form: distributed-parametric inference component accessed via external CLI/provider; weights and provider state are outside the checkout. No inspected bridge path changes parameters. Actual provider updates are uninspected. The exact model version is not pinned: tool argument or external config supplies a name, and a mutable endpoint may resolve differently. Replaying saved options preserves requested configuration, not immutable weights. Evidence: SRC-1, `commands/setup.md`, `mcp-servers/codex-exec/server.py`.

> The reviewer model comes from `~/.codex/config.toml` (ARIS assumes
>   `gpt-6-astra` at `xhigh`); nothing here changes it.
> --- `commands/setup.md`

Other reviewer backends are opaque alternatives in [RT-RTE-review-transition](#rt-rte-review-transition), not evidence that these two models exhaust deployed components.

### Operative objects

#### RT-OBJ-run-state
Label: Phase-state JSON

Source-native identity: `<root>/.aris/runs/<run_id>.json`. Form: symbolic status/provenance/configuration fields in filesystem JSON. Artifact and verdict values are handles, not the artifacts themselves. Stored executor/reviewer names are classified strings, not identity attestations. Ordered phases, policy and statuses determine the next resume phase. Each save uses a unique same-directory temporary file and `os.replace`; an advisory per-run lock is available on POSIX. This is ordinary run/recovery state; recording it alone establishes no learning. Evidence: SRC-1, `tools/run_state.py`.

#### RT-OBJ-skill
Label: Editable skill instruction body

Source-native identity: target `SKILL.md` files selected by meta-optimize/meta-apply. The procedural body is natural-language content stored as Markdown on disk; host-interpreted frontmatter/tool metadata is a distinct consumption surface whose enforcement is external. Proposed changes are stored as symbolic unified diffs before landing. Provenance sidecars contain symbolic process receipts and content hashes, not correctness certificates. Evidence: SRC-1, `skills/meta-optimize/SKILL.md`, `skills/meta-apply/SKILL.md`, `tools/provenance.py`. Authority after landing is [RT-BAP-skill-instructions](#rt-bap-skill-instructions).

### Routes

#### RT-RTE-research-pipeline
Label: Host-driven research pipeline and product revision

Endpoints/progression: human direction/project brief → host skill orchestration → idea report/plan → experiment code and results → reviewed fixes → narrative report → optional paper. Owner: foreground agent under host execution; subordinate skills return handoff artifacts. Decision policy is natural-language staged workflow with flags, budget and quality rules; fixed helper checks are local substeps rather than an encompassing executor.

- Immediate return: progress messages and final pipeline/narrative paths; optional PDF and logs if writing completes.
- Later read-back: experiment plan/results and review artifacts feed subsequent stages or resumed invocations; `COMPACT` requests additional recovery summaries, not parameter changes.
- Delegated visibility: child skills receive arguments and named project artifacts; reviewer gets its assigned context, not necessarily the complete foreground window.
- Selection predicate: argument flags and chosen idea; experiment milestones with at least ten jobs or phase dependencies route to queue, otherwise direct run skill.
- Invalidation or expiry: failure and unfinished acceptance lead to retry/re-audit instructions; no uniform artifact TTL established in inspected stages.
- Activation or effect: requests code/file changes, remote experiment effects through host tools, result interpretation and optional publication artifacts; compliance is not observed.
- Evidence limits: pipeline fully read; experiment sanity/deployment passages inspected, but queue executor, paper audits, child literature/idea loops and actual deployment uninspected.
- design conclusion status: claimed
- operation conclusion status: uninspected

Admission: model proposes and implements product changes; reviewer supplies critiques; user can veto at blocking selection/deployment/review checkpoints when enabled. Defaults do not require per-change approval. Trigger is an open research problem, followed by task-scoped experiments and review feedback, not a fixed answer curriculum. Answer oracle: no general expected research answer supplied; task plan success criteria and deterministic job completion are narrower checks. Guidance: experiment plan, project conventions and skill instructions. What persists: plans, generated code, metrics, trackers and final reports. Rejection/recovery: stop on exhausted sanity budget or unsuccessful fourth review; re-run with revised direction, with clean reimplementation limited to generated attempt code. Product rollback beyond that is uninspected. Theoretical hypotheses appear in artifacts, but this route alone does not establish content-directed scientific theory revision; that assessment needs the child idea/review mechanisms.

Evidence: SRC-1, `skills/research-pipeline/SKILL.md`, `skills/experiment-bridge/SKILL.md`.

> **Codex MCP unavailable** → skip silently, proceed to Phase 3 (graceful degradation)
> --- `skills/experiment-bridge/SKILL.md`

> Budget exhausted (2 patches + 2 reimplements), or two reimplements failed the SAME
>   way?** → stop, report the failure with all attempted fixes and error logs.
> --- `skills/experiment-bridge/SKILL.md`

#### RT-RTE-codex-call
Label: MCP reviewer subprocess and continuation

Endpoints/progression: host MCP request → `handle_call` → `build_argv` → external `codex exec`/`resume` → streamed events → result conversion. Owner: bridge controls launch/transport; external CLI owns agent actions and provider access. Symbolic Python rules construct argv; natural-language prompt is sent on stdin without a shell. Effects are the child's permitted filesystem/network/tool actions, not constrained by prompt wording alone.

- Immediate return: JSON-RPC tool result with `threadId` and last agent message; errors set `isError`; events/progress stream separately.
- Later read-back: saved per-thread model/config/sandbox/cwd options are reloaded for a matching reply; CLI owns conversation storage/read-back beyond those options.
- Delegated visibility: initial prompt and CLI-accessible working directory/resources; final message and event notifications cross back. Full transcript is not the normal text return.
- Selection predicate: tool name selects new call or thread continuation; caller supplies model/config/sandbox/cwd, or CLI defaults apply.
- Invalidation or expiry: no option TTL; missing/malformed records return empty options. Persistence errors are swallowed, so continuity is best effort.
- Activation or effect: bridge wires subprocess invocation and result delivery; model actions and semantic effect on foreground behavior are unobserved.
- Evidence limits: bridge fully inspected, external CLI/provider and actual sandbox deployment uninspected. Nightmare direct Bash invocation bypasses this bridge.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Capability surface: accepted sandbox names include read-only, workspace-write and danger-full-access; config accepts arbitrary additional settings. Current grant set: uninspected — no deployed host tool configuration supplied. Isolation envelope: uninspected — CLI and host enforcement external. The bridge offers no approval-policy argument and imposes no independent filesystem boundary. It remembers supplied sandbox settings, but arbitrary config and direct CLI are material alternate paths. Cancellation terminates the child; no recovery resubmission is automatic. A later caller can resume a thread explicitly.

Evidence: SRC-1, `mcp-servers/codex-exec/server.py`, `skills/auto-review-loop/SKILL.md`.

> SANDBOX_MODES = ["read-only", "workspace-write", "danger-full-access"]
> --- `mcp-servers/codex-exec/server.py`

> **Do NOT use MCP.** Instead, let GPT access the repo autonomously via `codex exec`:
> --- `skills/auto-review-loop/SKILL.md`

#### RT-RTE-review-transition
Label: Backend-specific review stop decision

Endpoints/progression: completed reviewer response → host parsing and memory append → `review_gate.py` → stop/continue/escalate/unavailable JSON → host next round/final report. Owner: deterministic transition helper decides from supplied fields; host orchestrator must invoke and obey it. The model reviewer proposes score/verdict/action items; the executor implements fixes. This is open task review with bounded rounds, not an answer-oracle mode. A score is judgment, not an expected answer.

- Immediate return: symbolic `decision`, `next_backend`, external-acquittal obligation, identity-assurance label and reason.
- Later read-back: instruction persists backend/obligation in `REVIEW_STATE.json`; later rounds also receive reviewer memory. The executable helper itself is stateless.
- Delegated visibility: ordinary routes pass model strings and parsed score/verdict; native Copilot loads evidence and response via another helper. Compatibility finalizer receives the project review task rather than a trusted acquittal log.
- Selection predicate: backend actually used this round, finite score in 1..10, valid verdict and backend-specific identity/evidence/finalizer conditions.
- Invalidation or expiry: invalid inputs/evidence or unavailable finalizer produce review-unavailable; failure to resolve/execute helper is instructed to terminate. Native evidence expiry/authenticity beyond the inspected loader is uninspected.
- Activation or effect: local code computes a next-step decision; only host consumption changes the live loop. Positive stop does not establish scientifically correct conclusions.
- Evidence limits: complete transition helper and stop instruction inspected; native evidence validator, reviewer transports other than Codex, and end-to-end host compliance uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: reviewer judges the product; helper can reject malformed/forbidden stop paths; host controls action effects; optional human checkpoint can alter subsequent fixes. No human is required for a default positive review. Ordinary negative reviews continue on the same backend. Compatibility Copilot positives escalate: OpenAI executor needs a manual non-OpenAI finalizer; other known executor families prefer available Codex then manual. Native Copilot requires revalidated evidence, known unequal families and matching response score/verdict; its reported assurance is `host_event_verified`, whose trust boundary includes uninspected host-evidence machinery. Manual requires reported identity; llm-chat requires declared unequal known families. Default Codex/Oracle/Agy stops on positive without the Copilot-finalizer identity obligation. Thus family assurance is path-specific, not universal. No product rollback is performed by this helper.

Evidence: SRC-1, `tools/review_gate.py`, `skills/auto-review-loop/SKILL.md`.

> positive = score >= 6 and normalized_verdict in POSITIVE_VERDICTS
> --- `tools/review_gate.py`

> if backend in {"codex", "oracle-pro", "agy"} and not requires_external_acquittal:
> --- `tools/review_gate.py`

> This is fail-closed route consistency, not independent executor attestation.
> --- `skills/auto-review-loop/SKILL.md`

#### RT-RTE-phase-resume
Label: Phase acceptance and resume selection

Endpoints/progression: caller's status/verdict arguments → phase API → filesystem JSON → `resume_point` returns first nonterminal phase. Owner: phase helper enforces symbolic field/status rules; foreground orchestrator determines whether real work and review happened. `accept` checks nonempty verdict/reviewer and, unless forced, completed state; it classifies declared model families and refuses unknown/same-family model acceptance. Deterministic reviewer labels are permitted without executing the named verifier.

- Immediate return: updated state/status or selected phase; CLI resume prints `COMPLETE` if none remains.
- Later read-back: later resume reloads run JSON and uses stored phase order, statuses and provisional policy.
- Delegated visibility: artifacts/verdicts are retained handles; helper does not deliver their contents or verify their provenance to reviewers.
- Selection predicate: first phase outside accepted/skipped, additionally skipping provisional only when per-run `provisional_advances` is true.
- Invalidation or expiry: failed/running/done phases remain resume targets; no artifact freshness/TTL verification; existing start is idempotent, not destructive.
- Activation or effect: persisted status changes the next requested stage if the host consumes resume output; it does not itself execute the stage or verifier.
- Evidence limits: full phase helper and family classifier inspected; arbitrary JSON edits and truthful reviewer labels are outside its enforcement. No actual crash/resume trace supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles: host supplies stage identity, verdict and reviewer; helper can veto invalid status/family strings. Human contribution is unresolved for individual API calls; generic caller identity is not per-verdict approval. Operating mode is workflow recovery, not research answer validation. Answer oracle: inapplicable — this helper records acceptance metadata rather than determining a task's expected answer. `--force` changes status precondition but not family check. `set skipped` is permitted without a verdict, and same-family provisional advancement is a deliberate shipped alternative. Rollback is possible through permitted status mutation or external file restoration, not an authenticated monotonic history. Single-writer contract plus advisory lock and atomic saves mitigate concurrency only within cooperating API writers.

Evidence: SRC-1, `tools/run_state.py`, `tools/provenance.py`, `skills/skills-codex/research-pipeline/SKILL.md`.

> if (state.get("policy") or {}).get("provisional_advances") is True:
>         base.add("provisional")
> --- `tools/run_state.py`

> A fresh Codex reviewer PASS uses `mark-provisional --reviewer gpt-6-astra
>   --verdict-id <trace-or-agent-id>`. This is terminal for resume but not accepted.
> --- `skills/skills-codex/research-pipeline/SKILL.md`

#### RT-RTE-meta-landing
Label: Trace-guided harness patch proposal and landing

Endpoints/progression: accumulated usage events and prior bottleneck ledger → meta-optimize diagnosis/diffs/advisory review/report → human-selected staging → separately human-invoked meta-apply → fresh Codex jury on staged diff/target → Write/Edit application, backup, provenance stamp and log → later skill invocation. Owners: producer model proposes; human chooses patches and invokes landing; fresh reviewer can KILL; applier performs mutation. Operating mode is open-ended maintenance from usage records, with optional trigger-rate probes, not a fixed correct-patch oracle. No known expected answer is supplied; PASS/KILL is model judgment.

- Immediate return: producer report and pending diffs, then applier LANDED/REFUSED result, backup and receipt paths.
- Later read-back: later cycle reads bottleneck ledger/report and changed skill; subsequent host invocations can consume landed instructions. Actual later consumption is not observed.
- Delegated visibility: landing jury receives staged diff and target paths in a fresh thread, not producer verdict as authority; advisory pre-screen can contain pasted material.
- Selection predicate: user names patch/all; fresh jury PASS plus recognized cross-family author/reviewer; unchanged accepted hash receipt governs eligibility for automatic curation through `is_auto_curatable`.
- Invalidation or expiry: KILL/unknown/same-family refuses landing by procedure; modified content invalidates hash-based auto-curation eligibility when checked. TTL/revocation auditor is recommended, not built in inspected implementation.
- Activation or effect: requests modification of behavior-bearing skill text, with implemented sidecar stamping; a future host must load and interpret it. No exercised beneficial behavior change established.
- Evidence limits: both skill procedures and provenance functions inspected; optional logging hooks, capture filter, trigger evaluator and any deployed integrity monitor not inspected. Landing itself is a model-followed procedure, not an atomic privileged service.
- design conclusion status: claimed
- receipt implementation conclusion status: wired
- operation conclusion status: uninspected

Admission and recovery: proposal guidance requires log-supported minimal changes and forbids deleting privilege boundaries/review gates. Human selects survivors but cannot override jury KILL under the protocol. Before mutation the applier copies target to backup; restoration is the rollback route. The applier writes a receipt AFTER editing, so stamp refusal is not an automatic transactional rollback. The optional Bash blacklist is supplementary, not a complete separation of privileges; Write/Edit discipline is expressly procedural. `stamp` authenticates neither reviewer execution nor verdict correctness; the receipt stores caller strings, a verdict handle and hash, and rechecks family relation. `is_auto_curatable` rechecks accepted fields and current content hash but only protects consumers that call it.

Evidence: SRC-1, `skills/meta-optimize/SKILL.md`, `skills/meta-apply/SKILL.md`, `tools/provenance.py`, `templates/claude-hooks/corpus_write_guard.py`.

> **This is a blacklist,
>   NOT a complete sandbox**
> --- `skills/meta-optimize/SKILL.md`

> that discipline is procedure, not a hook-enforced mechanism
> --- `skills/meta-apply/SKILL.md`

> The stamp is a **process receipt**
>    (who authored, who acquitted-at-landing, content hash) — NOT a claim the change is
>    correct.
> --- `skills/meta-apply/SKILL.md`

Theory account: the revised localized content is the method stated in a skill: stage ordering, scope conditions, retry/stop rules and reviewer guidance. The producer is instructed to criticize it against usage failures, interventions and model changes, attach why/data to each diff, and retain report, patches and bottleneck succession for the next cycle. This supports a requested reflective method-revision loop, not a witnessed theory-building episode. Theory-builder conditions 1–4, assessed independently: **1 localized content — afforded**, whole skill sections/rules are inspectable and replaceable; **2 consumption — claimed**, later skill invocation is the designed reader but no changed-content dependency trace supplied; **3 content-directed criticism — claimed**, instructions require target-specific evidence/rationale, but no actual criticism placing blame and revising reliance supplied; **4 iteration — claimed**, prior-cycle bottleneck/report is requested input to next analysis, without an observed next cycle. Addressability is rule/section-level in visible Markdown and diffs; no claim about opaque model reasoning. Persistence spans proposed cycles/sessions through disk artifacts; attained use horizon unobserved. Learning: improved future capacity is unestablished, not inferred from acceptance. Reflection: own skills and usage outcomes are represented and can influence proposals, and landed text can influence future calls; both directions are designed, exercised closure unobserved. Reflective theory builder: claimed method, conditions 2–4 not observed. Autonomous theory builder: this path deliberately requires internal human patch choice/landing, so fully computational autonomy is not established. Self-improvement boundary is ARIS skill organization across maintenance cycles; objective is fewer failures/interventions and better workflow operation, specified before the patch. Standing improvement-directed self-change is afforded; exercised membership and successful improvement remain unestablished because live later use and causal dependence are not supplied.

### Claims

#### RT-CLM-review-independence
Label: Unfiltered independent reviewer input

Claimed operation: reviewer reads primary artifacts without executor framing, reducing shared blind spots. Source is a universal review protocol, with same-thread feedback exception. Its force is instruction, not enforced input sanitation; the bridge accepts arbitrary prompts, and meta-optimize's advisory review explicitly pastes original section, diff and summary statistics. Actual independence/reduced error is unobserved. Evidence: SRC-1, `skills/shared-references/reviewer-independence.md`, `skills/meta-optimize/SKILL.md`, `mcp-servers/codex-exec/server.py`.

> **Content must reach the reviewer unfiltered. The executor points to files and sets the review task; the reviewer reads and judges independently.**
> --- `skills/shared-references/reviewer-independence.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-instructions
Label: Landed instruction to future host behavior

Consumer: foreground agent model on a later skill invocation. Channel: installed/read skill Markdown, with host tool/skill discovery external. Force: procedural natural-language direction interpreted by the model, not a guaranteed executable constraint. Horizon: later rounds/runs/sessions when the changed file is loaded; actual post-change load and activation unobserved. Source-native path: meta-apply edits target skill, then tells the user to test it next run. This gives a behavior-bearing destination to a proposed harness patch without proving improved capacity or exercised self-improvement. Evidence: SRC-1, `skills/meta-apply/SKILL.md`, `skills/meta-optimize/SKILL.md`.

> Remind the
> user a landed patch is revertable from its backup, and to test the changed skill next run.
> --- `skills/meta-apply/SKILL.md`

## Annotations

none
