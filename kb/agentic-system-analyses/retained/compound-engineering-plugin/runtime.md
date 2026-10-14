---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Compound Engineering Plugin runtime baseline: host-loaded skills, native implementation, cross-model transactions, shipping and change admission."
run-id: AAS-2026-10-13-compound-engineering-plugin-6ac79f4e7555-01
reviewed-boundary: "50532b00de523980010d97fe950965b35382a3b7"
---

# Compound Engineering Plugin runtime report

## Runtime account

### What runs, and who owns the next step

The plugin supplies coding-agent instructions and supporting programs, not an enclosing model/tool runtime. Its consequential work is planning, implementing, verifying, reviewing and shipping requested changes, and capturing and maintaining project reasoning for later work. The host owns model invocation, native tools, permissions and subagent scheduling. Executable plugin code handles resource registration, conversion/install and the external-worker controller. These responsibilities are distinct: registering an instruction is not implementing its prescribed behavior (SRC-1, `package.json`, `.opencode/plugins/compound-engineering.js`, `.pi/extensions/compound-engineering.ts`, `skills/ce-work/SKILL.md`).

Native entry paths include plugin manifests and the skill tree; Pi returns skill paths on resource discovery. OpenCode V2 registers skills and command callbacks; V1 supplies skill paths and command templates without overwriting an existing command name. Its command callback asks the host session to load and execute the named skill. The independent install CLI parses a plugin, converts it with a target handler, and writes host resources; it is not an implementation-worker dispatch ([RT-RTE-host-loading](#rt-rte-host-loading), [RT-RTE-resource-install](#rt-rte-resource-install)).

A representative ordinary invocation is an explicitly autonomous software request through `lfg`. The foreground host agent classifies the request; an implementation-ready plan goes directly to `ce-work`, a concrete defect goes to `ce-debug`, and an ordinary new change goes through `ce-plan`. Planning resolves output contract, scope, research, structure, review and handoff; it must not implement. Standard/Deep planning isolates research into specialist contexts and scratch dossiers, reads dossiers when their gist can change a decision, and always opens the learnings dossier when dispatched. It can read local solutions and configured packs; pack text is evidence, not instructions. The planner, rather than the pack resolver or researcher, owns the decisions and plan text (SRC-1, `skills/lfg/SKILL.md`, `skills/ce-plan/SKILL.md`, `skills/ce-plan/references/research.md`).

On the plan route, `lfg` invokes `ce-work mode:return-to-caller`. The implementation agent establishes a writable canonical checkout, protects existing dirt, selects its engine, derives bounded units, and selects evidence before behavioral edits. Native sequential work is inline; independent dependency layers use fresh native workers where available. Workers receive scoped plan excerpts and inherited restrictions. The foreground orchestrator inspects the actual tree, verifies and makes canonical commits. On return it reopens the plan, compares active units, verification contract and definition of done with the diff, and reports changed files, verification evidence, route/model facts and blockers. The caller then owns simplification, review, durable residual recording, conditional learning capture, browser verification and shipping. With a remote, this ends in a PR and CI-decided result followed by DONE; without one, commits remain local and all push/PR/CI-watch actions are skipped. Merge is not granted merely by invoking `lfg` ([RT-RTE-native-work](#rt-rte-native-work), [RT-RTE-lfg-shipping](#rt-rte-lfg-shipping)).

This is an inspected prescribed invocation, not an observed session. No target, tests, examples, host CLI or providers were executed. Operation, compliance, useful activation and benefit remain uninspected. Implementation evidence below supports exact executable checks; instruction evidence supports requested decisions.

### Material forcing routes and bounded guarantees

Three forcing cases change the interpretation of the ordinary path.

1. **Native shared-workspace workers versus isolated workers.** Native workers may share a checkout under exclusive ownership and no-index-write rules, or use harness isolation. A harness-isolated copy must verify its HEAD against the supplied base; isolated is not necessarily a faithful snapshot. No subagent mechanism selects inline work. Fresh contexts keep prior unit transcripts out and let only summaries/artifact paths and changes escape; this resembles a scoped frame, but the controller cannot prove what the external host actually places in a model window. These are model-facing policies, not plugin-enforced OS barriers (SRC-1, `skills/ce-work/references/execution-strategy.md`).

2. **Cross-model dispatch and integration.** The host selects one external recipient, records the egress source, route/intermediaries, packet and restrictions, initializes private state, prepares a detached worktree and starts a detached runner. The adapter obtains controller authorization before building the external prompt. The controller checks run/unit/attempt/job identity, runner argv, authorization bytes, packet paths/digests, workspace and result directory, then atomically binds the job. Completed authoring is terminalized into a transport commit; the host must inspect scope before calling the integration transaction. That transaction locks, preflights, applies without committing, runs host verification, reconciles tracked state, records evidence, commits, cleans up and releases. Failure restores or preserves blocked recovery state. A worker exit is not a canonical completion receipt ([RT-RTE-external-unit](#rt-rte-external-unit)).

3. **Autonomous shipping and unavailable external engines.** Return-to-caller mode does not own the shipping tail; standalone `ce-work` does. `lfg` is the explicit hands-off grant for pushing and opening a PR, but not ungranted irreversible actions. External `require` fixes recipient while viable yet still falls back to native when unavailable; it is not a guarantee that an external model must do the work. After a started attempt, fallback must await authoritative terminal/restoration evidence and controller authorization. No duplicate work is licensed by temporary lack of contact (SRC-1, `skills/lfg/SKILL.md`, `skills/ce-work/SKILL.md`, `skills/ce-work/references/cross-model-execution.md`).

| Load-bearing guarantee | Owner / enforcement / strength | Covered paths and alternate limits | External contract and status |
|---|---|---|---|
| Exact authorized external dispatch | Controller and adapter; `authorize-dispatch` before prompt construction; protocol | Bundled controller/runner/adapter path checks identity and packet, including substituted argv. Direct host shell calls or another extension's dispatch do not pass through it. Same-user mutable machinery is not a hostile-worker security boundary. | Runner metadata and controller files must remain trustworthy; implementation conclusion status: wired; operation conclusion status: uninspected. |
| Verification before canonical external commit | Integration transaction; subprocess exit plus semantic snapshot equality; protocol | `integrate` refuses a failing/mutating check and records recovery. Manual Git or direct controller subcommands do not become one atomic transaction merely by being available. Ignored caches/local databases are disclosed, not restored. | Verification command must actually test the intended behavior; Git and filesystem semantics are external dependencies; implementation conclusion status: wired; operation conclusion status: uninspected. |
| Bounded worker authority and no shipping inheritance | Foreground model's packet and workflow instructions; policy | Native/external workers are told not to commit canonically, ship, expand scope or schedule peers. External adapters approve all permission requests; worktree isolation prevents accidental overlapping edits, not out-of-workspace actions. | Host/tool permissions and worker compliance needed; implementation conclusion status: claimed; operation conclusion status: uninspected. |
| Complete caller return before shipping | Foreground model; structured return and `lfg` return gate; policy | Return-to-caller avoids standalone tail; direct standalone work has another finishing path. OpenCode loader only supplies instructions, not a parser that rejects a malformed model return. | Host must execute skill rules and caller must inspect evidence; implementation conclusion status: claimed; operation conclusion status: uninspected. |

The capability surface includes file edits, shell execution, native subagents, external write-capable agents and Git/PR operations. The grant set depends on the invoked skill and user request: a worker receives one unit, not canonical integration or shipping authority. The actual deployed isolation envelope is external. The bundled external adapter uses `--approve-all`, and its own contract calls every route cooperative; Codex shell restrictions and Grok edit restrictions are attributed route observations in that contract, not measurements in this analysis. Native dispatch deliberately omits a permission-mode override. There is no source warrant for a uniform plugin-wide sandbox (SRC-1, `skills/ce-work/scripts/cross-model-work.sh`, `skills/ce-work/references/cross-model-execution.md`, `skills/ce-work/references/execution-strategy.md`).

### Persistence, admission and coverage limits

Canonical Git commits retain product changes; private external run manifests, authorization files and receipts retain transaction/recovery state. These are symbolic control state, not automatically project-learning content. The external brief/packet is distilled, not a transcript; native research returns scratch dossiers rather than loading all raw research into the foreground window. Return-time reopening of the plan counters host compaction losses, but the plugin does not implement host compaction itself (SRC-1, `skills/ce-work/references/cross-model-execution.md`, `skills/ce-plan/references/research.md`, `skills/ce-work/references/return-to-caller.md`).

Learning capture and maintenance admit knowledge changes under model judgment and grounding, with mode-specific human decisions. The runtime record describes admission ownership and later planning delivery, leaving detailed retained-object and revision assessment to the memory analyst ([RT-RTE-learning-admission](#rt-rte-learning-admission)). Repository-local skill authoring is a different improvement plane: authors edit skill text against a standing authoring standard, mechanical guards and proportional fresh-context behavioral comparisons. Behavioral evals are best-effort, not CI gates; mechanical tests and manifest/release validation are CI steps. These support a proposed-change/testing pathway, not demonstrated learning or self-improvement ([RT-RTE-skill-authoring](#rt-rte-skill-authoring)).

Added inspection within SRC-1 includes complete OpenCode/Pi loaders, `package.json`, install command, work/plan/LFG/capture/refresh kernels, execution strategy, implementation loop, cross-model contract, return contract, capture assembly, refresh modes, repository-local authoring and evaluation references. Executable ranges cover controller dispatch authorization (`unit_workspace_jobs.py`), complete `cmd_integrate` (`unit_workspace_transaction.py`), adapter permission construction and handshake (`cross-model-work.sh`), and CI mechanical gates (`.github/workflows/ci.yml`). These are implementation or doctrine/design layers, not observed-run evidence. Converter writers beyond the install dispatch, controller resume/fallback internals, runner supervision internals, other review/debug/shipping skill references, release deployment internals and other host adapters remain available but not behaviorally audited here. This prevents exhaustive claims about every recovery branch, adapter permission or shipping gate; it does not establish their absence.

## Shared records

### Components

#### RT-CMP-host-model
Label: Foreground and native-worker models

Source-native identity: the active host's session model and inherited/selected native researcher or implementation-worker models. Representational form: distributed-parametric; substrate: external host/provider-served model weights, not files in this plugin. SRC-1, `skills/ce-plan/references/research.md`, `skills/ce-work/references/execution-strategy.md`.

Parameters changing during operation: uninspected — providers and hosts are outside the frozen source. Exact version pinned: no plugin-wide pin; researcher tier overrides are conditional, otherwise inherited. Mutable endpoint resolving to another model: uninspected — host/provider resolution is external. Fixed weights or absent in-plugin training cannot establish absence of learning through retained text.

> Use inherited model for high-judgment architecture, migration, and planning-deepening prompts unless the harness has an established cheaper capable tier.
> --- `skills/ce-plan/references/research.md`

#### RT-CMP-external-model
Label: Fixed-recipient external implementation model

Source-native identity: requested model associated with a controller route (`codex`, `claude`, `grok-cli`, `cursor`, `composer`, `grok-cursor`, `opencode`). Representational form: distributed-parametric; storage substrate: external model service. SRC-1, `skills/ce-work/references/cross-model-execution.md`, `skills/ce-work/scripts/cross-model-work.sh`.

Parameters changing during operation: uninspected — provider internals excluded. Exact version pinned: not globally; a model selector may be supplied, default/alias resolution remains host-specific and actual identity requires a receipt. Mutable endpoint resolving to another model: possible with defaults or aliases; actual served-model resolution uninspected. A fixed controller recipient is not immutable weights. acpx 0.19.4 pins transport, not a model.

> Disclose any compatible model alias or substitution, and never relabel an unverified served model.
> --- `skills/ce-work/references/cross-model-execution.md`

### Operative objects

#### RT-OBJ-skill-files
Label: Skill kernels and references

Source-native identity: `skills/<name>/SKILL.md` plus bundled references. Natural-language behavioral content on filesystem/package resources; frontmatter name/description/invocation metadata has symbolic loader consumers. These operative parts differ: code registers names and paths, while models interpret the bodies. SRC-1, `.opencode/plugins/compound-engineering.js`, `skills/ce-work/SKILL.md`.

> content: skill.content,
> --- `.opencode/plugins/compound-engineering.js`

#### RT-OBJ-run-manifest
Label: External controller run state

Source-native identity: private CE Work run state, per-unit authorizations and receipts, packet digests, transport refs and canonical-commit records. Symbolic JSON/control fields on local private filesystem plus Git refs/objects; packet prose is a distinct model-interpreted input, not an authorization rule by itself. Consumers include controller recovery/authorization/integration and the host building a structured return. SRC-1, `skills/ce-work/scripts/unit_workspace_jobs.py`, `skills/ce-work/scripts/unit_workspace_transaction.py`, `skills/ce-work/references/cross-model-execution.md`.

> attempt["dispatch_authorization_receipt"] = expected_dispatch_authorization_receipt
> --- `skills/ce-work/scripts/unit_workspace_jobs.py`

### Routes

#### RT-RTE-host-loading
Label: Native host resource loading

Endpoints/progression/owner: installed package skill tree → Pi resource discovery or OpenCode registration → host skill lookup → foreground model. OpenCode V2 command callbacks retain session identity/prompt/delivery; V1 mutates config and leaves conflicting command names intact. Symbolic loader rules select resources; model interpretation owns next steps. SRC-1, `.pi/extensions/compound-engineering.ts`, `.opencode/plugins/compound-engineering.js`, `package.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resources/registrations to the host; command callback submits a session prompt.
- Later read-back: inapplicable — static shipped skill resources, not use-derived retained material.
- Delegated visibility: registered name, path, content and optional description in V2; V1 configured skill directory and command template.
- Selection predicate: readable SKILL.md with leading frontmatter and name; slash commands exclude false `user-invocable` or `slash` fields.
- Invalidation or expiry: loader-time filesystem contents; hot reload and host caching uninspected.
- Activation or effect: registers resources and requests named skill execution; actual model compliance unobserved.
- Evidence limits: host internals and other adapter execution not frozen; registration is not execution.

> text: `Load and execute the \`${skill.name}\` skill.\n\n${prompt.text}`,
> --- `.opencode/plugins/compound-engineering.js`

#### RT-RTE-native-work
Label: Native plan implementation

Trigger/principal: user or orchestrator supplies a plan or concrete prompt. The foreground host agent owns engine/strategy selection, decisions, verification and canonical commits; fresh workers propose implementation within bounded packets. Plan U/R/KTD identities and base SHA anchor tasks and scope. The decision policy is natural-language workflow guidance; native tools execute actual edits, tests and Git actions. Open-request mode; no supplied answer oracle beyond task-specific expected behavior/tests chosen from the plan. Human veto remains at unresolved authority/input boundaries, not mandatory per-unit approval. Product admission is actual-diff review plus authoritative verification and host commit; failing tests block commits; collisions/settled-decision invalidation stop or requeue work. Guidance is the plan, current code/tests, project instructions and implementation rules; persisted output is code/tests, Git commits and verification reporting, not necessarily a revised methodology. SRC-1, `skills/ce-work/SKILL.md`, `skills/ce-work/references/execution-strategy.md`, `skills/ce-work/references/implementation-loop.md`, `skills/ce-work/references/return-to-caller.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: structured implementation/verification result in return-to-caller mode; standalone proceeds to its finishing workflow.
- Later read-back: canonical changes and plan remain inspectable by later invocations; receipt reuse is prescribed for same-plan recovery.
- Delegated visibility: bounded unit excerpts, relevant decisions, inherited rules and evidence strategy; fresh worker excludes prior implementation-unit transcript.
- Selection predicate: committed prerequisites and inspection-supported independence; inline for chained/trivial/no-worker paths, parallel batches around 3–5 for independent layers.
- Invalidation or expiry: stale base, collisions, unexpected scope or unworkable settled decision blocks integration or forces host resolution; retire worker handle after integration.
- Activation or effect: prescribed edits, tests, scope inspection and canonical commits; successful behavior is not observed here.
- Evidence limits: native isolation/scheduling/permissions are host-owned; summaries cannot prove a red-before-implementation test observation omitted by a worker.

> **No canonical commits.** Native workers implement and may run their *own unit's* focused tests in isolation as a self-check; the **orchestrator owns staging, the canonical commits, and the authoritative test runs**.
> --- `skills/ce-work/references/execution-strategy.md`

#### RT-RTE-external-unit
Label: External authoring and canonical admission

Trigger/principal: foreground agent resolves live/caller/config engine intent before sending content. It fixes recipient/model/intermediary, sanctions disclosed material and restrictions, and initializes private run state. Unit/attempt/job IDs, packet SHA and workspace bind dispatch. Python controller and shell adapter enforce symbolic checks; external model authors the unit; host decides semantic scope and supplies verification argv and commit message. Operating mode: bounded units within open requested work, not an improvement curriculum. Answer oracle: task-specific verification command; its correctness/coverage is not supplied by controller success. Worker proposes changes; host can reject unexpected scope; controller rejects identity/state/verification violations. No per-content human approval is required by this route. Recovery keeps failed work/receipts, restores tracked canonical state or retains lock when restoration cannot be proven; native fallback requires terminal evidence and explicit controller claim. Guidance includes bounded plan/brief, exclusions and evidence strategy. Product output persists as inspected transport and canonical commit; machinery/knowledge changes only if the authorized unit actually targets them. SRC-1, `skills/ce-work/references/cross-model-execution.md`, `skills/ce-work/scripts/unit_workspace_jobs.py`, `skills/ce-work/scripts/unit_workspace_transaction.py`, `skills/ce-work/scripts/cross-model-work.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: controller statuses/receipts; a terminal authoring result is not yet integrated, verified or committed.
- Later read-back: resume by supplied run ID, or exact plan identity discovery; stored receipts build completed returns without rerunning gates, as prescribed.
- Delegated visibility: controller-owned bounded packet and detached workspace; adapter-selected model/effort from authorization rather than ambient override.
- Selection predicate: ordered qualified route candidates before egress; exact authorized unit/attempt afterward. Post-init route remains locked unless fallback is authorized.
- Invalidation or expiry: moved base, altered authorization/packet, wrong argv, another bound job, unexpected scope, failing/mutating verification or unmatched state blocks progression.
- Activation or effect: executable authorization and integration checks; external edits and useful canonical outcomes unobserved.
- Evidence limits: no OS confinement; all permission requests approved. Scope acceptance is a host judgment. Resume/fallback/runner internals not fully audited; ignored state is outside exact tracked-state restoration.

> if meta.get("worker_argv") != expected_argv:
>     raise Operational(
>         "BLOCKED", "runner worker argv does not match the controller-issued fixed-route contract",
>         {"expected_argv": expected_argv, "actual_argv": meta.get("worker_argv")},
>     )
> --- `skills/ce-work/scripts/unit_workspace_jobs.py`

> if [ "$CONTROLLER_EXIT" -ne 0 ] || [ "$AUTH_STATUS" != "AUTHORIZED" ]; then
>   [ -n "$AUTH_RESPONSE" ] && printf '%s\n' "$AUTH_RESPONSE" >&2
>   log "controller dispatch authorization failed"
>   exit 2
> fi
> --- `skills/ce-work/scripts/cross-model-work.sh`

> verification_failed = verification_exit != 0 or after != before
> --- `skills/ce-work/scripts/unit_workspace_transaction.py`

> printf '%s\0' --approve-all
> --- `skills/ce-work/scripts/cross-model-work.sh`

#### RT-RTE-lfg-shipping
Label: Autonomous caller and shipping tail

Trigger/principal: explicit autonomous request or direct `lfg` invocation. Foreground agent classifies input and invokes available named child skills; it owns the sequential pipeline after each child return. Mode: open hands-off work. Planner/debugger proposes work source; foreground accepts only complete/evidenced returns, applies eligible review findings, records residuals and delegates shipping/CI. User grants ordinary end-to-end delivery, retains ungranted merge/irreversible-action veto and unresolved inputs. Oracle: requested outcome, child verification and CI result, not model consensus alone. Product admission runs implementation verification plus review/shipping gates; recovery stops rather than advances on malformed/blocked children and preserves already-pushed state. Plan and settled decisions guide proposals; product changes/learning/residual records persist via canonical commits, PR body/tickets/report. SRC-1, `skills/lfg/SKILL.md`, `skills/ce-work/references/return-to-caller.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: non-code child result, blocker, or DONE after code delivery; local-only terminal when no remote exists.
- Later read-back: commits, PR/residual records and qualifying learning may reach subsequent users/agents; successful reuse unobserved.
- Delegated visibility: work-source plan and structured implementation result, eligible review context and mode-specific shipping arguments.
- Selection predicate: plan, defect, unsettled judgment, ambiguous product shape or non-code request determines child; docs-only/tiny changes may skip simplify.
- Invalidation or expiry: work-source failure, incomplete child, invalidated decision or failed shipping process stops advancement.
- Activation or effect: requests implementation through PR/CI completion, without granting merge by default.
- Evidence limits: tail subskills' detailed references not audited; policies are not a host-enforced universal pipeline.

> Merging stays with the user unless they granted it for this run.
> --- `skills/lfg/SKILL.md`

#### RT-RTE-learning-admission
Label: Learning capture and maintenance admission

Trigger/principal: solved/verified work with non-recoverable durable reasoning, direct capture request or explicit store refresh. Foreground model judges eligibility, writes/adjudicates content and orchestrates read-only/scratch helpers. Capture accepts one learning, updates a high-overlap doc, or skips pack-covered content; Full mode grounds semantic claims, Lightweight omits that semantic validator. Refresh compares docs with current code, classifies and applies allowed actions, reports failed writes as recommended, and commits modified files. Operating mode: interactive or non-interactive open capture/maintenance requests. Answer reference: current tree, cited guidance, schema and mechanical flags; model grounding judgment is not a supplied expected-answer oracle. Human input is conditional: pack destination and discoverability instruction consent in interactive Full capture, ambiguous refresh judgments, and confirmed worth audit. Ordinary qualifying content and vocabulary edits are model-admitted, not all individually approved. Rejection is eligibility/overlap/grounding judgment; Git supplies version-history recovery for committed refresh changes, not an automatic rollback of every capture write. Guidance persists as solutions/pack rules and vocabulary; future planner delivery is prescribed. Detailed memory revisions remain for the memory analyst. SRC-1, `skills/ce-compound/SKILL.md`, `skills/ce-compound/references/assembly.md`, `skills/ce-compound-refresh/SKILL.md`, `skills/ce-compound-refresh/references/modes.md`, `skills/ce-plan/references/research.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Documentation complete/skipped, or refresh Applied/Recommended report and committed changes.
- Later read-back: planning researcher searches solutions plus declared packs, writes learnings dossier, and planner opens it when dispatched.
- Delegated visibility: resolved roots and task context to researchers; semantic validator receives written doc and changed glossary entries; helpers do not own product writes.
- Selection predicate: durable-reasoning counterfactual for capture; explicit narrowed store scope for refresh; matching title/applies_when or researcher relevance for planning delivery.
- Invalidation or expiry: overlap, contradictions/current-tree drift trigger update, replacement, deletion or stale-marking under mode rules; no automatic time-to-live established.
- Activation or effect: model-facing grounding/maintenance and planning use requirements; actual compliance or decision change unobserved.
- Evidence limits: no real sessions/stores/pack captures; capture's parser check is not semantic correctness, and delivery is not useful activation.

> **Apply edits silently in every mode. Do not prompt the user in interactive, lightweight, or non-interactive.** Vocabulary capture is a side effect of compounding, not a decision the user makes per run.
> --- `skills/ce-compound/references/assembly.md`

> A claim about current mechanics follows current code, but independently supported guidance does not become false merely because implementation stopped satisfying it: classify the doc from the guidance evidence and report the implementation conflict as a potential product regression.
> --- `skills/ce-compound-refresh/SKILL.md`

#### RT-RTE-resource-install
Label: Conversion and host-resource admission

Trigger/principal: human/automation invokes install CLI with plugin and target/options. Code resolves local/bundled source or shallow remote clone, parses, target-converts and writes selected host output; optional extra/all targets expand output. Symbolic options/handler rules drive progression. Capability change: installed resource files, not new model weights or an external worker. Caller chooses source/target, code rejects invalid permissions/target/scope or failed clone; no semantic content approval step in inspected installer. Mode: open installation request; answer oracle inapplicable — distribution rather than candidate-quality comparison. Guidance is manifests/converter rules and caller options. Temp clone is removed via cleanup; transactional rollback of already-written multiple target resources uninspected. SRC-1, `src/commands/install.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: installed-path console message or error; detected native-only tools may be skipped.
- Later read-back: inapplicable — installed static package resources are not use-derived retained learning.
- Delegated visibility: parsed plugin/options to target converters/writers, not to a model.
- Selection predicate: explicit plugin path/name and target; all selects detected implemented handlers; branch bypasses bundled resolution.
- Invalidation or expiry: explicit reinstallation/source changes; resource reload and replacement cleanup beyond inspected dispatch uninspected.
- Activation or effect: writes host resource output; later host loading follows its own contract.
- Evidence limits: per-target writer semantics and external host activation not fully inspected; requested remote branch is not immutable source pinning.

> await target.write(primaryOutputRoot, bundle, effectiveScope)
> --- `src/commands/install.ts`

#### RT-RTE-skill-authoring
Label: Repository-local behavior change and evaluation

Trigger/principal: contributor/agent changes or judges skill files, including responding to review. Author proposes text under `ce-skill-work` and the portable-authoring standard, checks provenance before removing mandates, and validates proportional to risk. Reviewer/eval results can reject or revise proposals; human merge/release veto configuration is uninspected. Mode: open improvement requests plus bounded scenario comparisons, not online production self-training. Expected-answer/rubric provider: scenario author uses pre-change contract and actual failure evidence; eval grading uses artifacts/ACTIONS and, for conversations, simulated users and blind grader. This is distinct from model judgment without a reference. Mechanical checks run CI; prose evaluation can legitimately be skipped for unavailable capabilities with exact reasons. Rollback is source-version reversion; deployed-version rollback machinery uninspected. What persists is changed skill/reference text, tests/scenarios and PR evaluation report. SRC-1, `.agents/skills/ce-skill-work/SKILL.md`, `.agents/skills/ce-skill-work/references/evaluate.md`, `package.json`, `.github/workflows/ci.yml`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: authored change/review report with validation evidence or exact skip reason; installation/publication is another route.
- Later read-back: future authors read changed method texts and recorded provenance/evaluation; end-user hosts may load published skills after distribution.
- Delegated visibility: fresh agent gets on-disk skill and necessary references/raw scenario artifacts, not author's diagnosis or intended fix.
- Selection predicate: changed behavior/risk selects eval scope and hosts; mechanical contracts go to tests; fresh reader pass for restructures.
- Invalidation or expiry: failed eval, conflicting standard, uncovered live path or changed consumer contract prompts revision; cache at session start necessitates fresh-context evaluation.
- Activation or effect: prescribed behavior-responsive editing and implemented eval entry commands; actual improved routing, release and later activation unobserved.
- Evidence limits: no evaluation runs supplied/inspected as observed traces; CI configuration is not a passed CI run or a proof of mandatory branch protection.

> Mechanical contracts (frontmatter, paths, greppable invariants, parity, script behavior) go in `bun test` and run in CI. Prose behavior — routing judgment, restraint, cross-model outcomes — is evaluated with a model and is best-effort evidence, not a CI job.
> --- `.agents/skills/ce-skill-work/references/evaluate.md`

> Baseline, then compare: run the scenario against the pre-change skill first when a behavior is being *changed* (so you can see the failure the change fixes), then against the edited skill.
> --- `.agents/skills/ce-skill-work/references/evaluate.md`

Theory account: the authoring standard formulates claims about instruction design (conditions rather than cases, owning-layer placement, proportional testing). Authors apply and criticize skill rules against provenance and evaluation; they can replace operative instructions and retain criticism in reports/scenarios. This account is scoped to repository-local methodology editing, not all coding work.

- theory-builder conditions 1–4:
  - Condition 1 conclusion status: afforded
    Whole localized skill/reference rules are inspectable and editable; the kernel exposes its standard.
  - Condition 2 conclusion status: claimed
    Authors are instructed to decide edits from that standard; actual content-dependent decisions unobserved.
  - Condition 3 conclusion status: claimed
    Content-directed defect findings and pre/post evaluation are requested; particular blame and revision in an executed episode unobserved.
  - Condition 4 conclusion status: claimed
    Retained PR findings/scenarios and method edits are intended to guide further changes; actual next-round dependence unobserved.
- Addressability: individual rule blocks and references can be inspected/revised; condition-to-case correspondence beyond inspected kernel uninspected.
- Persistence: files/Git span tasks and sessions; PR record and scenario consumer are specified by authoring/evaluation contract, not traced deployed reuse.
- learning: uninspected — no measured improved future capacity or attribution in this boundary.
- Reflection: afforded representation/editing path for the plugin's own skills and evaluation methods; both actual feedback updating method representation and changed representation affecting subsequent execution unobserved.
- Reflective theory builder conclusion status: claimed
  Evaluation of own method-guided operation is requested, but conditions 2–4 are not observed.
- Autonomous theory builder conclusion status: uninspected
  Agent authoring/grading is available, but every internal operation and human contribution across a complete iteration are not established.
- Self-improvement: dispositional pathway for changing plugin behavior under the independent objective of closing demonstrated behavioral gaps at the owning layer. Assessment horizon: future published/installed sessions. Evidence can guide proposed update and changed skill can enter the host-model instruction path; subsequent evidence-responsive update, installation and operation causally depending on that update are unobserved. No exercised or successful self-improvement attribution follows.

### Claims

#### RT-CLM-verified-change
Label: Verified implemented change

Claimed operation: `ce-work` delivers implementation and local verification while retaining host integration authority; external worker completion alone does not satisfy it. SRC-1, `skills/ce-work/SKILL.md`, `skills/ce-work/references/cross-model-execution.md`; qualified by [RT-RTE-native-work](#rt-rte-native-work) and [RT-RTE-external-unit](#rt-rte-external-unit).

> **Result:** A fully implemented, locally verified change set from a plan, specification, or concrete work prompt.
> --- `skills/ce-work/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-instructions
Label: Loaded skill behavioral guidance

Consumer: foreground host model and scoped native/external worker models. Channel: skill body/reference reads, bounded worker packets and caller results. Force: model-interpreted instructions/policies, not universal tool enforcement. Horizon: current invocation and future invocations loading static or newly published skills. SRC-1, `.opencode/plugins/compound-engineering.js`, `skills/ce-work/references/execution-strategy.md`; [RT-OBJ-skill-files](#rt-obj-skill-files), [RT-RTE-host-loading](#rt-rte-host-loading). Delivery is wired for inspected loader; reliable compliance unobserved.

#### RT-BAP-controller-state
Label: Controller transition authority

Consumer: authorization and integration programs. Channel: private manifest/authorization/runner metadata, exact digests/argv and Git snapshots. Force: fixed symbolic checks reject unsupported transitions on this route; does not govern arbitrary host shell actions. Horizon: external run attempts and recovery. SRC-1, `skills/ce-work/scripts/unit_workspace_jobs.py`, `skills/ce-work/scripts/unit_workspace_transaction.py`; [RT-OBJ-run-manifest](#rt-obj-run-manifest), [RT-RTE-external-unit](#rt-rte-external-unit). Executable route checks are wired; operational exercise uninspected.

## Annotations

none
