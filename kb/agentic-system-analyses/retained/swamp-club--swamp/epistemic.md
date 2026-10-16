---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Swamp epistemic routes: typed execution, plan criticism, review verdicts, skill evaluations and verification attestations."
run-id: AAS-2026-10-15-swamp-440d19cc0bcc-01
reviewed-boundary: "380e3c307164501c7d705f7707a864f4612b2785"
---

# Swamp epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on Swamp's agent-created automation and retained operational material. It uses the frozen repository and exclusions in [boundary](boundary.md#boundary-and-evidence), and cites its [Source register](boundary.md#source-register), SRC-1. The functional boundary includes the repository-local improvement plane, not external harness/provider or Swamp Club server internals. The public accuracy claim is [RT-CLM-agent-workflows](runtime.md#rt-clm-agent-workflows). It is not treated as a promise that every stored value is accepted knowledge.

All new source reads below are implementation evidence except explicitly labelled instruction/design passages. Supplied runtime findings are provisional evidence, not a complete operation inventory. No target execution, evaluator result, lifecycle episode or causal comparison was supplied or performed. Consequently implemented checks can be assessed, but their activation, diagnostic accuracy, realized improvement and downstream compliance cannot. Provider parameters and exact model fixity remain as in [RT-CMP-agent-models](runtime.md#rt-cmp-agent-models).

| Entry point or operation | SRC-1 source path | Coverage and records, or limit |
| --- | --- | --- |
| CLI command registration and installed hooks | `src/cli/mod.ts`; `.claude/settings.json` | Direct registration read; settings contains an enabled plugin, no hook configuration in that file. Plugin internals uninspected. This is not a system-wide absence of hooks or tools. |
| Launch, behavior run, workflow run, worker, approval, extension resolution | `src/libswamp/start/start.ts`; `src/domain/models/method_execution_service.ts`; `src/domain/workflows/execution_service.ts`; `src/worker/exec_dispatch.ts` | Supplied [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch), [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run), [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run), [RT-RTE-worker-dispatch](runtime.md#rt-rte-worker-dispatch), [RT-RTE-gate-resume](runtime.md#rt-rte-gate-resume), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load). Direct added reads of preflight and workflow behavior-validation seams; [EPI-RTE-preflight-check](#epi-rte-preflight-check). |
| Behavior/workflow validate and evaluate | `src/cli/commands/behavior.ts`; `src/cli/commands/workflow.ts`; `src/domain/workflows/validation_service.ts` | Direct dispatch searches and validation inventory; runtime supplies execution checks. Standalone command bodies and every evaluator branch remain uninspected; prevents complete classification of all evaluation products. |
| Issue plan review, iteration, recorded adversarial findings and clearance | `extensions/models/issue_lifecycle.ts`; `.claude/skills/issue-lifecycle/SKILL.md`; `.claude/skills/issue-lifecycle/references/adversarial-review.md` | Direct selected methods/checks and complete adversarial procedure; [EPI-RTE-issue-feedback](#epi-rte-issue-feedback), [EPI-RTE-review-record](#epi-rte-review-record), [EPI-RTE-issue-clearance](#epi-rte-issue-clearance), supplied [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission). Code-conformance and other lifecycle checks inventoried, not traced end to end; prevents whole-lifecycle completeness. |
| Agent review and verdict | `verification/workflow-verify-reviews.yaml`; `scripts/check_review_verdict.ts` | Supplied [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict); direct complete parser read and input deduction below. Individual review prompts not independently assessed. |
| Skill review, trigger/routing/sufficiency tests | `verification/workflow-verify-skills.yaml`; `scripts/review_skills.ts`; `scripts/eval_skill_triggers_promptfoo.ts`; `evals/promptfoo/generate_config.ts`; `evals/promptfoo/generate_routing_config.ts`; `evals/promptfoo/generate_sufficiency_config.ts` | Direct workflow and selected driver/generator reads; [EPI-RTE-skill-evals](#epi-rte-skill-evals). External Tessl/promptfoo/provider implementations and fixture-label validity unassessed. |
| Stored reports and verification summary | `src/cli/commands/report.ts`; `src/domain/reports/report_execution_service.ts`; `src/domain/reports/builtin/verification_summary_report.ts`; `src/libswamp/models/run.ts` | Direct summary, selection, persistence/error paths and caller search; [EPI-RTE-report-summary](#epi-rte-report-summary). Other registered/custom reports are opaque alternatives, preventing exhaustive semantic classification. |
| Attestation generation and CI validation | `scripts/build_attestation.ts`; `.github/workflows/ci.yml` | Direct projection and CI result/check paths; [EPI-RTE-attestation-build](#epi-rte-attestation-build), [EPI-RTE-attestation-ci](#epi-rte-attestation-ci). Generator input acquisition and remote posting/fetch authenticity not fully audited. |
| Activity summarise | `src/libswamp/summary/summarise.ts`; `src/domain/summary/summary_service.ts` | Direct libswamp entry and method-aggregation code; [EPI-RTE-activity-summary](#epi-rte-activity-summary). Workflow/data aggregation branches not fully read. |
| Additional registered operations, custom methods, report extensions and assertions | `src/cli/mod.ts`; `src/domain/models/method_execution_service.ts`; `src/domain/reports/report_execution_service.ts` | Open extension surface and remaining serve, audit, quest, datastore, expression/assertion, withdrawal and repair details not exhaustively inspected. They prevent a system-complete negative about semantic checking, claim production or adaptation. No inaccessibility is asserted for available code. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-task-brief](runtime.md#rt-obj-task-brief) | Not determinable as a class: goals can be non-truth-apt; task-specific assertions may be truth-apt | see record | see record | No populated task or agent trace supplied |
| [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run) | Recorded execution outcomes and provenance; instructions/plan fields are separately operational | see record | see record | Status is not proof of real-world task correctness |
| [EPI-OBJ-plan](#epi-obj-plan) | Summary, analysis, risks and testing claims mixed with intended actions and feedback | see record | see record | Actual entailment, criticism quality and truth depend on submitted content |
| [EPI-OBJ-adversarial-review](#epi-obj-adversarial-review) | Findings about a plan and their resolution flags | see record | see record | Code records caller judgments, not independent verification of them |
| [EPI-OBJ-verification-summary](#epi-obj-verification-summary) | Statements about recorded step outcomes and skips | see record | see record | Markdown says attestation; product is one-run summary, not authenticated evidence |
| [EPI-OBJ-attestation](#epi-obj-attestation) | Verification gate, run-derived steps, declared subject and config hashes | see record | see record | Run-record and acquisition contracts bound source warrant |
| [EPI-OBJ-skill-evals](#epi-obj-skill-evals) | Expected tool labels, generated assertions, scores and failure accounts | see record | see record | Labels measure routing behavior, not the truth of generated answers |

## Authority-route ledger

Repeated source-owned fields use `see` to avoid copying the shared records. Every implemented row describes capacity, not an observed episode. Multiple rows can use one route record when that implementation has distinct functions. Acceptance below means an evidence-consuming decision for a named use, not infallibility or all-purpose endorsement.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch) | operational admission/selection/consumption | implemented | see record | no content change | see record | see record | see record | see record | see record | Brief delivery licenses no task assertion | see record | see record | see record | none | none | External inference opaque |
| [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Argument/schema domain only | see record | see record | see record | [RT-CLM-agent-workflows](runtime.md#rt-clm-agent-workflows) | Shape is not action accuracy | Arbitrary method semantics opaque |
| [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run) | operational admission/selection/consumption | implemented | see record | no content change | see record | see record | see record | see record | see record | Outcomes support run-status claims, not causal mechanism | see record | see record | see record | [RT-CLM-agent-workflows](runtime.md#rt-clm-agent-workflows) | none | Cached/remote paths differ |
| [RT-RTE-gate-resume](runtime.md#rt-rte-gate-resume) | disposition/acceptance | implemented | see record | non-truth-apt policy/content update: caller authorizes continuation | see record | see record | see record | see record | see record | No semantic acceptance implied by permission | see record | see record | see record | none | none | Caller is not necessarily human |
| [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | operational admission/selection/consumption | implemented | see record | non-truth-apt policy/content update: capability registration | see record | see record | see record | see record | see record | Export compatibility, not safety | see record | see record | see record | none | none | Import precedes validation |
| [EPI-RTE-preflight-check](#epi-rte-preflight-check) | check/evidence production | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Callback-specific domain; generic interface adds no truth guarantee | see record | see record | see record | none | none | Custom predicate semantics uninspected |
| [EPI-RTE-preflight-check](#epi-rte-preflight-check) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Selected checks permit invocation only | see record | see record | see record | none | none | Local mutating subset, skip controls |
| [EPI-RTE-issue-feedback](#epi-rte-issue-feedback) | content transformation | implemented | [EPI-OBJ-plan](#epi-obj-plan) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Caller warrant unknown; feedback text preserved | see record | see record | see record | none | none | Revision reasoning occurs outside method |
| [EPI-RTE-issue-feedback](#epi-rte-issue-feedback) | retention | implemented | [EPI-OBJ-plan](#epi-obj-plan) | no content change | see record | see record | see record | see record | see record | Stored revision is not accepted truth | see record | see record | see record | none | none | No semantic incorporation test |
| [EPI-RTE-review-record](#epi-rte-review-record) | retention | implemented | [EPI-OBJ-adversarial-review](#epi-obj-adversarial-review) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Caller criticism warrant unknown | see record | see record | see record | none | none | Stored flags are not rechecked code facts |
| [EPI-RTE-issue-clearance](#epi-rte-issue-clearance) | check/evidence production | implemented | [EPI-OBJ-adversarial-review](#epi-obj-adversarial-review) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Existence, version equality and unresolved severity within retained records | see record | see record | see record | none | Runtime omitted computational clearance | Does not verify findings' truth |
| [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission) | disposition/acceptance | implemented | [EPI-OBJ-plan](#epi-obj-plan) | non-truth-apt policy/content update: approved phase | see record; added clearance above | see record | see record | see record | see record | Operational plan admission; human evidence-consuming acceptance is doctrine only | see record | see record | see record | none | Supplement with clearance | Empty method arguments do not prove consent |
| [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict) | check/evidence production | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Model review requested; no answer oracle or observed semantic result | see record | see record | see record | [RT-CLM-agent-workflows](runtime.md#rt-clm-agent-workflows) | none | Concrete review content unavailable |
| [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Explicit marker permits verification step, not claim-wide truth | see record | see record | see record | none | Parser accepts marker beyond first response line | See deterministic counterexample in conclusion |
| [EPI-RTE-skill-evals](#epi-rte-skill-evals), Tessl intake | check/evidence production | implemented | [EPI-OBJ-skill-evals](#epi-obj-skill-evals) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | External quality judgment has unknown source warrant | see record | see record | see record | none | Numeric score is not demonstrated quality | External evaluator opaque |
| [EPI-RTE-skill-evals](#epi-rte-skill-evals), fixture assertions | check/evidence production | implemented | [EPI-OBJ-skill-evals](#epi-obj-skill-evals) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Assertion arithmetic relative to labels and returned outputs | see record | see record | see record | none | Sufficiency tool choice is not answer accuracy | Label validity unassessed |
| [EPI-RTE-skill-evals](#epi-rte-skill-evals), Tessl threshold | disposition/acceptance | implemented | [EPI-OBJ-skill-evals](#epi-obj-skill-evals) | no content change | see record | see record | see record | see record | see record | Score and validation threshold for skill-review step only | see record | see record | see record | none | External score validity unassessed | No benefit measured |
| [EPI-RTE-skill-evals](#epi-rte-skill-evals), fixture threshold | disposition/acceptance | implemented | [EPI-OBJ-skill-evals](#epi-obj-skill-evals) | no content change | see record | see record | see record | see record | see record | Combined-rate criterion for trigger-eval step only | see record | see record | see record | none | Combined rate can mask a weaker phase | No generalization measured |
| [EPI-RTE-report-summary](#epi-rte-report-summary) | content transformation | implemented | [EPI-OBJ-verification-summary](#epi-obj-verification-summary) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Preserves selected run facts; not new action warrant | see record | see record | see record | none | Markdown title exceeds JSON's summary scope | No cryptographic authentication |
| [EPI-RTE-report-summary](#epi-rte-report-summary) | retention | implemented | [EPI-OBJ-verification-summary](#epi-obj-verification-summary) | no content change | see record | see record | see record | see record | see record | Latest artifact need not describe latest attempted report | see record | see record | see record | none | Empty result leaves prior version latest | Report errors can yield fallback artifacts |
| [EPI-RTE-attestation-build](#epi-rte-attestation-build) | content transformation | implemented | [EPI-OBJ-attestation](#epi-obj-attestation) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Gate follows supplied run records within projection domain | see record | see record | see record | none | Generated-by label is not authenticity | Subject and acquisition warrant external to pure function |
| [EPI-RTE-attestation-ci](#epi-rte-attestation-ci) | check/evidence production | implemented | [EPI-OBJ-attestation](#epi-obj-attestation) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | Checked commit, gate and supplied-hash consistency only | see record | see record | see record | none | Missing hashes and stale time warn | Authentication not independently audited |
| [EPI-RTE-attestation-ci](#epi-rte-attestation-ci) | disposition/acceptance | implemented | [EPI-OBJ-attestation](#epi-obj-attestation) | no content change | see record | see record | see record | see record | see record | CI attestation admission under named error criteria | see record | see record | see record | none | Warning does not veto | No merge-policy completeness claim |
| [EPI-RTE-activity-summary](#epi-rte-activity-summary) | content transformation | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Selected method status facts and counts | see record | see record | see record | none | Current names can label older records | Other summary branches unassessed |
| [EPI-RTE-issue-feedback](#epi-rte-issue-feedback) | lifecycle integration | doctrine only | [EPI-OBJ-plan](#epi-obj-plan) | no content change | see record | see record | see record | see record | see record | No implemented evidence-consuming semantic acceptance established | see record | see record | see record | none | Feedback association is not acceptance | Instructions connect criticism to next revision; compliant episode unobserved |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-agent-workflows](runtime.md#rt-clm-agent-workflows) | see record | see record | see record | [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run), [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run), [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict), [EPI-RTE-preflight-check](#epi-rte-preflight-check), [EPI-RTE-skill-evals](#epi-rte-skill-evals), [EPI-RTE-attestation-ci](#epi-rte-attestation-ci) | None supplied | No comparison; external inference and arbitrary behavior effects remain outside check licenses | Reviewable automation has concrete mechanisms. Accuracy is locally checked only against schemas, authored predicates, review judgments and verification criteria | No basis for universal semantic accuracy or measured improvement |

## Bounded conclusion

- **Typed operational permission is real but narrow.** [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run), [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load), and [EPI-RTE-preflight-check](#epi-rte-preflight-check) admit executions/capabilities under structural and configured predicates. They do not license every resulting real-world proposition. Remote preflight skipping, caller skip controls and executable imports are source-supported countercases to a universal evaluator or sandbox.
- **Plan criticism has an operative consumer, not just a log.** [EPI-RTE-review-record](#epi-rte-review-record) retains versioned findings; [EPI-RTE-issue-clearance](#epi-rte-issue-clearance) consumes them before local approval. The check permits approval only when a current review exists and no critical/high unresolved finding remains, within the selected-check path. It does not establish that the human consented or that the plan solves the issue. This supplements the provisional runtime account without withdrawing its consent limitation. [EPI-RTE-issue-feedback](#epi-rte-issue-feedback) associates previous feedback with caller-supplied revised plans; the method does not semantically demonstrate incorporation. Instructional criticism and iteration capacity therefore coexist with unobserved compliance and unestablished learning benefit.
- **Model-generated review and plan content is not automatically accepted ampliative knowledge.** For the abstract review route, truth-apt transformation is indeterminate: no concrete content establishes preservation, entailment or non-entailment. The plan/feedback methods import caller content with unknown warrant. Novel suggestions may occur in external agents, but neither an observed conjecture nor evidence-consuming acceptance of one is supplied. Retention, approved phase and later execution do not fill that gap. Formulated explanations, content-directed blame and all theory-builder conditions cannot be inferred from the plan label; particular plans and criticism episodes would be needed. This does not negate the implemented revision and clearance routes.
- **The verdict parser is a syntax gate, including a concrete failure contrast.** In inspected `scripts/check_review_verdict.ts` (SRC-1), the concrete input `A preface\nVERDICT: pass\nVERDICT: fail` has no provider-error match and its first matching line marker is pass, so it yields pass despite the later fail; input `VERDICT: pass\nauthentication_error` instead yields provider-error. These are deductions through code, not executions. The first input is below 50 bytes but marker matching precedes the size floor. Thus the parser's own inference supports only marker precedence, not an authentic, substantive or correct review. The consumer in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict) changes the step exit status. It is not an answer oracle or proof of the reviewed code's correctness.
- **Evaluation licenses differ.** [EPI-RTE-skill-evals](#epi-rte-skill-evals) uses fixture labels for trigger, guide routing and sufficient/insufficient tool choice, plus external Tessl validation/scores. These are separate targets. The generated sufficiency assertion does not inspect whether an answer is true. Combined-rate admission and review-score admission affect verification, not automatic skill rewrite or parameter updates. No supplied experiment supports transfer, component effects, improved routing or reviewer reliability.
- **Reports reshape evidence; attestations additionally derive a policy result.** [EPI-RTE-report-summary](#epi-rte-report-summary) and [EPI-RTE-activity-summary](#epi-rte-activity-summary) produce bounded selected facts. [EPI-RTE-attestation-build](#epi-rte-attestation-build) derives its gate from run statuses and workflow count. The derivation is warranted relative to those symbolic premises and inspected rules, not independently warranted source truth. [EPI-RTE-attestation-ci](#epi-rte-attestation-ci) checks an attestation for the intended use of CI admission at a PR head. Commit mismatch, false gate and supplied checksum mismatch cause errors; stale time and missing checksum cause warnings. This is evidence-consuming operational acceptance, not semantic acceptance of code behavior. Stored summaries and projections are not automatically lifecycle-integrated accepted claims.
- **Freshness, withdrawal and cleanup are selective.** Review-version mismatch withholds plan clearance; local capability refresh and failed workflow continuation have the limits in [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) and [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run). Empty report output can leave an older report latest, while failure can retain an error artifact. Worktree and temporary-file cleanup in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict) and [EPI-RTE-skill-evals](#epi-rte-skill-evals) does not retract every retained output or undo external effects. No universal correction/withdrawal guarantee follows.

There is implemented retention, selected read-back, evidence-relative derivation, configured admission and criticism-responsive workflow guidance. Direct autonomous behavior/policy adaptation, exercised self-improvement, accepted ampliative claim production and parameter learning are not established by these inspected routes or supplied evidence. The named uninspected operations prevent system-complete negatives; no single system-wide epistemic score follows.

## Shared records

### Operative objects

#### EPI-OBJ-plan
Label: Issue plan and feedback

Natural-language summary, analysis, steps, risks and feedback, with symbolic version and time fields in JSON resources `plan-main` and `feedback-main`. Unlike [RT-OBJ-task-brief](runtime.md#rt-obj-task-brief), this is an issue-lifecycle revision product, not a launch task. It overlaps [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission) as that route's retained input, not as the same object/route. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`. Feedback label does not authenticate human authorship. The body of `iterate` copies caller-supplied revised content; it does not synthesize a revision from evidence.

> summary: args.summary,
> dddAnalysis: args.dddAnalysis,
> steps: args.steps,
> testingStrategy: args.testingStrategy,
> potentialChallenges: args.potentialChallenges,
> feedbackIncorporated: allFeedback,
> --- `extensions/models/issue_lifecycle.ts`

#### EPI-OBJ-adversarial-review
Label: Adversarial review resource

Natural-language finding descriptions and symbolic severity, resolution, plan-version and time fields, persisted as JSON resource `adversarialReview-main`. Distinct from the plan input in [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission) and repository code-review output in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict). Its consumer is issue clearance. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`.

> const findings = args.findings.map((f) => ({
>   ...f,
>   resolved: f.resolved ?? false,
> }));
> --- `extensions/models/issue_lifecycle.ts`

#### EPI-OBJ-verification-summary
Label: Verification summary report

Mixed natural-language Markdown and symbolic JSON reflecting one workflow context, then persisted as report data artifacts. A projection of [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run), not the same run state and not a cryptographically authenticated attestation. SRC-1 implementation: `src/domain/reports/builtin/verification_summary_report.ts`.

> `# Verification Attestation`,
> --- `src/domain/reports/builtin/verification_summary_report.ts`

> type: "verification-summary",
> --- `src/domain/reports/builtin/verification_summary_report.ts`

#### EPI-OBJ-attestation
Label: Verification attestation

Symbolic JSON projection of verification runs and supplied environment/config-integrity values. It declares subject, steps, gate, timing, run identities and review configuration. Distinct derived product from [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run), spans multiple runs rather than being part of one. SRC-1 implementation: `scripts/build_attestation.ts`; CI reads a fetched JSON file in `.github/workflows/ci.yml`. End-to-end hosted storage/authenticity not inspected.

> // Stated, not proven. It says the document was projected from the run
> // records by this script rather than typed out; it does not say the
> // script was the only thing that could have produced it.
> generatedBy: "script",
> --- `scripts/build_attestation.ts`

#### EPI-OBJ-skill-evals
Label: Skill evaluation fixtures and results

Symbolic JSON labels, generated JavaScript assertions/configuration, returned tool-call names and numeric evaluation scores; natural-language queries, descriptions, guide text and failure displays. Fixtures/config/results live in files and driver memory; output and optional Actions summaries retain selected results. No counterpart among supplied runtime objects: [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict) checks code-review markers, not these skill tests. SRC-1 implementation: `evals/promptfoo/generate_config.ts`, `evals/promptfoo/generate_routing_config.ts`, `evals/promptfoo/generate_sufficiency_config.ts`, `scripts/eval_skill_triggers_promptfoo.ts`, `scripts/review_skills.ts`.

> const expectedTool = item.answerable_from_guide
>   ? "answer_from_guide"
>   : "need_reference";
> --- `evals/promptfoo/generate_sufficiency_config.ts`

### Routes

#### EPI-RTE-preflight-check
Label: Local mutating preflight checks
Part of: [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run)

The method service selects registered check callbacks for local mutating methods, calls them with definition/context and unresolved arguments, accumulates failed/invalid/throwing results, then throws before the body if any fail. This is the preflight part of the supplied execution route, not another execution engine. SRC-1 implementation: `src/domain/models/method_execution_service.ts`.

- Immediate return: Boolean pass/error arrays from selected callbacks, or preflight failure exception.
- Later read-back: inapplicable — inspected wrapper consumes callback results within the invocation; no retained predicate result is established here.
- Delegated visibility: Callback receives method name, definition metadata, global/unresolved method arguments and context services; no model delegation inherent in interface.
- Selection predicate: Mutating method, declared checks and local placement; definition skip and appliesTo precede required-name and CLI skip rules.
- Invalidation or expiry: Recomputed on covered invocations; remote placement skips these checks. Definition skip and CLI options can remove checks within their respective rules.
- Activation or effect: A false, invalid or throwing check adds a failure; any failure prevents the covered method body from proceeding.
- Evidence limits: Custom callback truth and external state accuracy uninspected; source wiring does not demonstrate execution or protection against arbitrary host effects.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: behavior/check author; selector and veto: service code plus definition/caller selection. No generic answer oracle. Mode: open automation, not curriculum. Trigger is method invocation, proposed change is its action; selected checks admit/reject only that invocation. No general rollback follows. Guidance and any retained checking policy reside in registered code/definition.

> // Definition-level skip always wins
> if (skippedCheckNames.has(name)) return false;
> --- `src/domain/models/method_execution_service.ts`

> if (!checkResult || typeof checkResult.pass !== "boolean") {
> --- `src/domain/models/method_execution_service.ts`

> throw new UserError(lines.join("\n"));
> --- `src/domain/models/method_execution_service.ts`

#### EPI-RTE-issue-feedback
Label: Issue feedback and revision import

Caller supplies feedback plus a complete revised plan → method enumerates previous feedback → stores feedback and revision → resets phase to plan_generated → lifecycle posting attempt. Unlike [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission), this proposes/revises rather than approves; unlike [RT-RTE-agent-launch](runtime.md#rt-rte-agent-launch), its object is not the launch brief. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`; doctrine/design: `.claude/skills/issue-lifecycle/references/adversarial-review.md`.

- Immediate return: Resource handles and revision/version log; lifecycle recording is attempted.
- Later read-back: `review` reads requested/current plan; later iterate reads current version and previous feedback. Skill instructs later-session state/phase queries and routes approved work to implementation.
- Delegated visibility: Caller supplies revised content and feedback; method does not expose or inspect the reasoning/conversation producing them. Review logs plan summary, steps and testing, not every stored field.
- Selection predicate: Named issue behavior/model identity, `plan-main`, and matching `feedback-main` entries and versions.
- Invalidation or expiry: New version increments current plan version and phase resets; subsequent clearance compares review to plan version. Method declares rollbackOnFailure; global remote/side-effect limits remain in runtime.
- Activation or effect: Writes feedback, plan and phase resources, preserving feedback association; does not itself implement the plan.
- Evidence limits: No actual plan/feedback episode; content truth, feedback incorporation and consent unknown. Prior enumeration depends on repository behavior; no complete historical retention guarantee asserted.
- implementation conclusion status: wired
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Proposer: caller/foreground agent, nominally responding to human or adversarial feedback; method decides structural admission, human is intended plan decider, clearance code can veto later approval. No answer oracle. Open interactive issue work. Guidance asks for actual-code inspection, explicit resolutions, renewed review and human consent. Software persists submitted plan/feedback, not an evidence-consuming semantic acceptance decision. Criticism-to-revision integration is instructed, not proven by copying `feedbackIncorporated`.

> allFeedback.push(args.feedback);
> --- `extensions/models/issue_lifecycle.ts`

> phase: "plan_generated",
> --- `extensions/models/issue_lifecycle.ts:1524-1529`

> 3. **Re-run adversarial review** on the new plan version. The review must be
>    current with the latest plan version — stale reviews block approval.
> --- `.claude/skills/issue-lifecycle/references/adversarial-review.md`

#### EPI-RTE-review-record
Label: Adversarial finding import

Caller-supplied findings → read current plan version → normalize resolution defaults → persist adversarialReview-main and log counts. Distinct from code-review verdict in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict); supplies a new material input to [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission), not that approval operation itself. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`; doctrine/design: `.claude/skills/issue-lifecycle/references/adversarial-review.md`.

- Immediate return: Review resource handle and severity-count log.
- Later read-back: Issue-clearance check reloads review for approval; finding-resolution operations and instructed review rounds can update it.
- Delegated visibility: Caller creates findings under skill instructions; extension receives structured descriptions, severities and flags, not code-inspection proof.
- Selection predicate: Current named issue model and plan; review is stamped with current plan version, or zero if no plan read.
- Invalidation or expiry: Later plan version makes stored review stale for clearance; finding flags may change through resolution.
- Activation or effect: Persists findings that can veto later approval when unresolved at blocking severity.
- Evidence limits: No actual criticism instance or code evidence provided. Current-version stamping does not authenticate what version caller reviewed.
- implementation conclusion status: wired
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Proposer: caller/agent following skill; computational writer stores findings; human contribution not authenticated; clearance code later decides admissibility. No reference-answer oracle. Open review. Proposed update is the review resource; argument validation and downstream policy can reject, while correction/review replaces content. No automatic guarantee that findings are true or fully resolved. Guidance explicitly asks the agent to read actual code rather than trusting plan names.

> "adversarialReview-main",
> {
>   planVersion,
>   findings,
>   reviewedAt: new Date().toISOString(),
> },
> --- `extensions/models/issue_lifecycle.ts`

> For each plan step, **read the actual code**:
> --- `.claude/skills/issue-lifecycle/references/adversarial-review.md`

#### EPI-RTE-issue-clearance
Label: Adversarial review clearance
Part of: [RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission)

The `adversarial-review-clear` preflight callback checks retained plan/review existence, version equality and unresolved critical/high findings before covered approval. This adds the missing computational clearance part to the provisional runtime route; its human-consent limitation remains valid. SRC-1 implementation: `extensions/models/issue_lifecycle.ts`, consumed through `src/domain/models/method_execution_service.ts`.

- Immediate return: `{pass:true}` or false with existence, stale-version or blocking-finding errors.
- Later read-back: inapplicable — this callback reads already retained plan/review and returns a current-invocation decision; its result is not shown as a separate durable artifact.
- Delegated visibility: Callback gets data repository and model identity, not user conversation or code-inspection evidence.
- Selection predicate: Check appliesTo approve; generic local mutating check selection controls whether it runs.
- Invalidation or expiry: Review-plan version mismatch rejects current clearance; resolution flags change next check. Skip/remote alternatives limit enforcement.
- Activation or effect: False result is consumed by method service to block the covered approval body; true result permits further execution checks, not necessarily final approval.
- Evidence limits: Derivation is about retained fields. Caller can submit empty findings or resolution claims; semantic review/human consent not proven. No activation observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: plan/review caller; decider: predicate and execution wrapper; veto: failed selected check. Human intended approval is separate. Oracle: stored review is a premise, not independently known truth. Mode: open issue workflow. Approval criterion is current review without unresolved high/critical findings for proceeding with that plan, not global correctness. No rollback of previous actions follows from a failed clearance.

> appliesTo: ["approve"],
> --- `extensions/models/issue_lifecycle.ts:861-866`

> if (review.planVersion !== plan.version) {
> --- `extensions/models/issue_lifecycle.ts:906-914`

> const unresolved = review.findings.filter(
>   (f) =>
>     !f.resolved &&
>     (f.severity === "critical" || f.severity === "high"),
> );
> --- `extensions/models/issue_lifecycle.ts:914-929`

#### EPI-RTE-report-summary
Label: Verification summary and report retention

One workflow context → selected step facts/counts and Markdown/JSON summary → report execution service → persisted report artifacts/events. Distinct projection from [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run), rather than a new run or code review. SRC-1 implementation: `src/domain/reports/builtin/verification_summary_report.ts`, `src/domain/reports/report_execution_service.ts`; caller failure propagation search: `src/libswamp/models/run.ts`.

- Immediate return: Report Markdown, JSON and handles, or report failure with best-effort error artifact and event.
- Later read-back: Stored report results are exposed through report search/get/describe. Nonempty results persist Markdown/JSON with report tags, 30d lifetime and garbageCollection 5 in writer configuration; backend deletion was not assessed.
- Delegated visibility: Report sees structured workflow context, not external effects; renderer/query consumers receive report products and handles.
- Selection predicate: Scope, registered defaults/require, YAML skip/method scoping and caller filters. Custom reports can execute opaque user code; this record assesses the builtin verification summary only plus its persistence wrapper.
- Invalidation or expiry: Empty Markdown skips persistence and leaves prior real version latest. Exceptions attempt fallback error artifacts; no global retraction of older claims is established.
- Activation or effect: Summaries expose recorded outcomes; report-execution failures count separately and behavior-run caller can mark reporting failed. A report's JSON allPassed is data, not an independent semantic check of execution.
- Evidence limits: No persisted report instance or consumer compliance. Summary's commit comes from inputs, default unknown; no subject/hash authenticity guaranteed by this builtin.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target/domain: one run's recorded step outcomes. Counts are derived over statuses; selected status rendering is reshaping. For concrete input with one succeeded and one skipped/guarded step and workflowStatus succeeded, the inspected builtin yields succeeded=1, skipped=1 and allPassed=true; it does not infer every step executed. This is an implementation deduction. No external answer oracle, knowledge admission or product-change proposal occurs in summary rendering.

> const succeeded = stepExecutions.filter((s) => s.status === "succeeded")
>   .length;
> --- `src/domain/reports/builtin/verification_summary_report.ts`

> allPassed: workflowStatus === "succeeded",
> --- `src/domain/reports/builtin/verification_summary_report.ts`

> // Empty markdown means the report is not applicable to this method.
> // Skip persistence so the previous real version stays latest, but still
> // announce completion so renderers can show it in verbose mode.
> --- `src/domain/reports/report_execution_service.ts`

#### EPI-RTE-attestation-build
Label: Verification attestation projection

Supplied verification runs, definitions and environment → pure buildAttestation projection → subject, steps, run-derived gate/timing and integrity fields for downstream attestation use. Distinct from [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict): consumes verification step statuses, not reviewer prose. It spans several [RT-OBJ-workflow-run](runtime.md#rt-obj-workflow-run) instances rather than being part of one. SRC-1 implementation: `scripts/build_attestation.ts`.

- Immediate return: JSON attestation object from pure function; CLI acquisition/output/posting outside this projection's full inspection.
- Later read-back: CI attestation job fetches by commit and reads gate/subject/hash fields; hosted provenance and persistence not independently established.
- Delegated visibility: Projection gets run records, definitions and supplied environment including hashes. It excludes machinery jobs from step counts.
- Selection predicate: Source runs passed to builder; reviewConfig uses verify-reviews source; gate requires no non-success/non-skip counted step and source count equal expected workflow count.
- Invalidation or expiry: Unknown/running/cancelled counted statuses oppose gate; recorded skips do not. Completion uses available run times with environment-clock fallback when none available. CI independently applies warning/error rules.
- Activation or effect: Produces a gate statement and supporting projection consumed by CI. Does not execute verification or authenticate run records by producing JSON.
- Evidence limits: Function's arithmetic is inspectable; selection, uniqueness, authentic acquisition and upstream run truth need acquisition/server contracts not fully assessed. No observed attestation supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

No counterpart among supplied runtime routes for this aggregate projection. Target is the policy proposition that selected verification records meet builder gate rules. Concrete symbolic deduction: with expected source count and only succeeded/skipped counted steps, failed=0 and allPassed=true; changing one counted step to unknown makes failed positive and gate false. This entails the gate within its formal input domain, not success of untested external operations. It is evidence production, not a separate semantic acceptance decision or automatic code revision.

> const failed = steps.length - succeeded - skipped;
> --- `scripts/build_attestation.ts`

> allPassed: failed === 0 && sources.length === WORKFLOWS.length,
> --- `scripts/build_attestation.ts`

#### EPI-RTE-attestation-ci
Label: CI attestation consistency and admission

Fetched attestation → read fields → version/subject/gate/freshness/hash checks → accumulated errors/warnings → job failure or passing summary. Distinct downstream consumer of [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict), not another reviewer. SRC-1 implementation: `.github/workflows/ci.yml`.

- Immediate return: Actions step summary and exit failure on errors, otherwise pass, possibly with warnings.
- Later read-back: inapplicable — this assessment establishes same-job check consumption and summary emission, not retained learning or later policy adaptation from the summary.
- Delegated visibility: CI receives fetched JSON and checkout files; checks compare named subject to PR head and supplied hashes to local sha256sum results.
- Selection predicate: validate-attestation job and fetched commit-associated attestation; external acquisition/authentication and complete repository protection settings uninspected.
- Invalidation or expiry: Unknown version, subject mismatch, false gate and supplied checksum mismatch add errors; old/unparseable/missing timestamp and missing checksum/file add warnings.
- Activation or effect: Nonzero accumulated errors exits 1; warnings alone pass. Changes CI status, not source code or evaluator policy.
- Evidence limits: Source text establishes this job's protocol, not hosted enforcement, authentic test execution, non-forgeability, complete merge gating or code correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: attestation submitter/generator; decider and veto: CI script on error predicates, not human review. No semantic answer oracle; expected PR head, version and local hashes are reference values for consistency only. Mode: repository verification. Intended use/scope: accepting verification attestation for this PR head under these checks. No automatic rollback; correction/rerun required. This is operational admission with evidence consumption, not acceptance of every plan/code claim.

> if [ "$all_passed" != "true" ]; then
> --- `.github/workflows/ci.yml`

> echo "::warning::Attestation is ${age_hours}h ${age_mins}m old (max 24h)"
> --- `.github/workflows/ci.yml`

> if [ "$errors" -gt 0 ]; then
>   echo "### ❌ Validation Failed" >> "$GITHUB_STEP_SUMMARY"
>   echo "$errors error(s), $warnings warning(s)" >> "$GITHUB_STEP_SUMMARY"
>   exit 1
> --- `.github/workflows/ci.yml`

#### EPI-RTE-skill-evals
Label: Skill test and review admission

Changed-skill guards → skill-review and skill-trigger-eval shell steps in fresh worktree → external Tessl review or promptfoo/provider calls → driver thresholds → workflow step status. Distinct targets from repository code review in [RT-RTE-review-verdict](runtime.md#rt-rte-review-verdict). SRC-1 implementation: `verification/workflow-verify-skills.yaml`, `scripts/review_skills.ts`, `scripts/eval_skill_triggers_promptfoo.ts`, `evals/promptfoo/generate_config.ts`, `evals/promptfoo/generate_routing_config.ts`, `evals/promptfoo/generate_sufficiency_config.ts`.

- Immediate return: Tessl description/content scores and validation status, or generated assertion pass counts/failure outputs; drivers emit summaries and threshold exits.
- Later read-back: Workflow run and shell outputs retain verification outcomes for aggregate verification; optional GITHUB_STEP_SUMMARY gets selected scores/failures. No automatic rewrite or later parameter update established.
- Delegated visibility: Promptfoo calls receive query plus skill descriptions/routing table or guide content and tool definitions. Tessl receives skill directory; its internal rubric/model/process is external and uninspected.
- Selection predicate: Changed-path guard covers skills, CLAUDE.md, review script and eval config paths. Three eval phases compare trigger names, expected guide tool, and sufficient/insufficient tool labels. Review script checks bundled skills.
- Invalidation or expiry: Fresh run worktree; promptfoo --no-cache; provider/config failures stop driver. Cleanup removes worktree and ephemeral definitions, not already captured output records.
- Activation or effect: Review requires each skill's averaged description/content score at least 0.9 and validation passing. Evals use configurable combined pass-rate threshold, default 0.9; driver tolerates promptfoo assertion-failure code 100 before its own threshold check. Failure propagates through shell step.
- Evidence limits: External evaluations unexecuted here; labels/rubrics are references, not established truth. Sufficiency assertion tests returned tool name, not answer entailment; fallback string search weakens structural tool-call interpretation. Combined threshold does not imply every phase/case passes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: skill/code author; computational deciders: assertions and score arithmetic plus external judges; driver vetoes threshold failures. Human fixture authors supply reference labels but per-result human approval not required by drivers. Mode: bounded fixture evaluation and external quality review inside open repository changes, not model training. No automatic successor-skill selection: proposed skill remains caller-authored, repair/rerun manual or agent-directed outside this driver. No runtime learning benefit follows merely from passing.

> const averageScore = (descriptionScore + contentScore) / 2;
> --- `scripts/review_skills.ts`

> if (averageScore < THRESHOLD || !validationPassed) {
>   allPassed = false;
> }
> --- `scripts/review_skills.ts`

> default: { model: "opus", concurrency: "20", threshold: "0.9" },
> --- `scripts/eval_skill_triggers_promptfoo.ts`

> if (combinedRate < passThreshold) {
> --- `scripts/eval_skill_triggers_promptfoo.ts`

> `  return calls.some(c => c.function?.name === needle || c.name === needle || c.functionCall?.name === needle);`,
> --- `evals/promptfoo/generate_sufficiency_config.ts`

#### EPI-RTE-activity-summary
Label: Activity method summary

Cutoff and optional limit → repository outputs/runs/data and current definitions/workflows → grouped activity response. Distinct read-side projection of [RT-RTE-behavior-run](runtime.md#rt-rte-behavior-run) and [RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run), not their persistence or execution routes. This finding is scoped to inspected method aggregation and libswamp entry. SRC-1 implementation: `src/libswamp/summary/summarise.ts`, `src/domain/summary/summary_service.ts`.

- Immediate return: Completed summary or no_activity result; method groups have status counts and selected recent run details.
- Later read-back: inapplicable — reads retained operational records, but inspected summary path does not persist a changed policy/summary for later invocation.
- Delegated visibility: CLI/API consumer receives selected response, not all raw output content; no model call intrinsic to this aggregation.
- Selection predicate: Repository Since(cutoffDate) reads; method grouping uses definition identity/method and current definition name lookup, descending startedAt details and optional per-group limit.
- Invalidation or expiry: Limit truncates details and marks truncated; counts are calculated before truncation. Current name resolution may differ from historical naming.
- Activation or effect: Presents recorded history; no automatic acceptance, source revision or policy adaptation is implemented by inspected method aggregation.
- Evidence limits: Workflow/data grouping branches not fully inspected; repository query completeness and observed consumer use unassessed. Current names are not historical provenance proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

For two method records in the same group with statuses succeeded and failed and limit 1, counts remain total 2/succeeded 1/failed 1, while only the latest detail survives with truncated true. This concrete deduction uses the method aggregation code, not execution. Counts add an entailed fact about selected records; presenting selected records is non-ampliative reshaping, not an explanation of why an operation succeeded.

> if (limit !== undefined && m.runs.length > limit) {
>   m.runs = m.runs.slice(0, limit);
>   m.truncated = true;
> }
> --- `src/domain/summary/summary_service.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; new routes state their consumer, channel, force and horizon in their own fields. Supplied [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions) and [RT-BAP-workflow-execution](runtime.md#rt-bap-workflow-execution) retain their distinct instructional and enforcing channels.
