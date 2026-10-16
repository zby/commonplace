---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Sentry Skills epistemic routes: bounded checks, operational decisions and evidence-directed instruction revision."
run-id: AAS-2026-10-14-skills-2719567f917c-01
reviewed-boundary: d18b7aa8ba878354e5c348310230e652f7690f9c
---

# Sentry Skills epistemic report

## Source-and-claim boundary

The question is how this host-consumed package acquires truth-apt material, checks candidates, licenses reliance and changes later behavior. Scope, frozen identity, host exclusions and evidence layers: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). This is a complete artifact with a partial operational loop, not an enclosing runtime. No target execution was performed. Source text supports helper implementation and prescribed model/human behavior, not compliance or benefit.

The assessed families are PR evidence acquisition and repair, skill-format checks, maintainer adoption, instruction-evidence retention, skill security screening, reader testing and endpoint-schema comparison. The functionality-preservation claim is [RT-CLM-preserve-functionality](runtime.md#rt-clm-preserve-functionality); the security-screening claim added here is [EPI-CLM-skill-security](#epi-clm-skill-security). These are bounded warrant claims, not a claim to infallible system-wide knowledge production.

| Entry point or operation | Source path, SRC-1 | Coverage and prevented conclusion |
|---|---|---|
| Installation, host selection, metadata and permissions | `README.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.claude/settings.json` | Supplied [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption), not independent host inspection. Excluded host implementation prevents enforcement/activation conclusions. |
| PR fetch, repair, monitor, direct-gh fallback | `skills/iterate-pr/SKILL.md`, `skills/iterate-pr/scripts/fetch_pr_checks.py`, `skills/iterate-pr/scripts/fetch_pr_feedback.py`, `skills/iterate-pr/scripts/monitor_pr_checks.py` | Supplied [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration), [RT-RTE-check-monitor](runtime.md#rt-rte-check-monitor). Bounded source transformations, not observed service truth or complete feedback. |
| Reply CLI | `skills/iterate-pr/scripts/reply_to_thread.py` | Direct complete read; [EPI-RTE-thread-reply](#epi-rte-thread-reply). Transport success is distinct from truth of a repair claim. |
| Triage and simplifier alternatives | `skills/triage-frontend-issues/SKILL.md`, `skills/triage-frontend-issues/references/archive-criteria.md`, `skills/code-simplifier/SKILL.md`, `agents/code-simplifier.md` | Supplied [RT-RTE-issue-triage](runtime.md#rt-rte-issue-triage), [RT-RTE-code-refinement](runtime.md#rt-rte-code-refinement). Approval does not certify taxonomy judgments; semantic preservation unobserved. |
| Skill revision, evidence storage, validation | `skills/skill-writer/references/iteration-path.md`, `skills/skill-writer/references/iteration-evidence.md`, `skills/skill-writer/scripts/quick_validate.py` | Direct complete reads, alongside supplied [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision); [EPI-RTE-example-retention](#epi-rte-example-retention). |
| Maintainer judge/adoption | `skills/skill-writer/EVAL.md`, `skills/skill-writer/evals/scenarios/iteration-from-bad-output.json` | Direct complete reads; supplied [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval) covers config/small-inline. Other scenario bodies and PR-writer eval remain uninspected: no full evaluator-coverage verdict. |
| Security scanner CLI, model filter, Warden trigger | `skills/skill-scanner/scripts/scan_skill.py`, `skills/skill-scanner/SKILL.md`, `warden.toml` | Direct complete scanner/prompt/config reads; [EPI-RTE-pattern-scan](#epi-rte-pattern-scan), [EPI-RTE-security-disposition](#epi-rte-security-disposition). Warden executable and scanner reference leaves uninspected: no enforced security admission conclusion. |
| Document reader test and human fallback | `skills/doc-coauthoring/SKILL.md` | Direct lines 240–354, containing Stage 3 and final review; [EPI-RTE-reader-testing](#epi-rte-reader-testing). Earlier drafting phases and final tips uninspected: no complete document-generation account. |
| Schema versus live endpoint | `skills/document-api-endpoint/SKILL.md` | Direct complete read; [EPI-RTE-endpoint-check](#epi-rte-endpoint-check). External source code/service not captured: actual schema fidelity unobserved. |
| Other shipped entry points | `skills/`, `agents/senpai.md` | Script/SKILL file inventory plus bounded search of scanner, document, work-summary, find-bugs, security-review and senpai for verification/evidence terms. Senpai research policy, security confidence policy and other leaf routes remain unassessed here. This prevents a system-complete negative about knowledge acquisition, checks or acceptance. |
| Other helper CLI | `skills/gh-review-requests/scripts/fetch_review_requests.py` | Inventoried, uninspected; cannot characterize its selection/warrant preservation. |

Every newly inspected file is at the registered SRC-1 revision. Supplied runtime findings remain provisional but no necessary supersession was found. The added scanner and reply routes extend coverage rather than replacing the valid runtime containers. Accessible model weights, exact foreground versions and mutable endpoint resolution remain outside evidence; see [RT-CMP-host-model](runtime.md#rt-cmp-host-model). Missing traces prevent observations of accepted claims, actual retention/read-back, deployed authority and learning. Missing interventions prevent causal attribution to individual prompt rules, helpers or judges.

## Epistemic-object inventory

Local O-labels identify candidate classes, not additional shared records.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md) | Domain assertions mixed with non-truth-apt workflow policies | see cited record | SRC-1, `skills/skill-writer/SKILL.md` | Natural-language and host-parsed parts differ; storage licenses neither truth nor compliance. |
| O-pr-results | Received check states, log excerpts, reviewer allegations and summaries | see [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration) | SRC-1, `skills/iterate-pr/scripts/fetch_pr_feedback.py` | Acquisition with bounded omissions; summaries cannot license complete feedback coverage. |
| O-monitor-marker | Proposition about received buckets, not complete CI success | see [RT-RTE-check-monitor](runtime.md#rt-rte-check-monitor) | SRC-1, `skills/iterate-pr/scripts/monitor_pr_checks.py` | Symbolic output over external inputs; unknown/skipped states weaken ordinary reading of success. |
| O-validation | Skill-format validity relative to coded predicates | see [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision) | SRC-1, `skills/skill-writer/scripts/quick_validate.py` | Structural JSON result, not semantic validation. |
| O-eval | Judge scores, artifacts, transcript and baseline comparison | see [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval) | SRC-1, `skills/skill-writer/EVAL.md` | Declared products, no actual result provided; model scores are not an answer oracle. |
| [EPI-OBJ-evidence-files](#epi-obj-evidence-files) | Expected/observed behavior, suspected causes, instruction deltas | see cited record | SRC-1, `skills/skill-writer/references/iteration-evidence.md` | Natural-language records on filesystem/Git; provenance is requested, not authenticated. |
| [EPI-OBJ-scan-findings](#epi-obj-scan-findings) | Pattern matches, locations, severities, URL labels | see cited record | SRC-1, `skills/skill-scanner/scripts/scan_skill.py` | Symbolic JSON carries bounded observations plus risk heuristics. |
| O-security-report | Malicious-intent judgment, risk and installation recommendation | see [EPI-RTE-security-disposition](#epi-rte-security-disposition) | SRC-1, `skills/skill-scanner/SKILL.md` | Natural-language assessment; intent judgments not entailed by regex matches. |
| O-document | Document assertions and fresh-reader answers | see [EPI-RTE-reader-testing](#epi-rte-reader-testing) | SRC-1, `skills/doc-coauthoring/SKILL.md` | Correct reader response need not establish real-world truth of document. |
| O-schema | TypedDict/decorator assertions about response keys, types and optionality | see [EPI-RTE-endpoint-check](#epi-rte-endpoint-check) | SRC-1, `skills/document-api-endpoint/SKILL.md` | Code and measured response are requested comparators; no such results supplied. |
| O-reply | Caller-provided assertion such as a fix report | see [EPI-RTE-thread-reply](#epi-rte-thread-reply) | SRC-1, `skills/iterate-pr/scripts/reply_to_thread.py` | Published natural-language content; helper checks mutation response, not assertion truth. |
| O-triage | Noise-category and archive suitability judgment | see [RT-RTE-issue-triage](runtime.md#rt-rte-issue-triage) | SRC-1, `skills/triage-frontend-issues/SKILL.md` | Model classification and human authorization are distinct from correctness. |

## Authority-route ledger

The ledger splits checks from dispositions and retention from integration. Field values owned by shared records are referenced rather than restated. Status describes architecture at the inspected package boundary; a doctrine-only model procedure can use an implemented helper.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration) | content transformation | implemented | O-pr-results | truth-apt transformation: acquisition/import | Received service content; see record | External gh/GitHub outputs, not independently authenticated | see record | see record | JSON delivered to host | Source warrant unknown; bounded lineage retained, completeness degraded | Inputs can redirect diagnosis; not repair approval | see [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | SRC-1, `skills/iterate-pr/scripts/fetch_pr_feedback.py` | none | none | Limited pagination/filtering; direct CLI alternative. |
| [RT-RTE-check-monitor](runtime.md#rt-rte-check-monitor) | check/evidence production | implemented | O-monitor-marker | truth-apt transformation: entailed derivation | Received pending/fail buckets | Fixed bucket/regex logic; see record | see record | see record | Terminal marker, not merge gate | Entailed classification relative to received list; service truth remains a premise | Can signal host to continue, wait or diagnose | Host/optional monitor channel, advisory, current PR cycle; see record | SRC-1, `skills/iterate-pr/scripts/monitor_pr_checks.py` | none | Label stronger than checked predicate | Passing marker does not entail all checks passed or feedback clean. |
| [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration) | disposition/acceptance | doctrine only | Proposed repair | no content change | Suitability to push/stop | Local tests and feedback, user on escalation; see record | see record | see record | Instruction policy | Tested behavior only; no recorded accepted general root-cause claim | Push after local verification; stop/ask on specified conditions | see [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | SRC-1, `skills/iterate-pr/SKILL.md` | none | none | Operational success not causal diagnosis or transfer. |
| [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision) | check/evidence production | implemented | O-validation | truth-apt transformation: entailed derivation | SKILL.md structure and recognized local file references | Python/YAML/path predicates | see record | Valid/errors/warnings; see record | CLI result/exit code | Validity only relative to checked syntax, keys and files | Supports compliant author finishing validation; does not intercept commits | Author, stdout/exit status, advisory outside helper, current validation | SRC-1, `skills/skill-writer/scripts/quick_validate.py` | none | none | Size advisory; semantic correctness/security excluded from this check's license. |
| [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval) | check/evidence production | doctrine only | O-eval | truth-apt transformation: indeterminate | Generated artifacts/behavior versus scenario criteria | External model judge and manual rubric; see record | see record | see record | Configured checks; scoring execution external | Bounded scenario fit, not mechanism truth or universal generalization | Results inform adopt/revise/reject, do not install by themselves | see record | SRC-1, `skills/skill-writer/EVAL.md` | none | none | No observed comparisons; judge implementation uninspected. |
| [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval) | disposition/acceptance | doctrine only | Candidate skill-writer revision | no content change | Intended later skill-authoring use | Maintainer adoption gate, target improvement and holdout non-regression | see record | see record | Prescribed human decision, not automated transaction | Acceptance of revision for intended use if evidence consumed; no actual accepted ampliative claim evidenced | May adopt, revise or reject future instruction change | Maintainer, reports/rubric, permissive policy, later installed invocations | SRC-1, `skills/skill-writer/EVAL.md` | none | none | Missing deployment/read-back; scores alone do not satisfy gate. |
| [EPI-RTE-example-retention](#epi-rte-example-retention) | retention | doctrine only | [EPI-OBJ-evidence-files](#epi-obj-evidence-files) | truth-apt transformation: indeterminate | Summarized/redacted examples and interpreted findings | see record | see record | see record | see record | Retains candidates with requested provenance/origin tags, not endorsement | Makes examples available for later revision | see record | SRC-1, `skills/skill-writer/references/iteration-evidence.md` | none | none | Semantic preservation of redaction unknown; no acceptance established by storage. |
| [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision) | behavior/policy adaptation | doctrine only | Future SKILL.md/reference policy | non-truth-apt policy/content update: behavioral rules and trigger changes | Future instruction behavior | Replay/review and author judgment; see record | see record | see record | Model/human instruction-revision policy | Outcome evidence may shape rules; actual knowledge acceptance not implied | Later loaded guidance can change action selection | see [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | SRC-1, `skills/skill-writer/references/iteration-path.md` | none | none | Not observed learning; no causal attribution of improved capacity. |
| [EPI-RTE-pattern-scan](#epi-rte-pattern-scan) | check/evidence production | implemented | [EPI-OBJ-scan-findings](#epi-obj-scan-findings) | truth-apt transformation: entailed derivation | Pattern occurrence and structure under coded rules | see record | see record | see record | see record | Pattern occurrence only; severity labels have no independent security warrant | Provides investigation leads, no automatic install block | see record | SRC-1, `skills/skill-scanner/scripts/scan_skill.py` | [EPI-CLM-skill-security](#epi-clm-skill-security) | Pattern match is not malicious intent | Scope of derivation excludes semantic risk judgment; unread files may be skipped. |
| [EPI-RTE-security-disposition](#epi-rte-security-disposition) | disposition/acceptance | doctrine only | O-security-report | truth-apt transformation: indeterminate | Security allegation and install suitability | see record | see record | see record | see record | Context-evaluated assessment if performed; no recorded evidence-consuming acceptance | Advises installation/review and discards low-confidence allegations | see record | SRC-1, `skills/skill-scanner/SKILL.md` | [EPI-CLM-skill-security](#epi-clm-skill-security) | none | Non-entailment of a particular report not evidenced; model semantics opaque. |
| [RT-RTE-issue-triage](runtime.md#rt-rte-issue-triage) | operational admission/selection/consumption | doctrine only | O-triage | no content change | Displayed archive batch | User explicit approval; see record | see record | see record | Approval policy, not wrapper | Authorizes operation, does not prove noise classification | Archive only approved displayed items; no automatic reversal | see record | SRC-1, `skills/triage-frontend-issues/SKILL.md` | none | none | External service status can influence later queue selection without knowledge integration. |
| [EPI-RTE-reader-testing](#epi-rte-reader-testing) | check/evidence production | doctrine only | O-document | truth-apt transformation: indeterminate | Document readability, ambiguity and contradictions | see record | see record | see record | see record | Reader comprehensibility for selected questions; no factual certification | Failed comprehension routes back to refinement | see record | SRC-1, `skills/doc-coauthoring/SKILL.md` | none | none | Fresh-model agreement cannot certify external truth; human fact review remains distinct. |
| [EPI-RTE-reader-testing](#epi-rte-reader-testing) | disposition/acceptance | doctrine only | O-document | no content change | Readiness for intended readers | Author judges consistency of reader answers and unresolved gaps; user final quality review | After reader checks; see record | Ready or return to refinement; see record | Instruction policy, not publication enforcement | Acceptance for comprehension if checks consumed; factual truth remains separately reviewable | Allows finishing document or requires revisiting problematic sections | Author/user, reader summaries, permissive/advisory, current document | SRC-1, `skills/doc-coauthoring/SKILL.md` | none | none | No actual readiness decision supplied; user can request further review. |
| [EPI-RTE-endpoint-check](#epi-rte-endpoint-check) | check/evidence production | doctrine only | O-schema | no content change | Declared schema versus actual response | see record | see record | see record | see record | Response samples/source comparisons within inspected endpoint domain | Requests correcting types and validating before downstream regeneration | see record | SRC-1, `skills/document-api-endpoint/SKILL.md` | none | none | One request cannot establish all optional fields/configurations; no execution supplied. |
| [EPI-RTE-thread-reply](#epi-rte-thread-reply) | operational admission/selection/consumption | implemented | O-reply | truth-apt transformation: non-ampliative reshaping | Body publication and per-alias mutation result | see record | see record | see record | see record | Transport acknowledgement only, not truth/acceptance of body | Posts caller text through gh; status lets caller retry failures | see record | SRC-1, `skills/iterate-pr/scripts/reply_to_thread.py` | none | none | Newline conversion assumes caller encoding; no content evaluator. |

> Adopt a `skill-writer` change only when:
>
> 1. AXIS runs complete for the working set.
> 2. no critical dimension regresses on holdout cases.
> 3. at least one target dimension improves on the case that motivated the change.
> 4. structural validation passes for generated skills or the transcript explains a legitimate blocker.
> 5. runtime `SKILL.md` remains a router and does not link to eval files.
> 6. source and maintenance notes are updated only when the skill contract changes.
> --- `skills/skill-writer/EVAL.md`

No lifecycle-integration route is established by these checks alone. The example-promotion policy changes future behavior and organizes provenance, but neither stored examples nor installed rules establish that a truth-apt candidate was first accepted against a named criterion. This is a limitation of the assessed routes, not a complete-system absence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-preserve-functionality](runtime.md#rt-clm-preserve-functionality) | see record | SRC-1, `skills/code-simplifier/SKILL.md`, doctrine/design | see [RT-RTE-code-refinement](runtime.md#rt-rte-code-refinement) | No inspected semantic-equivalence checker; route is prescribed | None supplied | No experiment; requested preservation is not proof | Preservation policy exists on both entry forms | Actual preservation unknown. |
| [EPI-CLM-skill-security](#epi-clm-skill-security) | see record | SRC-1, `skills/skill-scanner/SKILL.md`, doctrine/design | Context/intent filter explicitly bounds raw matches | [EPI-RTE-pattern-scan](#epi-rte-pattern-scan); model disposition is doctrine only | None supplied | No detector accuracy or component intervention evidence | Mechanical leads plus prescribed semantic screening | Broad detection/adoption safety not established by JSON findings alone. |

Structural validation is expressly scoped, not a discovered claim to semantic proof: see [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision). Maintainer evaluation also explicitly separates scoring from adoption: see [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval). These source-supported qualifications defeat a stronger allegation that all checks purport to certify truth. Reader testing retains a separate final fact review, so its completion condition should not be read as factual validation.

## Bounded conclusion

Sentry Skills provides heterogeneous checks and decision policies. PR helpers acquire service reports with unknown source warrant and bounded coverage. The monitor derives a bucket classification, not a complete success claim. The validator derives structural validity, not semantic correctness. Scanner matching derives occurrence claims; it explicitly sends intent and false-positive evaluation to the agent. Neither terminal labels nor risk labels widen those check domains.

The instruction package prescribes evidence-responsive revision, retained examples with provenance, working/holdout replay and a maintainer adoption gate. The gate names intended use and criteria: future skill-authoring behavior, target improvement, critical holdout non-regression and structural validation. No actual acceptance decision, deployed update or read-back is supplied. Retention and policy adaptation therefore remain separate from acceptance and lifecycle integration. No particular produced accepted ampliative claim is established by the supplied evidence.

Reader testing licenses selected comprehension judgments and revision requests, not truth of the document. Endpoint checking requests concrete response/source comparisons and schema corrections; its license cannot exceed the tested response domain. Triage approval grants operational permission for a displayed batch, not epistemic endorsement. Reply helpers can publish an unchecked claim while accurately reporting a mutation acknowledgement. These differing authority paths should not be collapsed into one truth mechanism.

For instruction revision, localized guidance and persistent evidence are afforded; see [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision). Requested consumption and iteration do not establish exercised content-directed criticism or future capacity improvement. Learning, reflection, autonomy, theory-builder conditions and self-improvement retain that record's separate limits. Distributed-parametric state remains external and uninspected, not shown fixed or adaptive. Unassessed shipped routes prevent a system-complete negative. No run or intervention evidence establishes effectiveness, reliable compliance or component causation.

## Shared records

### Operative objects

#### EPI-OBJ-scan-findings
Label: Scanner JSON findings

Symbolic JSON on stdout includes fixed-rule pattern findings, locations, severity counts, URL labels, structure and an overlap heuristic. Natural-language description/evidence fields become consequential through the later model consumer. This is distinct from [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md): scanner output, not workflow instructions; no supplied output-object counterpart. SRC-1, `skills/skill-scanner/scripts/scan_skill.py`, implementation.

> Output: JSON to stdout with structured findings.
> --- `skills/skill-scanner/scripts/scan_skill.py`

> "description_body_overlap": round(overlap, 2),
> --- `skills/skill-scanner/scripts/scan_skill.py`

#### EPI-OBJ-evidence-files
Label: Iteration evidence files

Natural-language Markdown on filesystem/Git: findings log, working set and holdout set. Expected behavior, observed behavior, suspected causes, origins and deltas are distinct fields; a tag such as human-verified is requested provenance, not an independent verification. This object is accumulated improvement evidence, distinct from the static instruction object [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md); it is a material retained product of [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), not another declaration of that route. SRC-1, `skills/skill-writer/references/iteration-evidence.md`, doctrine/design.

> `references/evidence/findings-log.md` records interpreted findings:
>
> - repeated failure patterns
> - preserved success patterns
> - suspected root causes
> - instruction changes made in response
> - unresolved risks
> --- `skills/skill-writer/references/iteration-evidence.md`

### Routes

#### EPI-RTE-pattern-scan
Label: Skill pattern scan

CLI directory → file reads and coded checks → JSON findings; Python owns this implemented diagnostic route. It inspects SKILL.md and immediate reference/script leaves, with recursive structural probes. It can skip unreadable leaves; absence of findings is not complete safety evidence. No supplied route counterpart: the Warden mention in [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval) is an external trigger, not this scanner's internal transformation. SRC-1, `skills/skill-scanner/scripts/scan_skill.py`, implementation.

- Immediate return: JSON findings/counts/structure/URLs, or error object; CLI validates directory and missing arguments.
- Later read-back: inapplicable — helper writes no durable evidence artifact.
- Delegated visibility: inapplicable — no model worker is invoked by Python.
- Selection predicate: argument-selected skill; matching regexes, coded structure rules and file suffixes select findings.
- Invalidation or expiry: inapplicable — fresh filesystem scan each call, no stored verdict.
- Activation or effect: stdout provides leads to the calling agent; no installation blocker is implemented here.
- Evidence limits: fixed patterns/heuristics and readable selected files only; no observed scan or efficacy data.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The program proposes leads, not final malicious-intent decisions; a downstream agent can discard them. This is a bounded diagnostic mode with no comprehensive security oracle. Concrete source deduction, without execution: input line `ignore previous instructions` matches the first regex, so `check_prompt_injection` appends a critical Prompt Injection Pattern finding at line 1 with that line as evidence. The occurrence follows from inspected code, but malicious intent does not: a teaching example has the same text. Thus the ledger's entailed derivation covers pattern occurrence, not its heuristic severity's real-world validity.

> (r"(?i)ignore\s+(all\s+)?previous\s+instructions", "Instruction override: ignore previous instructions", "critical"),
> --- `skills/skill-scanner/scripts/scan_skill.py`

> if re.search(pattern, line):
>     findings.append({
>         "type": "Prompt Injection Pattern",
>         "severity": severity,
>         "location": f"{filepath}:{line_num}",
>         "description": description,
>         "evidence": line.strip()[:200],
>         "category": "Prompt Injection",
>     })
>     break  # One finding per line
> --- `skills/skill-scanner/scripts/scan_skill.py`

#### EPI-RTE-security-disposition
Label: Contextual security disposition

Scanner/manual leads → surrounding-context and full behavioral review → confidence filtering → installation recommendation. Agent proposes and decides report contents; user remains the installation consumer. Distinct from [EPI-RTE-pattern-scan](#epi-rte-pattern-scan): semantic intent assessment, not regex occurrence. No supplied runtime counterpart beyond the registration mentioned in [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval). SRC-1, `skills/skill-scanner/SKILL.md`, doctrine/design.

- Immediate return: findings, needs-verification items and Safe to install/Install with caution/Do not install recommendation.
- Later read-back: uninspected — no durable report write or later loader is required by this prompt.
- Delegated visibility: inapplicable — this workflow declares no mandatory model delegation.
- Selection predicate: high confidence reports severity; medium needs verification; low is not reported.
- Invalidation or expiry: uninspected — no stored verdict withdrawal protocol specified.
- Activation or effect: advisory installation judgment; Warden enforcement remains external.
- Evidence limits: model intent evaluation is prescribed; no performed decisions, accuracy data or security oracle.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Open audit requests trigger review; script failure permits manual fallback. Agent can reject allegations by identifying benign discussion rather than operative injection. No automatic rollback/removal is prescribed. Warden configuration has failOn high/reportOn medium, but its missing implementation prevents attribution of an enforcing security gate to this package. SRC-1, `warden.toml`.

> Returns JSON with findings, URLs, structure info, and severity counts. The script catches patterns mechanically — your job is to evaluate intent and filter false positives.
> --- `skills/skill-scanner/SKILL.md`

> **Critical distinction**: A security review skill that lists injection patterns in its references is documenting threats, not attacking. Only flag patterns that would execute against the agent running the skill.
> --- `skills/skill-scanner/SKILL.md`

#### EPI-RTE-example-retention
Label: Revision example retention
Part of: [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision)

Example intake → summarization/redaction and provenance/origin tagging → evidence-file write → later working/holdout revision. Author agent or maintainer owns writing; no separate per-example human approval requirement is stated. This is the retention part, not a duplicate of the revision container or an acceptance decision. SRC-1, `skills/skill-writer/references/iteration-evidence.md`, doctrine/design.

- Immediate return: concise records and interpreted findings in [EPI-OBJ-evidence-files](#epi-obj-evidence-files).
- Later read-back: future revisions consume stored working examples and holdout validation material; actual consumption unobserved.
- Delegated visibility: uninspected — no record-transfer boundary specified for workers.
- Selection predicate: examples should outlive current task; one-off small fixes use SOURCES.md instead.
- Invalidation or expiry: guidance updates transformed examples; holdouts stay separate unless user moves them into working set.
- Activation or effect: provenance/example availability for later author judgment; promotion directs universal rules to SKILL.md and narrower examples to references.
- Evidence limits: storage/update policy only; no supplied persisted examples with route provenance or exercised acceptance.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Improvement trigger is positive/negative outcomes and review evidence. Proposed changes are instructions/references/description/validation; author chooses deltas or defers. Admission/rollback for deployed changes remains the container's bounded policy, not a new automatic gate. Origins may be human-verified, mixed or synthetic; expected behavior is an example-specific comparator, not a universal oracle. Evidence interpretation may introduce conjectured root causes; no particular non-entailed claim is available to classify as an observed conjecture.

> Do not tune directly against holdout examples unless the user explicitly moves them into the working set.
> --- `skills/skill-writer/references/iteration-evidence.md`

> Promote evidence into the skill artifacts only when it changes future behavior:
>
> - Put universal behavioral rules in `SKILL.md`.
> - Put domain-specific examples in a focused reference.
> - Put source provenance and decisions in `SOURCES.md`.
> - Keep raw or semi-raw examples in `references/evidence/`.
> --- `skills/skill-writer/references/iteration-evidence.md`

#### EPI-RTE-reader-testing
Label: Fresh reader testing

Document/questions → fresh reader answers and ambiguity checks → author diagnosis → refinement or readiness. Agent proposes questions and judges answers; if subagents unavailable, user conducts fresh-conversation tests and reports results. Distinct from [RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval): document comprehension in a user workflow, not package-adoption scoring. SRC-1, `skills/doc-coauthoring/SKILL.md`, doctrine/design, inspected Stage 3 and final-review portion only.

- Immediate return: answer-quality/gap summary and instruction to refine or finish.
- Later read-back: uninspected — document may persist but this portion specifies no future invocation loader.
- Delegated visibility: document plus question only to fresh reader; prior author conversation excluded by policy, host isolation uninspected.
- Selection predicate: predicted reader questions and checks for ambiguity, assumptions and contradictions.
- Invalidation or expiry: loop back to problematic sections when reader struggles; readiness requires consistent correct answers and no new gaps.
- Activation or effect: author revisions or final review; consumer is author/user via natural-language feedback, advisory current document horizon.
- Evidence limits: reader and author judgments, no independent fact oracle or execution evidence.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Bounded reader tests operate inside an open coauthoring request. Author decides corrections, user owns final quality and can request another review. Revision is requested, not automatically admitted or rolled back. No trace proves factual acceptance or knowledge integration.

> For each question, invoke a sub-agent with just the document content and the question.
> --- `skills/doc-coauthoring/SKILL.md`

> When Reader Claude consistently answers questions correctly and doesn't surface new gaps or ambiguities, the doc is ready.
> --- `skills/doc-coauthoring/SKILL.md`

> 2. Suggest double-checking any facts, links, or technical details
> --- `skills/doc-coauthoring/SKILL.md`

#### EPI-RTE-endpoint-check
Label: Endpoint response check

Endpoint identification → schema/type editing → requested build/tests/live-response comparison → corrections → downstream regeneration. Foreground agent proposes and judges corrections; environment response and source implementation provide scoped reference outcomes. Distinct from [RT-RTE-code-refinement](runtime.md#rt-rte-code-refinement): checks response-schema fidelity, not generic simplification. SRC-1, `skills/document-api-endpoint/SKILL.md`, doctrine/design.

- Immediate return: requested documented/typed endpoint and validation evidence; exact final message unspecified.
- Later read-back: generated schema reaches SDK/MCP only after downstream regeneration; external consumer implementation uninspected.
- Delegated visibility: inapplicable — no subagent operation specified.
- Selection predicate: user-selected endpoint and owning class, canonical response type where available.
- Invalidation or expiry: correct declared types to runtime; migrate all legacy methods on a path together.
- Activation or effect: type/decorator edits and optional public-status change, subject to external repository admission; policy current edit and later regenerated schema horizon.
- Evidence limits: live request is preferred, not supplied; serializers may be inaccurate and samples need not cover every response configuration.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Open documentation/type repair request triggers changes. Agent can revise a mismatch; no mandatory per-type human approval or automated rollback is specified. Validation commands name tested domains, not a proof of all service behavior. The method replaces inaccurate declared types rather than granting type annotations authority over runtime facts.

> Ideally, hit the live endpoint with a real token and diff the keys and types against your TypedDict. Serializers are sometimes inaccurate.
> --- `skills/document-api-endpoint/SKILL.md`

> The change reaches the `@sentry/api` SDK / MCP only after `sentry-api-schema` regenerates downstream.
> --- `skills/document-api-endpoint/SKILL.md`

#### EPI-RTE-thread-reply
Label: Review thread reply
Part of: [RT-RTE-pr-iteration](runtime.md#rt-rte-pr-iteration)

CLI thread/body pairs → newline normalization and JSON escaping → aliased gh GraphQL mutation → per-operation response classification. Python owns publication and acknowledgement handling, not truth assessment. This is the formerly uninspected reply-helper part of the PR route. SRC-1, `skills/iterate-pr/scripts/reply_to_thread.py`, implementation.

- Immediate return: operation/thread success or failure JSON; nonzero on any failed operation.
- Later read-back: GitHub retains posted text; later workflow may read feedback, but no required self-reply read-back link is established.
- Delegated visibility: inapplicable — no model worker invoked; gh receives target IDs and normalized bodies.
- Selection predicate: caller supplies thread/body pairs; aliases isolate response/error handling.
- Invalidation or expiry: inapplicable — no content expiry, retraction or replacement operation implemented.
- Activation or effect: remote comment publication; caller consumes stdout/exit status for current reply attempt; readers receive advisory text over later thread horizon.
- Evidence limits: API acknowledgement does not verify body truth; external service and actual publication unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deduction: body containing literal `Fixed.\nTested.` becomes two lines, then json.dumps escapes it into the GraphQL argument. This changes encoding, not the claim that work was fixed/tested. Parsed non-null alias data without alias-path errors yields success; it does not test those claims. Caller chooses content and can decline publication; no epistemic admission criterion or rollback is implemented. Errors/timeouts classify attempts as failed rather than withdrawing any already successful alias.

> return body.replace("\\r\\n", "\\n").replace("\\n", "\n")
> --- `skills/iterate-pr/scripts/reply_to_thread.py`

> if alias in error_paths or data.get(alias) is None:
>     operation_results.append((tid, False))
> else:
>     operation_results.append((tid, True))
> --- `skills/iterate-pr/scripts/reply_to_thread.py`

### Claims

#### EPI-CLM-skill-security
Label: Skill security screening

The skill claims security detection before adoption and produces an installation recommendation. This is distinct from [RT-CLM-preserve-functionality](runtime.md#rt-clm-preserve-functionality), a behavior-preservation claim, and has no supplied matching claim record. SRC-1, `skills/skill-scanner/SKILL.md`, doctrine/design. Mechanical patterns support leads; contextual intent assessment is explicitly delegated. Actual safe adoption, detector completeness and enforced rejection remain unobserved.

> Scan agent skills for security issues before adoption. Detects prompt injection, malicious code, excessive permissions, secret exposure, and supply chain risks.
> --- `skills/skill-scanner/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
