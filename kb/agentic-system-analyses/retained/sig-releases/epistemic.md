---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Sig epistemic routes: what capture, synthesis, human sharing approval and later AI context license in the frozen release documentation."
run-id: AAS-2026-10-14-sig-releases-50379145ac31-01
reviewed-boundary: "314bbea9d1cef911cea0f201eec66a57c2e59020"
---

# Sig epistemic report

## Source-and-claim boundary

The question is whether Sig's declared accumulation of work context includes checks and acceptance of truth-apt claims, rather than retention and permission to share. Scope, exclusions and frozen evidence identity are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). This is a documentation-grounded partial application loop, not an inspected implementation. No target execution was performed.

Direct inspection here covered the complete README, beta release notes, analytics document and all three issue forms in SRC-1, plus the tracked-tree inventory at the reviewed commit. The runtime findings are provisional but no defective supplied fact or needed supersession was found. The combined capture/share record remains a valid container; the records below separate its materially different parts.

| Entry point or operation | Source path in SRC-1 | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Desktop launch, capture and voice input | `RELEASE_NOTES_v0.1.0-beta.md`, `README.md` | Direct reads; [RT-RTE-capture-share](runtime.md#rt-rte-capture-share), [EPI-RTE-private-synthesis](#epi-rte-private-synthesis) | Launch assets and voice implementation unavailable; no call graph or transcription fidelity conclusion |
| Private synthesis, factual/personal separation | `README.md` | Direct read; [EPI-CLM-factual-layer](#epi-clm-factual-layer), [EPI-RTE-private-synthesis](#epi-rte-private-synthesis) | No input/output instance, prompt or evaluator; cannot individuate produced propositions or classify their entailment |
| Organizational draft and send gate | `README.md`, `RELEASE_NOTES_v0.1.0-beta.md` | Direct reads; [EPI-RTE-org-draft](#epi-rte-org-draft), [EPI-RTE-share-approval](#epi-rte-share-approval) | No review trace or enforcement code; permission is not established truth acceptance |
| Local storage, deletion and team sync | `README.md`, `RELEASE_NOTES_v0.1.0-beta.md` | Direct reads; [EPI-RTE-note-retention](#epi-rte-note-retention), [EPI-RTE-context-use](#epi-rte-context-use), [EPI-RTE-local-deletion](#epi-rte-local-deletion) | No provenance schema, conflict handling, correction or remote retraction mechanism |
| Provider messages, replies and retained-context use | `README.md`, `ANALYTICS.md` | Direct reads; [RT-RTE-provider-message](runtime.md#rt-rte-provider-message), [RT-CMP-ai-provider](runtime.md#rt-cmp-ai-provider), [EPI-RTE-context-use](#epi-rte-context-use) | No payload, response specimen or provider implementation; truth-apt response content and checking not determinable |
| Shared skills | `README.md` | Direct read; [RT-OBJ-skills](runtime.md#rt-obj-skills), [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync) | No skill bodies, loader or recipient review; truth-apt portions and behavior-changing force unresolved |
| Slack and optional connections | `README.md`, `ANALYTICS.md` | Direct reads; optional connections and Slack sync counts named | No exposed operation definitions or content path; acquisition, maintenance and evaluation through Slack unassessed |
| Analytics, errors, feedback and prioritization | `ANALYTICS.md` | Direct read; [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress), [RT-CLM-telemetry-filter](runtime.md#rt-clm-telemetry-filter) | Counts and sanitation are not correctness checks; no consumer admitting a product revision shown |
| Public bug/feature intake | `.github/ISSUE_TEMPLATE/bug_report.yml`, `.github/ISSUE_TEMPLATE/feedback.yml`, `.github/ISSUE_TEMPLATE/config.yml` | Direct reads; [RT-RTE-product-feedback](runtime.md#rt-rte-product-feedback) | Forms solicit reports and a privacy attestation; no repair, truth adjudication or release consumer shown |
| CLI dispatch, hooks, registered tools, cleanup and rejection operations | Complete tracked-tree inventory | No executable source, tool definitions or shipped prompts in the frozen artifact; supplied boundary corroborates inventory | Does not establish absence in the app; prevents system-complete negative about alternate evaluators or bypasses |
| License and screenshots | `LICENSE`, `screenshots/03-chat.png`, `screenshots/icon.png` | License role supplied by boundary; images remain excluded from visual inspection | No legal or UI-layout inference; these do not close the application-loop gap |

The principal warrant-related claims are see [EPI-CLM-factual-layer](#epi-clm-factual-layer) and [EPI-CLM-context-payoff](#epi-clm-context-payoff). Publication/privacy claims are see [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing), [RT-CLM-provider-direct](runtime.md#rt-clm-provider-direct) and [RT-CLM-telemetry-filter](runtime.md#rt-clm-telemetry-filter). None expressly promises a correctness test for meeting claims. Unavailable implementation prevents determining whether an undisclosed evaluator exists. Missing run evidence separately prevents establishing activation; missing comparisons prevent establishing benefit or attributing it to accumulated context.

## Epistemic-object inventory

Each evidence cell identifies a declaring record rather than duplicating its fields. Candidate content describes potential truth conditions, not observed propositions.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-capture](#epi-obj-capture) | User reports about what happened or was agreed in a meeting | see record | SRC-1, `README.md` | No actual report or provenance instance |
| [EPI-OBJ-factual-record](#epi-obj-factual-record) | Meeting events, decisions and commitments as represented in a structured note | see record | SRC-1, `README.md` | Label factual does not establish truth or derivation |
| [EPI-OBJ-personal-layer](#epi-obj-personal-layer) | Interpretations may assert causes or meanings; some portions may instead express preference | see record | SRC-1, `README.md` | No instance; truth-apt and non-truth-apt portions cannot be individuated |
| [EPI-OBJ-org-version](#epi-obj-org-version) | Selected organizational account of the meeting | see record | SRC-1, `README.md` | Exact retained statements and omitted context unknown |
| [RT-OBJ-skills](runtime.md#rt-obj-skills) | Not determinable: no workflow body supplied | see record | SRC-1, `README.md` | Workflow label alone cannot establish knowledge or policy content |
| [RT-CMP-ai-provider](runtime.md#rt-cmp-ai-provider) | Distributed-parametric model content not locally individuated; conversational response may contain claims | see record | SRC-1, `README.md`, `ANALYTICS.md` | No exact version, weight access, payload or response specimen; no inference of parameter updates |
| [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress) | Event assertions about usage, errors and success; explicit user feedback | see record | SRC-1, `ANALYTICS.md` | Success field's criterion unspecified; errors need not be semantic failures |
| [RT-RTE-product-feedback](runtime.md#rt-rte-product-feedback) | Reporter assertions about expected versus actual behavior | see record | SRC-1, `.github/ISSUE_TEMPLATE/bug_report.yml` | Submission affordance, not accepted diagnosis |

## Authority-route ledger

All architectural statuses below refer to documentary routes, not inspected app code. A declared reviewer is not silently promoted to a truth evaluator. Source warrant on imported narrative is unknown; restructuring, storage and permission do not strengthen it. Fields owned by a cited record are marked see.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-capture-share](runtime.md#rt-rte-capture-share) | content transformation | doctrine only | [EPI-OBJ-capture](#epi-obj-capture) | truth-apt transformation: acquisition/import | User meeting account enters capture | User recollection; no independent check specified | see record | see record | No inspected app force | Imported account; source warrant unknown | Declared start of local synthesis | Sig capture channel; proposed input; current capture | SRC-1, `README.md` | none | none | Import does not produce or verify the meeting facts |
| [EPI-RTE-private-synthesis](#epi-rte-private-synthesis) | content transformation | doctrine only | [EPI-OBJ-factual-record](#epi-obj-factual-record), [EPI-OBJ-personal-layer](#epi-obj-personal-layer) | truth-apt transformation: indeterminate | Narrative to separated private layers | No truth evaluator specified | see record | see record | No inspected app force | Candidate organization only | Declared local note creation | Private note consumer; markdown; advisory context; later sessions claimed | SRC-1, `README.md` | [EPI-CLM-factual-layer](#epi-clm-factual-layer) | unknown semantic fidelity | Reshaping, derivation and conjecture cannot be distinguished without contents and transformation evidence |
| [EPI-RTE-org-draft](#epi-rte-org-draft) | content transformation | doctrine only | [EPI-OBJ-org-version](#epi-obj-org-version) | truth-apt transformation: indeterminate | Private account to clean org-level draft | No semantic evaluator specified | see record | see record | No inspected app force | Candidate for publication, not accepted knowledge | Declared presentation to reviewer | User; exact-text review UI; advisory proposal; this share | SRC-1, `README.md` | [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing) | unknown omissions | Removing personal material may change interpretation; no checked preservation evidence |
| [EPI-RTE-share-approval](#epi-rte-share-approval) | disposition/acceptance | doctrine only | [EPI-OBJ-org-version](#epi-obj-org-version) | no content change | Permission to send selected exact text | Human chooses inclusion and approves; publication/privacy domain, not named truth criterion | see record | see record | Enforcing gate claimed, not inspected | No evidence-consuming truth acceptance established | Declared approval permits team publication; withholding blocks this share | Sig send boundary then team repository; permissive; this share and retained team context | SRC-1, `README.md` | [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing) | scope distinction | No separate correctness-check result, evidence or acceptance criterion disclosed |
| [EPI-RTE-note-retention](#epi-rte-note-retention) | retention | doctrine only | [EPI-OBJ-factual-record](#epi-obj-factual-record), [EPI-OBJ-personal-layer](#epi-obj-personal-layer), [EPI-OBJ-org-version](#epi-obj-org-version) | no content change | Local persistence and approved team availability | Local write policy opaque; team write follows publication approval | see record | see record | No inspected app force | Retention grants no new warrant | Declared later availability | Local files or git-backed team knowledge; availability, not compliance; across sessions | SRC-1, `README.md`, `RELEASE_NOTES_v0.1.0-beta.md` | [EPI-CLM-context-payoff](#epi-clm-context-payoff) | retention is not integration | No accepted claim linked to evidence or changed organization after truth acceptance shown |
| [EPI-RTE-context-use](#epi-rte-context-use) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-factual-record](#epi-obj-factual-record), [EPI-OBJ-personal-layer](#epi-obj-personal-layer), [EPI-OBJ-org-version](#epi-obj-org-version) | no content change | Retained work history reaches later AI context | Selector, request boundary and evaluation opaque | see record | see record | Context supply claimed, compliance unobserved | Relevance and correctness not licensed by presence | Claimed influence on later answers | AI tools and teammate Sig; context channel; advisory content; later sessions | SRC-1, `README.md` | [EPI-CLM-context-payoff](#epi-clm-context-payoff) | delivery versus benefit | Exact selected subset and post-selection content unknown |
| [EPI-RTE-local-deletion](#epi-rte-local-deletion) | lineage/freshness/recovery | doctrine only | Local retained layers | no content change | User removes local files | User file deletion, not a stated truth rejection | see record | see record | User ability claimed | No documented withdrawal of a proposition's warrant | Local removal only claimed | Filesystem; destructive local removal; subsequent local availability | SRC-1, `README.md`, `RELEASE_NOTES_v0.1.0-beta.md` | none | local versus global withdrawal | Remote copies, cached context and correction propagation unresolved |
| [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync) | operational admission/selection/consumption | doctrine only | [RT-OBJ-skills](runtime.md#rt-obj-skills) | no content change | Shared workflow becomes available | User shares; recipient activation unknown | see record | see record | No inspected loader force | Not determinable without skill bodies | Reusable workflows advertised; no evidence-responsive policy update established | see record; invocation force unresolved | SRC-1, `README.md` | none | none | Sync alone does not prove use, criticism or adaptation |
| [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress) | check/evidence production | doctrine only | Usage/error events and comments | no content change | Event/property eligibility and privacy sanitation | Claimed allowlist/sanitizer; telemetry payload domain, not work-content truth | see record | see record | Dropping disallowed fields claimed | No correctness warrant; success metric undefined | Allowed telemetry can leave; prioritization claimed | App emitter to PostHog and developers; diagnostic/advisory; later prioritization | SRC-1, `ANALYTICS.md` | [RT-CLM-telemetry-filter](runtime.md#rt-clm-telemetry-filter) | diagnostics versus validation | Sanitization not inspected; no admitted repair consumer |
| [RT-RTE-product-feedback](runtime.md#rt-rte-product-feedback) | check/evidence production | implemented | Reporter problem account | truth-apt transformation: acquisition/import | Required report fields and privacy attestation | Form definitions impose required fields; human supplies assessment, not software adjudication | see record | see record | Form affordance only; hosting unobserved | Imported report with unknown warrant | Intake supported, no implemented production revision | GitHub issue form; advisory report to humans; later triage unspecified | SRC-1, `.github/ISSUE_TEMPLATE/bug_report.yml`, `.github/ISSUE_TEMPLATE/feedback.yml` | none | intake versus correction | Required privacy checkbox does not inspect text or validate diagnosis |

No distinct truth-check, truth-acceptance, accepted-claim lifecycle-integration or evidence-responsive behavior-adaptation route was established in these documents. This is not a system-complete negative: the app, tool surface, optional integrations and provider implementation are unavailable. The private and organizational transformations cannot be classified as non-ampliative merely because the product calls them synthesis. Nor does failure to establish entailment prove ampliative conjecture. No concrete deterministic text transformation can be deduced from implementation: sanitation is documented, not supplied as code.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-factual-layer](#epi-clm-factual-layer) | see record | SRC-1, `README.md`; doctrine/design and reported operation in beta notes | see record | none inspected | none supplied | No source-grounded factuality comparison | Declared separation of facts and personal interpretation | Actual separation and truth of factual layer unknown |
| [EPI-CLM-context-payoff](#epi-clm-context-payoff) | see record | SRC-1, `README.md`; doctrine/design | see record | none inspected | none supplied | No baseline, intervention, task domain, metric or component contrast | Retained context is intended to aid later AI work | Dramatically sharper AI not demonstrated |
| [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing) | see record | SRC-1, `README.md`; doctrine/design | see record | none inspected | none supplied | No gate trace or bypass coverage | Declared human publication permission | Approval does not establish truth acceptance or universal egress control |
| [RT-CLM-provider-direct](runtime.md#rt-clm-provider-direct) | see record | SRC-1, `README.md`; doctrine/design | see record | none inspected | none supplied | No transport or payload evidence | Independent provider-egress claim bounds local-only wording | Does not warrant response correctness or provider privacy |
| [RT-CLM-telemetry-filter](runtime.md#rt-clm-telemetry-filter) | see record | SRC-1, `ANALYTICS.md`; doctrine/design | see record | none inspected | none supplied | No payload trace, sanitizer or backend evidence | Claimed payload filtering; explicit comments are an exception | Privacy filtering cannot be used as a work-knowledge evaluator |

## Bounded conclusion

Sig declares an acquisition-and-context route: a user's meeting account becomes private structured notes, a selected organizational account can be human-approved for team publication, and retained history is intended to reach later AI context. Sources, roles and limits are see [EPI-RTE-private-synthesis](#epi-rte-private-synthesis), [EPI-RTE-org-draft](#epi-rte-org-draft), [EPI-RTE-share-approval](#epi-rte-share-approval), [EPI-RTE-note-retention](#epi-rte-note-retention) and [EPI-RTE-context-use](#epi-rte-context-use). Imported source warrant is unknown. No supplied artifact shows which statements survive synthesis, which are added, or whether a claimed fact is true.

The consequential named decision is permission to share selected text, not evidence-consuming acceptance against a truth criterion. Its intended use is team publication and its scope is the organizational version; the proposed consumer is Sig's send boundary, followed by team storage and later AI context. The declared gate is permissive for that share, not an observed correctness guarantee. Local retention can precede any sharing decision. Consequently retention and operational use do not establish accepted ampliative knowledge or post-acceptance lifecycle integration.

The accessible documents establish neither warranted entailed derivation nor a specific ampliative conjecture: no warranted premise set, concrete derived claim or checked interpretation is supplied. Response-generation semantics, skill bodies and distributed-parametric state remain opaque; no model update, accepted theory or criticism loop can be inferred. Learning benefit is unestablished independently of intended persistence. Reflection, autonomous theory building and self-improvement are not established by sync, telemetry or accumulated notes. These are separate evidence limits, not consequences of a single unfavorable status.

The counterexamples that bound stronger readings are material: explicit provider requests and telemetry comments qualify the broad local-only wording; user sharing approval checks publication permission rather than disclosed truth criteria; deleting a local folder does not document withdrawal from team or provider context. Diagnostics and public reports can supply evidence about operation, but no admitted repair or subsequent behavior causally depending on it is shown. The narrower operational design is coherent without a knowledge-production claim. Its advertised compounded AI benefit remains a claim, not an observed or causally supported result.

## Shared records

### Operative objects

#### EPI-OBJ-capture
Label: Capture

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

Distinct input part of the supplied route, not its retained output. SRC-1, `README.md` describes a user's raw meeting account. Natural-language narrative is interpreted by Sig; voice is optional, but transcription and initial storage substrate are unspecified. It can report decisions and commitments with truth conditions over that meeting. No concrete account or provenance trace is supplied. The capture/synthesis/share passage is retained in the parent record.

#### EPI-OBJ-factual-record
Label: Factual record

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

Distinct private output part: the factual layer, not the personal interpretation or org draft. SRC-1, `README.md` identifies natural-language work records retained as local markdown in the chosen folder. File schema and links to original capture are uninspected. Its load-bearing source passage is retained in [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing). Factual is the product's role label, not a verified truth status.

#### EPI-OBJ-personal-layer
Label: Personal layer

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

Distinct private interpretive output part. SRC-1, `README.md` describes the user's read on what the facts mean, stored locally with the private notes and not shared. Natural-language interpretation has human/model consumption; local markdown is the declared substrate. Some contents could assert explanations; others could express attitudes. Neither is instantiated here. Evidence passage is see [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing). File-level separation and access enforcement are uninspected.

#### EPI-OBJ-org-version
Label: Org-level version

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

Distinct proposed team-facing account, not either private layer. SRC-1, `README.md` says Sig prepares a clean org-level version for exact-text review, then team knowledge is synchronized using git. Natural-language content is interpreted by reviewer and downstream AI. Draft storage and exact shared encoding are unspecified; local notes are markdown, but that alone does not establish a team schema. Evidence passage is see the parent record. No specimen establishes what was preserved or removed.

### Routes

#### EPI-RTE-private-synthesis
Label: Private synthesis

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

This is the private transformation part, separate from the parent's publication progression. Endpoints are [EPI-OBJ-capture](#epi-obj-capture) and the factual/personal output layers. Sig is the declared synthesizer; the user supplies the account. SRC-1, `README.md` and `RELEASE_NOTES_v0.1.0-beta.md` declare the operation; the minimum passage is retained in the parent. Synthesis prompts, model attribution and semantic checks are unavailable. The source's guidance is to structure the account and separate facts from personal observations. Human initiation is not disclosed per-content approval of the local write. Rejection, veto and rollback of synthesis are uninspected; local deletion is separately declared. Mode is open user capture; no reference-answer oracle or improvement trigger is disclosed.

- Immediate return: Structured private note is advertised; no instance supplied.
- Later read-back: Work history is advertised for later AI context; exact consumption is uninspected.
- Delegated visibility: Private material is declared local; inference payload visibility is unresolved.
- Selection predicate: Capture initiates synthesis; factual/personal classification rules are uninspected.
- Invalidation or expiry: uninspected — no synthesis correction or versioning policy supplied.
- Activation or effect: Claimed private note production, not observed semantic separation.
- Evidence limits: Documentation without prompts, code, inputs, outputs or checks; content relation indeterminate.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-org-draft
Label: Org draft

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

This is the team-facing proposal transformation, distinct from private synthesis and the send decision. SRC-1, `README.md`, parent passage, declares Sig prepares a clean org-level version from capture material and presents exact text to the user. It does not expose the input subset, transformation rules, original-text comparison or omitted context. Sig proposes; the human can withhold the later share and decide inclusion. Guidance is organizational relevance and separation from the personal layer. This is open capture-driven drafting, not a curriculum; no oracle, evidence-responsive revision mechanism, draft recovery or truth acceptance is disclosed. The proposed org text may later persist if shared; draft lifetime is unknown.

- Immediate return: Proposed org-level text for review.
- Later read-back: uninspected — draft reload is unspecified; approved team text is covered separately.
- Delegated visibility: User sees proposed text; no draft-stage team visibility is declared.
- Selection predicate: User decides inclusion; automatic preparation policy is uninspected.
- Invalidation or expiry: uninspected — no draft rejection storage or expiry policy supplied.
- Activation or effect: Claimed preparation and review opportunity; not observed preservation of meaning.
- Evidence limits: No concrete draft, provenance map or semantic evaluator; relation indeterminate.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-share-approval
Label: Share approval

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

This is the publication-disposition part, not the draft producer or retention step. SRC-1, `README.md`, parent passage, gives the user the inclusion decision, exact-text review and send action; [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing) retains the explicit-approval claim. Target/domain is permission to publish this organizational text to the team. No named truth criterion, evidence input, reference answer or recorded correctness decision is disclosed. Human review may in practice catch errors, but neither that practice nor an operative truth-check result is evidenced. The human decides and can veto; Sig prepares and is claimed to gate send. Trigger is a proposed share, guidance is private-by-default selective sharing, persisted change is team availability of approved text. Mode is open user work. Recovery and remote rollback are uninspected. Operational permission is not acceptance under the epistemic-report definition.

- Immediate return: Permission to send selected text, or withheld publication; acknowledgment unspecified.
- Later read-back: Approved content is claimed to become teammate context.
- Delegated visibility: Team receives the organizational material; exact recipient scope is unspecified.
- Selection predicate: Human decides contents and explicitly sends after review.
- Invalidation or expiry: uninspected — no revocation or correction propagation described.
- Activation or effect: Human publication gate claimed; enforcement and successful send unobserved.
- Evidence limits: No executable gate or reviewed instance; no demonstrated truth acceptance.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-note-retention
Label: Note retention

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

This separates persistence from transformation, publication disposition and later use. SRC-1, `README.md`, declares local markdown in a selected folder and git-backed central team knowledge; passages are retained in the parent and [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing). Local private layers and approved team content have different admission policies: per-local-write approval is unspecified; team publication requires user approval. Sig owns declared note writes and git handles team synchronization. There is no documented evidence-acceptance prerequisite, evidence linkage or integration after truth acceptance. Guidance is capture retention and selective team sharing, not a named correctness criterion; no oracle or improvement trigger is given. Local delete is available, remote rollback is unresolved.

- Immediate return: Claimed local files and, after approval, team knowledge availability.
- Later read-back: Private history and teammate context advertised; selector and exact payload unknown.
- Delegated visibility: Local personal layer versus approved team layer, as declared; provider payload not enumerated.
- Selection predicate: Capture for local retention; explicit user selection for publication.
- Invalidation or expiry: Local deletion permitted; remote expiry, conflicts and supersession uninspected.
- Activation or effect: Retention and synchronization claimed; no runtime persistence trace supplied.
- Evidence limits: Markdown substrate and git mechanism do not establish lineage, truth acceptance or semantic integrity.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-context-use
Label: Context use

Part of: [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

This is the parent's later-consumption part, separate from transport and storage. SRC-1, `README.md`, parent passage and [EPI-CLM-context-payoff](#epi-clm-context-payoff), declares history usable by AI and shared knowledge immediately available as teammate context. Consumer is later AI tooling or teammate Sig; exact request, content subset, insertion point and context-control policy are not supplied. Claimed force is advisory context through natural-language interpretation, not an enforced instruction or demonstrated compliance. No check precedes disclosed use beyond the publication gate for the team layer. Personal-layer inclusion in provider requests remains unresolved; direct requests are separately described in [RT-RTE-provider-message](runtime.md#rt-rte-provider-message).

- Immediate return: uninspected — no context selector response or constructed request supplied.
- Later read-back: Accumulated private history and approved team knowledge are advertised as later context.
- Delegated visibility: Teammate Sig receives shared context; provider-visible subset unknown.
- Selection predicate: uninspected — no query, ranking, inclusion rule or request policy supplied.
- Invalidation or expiry: uninspected — no stale-context eviction or correction handling supplied.
- Activation or effect: Context delivery and improved AI work claimed; actual influence unobserved.
- Evidence limits: No selected payload, invocation trace, response or comparison; delivery is not warrant or benefit.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-local-deletion
Label: Local deletion

Distinct responsibility from the capture/share progression: user removal of retained local files, overlapping its persistence endpoint but not contained in its production sequence. SRC-1, `README.md` and `RELEASE_NOTES_v0.1.0-beta.md` explicitly permit deletion and say uninstall leaves captures intact. Owner is the user acting on local storage. No proposition-level rejection, evidence-driven revision or team retraction route follows. Trigger is user choice, change is local removal, veto is the user's decision not to delete, and recovery is unspecified. This is not an oracle-guided or improvement-mode route.

> Captures and notes are stored as plain markdown in the folder you choose during first-run setup.
> --- `RELEASE_NOTES_v0.1.0-beta.md`

> Drag Sig from Applications to the Trash (macOS), or remove the package via your package manager (Linux). Your captures stay on your computer as plain markdown in the folder you picked during setup. Delete that folder if you want them gone.
> --- `RELEASE_NOTES_v0.1.0-beta.md`

- Immediate return: Claimed local file removal by user action; uninstall alone preserves files.
- Later read-back: uninspected — whether removed files cease reaching cached context is unspecified.
- Delegated visibility: inapplicable — local deletion itself has no described recipient; remote copies remain unresolved.
- Selection predicate: User chooses files or the capture folder for deletion.
- Invalidation or expiry: Local removal is described; remote invalidation and recovery uninspected.
- Activation or effect: User ability declared; no deletion run or propagated withdrawal shown.
- Evidence limits: No deletion implementation or cached/remote consumer trace; no global withdrawal inference.
- documentation conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

### Claims

#### EPI-CLM-factual-layer
Label: Factual layer

SRC-1, `README.md` claims separation and saving of a factual record and personal interpretation; `RELEASE_NOTES_v0.1.0-beta.md` reports the corresponding beta function. This claim concerns output organization, not an explicit evidence-consuming truth test. Closest supplied claim is [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing), which owns privacy/publication authority and retains the two-layer passage. This is a distinct claim about synthesis's semantic organization, not a duplicate privacy guarantee.

> - **Synthesis** — facts separated from your personal layer, stored on your machine
> --- `RELEASE_NOTES_v0.1.0-beta.md`

#### EPI-CLM-context-payoff
Label: Context payoff

SRC-1, `README.md` claims accumulated history makes AI dramatically sharper. No supplied claim record has this referent: [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing) addresses privacy, and [RT-RTE-capture-share](runtime.md#rt-rte-capture-share) quotes the benefit in its surrounding account but declares a workflow, not a benefit claim. The doctrine supports intended reuse, not observed learning or causal improvement. Target tasks, contrast, metric and assessment horizon beyond the rhetorical week labels are unspecified.

> **Week 12:** You've built something nobody else has — months of real work history that makes every AI you use dramatically sharper.
> --- `README.md`
