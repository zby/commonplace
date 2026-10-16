---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Sentry Skills runtime baseline: host-consumed instructions, PR repair helpers, approval-scoped triage and skill change admission."
run-id: AAS-2026-10-14-skills-2719567f917c-01
reviewed-boundary: d18b7aa8ba878354e5c348310230e652f7690f9c
---

# Sentry Skills runtime report

## Runtime account

Sentry Skills supplies workflows and helpers, not the enclosing model/tool execution loop. The [boundary](boundary.md) fixes a complete repository artifact with a partial operational loop. Installation, automatic relevance matching and tool execution depend on external hosts. The marketplace points to `./`; the README identifies canonical `skills/` and `agents/`, and offers skills.sh as another distribution path. Neither manifest implements scheduling or permission enforcement. SRC-1, `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `README.md`.

> Restart Claude Code after installation. Skills activate automatically when relevant.
> --- `README.md`

The ordinary traced invocation is a user asking to repair PR failures or feedback. The host selects the skill, delivers its natural-language instructions and executes requested commands. The foreground model owns the next repair decision, while helper code owns fetching, classification and polling. Target repository cwd, authenticated `gh`, `uv`, PR number/branch and current service results identify the work. The branch, local changes, GitHub checks and review threads supply state. The prescribed cycle is fetch, diagnose, edit, test, commit, push, poll and recheck feedback. Success means actionable CI and feedback are clean, not that the PR is mergeable. [RT-RTE-pr-iteration](#rt-rte-pr-iteration) retains the admission and stopping rules; [RT-RTE-check-monitor](#rt-rte-check-monitor) separates the deterministic monitor from that model-directed cycle.

Three forcing cases challenge a stronger runtime interpretation:

1. **Helper failure and direct CLI fallback.** The skill explicitly permits direct `gh` when scripts fail. Consequently helper classifications are not a mandatory control point. The fetcher can return an empty check list on errors, whereas the monitor distinguishes transient failures and retries. Neither output is proof of complete successful service observation. SRC-1, `skills/iterate-pr/SKILL.md`, `skills/iterate-pr/scripts/fetch_pr_checks.py`, `skills/iterate-pr/scripts/monitor_pr_checks.py`.
2. **Approval-sensitive remote mutation.** Triage requires explicit approval of a displayed batch before Sentry issue updates. This is a natural-language policy, not a shipped wrapper intercepting `update_issue`. Its declared tool list includes that mutation capability; actual grants and server authorization remain external. [RT-RTE-issue-triage](#rt-rte-issue-triage).
3. **Same objective through skill versus subagent.** Code simplification is supplied both as an ordinary skill and as a subagent prompt naming `opus`. Both demand behavior preservation; neither implements semantic equivalence enforcement. A separate agent may change context boundaries, but the package does not specify host frame contents or return transport. [RT-RTE-code-refinement](#rt-rte-code-refinement).

Capability surface, declared grant configuration and deployed isolation are distinct. `.claude/settings.json` allows registered skills, read-oriented shell commands, broad `Bash(gh api:*)`, selected fetch domains and all project MCP servers; its deny list is empty. That does not establish the permissions of a consuming repository, or permission-free mutation. PR instructions request commit/push commands not listed there. The config is a project-local declaration, not evidence that this installation grants those effects. Triage's allowed-tools metadata similarly names capabilities without establishing enforcement of argument-level scope. SRC-1, `.claude/settings.json`, `skills/iterate-pr/SKILL.md`, `skills/triage-frontend-issues/SKILL.md`.

The model is supplied by the host; a subagent alias is not an immutable model version. [RT-CMP-host-model](#rt-cmp-host-model) records parameter and endpoint limits. Scripts are symbolic Python programs and JSON consumers, not model calls. Natural-language workflow bodies and references reach effects through model interpretation; JSON/YAML manifests and settings reach effects through external fixed-rule consumers. [RT-OBJ-skill-md](#rt-obj-skill-md) and [RT-BAP-skill-consumption](#rt-bap-skill-consumption) retain this distinction.

Working-context controls are prescribed rather than implemented here. Skill-writer instructs loading only current-step references, selecting optional leaves by need, and keeping runtime routing separate from maintenance and eval material. This is model-decided on-demand context admission, not measured context eviction. Its fork reference describes isolated Claude contexts as an authoring option, not an activated fork in the inspected skill. Subagent prompts afford separated work but do not expose what the host pushes into a frame, what it removes afterwards or what crosses back. The frame analogy is useful for intended isolation only; no implementation establishes frame-pop behavior. SRC-1, `skills/skill-writer/SKILL.md`, `skills/skill-writer/references/claude-subagent-fork.md`, `agents/code-simplifier.md`.

> Follow the workflow steps in order. Load only the reference files required for the step you are on.
> --- `skills/skill-writer/SKILL.md`

Changes to the package itself pass through a prescribed authoring, registration and structural-validation workflow. Maintainer evaluation adds isolated generation scenarios, model-graded rubrics and a human adoption decision; structural validation is not a semantic gate. Warden registers a security-scanner trigger and severity configuration, but its execution/enforcement are external. [RT-RTE-skill-revision](#rt-rte-skill-revision), [RT-RTE-maintainer-eval](#rt-rte-maintainer-eval). Retained example and instruction revision details remain for the memory analyst.

**Guarantee scope.** PR root-cause repair and local verification are policies owned by the foreground agent; the enforcement point is the instruction consumer, strength **policy**, covered path the prescribed workflow, alternate path direct `gh` or ordinary shell work, external contract host compliance/tool permissions. Instruction conclusion status: claimed. Operation conclusion status: uninspected. Triage's approval/project/archive-only rules have the same strength and external dependency, covering only compliant execution of that skill. Code preservation is **best effort**, with no shipped semantic equivalence checker on either entry path. Structural validation has **invariant** strength only for its own returned validity relative to its coded checks; it does not prohibit a maintainer bypass or police deployment. The monitor's terminal classification is a code rule over received checks, not an invariant that CI passed, all feedback was received or the PR is mergeable. Supporting quotes and path-specific limits appear in the records below.

**Coverage and evidence limits.** Added full inspection covers PR check and feedback fetchers, the monitor, triage and its archive taxonomy, both code-simplifier entry forms, skill-writer and its iteration/registration/fork references, validator, EVAL and the small-inline AXIS scenario/config, manifests, settings, AGENTS and Warden config. These supply implementation and doctrine/design under SRC-1, not observed runs. A bounded entry-metadata search across all `skills/*/SKILL.md` and `agents/*.md` checked model/tool/fork/delegation alternatives; it does not establish all runtime behavior. Senpai's body, other skills' leaf workflows, reply-to-thread implementation, and other evaluation scenarios remain uninspected here. Service authorization, model compliance, actual host isolation, activation, operational success, performance and benefit remain unobserved. No target scripts, evaluators, tests or services were executed.

## Shared records

### Components

#### RT-CMP-host-model
Label: Host-selected model and opus subagent alias

Distributed-parametric component outside the checkout: the foreground host model interprets skills; the code-simplifier subagent requests `opus`. Numerical parameters reside in external provider/runtime storage, not the skill files. Foreground version and provider selection are uninspected; `opus` does not pin an exact revision and host alias resolution may select a different model. Parameter changes during operation are uninspected, not established as fixed or adaptive. No provider implementation is captured. SRC-1, `agents/code-simplifier.md`, `README.md`.

> model: opus
> --- `agents/code-simplifier.md`

### Operative objects

#### RT-OBJ-skill-md
Label: SKILL.md workflow instructions

Source-native skill bodies are natural-language Markdown on Git/filesystem storage. They supply triggers, instructions, reference-routing reasons and output contracts to external model consumers. Frontmatter is a separate symbolic metadata consumption path: name/description/tool and invocation fields are parsed by host-specific consumers. Their meaning and force are not established by storage alone. SRC-1, `skills/iterate-pr/SKILL.md`, `skills/skill-writer/SKILL.md`, `README.md`.

> `SKILL.md` is the primary router: every bundled reference file should be flat under `references/` and listed here with a direct "open when..." reason.
> --- `skills/skill-writer/SKILL.md`

### Routes

#### RT-RTE-pr-iteration
Label: PR repair and feedback iteration

User request or relevant task → host skill selection → helper/CLI results → foreground diagnosis and edits → local verification → Git commit/push → fresh CI/feedback → terminal report. The foreground model proposes and decides fixes; the user chooses low-priority feedback and is consulted after two repeated failures, unclear feedback or infrastructure issues. GitHub/CI accept or reject external effects independently. Invocation is an open request, with repeated improvement triggered by actionable failures or high/medium feedback. CI assertions/checkers provide reference outcomes for their tested behavior; reviewer comments are criticism, not a comprehensive answer oracle. Local tests and logs inform diagnosis; no supplied oracle establishes complete semantic correctness. SRC-1, `skills/iterate-pr/SKILL.md`.

- Immediate return: terminal success, stop or ask-user report from the host agent; helpers return JSON/markers.
- Later read-back: pushed code and subsequent GitHub results feed the next iteration; cross-invocation retained guidance is not established by this route.
- Delegated visibility: optional monitor receives PR identity and service checks, not the full code-repair context; no required model worker is declared.
- Selection predicate: failed checks and high/medium comments; low priority requires user choice, informational/resolved comments are skipped.
- Invalidation or expiry: restart monitor after each push; fetch feedback again ten seconds after actionable checks pass.
- Activation or effect: prescribed local edits and remote pushes; actual compliant edits and improvement unobserved.
- Evidence limits: natural-language repair policy plus implemented fetch/transform capacity; no execution trace or target-repository permission envelope.
- instruction conclusion status: claimed
- helper implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: trigger is failed CI or feedback; proposed change is target-repository code, not necessarily this package. Verification-before-push is prescribed; user can redirect or stop, but there is no per-fix human approval requirement. Repeated failure is a consultation rule. Commit history affords recovery, but automatic rollback is not specified. Guidance calls for diagnosis before editing, related-pattern search and focused tests. Code and commits persist; successful repair is not established.

> - local failure: fix before pushing
> --- `skills/iterate-pr/SKILL.md`

Forcing-path qualification: fallback uses direct CLI, bypassing helper transformation. The check fetcher returns `[]` on several failures and matches failed runs by workflow name from ten recent branch runs, not by an enforced current-head identity. Failure snippets retain at most a bounded neighborhood around the first regex match (or log tail); they are not the whole log. Feedback GraphQL fetches first 100 threads and first 10 comments per thread; processing uses the first comment, skips self-comments/very short bodies, buckets bot authors and supplies both a short summary and `full_body`. Thread completeness is not warranted. SRC-1, `skills/iterate-pr/scripts/fetch_pr_checks.py`, `skills/iterate-pr/scripts/fetch_pr_feedback.py`.

> If scripts fail, use `gh` CLI directly:
> --- `skills/iterate-pr/SKILL.md`

#### RT-RTE-check-monitor
Label: PR check monitor terminal classification

CLI invocation → initial PR identity lookup → repeated `gh pr checks` JSON reads → pending/failure/gate classification → marker and up to 20 tab-separated check rows. Python owns progression, sleeps and return codes; there is no model decision inside this loop. It captures PR draft/review metadata initially, not on every poll. Missing checks get a default 180-second grace period; failed fetches retry without a total retry limit. Missing executable/other uncaught exceptions need not enter that retry path. SRC-1, `skills/iterate-pr/scripts/monitor_pr_checks.py`.

- Immediate return: terminal marker and bounded summary, exit zero for terminal classifications including failures; initial unresolved PR exits one.
- Later read-back: inapplicable — the script does not write durable material for later invocation.
- Delegated visibility: optional host MonitorTool receives output; its isolation and notification behavior are external.
- Selection predicate: all non-human-gate pending checks delay completion; regex-matched human gates do not.
- Invalidation or expiry: no-check timer resets when checks appear; owning skill prescribes restart after push.
- Activation or effect: implemented polling and output, not code changes or verified PR success.
- Evidence limits: classification trusts gh bucket data and regexes; no executed service result or complete feedback view.
- implementation conclusion status: wired
- operation conclusion status: uninspected

A pending non-human check takes precedence over failed checks. With none pending, a fail yields failure marker; remaining human pending yields blocked marker; otherwise success marker. Cancel/skipping/unknown buckets are not independently rejected. Thus `ALL_CHECKS_PASSED` means no inspected `pending`/`fail` bucket, not necessarily every check's `pass` bucket. The monitor is not equivalent to the skill's post-CI feedback success condition.

> pending_checks = [check for check in checks if check.get("bucket") == "pending"]
> failed = sum(1 for check in checks if check.get("bucket") == "fail")
> --- `skills/iterate-pr/scripts/monitor_pr_checks.py`

#### RT-RTE-issue-triage
Label: Approval-scoped frontend issue archiving

User request → argument parsing/default queue → Sentry MCP search and detail reads → model classification using archive taxonomy → displayed plan → explicit user approval/subset → sequential `update_issue` → report. Foreground model proposes; human decides per displayed batch and can cancel or revise. Sentry service owns mutation execution. Open request mode; queue cleanup is the objective, with taxonomy rather than an expected correct-answer oracle. SRC-1, `skills/triage-frontend-issues/SKILL.md`, `skills/triage-frontend-issues/references/archive-criteria.md`.

- Immediate return: plan before approval, then archive/skip/human/failure report.
- Later read-back: service issue status can affect subsequent queue searches; no instruction update is established.
- Delegated visibility: issue detail fetches may run in parallel, but updates must be sequential; model-worker delegation uninspected.
- Selection predicate: unresolved sentry/javascript queue, ownership exclusions, documented noise categories and negative criteria; ambiguous cases skip or need human.
- Invalidation or expiry: approval covers displayed plan only; edits require rebuilding and reconfirming, new batches need approval.
- Activation or effect: prescribed status=ignored and ignoreMode=untilEscalating with category-tagged reason.
- Evidence limits: policy is model-consumed; MCP implementation and actual permission enforcement/mutations are not frozen.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Admission concerns remote queue status, not new package capabilities. Human veto precedes each plan's application; failures are recorded and remaining items continue. Recovery from a wrong archive belongs to the user; the skill forbids automatic reversal. Scope is an argument-level policy; allowed-tools does not itself enforce organization, project, status or approval.

> 6. **Never archive without confirmation.** Build a full plan, show it to the user, wait for explicit approval before calling `update_issue`. A single approval covers the displayed plan only; new batches need new approval.
> --- `skills/triage-frontend-issues/SKILL.md`

#### RT-RTE-code-refinement
Label: Skill and subagent code simplification

Relevant request/recent edits → ordinary skill or host-selected code-simplifier subagent → inspect modified code and project standards → model edits → verification/documentation. The model proposes and judges refinement; user may broaden scope. Subagent declares proactive autonomy, which is a requested operating policy rather than observed scheduling. No equivalence oracle or mandatory human admission gate is supplied. Operating mode is open refinement, triggered by modified code or explicit request. SRC-1, `skills/code-simplifier/SKILL.md`, `agents/code-simplifier.md`.

- Immediate return: requested refined code and significant-change explanation; exact host transport uninspected.
- Later read-back: changed source may be used later, but no package-defined retained instruction write is established here.
- Delegated visibility: subagent input context/return channel are host-owned and uninspected; ordinary skill shares its invocation's context.
- Selection predicate: recently touched code unless user explicitly broadens scope.
- Invalidation or expiry: inapplicable — no explicit lifecycle for refinement instructions beyond host invocation.
- Activation or effect: requested code edits preserving behavior; no observed edits or equivalence proof.
- Evidence limits: both entries are prompts, not enclosing execution or semantic enforcement code.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Admission is model-directed code editing subject to external host tool controls; rollback/rejection tooling is not specified. Guidance prioritizes explicit readability over brevity, avoids nested ternaries and applies project standards; edits persist in source only if the host executes them. [RT-CMP-host-model](#rt-cmp-host-model) describes the alias/version limit.

> Never change what the code does - only how it does it. All original features, outputs, and behaviors must remain intact.
> --- `skills/code-simplifier/SKILL.md`

#### RT-RTE-skill-revision
Label: Skill creation and evidence-directed revision

Maintainer request → mode/shape selection → optional synthesis or example iteration → authoring/precision passes → trigger optimization → registration → quick validation/manual judgment → summary and gaps. Foreground model drafts and evaluates; human scope clarification is required when location is ambiguous. Repository instructions mandate skill-writer and registration, but Git admission/review enforcement is external. Mode is open creation/update, with bounded working/holdout replay when iterating. Positive/negative/fix examples provide reference behavior where supplied; description query sets test trigger behavior, not a universal answer oracle. SRC-1, `AGENTS.md`, `skills/skill-writer/SKILL.md`, `skills/skill-writer/references/iteration-path.md`, `skills/skill-writer/references/registration-validation.md`.

- Immediate return: Summary, Changes Made, Validation Results and Open Gaps.
- Later read-back: updated SKILL.md/references are intended for later agent invocation; maintenance notes/examples may guide later revisions, with actual host loading unobserved.
- Delegated visibility: chosen execution shape may introduce workers/forks, but this router does not instantiate an enforced delegation protocol.
- Selection predicate: operation and observed conventions determine minimum path; references loaded by current-step need.
- Invalidation or expiry: pre-edit narrowing/replacement and post-change precision passes are prescribed; old installed copies require external update/reload.
- Activation or effect: authored instructions, helper code, registration and manifests can change future package behavior; activation unobserved.
- Evidence limits: structural validator is executable, qualitative review and behavior-directed iteration are instructions; no admitted revision/run result supplied.
- instruction conclusion status: claimed
- validator implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: proposed changes include behavior-determining skill bodies, references, scripts and registration. Quick validator checks existence, YAML mapping, required nonempty name/description, matching directory name and recognized local reference paths. Oversize content produces warning, not rejection. It does not validate semantic correctness, every possible link syntax, SPEC quality, triggers or security. Human/model judgment handles those; there is no automatic repository admission transaction or rollback. SRC-1, `skills/skill-writer/scripts/quick_validate.py`.

> The validator is a structural check. It should fail only for invalid skill format or missing referenced files. The size warning requires author judgment, not a machine gate.
> --- `skills/skill-writer/references/registration-validation.md`

Theory account: the method applies explicit routing, precision and evidence-iteration rules; it proposes changing guidance from replay results and retains artifacts, examples and deltas. Localized content is inspectable, but executed dependence, claim-specific blame and retained criticism affecting another round are not shown. These facts should not be collapsed into an absent learning mechanism.

- theory-builder conditions 1–4: condition 1 conclusion status: afforded — complete method-rule units are explicit; condition 2 conclusion status: claimed — instructed decisions depend on those rules; condition 3 conclusion status: uninspected — replay outcomes are requested but no formulated claim/blame/revision trace is supplied; condition 4 conclusion status: claimed — persistent examples and revision deltas are prescribed for future rounds, not observed.
- Addressability: sections and routed reference files are individually inspectable/editable; actual fine-grained criticism unobserved.
- Persistence: intended Git-backed instruction/example artifacts across sessions; deployment/read-back not observed.
- learning: uninspected — no improved future capacity or attribution evidence supplied.
- Reflection: afforded — skill-writer can revise its own method texts using outcome examples, with maintainer evaluation as a prescribed feedback path; both exercised causal directions unobserved.
- Reflective theory builder: uninspected — method criticism against its own operation is not evidenced as an exercised condition-1–4 chain.
- Autonomous theory builder: uninspected — workflow permits model work but does not establish computational performance of every internal operation or remove maintainer judgment.

Self-improvement assessment is dispositional, not exercised: boundary is this instruction package, horizon later installed invocations, objective high-value input coverage with reduced wasted runtime tokens. The route affords evidence-responsive modification of its own guidance. Evidence shaping an actual update, retained update entering live host authority, and later operation causally depending on it are not observed; successful improvement is separately unestablished.

> Primary success condition: maximize high-value input coverage before authoring while minimizing wasted runtime tokens.
> --- `skills/skill-writer/SKILL.md`

#### RT-RTE-maintainer-eval
Label: AXIS maintainer evaluation and adoption

Maintainer starts AXIS → scenario copies repository into temporary workspace → external Codex generates skill artifacts → external model judge checks transcript/workspace → comparison/manual review → adopt, revise or reject. Config sets one concurrent scenario, fifteen-minute scenario limit and Codex full-auto flags. EVAL declares isolated HOME/CODEX_HOME; actual isolation remains an external harness contract. The small-inline scenario supplies explicit task and weighted checks; those are reference criteria, not a known exact textual answer. Operating mode is bounded evaluation, separate from open authoring. SRC-1, `skills/skill-writer/EVAL.md`, `skills/skill-writer/evals/axis.config.json`, `skills/skill-writer/evals/scenarios/small-inline-workflow.json`.

- Immediate return: declared AXIS transcripts, artifacts, scores and maintainer eval summary; no result supplied.
- Later read-back: reviewed baseline/report may guide subsequent comparisons and adoption; actual saved results uninspected.
- Delegated visibility: Codex receives copied repository and scenario prompt; judge is declared to see transcript/workspace; host implementations uninspected.
- Selection predicate: maintainer selects scenario/set and compares baseline; adoption requires improvement without critical holdout regressions.
- Invalidation or expiry: baseline refreshed only after reviewing report; temp workspace lifecycle belongs to AXIS.
- Activation or effect: configured artifact production and prescribed adopt/revise/reject decision, not deployed package change by itself.
- Evidence limits: no frozen AXIS/Codex implementation, reports or causal experiments; other scenarios not fully inspected.
- configuration conclusion status: wired
- adoption policy conclusion status: claimed
- operation conclusion status: uninspected

Model proposes artifacts and external judge scores them; maintainer rubric/adoption gate decides and can veto. Rollback is not specified. Baseline comparison informs revision rather than automatically replacing installed guidance. Warden is another declared review route: pull_request opened/synchronize and local triggers scan `**/skills/**`, with failOn high/reportOn medium. This config alone cannot establish rejection coverage or security guarantees. SRC-1, `warden.toml`.

> Adopt a `skill-writer` change only when:
> --- `skills/skill-writer/EVAL.md`

### Claims

#### RT-CLM-preserve-functionality
Label: Functionality-preserving code simplification

Both simplifier entry forms claim improvement without behavior change. The requested preservation policy is evidenced in [RT-RTE-code-refinement](#rt-rte-code-refinement); no supplied trace or enforced equivalence checker substantiates preservation in operation. SRC-1, `skills/code-simplifier/SKILL.md`, `agents/code-simplifier.md`.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-consumption
Label: Installed skill instructions reaching host decisions

Consumer: external foreground model or named subagent. Channel: host-selected SKILL.md, optional routed references, repository guidance and subagent prompt. Force: natural-language instruction policy; metadata/config have distinct host-interpreted symbolic force. Horizon: current invocation for loaded content; later sessions only after retained package changes are installed/loaded. Automatic relevance activation and update commands are declared in README, not observed. Delivery alone does not establish compliance. SRC-1, `README.md`, `AGENTS.md`, `skills/skill-writer/SKILL.md`, `agents/code-simplifier.md`.

> **Update:**
> --- `README.md`

## Annotations

none
