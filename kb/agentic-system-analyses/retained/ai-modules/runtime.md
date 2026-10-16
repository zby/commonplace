---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ai-modules runtime baseline: model-interpreted task and wiki workflows, helper controls, charter interception, deployment and evaluator launch at the frozen commit."
run-id: AAS-2026-10-14-ai-modules-a7044d5627d2-01
reviewed-boundary: "0cf0227c416f75a79d7317f603a209a63e7a3c8f"
---

# ai-modules runtime report

## Runtime account

### Responsibility and evidence

ai-modules supplies procedures, role definitions and executable bookkeeping to an enclosing agent host. It does not own the host's model/tool loop. Its consequential claimed work is preparing and implementing durable task briefs, producing and consuming a Markdown wiki, and making these procedures reusable across hosts. The shipped entry paths are plugin registration, copied/transformed deployments, skill activation in the host, and standalone evaluator drivers. The model interprets a selected skill, decides which files and tools to use, and returns chat output plus filesystem changes. Bash/Python scripts execute narrower rules. A procedure saying an agent must stop is not equivalent to a tool runtime denying a write (SRC-1, `README.md`, `.claude-plugin/marketplace.json`, `deployment/deployment.sh`, `plugins/ai_dev/skills/task_implement/SKILL.md`). See [RT-CLM-persistent-context](#rt-clm-persistent-context), [RT-OBJ-skill-bodies](#rt-obj-skill-bodies) and [RT-CMP-host-model](#rt-cmp-host-model).

This account uses implementation and doctrine/design at the boundary's exact revision. No target, example, test or provider was executed. No retained result report or transcript was used as execution evidence. Consequently activation, reliability, cost savings and successful operation are unobserved here; missing traces do not establish absent behavior. Newly inspected SRC-1 coverage includes the complete task implement/check/auto-check and agent-spinner procedures; gate/verifier agents; import/wrapup procedures; wiki orientation, ingest, query and lint sections; wiki-shaper opening contract; charter hook and plugin hook configuration; deployment agent rewriting, Codex generation, install dispatch, backup, uninstall and main loop; evaluator worker command construction, worker launch and wiki layer-2 driver; and the wiki linter entry point. These are additional paths within the registered source, not new sources.

The remaining included families are not silently excluded: git workflows, formatting, instruction authoring, portability, editorial work and document distillation share the model-consumed skill delivery surface in `README.md`, but their detailed control paths were not comprehensively inspected. Task whole-tree shaping, the remaining wiki-shaper semantic checks, all deployment transforms and evaluator graders also remain partial inspection. This report therefore does not assert exhaustive workflow equivalence, universal host compatibility, complete evaluator correctness or absence of additional mechanisms. Memory revisions and the page-level authority of retained knowledge belong to specialist analysis; this report establishes their entry/admission and later-consumption interfaces.

### Ordinary invocation: implement one existing task

A user asks the foreground host agent to implement one named task. The host selects/loads `task_implement`; ai-modules supplies the procedure, not a router implementation. The principal is that user's work request. Task identity is the resolved task path; its lifecycle status and content identify the current work contract. Before edits, the agent reads the task, discovers live inbound and outbound prerequisites using the base task taxonomy, loads standing guardrails and examines existing code. Live hard prerequisites cause a stop for the user's explicit go-ahead; a cycle is surfaced. An already audited or archived task stops before editing rather than receiving an implementation stamp (SRC-1, `plugins/ai_dev/skills/task_implement/SKILL.md`; [RT-RTE-task-implement](#rt-rte-task-implement)).

The foreground model owns next-step selection. Its decision policy is natural-language guidance: follow the task Approach, treat the codebase as ground truth, reconcile open choices only when the ordered evidence settles them, otherwise ask. Context comprises the task, base task rules, governing standing instructions, nearby code/tests and any user answer. Current working state is the host conversation and tool results. Durable state is the task file and modified project tree. The host's tools execute writes and test commands; ai-modules supplies no new OS isolation boundary. On completing implementation, the model stamps `implemented`, author, update time and an explicit design-extension verdict, builds tests, checks each Acceptance item, reports actual verification results and updates docs/versions. It stops before audit and archive, pointing to user-run `task_audit` and `task_finish`. No automatic commit or deployment is established by this path (SRC-1, `plugins/ai_dev/skills/task_implement/SKILL.md`).

That path permits direct implementation requests rather than mechanically requiring a previously ready task. The manual create → check → implement → audit → finish spine is workflow advice, not a runtime-wide access-control chain. A failed verification calls for repair of introduced failures and explicit reporting of unrelated red checks; no transaction restores the original code tree. A scope conflict holds the workflow for a decision rather than silently widening work. Terminal output is an acceptance-by-acceptance report and changed task/project files, not an autonomous shipped release (SRC-1, `plugins/ai_dev/skills/task_implement/SKILL.md`, `plugins/ai_dev/skills/task_check/SKILL.md`).

### Material alternate and forcing routes

Four forcing cases constrain the strongest plausible guarantees:

1. **Unavailable helper surface.** Generic orchestration can degrade to separately prompted inline passes. The task readiness loop cannot: it stops before freeze when no spawn mechanism exists and asks the user to choose a manual route. A deployed agent file therefore neither proves callability nor licenses inline substitution. [RT-RTE-helper-dispatch](#rt-rte-helper-dispatch) and [RT-RTE-readiness-repair](#rt-rte-readiness-repair) retain the separate contracts (SRC-1, `plugins/ai_dev/skills/agent_spinner/SKILL.md`, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).
2. **Approval-sensitive wiki front ends versus direct hub/query.** Import waits for page selections after raw capture; wrapup waits before any wiki write. The hub can ingest directly, skip discussion in cron contexts, and file a synthesis before user validation. There is no system-wide per-page human approval invariant. Maintenance also grants deterministic autonomous fixes rather than seeking approval for every content change. [RT-RTE-wiki-triage](#rt-rte-wiki-triage) and [RT-RTE-wiki-consume](#rt-rte-wiki-consume) distinguish these routes (SRC-1, `plugins/knowledge_management/skills/wiki_import/SKILL.md`, `plugins/knowledge_management/skills/wiki_wrapup/SKILL.md`, `plugins/knowledge_management/skills/wiki/SKILL.md`, `plugins/knowledge_management/agents/auto_shaper_wiki.md`).
3. **Literal charter edit versus indirect shell mutation.** The charter hook intercepts supported direct edits, patch markers and known shell mutators. Variable-built paths or other interpreters can escape its static scan. A matching branch passes without checking a human approval artifact. The effective guarantee is conditional interception, not content-level authorization or tamper-proof charter immutability ([RT-RTE-charter-protect](#rt-rte-charter-protect); SRC-1, `plugins/ai_dev/hooks/charter_guardrail.sh`).
4. **Evaluator scratch separation versus confinement.** Drivers create distinct scenario directories and scratch deployments, but Claude launch requests permission bypass and Cursor launch explicitly disables its sandbox. Post-run read-path classification is not a preventive filesystem boundary. This defeats an inference from the word “sandbox” to deployed security isolation ([RT-RTE-evaluator-worker](#rt-rte-evaluator-worker); SRC-1, `tests/wiki/layer2/run.py`, `tests/lib/vendor.py`, `tests/lib/micro_deploy.py`).

Provider-native tools, arbitrary host callbacks, remote worker implementations and host context compaction are outside the inspected host boundary. Bundled scripts and evaluator subprocesses are included and traced. Their coverage cannot be extended to every tool the host might grant or every shell program an agent can invoke. No forcing case was executed.

### Controls and guarantees by owner

| Load-bearing guarantee | Owner and enforcement point | Strength and covered path | Alternate path / required external contract | Conclusion statuses |
| --- | --- | --- | --- | --- |
| Preserve frozen intent; apply no unverified body repair | Foreground model following auto-check freeze, verifier decision, anchored apply and delta audit | protocol; delegated readiness loop | Direct manual editing and implementation use different rules; mechanical lint repairs use a separate direct path. Host must actually isolate/spawn helpers and expose completed returns. | design conclusion status: claimed; operation conclusion status: uninspected |
| Read-only verifier | Role metadata and deployment generator; host tool/sandbox enforcement | deployment guarantee for emitted configuration, policy for role prose | Codex generator emits read-only sandbox from `readonly: true`; generic inline floor has no isolated tool set. Actual host enforcement is external. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Protect root charter outside named branch | Hook scanner and final Git branch test | best effort; recognized direct/patch/shell mutations reaching registered hook | Unrecognized interpreter/variable paths, undeployed hook, host channels not routed through it; host must honor denial semantics. Matching branch is not proof of review. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Lint before declaring wiki completion | Model invocation of linter; linter severity exit rule | protocol for calling/repair; invariant of inspected exit decision: blocking issue implies exit 1 | Direct file writes can omit lint. Exit 0 still permits warnings/info and does not certify semantic truth. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Distinct evaluator pass state | Layer-2 driver fresh-root setup and per-pass output paths | deployment guarantee of staged directory separation, not OS confinement | Worker receives bypass/disabled sandbox flags; provenance is retrospective and dependent on observable tools. | implementation conclusion status: wired; operation conclusion status: uninspected |

The capability surface is skill prose, scripts, generated roles and hook adapters. Current grant sets are installation filters, available host tools and per-role settings, not a central ai-modules permission ledger. Deployment can emit restrictions, but the live installation and host's enforcement envelope were not inspected. Roles with `model: inherit` use the host's model; evaluator aliases and CLI overrides likewise do not pin immutable model versions ([RT-CMP-host-model](#rt-cmp-host-model), [RT-RTE-deploy-artifacts](#rt-rte-deploy-artifacts); SRC-1, `deployment/deployment.sh`, `plugins/ai_dev/agents/auto_verifier_task.md`, `tests/lib/vendor.py`).

### State, coordination and changes to behavior

Auto-check uses an ignored relay directory keyed by task stem. It clears earlier contents, saves frozen intent/task and pointer-only prompts, retains completed helper returns verbatim, checks fresh target content before writes and audits applied deltas. This is a model-executed optimistic concurrency protocol, not a file lock or atomic compare-and-swap. The gate receives admitted paths but is told not to discover other relay returns or host state. A verifier receives gate/proposal files intentionally; those inputs differ from a blind gate. Generic agent-spinner isolates passes only at the spawned tier; the inline floor keeps them in one context. Broad wiki audits request a separate context so dozens of repair reads do not displace the foreground conversation. The host owns actual context assembly and disposal (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/agents/auto_gate_task.md`, `plugins/ai_dev/skills/agent_spinner/SKILL.md`, `plugins/knowledge_management/skills/wiki/SKILL.md`).

This resembles a per-call frame only when the host actually spawns: named file inputs enter; a contract-shaped return escapes. Persistent files can survive the frame and be reread by path. They are not references in the model window and their liveness is not tracked by ai-modules. Other working-context controls are bounded recent-log reads, index/topic selection and pointer-based large handoffs. No claim is made about host trimming, summarization or reload of compacted turns. Static skill/agent installation is behavioral guidance delivery, not read-back of accumulated experience ([RT-BAP-skill-guidance](#rt-bap-skill-guidance)).

Product changes are admitted by user-triggered implementation and model-directed verification. Task-body changes can be admitted by the bounded computational readiness loop under human stop boundaries. Wiki writes can be selection-approved, direct, synthesis-triggered or maintenance-driven. Changes to instruction/agent sources can be ordinary project work; deployment subsequently copies/transforms the changed files into later host inputs. Guardrail documents declare a human-owned review path; the executable charter hook only checks branch naming. Global deployment backs up active configurations, project-dir mode does not, and uninstall uses the deployment log to remove artifacts or restore prior JSON keys. None of these inspected paths automatically retrains model weights, proves learning benefit or establishes exercised self-improvement. Source-native method criticism and retained knowledge transformations require specialist grounding rather than inference from the repository's ability to edit itself (SRC-1, `plugins/ai_dev/skills/guardrail/SKILL.md`, `deployment/deployment.sh`, `README.md`).

## Shared records

### Components

#### RT-CMP-host-model
Label: Host-selected inference model

Source-native identity: helper `model: inherit`; evaluator Claude `sonnet` and Cursor `auto` defaults, with CLI overrides/inheritance. Representational form: distributed-parametric. Storage substrate: opaque external host/provider model service; no local parameter store inspected. Used by all model-interpreted routes below. Parameters changing during operation: uninspected — provider internals and adaptation are outside this source; no weight-update operation is established by inspected ai-modules routes. Exact version pinned: no immutable model version is specified by these aliases. Mutable endpoint resolving to another model: possible through inherited host choice, `auto` selection or caller override; actual resolution uninspected. This supports model-selection flexibility, not an observed version change (SRC-1, `plugins/ai_dev/agents/auto_gate_task.md`, `plugins/ai_dev/agents/auto_verifier_task.md`, `tests/lib/vendor.py`, `tests/wiki/layer2/run.py`).

> model: inherit
> background: false
> effort: max
> model_reasoning_effort: xhigh
> readonly: true
> tools: Read, Grep, Glob
> --- `plugins/ai_dev/agents/auto_verifier_task.md`

### Operative objects

#### RT-OBJ-skill-bodies
Label: Installed skill and agent procedure bodies

Source-native identity: `SKILL.md` procedure bodies and agent Markdown role bodies under the shipped plugins. Representational form: natural-language guidance, even when organized with pseudo-XML. Storage substrate: source Markdown, copied Markdown or generated TOML developer-instruction strings. The model interprets their content; structural tags do not turn behavioral instructions into a fixed executable state machine. Distinct from parsed manifests/settings in [RT-OBJ-host-config](#rt-obj-host-config). Evidence: SRC-1, `README.md`, `deployment/deployment.sh`, `plugins/ai_dev/skills/task_auto_check/SKILL.md`.

> Each skill is a written procedure the model loads when its trigger fires.
> --- `README.md`

#### RT-OBJ-host-config
Label: Plugin registrations and generated host settings

Source-native identity: marketplace/plugin registrations, hook JSON and generated role metadata. Representational form: symbolic as consumed by discovery/configuration rules. Storage substrate: JSON, Markdown frontmatter and generated TOML files in host configuration trees. Carries plugin roots, role names, tool/read-only settings and hook registration; body guidance remains [RT-OBJ-skill-bodies](#rt-obj-skill-bodies). Registration establishes an entry affordance, not successful host loading or model compliance (SRC-1, `.claude-plugin/marketplace.json`, `plugins/ai_dev/hooks/hooks.json`, `deployment/deployment.sh`).

#### RT-OBJ-relay-files
Label: Task auto-check relay artifacts

Source-native identity: `.task_auto_check/<task-file-stem>/` frozen snapshots, helper prompts/returns, lint output and diffs. Representational form: natural-language evidence and task content interpreted by helpers; exact-byte snapshots/anchors/diffs are used for comparison and application rules. Storage substrate: ignored `.txt` files on project filesystem. The different consumers are separated in [RT-RTE-readiness-repair](#rt-rte-readiness-repair): gate admitted paths, proposal/citation/delta verifier inputs and writer baseline. Persistence lasts beyond run end but the next run for the same stem clears it; this is not established cross-run learning (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/agents/auto_gate_task.md`).

> Keep the run's helper hand-offs under `<project-root>/.task_auto_check/<task-file-stem>/`. During `<freeze>`, create that relay directory, clear everything an earlier run left there for the same task-file stem, and create `.task_auto_check/.gitignore` containing `*`. Keep the relay directory in place after the run and name it in the report. Every relay artifact uses the `.txt` extension:
> --- `plugins/ai_dev/skills/task_auto_check/SKILL.md`

### Routes

#### RT-RTE-task-implement
Label: User-triggered task implementation

Endpoints/progression: user request → host-loaded `task_implement` → task/base-rule/dependency/guardrail/code reads → project and task writes → tests and acceptance report → user-owned audit/finish. Owner/next-step selector: foreground model; executor: host file/shell tools. Task path/status identify work; content constrains intended effects. Decision roles: human supplies work and can veto prerequisite override or unresolved scope choices; model reconciles evidence, authors code/tests and evaluates acceptance. Operating mode: open user-requested work, not a bounded benchmark. Answer oracle: task Acceptance contract and named test expectations provide reference outcomes; model judgment itself is not an oracle. Admission: implemented project changes and task stamp precede independent audit/close-out. Guidance: Approach, codebase and guardrails. Rejection/recovery: stop on protected status, hard prerequisite without go-ahead or unsettled scope; repair introduced failures and report unrelated ones; no automatic whole-tree rollback specified. Persisted result: task plus code/tests/docs, usable in later sessions (SRC-1, `plugins/ai_dev/skills/task_implement/SKILL.md`, `plugins/ai_dev/skills/task_check/SKILL.md`).

- Immediate return: Acceptance-item met/unmet report with verification evidence and next audit recommendation.
- Later read-back: Updated task is available to later audit/finish; modified project is later codebase ground truth.
- Delegated visibility: inapplicable — this procedure does not require helpers for its ordinary implementation flow.
- Selection predicate: User names one task; agent resolves it and checks status/dependencies.
- Invalidation or expiry: Completed statuses stop stamping; code/task conflicts require reconciliation rather than a fixed TTL.
- Activation or effect: Requests project edits and implementation metadata; successful exercise is unobserved.
- Evidence limits: Natural-language workflow, not an enforced host transaction; verification was not run in this analysis.
- design conclusion status: claimed
- operation conclusion status: uninspected

> Stopping here keeps each sibling single-purpose and keeps the close-out (a checkpoint the user owns) out of an automated build step. On success, report the work as done and recommend the next links in the chain (`task_audit` to verify, then `task_finish` to close); leave running them to the user.
> --- `plugins/ai_dev/skills/task_implement/SKILL.md`

#### RT-RTE-readiness-repair
Label: Delegated bounded task readiness repair

Endpoints/progression: opt-in request → orient/status gate → frozen snapshots → drift helper → readiness gate → stance proposals → proposal verifier → foreground anchored writes/lint → delta verifier → next gate/finalization. Owner: foreground model orchestrates; `task_check` through gate owns readiness status. Reviewer proposes; verifier can reject/narrow or route human decisions; foreground applies approved edits. Human owns deliberate intent changes, frozen-commitment deletion/narrowing, structural splits and dead-premise disposition. Operating mode: open task-specific repair under a default five-round cap, positive user override, and one last-call citation-refutation exception. Answer oracle: no independent known-good task text; frozen intent, base repair rules, code evidence and cited acceptance promises are reference constraints. A verifier verdict is a judgment, not a ground-truth answer.

Admission: only approved issue-resolving, intent-preserving body edits; mechanical lint finalization is a separate directly authorized edit class. Trigger: user asks to make a task ready, never to build its described work. Guidance: base task rules, task-check checklist, frozen title/Goal and optional creation intent. Persisted changes: task body/status, timestamps and relay evidence. Rejection/recovery: missing spawn surface stops before freeze; deliberate inability does not retry; most failed/invalid helper results retry once, the narrow spawn-echo glitch twice. Drift, invalidated premise, concurrent divergence and unresolved structural choices stop for a human. Delta failure restores pre-apply content and retries application/audit once; persistent failure restores then finalizes mechanical lint. Failed delta invocation restores then takes helper-failure stop without finalization. Fresh-read comparison is not atomic locking (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/agents/auto_gate_task.md`, `plugins/ai_dev/agents/auto_verifier_task.md`).

- Immediate return: Final status, stop reason, counts, approved/rejected/human-routed edits, audit/lint evidence and relay path.
- Later read-back: Repaired task reaches later implementation; relay reaches later steps of this run and remains inspectable, but is cleared on next same-stem run.
- Delegated visibility: Pointer-only admitted inputs differ by helper mode; gate excludes prior returns, other relay files and host/session state; proposal verifier intentionally sees gate/reviewers and frozen task.
- Selection predicate: One user-selected task at open/checked/ready; lazy stance selection from gate issues and recorded repeated-link findings.
- Invalidation or expiry: New same-stem run clears relay; fresh target divergence stops writes; frozen task/intent remain unchanged within run.
- Activation or effect: Requested verified task-body repair and gate-owned status changes; not implementation, archiving or demonstrated improved readiness.
- Evidence limits: Prompt-governed orchestration and self-reported isolation, with host-spawn implementation outside source; no exercised trace inspected.
- design conclusion status: claimed
- operation conclusion status: uninspected

> Two invariants hold on every failure path: no unverified proposal is ever applied, and no helper result is ever improvised. The loop never role-plays a missing gate, drift, reviewer, or verifier result in the main context and never computes a readiness verdict outside `task_check`.
> --- `plugins/ai_dev/skills/task_auto_check/SKILL.md`

The guarantee owner is the interpreting orchestrator; enforcement points are verifier-result consumption, pre-write read and delta audit, all requested as prose. Guarantee strength: protocol. Coverage excludes direct/manual task edits and separately authorized mechanical lint repairs; host completion and file-tool contracts are external dependencies.

Theory account: the route applies fixed methodology rather than revising its own method. A task's Goal/Approach may state a localized causal design, but no particular task theory was inspected here. It criticizes task/code/acceptance mismatches and retains edits plus criticism returns for a next gate; that does not automatically constitute content-directed criticism of a theory. theory-builder conditions 1–4: condition 1 conclusion status: uninspected — no selected task theory assessed; condition 2 conclusion status: uninspected — dependency on such theory content not established; condition 3 conclusion status: uninspected — general repair contract does not supply a concrete theory criticism/blame witness; condition 4 conclusion status: claimed — repair outcomes feed another gate, but theory-specific iteration is unestablished. Addressability: exact textual anchors and section-level task criticism are requested. Persistence: task across sessions, relay within-run/review horizon until replacement. learning: uninspected — no future-capacity improvement or attribution evidence. Reflection: uninspected — task descriptions represent work, not necessarily the system's own operation. Reflective theory builder and autonomous theory builder: uninspected — the required theory-specific conditions and computational ownership of each internal theory operation are not established. These limits do not negate the positive computational proposal/verification route.

#### RT-RTE-helper-dispatch
Label: Generic helper orchestration and degradation

Endpoints/progression: general request → host capability probe → declared shape/width/phase plan → passes → refute-by-default checking → one repair round/aggregation → verdict-first report. Owner: foreground orchestrator. Decision roles: model sizes/dispatches/aggregates; helpers propose/find/check; user chooses consequential narrowing and degraded recovery. Operating mode: open jobs with enumerated artifacts/lenses or bounded candidate comparisons; shape-dependent oracles are a closed checklist or criterion, not an independent universal answer key. State: stable item identifiers and external scratch roster. Effect boundary: one named path per write helper, one writer per tree and one delegation level, enforced only by prompt unless a host lever is established (SRC-1, `plugins/ai_dev/skills/agent_spinner/SKILL.md`).

- Immediate return: Tier, dispatched/returned counts, cited verdict and distinct findings beyond brief/user-review decisions.
- Later read-back: inapplicable — roster is current-run coordination; this generic skill owns no retained domain artifact.
- Delegated visibility: At spawned tier each pass has its own context; inline floor shares one context. Preamble/per-item/kind brief controls requested supply, with stated downstream payload cap and reread of load-bearing trimmed material.
- Selection predicate: Named skill family retains authority; otherwise job shape determines count from a written list, not an arbitrary round number.
- Invalidation or expiry: Per-helper wall-clock bound identifies unreturned items; next run sizes nested work rather than recursive delegation.
- Activation or effect: Requests bounded helper work and aggregation; actual concurrency, isolation and benefit not observed.
- Evidence limits: Capability probes are required host checks, not known live grants; no fresh context exists at inline floor.
- design conclusion status: claimed
- operation conclusion status: uninspected

> The inline floor is the floor for a run the orchestrator owns outright. Where a governing skill states its own stop-and-ask boundary for a host with no spawn surface, honour that boundary, offer that skill's manual routes, and perform no helper role inline, as `<invocation_boundary>` already establishes.
> --- `plugins/ai_dev/skills/agent_spinner/SKILL.md`

Guarantee strength: protocol; owner/enforcement: orchestrator interpreting containment and checking instructions. A host-enforced read-only tier requires actual host denial, not just a reviewer prompt. Failed invocation/contract or missing return earns one identical retry; persistent failure waits for user-selected degradation. One repair round leaves repaired work marked unverified rather than repeatedly checking until pass.

#### RT-RTE-wiki-triage
Label: Resource or session triage before wiki admission

Endpoints/progression: named resource or visible-session wrapup request → discover/orient → raw capture for import only → mine/classify/diff → proposal → user selections → hub writes/lint/log. Owner/selector: foreground model; human decides which page changes to admit. Operating mode: open single-source/session work. Answer oracle: captured resource or visible session and existing wiki are reference inputs, not an independently validated answer corpus. Proposed changes are NEW/EXTEND/CONFLICT candidates; contradiction options carry both excerpts. Admission: human selects page changes; import's raw capture precedes selection, while wrapup forbids every wiki write before selection. Human can reject all pages. Guidance: SCHEMA domain/types/taxonomy, index/recent log, captured material and hub write rules. Recovery: ambiguity stops discovery; re-ingest drift check precedes replacing old raw body; no general multi-file rollback specified (SRC-1, `plugins/knowledge_management/skills/wiki_import/SKILL.md`, `plugins/knowledge_management/skills/wiki_wrapup/SKILL.md`, `plugins/knowledge_management/skills/wiki/SKILL.md`).

- Immediate return: Three proposal sections with type/target/source anchors and contradiction options; after approval, changed-file report.
- Later read-back: Approved pages/raw/navigation/log are inputs to subsequent wiki sessions through the hub.
- Delegated visibility: inapplicable — these front ends do not require isolated helpers.
- Selection predicate: One confirmed resource or durable visible-session items, domain-limited and compared with existing pages.
- Invalidation or expiry: Source drift can replace raw body after comparison; superseded pages can archive; no TTL specified.
- Activation or effect: Requests retained knowledge writes after selection, except pre-selection raw capture; later behavioral effect unobserved.
- Evidence limits: Human approval is a procedure contract, not a filesystem gate, and does not cover direct hub/query/maintenance routes.
- design conclusion status: claimed
- operation conclusion status: uninspected

> <propose_then_act>Emit the proposal and wait for user selections before any wiki-page write. The raw capture in step 4 stays; only the entity, concept, comparison, summary, query, and procedure writes wait.</propose_then_act>
> --- `plugins/knowledge_management/skills/wiki_import/SKILL.md`

#### RT-RTE-wiki-consume
Label: Wiki retrieval, synthesis filing and maintenance

Endpoints/progression: domain question → schema/index/recent-log orientation → index selection plus topic search at 100+ pages → relevant pages → cited answer → optional trigger-governed retained synthesis/log. Direct ingest is another hub entry, not forced through triage. Broad repair requests instead dispatch wiki-shaper for orient/assess/remediate/verify; narrow lint stays inline. Owner/next-step selector: foreground model, or delegated wiki-shaper for maintenance. Decision roles: model proposes/admits first synthesis and deterministic maintenance; human corrects later and resolves genuine contested ambiguity. Operating mode: open query/ingest/maintenance. Answer oracle: retained pages/source text and schema/reference anatomy are inputs/constraints, not a known-correct semantic answer. Guidance: schema, hub conventions and shaper safe/deterministic contract. Admission trigger: three-page synthesis or novel cross-page reasoning; first filing carries medium confidence pending validation. Rejection/recovery: explain skipped trigger, later correction through ordinary update; maintenance surfaces contradictions rather than resolving them; linter reports structural errors, does not undo writes (SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, `plugins/knowledge_management/agents/auto_shaper_wiki.md`, `plugins/knowledge_management/skills/wiki/scripts/lint.py`).

- Immediate return: Cited answer and one-line filing decision, or maintenance changed-file/audit report.
- Later read-back: Filed synthesis and maintained wiki scaffold/pages reach later queries and orientation.
- Delegated visibility: Broad audit is requested in its own context; foreground retains report/files rather than entire repair loop. Host isolation itself is uninspected.
- Selection predicate: Index/topic relevance for query; three-plus pages or novel reasoning for filing; corpus-wide scope/drift for broad audit versus narrow per-operation lint.
- Invalidation or expiry: Ordinary updates, archive on full supersession and contested flags; pending synthesis has no automatic expiration.
- Activation or effect: Model-interpreted page content is delivered to answer generation and can become further retained content; exercised influence unobserved.
- Evidence limits: Query-trigger policy is natural language; structural linter exit does not certify truth or complete warning cleanup. Detailed semantic maintenance checks not all inspected.
- design conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

> This line
>    stands in place of asking permission before filing: decide on the
>    trigger, report the call, and let the user correct it in the next turn,
> --- `plugins/knowledge_management/skills/wiki/SKILL.md`

>     return 1 if any(i.severity == SEV_BLOCKING for i in issues) else 0
> --- `plugins/knowledge_management/skills/wiki/scripts/lint.py`

The wired status covers the inspected linter call/exit mechanism, not reliable semantic model compliance. This route is deliberately separate from triage approval; its memory transformations should receive their own specialist findings.

#### RT-RTE-charter-protect
Label: Best-effort charter mutation interception

Endpoints/progression: host PreToolUse event → shell script reads JSON → literal-name fast path → JSON/cwd/repo resolution → candidate direct/patch/shell paths → root-charter match → branch test → allow or deny. Owner/executor: hook shell/jq/Git rules; host owns invocation and denial enforcement. State/identity: canonical repo-root charter path and current symbolic branch. Decision policy: recognized mutation passes only on `guardrail/charter-*`; no content review or approval credential is checked. Claim of human-reviewed branch belongs to doctrine, not the mechanical condition. Operating mode: deterministic interception of supported events; answer oracle: path equality and branch pattern are reference predicates, not semantic approval.

Admission of charter changes: branch match permits tool execution; guardrail procedure separately says humans approve drafts. Human can reject via review; that veto is not implemented by this scanner. Recovery: no mutation rollback, hook attempts prevention. Invalid JSON/missing jq on literal charter input emits abort signals; unrelated input fast-exits. External contract: host registers relevant channels, supplies compatible schemas and honors exit/decision formats. Guarantee strength: best effort. Covered equivalent paths include `file_path`, apply_patch markers, redirection, known mutators and non-read Antigravity string arguments. Alternate channels, indirect shell variables and interpreters outside the mutator set are not covered (SRC-1, `plugins/ai_dev/hooks/charter_guardrail.sh`, `plugins/ai_dev/hooks/hooks.json`, `plugins/ai_dev/skills/guardrail/SKILL.md`).

- Immediate return: Allow exit or host-specific denial signal; no content result.
- Later read-back: inapplicable — interceptor retains no experience; permitted charter text has a separate later consumer path.
- Delegated visibility: inapplicable — event interception has no helper handoff.
- Selection predicate: Literal CHARTER.md presence, recognized candidate resolving to existing root charter, branch mismatch for denial.
- Invalidation or expiry: Current cwd/repo/branch evaluated per event; absence of charter or recognized target permits exit.
- Activation or effect: Wired denial on covered events outside branch pattern, contingent on host honoring it; no operational enforcement observed.
- Evidence limits: Static shell scan, not arbitrary-program analysis; branch naming alone supplies neither human approval nor content safety.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # The shell scan is a best-effort static reading of the command. A path built
> # from a shell variable, or an in-place edit by an interpreter outside the
> # known mutator set, is not caught here; that residual relies on the agents'
> # read-and-respect contract with the charter.
> --- `plugins/ai_dev/hooks/charter_guardrail.sh`

> case "$branch" in
>   guardrail/charter-*) exit 0 ;;
> esac
> --- `plugins/ai_dev/hooks/charter_guardrail.sh`

#### RT-RTE-deploy-artifacts
Label: Admit skills, roles and hooks into host installations

Endpoints/progression: operator shell/Make deployment request → option/config parsing and filters → global backup or project-mode skip → artifact discovery → per-host copy/transformation/replacement → deployment log/summary. Plugin marketplace registration is an alternate discovery path rather than this copy loop. Owner/executor: deployment Bash functions, no model needed. Decision roles: caller selects targets/types/names; configuration can disallow paths; code transforms selected files; no per-body semantic approval is implemented. Operating mode: caller-selected deployment, preview or uninstall. Answer oracle: artifact-name/type/target rules, not behavioral compatibility. Trigger/proposed change: install/update/remove host guidance, capabilities and hook wiring. Admission/rejection: filter/config and existence checks admit artifacts; unknown `--only` names abort before backup/copy. Guidance shaping content comes from already-authored files, not generated model proposals. Persisted output is host tree/config and deployment log. Recovery: global timestamped backup; project-dir backups disabled; logged uninstall removes paths or restores prior JSON keys, keeping failed entries; no all-target atomic rollback established (SRC-1, `deployment/deployment.sh`, `.claude-plugin/marketplace.json`).

- Immediate return: Copy/generation/skip summaries or preview/uninstall report.
- Later read-back: Host later discovers copied skill/role/settings; this is static deployment consumption, not accumulated-experience read-back.
- Delegated visibility: Agent body and supported metadata are transformed to host formats; Codex uses developer_instructions and read-only sandbox setting. Unsupported metadata cannot be assumed preserved across other transforms.
- Selection predicate: Activated targets, type/name filters and configuration disallow/replacement rules.
- Invalidation or expiry: Redeploy replaces selected destinations; logged uninstall/JSON prior restoration removes installation effects; no immutable installed revision enforcement shown.
- Activation or effect: Executable copying/config generation is wired; actual host loading/callability/behavior is not observed.
- Evidence limits: Inspected representative transforms and main/recovery paths, not every host bridge; configuration emitted is not proof of live host support.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>     if [[ "$readonly" == "true" ]]; then
>       printf 'sandbox_mode = "read-only"\n'
>     fi
>     printf 'developer_instructions = """\n%s\n"""\n' "$(escape_toml_basic_string "$body")"
> --- `deployment/deployment.sh`

>   info "skip" "Backups are disabled in project-dir mode"
> --- `deployment/deployment.sh`

#### RT-RTE-evaluator-worker
Label: Wiki scenario worker launch and retained evaluation artifacts

Endpoints/progression: layer-2 CLI → scenario selection → fresh outside-checkout root/fixture setup → prompt construction → micro-deployed artifact paths → worker subprocess → capture/provenance/snapshot → root removal → normalization/grading/aggregation. Owner/next-step selector: Python driver and scenario config; model chooses behavior inside each worker invocation. Role identities: scenario ID, pass number, run timestamp and returned session ID where parsed. Operating mode: bounded scenario/pass regression evaluation, not live user corpus maintenance. Decision roles: author/caller defines scenario and parameters, software schedules and captures, worker model acts; grader internals not inspected, so no complete answer-oracle characterization. Driver names `grade.py`/`aggregate.py` but names alone do not establish semantic validity. No automatic product-change admission follows benchmark output in this inspected driver.

Coordination: ThreadPoolExecutor across scenarios, sequential independent passes per scenario. Executor/effect boundary: vendor CLI subprocess with scratch deployment environment and scenario cwd; capability grant requests Claude bypassPermissions or Cursor force/sandbox-disabled. Timeout returns rc -1 and retained partial output; scenario exceptions are printed while other futures continue. Provenance parses stream/helper transcript tools and classifies read paths after execution. Snapshot precedes cleanup. The actual OS access boundary is external; directory separation is not a security sandbox (SRC-1, `tests/wiki/layer2/run.py`, `tests/lib/vendor.py`, `tests/lib/micro_deploy.py`).

- Immediate return: Worker final message/rc/stderr/tools, then benchmark/report paths and aggregation rc.
- Later read-back: Driver can supply a previous benchmark to aggregation; responses/timing/provenance/snapshots remain for later evaluation, not automatically fed to the worker as learning.
- Delegated visibility: Worker receives rewritten deployed paths and scenario prompt; helper calls are included in intended provenance capture. Actual host helper input assembly is uninspected.
- Selection predicate: Scenario IDs, pass count, vendor/model/bin overrides and bounded worker count; unknown scenarios abort.
- Invalidation or expiry: Each pass restages independent state; temporary roots removed in finally; retained pass artifacts remain under run directory.
- Activation or effect: Wired model-worker launch and artifact capture; model behavior, sandbox compliance and benchmark outcomes unobserved here.
- Evidence limits: No run performed or result trace inspected; provenance depends on observable tool records/path parsing, not preventive mediation of all I/O.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>             cmd = [bin, "-p", "--permission-mode", "bypassPermissions"]
> --- `tests/lib/vendor.py`

>     cmd = [bin, "-p", "--force", "--sandbox", "disabled"]
> --- `tests/lib/vendor.py`

### Claims

#### RT-CLM-persistent-context
Label: Explicit retained intent and knowledge reduce reconstruction gaps

Claimed operation: source-native task/wiki files preserve what a project intends and knows for later agent sessions; bundled scripts reduce repeated improvised bookkeeping. This is declared intent supported by inspected admission/consumption paths, not evidence of improved accuracy, cost or convergence across sessions. Source: SRC-1, `README.md`; routes [RT-RTE-task-implement](#rt-rte-task-implement), [RT-RTE-wiki-consume](#rt-rte-wiki-consume).

> Both are plain CommonMark Markdown files on disk. You can grep them, diff them, version them in git, and open them in any editor, with no database, no SaaS, or proprietary reader in the loop.
> --- `README.md`

#### RT-CLM-callability-distinction
Label: A deployed role is not necessarily callable

Claimed operation: orchestration must establish host callability and capability tier rather than infer it from role presence. This qualifies deployment success and all helper routes; source is a doctrine/design warning, not a record of a particular failed installed host (SRC-1, `plugins/ai_dev/skills/agent_spinner/SKILL.md`).

> A role definition on disk is evidence that the file deployed, not evidence that it can be called: definition-present-and-uncallable is a real state, so a registration check reporting a definition as available settles deployment alone.
> --- `plugins/ai_dev/skills/agent_spinner/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Installed procedure to host-model decisions

Consumer: foreground/helper host-selected model. Channel: loaded skill/agent body, including generated Codex developer_instructions; symbolic settings separately configure host tools. Force: natural-language behavioral guidance, with host-specific instruction authority not independently established here. Horizon: installed artifact reused across invocations until redeploy/edit/uninstall. Source-native body content can determine requested next actions, but delivery does not prove compliance. Evidence: SRC-1, `README.md`, `deployment/deployment.sh`; [RT-OBJ-skill-bodies](#rt-obj-skill-bodies), [RT-RTE-deploy-artifacts](#rt-rte-deploy-artifacts).

#### RT-BAP-task-guidance
Label: Durable task brief to later implementation

Consumer: implementation model, later gate/audit readers. Channel: named task file and referenced standing rules loaded by host tools. Force: user-selected work contract interpreted by model; codebase evidence can require mechanical deviations, unresolved scope choices return to user. Horizon: across sessions/task lifecycle until completed or deliberately changed. Evidence: SRC-1, `plugins/ai_dev/skills/task_implement/SKILL.md`, `plugins/ai_dev/skills/task_check/SKILL.md`; [RT-RTE-task-implement](#rt-rte-task-implement), [RT-RTE-readiness-repair](#rt-rte-readiness-repair).

#### RT-BAP-wiki-guidance
Label: Retained wiki text to answer and write decisions

Consumer: foreground query/ingest model and maintenance helper. Channel: schema/index/recent-log orientation and selected pages read by tools. Force: schema as requested writing constraint; page content as evidence for synthesized answers rather than executable command authority. Horizon: later invocations across sessions; archival/update changes future selection. Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, `plugins/knowledge_management/agents/auto_shaper_wiki.md`; [RT-RTE-wiki-consume](#rt-rte-wiki-consume). Whether a particular delivered page altered an actual decision is unobserved, not inferred from the presence of citations.

## Annotations

none
