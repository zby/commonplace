---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SkillNote epistemic routes: procedural candidates, user review, feedback checks and consequential ranking."
run-id: AAS-2026-10-14-skillnote-0ccfe85cda4a-01
reviewed-boundary: "7ea2fc7a8435af64d1c080d8765c0eabba1121ea"
---

# SkillNote epistemic report

## Source-and-claim boundary

The question is what licenses reliance on retained procedures and on feedback about those procedures. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is SRC-1, see [Source register](boundary.md#source-register). The external task-performing models and their weights remain outside the frozen implementation. No observed run, actual skill corpus, approval exchange or causal experiment is supplied. These missing items prevent conclusions about exercised checks, host compliance, source truth and improved capacity respectively.

Skill bodies can contain truth-apt descriptions, explanations and conditional predictions, but imperative instructions are not themselves propositions. Individual corpus claims are **not determinable** without a corpus. Outcome descriptions and comments can assert task-specific facts; numeric ratings are attributed judgments, not verified outcomes. Coverage below includes material shipped operations but is not an exhaustive implementation audit. Available uninspected paths prevent a system-complete negative about semantic evaluation or acceptance.

The consequential public claims found are see [EPI-CLM-pattern-learning](#epi-clm-pattern-learning) and [EPI-CLM-registry-improves](#epi-clm-registry-improves).

| Entry point or operation | Source path in SRC-1 | Coverage and records, or remaining limit |
| --- | --- | --- |
| CLI dispatch | `cli/src/index.ts` | Direct complete dispatch read; add is supplied [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install); update/remove directly read, see [EPI-RTE-install-maintenance](#epi-rte-install-maintenance). Lifecycle, doctor, check, connect/disconnect, bridge and reset internals not independently traced; operational diagnostics, destructive cleanup and adapter revocation guarantees remain incomplete. |
| Registry POST/PATCH, browser save, content rollback | `backend/app/api/skills.py`; `src/lib/skills-store.ts` | Supplied [RT-RTE-registry-write](runtime.md#rt-rte-registry-write). No independent full endpoint audit. |
| Authoring and completion prompts | `plugin/skills/skill-push/SKILL.md`; `plugin/skills/complete-skill/SKILL.md` | Direct full reads; review and rating policies, see [EPI-OBJ-skill-push](#epi-obj-skill-push), [EPI-OBJ-feedback-text](#epi-obj-feedback-text). Skill-creator agent and Codex authoring variants not directly read; no universal authoring-policy conclusion. |
| Claude Code/Codex hooks | `plugin/hooks/hooks.json`; `plugin/hooks-handlers/sync.sh`; `plugin-codex/hooks/handlers/sync.sh` | Supplied [RT-RTE-project-sync](runtime.md#rt-rte-project-sync), [RT-RTE-context-hooks](runtime.md#rt-rte-context-hooks), [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report); direct sync transformation read. Picker and other handler internals remain uninspected; complete context-delivery force not established. |
| MCP registered skill and completion tools | `backend/mcp_server.py` | Supplied [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery), [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report); direct bounded symbol search of tool generation, completion and event logging. No host trace. |
| OpenClaw selection, feedback and context bundle | `plugin-openclaw/skillnote/SKILL.md`; `backend/app/api/openclaw.py` | Direct selection/feedback prompt and complete context-bundle handler reads; supplied [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use). Usage handler validation and watcher parser not fully read; automatic read-event attribution cannot be judged. |
| Comment checks, persistence, edit/delete | `backend/app/api/comments.py`; `backend/app/schemas/comment.py` | Direct complete reads, see [EPI-RTE-comment-check](#epi-rte-comment-check), [EPI-RTE-comment-retention](#epi-rte-comment-retention). |
| Rating submission | `backend/app/api/analytics.py` | Direct payload/submission read; see [EPI-RTE-rating-admission](#epi-rte-rating-admission). Aggregate consumers beyond supplied OpenClaw findings not fully traced; no complete cross-dashboard lineage conclusion. |
| Import/refresh; publish/download withdrawal | `backend/app/services/imports/importer.py`; `backend/app/api/imports.py`; `backend/app/api/publish.py`; `backend/app/api/downloads.py` | Supplied [RT-RTE-source-import](runtime.md#rt-rte-source-import), [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install). Inspectors and refresh diff internals remain uninspected; remote content not captured. |
| Browser reverse import and delivery | `extensions/claude-ai/src/background.ts`; `backend/app/api/claude_ai.py` | Supplied [RT-RTE-browser-sync](runtime.md#rt-rte-browser-sync). Server collision admission and bundle parsing remain uninspected; no complete inbound semantic-preservation conclusion. |
| Adapter self-update | `plugin-openclaw/skillnote/sync.sh` | Supplied [RT-RTE-adapter-update](runtime.md#rt-rte-adapter-update); package bytes absent, so no evaluated improvement conclusion. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-skill-push](#epi-obj-skill-push) | None for imperative steps; rationale about persistent conventions can be truth-apt | see record | SRC-1, `plugin/skills/skill-push/SKILL.md` | Policy is shipped, compliance unobserved |
| [EPI-OBJ-skill-content](#epi-obj-skill-content) | Conditional procedural predictions, explanations or factual assertions if present | see record | SRC-1, `plugin/hooks-handlers/sync.sh` | No actual registry corpus supplied |
| [EPI-OBJ-feedback-text](#epi-obj-feedback-text) | Task outcomes, alleged issues, patch suggestions, deprecation assertions | see record | SRC-1, `plugin-openclaw/skillnote/SKILL.md` | Attributed judgments; source truth unchecked |
| [EPI-OBJ-context-bundle](#epi-obj-context-bundle) | Counts/means about stored reports; status labels are code classifications | see record | SRC-1, `backend/app/api/openclaw.py` | A label does not establish semantic health |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Internal truth-apt content not determinable | see record | SRC-1, `plugin-openclaw/skillnote/SKILL.md` | Exact model and parameter updates uninspected |

## Authority-route ledger

Fields owned by cited records are given as `see`; entries below split checking, disposition, retention and selection rather than assigning one warrant to a whole pipeline.

Route ID: [RT-RTE-registry-write](runtime.md#rt-rte-registry-write)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Conversation convention into reusable procedure. Literal preservation and new generalization are both possible; no draft instance permits choosing between them.
Evaluator/condition and domain: see record; draft guidance is not an inference proof.
Activation and timing: see record
Possible or observed result: see record
Implemented force: Authoring request only; no observed generation.
Epistemic authority and scope: Candidate procedure only, not established transfer from repeated instances.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-host-instructions](runtime.md#rt-bap-host-instructions)
Evidence source ID and local anchor: SRC-1, `plugin/skills/skill-push/SKILL.md`
Claim IDs: [EPI-CLM-pattern-learning](#epi-clm-pattern-learning)
Mismatch marker: Repetition does not establish correctness or improved capacity.
Gap/limit: No produced instance or approval transcript.

Route ID: [RT-RTE-registry-write](runtime.md#rt-rte-registry-write)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: Full draft and trigger-description suitability for publishing as a reusable skill.
Evaluator/condition and domain: Human preview and approval, see record. The named prompt criterion is good trigger keywords, not verified factual accuracy.
Activation and timing: see record
Possible or observed result: Approval or refusal requested; no evidence-consuming decision observed.
Implemented force: Prompt policy, bypassable through direct API writes.
Epistemic authority and scope: No recorded truth acceptance; proposed user approval licenses publication on this path.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: Authoring agent, user response, permissive publication policy, current draft.
Evidence source ID and local anchor: SRC-1, `plugin/skills/skill-push/SKILL.md`
Claim IDs: [EPI-CLM-pattern-learning](#epi-clm-pattern-learning)
Mismatch marker: Approval cannot be generalized to alternate admission paths.
Gap/limit: Actual user reasoning and criterion application unknown.

Route ID: [RT-RTE-registry-write](runtime.md#rt-rte-registry-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller-provided instruction body into current row and snapshot; source warrant unknown.
Evaluator/condition and domain: see record; structural request checks do not evaluate content truth.
Activation and timing: see record
Possible or observed result: see record
Implemented force: Database persistence; separate browser-local fallback.
Epistemic authority and scope: Availability as a candidate, not evidence-consuming truth acceptance or lifecycle integration.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-host-instructions](runtime.md#rt-bap-host-instructions)
Evidence source ID and local anchor: SRC-1, `backend/app/api/skills.py`
Claim IDs: [EPI-CLM-pattern-learning](#epi-clm-pattern-learning)
Mismatch marker: Retention is not acceptance.
Gap/limit: No observed saved candidate; alternate history semantics bounded by runtime record.

Route ID: [RT-RTE-source-import](runtime.md#rt-rte-source-import), [RT-RTE-browser-sync](runtime.md#rt-rte-browser-sync)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: External procedures admitted to registry, warrant unknown; not locally produced knowledge.
Evaluator/condition and domain: see records; branch selection and collision handling are not source-truth tests.
Activation and timing: see records
Possible or observed result: see records
Implemented force: Registry admission and redistribution, bounded by inspected branches.
Epistemic authority and scope: No source correctness license established.
Operational authority: behavior permitted, blocked, or changed: see records
Behavioral-authority path: consumer, channel, force, horizon: see records and [RT-BAP-host-instructions](runtime.md#rt-bap-host-instructions)
Evidence source ID and local anchor: SRC-1, `backend/app/services/imports/importer.py`; `extensions/claude-ai/src/background.ts`
Claim IDs: none
Mismatch marker: Same-origin hash update can leave body unchanged; refresh apply is a stub, see runtime.
Gap/limit: Imported source content and reverse-import parsing unavailable or uninspected respectively.

Route ID: [RT-RTE-project-sync](runtime.md#rt-rte-project-sync), [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Packaging and configured URL substitution, not generalization or correctness checking.
Evaluator/condition and domain: Inspected string concatenation/replacement; see [EPI-OBJ-skill-content](#epi-obj-skill-content) for concrete symbolic deduction.
Activation and timing: see records
Possible or observed result: see records
Implemented force: Files or returned tool prose.
Epistemic authority and scope: No additional warrant for the body's assertions. Configured URLs bind placeholders; arbitrary uses of placeholder strings may change literal meaning.
Operational authority: behavior permitted, blocked, or changed: see records
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-host-instructions](runtime.md#rt-bap-host-instructions)
Evidence source ID and local anchor: SRC-1, `plugin/hooks-handlers/sync.sh`; `backend/mcp_server.py`
Claim IDs: [EPI-CLM-pattern-learning](#epi-clm-pattern-learning)
Mismatch marker: Delivery is not application.
Gap/limit: Classification applies to inspected packaging, not arbitrary corpus compression or semantic equivalence of all placeholder uses.

Route ID: [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install), [EPI-RTE-install-maintenance](#epi-rte-install-maintenance)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: Bundle byte agreement, extractable entry structure, active release availability; not procedure efficacy.
Evaluator/condition and domain: see records
Activation and timing: see records
Possible or observed result: see records
Implemented force: Check failures prevent installation/update through selected branches.
Epistemic authority and scope: Checksum consistency and archive constraints only, not authentic authorship, safe agent actions or task truth.
Operational authority: behavior permitted, blocked, or changed: see records
Behavioral-authority path: consumer, channel, force, horizon: CLI installer, code branch, enforcing, current install/update attempt.
Evidence source ID and local anchor: SRC-1, `cli/src/commands/update.ts`; `backend/app/api/downloads.py`
Claim IDs: none
Mismatch marker: Cached installations and current-row delivery survive archive withdrawal.
Gap/limit: No observed installation; no universal revocation.

Route ID: [EPI-RTE-install-maintenance](#epi-rte-install-maintenance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-content](#epi-obj-skill-content)
Content/update relation: no content change
Transition or check target: Update/release replacement or local removal, not epistemic rejection.
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: File replacement/removal or skipped update; shared files may be retained.
Epistemic authority and scope: No changed truth license; active status is release selection.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: Host discovery via local files, enforcing filesystem availability, later sessions until replaced/removed.
Evidence source ID and local anchor: SRC-1, `cli/src/commands/update.ts`; `cli/src/commands/remove.ts`
Claim IDs: none
Mismatch marker: Withdrawn release skips updating rather than deleting the previous copy.
Gap/limit: Cross-adapter rollback and host compliance unestablished.

Route ID: [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-feedback-text](#epi-obj-feedback-text)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Fit/helpfulness of a procedure in a completed task.
Evaluator/condition and domain: External agent self-assessment, see [EPI-OBJ-feedback-text](#epi-obj-feedback-text); no independent expected-answer oracle supplied.
Activation and timing: see record
Possible or observed result: Requested 1–5 judgment plus optional outcome, not observed evaluation.
Implemented force: Advisory reporting request only.
Epistemic authority and scope: Attributed assessment of local task utility; does not warrant producing process, mechanism or transfer.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: Host agent receives rating instruction, advisory, after task use.
Evidence source ID and local anchor: SRC-1, `plugin/skills/complete-skill/SKILL.md`
Claim IDs: [EPI-CLM-registry-improves](#epi-clm-registry-improves)
Mismatch marker: Self-report differs from measured benefit.
Gap/limit: Outcome truth, actual checking and non-entailment of generated explanations not determinable.

Route ID: [EPI-RTE-comment-check](#epi-rte-comment-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-feedback-text](#epi-obj-feedback-text)
Content/update relation: no content change
Transition or check target: Comment structure and optional usage-reference membership, not factual complaint truth.
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: Validation errors prevent admission on this endpoint.
Epistemic authority and scope: Referential consistency under the named conditions only; no verified task outcome.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: Handler, parsed payload and database lookup, enforcing, current request.
Evidence source ID and local anchor: SRC-1, `backend/app/api/comments.py`; `backend/app/schemas/comment.py`
Claim IDs: [EPI-CLM-registry-improves](#epi-clm-registry-improves)
Mismatch marker: Linked usage is optional and membership guard excludes empty skill lists.
Gap/limit: Caller-supplied author_type is not independently authenticated evaluator identity here.

Route ID: [EPI-RTE-comment-retention](#epi-rte-comment-retention), [EPI-RTE-rating-admission](#epi-rte-rating-admission), [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-feedback-text](#epi-obj-feedback-text)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Retain caller assessments, with source warrant unknown. API `accepted` is submission success, not epistemic acceptance.
Evaluator/condition and domain: see records
Activation and timing: see records
Possible or observed result: see records
Implemented force: Database reporting and later aggregation.
Epistemic authority and scope: Retained allegations/judgments; no named evidence-consuming truth decision.
Operational authority: behavior permitted, blocked, or changed: see records
Behavioral-authority path: consumer, channel, force, horizon: see records; distinct comment and SkillRating stores have distinct consumers.
Evidence source ID and local anchor: SRC-1, `backend/app/api/comments.py`; `backend/app/api/analytics.py`; `backend/mcp_server.py`
Claim IDs: [EPI-CLM-registry-improves](#epi-clm-registry-improves)
Mismatch marker: Comment delete does not retract its fan-out SkillRating in inspected handler.
Gap/limit: No observed reports; current-version attribution need not identify the version actually used.

Route ID: [EPI-RTE-bundle-metadata](#epi-rte-bundle-metadata)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-bundle](#epi-obj-context-bundle)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Counts and rating means derived from retained rows within the SQL filters; status label derived from rating threshold/deprecation existence.
Evaluator/condition and domain: see record; database aggregation and code rules, not an environmental task evaluator.
Activation and timing: see record
Possible or observed result: see record
Implemented force: Metadata returned to bundle consumers.
Epistemic authority and scope: Conditional arithmetic facts about stored rows only, assuming database evaluation matches inspected SQL. No warrant for report truth or semantic skill health.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: SRC-1, `backend/app/api/openclaw.py`
Claim IDs: [EPI-CLM-registry-improves](#epi-clm-registry-improves)
Mismatch marker: `healthy` also results when there is no rating and no deprecation warning.
Gap/limit: Premises are warranted as inspected rules, not as observed accurate task reports.

Route ID: [EPI-RTE-bundle-selection](#epi-rte-bundle-selection)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-context-bundle](#epi-obj-context-bundle)
Content/update relation: non-truth-apt policy/content update: feedback-dependent candidate ordering and truncation
Transition or check target: Change which procedures enter the response, using persisted usage and comment ratings.
Evaluator/condition and domain: see record; proxy ranking, not semantic task matching or truth acceptance.
Activation and timing: see record
Possible or observed result: see record
Implemented force: Ranking plus enforcing truncation of returned catalog.
Epistemic authority and scope: None beyond metadata arithmetic; popularity and rating do not establish correctness.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: SRC-1, `backend/app/api/openclaw.py`
Claim IDs: [EPI-CLM-registry-improves](#epi-clm-registry-improves)
Mismatch marker: An alphabetic preliminary window excludes some skills before feedback ranking; shipped prompt does not establish resolver invocation.
Gap/limit: No observed selection, task effect or improvement comparison.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-pattern-learning](#epi-clm-pattern-learning) | see record | SRC-1, `plugin/skills/skill-push/SKILL.md`, doctrine/design | Confirmation, draft, preview and push policy | [RT-RTE-registry-write](runtime.md#rt-rte-registry-write), [RT-RTE-project-sync](runtime.md#rt-rte-project-sync), [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery) | None supplied | No controlled task comparison or host consumption trace | Persistent procedural distribution is supported; candidate generalization is requested | Improved agent capacity and reliable generalization unestablished |
| [EPI-CLM-registry-improves](#epi-clm-registry-improves) | see record | SRC-1, `plugin-openclaw/skillnote/SKILL.md`, doctrine/design | Outcome honesty and concrete typed feedback requested | [EPI-RTE-comment-retention](#epi-rte-comment-retention), [EPI-RTE-bundle-selection](#epi-rte-bundle-selection), [EPI-RTE-bundle-metadata](#epi-rte-bundle-metadata) | None supplied | Popularity/rating proxy, optional lineage and no independent outcome verification | Feedback can change delivered candidate order and review labels | No demonstrated skill-content correction, truth acceptance or successful improvement follows |

## Bounded conclusion

SkillNote acquires, stores and distributes procedural candidates. It has separate prompt-level author approval, code-level structural admission, release checks and host-level application paths. Their authority is not interchangeable. See [RT-RTE-registry-write](runtime.md#rt-rte-registry-write), [RT-RTE-source-import](runtime.md#rt-rte-source-import), [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery). Imported warrant remains unknown; wrapping and placeholder substitution add no truth warrant. The draft route may preserve an explicit convention or propose a new rule; no draft evidence supports a specific ampliative-conjecture finding.

The named proposed human criterion is trigger suitability for reusable publication, not a demonstrated evidence-consuming acceptance of a truth-apt claim. Checks of range, reference consistency, checksum and release status have narrower licenses. No lifecycle integration after epistemic acceptance is established in the inspected routes; this is not a system-complete absence because the coverage table names remaining uninspected paths.

Feedback has consequential implemented consumers. Comment-backed counts, averages, deprecation flags and truncated comments reach later context-bundle requests; ordering and truncation change the available catalog. See [EPI-RTE-bundle-metadata](#epi-rte-bundle-metadata) and [EPI-RTE-bundle-selection](#epi-rte-bundle-selection). This is direct feedback-dependent behavior shaping without establishing a new accepted truth claim. Arithmetic derivation is licensed only over retained rows, not task efficacy. Warnings yield `needs_review`, not automatic withdrawal; absence of warnings yields no correctness assurance.

Withdrawal and recovery are path-specific. Archive download rejection does not revoke current-row MCP content or cached installations. CLI update can skip a withdrawn skill while preserving the installed copy; remove can preserve shared global files. Comment deletion can remove a bundle warning without removing its analytics rating fan-out. See [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install), [EPI-RTE-install-maintenance](#epi-rte-install-maintenance), [EPI-RTE-comment-retention](#epi-rte-comment-retention).

The external distributed-parametric model remains see [RT-CMP-host-model](runtime.md#rt-cmp-host-model). Feedback retention and ranking do not establish weight learning. Future-action improvement, reliable reflection, autonomous content criticism and exercised self-improvement remain independently unestablished, not collectively absent. Adapter version replacement is an update route, not an evidenced improvement experiment, see [RT-RTE-adapter-update](runtime.md#rt-rte-adapter-update). No single system-wide epistemic verdict follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-skill-push
Label: Skill Push authoring policy

Natural-language guidance stored in shipped Markdown, SRC-1, `plugin/skills/skill-push/SKILL.md`. It asks an external authoring agent to turn persistent conventions into reviewed instructions. No object counterpart is declared in the supplied runtime; [RT-RTE-registry-write](runtime.md#rt-rte-registry-write) describes its consuming route, not this static text object. Human permission and final review are guidance, not universal backend enforcement.

> Only suggest for PERSISTENT conventions, not temporary workarounds.
> --- `plugin/skills/skill-push/SKILL.md`

> Show complete skill preview. Emphasize: "Does the description have good trigger keywords?" Wait for approval.
> --- `plugin/skills/skill-push/SKILL.md`

#### EPI-OBJ-skill-content
Label: Retained skill body

Natural-language description/body, stored in registry rows, content snapshots and installed Markdown. Truth-apt assertions, if present, coexist with imperative instructions. No runtime object counterpart; overlapping routes are [RT-RTE-registry-write](runtime.md#rt-rte-registry-write), [RT-RTE-project-sync](runtime.md#rt-rte-project-sync) and [RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery). This is their carried content, not another delivery route. Source-native field `content_md` supplies identity. SRC-1, `plugin/hooks-handlers/sync.sh`.

Concrete deduction from inspected code, not target execution: for a nonempty body `Fetch {{API_URL}}/v1/skills`, configured API `http://localhost:8082` and otherwise ordinary skill metadata, replacement produces `Fetch http://localhost:8082/v1/skills`, then attaches frontmatter. No new causal claim about fetching is inferred. Wrapping is non-ampliative; placeholder binding does not guarantee all literal uses preserve intended meaning.

> raw_body = raw_body.replace('{{API_URL}}', api_url).replace('{{WEB_URL}}', web_url)
> content = '---\n' + '\n'.join(fm_lines) + '\n---\n\n' + raw_body
> --- `plugin/hooks-handlers/sync.sh`

#### EPI-OBJ-feedback-text
Label: Ratings and outcome comments

Natural-language outcome/comment bodies and symbolic scores/types, split by consumption: humans/models interpret text; range checks, arithmetic and status rules consume numeric/type fields. Storage substrates are Comment and SkillRating database rows, not host weights. SRC-1, `backend/app/api/comments.py`, `backend/app/api/analytics.py`. No supplied object counterpart; [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report) is the reporting container. The objects carry attributed assessments, not verified ground truth.

> - **5** — Perfect fit, followed instructions exactly
> - **4** — Good, mostly helpful with minor adjustments
> - **3** — Okay, partially useful
> - **2** — Poor, unclear or wrong approach
> - **1** — Not applicable or caused issues
> --- `plugin/skills/complete-skill/SKILL.md`

> - **`failed`** — skill applied BUT didn't help (wrong result, error, or trigger criteria didn't match the actual situation). Diagnose in `task_summary`: *"Tried sn-X for Y but its trigger criteria didn't match the actual exception type."*
> --- `plugin-openclaw/skillnote/SKILL.md`

#### EPI-OBJ-context-bundle
Label: Context bundle metadata

Symbolic usage counts, mean ratings and status labels plus natural-language latest-comment prefix and current skill text. Stored response is current-request data derived from retained database rows; later requests reconstruct it. SRC-1, `backend/app/api/openclaw.py`. No runtime object counterpart; [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use) contains its generation/use route. Text and metadata have different licenses: a 200-character comment prefix can omit conditions, while a mean characterizes stored ratings rather than procedure truth.

> row.skill_id: row.body[:200] if row.body else None
> --- `backend/app/api/openclaw.py`

### Routes

#### EPI-RTE-comment-check
Label: Comment reference validation

Caller → schema → comment handler → structural/reference success or API error. Owner is backend code. Target/domain: nonempty body, permitted comment type/author-type combination, rating 1–5 and optional linked event existence; if an agent cites an event with a nonempty skill list, the commented skill must occur there. This counterexample to an unqualified "no checking" claim establishes real checks but not claim-truth evaluation. No expected-answer oracle. Open-request feedback; caller proposes content, code can reject, human veto is not required. Distinct from [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report): a comment endpoint, not MCP rating insertion. SRC-1, `backend/app/api/comments.py`, `backend/app/schemas/comment.py`.

- Immediate return: Validated payload progression or 422/404 error.
- Later read-back: inapplicable — validation itself persists nothing; separately admitted comments are handled by comment retention.
- Delegated visibility: API caller receives errors; no external task trace is inspected.
- Selection predicate: Skill slug, author_type, optional linked_usage_id and nonempty linked skill_ids.
- Invalidation or expiry: inapplicable — per-request checks, not retained claims.
- Activation or effect: Invalid requests are blocked by code; actual activation unobserved.
- Evidence limits: No task-result verification; linked usage optional and caller authorship fields not independently verified here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (
>             payload.author_type == "agent"
>             and usage_event.skill_ids  # non-empty list
>             and str(skill.id) not in usage_event.skill_ids
>         ):
> --- `backend/app/api/comments.py`

> rating: int | None = Field(default=None, ge=1, le=5)
> linked_usage_id: uuid.UUID | None = None
> --- `backend/app/schemas/comment.py`

#### EPI-RTE-comment-retention
Label: Comment persistence and removal

Validated caller → Comment row; an agent rating additionally creates a SkillRating. Owner is backend. Subsequent bundle queries read comments; analytics reads rating rows. PATCH changes body only; DELETE deletes the selected Comment, not its fan-out rating in this inspected handler. Admission is structural validation, not acceptance of a proposed mechanism. Caller proposes; software decides structural admission; no human approval artifact or independent outcome oracle. Open feedback requests; delete/edit provide partial correction, no automatic instruction patch. Distinct endpoint from [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report), linked later consumer is a part of [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use). SRC-1, `backend/app/api/comments.py`.

- Immediate return: Committed comment, edited comment or 204 deletion.
- Later read-back: Comments feed later lists, rating means, latest comment text and deprecation flags; fan-out ratings feed analytics.
- Delegated visibility: Registry/bundle clients receive comment-derived data; host application remains unobserved.
- Selection predicate: Skill slug; edit/delete additionally require comment ID tied to that skill; fan-out requires author_type agent and nonnull rating.
- Invalidation or expiry: Body edits update the comment; delete removes that row, with no fan-out rating retraction in inspected code.
- Activation or effect: Durable database changes wired; no observed truthful assessment or improvement.
- Evidence limits: No authentication or corpus correctness assessment; old warnings remain effective until removed, and latest-comment prefixes need not explain older warning flags.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if payload.author_type == "agent" and payload.rating is not None:
>         db.add(SkillRating(
> --- `backend/app/api/comments.py`

> db.delete(comment)
> db.commit()
> --- `backend/app/api/comments.py`

#### EPI-RTE-rating-admission
Label: Analytics rating submission

Caller → RatingPayload structural validation → deduplicating update or insert → commit and `accepted`. Owner is backend code. Score, version, session and outcome are caller supplied; no task oracle is consumed. Distinct from [RT-RTE-feedback-report](runtime.md#rt-rte-feedback-report): REST analytics endpoint accepts submitted version rather than the inspected MCP current-version lookup. User/agent supplies proposal, code rejects structural violations; open feedback mode, no required human approval. Replacement for matching session/agent/slug supplies recovery from duplicate reports, not content rollback. SRC-1, `backend/app/api/analytics.py`.

- Immediate return: accepted submission JSON after database commit.
- Later read-back: Rating/outcome rows remain available to reporting consumers; not the Comment-based bundle mean unless separately inserted there.
- Delegated visibility: API caller gets submission acknowledgment; later reporting clients can retrieve assessments.
- Selection predicate: Supplied slug; deduplication only with nonempty session_id and matching slug/session/agent.
- Invalidation or expiry: Matching deduplication updates rating, outcome, version and timestamp; no expiry in this handler.
- Activation or effect: Reporting persistence wired; successful task checking not established.
- Evidence limits: `accepted` means admitted report, not epistemic acceptance; no usage-proof or actual consumed-version comparison in inspected handler.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> skill_version: int = Field(default=1, ge=0)
> session_id: str = Field(default="", max_length=256)
> --- `backend/app/api/analytics.py`

> return {"status": "accepted", "skill_slug": payload.skill_slug, "rating": payload.rating}
> --- `backend/app/api/analytics.py:338-338`

#### EPI-RTE-bundle-metadata
Label: Context bundle aggregation
Part of: [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use)

Database rows → aggregate SQL → metadata/status response. Backend owns arithmetic and classification. Usage count concerns retained events newer than 30 days; ratings average all nonnull Comment ratings for candidate skills; any deprecation-warning comment triggers review regardless of latest comment. No outcome oracle is consumed. Status rule is classification, not semantic validation. SRC-1, `backend/app/api/openclaw.py`.

- Immediate return: Counts, means, latest-comment prefix and healthy/needs_review labels in bundle.
- Later read-back: Later bundle requests recompute from durable comments and usage events; bundle response itself is not retained memory.
- Delegated visibility: Bundle caller receives metadata and current bodies; described resolver compliance not observed.
- Selection predicate: Candidate skill IDs and stated SQL filters.
- Invalidation or expiry: Usage ages out of 30-day window; changed/deleted comments change subsequent means/flags; no deprecation-age cutoff in inspected query.
- Activation or effect: Code computes metadata; no observed output or truthful premises supplied.
- Evidence limits: Counts/means describe reported data, not verified effectiveness; healthy can mean no evidence of trouble.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> select(Comment.skill_id, func.avg(Comment.rating).label("avg"))
>         .where(Comment.skill_id.in_(skill_id_uuids))
>         .where(Comment.rating.is_not(None))
>         .group_by(Comment.skill_id)
> --- `backend/app/api/openclaw.py`

> def _staleness(skill_id, rating: float | None) -> str:
>         if skill_id in deprecated:
>             return "needs_review"
>         if rating is not None and rating < 3.0:
>             return "needs_review"
>         return "healthy"
> --- `backend/app/api/openclaw.py`

Concrete implementation deduction: two retained ratings 1 and 5 give mean 3; with no warning the status is healthy. Adding a warning changes status to needs_review without changing body or mean. Thus labels neither verify correctness nor automatically disable delivery.

#### EPI-RTE-bundle-selection
Label: Context bundle proxy selection
Part of: [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use)

Candidate database query → alphabetic max_skills*4 window → descending usage, descending rating, name tiebreak → requested-size response. Backend decides; caller supplies limit/collection, not semantic ranking evidence. Persisted feedback changes later candidate availability. No answer oracle; ordinary request mode. Code truncates, no human per-response veto required. No instruction-body change is admitted here; recovery is a later request with changed inputs or retained reports. SRC-1, `backend/app/api/openclaw.py`.

- Immediate return: Ordered truncated candidate bundle.
- Later read-back: Repeated requests use persisted usage counts and Comment ratings to select procedures differently.
- Delegated visibility: Caller receives only selected candidate window; excluded rows cannot be reranked from this response.
- Selection predicate: Optional collection, initial alphabetic limit, usage count, rating mean, name and max_skills.
- Invalidation or expiry: Changed counts/comments or elapsed usage window can change ranking; current catalog changes alter initial window.
- Activation or effect: Enforcing candidate truncation is wired; actual host behavior and task improvement unobserved.
- Evidence limits: Proxy selection does not consume task summary here; resolver docstring is not execution evidence; endpoint use by shipped foreground picker unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> candidate_skills.sort(
>         key=lambda s: (
>             -int(usage_counts.get(str(s.id), 0)),  # higher usage first
>             -(rating_avgs.get(s.id) or 0.0),       # higher rating first
>             s.name,                                 # alphabetical tiebreak
>         )
>     )
>     ranked_skills = candidate_skills[: req.max_skills]
> --- `backend/app/api/openclaw.py`

#### EPI-RTE-install-maintenance
Label: CLI update and removal

CLI user request → installed manifest → update active version/checksum or remove adapter files → manifest save. Code owns effects; server release status supplies update eligibility. Different from [RT-RTE-bundle-install](runtime.md#rt-rte-bundle-install): successor replacement/removal of existing installs rather than first add. Caller proposes updating/removing identifier, code decides active version and checks bytes; optional yes flag is exposed but inspected update function does not request approval. Open operational maintenance, no answer oracle or improvement experiment. Replacement deletes destination before copying; no transactional multi-adapter rollback established. Remove checks global sharing before deleting user-scoped files. SRC-1, `cli/src/commands/update.ts`, `cli/src/commands/remove.ts`.

- Immediate return: Updated/skipped/failed notices or removal notice; manifest reflects completed local changes.
- Later read-back: External hosts may consume replacement files; skipped withdrawn updates preserve installed files; shared global removal retains files for other projects.
- Delegated visibility: Adapter destinations select host exposure; not a universal registry revocation channel.
- Selection predicate: Installed slug(s), first active returned release or current checksum; remove uses manifest agents and global install release result.
- Invalidation or expiry: Replacement removes old destination and Codex legacy path where applicable; removal deletes only eligible adapter files and manifest entry.
- Activation or effect: Filesystem/manifest writes wired; no observed update or host discovery supplied.
- Evidence limits: Checksum establishes byte agreement only; partial-copy failure rollback, global-registry internals and host compliance not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!latest && versions.length > 0) {
>       spin.stop()
>       ui.warn(`${slug}: no active version (all published versions are disabled)`)
>       skipped++
>       continue
>     }
> --- `cli/src/commands/update.ts`

> if (!releaseGlobalInstall(agentName, skill, projectDir)) {
>         shared.push(adapter.displayName)
>         continue
>       }
> --- `cli/src/commands/remove.ts`

### Claims

#### EPI-CLM-pattern-learning
Label: Agents learn repeated patterns

SRC-1 doctrine/design, `plugin/skills/skill-push/SKILL.md`, claims connected agents learn from repeated patterns through publishing skills. No supplied claim counterpart; [RT-RTE-registry-write](runtime.md#rt-rte-registry-write) supplies the proposed path. Persistence and delivery are supported, improved future-action capacity is not demonstrated.

> Create and push reusable skills to the SkillNote registry so all connected agents learn from repeated patterns.
> --- `plugin/skills/skill-push/SKILL.md`

#### EPI-CLM-registry-improves
Label: Registry improves from feedback

SRC-1 doctrine/design, `plugin-openclaw/skillnote/SKILL.md`, links which-helped/failed signals to registry improvement over time. No supplied claim counterpart. [RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use) is the parent workflow; aggregation/selection parts establish a narrower feedback consumer, not measured improvement.

> description: "Self-hosted skill registry for OpenClaw. Stores procedures your team writes (name, description, body), syncs them to disk before each task, and collects which-helped/which-failed signals from the agent so the registry improves over time."
> --- `plugin-openclaw/skillnote/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
