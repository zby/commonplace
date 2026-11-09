---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Nemsy epistemic routes: document acquisition, generated Wiki content, model checks and downstream reliance."
run-id: AAS-2026-11-09-nemsy-2a6b7963bf65-01
reviewed-boundary: "2338bab0aab96a91efb90a80249f33510b630260"
---

# Nemsy epistemic report

## Source-and-claim boundary

This assesses the whole shipped document-to-Wiki-to-answer loop fixed in
[boundary](boundary.md#boundary-and-evidence), using its
[Source register](boundary.md#source-register). SRC-1 supplies implementation
and doctrine/design, not observed operation. The question is whether imported
documents and model responses acquire warranted reliance, rather than merely
being stored and reused. Exclusions and dependency boundaries are see
[boundary](boundary.md#boundary-and-evidence); no development-plane or roadmap
claim is assessed.

Public/design claims are [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding) and
[EPI-CLM-knowledge-accumulation](#epi-clm-knowledge-accumulation). The former is a generation constraint;
the latter promises accumulation and requests related-page updates, not a
formal proof or universal truth oracle.

| Entry point or operation | Source path | Coverage and records |
|---|---|---|
| CLI default chat, slash commands, ingest/query/lint and reasoning alternate | SRC-1: `src/nemsy/cli.py` | Supplied runtime dispatch findings: [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat), [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [RT-RTE-reasoning-query](runtime.md#rt-rte-reasoning-query), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint); direct focused read of smoke dispatch |
| Agent generation, parser, archive, save and context loader | SRC-1: `src/nemsy/agent.py` | Direct complete read; all five task prompts and their consumers; [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup) plus runtime routes |
| Web chat/query/lint/ingest/save | SRC-1: `src/nemsy/web.py` | Direct read of these handlers; independent prompt construction checked against [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [RT-RTE-insight-save](runtime.md#rt-rte-insight-save) and [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) |
| Wiki listing, citation resolution and file viewing | SRC-1: `src/nemsy/web.py`, `frontend/src/components/MessageContent.tsx` | Direct component/resolver reads plus correction-round Chat callback and file endpoint reads; [EPI-RTE-citation-display](#epi-rte-citation-display); browser save/history boundary otherwise supplied [RT-RTE-insight-save](runtime.md#rt-rte-insight-save) |
| Status, source list, balance and settings | SRC-1: `src/nemsy/web.py`, `src/nemsy/cli.py` | Endpoint/function enumeration directly searched; supplied runtime account covers counters and inert settings POST. Accounting, not truth acceptance; detailed rendering uninspected, preventing a complete UI-correctness claim |
| Hash/status, persistence, deletion and guidance | SRC-1: `src/nemsy/vault.py` | Direct hash/status read; write/delete/guidance responsibilities otherwise supplied [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and runtime account. No inference that deleting a page retracts its copies |
| LLM dispatch and provider state | SRC-1: `src/nemsy/llm.py` | Direct message construction, chat and stream calls; text-only request without registered tools; reasoning/text extraction otherwise supplied [RT-CMP-deepseek](runtime.md#rt-cmp-deepseek) and [RT-RTE-reasoning-query](runtime.md#rt-rte-reasoning-query) |
| Page schema and smoke evaluators | SRC-1: `src/nemsy/schema.py`, `tests/test_smoke.py`, `src/nemsy/cli.py` | Direct complete schema/test reads; [EPI-RTE-smoke-check](#epi-rte-smoke-check), [EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition) |
| Public intent | SRC-1: `README.md` | Direct opening/structure read; [EPI-CLM-knowledge-accumulation](#epi-clm-knowledge-accumulation); remainder not used as evidence |

Missing user documents and actual generated pages prevent proposition-level
fidelity, entailment or novelty judgments. Missing service traces prevent
claims of compliance or activated reliance. Missing interventions/comparisons
prevent benefit and component-effect attribution. Opaque provider internals
prevent an account of hidden model evaluation or training. The available
source is sufficient to distinguish implemented request, admission and
consumption; it does not license a system-complete negative about every
possible evaluator or external human workflow.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-content](#epi-obj-source-content) | see record | see record | SRC-1: `src/nemsy/agent.py` | see record |
| [EPI-OBJ-summary-content](#epi-obj-summary-content) | see record | see record | SRC-1: `src/nemsy/agent.py` | see record |
| [EPI-OBJ-questions-content](#epi-obj-questions-content) | see record | see record | SRC-1: `src/nemsy/agent.py` | see record |
| [EPI-OBJ-answer-content](#epi-obj-answer-content) | see record | see record | SRC-1: `src/nemsy/agent.py` | see record |
| [EPI-OBJ-insight-content](#epi-obj-insight-content) | see record | see record | SRC-1: `src/nemsy/agent.py` | see record |
| [EPI-OBJ-lint-content](#epi-obj-lint-content) | see record | see record | SRC-1: `src/nemsy/agent.py` | see record |
| [EPI-OBJ-index-content](#epi-obj-index-content) | see record | see record | SRC-1: `src/nemsy/agent.py` | see record |
| [RT-CMP-deepseek](runtime.md#rt-cmp-deepseek) | not determinable at individual parametric proposition level | see record | SRC-1: `src/nemsy/llm.py` | Remote weights and their provenance uninspected; no inference from Wiki updates to weight learning |

## Authority-route ledger

Each compact entry separates a consequential function. “See” leaves the
declaring record's endpoints, timing and evidence limits with that record.
Architectural status below describes source wiring, not exercised behavior.
Retention is not treated as lifecycle integration.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source-content](#epi-obj-source-content) → [EPI-OBJ-summary-content](#epi-obj-summary-content)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Local source text enters generation
Evaluator/condition and domain: Caller supplies content; no source-veracity check
Activation and timing: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Possible or observed result: Source and Wiki context delivered
Implemented force: Permissive input admission
Epistemic authority and scope: Source warrant unknown; import does not endorse source
Operational authority: Allows document text to inform a proposed summary
Behavioral-authority path: Configured model, request text, advisory, one ingest
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-summary-content](#epi-obj-summary-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Document plus selected Wiki to generated SUMMARY
Evaluator/condition and domain: Model requested to extract and relate; domain is supplied text
Activation and timing: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Possible or observed result: Candidate Markdown
Implemented force: Generation, not verification
Epistemic authority and scope: No checked entailment or evidence-consuming acceptance
Operational authority: Makes a candidate available to parser
Behavioral-authority path: Parser, response string, permissive, this ingest
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Claim IDs: [EPI-CLM-knowledge-accumulation](#epi-clm-knowledge-accumulation)
Mismatch marker: none
Gap/limit: Could faithfully reshape, derive or conjecture; actual output needed. Non-entailment is not established merely by generation.

Route ID: [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-summary-content](#epi-obj-summary-content); [EPI-OBJ-questions-content](#epi-obj-questions-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup)
Evaluator/condition and domain: see [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup)
Activation and timing: see [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup)
Possible or observed result: see [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup)
Implemented force: Enforcing text selection, not truth validation
Epistemic authority and scope: No increased warrant
Operational authority: Changes which returned spans survive
Behavioral-authority path: Parser, regex/string operations, enforcing, saved page
Evidence source ID and local anchor: see [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-summary-content](#epi-obj-summary-content)
Content/update relation: no content change
Transition or check target: Presence of SUMMARY delimiter, not accuracy
Evaluator/condition and domain: Python regex in response-format domain
Activation and timing: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Possible or observed result: None on missing delimiter; text eligible otherwise
Implemented force: Syntactic veto only
Epistemic authority and scope: Not epistemic acceptance
Operational authority: Allows write without per-content semantic review
Behavioral-authority path: Writer, parse result, permissive, current write
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Claim IDs: [EPI-CLM-knowledge-accumulation](#epi-clm-knowledge-accumulation)
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-summary-content](#epi-obj-summary-content); [EPI-OBJ-questions-content](#epi-obj-questions-content)
Content/update relation: no content change
Transition or check target: Candidate page to filesystem
Evaluator/condition and domain: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Activation and timing: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Possible or observed result: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Implemented force: Durable candidate use
Epistemic authority and scope: No added license from storage
Operational authority: Page becomes eligible for recency read-back
Behavioral-authority path: Wiki loader then model, file text, permissive then advisory, later requests
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-source-content](#epi-obj-source-content)
Content/update relation: no content change
Transition or check target: Source hash equality; not source truth or summary correctness
Evaluator/condition and domain: Stripped UTF-8 SHA-256 comparison, direct inspected vault code
Activation and timing: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Possible or observed result: new/changed/done/empty
Implemented force: CLI skip/force policy; Web differs
Epistemic authority and scope: Hash equality only, not endorsement
Operational authority: Unchanged input may skip regeneration even after a failed parse
Behavioral-authority path: CLI pending selector, JSON hash, enforcing unless force, later ingest
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Claim IDs: none
Mismatch marker: none
Gap/limit: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); page/result-independent recording limits 'done'.

Route ID: [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-index-content](#epi-obj-index-content); [EPI-OBJ-summary-content](#epi-obj-summary-content); [EPI-OBJ-answer-content](#epi-obj-answer-content); [EPI-OBJ-insight-content](#epi-obj-insight-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Index plus count-bounded recency pages enter request
Evaluator/condition and domain: Python mtime/count selector; model relevance interpretation
Activation and timing: see [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)
Possible or observed result: Subset concatenated with file labels
Implemented force: Selection enforcing; interpretation advisory
Epistemic authority and scope: Retained page status supplies no correctness license
Operational authority: Allows retained text to inform answers
Behavioral-authority path: see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context)
Evidence source ID and local anchor: see [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)
Claim IDs: [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding)
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-content](#epi-obj-answer-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Wiki text and question to answer/citations
Evaluator/condition and domain: Model; open questions without a reference oracle
Activation and timing: see [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)
Possible or observed result: Answer including possible abstention or ARCHIVABLE marker
Implemented force: Returned directly, no semantic veto
Epistemic authority and scope: Grounding policy only
Operational authority: Answer delivered before independent checking
Behavioral-authority path: Human reader, text/SSE, advisory, current question
Evidence source ID and local anchor: see [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)
Claim IDs: [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding)
Mismatch marker: none
Gap/limit: Entailment versus conjecture needs actual inputs/output; reasoning alternate has the separately recorded tuple-consumer defect.

Route ID: [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-content](#epi-obj-answer-content)
Content/update relation: no content change
Transition or check target: Wiki snapshot/history to subsequent chat turn
Evaluator/condition and domain: see [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat)
Activation and timing: see [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat)
Possible or observed result: see [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat)
Implemented force: Context admission
Epistemic authority and scope: Conversation reuse is not independent corroboration
Operational authority: Prior text can influence next reply
Behavioral-authority path: see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context)
Evidence source ID and local anchor: see [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat)
Claim IDs: [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding)
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-content](#epi-obj-answer-content)
Content/update relation: no content change
Transition or check target: Caller archive flag, not answer truth
Evaluator/condition and domain: Caller operation choice; no expected-answer oracle
Activation and timing: see [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Possible or observed result: Eligible answer archived irrespective of ARCHIVABLE
Implemented force: Permissive flag
Epistemic authority and scope: Not evidence-consuming epistemic acceptance
Operational authority: Authorizes write before caller review of that generated answer
Behavioral-authority path: Archive helper, flag and answer text, permissive, current query
Evidence source ID and local anchor: see [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-content](#epi-obj-answer-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Strip ARCHIVABLE marker, add query metadata and index
Evaluator/condition and domain: see [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Activation and timing: see [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Possible or observed result: see [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Implemented force: Filesystem retention
Epistemic authority and scope: No added warrant
Operational authority: Eligible for later Wiki read-back
Behavioral-authority path: Wiki loader/model, Markdown, advisory, later invocations
Evidence source ID and local anchor: see [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-insight-content](#epi-obj-insight-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: History to rewritten insight page
Evaluator/condition and domain: Model; requested conclusions/background/links, no supplied fresh Wiki
Activation and timing: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Possible or observed result: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Implemented force: Generation
Epistemic authority and scope: Neither format nor a 'background and derivation' heading proves entailment
Operational authority: Proposes a replacement representation of the chosen history
Behavioral-authority path: Save parser, returned Markdown, permissive, one save
Evidence source ID and local anchor: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Claim IDs: none
Mismatch marker: none
Gap/limit: Could reshape or add content; actual history/output needed.

Route ID: [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-insight-content](#epi-obj-insight-content)
Content/update relation: no content change
Transition or check target: Nonempty history and caller save request
Evaluator/condition and domain: Human chooses operation/history boundary; code/model choose content/title
Activation and timing: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Possible or observed result: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Implemented force: Operation approval, not particular-content approval
Epistemic authority and scope: No semantic acceptance decision
Operational authority: Allows generated page write without post-generation confirmation
Behavioral-authority path: Writer, parsed text/title, permissive, current save
Evidence source ID and local anchor: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-insight-content](#epi-obj-insight-content)
Content/update relation: no content change
Transition or check target: Generated insight and index to disk
Evaluator/condition and domain: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Activation and timing: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Possible or observed result: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Implemented force: Durable candidate
Epistemic authority and scope: No added warrant
Operational authority: Later context eligible; cached CLI snapshot unchanged
Behavioral-authority path: Wiki loader/model, Markdown, advisory, later loads
Evidence source ID and local anchor: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-lint-content](#epi-obj-lint-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Contradictions, obsolete claims, orphans and gaps in supplied Wiki window
Evaluator/condition and domain: Model diagnosis; no independent source/reference oracle; graph coverage windowed
Activation and timing: see [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)
Possible or observed result: ISSUES/SUGGESTIONS/NEXT_SOURCES text requested
Implemented force: Advisory to user, not enforcing against a page
Epistemic authority and scope: Diagnostic candidates, not established contradictions
Operational authority: No installed page correction or changed reliance state
Behavioral-authority path: User, report/SSE, advisory, current maintenance request
Evidence source ID and local anchor: see [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)
Claim IDs: [EPI-CLM-knowledge-accumulation](#epi-clm-knowledge-accumulation)
Mismatch marker: none
Gap/limit: Missing outputs prevent evaluating an individual diagnosis; no automatic lint-result withdrawal/rejection consumer in these handlers.

Route ID: [EPI-RTE-citation-display](#epi-rte-citation-display)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-content](#epi-obj-answer-content); resolved retained pages: [MEM-OBJ-source-page](memory.md#mem-obj-source-page), [MEM-OBJ-query-page](memory.md#mem-obj-query-page), [MEM-OBJ-insight-page](memory.md#mem-obj-insight-page)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [EPI-RTE-citation-display](#epi-rte-citation-display)
Evaluator/condition and domain: see [EPI-RTE-citation-display](#epi-rte-citation-display)
Activation and timing: see [EPI-RTE-citation-display](#epi-rte-citation-display)
Possible or observed result: see [EPI-RTE-citation-display](#epi-rte-citation-display)
Implemented force: Navigational, not evidential endorsement
Epistemic authority and scope: A clickable page is not a verified support relation
Operational authority: Allows reader to inspect a resolved page
Behavioral-authority path: Browser/user, numbered links then file API, advisory, current display
Evidence source ID and local anchor: see [EPI-RTE-citation-display](#epi-rte-citation-display)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [EPI-RTE-smoke-check](#epi-rte-smoke-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-summary-content](#epi-obj-summary-content); [EPI-OBJ-answer-content](#epi-obj-answer-content)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-smoke-check](#epi-rte-smoke-check)
Evaluator/condition and domain: see [EPI-RTE-smoke-check](#epi-rte-smoke-check)
Activation and timing: see [EPI-RTE-smoke-check](#epi-rte-smoke-check)
Possible or observed result: see [EPI-RTE-smoke-check](#epi-rte-smoke-check)
Implemented force: Assertions halt test on failure
Epistemic authority and scope: Only the asserted structural/substring properties
Operational authority: Can fail the test invocation, not gate normal writes
Behavioral-authority path: pytest, assertions, enforcing, selected test run
Evidence source ID and local anchor: see [EPI-RTE-smoke-check](#epi-rte-smoke-check)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

Route ID: [EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-summary-content](#epi-obj-summary-content); [EPI-OBJ-answer-content](#epi-obj-answer-content)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition)
Evaluator/condition and domain: see [EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition)
Activation and timing: see [EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition)
Possible or observed result: see [EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition)
Implemented force: Smoke command exit status
Epistemic authority and scope: No truth or production-admission license
Operational authority: Reports pass/fail, does not roll back already written pages
Behavioral-authority path: CLI/caller, pytest return code, enforcing exit, smoke invocation
Evidence source ID and local anchor: see [EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition)
Claim IDs: none
Mismatch marker: none
Gap/limit: No supplied run; delivery is not demonstrated activation.

No lifecycle-integration entry is claimed: these retention paths do not first
establish acceptance against an evidence-consuming content criterion. Index
appending connects files navigationally, but does not convert admission into
epistemic acceptance. No behavior/policy-adaptation entry is inferred merely
from suggestions or the name “insight.”

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding) | see record | see record | see record | [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat), [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | None supplied | None supplied; prompt compliance and citation entailment unchecked | Wiki-only generation is requested | Confident style and citations do not prove warrant; partial context cannot prove whole-Wiki absence |
| [EPI-CLM-knowledge-accumulation](#epi-clm-knowledge-accumulation) | see record | see record | see record | [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-insight-save](runtime.md#rt-rte-insight-save), [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) | None supplied | No comparison; related-page edits are not implemented by a general edit-plan executor | Accumulation by caller-triggered generation/storage and index append | Broader autonomous maintenance or improved knowledge quality unestablished |

## Bounded conclusion

Nemsy imports local documents with unknown source warrant, generates candidate
pages and answers, and reuses recent retained text. See
[RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer),
[RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive) and [RT-RTE-insight-save](runtime.md#rt-rte-insight-save).
These operations are wired, not observed. A source hash controls redundant
work, not reliability. The parser can remove text and admit a malformed or
unsupported summary; [EPI-RTE-summary-cleanup](#epi-rte-summary-cleanup) demonstrates its narrow
transformation without executing the target.

There is no demonstrated produced accepted ampliative claim in these routes.
Without actual source/output pairs their generation relation is indeterminate,
not automatically novel conjecture. Prompted synthesis and a derivation heading
do not establish entailed derivation. No warranted premises plus checked
interpretation establish a new conclusion here. No actual user source is
available to decide that more specifically.

Checking is heterogeneous. The SUMMARY delimiter checks parseability.
[RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) requests model criticism of a limited page window,
but its suggestions have no implemented edit/withdrawal consumer.
[EPI-RTE-smoke-check](#epi-rte-smoke-check) asserts limited structural and substring criteria;
[EPI-RTE-smoke-disposition](#epi-rte-smoke-disposition) consumes test success only for a smoke
command's message/exit. The test writes precede checks and are not rolled back.
These are real limited evaluators, counterexamples to “no checks,” but not
semantic acceptance of retained claims.

Actual operational authority lies in writes and later context delivery:
caller-selected operations permit code to write model-selected content,
and the model later receives it as Wiki text. See [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context).
Schema, freshness and link rendering do not add truth warrant. The browser
can resolve a claimed citation and deliver current retained Wiki page text to a
later human browser consumer without checking that it supports the answer; [EPI-RTE-citation-display](#epi-rte-citation-display). Regeneration/overwrites and the
caller-trusted deletion helper described in the runtime account supply no
claim-level retraction propagation to archived answers, insights or a cached
CLI Wiki snapshot.

Provider parameters, exact version and endpoint fixity are see
[RT-CMP-deepseek](runtime.md#rt-cmp-deepseek). Hidden learning or evaluation is not determinable.
Persisted insights afford future consumption; they do not alone demonstrate
improved capacity. Lint has no retained criticism-to-next-round revision
loop in the inspected functions. Thus this account establishes neither an
exercised self-improvement pathway nor autonomous evidence-responsive theory
revision. These limits do not negate the separate implemented acquisition,
generation, diagnostic and retention routes, and give Nemsy no single
epistemic score.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-content
Label: Imported source text

SRC-1: `src/nemsy/agent.py`. Natural-language assertions in caller UTF-8 documents; filesystem substrate before import, request string during ingestion. External claims are acquired, not produced. Directory guidance is separate instruction text in the same request. Particular propositions and source warrant unknown without a supplied Vault.
Distinct identity: operative content object, not the progression represented by
[RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); no operative-object counterpart is declared in the supplied runtime.
Evidence passages: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and the task/cleanup passages below.

#### EPI-OBJ-summary-content
Label: SUMMARY page body

SRC-1: `src/nemsy/agent.py`. Natural-language generated claims and links in a response string, then Markdown file. Requested type/source/date metadata is symbolic labeling; the unvalidated body supplies future model-interpreted content. No particular proposition or faithful compression is demonstrated.
Distinct identity: operative content object, not the progression represented by
[RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); no operative-object counterpart is declared in the supplied runtime.
Evidence passages: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and the task/cleanup passages below.

#### EPI-OBJ-questions-content
Label: QUESTIONS appendix

SRC-1: `src/nemsy/agent.py`. Natural-language questions, requested to distinguish original-source clues from external-verification needs; normally not truth-apt questions themselves, although embedded premises/labels may assert claims. Response substring appended to the source Markdown, not a research-result evaluator.
Distinct identity: operative content object, not the progression represented by
[RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); no operative-object counterpart is declared in the supplied runtime.
Evidence passages: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and the task/cleanup passages below.

#### EPI-OBJ-answer-content
Label: Answer and archived query body

SRC-1: `src/nemsy/agent.py`. Natural-language answers/abstentions with [[page]] references and optional ARCHIVABLE marker in returned strings, console/SSE and optional query Markdown. Wiki-only and synthesis criteria are instructions, not checked facts. Archive metadata/marker stripping are symbolic formatting, not new warrant.
Distinct identity: operative content object, not the progression represented by
[RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer); no operative-object counterpart is declared in the supplied runtime.
Evidence passages: see [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer) and the task/cleanup passages below.

#### EPI-OBJ-insight-content
Label: Conversation insight page

SRC-1: `src/nemsy/agent.py`. Natural-language conclusions, background and linked knowledge generated from selected history, stored as Markdown after code-fence removal. Symbolic title extraction controls filename. No new Wiki is loaded for this call, and the saved content is not reviewed before write.
Distinct identity: operative content object, not the progression represented by
[RT-RTE-insight-save](runtime.md#rt-rte-insight-save); no operative-object counterpart is declared in the supplied runtime.
Evidence passages: see [RT-RTE-insight-save](runtime.md#rt-rte-insight-save) and the task/cleanup passages below.

#### EPI-OBJ-lint-content
Label: Wiki lint report

SRC-1: `src/nemsy/agent.py`. Natural-language diagnostic assertions and suggested actions returned from a model request; response-string substrate. Contradiction/orphan/obsolescence targets differ, but none has an independent formal evaluator in this route. No retained report or installed correction in the handler.
Distinct identity: operative content object, not the progression represented by
[RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint); no operative-object counterpart is declared in the supplied runtime.
Evidence passages: see [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) and the task/cleanup passages below.

#### EPI-OBJ-index-content
Label: Wiki index entries

SRC-1: `src/nemsy/agent.py`. Markdown index mixes navigational [[stem]] identifiers and natural-language summary labels plus date. Filesystem substrate; loader preferentially supplies index to later requests. Label 'summary' or 'query result' denotes provenance category, not acceptance. Repeated appends are not a deduplicated truth registry.
Distinct identity: operative content object, not the progression represented by
[RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); no operative-object counterpart is declared in the supplied runtime.
Evidence passages: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and the task/cleanup passages below.

> entry = f"- [[{stem}]] — {summary_line} （{date.today()}）\n"
> --- `src/nemsy/agent.py`

> [值得进一步探究的问题列表，每条标注：【原文已有线索】或【需外部文献验证】]
> --- `src/nemsy/agent.py`

> 5. 仅当答案是对多个页面的深度综合分析、且结论不能从任何单一页面直接读出时，
>    才在末尾单独一行标注 ARCHIVABLE: true；
>    简单检索、单页引用、或仅整理已有内容不标注
> --- `src/nemsy/agent.py`

### Routes

#### EPI-RTE-summary-cleanup
Label: SUMMARY selection and appendix cleanup
Part of: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)

SRC-1: `src/nemsy/agent.py`, implementation. This is the deterministic text-selection
part of ingestion, not another end-to-end ingestion declaration. Python owns
response-to-page progression: regex selects SUMMARY, removes an enclosing fence,
deletes a heading-matched suffix, and appends separately extracted QUESTIONS.
The caller/model proposal and admission limits are see
[RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest). No semantic oracle
or human review occurs in this cleanup.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned summary string proceeds to the page writer; missing SUMMARY returns None.
- Later read-back: Surviving text reaches later Wiki loads after the enclosing ingest writes it; removed spans are not separately retained by this parser.
- Delegated visibility: inapplicable — local string handling launches no worker or provider call.
- Selection predicate: SUMMARY delimiter and optional QUESTIONS delimiter; full enclosing code fence; suffix beginning at the matched pending-questions heading.
- Invalidation or expiry: inapplicable — transient intermediate string, not an independently versioned object.
- Activation or effect: Enforces textual deletion/recomposition before persistence, not accuracy or premise preservation.
- Evidence limits: Deduction from inspected code, no execution; arbitrary matched suffixes can contain substantive claims.

Concrete input trace, a deduction in the implementation layer: with response
`---SUMMARY---\nA\n## 待探索问题\nB` and no QUESTIONS delimiter,
SUMMARY extraction first yields `A\n## 待探索问题\nB`.
There is no enclosing fence. The first cleanup regex (requiring a separator)
does not match; the second removes the heading and everything following it.
The final saved body is `A`. Thus a real claim represented by B would be lost
by position alone, not judged false. Conversely
`---SUMMARY---\nA\n---QUESTIONS---\nQ` retains A and appends Q under the
questions heading. The route is non-ampliative reshaping/deletion, not a
truth check; no semantic-preservation guarantee follows.

> summary_match = re.search(r"---SUMMARY---\n(.*?)(?=---QUESTIONS---|$)", response, re.DOTALL)
> --- `src/nemsy/agent.py`

> summary_content = re.sub(
>     r"\n{0,2}## 待探索问题\b.*$",
>     "",
>     summary_content,
>     flags=re.DOTALL,
> ).rstrip()
> --- `src/nemsy/agent.py`

> if questions_text:
>     summary_content = summary_content + "\n\n---\n\n## 待探索问题\n\n" + questions_text
> --- `src/nemsy/agent.py`

#### EPI-RTE-citation-display
Label: Answer citation rendering and resolution

SRC-1: `frontend/src/components/MessageContent.tsx`,
`frontend/src/views/Chat.tsx`, `src/nemsy/web.py`, implementation. Distinct from
[RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), which produces answers,
this downstream browser/backend mechanism rewrites link markers, enumerates
references and resolves a requested title to a file. The component returns
reference titles through its callback; the resolver matches lowercased stems.
Direct correction-round inspection confirms Chat's callback opens the resolved
file endpoint in a new tab, which returns current UTF-8 text in JSON subject to
the runtime's bounded lexical Vault check. This supplies inspectability and later
human-facing read-back, not a proposition-to-evidence test. It overlaps
[MEM-RTE-browser-read](memory.md#mem-rte-browser-read) at citation resolution
and file delivery, but separately includes answer-marker rendering; neither
record supersedes the other. Retained generated pages can be
[MEM-OBJ-source-page](memory.md#mem-obj-source-page),
[MEM-OBJ-query-page](memory.md#mem-obj-query-page) or
[MEM-OBJ-insight-page](memory.md#mem-obj-insight-page).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Numbered reference display; resolver returns path metadata or 404; file endpoint returns UTF-8 text.
- Later read-back: Generated source summaries, archived query answers and saved insights can reach a later human browser consumer when a citation resolves to their retained Wiki file; the file endpoint returns current text in JSON. This route need not write content to deliver accumulated material. Viewing arbitrary static source text alone does not establish retained memory.
- Delegated visibility: inapplicable — browser callbacks/HTTP handlers, not a model or worker.
- Selection predicate: All regex-recognized double-bracket titles; deduplicated by trimmed title in appearance order; resolver uses first matching case-insensitive stem.
- Invalidation or expiry: Resolution uses the current list, with no pinned page version or retained historical evidence target.
- Activation or effect: Human can inspect a linked page; rendering does not test reference existence and resolution does not test support or entailment.
- Evidence limits: Direct reads establish marker rendering, Chat callback, resolver and file-content return, not observed interaction, human reliance or source/bundle equivalence. Read-back is conditional on resolution to a retained generated page, not established for every viewable file.

Concrete implementation deduction: `A [[Page]] B [[Page]]` produces one
reference numbered 1; both occurrences become `%%REF:1:Page%%` before
Markdown rendering. Whether Page supports A or B is never an input to these
functions. The same renderer accepts a nonexistent Page, whose later
resolution may return 404.

> const title = match[1].trim()
> if (!seen.has(title)) {
>   seen.set(title, counter++)
> }
> --- `frontend/src/components/MessageContent.tsx`

> return idx !== undefined ? `%%REF:${idx}:${title.trim()}%%` : title.trim()
> --- `frontend/src/components/MessageContent.tsx`

> if note.stem.lower() == target:
>     return {"title": title, "abs_path": str(note), "rel_path": str(note.relative_to(wiki_path))}
> --- `src/nemsy/web.py`

> .then((d) => { if (d?.abs_path) window.open(`/api/file?path=${encodeURIComponent(d.abs_path)}`, '_blank') })
> --- `frontend/src/views/Chat.tsx`

> return {"path": path, "content": p.read_text(encoding="utf-8")}
> --- `src/nemsy/web.py`

#### EPI-RTE-smoke-check
Label: Smoke assertion evaluators

SRC-1: `tests/test_smoke.py`, implementation/test definitions. No counterpart
after comparison with the runtime's routes: it mentions smoke tests but declares
no evaluator record. Tests call ingest and query, then Python assertions assess
paths, existence, metadata, length and answer substrings. Test authors provide
a known source page and question; this is a bounded fixture-based mode, distinct
from open user queries. The expected-answer oracle is weak: query permits any
of DeepSeek, API or 暂无, not an exact reference answer. Ingest's oracle is
structural metadata and length, not correspondence to source assertions.
Archive checking asks for any dated query file and checks the latest one,
not a guaranteed question-specific file. These checks are not an acceptance
criterion for normal application knowledge writes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Assertion pass or pytest failure; tests print diagnostic output.
- Later read-back: Tests write into the configured Wiki and require manual cleanup; generated pages can later be loaded irrespective of assertions.
- Delegated visibility: Live model calls receive fixture source and current Wiki through the ordinary agent routes.
- Selection predicate: Explicit pytest selection or smoke command, not an application admission hook.
- Invalidation or expiry: Fixture source file is removed by cleanup; generated Wiki files require manual cleanup, with no assertion-triggered rollback.
- Activation or effect: A failed assertion stops its test; passing does not independently establish grounded answers or source fidelity.
- Evidence limits: No supplied execution result. Structural checks, permissive disjunction and any-date-file archive lookup cannot establish semantic correctness, causal benefit or complete archive attribution.

> assert "DeepSeek" in result or "API" in result or "暂无" in result
> --- `tests/test_smoke.py`

> assert note.metadata["type"] == "source"
> assert "date" in note.metadata
> assert "tags" in note.metadata
> --- `tests/test_smoke.py`

> query_files = list(queries_dir.glob(f"*{date.today()}.md"))
> --- `tests/test_smoke.py`

#### EPI-RTE-smoke-disposition
Label: Smoke exit-result consumption

SRC-1: `src/nemsy/cli.py`, implementation. Distinct consumer of
[EPI-RTE-smoke-check](#epi-rte-smoke-check): the smoke driver starts pytest,
then prints success on zero or exits 1 otherwise. No counterpart route in
the supplied runtime. Test code decides pass/fail, caller initiates the
bounded smoke invocation and may decide subsequent action; no automatic
product installation/admission or knowledge rollback consumes the result.
The target is this test invocation's exit status, not Wiki truth.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Success message or failure message and process exit 1.
- Later read-back: inapplicable — the driver retains no acceptance artifact or revised policy for later runs.
- Delegated visibility: pytest subprocess runs the selected tests; this is not a model-selected agent delegation.
- Selection predicate: Explicit nemsy-smoke invocation, fixed tests/test_smoke.py.
- Invalidation or expiry: inapplicable — immediate process-result consumption, no persistent accepted status.
- Activation or effect: Changes the command's terminal outcome; no rollback of test-generated Wiki changes.
- Evidence limits: No observed run; a green message's implemented license is only the selected assertion suite.

> if result.returncode == 0:
>     console.print("\n[green]✓ 烟雾测试通过！[/green]")
> else:
>     console.print("\n[red]✗ 烟雾测试失败，请检查输出。[/red]")
>     sys.exit(1)
> --- `src/nemsy/cli.py`

### Claims

#### EPI-CLM-knowledge-accumulation
Label: Continuous accumulation and autonomous induction

SRC-1: `README.md`, `src/nemsy/agent.py`, doctrine/design. README calls Nemsy
a self-building personal knowledge assistant and describes continuous accumulation
and autonomous induction. BASE_SYSTEM requests updating related pages rather
than merely summarizing and asks for contradiction marking. This differs from
[RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding), which limits answers'
information source. In inspected implementation, ingest creates one summary
page and appends index; lint advises rather than automatically applying repairs.
The model can include links/contradiction labels inside that new page, a genuine
partial realization; it has no general arbitrary-page edit execution grant.
“Self-building” is therefore not evidence of exercised self-improvement,
independent truth acceptance or autonomous maintenance of the whole Wiki.

> 本项目基于 Karpathy 的 LLM Wiki 理念，由 DeepSeek 超长上下文模型驱动，以 Obsidian Vault 为知识源，为唯一用户提供持续积累、自主归纳的个人知识服务。
> --- `README.md`

> 1. 知识积累优先：每次摄取新资料都要更新相关 Wiki 页面，不只是生成摘要
> 2. 交叉引用：若内容与已有 Wiki 页面有明确关联，用 [[页面名]] 标注；无需强行寻找关联
> 3. 矛盾标注：用 > ⚠️ 矛盾 格式标注与已有知识相悖的内容
> --- `src/nemsy/agent.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
