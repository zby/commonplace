---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "CQ epistemic routes: host-led candidate checking, persistence before acceptance, remote review admission, and feedback-driven advice selection."
run-id: AAS-2026-10-14-cq-8fb3dc41c334-01
reviewed-boundary: "5765494a3840e5f5a7223c42101f41e85cb9d898"
---

# CQ epistemic report

## Source-and-claim boundary

This report asks how CQ's shared advice becomes available, checked, retained and licensed for later reliance. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); sources are see [Source register](boundary.md#source-register). All added inspection uses SRC-1 at the frozen commit. No execution, host session, reviewer decision trace, model output or causal comparison was supplied. Test source is not an observed check result.

The material routes include host candidate drafting and sanitization, client/server admission, local and remote retention, remote review, ordinary/semantic retrieval, confirm/flag, drain, installation and the Cursor failure reminder. Transport is material where it removes warning context or breaks identity. Provider weights and host decisions remain opaque: see [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-CMP-token-embedding](runtime.md#rt-cmp-token-embedding). Their opacity does not erase the inspectable symbolic admission and ranking rules.

Consequential claims are see [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval), [RT-CLM-approved-query](runtime.md#rt-clm-approved-query), [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer), [EPI-CLM-reflection-server](#epi-clm-reflection-server) and [EPI-CLM-flag-protection](#epi-clm-flag-protection). The architecture document contains prospective mechanisms; its claims are not upgraded to implemented evaluators.

| Entry point or operation | SRC-1 source path | Coverage and evidence basis | Remaining limit / conclusion prevented |
|---|---|---|---|
| CLI dispatch, prompt output and internal hook | `cli/main.go`; `cli/cmd/prompt.go` | Direct dispatch read and prompt-command search; supplied [RT-RTE-host-installation](runtime.md#rt-rte-host-installation), [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder) | Auth/status/configuration are not factual advice evaluators; full adapter equivalence unassessed. |
| Registered MCP operations | `cli/mcpserver/server.go` | Direct full read; query/propose/confirm/flag/status registered, matching supplied runtime | No registered reflection operation; no host operation trace. |
| Proposal validation and server creation | `sdk/go/validate.go`; `server/backend/src/cq_server/services/knowledge.py` | Direct reads; supplied [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal) | Structural validity does not settle factual truth, safety or user approval. |
| Host drafting, VIBE√ and retrospective extraction | `sdk/go/prompts/SKILL.md`; `sdk/go/prompts/reflect.md` | Direct relevant prompt ranges; supplied [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection) | Doctrine, not exercised checking or accepted conjecture; actual inputs/outputs missing. |
| Local stores, remote retention and drain | `sdk/go/store_sqlite.go`; `sdk/go/client.go`; `sdk/python/src/cq/client.py` | Direct SQLite Delete read; other retention/drain findings supplied by [RT-RTE-local-drain](runtime.md#rt-rte-local-drain), [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal) | Custom stores and full PostgreSQL/Python parity uninspected; no universal deletion or lineage guarantee. |
| Remote review driver and disposition | `server/frontend/src/pages/ReviewPage.tsx`; `server/frontend/src/components/ReviewCard.tsx`; `server/backend/src/cq_server/services/reviews.py` | Direct decision-driver/card/service reads; supplied [RT-RTE-remote-review](runtime.md#rt-rte-remote-review) | Human examination possible; criterion, evidence consumed and independence not recorded by these endpoints. |
| Query/status predicates and feedback rank consumer | `server/backend/src/cq_server/repositories/_queries.py`; `sdk/go/scoring.go`; `server/backend/src/cq_server/semsearch/queries.py` | Direct SQL predicate/ranker and semantic combined-query reads; supplied [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback) | No correctness oracle; semantic distance contributes to final ordering as well as preselection; provider quality unassessed. |
| Flag construction and rejection | `sdk/python/src/cq/models.py`; `sdk/python/src/cq/scoring.py`; `sdk/python/src/cq/client.py`; `server/backend/src/cq_server/models/knowledge.py`; `server/backend/src/cq_server/services/knowledge.py` | Direct reason-only caller, request-model and duplicate-validator reads; supplied [MEM-OBJ-flags](memory.md#mem-obj-flags) | Server and Python Client duplicate flags fail before update; Go-local duplicate feedback remains distinct. |
| Instruction transformation | `cli/internal/install/pi.go` | Direct transform read, see [RT-RTE-host-installation](runtime.md#rt-rte-host-installation) | Static reshaping; no experience-driven instruction revision inferred. |
| Cleanup, withdrawal, supersession | `sdk/go`; `sdk/python/src/cq`; `server/backend/src/cq_server`; `server/scripts`; `schema` | Scoped source search for cleanup/tombstone/superseded/decay/DELETE/delete/retention; direct SQLite deletion and review/service reads | Search finds store deletion, drain and index cleanup; superseded_by schema field is not an inspected replacement evaluator. No system-complete negative about every maintenance implementation. |
| Seed, backup, migrations, failure sweep | `server/scripts/seed-kus.py`; `server/scripts/backup-db.sh`; `cli/internal/hook/cursor.go` | Supplied boundary/runtime findings; search also identifies FTS rebuild in `server/scripts/migrate-v1.sh` | Seed approval is an automated alternate, not independent truth validation; backup/index rebuilding and failure-file expiry do not validate insight content. |
| Other host adapters, discovery and remaining maintenance/test bodies | `cli/internal/install`; `sdk/go/discovery`; `server/scripts`; `server/backend/tests` | Included but not independently inspected beyond supplied findings/search | Prevents exhaustive equivalence and a system-complete absence claim. No tests executed. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-insight](#epi-obj-insight) | Summary/detail can state API behavior, causes or scope; action is a recommendation, not necessarily a proposition | Shared lesson | See record | No actual candidate/provenance trace; truth aptitude is individuated by a candidate's content, not its field name. |
| [EPI-OBJ-evidence](#epi-obj-evidence) | Counts/times/retained flags report feedback events; numerical confidence is not a measured probability of correctness | Social confidence and ranking input | See record | Stale/incorrect flags can persist; duplicate flags persist on Go-local paths but fail before server/Python Client update. Optional prose criticism has a different consumer from arithmetic; this combined container does not establish a complete part-addressed inventory. Caller independence unverified. |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | Method claims and directives; not itself evidence a lesson is true | Host behavioral protocol | See record | Host interpretation/compliance unobserved. |
| [RT-OBJ-failure-record](runtime.md#rt-obj-failure-record) | Event snippet can report a tool failure; no diagnosis or generalized causal lesson follows | Later failure reminder | See record | Clipped latest event; underlying error and successful correction not independently checked. |
| [RT-CMP-token-embedding](runtime.md#rt-cmp-token-embedding) | No individuated proposition in the dense vector | Similarity retrieval representation | See record | Numerical similarity does not confer truth warrant; provider lineage/version opaque. |
| [RT-RTE-remote-review](runtime.md#rt-rte-remote-review) | Symbolic status/reviewer/time records a decision, not its reasons | Public-query eligibility | See record | The record is a route containing this material status part; no new duplicate status object declared. |
| [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection) | Requested session summary/candidates, none supplied | Extract shareable lessons | See record | Neither candidate existence nor ampliative production established by prompt presence. |

## Authority-route ledger

Each repeated route citation identifies a different function within its valid supplied container, not a supersession. Declaring-record endpoint/state facts are see the cited record. All implemented rows remain unobserved in operation. Supporting passages are in the cited records or Shared records below.

Route ID: [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: truth-apt transformation: indeterminate. Summarization can reshape existing observations; generalized lessons can exceed them. No candidate and inputs allow entailment or non-entailment assessment.
Transition or check target: session history to compact summary and shareable candidate.
Evaluator/condition and domain: foreground agent interprets observed errors, resolutions and context; proposed scope is coding advice beyond the originating project.
Activation and timing: requested at retrospective command invocation, with mid-task drafting separately requested by skill.
Possible or observed result: requested summary, excluded routine events, candidate list; no observed result.
Implemented force: packaged instruction request, not a CQ-owned extraction computation.
Epistemic authority and scope: candidate generation only; fluency/novelty/generalizability judgments do not license truth.
Operational authority: behavior permitted, blocked, or changed: invites user presentation and later propose.
Behavioral-authority path: see [RT-BAP-skill-protocol](runtime.md#rt-bap-skill-protocol); host instruction channel, advisory/requested force, current session.
Evidence source ID and local anchor: SRC-1 `sdk/go/prompts/reflect.md`; see route for passages.
Claim IDs: [EPI-CLM-reflection-server](#epi-clm-reflection-server).
Mismatch marker: server-extraction claim disagrees with dedicated command/tool registration.
Gap/limit: absent session/candidate trace prevents classification of any actual produced claim; opaque host reasoning is not evidenced absence of reasoning.

Route ID: [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: no content change. Checking precedes any proposed sanitization.
Transition or check target: all proposal fields, recommended action risks, unsupported generalization and edge cases.
Evaluator/condition and domain: requested host VIBE√ judgment of vulnerabilities, impact, bias and edge cases; a safety/generalizability screen, not a universal factual oracle.
Activation and timing: before each direct or reflective propose under instruction.
Possible or observed result: clean, soft concern or hard finding; none observed.
Implemented force: natural-language request only; handlers do not require its result.
Epistemic authority and scope: a correctly exercised screen could identify hazards or overclaiming; clean classification alone is not acceptance of truth.
Operational authority: behavior permitted, blocked, or changed: requests caveat, sanitized alternative, hold or exclusion.
Behavioral-authority path: see [RT-BAP-skill-protocol](runtime.md#rt-bap-skill-protocol); foreground agent, instruction, advisory/requested, pre-proposal.
Evidence source ID and local anchor: SRC-1 `sdk/go/prompts/SKILL.md`; [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer) retains contrast passages.
Claim IDs: [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval), [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer).
Mismatch marker: requested model check is not automated endpoint filtering.
Gap/limit: no VIBE√ result or evaluator reliability evidence.

Route ID: [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: truth-apt transformation: indeterminate. Removing identifiers might preserve a claim, remove necessary scope conditions, or alter its meaning; no concrete rewrite establishes which.
Transition or check target: hard-finding candidate to sanitized fields including tags, pattern and action.
Evaluator/condition and domain: host rewriting under VIBE√ instructions, with user choice interactively.
Activation and timing: after hard findings, before presentation/proposal; headless hard findings instead block the requested proposal.
Possible or observed result: rewritten candidate or exclusion if no coherent generalizable lesson survives; none observed.
Implemented force: prompt instruction, not programmatic sanitization.
Epistemic authority and scope: no added warrant; preservation of source conditions must be checked per rewrite.
Operational authority: behavior permitted, blocked, or changed: supplies alternatives for approval, or holds content.
Behavioral-authority path: see [RT-BAP-skill-protocol](runtime.md#rt-bap-skill-protocol); host/user text, advisory/requested, pre-storage.
Evidence source ID and local anchor: SRC-1 `sdk/go/prompts/SKILL.md`; [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer).
Claim IDs: [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer).
Mismatch marker: none.
Gap/limit: no observed semantic-preserving sanitization or safety guarantee; instructions allow original selection by the user.

Route ID: [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: no content change.
Transition or check target: candidate publication choice, not an established truth decision.
Evaluator/condition and domain: interactive user approves/edits/skips presented content; headless agent follows requested clean/caveated safety conditions.
Activation and timing: after drafting/screening, before propose.
Possible or observed result: permission to submit, edit or hold; no observed acceptance.
Implemented force: external protocol, bypassable by direct handlers/SDK calls.
Epistemic authority and scope: permission is not evidence-consuming acceptance against a factual criterion for a named intended use.
Operational authority: behavior permitted, blocked, or changed: instructed host may submit approved candidate; headless exception permits no-user submission.
Behavioral-authority path: see [RT-BAP-skill-protocol](runtime.md#rt-bap-skill-protocol); user/host instruction exchange, requested permissive force, one submission.
Evidence source ID and local anchor: SRC-1 `sdk/go/prompts/SKILL.md`; see [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval).
Claim IDs: [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval).
Mismatch marker: approval is not enforced universally.
Gap/limit: no recorded decision, evidence consumption or criterion establishes accepted ampliative knowledge.

Route ID: [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: no content change.
Transition or check target: proposal lengths/list counts/domain presence and server model validity; credentials separately authenticate caller.
Evaluator/condition and domain: fixed code validation and Pydantic over wire structure, not factual content.
Activation and timing: before persistence; client/server validation scopes differ.
Possible or observed result: error or structurally admissible unit; none observed.
Implemented force: admission rejection on inspected validation failure.
Epistemic authority and scope: valid encoding/bounds only; credential authentication supplies principal identity, not human presence or truth.
Operational authority: behavior permitted, blocked, or changed: invalid input rejected, valid input can proceed to storage.
Behavioral-authority path: client/service code, validation result/errors, enforcing, this request.
Evidence source ID and local anchor: SRC-1 `sdk/go/validate.go`, `server/backend/src/cq_server/services/knowledge.py`; see [EPI-OBJ-insight](#epi-obj-insight).
Claim IDs: [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer).
Mismatch marker: structural validity is weaker than declared PII/factual filtering.
Gap/limit: no inspected automatic truth/PII evaluator on this selected path; no complete negative about every uninspected adapter.

Route ID: [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight), [EPI-OBJ-evidence](#epi-obj-evidence).
Content/update relation: truth-apt transformation: acquisition/import. Caller content enters CQ; original source warrant is unknown and not independently authenticated.
Transition or check target: structurally admitted input to serialized local or remote unit.
Evaluator/condition and domain: storage/client/service rules; ordinary remote persist or local fallback under conditions see route.
Activation and timing: propose success/fallback, before remote review and before any established epistemic acceptance.
Possible or observed result: persisted candidate; remote pending/private, local immediately queryable; none observed.
Implemented force: future availability conditional on store/query selection.
Epistemic authority and scope: retention ledger only, not produced accepted knowledge or lifecycle integration.
Operational authority: behavior permitted, blocked, or changed: local candidate may advise next query; remote candidate awaits review eligibility.
Behavioral-authority path: local/remote store to query caller, JSON/text, later advisory force through [RT-BAP-knowledge-guidance](runtime.md#rt-bap-knowledge-guidance), future invocations.
Evidence source ID and local anchor: SRC-1 `server/backend/src/cq_server/services/knowledge.py`, `sdk/go/client.go`; see route.
Claim IDs: [RT-CLM-approved-query](runtime.md#rt-clm-approved-query).
Mismatch marker: remote approved-only does not cover local persistence.
Gap/limit: lineage need not include source quotes or tests; tags/created_by do not establish source truth.

Route ID: [RT-RTE-remote-review](runtime.md#rt-rte-remote-review)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: no content change.
Transition or check target: displayed pending unit, summary/detail/action plus social metrics.
Evaluator/condition and domain: browser affords human content inspection; actual judgment and external verification are uninspected. API can be driven by a program, see runtime seed alternate.
Activation and timing: pending queue before approve/reject.
Possible or observed result: reviewer choice; no evidence-consuming truth-check result supplied.
Implemented force: presentation affords a decision but does not enforce a review standard.
Epistemic authority and scope: content-aware inspection is possible, not established factual validation or independent acceptance.
Operational authority: behavior permitted, blocked, or changed: choice can drive disposition in next row; skip only changes browser's session selection.
Behavioral-authority path: review card to reviewer, natural-language rendering, advisory, this review session.
Evidence source ID and local anchor: SRC-1 `server/frontend/src/components/ReviewCard.tsx`, `server/frontend/src/pages/ReviewPage.tsx`; [EPI-OBJ-insight](#epi-obj-insight).
Claim IDs: [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer).
Mismatch marker: displayed content and approve button do not prove evidence was evaluated.
Gap/limit: no criterion, reference outcome, rationale or reviewer trace supplied; no canonical answer oracle.

Route ID: [RT-RTE-remote-review](runtime.md#rt-rte-remote-review)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: review status part, see route.
Content/update relation: no content change.
Transition or check target: existing pending status to approved/rejected.
Evaluator/condition and domain: JWT-bearing caller decides; service checks unit exists and pending; SQL writes status/reviewer/time.
Activation and timing: explicit approve/reject endpoint after pending lookup.
Possible or observed result: query eligibility or exclusion; missing/already-reviewed errors; none observed.
Implemented force: approved status gates ordinary server query; rejected excludes it without deleting candidate.
Epistemic authority and scope: operational publication decision, not established acceptance of truth under a named evidence criterion.
Operational authority: behavior permitted, blocked, or changed: approved content may enter ordinary public remote results, including private-tier units.
Behavioral-authority path: review service to SQL query selector, symbolic status, enforcing eligibility, subsequent remote queries.
Evidence source ID and local anchor: SRC-1 `server/backend/src/cq_server/services/reviews.py`, `server/backend/src/cq_server/repositories/_queries.py`; see route and [RT-CLM-approved-query](runtime.md#rt-clm-approved-query).
Claim IDs: [RT-CLM-approved-query](runtime.md#rt-clm-approved-query), [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer).
Mismatch marker: no human-only, independent-review or factual-warrant invariant.
Gap/limit: read then unconditional update is not atomic single-winner review; no ordinary reversal handler established by inspected service.

Route ID: [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight), [EPI-OBJ-evidence](#epi-obj-evidence), [RT-CMP-token-embedding](runtime.md#rt-cmp-token-embedding).
Content/update relation: truth-apt transformation: non-ampliative reshaping. Selecting/ranking/deduplicating units does not generate an accepted explanatory claim.
Transition or check target: stored units to delivered advice subset.
Evaluator/condition and domain: ordinary local/server rankers use domain/context relevance × confidence. Optional server semantic retrieval first preselects approved domain-matching nearest vectors, then ranks by (0.8 × relevance + 0.2 × (1 − normalized distance)) × confidence; normalized distance is distance divided by the selected set's total distance when positive, otherwise 0. Distance therefore continues to affect final ordering, not only inclusion. Remote approved predicates and Go local-first merge remain distinct; see route.
Activation and timing: caller query; Go local-first merge can displace remote units; optional embeddings depend on configuration.
Possible or observed result: selected serialized units; none observed.
Implemented force: ranking and truncation determine delivered advice, not whether its action is executed.
Epistemic authority and scope: content imported from store, original warrant remains unknown; scores do not establish accuracy/freshness. MCP omits client's warning/source metadata, degrading delivery context for diagnosing incomplete remote retrieval.
Operational authority: behavior permitted, blocked, or changed: host can use received action as starting point under instruction to verify.
Behavioral-authority path: see [RT-BAP-knowledge-guidance](runtime.md#rt-bap-knowledge-guidance); host via tool/CLI/SDK text, ranking then advisory, current and later tasks.
Evidence source ID and local anchor: SRC-1 `sdk/go/scoring.go`, `cli/mcpserver/query.go`, `server/backend/src/cq_server/repositories/_queries.py`, `server/backend/src/cq_server/semsearch/queries.py`; see route and the semantic arithmetic passage below.
Claim IDs: [RT-CLM-approved-query](runtime.md#rt-clm-approved-query), [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer).
Mismatch marker: nearest/confident/approved is not true/current.
Gap/limit: provider semantic quality, host reliance and custom-store alternatives uninspected; wrapped semantic errors can defeat intended fallback, see runtime.

Route ID: [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: no content change.
Transition or check target: retrieved behavior claim or guidance for current environment/task.
Evaluator/condition and domain: host verifies current docs/tool output or claimed issue resolution; stale/incorrect/duplicate contrasts differ.
Activation and timing: before confirm/flag according to skill.
Possible or observed result: claimed success, independent verification or reason for objection; no observed outcome.
Implemented force: requested evaluation; feedback API trusts assertion rather than requiring evidence artifact.
Epistemic authority and scope: verified local behavior could warrant that behavior in its tested scope, not causal mechanism, transfer or replay safety. Avoided-error success needs its own contrast.
Operational authority: behavior permitted, blocked, or changed: host chooses confirmation or flag; not automatic.
Behavioral-authority path: see [RT-BAP-skill-protocol](runtime.md#rt-bap-skill-protocol); host instruction, advisory/requested, post-query.
Evidence source ID and local anchor: SRC-1 `sdk/go/prompts/SKILL.md`; see route and [EPI-CLM-flag-protection](#epi-clm-flag-protection).
Claim IDs: [EPI-CLM-flag-protection](#epi-clm-flag-protection).
Mismatch marker: none.
Gap/limit: no reference outcome or verification trace; actual factual check not established by confirm count.

Route ID: [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-evidence](#epi-obj-evidence).
Content/update relation: non-truth-apt policy/content update: numerical ranking weight and feedback metadata change; insight text is unchanged.
Transition or check target: confirmation or supported flag assertion to boosted/penalized confidence, count/time or appended flag; duplicate construction on server/Python Client paths instead rejects before persistence.
Evaluator/condition and domain: deterministic arithmetic over supplied unit and flag reason, plus Python Flag validation requiring duplicate_of for duplicate; not a factual evaluator. Server and Python Client reason-only calls omit that reference.
Activation and timing: confirm/flag invocation after ID/tier lookup; remote lookup requires approved unit. Stale/incorrect flags can complete these paths; Go-local duplicate flags can retain a reference. Server/Python Client duplicate failures precede store update.
Possible or observed result: changed stored rank input for successful confirmations and supported flags, or validation error without persisted duplicate feedback on server/Python Client paths; none observed.
Implemented force: later query ranking, not hard content withdrawal.
Epistemic authority and scope: social event ledger; no reliability/probability calibration or evidence-consuming acceptance.
Operational authority: behavior permitted, blocked, or changed: future advice priority can change; incorrect/stale flag does not revoke approved status in inspected service.
Behavioral-authority path: scoring/store to ranker to host advice, symbolic numeric then text, ranking then advisory, future queries.
Evidence source ID and local anchor: SRC-1 `sdk/go/scoring.go`, `schema/scoring.json`, `server/backend/src/cq_server/services/knowledge.py`; [EPI-OBJ-evidence](#epi-obj-evidence).
Claim IDs: [EPI-CLM-flag-protection](#epi-clm-flag-protection).
Mismatch marker: weakening is not guaranteed protection against incorrect guidance.
Gap/limit: no confidence calibration, independent-confirmation check or observed benefit. A successfully persisted flag can leave the sole matching result retrievable even at zero score. No retention/ranking authority is assigned to server/Python Client duplicate objections that fail before update; see [MEM-OBJ-flags](memory.md#mem-obj-flags).

Route ID: [RT-RTE-local-drain](runtime.md#rt-rte-local-drain)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: truth-apt transformation: acquisition/import. Remote re-proposal carries content, not a verified chain of original acceptance; source warrant unknown.
Transition or check target: LOCAL unit to new remote identity, then local delete on successful post.
Evaluator/condition and domain: HTTP success and storage deletion, not correctness or human content approval.
Activation and timing: explicit drain or configured MCP startup background attempt.
Possible or observed result: remote pending replacement/local removal; failure retains retry candidate; none observed.
Implemented force: transfer changes availability and identity; no uninterrupted-read guarantee.
Epistemic authority and scope: transport acknowledgement does not confer warrant or prove stable global identity.
Operational authority: behavior permitted, blocked, or changed: formerly immediate local advice can disappear until new remote unit is approved.
Behavioral-authority path: startup/client to stores and future selectors, symbolic transfer results, enforcing retention change, subsequent queries.
Evidence source ID and local anchor: SRC-1 `sdk/go/client.go`, `sdk/go/remote.go`; see route.
Claim IDs: [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval).
Mismatch marker: no fresh per-content approval; no exactly-once transfer invariant.
Gap/limit: duplicate posts/lost acknowledgement/deletion failures remain possible; no observed drain.

Route ID: [EPI-RTE-store-deletion](#epi-rte-store-deletion)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-insight](#epi-obj-insight).
Content/update relation: no content change.
Transition or check target: caller-selected local ID to physical deletion from unit and FTS tables.
Evaluator/condition and domain: programmatic store operation; transaction checks existence and storage result, not validity of claim.
Activation and timing: direct Store Delete or drain calls; no top-level CLI delete/MCP delete registered in inspected dispatch.
Possible or observed result: committed removal/error; none observed.
Implemented force: local withdrawal by physical removal.
Epistemic authority and scope: no correctness judgment and no accepted replacement inferred.
Operational authority: behavior permitted, blocked, or changed: removes this local stored unit from future queries.
Behavioral-authority path: caller/store to query DB, symbolic ID/transaction, enforcing, future local queries.
Evidence source ID and local anchor: see record, SRC-1 `sdk/go/store_sqlite.go`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: removal cannot retract advice already delivered; no automatic stale evaluator is established by this method.

Route ID: [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-failure-record](runtime.md#rt-obj-failure-record).
Content/update relation: truth-apt transformation: non-ampliative reshaping. Event strings are clipped and rendered, not generalized into a diagnosis.
Transition or check target: selected failure event to bounded latest record and stop reminder.
Evaluator/condition and domain: code excludes interrupts, selects latest per conversation, bounds snippets; not a truth evaluator.
Activation and timing: failure hook writes; later stop reads/clears; session start sweeps old files.
Possible or observed result: reminder then deletion; none observed.
Implemented force: automatic context supply under host hook contract, not an epistemic decision.
Epistemic authority and scope: incomplete event report with source-error truth unknown; no warranted lesson.
Operational authority: behavior permitted, blocked, or changed: host may notice failure and reconsider; no enforced action.
Behavioral-authority path: hook stdout to host, event text, advisory, next stop; expiry limits retained horizon.
Evidence source ID and local anchor: SRC-1 `cli/internal/hook/cursor.go`; see route.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: host correction/compliance unobserved; truncation may remove conditions necessary for diagnosis.

Route ID: [RT-RTE-host-installation](runtime.md#rt-rte-host-installation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: static instructions, see [RT-OBJ-skill](runtime.md#rt-obj-skill).
Content/update relation: truth-apt transformation: non-ampliative reshaping. Pi transform removes name metadata and changes slash-command spelling; it does not create a new lesson.
Transition or check target: packaged command text to installed host command file.
Evaluator/condition and domain: deterministic frontmatter detection/string replacement; ownership hashes govern overwrite separately.
Activation and timing: operator installation; actual host load unobserved.
Possible or observed result: transformed static file; none observed.
Implemented force: future instruction availability conditional on host loading.
Epistemic authority and scope: imported methodology remains source doctrine, not experience-derived acceptance.
Operational authority: behavior permitted, blocked, or changed: Pi command references match filename-derived naming.
Behavioral-authority path: see [RT-BAP-skill-protocol](runtime.md#rt-bap-skill-protocol); installed Markdown, requested force, future sessions.
Evidence source ID and local anchor: SRC-1 `cli/internal/install/pi.go`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: concrete implementation deduction: input `---\nname: cq:reflect\ndescription: Mine\n---\nRun /cq:reflect\n` yields `---\ndescription: Mine\n---\nRun /cq-reflect\n`; no target execution needed. Missing/unclosed frontmatter returns original source, so replacement is conditional.

> if inFrontmatter && strings.HasPrefix(line, "name:") {
> continue
> }
> --- `cli/internal/install/pi.go`

> if !closed {
> return source
> }
> return strings.ReplaceAll(strings.Join(out, ""), "/cq:", "/cq-")
> --- `cli/internal/install/pi.go`

> relevance_weight = 0.8
> distance_weight = 0.2
> normalized_distance = distance / total_distance if total_distance > 0 else 0
> result = relevance * relevance_weight + (1 - normalized_distance) * distance_weight
> --- `server/backend/src/cq_server/semsearch/queries.py`

> * u.evidence.confidence,
> u.id,
> u,
> --- `server/backend/src/cq_server/semsearch/queries.py`

These implementation passages establish the optional semantic final-score formula, not observed ordering quality or truth warrant. They refine the supplied runtime's compressed reranking description without changing its route identity.

No lifecycle-integration route is established by these inspected retention, indexing, feedback and review operations: acceptance in the epistemic sense has not been established. This is a limitation on this assessment, not a system-complete absence claim about host behavior. Nor is an entailed explanatory derivation established. Code supports exact deductions about its declared arithmetic/formatting domain; those deductions do not prove caller content true.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval) | See record | See record | Interactive approval requested; headless exception | [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), [RT-RTE-local-drain](runtime.md#rt-rte-local-drain) | None supplied | No human-compliance comparison | Host protocol, not universal admission invariant | Direct APIs/startup drain do not prove approval. |
| [RT-CLM-approved-query](runtime.md#rt-clm-approved-query) | See record | See record | Approved remote query selection | [RT-RTE-remote-review](runtime.md#rt-rte-remote-review), [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | None supplied | SQL scope only; local/review APIs differ | Operational status gate implemented | Approved does not mean true, private or independently reviewed. |
| [EPI-CLM-guardrails-layer](#epi-clm-guardrails-layer) | See record | See record | Safety/quality checks declared at ingestion, promotion and retrieval | [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), [RT-RTE-remote-review](runtime.md#rt-rte-remote-review), [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | None supplied | No filtering efficacy or factual-check comparison | Prompt checks, shape admission and review status are distinct supported mechanisms | Selected executable paths do not implement the claimed automatic PII/factual/staleness evaluator suite. |
| [EPI-CLM-reflection-server](#epi-clm-reflection-server) | See record | See record | Skill subsection describes server extraction | [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection) | None supplied | No session or model output | Dedicated command asks foreground agent to extract | No registered reflection MCP tool; server-extraction claim not supported. |
| [EPI-CLM-flag-protection](#epi-clm-flag-protection) | See record | See record | Flag wrong/stale/duplicate guidance to protect others | [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback), [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) | None supplied | No controlled accuracy/behavior outcomes | Stale/incorrect flags and Go-local duplicate flags can retain objections and penalize confidence | Server/Python Client duplicates fail before update; successful penalization does not ensure withdrawal or prevent reliance. |

## Bounded conclusion

CQ implements acquisition and retention of caller-authored natural-language advice, with source warrant **unknown**, plus retrieval and non-ampliative ranking/formatting. It affords requested host candidate production and screening. Without concrete session inputs, candidate text and decision evidence, neither an actual ampliative conjecture nor an accepted produced claim is established. Source-native examples and field labels do not resolve that gap: see [EPI-OBJ-insight](#epi-obj-insight) and [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection).

The admission mechanisms have different targets. Client/server checks license valid bounded structure. Interactive user approval licenses instructed submission; headless rules offer a separate requested gate. Remote approve/reject licenses ordinary remote query eligibility based on status. None of these supplied records establishes an evidence-consuming truth acceptance decision naming criterion, intended use and scope. Retention, remote approval and indexing consequently are not promoted to lifecycle integration. The browser can support real human judgment; the lack of a trace limits this report, not the human's possible competence: see [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal) and [RT-RTE-remote-review](runtime.md#rt-rte-remote-review).

Verification is requested against current documentation/tool output or local successful use. A genuine local result could support a bounded behavior claim; it cannot alone license a causal explanation, transfer or component attribution. Confirmation/flag code consumes assertions without verifying those results. Successful confirmations and supported flags change social metrics and subsequent ranking, not insight content or approved status. Stale/incorrect flags can persist locally and remotely, and Go-local duplicate flags can persist; server/Python Client duplicate construction fails before update and supplies no retained objection or changed rank input. Thus the implemented future influence is ranking then advisory host guidance, not enforced truth reliance or automatic withdrawal: see [EPI-OBJ-evidence](#epi-obj-evidence), [EPI-CLM-flag-protection](#epi-clm-flag-protection), [RT-BAP-knowledge-guidance](runtime.md#rt-bap-knowledge-guidance).

Local candidates can reach later queries before remote review; drain can replace them with new remote identities and delete the local copy before remote approval. MCP warning omission and identity-changing transfer limit provenance/availability in different ways. Store deletion and remote rejection remove eligibility under their distinct scopes, but cannot retract already delivered advice: see [RT-RTE-local-drain](runtime.md#rt-rte-local-drain), [EPI-RTE-store-deletion](#epi-rte-store-deletion), [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query).

The Cursor hook supplies selected failure evidence rather than generating a lesson. Static installation reshapes instructions rather than revising them from experience. Optional embeddings influence both nearest-vector preselection and final weighted distance/relevance scoring multiplied by confidence, with opaque provider state and no factual-check license. These independent contributions coexist with missing operation and causal evidence: see [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder), [RT-RTE-host-installation](runtime.md#rt-rte-host-installation), [RT-CMP-token-embedding](runtime.md#rt-cmp-token-embedding).

Experience-responsive retained feedback gives a wired future selection capacity; improved future action capacity remains unestablished. Agent-led reflection is requested, while exercised reflection and theory-builder conditions 1–4 remain independently uninspected as in [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection). CQ does not own the external model's reasoning or next application action; computation-owned score changes do not establish whole-loop autonomy. No exercised self-improvement follows: evidence-responsive assertions change rank state and can reach later hosts, but actual later behavioral dependence and independently assessed improvement are not supplied. These are separate property limits, not one system-wide negative verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-insight
Label: KnowledgeUnit insight

Source-native identity: `KnowledgeUnit.insight`, fields summary/detail/action. Natural-language content is stored within serialized units in local/remote databases and interpreted by host agents or browser reviewers. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill), which is shipped method guidance rather than per-discovery content. It is the content passed through [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal) and [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), not a duplicate of those routes. SRC-1 `schema/knowledge_unit.json`, `server/backend/src/cq_server/services/knowledge.py`, `server/frontend/src/components/ReviewCard.tsx`.

> "description": "Tripartite insight: what happened, why it matters, what to do.",
> "required": ["summary", "detail", "action"],
> --- `schema/knowledge_unit.json`

> await self._knowledge.insert(unit)
> return unit
> --- `server/backend/src/cq_server/services/knowledge.py`

> <p className="text-gray-600 dark:text-slate-300 mb-3 leading-relaxed">
> {unit.insight.detail}
> </p>
> --- `server/frontend/src/components/ReviewCard.tsx`

The schema permits behavior claims and causal explanations but imposes no evidential sufficiency test. Go proposal validation rejects size/count/presence failures rather than evaluating semantics. SRC-1 `sdk/go/validate.go`.

> validateLength("summary", params.Summary, cqschema.SummaryMaxLength()),
> validateLength("detail", params.Detail, cqschema.DetailMaxLength()),
> validateLength("action", params.Action, cqschema.ActionMaxLength()),
> --- `sdk/go/validate.go`

No candidate instance or input/output trace is supplied. Recommendations need not be truth-apt; accompanying behavior/scope claims can be. Source warrant is unknown at acquisition and remains unverified by these structural checks.

#### EPI-OBJ-evidence
Label: KnowledgeUnit evidence and flags

Source-native identity: evidence confidence/confirmations/last_confirmed and flags reason/time/detail. Symbolic numeric/enum/time fields are consumed by fixed code; optional flag detail is natural language. Substrate: serialized knowledge units in stores, not an independent evidence/test archive. The supplied [MEM-OBJ-flags](memory.md#mem-obj-flags) overlaps this combined container's flags array; evidence confidence/confirmations/last_confirmed are additional parts here. These are overlapping containers, not distinct uniform objects or a complete part-addressed inventory. Symbolic arithmetic consumes confidence/reason; optional explanatory detail can reach a host as prose on Go-local serialized delivery, not as an argument evaluated by the ranker. [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback) updates supported parts, [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) consumes them. SRC-1 `schema/knowledge_unit.json`, `schema/scoring.json`, `sdk/go/scoring.go`, `server/backend/src/cq_server/services/knowledge.py`.

> out.Evidence.Confidence = max(out.Evidence.Confidence-cqschema.FlagPenalty(), cqschema.ConfidenceFloor())
> now := time.Now()
> out.Flags = append(slices.Clone(ku.Flags), Flag{
> --- `sdk/go/scoring.go`

> relevance := ku.relevance(domains, languages, frameworks, pattern)
> results = append(results, ranked{ku: ku, score: relevance * ku.Evidence.Confidence})
> --- `sdk/go/scoring.go`

Confirmation boost/count passage is see [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback). An implementation deduction, not an execution result: schema defaults supply initial confidence 0.5, boost 0.1, penalty 0.15, ceiling 1 and floor 0. A confirmation transforms 0.5 to 0.6 and increments count; a following successfully constructed stale/incorrect flag transforms 0.6 to 0.45 and appends reason/time. Go-local duplicate flags can likewise be retained, including a duplicate link. This deduction does not apply to duplicate requests on the server/Python Client paths, which fail before update. Insight text is unchanged. At equal relevance this changes ranking weight, not truth warrant. SRC-1 `schema/scoring.json`, `sdk/go/scoring.go`.

> "confirmation_boost": {
> "type": "number",
> "default": 0.1,
> "description": "Confidence increase per confirmation."
> },
> --- `schema/scoring.json`

> flagged = apply_flag(unit, reason)
> await self._knowledge.update(flagged)
> return flagged
> --- `server/backend/src/cq_server/services/knowledge.py`

For supported stale/incorrect reasons, the inspected flag service updates serialized unit data, not review status. Server FlagRequest carries only reason; the server service and Python Client call apply_flag without duplicate_of. Python Flag validation therefore rejects duplicate before the update, even though the standalone scoring function can accept a reference. The supplied [MEM-OBJ-flags](memory.md#mem-obj-flags) retains the Go-local counterpart and remote payload loss. SRC-1 `server/backend/src/cq_server/models/knowledge.py`, `sdk/python/src/cq/client.py`, `sdk/python/src/cq/scoring.py`, `sdk/python/src/cq/models.py`.

> new_flag = Flag(reason=reason, duplicate_of=duplicate_of)
> --- `sdk/python/src/cq/scoring.py`

> if self.reason is FlagReason.DUPLICATE and not self.duplicate_of:
> raise ValueError("duplicate_of is required when reason is 'duplicate'")
> --- `sdk/python/src/cq/models.py`

> flagged = apply_flag(unit, reason)
> self._store.update(flagged)
> --- `sdk/python/src/cq/client.py`

The optional prose part and arithmetic part remain separate consumer mechanisms inside this coarse combined record; no uniform representational-form or authority classification is inferred. The SQL status update is a separate operation. No claimant independence, probability calibration or automatic stale/incorrect removal is established here. The sole-candidate counterexample is source-derived: the ranker sorts/truncates without a positive-score admission threshold, so a flagged matching sole candidate can remain delivered, even with zero confidence. This qualifies protection, not the existence of flagging.

> if len(results) > limit {
> results = results[:limit]
> }
> --- `sdk/go/scoring.go`

### Routes

#### EPI-RTE-store-deletion
Label: Local store deletion

Owner/endpoints: direct Store caller → Go SQLite Store.Delete → transaction → later local query. This is a separately exposed store operation, not a duplicate of the transport progression in [RT-RTE-local-drain](runtime.md#rt-rte-local-drain); drain is one caller. Compared with [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback), deletion removes content rather than penalizing it. SRC-1 `sdk/go/store_sqlite.go`, `cli/main.go`, `cli/mcpserver/server.go`.

- Immediate return: committed deletion or transaction/not-found error.
- Later read-back: removed local unit and FTS entry are unavailable to subsequent store queries.
- Delegated visibility: no remote transfer in this method; callers own any further effects.
- Selection predicate: supplied unitID equality in DELETE statements.
- Invalidation or expiry: physical removal on successful transaction; no expiry/evaluator in this method.
- Activation or effect: wired local removal, not observed; host copies already returned remain outside its control.
- Evidence limits: inspected Go SQLite method only; no executed transaction or universal store/provider equivalence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller proposes and decides withdrawal; program can veto missing ID, closed store or storage failure. Operating mode: direct storage maintenance, including drain. Answer oracle: inapplicable — storage outcome rather than truth reference. Trigger is Delete invocation; proposed change is removal. Recovery: transaction rollback on failure; no restoration archive in this method. No human per-content approval required; guidance shaping the call is outside the method, except the supplied drain procedure. No formulated theory or accepted successor is established.

> // Delete removes a knowledge unit by ID.
> func (s *sqliteStore) Delete(ctx context.Context, unitID string) error {
> --- `sdk/go/store_sqlite.go`

> res, err := tx.ExecContext(ctx, "DELETE FROM knowledge_units WHERE id = ?", unitID)
> --- `sdk/go/store_sqlite.go`

> if affected == 0 {
> return fmt.Errorf("unit %q not found", unitID)
> }
> --- `sdk/go/store_sqlite.go`

### Claims

#### EPI-CLM-guardrails-layer
Label: Automatic guardrails layer

Claimed operation: architecture declares ingestion PII/prompt-injection/quality filtering, graduation factual/security/quality checks and retrieval staleness/dispute/low-confidence validation. SRC-1 `docs/architecture.md`, doctrine/design. Distinct from interactive approval in [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval) and status filtering in [RT-CLM-approved-query](runtime.md#rt-clm-approved-query): this claim names content evaluators, not those gates.

> **Ingestion filtering** is the primary PII control. Automated guardrails handle PII detection; human reviewers focus on accuracy, relevance, quality, and generalizability.
> --- `docs/architecture.md`

> **Graduation gates** run a more thorough assessment when knowledge is nominated for promotion between tiers — checking factual consistency, potential security implications, and alignment with quality standards.
> --- `docs/architecture.md`

> **Retrieval-time validation** flags knowledge that has been disputed, is approaching staleness thresholds, or has low confidence relative to the agent's domain.
> --- `docs/architecture.md`

Counterevidence to broad absence of checking: shipped VIBE√ requests meaningful host criticism and rewriting. This supports requested checking, not an enforced automated endpoint suite. SRC-1 `sdk/go/prompts/SKILL.md`.

> - **E — Edge cases**: Was the lesson learned from a single observation, or has it been validated across multiple cases? Are there obvious conditions (OS, version, scale, concurrency) under which it would not hold and that the candidate fails to acknowledge?
> --- `sdk/go/prompts/SKILL.md`

> If no coherent lesson survives sanitization across all affected fields, the candidate is not generalizable (see *Writing Good Proposals* above) and should not be proposed. Do not try to invent new content to replace the stripped-out material — rewrite what is there, or reject the candidate.
> --- `sdk/go/prompts/SKILL.md`

Inspected executable proposal/service paths check shape and persist; review changes status; ordinary rankers select by relevance/confidence, while optional semantic ranking also includes weighted normalized distance. No implementation or observed operation of the declared automatic suite is established on these selected routes. Architectural support for that suite remains doctrine only within this inspection scope. Available uninspected adapters prevent a system-complete negative.

#### EPI-CLM-reflection-server
Label: Server reflection extraction

Claimed operation: skill's reflection subsection asks for full session context and says server returns candidate units. SRC-1 `sdk/go/prompts/SKILL.md`, doctrine/design. No supplied claim is this referent. Closest supplied route [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection) already identifies the conflicting procedure.

> Pass the full session conversation context to `reflect`. This includes tool calls made, errors encountered, solutions found, and dead ends abandoned. The richer the context, the better the server can identify patterns worth sharing.
> --- `sdk/go/prompts/SKILL.md`

> The server returns a list of candidate knowledge units. Each candidate contains:
> --- `sdk/go/prompts/SKILL.md`

Dedicated command and stub evidence is see [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection). Direct frozen registration check adds implementation evidence:

> srv.mcpSrv.AddTool(QueryTool(), srv.HandleQuery)
> srv.mcpSrv.AddTool(ProposeTool(), srv.HandlePropose)
> srv.mcpSrv.AddTool(ConfirmTool(), srv.HandleConfirm)
> srv.mcpSrv.AddTool(FlagTool(), srv.HandleFlag)
> srv.mcpSrv.AddTool(StatusTool(), srv.HandleStatus)
> --- `cli/mcpserver/server.go`

This establishes a documentation mismatch, not a defective runtime referent requiring supersession. CQ supplies agent-led instructions, not this described server extraction endpoint. No actual session upload/extraction operation is observed.

#### EPI-CLM-flag-protection
Label: Flag protection

Claimed operation: flagging incorrect/stale/duplicate guidance protects other agents from incorrect information. SRC-1 `sdk/go/prompts/SKILL.md`, doctrine/design. Distinct from supplied claim records; [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback) is its closest route counterpart.

> Always flag rather than silently ignoring bad knowledge. This protects other agents from acting on incorrect information.
> --- `sdk/go/prompts/SKILL.md`

The skill bounds confidence explicitly:

> Newly proposed units start at confidence 0.5. Each confirmation adds 0.1; each flag subtracts 0.15. Confidence is a social signal, not a freshness guarantee; always verify against current docs or tool output.
> --- `sdk/go/prompts/SKILL.md`

Implemented penalty, retained objection and later ranking are supported by [EPI-OBJ-evidence](#epi-obj-evidence) for stale/incorrect flags and Go-local duplicate flags. Server/Python Client duplicate requests fail validation before update, so those objections do not reach retention or ranking. Successfully persisted penalties can lower priority but do not revoke review status or ensure the unit is not delivered. No outcome comparison establishes actual protection. The counterexample qualifies the claim's strength, while preserving feedback's implemented future influence.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
