---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Claude Context Guard's truth-apt records, QA and lesson admission, integrity checks and later behavioral authority."
run-id: AAS-2026-10-13-claude-context-guard-357cd90664df-01
reviewed-boundary: efcd0a1815887483a862b32bfb3fbfd6aac79aa6
---

# Claude Context Guard epistemic report

## Source-and-claim boundary

The question is what licenses later reliance on project records, learned behaviours, helpers and code descriptions, rather than merely making them available. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). SRC-1 supplies executable shell implementation and model-facing doctrine/design. It supplies no populated project histories, tests of generated helpers, observed host invocation or causal comparison. Model compliance, actual acceptance, successful recovery and improved future action therefore remain unobserved. External research linked by the README is not evidence acquired in this run. Images and host/provider internals remain excluded as in the boundary.

This analyst directly read the installer, settings, both hooks, all six commands, all eight templates and README at the registered revision. The tracked dispatch surface agrees with the supplied runtime: six command prompts, two event hooks, installer and manual-copy entry points; no additional registered tool operation was found in those paths. The table distinguishes these reads from reliance on runtime records. Nothing in the relevant shipped text surface is left unassessed; this is not complete coverage of possible consumer-project or host operations.

| Entry point or operation | Source path | Coverage and evidence basis |
|---|---|---|
| Install and manual copy | SRC-1, `install.sh`, `README.md`, `.claude/settings.json` | Direct reads; see [RT-RTE-install-package](runtime.md#rt-rte-install-package). Copy admission and conditional hook activation, not truth validation. |
| First-run creation and recovery | SRC-1, `.claude/commands/start.md` | Direct read; see [RT-RTE-start-session](runtime.md#rt-rte-start-session). Imports human details; later consumes current files and selected archive entries. |
| Incremental updates and code-index maintenance | SRC-1, `templates/CLAUDE.md` | Direct read; see [RT-BAP-project-rules](runtime.md#rt-bap-project-rules). Model-operated logging and description revision, not an executable acceptance gate. |
| Checkpoint, wrap-up, rotation and supersession | SRC-1, `.claude/commands/save.md`, `.claude/commands/end.md` | Direct reads; see [RT-RTE-save-session](runtime.md#rt-rte-save-session), [EPI-RTE-feature-check](#epi-rte-feature-check), [EPI-RTE-feature-admission](#epi-rte-feature-admission). |
| Scratch-script harvest, helper tests, approval and deletion | SRC-1, `.claude/commands/lessons.md` | Direct read; see [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons), [EPI-RTE-lesson-inference](#epi-rte-lesson-inference). |
| Code labels, description generation, filtered comparison and restoration | SRC-1, `.claude/commands/itemise.md` | Direct read; see [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code), [EPI-RTE-itemise-filter](#epi-rte-itemise-filter). |
| Integrity diagnosis, report retention, selected repairs | SRC-1, `.claude/commands/audit.md` | Direct read; see [RT-RTE-audit-project](runtime.md#rt-rte-audit-project). Includes archive IDs, dates, contradictions and source/sidecar parity. |
| Commit reminder | SRC-1, `.claude/hooks/pre-commit-check.sh` | Direct read; see [RT-RTE-commit-reminder](runtime.md#rt-rte-commit-reminder). Raw substring produces advice, not a ledger check. |
| PreCompact backup | SRC-1, `.claude/hooks/pre-compact-save.sh` | Direct read; see [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup). Existing bytes copied, no knowledge acceptance or automatic later restore. |
| Retained-state formats | SRC-1, `templates/COMMENTS.md`, `templates/SESSION_LOG.md`, `templates/RESUME_STATE.md`, `templates/TASK_REGISTRY.md`, `templates/DECISIONS.md`, `templates/LEARNED_BEHAVIOUR.md`, `templates/FEATURE_LIST.json` | Direct reads; see object records below. Templates are not actual histories or QA results. |
| Host numerical state and compaction | SRC-1, `README.md`, `.claude/settings.json` | Supplied host findings: see [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code). No accessible parameters, exact model version, model processing trace or compaction policy; truth-apt numerical content and parameter learning are not determinable. |

Consequential claims are see [RT-CLM-progress-protection](runtime.md#rt-clm-progress-protection), [EPI-CLM-diff-record](#epi-clm-diff-record), [EPI-CLM-helper-safety](#epi-clm-helper-safety), [EPI-CLM-archive-truth](#epi-clm-archive-truth), [EPI-CLM-itemise-preservation](#epi-clm-itemise-preservation) and [EPI-CLM-context-economy](#epi-clm-context-economy). Their scopes differ: recovering records is not producing justified factual knowledge; navigating code is not proving code descriptions true.

## Epistemic-object inventory

Object identities, forms, substrates and quoted evidence are owned by the cited records; `see` below refers to those fields rather than redeclaring them. Candidate content is scoped to hypothetical consumer entries, not to the empty/example templates.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-comments](#epi-obj-comments) | That the user said a particular sentence in a session; the sentence itself may be a directive, not a proposition | see record | SRC-1, `templates/COMMENTS.md` | Verbatim recording preserves attribution if followed, not the truth of user assertions. |
| [EPI-OBJ-session-log](#epi-obj-session-log) | What occurred, what was completed, errors and fixes | see record | SRC-1, `templates/SESSION_LOG.md` | Model recollection/compression; no actual entry checked. |
| [EPI-OBJ-resume-state](#epi-obj-resume-state) | Current approach, in-flight work and next micro-step; clean/unclean marker | see record | SRC-1, `templates/RESUME_STATE.md` | A clean marker is a procedure result, not proof all work is preserved. |
| [EPI-OBJ-task-registry](#epi-obj-task-registry) | Task provenance, status, files and approach | see record | SRC-1, `templates/TASK_REGISTRY.md` | Done status is deliberately not feature QA. |
| [EPI-OBJ-decisions](#epi-obj-decisions) | Rationale and source assertions; choices/categories also grant policy authority | see record | SRC-1, `templates/DECISIONS.md` | Binding force is independent of whether the rationale is true. |
| [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour) | Scoped failure, workaround and optional root-cause explanation | see record | SRC-1, `templates/LEARNED_BEHAVIOUR.md` | Ordinary save can admit entries without the lesson approval path. |
| [EPI-OBJ-feature-list](#epi-obj-feature-list) | A named feature passed human end-to-end verification, or has a reported failing case | see record | SRC-1, `templates/FEATURE_LIST.json` | No environment, test protocol or observed user judgment supplied. |
| [EPI-OBJ-sidecar-index](#epi-obj-sidecar-index) | What a numbered code block does and when its description was edited | see record | SRC-1, `.claude/commands/itemise.md` | Symbolic number parity cannot warrant natural-language meaning. |
| [EPI-OBJ-helper-library](#epi-obj-helper-library) | None inherent in executable behavior; associated assumptions/specifications may be truth-apt | see record | SRC-1, `.claude/commands/lessons.md` | No generated code supplied; whether a helper formally encodes a proposition is not determinable. |
| [EPI-OBJ-audit-report](#epi-obj-audit-report) | Detected consistency defects, passing checks and proposed fixes | see record | SRC-1, `.claude/commands/audit.md` | Report is retained diagnosis, not a independently validated account. |
| [RT-OBJ-claude](runtime.md#rt-obj-claude) | Principally policy; some factual assumptions about host behavior and recovery | see record | SRC-1, `templates/CLAUDE.md` | Host delivery and conflicting instructions remain limits. |
| [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) | Not determinable from accessible numerical state | see record | SRC-1, `README.md` | Version/fixity/mutable endpoint and hidden reasoning uninspected; no inference of absent learning. |

## Authority-route ledger

Rows split consequential functions even where one supplied route is their valid container. Generic progression, return, read-back, selectors, expiry and evidence limits are `see` the declaring record. All prompt-directed rows are **doctrine only**: host execution of Bash instructions is requested, not inspected package automation. **Implemented** applies only to inspected shell logic. No row claims observed operation. `None` in epistemic license means the route itself licenses no new truth claim, not that its inputs must be false.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-start-session](runtime.md#rt-rte-start-session) | content transformation | doctrine only | [EPI-OBJ-comments](#epi-obj-comments), [RT-OBJ-claude](runtime.md#rt-obj-claude) | truth-apt transformation: acquisition/import | User details and custom/existing project records enter model context | see record | see record | Requested reads and user details; source warrant unknown | see record | Attribution can be preserved; endorsement not established | Setup and recovery context made available | see record and [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) | SRC-1, `.claude/commands/start.md` | [EPI-CLM-context-economy](#epi-clm-context-economy) | Partial loading is not full-context warrant | No authentic consumer data supplied |
| [RT-RTE-save-session](runtime.md#rt-rte-save-session) | content transformation | doctrine only | [EPI-OBJ-session-log](#epi-obj-session-log), [EPI-OBJ-resume-state](#epi-obj-resume-state), [EPI-OBJ-task-registry](#epi-obj-task-registry), [EPI-OBJ-decisions](#epi-obj-decisions), [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour) | truth-apt transformation: indeterminate | Conversation/events become summaries, rationale and causal explanations | see record | see record | Requested entries; no populated instance | see record | Summary fidelity and entailment unestablished; root-cause text can add hypotheses | Entries guide later work before distinct factual acceptance | see record and [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) | SRC-1, `.claude/commands/save.md` | none | None; retention is not acceptance | Need inputs and authored entries to classify individual edges |
| [RT-RTE-save-session](runtime.md#rt-rte-save-session) | check/evidence production | doctrine only | [EPI-OBJ-comments](#epi-obj-comments), [EPI-OBJ-task-registry](#epi-obj-task-registry), [EPI-OBJ-decisions](#epi-obj-decisions), [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour) | no content change | Missing entries and trigger coverage | Foreground model reviews conversation and named checklists; bookkeeping domain | see record | Requested completeness checklist or return to updating | see record | Internal coverage evidence only; not independent factual testing | May delay Git step until each file addressed | Foreground model, checklist prompt, requested continuation gate, this save | SRC-1, `.claude/commands/save.md` | none | Self-check is not independent verification | Accurate conversation interpretation unobserved |
| [RT-RTE-save-session](runtime.md#rt-rte-save-session) | retention | doctrine only | [EPI-OBJ-comments](#epi-obj-comments), [EPI-OBJ-session-log](#epi-obj-session-log), [EPI-OBJ-resume-state](#epi-obj-resume-state), [EPI-OBJ-task-registry](#epi-obj-task-registry), [EPI-OBJ-decisions](#epi-obj-decisions), [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour) | no content change | File writes and optional explicit-path Git durability | see record | see record | Requested durable state; no observed write | see record | No additional warrant from persistence | Later sessions can select retained state | see record | SRC-1, `.claude/commands/save.md` | [RT-CLM-progress-protection](runtime.md#rt-clm-progress-protection) | Retention without acceptance | No multi-file transaction |
| [RT-RTE-save-session](runtime.md#rt-rte-save-session) | lineage/freshness/recovery | doctrine only | [EPI-OBJ-decisions](#epi-obj-decisions), [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour), [EPI-OBJ-task-registry](#epi-obj-task-registry) | truth-apt transformation: non-ampliative reshaping | Full bodies move intact; index titles/categories point to them | see record | see record | Requested rotation, supersession link, resolved LB marker or backlog disposition | see record | Archival preserves existing warrant at best, creates none | Active constraints remain binding; resolved entries need not be read; superseded decisions point to replacements | Later model, main indexes then archive body, requested policy, later sessions | SRC-1, `.claude/commands/end.md` | [EPI-CLM-archive-truth](#epi-clm-archive-truth), [EPI-CLM-context-economy](#epi-clm-context-economy) | Movement does not establish truth | Title relevance selection can omit a needed condition; template category conflict see runtime |
| [RT-RTE-start-session](runtime.md#rt-rte-start-session) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-resume-state](#epi-obj-resume-state), [EPI-OBJ-decisions](#epi-obj-decisions), [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour), [EPI-OBJ-feature-list](#epi-obj-feature-list), [EPI-OBJ-task-registry](#epi-obj-task-registry) | no content change | Handoff, pending tasks and relevant rules enter later work | see record | see record | Requested summary, retrieval and wait for user go-ahead | see record | Loaded data retain unknown original warrant; human continuation is not per-claim acceptance | Guides next task and forbids contradicting constraints | see record and [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) | SRC-1, `.claude/commands/start.md` | [EPI-CLM-context-economy](#epi-clm-context-economy), [EPI-CLM-archive-truth](#epi-clm-archive-truth) | Operational force without factual endorsement | Relevance and compliance are model judgments |
| [EPI-RTE-feature-check](#epi-rte-feature-check) | check/evidence production | doctrine only | [EPI-OBJ-feature-list](#epi-obj-feature-list) | no content change | Named user-facing feature works end-to-end | see record | see record | Human pass verification or broken-case report, not task completion | see record | Bounded user verification, not all-environment correctness | Supplies input to status admission | see record | SRC-1, `.claude/commands/save.md` | none | none | Verification scope/protocol not frozen |
| [EPI-RTE-feature-admission](#epi-rte-feature-admission) | disposition/acceptance | doctrine only | [EPI-OBJ-feature-list](#epi-obj-feature-list) | non-truth-apt policy/content update: QA status admission or withdrawal | Record pass only after human verification; reset on break report | see record | see record | Requested true or false flag with failure notes | see record | Criterion/intended use are end-to-end user QA tracking; actual accepted instance absent | Later model treats verified versus failing/untested features differently | see record | SRC-1, `.claude/commands/save.md` | none | Acceptance rule, not observed acceptance | User authority and file update remain requested |
| [EPI-RTE-lesson-inference](#epi-rte-lesson-inference) | content transformation | doctrine only | [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour), [EPI-OBJ-helper-library](#epi-obj-helper-library) | truth-apt transformation: indeterminate | Script edits become a challenged belief and classified lesson | see record | see record | Candidate FACT, HELPER, INSTRUMENT FAULT or JUDGEMENT | see record | A diff alone establishes changed text, not falsity, cause or transfer | Produces proposals, not authority to install yet | see record | SRC-1, `.claude/commands/lessons.md` | [EPI-CLM-diff-record](#epi-clm-diff-record) | Diff-as-falsification overstates evidence | Need script inputs, outcomes and candidate to decide entailment/non-entailment |
| [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons) | check/evidence production | doctrine only | [EPI-OBJ-helper-library](#epi-obj-helper-library) | no content change | Proposed helper rejects known-broken input and accepts known-good input | see record | see record | Requested two-way self-test proof summary | see record | Contrast licenses only tested cases with trustworthy case labels | Intended guard on installed helper quality | Foreground model, helper self-tests and report, requested protocol, harvest and future callers | SRC-1, `.claude/commands/lessons.md` | [EPI-CLM-helper-safety](#epi-clm-helper-safety) | Two cases do not prove universal safety | No tests/results; test is after approval/install, no explicit failed-test rollback |
| [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons) | disposition/acceptance | doctrine only | [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour), [EPI-OBJ-helper-library](#epi-obj-helper-library), [EPI-OBJ-decisions](#epi-obj-decisions) | no content change | User approves class/destination proposals before write, install or delete | see record | see record | Approved subset or no new lesson | see record | Human selection licenses installation, not a specified evidence-consuming truth criterion for every FACT/Why | Unapproved proposals cannot be installed by this prompt | see record | SRC-1, `.claude/commands/lessons.md` | [EPI-CLM-helper-safety](#epi-clm-helper-safety) | Approval is not universal epistemic acceptance | Human reasoning not supplied; no actual response |
| [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons) | retention | doctrine only | [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour), [EPI-OBJ-helper-library](#epi-obj-helper-library), [EPI-OBJ-decisions](#epi-obj-decisions) | no content change | Approved content installed before named scratch-script cleanup | see record | see record | Requested LB/helper/decision plus deletion/keep report | see record | Installed result does not gain warrant by replacing its evidence | Removes mined scripts; retains referenced and untracked/unmined files | see record | SRC-1, `.claude/commands/lessons.md` | [EPI-CLM-diff-record](#epi-clm-diff-record) | No mandatory retained input/outcome evidence bundle | Untracked mined evidence deletion may be irreversible |
| [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons) | behavior/policy adaptation | doctrine only | [EPI-OBJ-helper-library](#epi-obj-helper-library), [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour), [EPI-OBJ-decisions](#epi-obj-decisions) | non-truth-apt policy/content update: helper/constraint admission | Approved lesson becomes later guidance or exported executable guard | see record | see record | Requested installed helper, Enforced by link or decision | see record | Helper behavior and linked prose have different licenses; no inherent proposition identified in absent code | Can constrain future callers or later agents | see record and [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) | SRC-1, `.claude/commands/lessons.md` | [EPI-CLM-helper-safety](#epi-clm-helper-safety) | Export is not future call integration | Consumer use and improved action unobserved |
| [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code) | content transformation | doctrine only | [EPI-OBJ-sidecar-index](#epi-obj-sidecar-index) | truth-apt transformation: indeterminate | Code body becomes a job description or calls annotation; long units left blank | see record | see record | Requested new descriptions; existing descriptions preserved verbatim | see record | Semantic interpretation not automatically checked; particular descriptions might be faithful reshaping or new claims | Descriptions steer later code selection | see record | SRC-1, `.claude/commands/itemise.md` | [EPI-CLM-context-economy](#epi-clm-context-economy) | Not a semantic proof | Need generated description/body pair; dates/number parity cannot decide truth |
| [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code) | check/evidence production | doctrine only | [EPI-OBJ-sidecar-index](#epi-obj-sidecar-index) | no content change | Source marker numbers equal sidecar row numbers; each label lands on one job | see record | see record | Requested parity pass/fail and model granularity self-check | see record | Set equality licenses identifier coverage only, not description fidelity, order or granularity | Parity failure delays completion; granularity asks for subdivision | see record | SRC-1, `.claude/commands/itemise.md` | [EPI-CLM-itemise-preservation](#epi-clm-itemise-preservation) | Different checks cover different properties | All checks are prompt operations, no execution supplied |
| [EPI-RTE-itemise-filter](#epi-rte-itemise-filter) | check/evidence production | doctrine only | [EPI-OBJ-sidecar-index](#epi-obj-sidecar-index) | non-truth-apt policy/content update: comparison-stream normalization | Comparison inputs normalized by marker filtering and CR deletion | see record | see record | No-output diff or difference; concrete false-negative below | see record | Equality in the filter's quotient, not byte or semantic equality | Supplies pass/fail to backup disposition | see record | SRC-1, `.claude/commands/itemise.md` | [EPI-CLM-itemise-preservation](#epi-clm-itemise-preservation) | Filter can hide executable string content | Command is embedded doctrine, not an automatic installed checker |
| [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code) | disposition/acceptance | doctrine only | [EPI-OBJ-sidecar-index](#epi-obj-sidecar-index) | no content change | Complete parity and normalized diff license completion; diff failure restores source | see record | see record | Requested success, backup deletion or restored source | see record | Operational acceptance for labeling; cannot warrant all-code preservation | Keeps successful edits, restores failed source, ends backup recovery | see record | SRC-1, `.claude/commands/itemise.md` | [EPI-CLM-itemise-preservation](#epi-clm-itemise-preservation) | Sidecar rollback not paired explicitly | False pass can discard recovery copy |
| [RT-RTE-audit-project](runtime.md#rt-rte-audit-project) | check/evidence production | doctrine only | [EPI-OBJ-audit-report](#epi-obj-audit-report), [EPI-OBJ-sidecar-index](#epi-obj-sidecar-index), [EPI-OBJ-decisions](#epi-obj-decisions), [EPI-OBJ-task-registry](#epi-obj-task-registry) | truth-apt transformation: indeterminate | Task provenance, archive pointer/ID consistency, contradictions, Git state, dates and parity | see record | see record | Requested severity-tagged findings and passing checks | see record | Internal consistency/mtime evidence, not external truth or feature correctness; contradiction diagnoses require model interpretation | Surfaces issues; does not auto-rewrite descriptions | see record | SRC-1, `.claude/commands/audit.md` | [EPI-CLM-archive-truth](#epi-clm-archive-truth) | Resume warning conflicts with normal save behavior, see runtime | No audit accuracy evidence; date mismatch is only a hint |
| [RT-RTE-audit-project](runtime.md#rt-rte-audit-project) | disposition/acceptance | doctrine only | [EPI-OBJ-audit-report](#epi-obj-audit-report), [EPI-OBJ-sidecar-index](#epi-obj-sidecar-index) | non-truth-apt policy/content update: admit user-selected repairs | User chooses each issue to fix or ignore | see record | see record | Requested selected repairs only; ignored issues not failures | see record | User permission, not automatically a truth judgment on diagnosis | Permits chosen fixes, withholds unchosen ones | see record | SRC-1, `.claude/commands/audit.md` | none | Ignored diagnosis remains without repair | Rollback/recheck not specified |
| [RT-RTE-audit-project](runtime.md#rt-rte-audit-project) | retention | doctrine only | [EPI-OBJ-audit-report](#epi-obj-audit-report) | no content change | Displayed report saved to timestamped file | see record | see record | Requested durable audit | see record | Retention adds no independent warrant | Latest audit may guide a later agent via template | see record and [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) | SRC-1, `.claude/commands/audit.md` | none | Report persistence is not lifecycle integration of accepted claims | Startup command lacks explicit latest-audit read |
| [RT-RTE-commit-reminder](runtime.md#rt-rte-commit-reminder) | operational admission/selection/consumption | implemented | [RT-OBJ-settings](runtime.md#rt-obj-settings) | non-truth-apt policy/content update: per-event reminder | Raw Bash payload contains git commit | see record | see record | Checklist and unconditional zero exit | see record | None; no completeness evidence produced | Commit allowed whether records updated or not | see record | SRC-1, `.claude/hooks/pre-commit-check.sh` | none | Not a verifying or enforcing gate | Host/settings activation unobserved |
| [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup) | lineage/freshness/recovery | implemented | [EPI-OBJ-session-log](#epi-obj-session-log), [EPI-OBJ-task-registry](#epi-obj-task-registry), [EPI-OBJ-comments](#epi-obj-comments), [EPI-OBJ-decisions](#epi-obj-decisions), [EPI-OBJ-feature-list](#epi-obj-feature-list) | no content change | Copy existing five root files to timestamped directory | see record | see record | Attempted copies and count; no restore consumer | see record | Byte-copy intent preserves existing content, not unsaved progress or warrant | Provides recovery affordance, never blocks compaction | see record | SRC-1, `.claude/hooks/pre-compact-save.sh` | [RT-CLM-progress-protection](runtime.md#rt-clm-progress-protection) | Five-file/stale-state counterexample to all progress | Unchecked copy failure can still increment count |

No lifecycle-integration row is established for accepted ampliative factual claims in these inspected paths. `/lessons` does connect approved entries to helpers and decisions, but its generic human permission rule does not specify evidence-consuming factual acceptance; ordinary save admits LB prose without that gate. Feature QA specifies a criterion, but tracking that result is not by itself explanatory integration. This bounded finding leaves open what an actual consumer might do; it does not convert missing deployments into an absence of checking.

## System-claim versus route comparison

The claims and their source passages are `see` the cited claim records. There is no supplied observed-run or causal-experiment support for any row.

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-progress-protection](runtime.md#rt-clm-progress-protection) | see record | SRC-1, `README.md`; doctrine/design | Incremental logging, checkpoint and backup policy | [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup) | Uninspected | No intervention/comparison; stale/omitted state cannot be copied | Narrow backup mechanism plus requested maintenance | All-progress/no-loss exceeds file coverage and unchecked copy result |
| [EPI-CLM-diff-record](#epi-clm-diff-record) | see record | SRC-1, `.claude/commands/lessons.md`; doctrine/design | Classifies changed beliefs, including instrument faults; excludes cosmetics | None; [EPI-RTE-lesson-inference](#epi-rte-lesson-inference) is doctrine only | Uninspected | No inputs/outcomes or attribution of edits | Useful candidate-mining instruction | Changed parameter may reflect changed requirements, not falsified belief |
| [EPI-CLM-helper-safety](#epi-clm-helper-safety) | see record | SRC-1, `.claude/commands/lessons.md`; doctrine/design | Prefer helpers, two-way tests, approval/install before cleanup | None; see [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons) | Uninspected | Two examples do not exhaust inputs; future caller may not use helper | Intended executable guard and linked warning | Universal impossibility/never-forgotten claims unsupported |
| [EPI-CLM-archive-truth](#epi-clm-archive-truth) | see record | SRC-1, `.claude/commands/end.md`; doctrine/design | Intact bodies, indexes, resolved and superseded markings | None; see [RT-RTE-save-session](runtime.md#rt-rte-save-session), [RT-RTE-audit-project](runtime.md#rt-rte-audit-project) | Uninspected | No archive integrity or recall experiment | Archiving is intended not to revoke active constraints | Continued policy force is supportable design; factual truth does not follow from movement |
| [EPI-CLM-itemise-preservation](#epi-clm-itemise-preservation) | see record | SRC-1, `.claude/commands/itemise.md`; doctrine/design | Insert-only instruction, backups, parity, granularity and filtered comparison | None; [EPI-RTE-itemise-filter](#epi-rte-itemise-filter) analyzes requested command | Uninspected | Concrete multiline-string countercase below; Edit can replace matched text | Requested restricted labeling with an operational restore path | Neither tool name nor normalized comparison proves every character/semantics preserved |
| [EPI-CLM-context-economy](#epi-clm-context-economy) | see record | SRC-1, `README.md`; doctrine/design | Last-five-session bodies, index scans, on-demand archive and code reads | None; see [RT-RTE-start-session](runtime.md#rt-rte-start-session), [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code) | Uninspected | Growing indexes/backlog, arbitrary body sizes/custom files, conflicting plan read; no token measurement | Intended selective access can avoid some full bodies | Predictable age-independent small cost, full recovery and measured savings not established |

## Bounded conclusion

**Records receive operational authority more readily than epistemic warrant.** `/save`, `/end` and incremental instructions retain conversation-derived status, summaries, decisions and gotchas. Comments are requested verbatim imports: that preserves attribution, not the truth of their propositions. Other outputs require interpretation; without input/output pairs, non-ampliative summary, derivation and conjecture cannot be distinguished claim by claim. Scoped root-cause and workaround fields can host criticizable content, but neither formatting nor retention supplies truth acceptance. See [RT-RTE-save-session](runtime.md#rt-rte-save-session), [EPI-OBJ-comments](#epi-obj-comments), [EPI-OBJ-learned-behaviour](#epi-obj-learned-behaviour).

**Two admission regimes must not be collapsed.** Feature QA names a human end-to-end criterion, an intended use (QA tracking), and a withdrawal input (reported breakage). It can license a bounded pass record if followed; no actual accepted instance or protocol-wide correctness is evidenced. `/lessons` instead asks permission to install proposals, while helper tests check two labeled cases after approval/install. That is a real requested check, not an absent evaluator, but it does not license every FACT or causal Why. Ordinary gotcha logging bypasses lesson approval. See [EPI-RTE-feature-check](#epi-rte-feature-check), [EPI-RTE-feature-admission](#epi-rte-feature-admission), [EPI-RTE-lesson-inference](#epi-rte-lesson-inference), [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons).

**The later authority paths are concrete but policy-level.** `/start` reloads main records and indexes, uses a handoff marker, and requests relevant full archive bodies at task time. Decision supersession changes the active rule; resolved LB markings reduce reading without destroying the original. Constraints and lessons influence a later model through file reads; helpers can enforce guards only at actual calls. Approval, exporting and loading do not establish content-dependent behavior or successful learning. The numerical host component's version, mutability and internal truth-apt state remain uninspected; opaque reasoning is not evidence for or against hidden checking. See [RT-BAP-project-rules](runtime.md#rt-bap-project-rules), [RT-RTE-start-session](runtime.md#rt-rte-start-session), [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code).

**Checks license their own domains.** Audit pointer/ID parity and code-marker parity assess internal consistency. Date comparison is expressly a stale-description hint, not a truth check. Contradiction/completeness checks are model interpretations with user-selected repairs. Filtered diff checks normalized text only; its false-negative witness prevents a universal preservation guarantee. The commit hook merely advises; the backup hook duplicates selected existing bytes without checking truth or restoreability. See [RT-RTE-audit-project](runtime.md#rt-rte-audit-project), [EPI-RTE-itemise-filter](#epi-rte-itemise-filter), [RT-RTE-commit-reminder](runtime.md#rt-rte-commit-reminder), [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup).

**Lesson theory properties remain separate.** The supplied theory account is see [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons): localized LB/helper candidates are afforded; content-dependent consumption, criticism and retained next-round influence are claimed, not observed. This analyst's diff countercase qualifies the evidence that would satisfy criticism, without negating the instruction to distinguish instrument faults. User approval limits autonomy of admission. Retained debug beliefs can represent consumer-agent operation, but actual bidirectional reflection, improved capacity and criticism of Context Guard's own method remain unestablished. The potential improvement objective is avoiding recurrent consumer debugging errors across sessions; proposals, installed guidance and later channels are intended links, while actual update attribution and subsequent change-dependent behavior are missing. No exercised self-improvement or successful improvement follows. These uncertainties coexist with the described retention and checking capacities; they do not yield a single system-wide epistemic score.

## Shared records

### Operative objects

These objects are distinct consumer artifacts, not additional declarations of [RT-OBJ-claude](runtime.md#rt-obj-claude) or [RT-OBJ-settings](runtime.md#rt-obj-settings). The closest supplied route container is cited per object; a route's description of its output is not a competing declaration of that output object. No supplied object counterpart was found after comparison. Generated objects are specified, not observed.

#### EPI-OBJ-comments
Label: Verbatim comments

Source-native identity: consumer `COMMENTS.md` and `COMMENTS_pageN.md`. Representational form: natural-language utterances plus textual timestamps/session attribution. Storage substrate: project files, optionally Git. Closest supplied record: [RT-RTE-save-session](runtime.md#rt-rte-save-session), which writes but is not this artifact. Intended later consumer: `/start` and `/audit`; actioned comments can move out of the main file. Evidence: SRC-1, `templates/COMMENTS.md`, `.claude/commands/end.md`.

> # Format: Timestamp | Session | Verbatim comment
> --- `templates/COMMENTS.md`

#### EPI-OBJ-session-log
Label: Session history

Source-native identity: consumer `SESSION_LOG.md` and its archive pages. Representational form: natural-language event summaries and status claims. Storage substrate: project files, optionally Git. Closest supplied record: [RT-RTE-save-session](runtime.md#rt-rte-save-session). Historical entries differ from replaceable current state below. Evidence: SRC-1, `templates/SESSION_LOG.md`, `.claude/commands/save.md`.

> # Format: Session ID | Date | Summary of work done | Tasks completed | Tasks remaining
> --- `templates/SESSION_LOG.md`

#### EPI-OBJ-resume-state
Label: Current in-flight state

Source-native identity: consumer `RESUME_STATE.md`. Representational form: natural-language handoff with a textual boolean marker interpreted by the model. Storage substrate: overwriteable project file, optionally Git. Closest supplied record: [RT-RTE-save-session](runtime.md#rt-rte-save-session); unlike historical entries, `/end` clears this object. Evidence: SRC-1, `templates/RESUME_STATE.md`, `.claude/commands/start.md`.

> # Overwritten by /save. Wiped by /end. Read first by /start.
> # This file holds ONLY current in-flight state, not history. History lives in SESSION_LOG.md.
> --- `templates/RESUME_STATE.md`

#### EPI-OBJ-task-registry
Label: Task provenance and status

Source-native identity: consumer `TASK_REGISTRY.md` and pages. Representational form: natural-language task/approach notes in a textual table with conventional IDs/status markers; host-model interpretation supplies consequences. Storage substrate: files, optionally Git. Closest supplied record: [RT-RTE-save-session](runtime.md#rt-rte-save-session). Task done is distinct from feature verified. Evidence: SRC-1, `templates/TASK_REGISTRY.md`, `.claude/commands/save.md`.

> # CHECK THIS FILE BEFORE CREATING NEW TASKS. DO NOT DUPLICATE
> --- `templates/TASK_REGISTRY.md`

> #   - On completion, amend with: `Files: path1, path2 | Approach: one-sentence pattern/library | Governed by: D-xx`
> --- `templates/TASK_REGISTRY.md`

#### EPI-OBJ-decisions
Label: Decisions and rationale

Source-native identity: consumer `DECISIONS.md` and pages/index. Representational form: natural-language choice/rationale/source and model-interpreted category/links. Storage substrate: files, optionally Git. Closest supplied record: [RT-RTE-save-session](runtime.md#rt-rte-save-session). Unlike [RT-OBJ-claude](runtime.md#rt-obj-claude), these are use-derived per-decision constraints, not the template that tells the agent to respect them. Evidence: SRC-1, `templates/DECISIONS.md`, `.claude/commands/end.md`.

> # **Decision:** [The choice that was made]
> # **Rationale:** [The reasoning that led to it]
> # **Source:** [User comment | Plan | Session | External requirement]
> --- `templates/DECISIONS.md`

> - If a new decision supersedes an earlier one, mark the old `Category: superseded` with a pointer to the new D-number.
> --- `.claude/commands/end.md`

#### EPI-OBJ-learned-behaviour
Label: Tactical knowledge entries

Source-native identity: consumer `LEARNED_BEHAVIOUR.md`, pages/index and optional helper references. Representational form: natural-language scoped failure/workaround/explanation; `resolved` is model-interpreted disposition text. Storage substrate: files, optionally Git. Closest supplied records: [RT-RTE-save-session](runtime.md#rt-rte-save-session) and [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons), two writers of the same object, not two object identities. No actual lesson examined. Evidence: SRC-1, `templates/LEARNED_BEHAVIOUR.md`, `.claude/commands/lessons.md`.

> **Context:** Where this surfaces (platform, plugin, version)
> **Gotcha:** What fails and how (symptom)
> **Workaround:** What actually works
> **Why:** Root cause if known
> --- `templates/LEARNED_BEHAVIOUR.md`

> 3. An entry whose underlying platform or library has been removed, or upgraded past the bug, can be marked `resolved` in the index, so it stays findable but no longer needs reading.
> --- `.claude/commands/end.md`

#### EPI-OBJ-feature-list
Label: Feature QA status

Source-native identity: consumer `FEATURE_LIST.json`, initialized with an empty features array. Representational form: symbolic JSON fields whose intended QA semantics require human/model interpretation; natural-language names/failure notes are separate claim content. Storage substrate: files, optionally Git. Closest supplied record: [RT-RTE-save-session](runtime.md#rt-rte-save-session). Truth-apt human-verification attribution is separate from operational pass classification. Evidence: SRC-1, `templates/FEATURE_LIST.json`, `.claude/commands/save.md`.

> "verifiedBy": "user | null",
> "verifiedAt": "YYYY-MM-DD | null",
> "notes": "Failing case description, linked task IDs, or empty string"
> --- `templates/FEATURE_LIST.json`

#### EPI-OBJ-sidecar-index
Label: Code sidecar descriptions

Source-native identity: generated `<source_filename>.index.md` paired with numbered source markers. Representational form: natural-language job descriptions plus symbolic section addresses and date strings; semantic selection by a model, marker matching by grep if executed. Storage substrate: project source/Markdown files, optionally Git. Closest supplied record: [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code). No generated sidecar supplied; descriptions do not have the same warrant as source code. Evidence: SRC-1, `.claude/commands/itemise.md`, `templates/CLAUDE.md`.

> 2. **If the section is fewer than 50 lines**, write a one-line description following the ruleset.
> 3. **If the section is 50 lines or longer**, leave the description as `_(blank, fill on first edit)_`. This is a **deliberate token-saving choice**: long sections need careful summarisation, and an inaccurate auto-generated description is worse than no description (it misleads agents and corrupts their model of the codebase). Calibration scaffolding is not authoritative, so let the next coding agent fill it in when they touch the section for the first time.
> --- `.claude/commands/itemise.md`

> 2. **Preserve every existing description verbatim.** Do not rewrite even if it doesn't match the auto-generated style. Hand-written descriptions are sacred and exist for a reason.
> --- `.claude/commands/itemise.md`

#### EPI-OBJ-helper-library
Label: Installed lesson helpers

Source-native identity: functions in a consumer project's helper library, exported by `/lessons`, optionally named by LB `Enforced by`. Representational form: symbolic executable code; associated explanatory prose belongs to the LB object. Storage substrate: consumer code files, optionally Git. Closest supplied record: [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons). No helper implementation available, so exact assumptions, consumer call paths and proposition encoding are not determinable. Evidence: SRC-1, `.claude/commands/lessons.md`.

> - **LEARNED_BEHAVIOUR entries**: standard format (`## LB-NNN: title (Session N, dd/mm/yy)` with Context / Gotcha / Workaround / Why). Where a helper now enforces the lesson, add an `**Enforced by:**` line naming it. That tells a future reader the rule is already load-bearing in code and does not depend on them remembering it.
> --- `.claude/commands/lessons.md`

The supplied [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons) retains the helper export/two-way self-test passage. That instruction does not itself show the helper is called.

#### EPI-OBJ-audit-report
Label: Persistent integrity diagnosis

Source-native identity: generated `audits/YYYY-MM-DD_HHMMSS.md`. Representational form: natural-language issue/severity/details/fix and passing checks. Storage substrate: project Markdown file. Closest supplied record: [RT-RTE-audit-project](runtime.md#rt-rte-audit-project). Report creation precedes selected repairs; retained diagnosis is not proof fixes succeeded. Evidence: SRC-1, `.claude/commands/audit.md`, `templates/CLAUDE.md`.

> Save the full audit report (exactly as displayed above) to:
> `audits/YYYY-MM-DD_HHMMSS.md`
> --- `.claude/commands/audit.md`

### Routes

#### EPI-RTE-feature-check
Label: Human end-to-end feature check
Part of: [RT-RTE-save-session](runtime.md#rt-rte-save-session)

Endpoints/progression/owner: user tests a named feature end-to-end or reports a broken case → foreground model obtains that report → QA admission consumes it. This is the evaluation part of the supplied save/end route, not its file update. Context: user-facing feature under the user's actual test conditions, unspecified in the package. Evaluator and answer reference: human expected end-to-end behavior; the package freezes neither an oracle nor test suite. User supplies judgment, model is recorder; model task-completion status cannot substitute. Operating mode: open project QA, triggered by human verification or a broken report, not a controlled experiment.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: user verification or failing-case report, if supplied.
- Later read-back: inapplicable — this part produces the judgment; status retention and later reads belong to admission and the parent route.
- Delegated visibility: inapplicable — no separate worker specified for human verification.
- Selection predicate: a named feature manually verified end-to-end or reported broken by the user.
- Invalidation or expiry: later broken report can defeat the recorded positive result; no version/environment expiry prescribed.
- Activation or effect: requested judgment becomes input to QA status update, not an automatic product pass.
- Evidence limits: no human test transcript, feature implementation, environment or result supplied.

Evidence: SRC-1, `.claude/commands/save.md`; the load-bearing human-verification passage is see [RT-RTE-save-session](runtime.md#rt-rte-save-session). Distinct from admission: this part assesses behavior; admission authorizes the record change.

#### EPI-RTE-feature-admission
Label: Admit or withdraw feature status
Part of: [RT-RTE-save-session](runtime.md#rt-rte-save-session)

Endpoints/progression/owner: human verification/break report → foreground model evaluates the admission trigger → changes `passes` and failure notes → later `/start` QA summary. Proposed change: bounded status claim, not task completion. Human controls the qualifying evidence and can withhold it; model performs the update. Criterion: user manually verified end-to-end success; intended use and scope: the project's QA tracker for that feature, not universal correctness. A broken report withdraws positive reliance. Operating mode: open QA tracking; reference outcome is the human check above. Guidance is the FEATURE_LIST semantic rule. Recovery: later reports can reverse status; no automatic code rollback is specified. Parent route supplies durability, not independent validation.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested true/false status and failing-case notes.
- Later read-back: QA status reaches later `/start` and model summaries through FEATURE_LIST.
- Delegated visibility: uninspected — no host propagation of QA status to other agents supplied.
- Selection predicate: human verification permits true; human break report requires false; task completion alone is insufficient.
- Invalidation or expiry: later break report resets status; no automatic expiry on code change specified.
- Activation or effect: requested status-dependent later QA interpretation; actual changed reliance unobserved.
- Evidence limits: no recorded acceptance instance or downstream behavior supplied; verifiedBy/verifiedAt are template fields, not enforced provenance.

Evidence: SRC-1, `.claude/commands/save.md`, `templates/FEATURE_LIST.json`. Separate from [EPI-RTE-feature-check](#epi-rte-feature-check): admission changes the status artifact, not the test outcome.

> - If the user reports a feature broken, flip `passes: false` with a `notes` description of the failing case.
> --- `.claude/commands/save.md`

#### EPI-RTE-lesson-inference
Label: Infer lessons from script changes
Part of: [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons)

Endpoints/progression/owner: foreground model selects current-session script series → consecutive diffs → interprets a prior belief and its alleged failure → deduplicates/classifies → presents proposals to human. Context includes existing LB/decision indexes and helper library. This part produces the candidate, unlike the parent's approval/install/check/cleanup stages. Proposed change: scoped FACT, HELPER, INSTRUMENT FAULT or JUDGEMENT. Model proposes and classifies; human can veto the later installation. Operating mode: open debugging harvest, no frozen expected-answer oracle. Static guidance prefers helpers, ignores cosmetic changes and treats check failure separately from product failure. What persists, if approved: Context/Gotcha/Workaround/Why, helper links/code and constraint rationale; input/outcome traces need not survive script deletion. Rollback/recovery: no candidate rollback needed before approval; parent's Git/cleanup limits apply after installation.

The content/update relation is indeterminate without actual scripts/outcomes and authored lesson. A changed selector can correct a mistaken assumption, reflect changed requirements, or simply target another page. This source-supported alternative prevents treating every diff as an entailed falsification. The prompt's own cosmetic exclusion and INSTRUMENT FAULT category confirm that changed text does not uniquely identify the blame target. No actual ampliative accepted claim is evidenced.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: proposed classified lessons or nothing-new result.
- Later read-back: inapplicable — proposals alone are not retained by this part; approved outputs reach later consumers through the parent.
- Delegated visibility: inapplicable — foreground harvest has no delegated mining step.
- Selection predicate: session prefix/mtime, name-stem series, changed substantive selectors/waits/endpoints/guards, novelty against existing knowledge.
- Invalidation or expiry: duplicate/cosmetic candidates rejected; user may reject before writes; no retained proposal expiry specified.
- Activation or effect: requested proposal generation, no installation authority until parent approval.
- Evidence limits: no actual series, outcomes or lesson instance; diff is not a test result or causal contrast.

Evidence: SRC-1, `.claude/commands/lessons.md`. Theory account and theory-builder conditions 1–4 are see [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons), the containing route: this inference part applies its static criticism guidance but supplies no separately observed formulation, consumption, criticism or iteration. Addressability is afforded by localized LB fields/helper functions; persistence and improved future capacity remain unobserved. learning: uninspected — no improvement/attribution evidence. Reflection is afforded for consumer debug beliefs, with actual two causal directions unobserved. Human approval is outside this inference part but remains inside the complete admission route, so it does not establish an autonomous theory builder. No criticism-fed revision of the shipped harvest method is shown. The complete route's dispositional self-change assessment is not upgraded by this candidate-generation part.

Theory-builder conditions 1–4 for this part:
- condition 1 conclusion status: afforded

The requested whole LB/helper proposal can localize a claim; no actual formulation supplied.

- condition 2 conclusion status: claimed

Classification is requested to depend on candidate content; no decision trace supplied.

- condition 3 conclusion status: claimed

The prompt asks for the challenged belief and separates instrument fault; diff alone does not establish that the criticism occurred or was warranted.

- condition 4 conclusion status: claimed

The parent requests installation for later use; this candidate-generation part alone supplies no next-round evidence.

> For each consecutive pair of files in a series, answer one question: **what did the agent believe in file N that turned out to be wrong in file N+1?**
> --- `.claude/commands/lessons.md`

> Look for a changed selector, wait condition, endpoint, parameter name, assertion, path, encoding, or a guard that suddenly appeared. Ignore cosmetic churn: renamed variables and reformatting are not lessons.
> --- `.claude/commands/lessons.md`

> | **INSTRUMENT FAULT** | a LEARNED_BEHAVIOUR entry, flagged as such | the *check* was wrong while the thing being checked was fine |
> --- `.claude/commands/lessons.md`

#### EPI-RTE-itemise-filter
Label: Normalized itemisation comparison
Part of: [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)

Endpoints/progression/owner: foreground model is told to run Bash → both source/backup streams pass through grep exclusion and CR deletion → `diff -B` emits differences or no output → parent keeps edits/deletes backups or restores. This is the comparison part, not the parent's marker generation/parity or disposition. Evaluator: deterministic text filter and diff, if executed. Target/domain: normalized line equality after removing regex-matching lines, carriage returns and blank-only differences. Oracle: backup under the same normalization. Operating mode: bounded labeling check; model invokes/interprets, program compares, human approved scope earlier. The producing command is inspected as embedded doctrine; it is not installed executable enforcement and was not run here.

Concrete deduction from the inspected expression, not target execution: take a Python file with the three lines `s = """`, `# 1. alpha`, `"""`. Change only the middle line to `# 1. beta`. That middle line is string data, not a Python comment, yet both lines match the stated regex and are removed by `grep -Ev`. The two normalized streams both consist of the unchanged opening and closing string lines; CR deletion and `diff -B` cannot distinguish them. The requested no-output branch labels this PASS although the value of `s` changed. Marker syntax therefore does not identify comments in a language-aware domain. Independently, `tr -d '\r'` removes all CR bytes, not only CRLF endings. These source-level deductions qualify universal source-preservation warrant, without asserting a real corrupted file.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested diff output or no output, consumed as FAIL/PASS.
- Later read-back: inapplicable — comparison streams are current-operation inputs, not accumulated memory; parent keeps source/sidecar edits.
- Delegated visibility: uninspected — foreground is to verify a worker's edits, but actual worker/result handling is not supplied.
- Selection predicate: each approved itemised source and its pre-edit backup; both use identical filter.
- Invalidation or expiry: backup deletion on completion ends immediate comparison/recovery reference; re-itemisation makes a new backup.
- Activation or effect: intended completion/restoration decision in the parent, not independently observed force.
- Evidence limits: no command run; filter equality licenses only its quotient, not semantic or byte preservation; error-status handling is not prescribed by the output-only branch.

Evidence: SRC-1, `.claude/commands/itemise.md`. No theory is formulated by this deterministic comparison part. Normalization rearranges/removes comparison representation without deriving a new factual code claim; the semantic inference from no diff to no code change is not warranted across the advertised language domain.

> PATTERN="^\s*(\/\/|#|/\*|<!--|--)\s+([0-9]+(\.[0-9]+)*(\s|\.)|end of\s+[0-9]+)"
> diff -B <(grep -Ev "$PATTERN" "{filename}" | tr -d '\r') <(grep -Ev "$PATTERN" "{filename}.itemise-backup" | tr -d '\r')
> --- `.claude/commands/itemise.md`

> - If `diff` produces no output: **PASS**, only comment lines (and cosmetic blank lines) were added
> - If `diff` produces output: **FAIL**, actual code was changed
> --- `.claude/commands/itemise.md`

### Claims

Each new claim has a distinct public/design assertion from [RT-CLM-progress-protection](runtime.md#rt-clm-progress-protection), whose backup/recovery referent is unchanged. These claims concern inference, helper universality, archive truth, preservation checking and context cost respectively; none supersedes the supplied record.

#### EPI-CLM-diff-record
Label: Script diff records false belief

Claimed operation: consecutive script differences are a literal record of an agent belief that proved false and can be mined into permanent lessons. Source: SRC-1, `.claude/commands/lessons.md`, `README.md`; doctrine/design. The diff itself lacks outcome/blame identification; changed needs and cosmetics are alternatives. Design conclusion status: claimed. Operation conclusion status: uninspected.

> **The diff between consecutive versions of a throwaway script is a literal record of what the agent believed that turned out to be false.**
> --- `.claude/commands/lessons.md`

#### EPI-CLM-helper-safety
Label: Helper prevents wrong answer

Claimed operation/warrant: a helper can make wrong answers impossible and avoid the failure of remembered prose. Source: SRC-1, `.claude/commands/lessons.md`; doctrine/design. Two-way testing and user approval support a narrower intended guard, not universal correctness or inevitable future calls. Design conclusion status: claimed. Benefit conclusion status: uninspected.

> **The governing principle: prefer a helper over prose.** A rule that must be remembered fails. A helper function that gets called, and a LEARNED_BEHAVIOUR entry that a future `/start` surfaces, do not. When a lesson can be expressed as code that makes the wrong answer impossible, write the code. A prose note saying "remember to escape the path" decays, a `safePath()` that escapes it cannot be forgotten.
> --- `.claude/commands/lessons.md`

#### EPI-CLM-archive-truth
Label: Archived lesson remains true

Claimed warrant: an archived learned behaviour is still true; archived active decisions still govern. Source: SRC-1, `.claude/commands/end.md`; doctrine/design. Normative continuation differs from factual validity. Resolved markers and intact relocation can preserve available content but do not test its premises. Design conclusion status: claimed. Operation conclusion status: uninspected.

> An archived learned behaviour is still true. The index line is what stops a future session re-discovering it the hard way.
> --- `.claude/commands/end.md`

> **Archiving does not revoke a decision.** `forever-active` and `active-constraint` decisions govern from the archive exactly as they did from the main file, and the index is how future sessions find them.
> --- `.claude/commands/end.md`

#### EPI-CLM-itemise-preservation
Label: Itemisation preserves existing source

Claimed operation/warrant: labeling adds comments without changing source; Edit structurally prevents loss and the verification check catches any character change. Source: SRC-1, `.claude/commands/itemise.md`; doctrine/design, including attributed Session 1 operation rather than an acquired trace. No observed run/causal experiment supplied. The insert-only discipline is a real requested restriction; Edit's ability to replace `old_string` does not enforce inclusion of every old character, and the filter has a semantic false-negative witness. Design conclusion status: claimed. Operation conclusion status: uninspected.

> Removing, altering, or rewriting ANY existing character in the file, whether code or comment, is a catastrophic failure. The verification step (Step 5) will catch this, but the Edit-based approach prevents it structurally.
> --- `.claude/commands/itemise.md`

#### EPI-CLM-context-economy
Label: Small predictable recovery context

Claimed operation/warrant: recovery uses only five-session content at a predictable small token cost independent of project age; sidecar-guided code reads scope to relevant code. Source: SRC-1, `README.md`; doctrine/design. Variable-sized recent bodies and growing indexes/backlog prevent the stated fixed-cost implication. Sidecar guidance may reduce reads, not prove relevance/completeness or measured savings. Design conclusion status: claimed. Benefit conclusion status: uninspected.

> It reads the last five sessions' worth of content and nothing more: archives and plan files stay closed, so recovery costs a predictable, small number of tokens no matter how old the project is.
> --- `README.md`

> **Why this exists:** a number on its own (e.g. `2.1`) is a coordinate without a label. With the sidecar, an agent answering "where is the code that does X?" reads the small sidecar (cheap), picks the matching number, then greps the source for that number's start/end markers and reads only those bytes. Token usage scopes to exactly the relevant code instead of the whole file.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; the applicable project-file channel is see [RT-BAP-project-rules](runtime.md#rt-bap-project-rules), with per-route narrower consumers/force distinguished in the ledger.
