---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "BRAN epistemic routes: declared authority, source-byte grounding, document admission and diagnostic feedback without demonstrated semantic warrant."
run-id: AAS-2026-11-08-bran-2be75f1c9e69-01
reviewed-boundary: "7bc428b2ccdfad38e05caa0c0cba2bb19041993a"
---

# BRAN epistemic report

## Source-and-claim boundary

The question is which BRAN outputs license reliance on repository content, which checks actually constrain their use, and whether retained feedback establishes new warranted claims. Scope and external exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). All additional source reads here are SRC-1 at the frozen commit. HEAD was checked against that commit. Implementation deductions below are not target executions.

BRAN's public authority language is consequential: [EPI-CLM-authoritative-files](#epi-clm-authoritative-files) and [EPI-CLM-declared-authority](#epi-clm-declared-authority). Its narrower task boundary is [RT-CLM-evidence-location](runtime.md#rt-clm-evidence-location). The retention claim [RT-CLM-session-retention](runtime.md#rt-clm-session-retention) matters because accepted output can persist even when a host is asked not to retain a session.

| Entry point or operation | Source path, SRC-1 | Coverage and evidence basis |
|---|---|---|
| CLI dispatch, registered mode, query/packet and multi-root | `crates/bran-cli/src/main.rs` | Direct dispatch and excerpt reads; supplied [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) for ranking, packet bounds and policy branches. Direct dispatch confirms additional document, check, evidence, doctor and body-preserved operations, not just connected execution. |
| Connected CLI/TUI, read/search grants, runtime ports | `crates/bran-core/src/agent/coordinator.rs`, `crates/bran-core/src/agent/delegate.rs`, `crates/bran-cli/src/main.rs` | Direct claim validator, fresh-support and completion/publication reads; supplied [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port). Provider dispatch and actual tools remain external; supplied runtime establishes the read/search allowlist, not host confinement. No additional hook-driven epistemic loop is established by these reads. |
| Structural connected library | `crates/bran-core/src/adapters/connected.rs` | Direct complete response-validator and canonicalization reads; supplied [RT-RTE-structural-connected](runtime.md#rt-rte-structural-connected) for invocation and returned-byte rejection/fallback. |
| SQZ | `crates/bran-core/src/adapters/sqz.rs` | Direct fidelity predicate, candidate rejection and byte-benefit selection reads; [EPI-RTE-sqz-check](#epi-rte-sqz-check). External compressor not frozen: semantic preservation cannot be established. |
| Document inspect, query/packet addition | `crates/bran-document/src/admit.rs`, `crates/bran-cli/src/document_evidence.rs`, `crates/bran-cli/src/main.rs` | Direct admission, fidelity, budgets, discovery, anchor rank and inspect-return reads; [EPI-RTE-document-admit](#epi-rte-document-admit). Native parser internals not audited here: parser-wide fidelity/conformance is not concluded. |
| Check and strict revalidation | `crates/bran-core/src/profile.rs`, `crates/bran-cli/src/main.rs` | Direct profile floor/optional-family rules and CLI check-result consumer; [EPI-RTE-profile-check](#epi-rte-profile-check). Full strict-rule implementation not audited; no exhaustive strict-conformance judgment. Maintenance/rollback supplied by [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply). |
| Evidence summarize/propose/replay/clear | `crates/bran-cli/src/main.rs` | Direct gap collection, null replacement/authority proposals, ranking comparison and clear reads; [EPI-RTE-evidence-summary](#epi-rte-evidence-summary), [EPI-RTE-evidence-replay](#epi-rte-evidence-replay). Record write/read mechanism supplied by [RT-RTE-query-packet](runtime.md#rt-rte-query-packet); no peer memory report supplied. |
| Body-preserved | `crates/bran-core/src/migration.rs`, `crates/bran-cli/src/main.rs` | Direct comparison and report-to-exit reads; [EPI-RTE-body-preserved](#epi-rte-body-preserved). Frontmatter stripper internals not audited: judgment is bounded to the compared stripped bodies. |
| Doctor, agents list, help/version/smoke | `crates/bran-cli/src/main.rs` | Direct dispatch and doctor readiness reads; [EPI-RTE-doctor-readiness](#epi-rte-doctor-readiness). Listings/static identity outputs are not semantic claim evaluation. No target command was invoked. |
| Settings Apply and get | `crates/bran-cli/src/main.rs`, `crates/bran-tui/src/settings.rs` | Supplied [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply), [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), not an independent full store/settings audit. |
| Shipped skill, deployment, CI/benchmarks, export/database/derived-state, SCIP, release and cloud attestation fixtures | Paths inventoried in [boundary](boundary.md#boundary-and-evidence) | Skill/deployment and SCIP limits supplied by runtime/boundary. Detailed CI, export, database, derived-state, release and cloud-evaluator routes unassessed here. Their effects on conformance, production admission and empirical warrant remain unresolved. They prevent a system-complete negative about all possible evaluation or acceptance routes. |

No observed run or causal experiment is registered. This prevents claims of exercised acceptance, actual host/tool compliance, retrieval benefit or causal improvement. No trace ties retained connected answers to subsequent task behavior. Provider weights and exact resolved model versions remain uninspected, as [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) specifies. External compressor internals prevent deciding semantic preservation of compressed prose. Available but uninspected evaluator/parser/export material is not an access gap or evidence of absence.

## Epistemic-object inventory

Fields owned by cited declarations are not redefined here.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet) | Selected repository assertions where present; locator/accounting text alone need not assert domain facts | see record | SRC-1 `crates/bran-core/src/packet/mod.rs` | Delivery is not endorsement; not every selected file is semantically relevant. |
| [RT-OBJ-packet-receipt](runtime.md#rt-obj-packet-receipt) | Assertions about selection, omission and byte/token estimates | see record | SRC-1 `crates/bran-core/src/packet/mod.rs` | Accounting domain, not truth of selected prose; estimate is not measured provider tokens. |
| [EPI-OBJ-provider-claims](#epi-obj-provider-claims) | Claim text, supporting text and source associations | Grounded answer | SRC-1 `crates/bran-core/src/agent/coordinator.rs` | Materiality is required as a flag; semantic truth and completeness remain unchecked by byte equality. |
| [EPI-OBJ-structural-response](#epi-obj-structural-response) | Model claim text and claimed usages | Structural response; see record | SRC-1 `crates/bran-core/src/adapters/connected.rs` | Packet identity consistency is not semantic entailment. |
| [EPI-OBJ-document-anchors](#epi-obj-document-anchors) | Parsed document assertions where text is truth-apt, plus locator/digest/fidelity data | Admitted evidence | SRC-1 `crates/bran-document/src/admit.rs` | Format normalization and omissions differ; fidelity labels do not authenticate source assertions. |
| [EPI-OBJ-evidence-gaps](#epi-obj-evidence-gaps) | Propositions about recorded requests, current inventory and retrieval differences | Maintenance diagnostics | SRC-1 `crates/bran-cli/src/main.rs` | A missed term is not proof knowledge is false or missing; selection history is not an answer oracle. |
| [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) | Not determinable at parameter level; generated content assessed at the output edge instead | see record | SRC-1 `crates/bran-core/src/adapters/provider/mod.rs` | External numerical state and its mutability unresolved. |
| [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply) | None required: typed invocation policy | see record | SRC-1 `crates/bran-tui/src/settings.rs` | Not evidence-driven truth acceptance. |
| [EPI-RTE-profile-check](#epi-rte-profile-check), [EPI-RTE-body-preserved](#epi-rte-body-preserved), [EPI-RTE-doctor-readiness](#epi-rte-doctor-readiness) | Local conformance, stripped-body equality and readiness propositions respectively | Diagnostic outputs; see records for forms/substrates | SRC-1 `crates/bran-core/src/profile.rs`, `crates/bran-core/src/migration.rs`, `crates/bran-cli/src/main.rs` | Different domains; none is a general correctness evaluator. |

## Authority-route ledger

Architectural status is about inspected wiring, not exercised behavior. Each row is a separate epistemic function even when it cites a container route shared with another row. “See” delegates generic implementation fields to the declaring record; epistemic license is assessed here. No ledger row claims observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) | content transformation | implemented | [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet) | truth-apt transformation: acquisition/import | Repository text into evidence selection | see route | see route | see route | see route | Source attribution retained; source truth warrant unknown | see route | see [RT-BAP-evidence-supply](runtime.md#rt-bap-evidence-supply) | SRC-1 `crates/bran-cli/src/main.rs` | [EPI-CLM-authoritative-files](#epi-clm-authoritative-files) | Selection is not verification | No exhaustive relevance guarantee |
| [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) | content transformation | implemented | [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet) | truth-apt transformation: non-ampliative reshaping | Optional UTF-8-safe prefix excerpt | Code slices body after metadata header | Per excerpt option and public/safe metadata; see route | Prefix, possibly incomplete sentence | Context-byte reduction, no semantic veto | Byte-preserving selection of a prefix only, not preservation of every proposition's scope | see route | see [RT-BAP-evidence-supply](runtime.md#rt-bap-evidence-supply) | SRC-1 `crates/bran-cli/src/main.rs` | none | Truncation can remove a necessary condition | Concrete deduction in bounded conclusion |
| [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) | operational admission/selection/consumption | implemented | [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet) | no content change | Relevance/declared priority and bounded delivery | see route | see route | see route | Ranking and bounds, not truth veto | License to inspect candidate files, not to assume their correctness | see route | see [RT-BAP-evidence-supply](runtime.md#rt-bap-evidence-supply) | SRC-1 `crates/bran-cli/src/main.rs` | [EPI-CLM-declared-authority](#epi-clm-declared-authority) | Declared authority is input to selection | Inherited metadata may be wrong |
| [EPI-RTE-document-admit](#epi-rte-document-admit) | check/evidence production | implemented | [EPI-OBJ-document-anchors](#epi-obj-document-anchors) | truth-apt transformation: acquisition/import | Format projection, emitted text and locator | see route | see route | see route | Typed refusal/eligibility checks | Bounded envelope admissibility with explicit normalization/omission; source warrant unknown | see route | Query/packet code, admitted anchors, enforcing eligibility, current invocation | SRC-1 `crates/bran-document/src/admit.rs` | none | Admitted is not true | Parser correctness not fully audited |
| [EPI-RTE-document-admit](#epi-rte-document-admit) | disposition/acceptance | implemented | [EPI-OBJ-document-anchors](#epi-obj-document-anchors) | no content change | Eligibility for query/packet or inspect return | see route | see route | see route | Enforcing evidence eligibility | Operational acceptance for evidence transport, not acceptance of source claims as knowledge | see route | CLI caller gets envelope/refusal; refusal may have exit zero; current invocation | SRC-1 `crates/bran-cli/src/main.rs` | none | Exit success is not admission | No model or human semantic approval required |
| [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) | content transformation | implemented | [EPI-OBJ-provider-claims](#epi-obj-provider-claims) | truth-apt transformation: indeterminate | Provider production before validation | External model; see route | see route | see route | Candidate production | No warrant from fluency or claim flag | see route | Provider output into runtime validator, candidate-only, current attempt | SRC-1 `crates/bran-core/src/agent/coordinator.rs` | [RT-CLM-evidence-location](runtime.md#rt-clm-evidence-location) | none | Without concrete input/output, copied versus novel content unresolved |
| [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) | check/evidence production | implemented | [EPI-OBJ-provider-claims](#epi-obj-provider-claims) | no content change | Answer/claims/citations and fresh support | see route | see route | see route | Enforcing source-byte and surface predicates | Claim text occurs in unchanged admitted source; does not establish source truth, inference validity or relevance | see route | Validator to completion branch, Boolean veto, current attempt | SRC-1 `crates/bran-core/src/agent/delegate.rs` | none | Grounding is narrower than truth | Substrings need not be whole propositions |
| [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) | disposition/acceptance | implemented | [EPI-OBJ-provider-claims](#epi-obj-provider-claims) | no content change | Completion after checks and storage | see route | see route | see route | Incomplete versus complete receipt | Acceptance criterion is source support and protocol validity for evidence return, not established novel ampliative knowledge | see route | Completion code, inline receipt/store, enforcing return gate, current invocation | SRC-1 `crates/bran-core/src/agent/coordinator.rs` | none | Not a semantic answer oracle | Grounded output SQZ must be byte-identical |
| [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) | retention | implemented | [EPI-OBJ-provider-claims](#epi-obj-provider-claims) | no content change | Accepted inline output/artifacts into local store | see route | see route | see route | Completion depends on store success | Retained source-supported result, not new warrant | see route | Store/get, canonical bytes and digests, permissive later retrieval, bounded store horizon | SRC-1 `crates/bran-core/src/agent/coordinator.rs` | [RT-CLM-session-retention](runtime.md#rt-clm-session-retention) | No-session does not disable local publication | No automatic next-prompt injection established |
| [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port) | disposition/acceptance | implemented | [EPI-OBJ-provider-claims](#epi-obj-provider-claims) | no content change | Generic completion without grounding contract | see route | see route | see route | Grounding predicates return true when absent | No fresh-source support license on that alternate path | see route | Caller-supplied ports/store, permissive API, caller-defined horizon | SRC-1 `crates/bran-core/src/agent/coordinator.rs` | none | Production CLI guarantee is not universal | Actual caller policy unresolved |
| [RT-RTE-structural-connected](runtime.md#rt-rte-structural-connected) | check/evidence production | implemented | [EPI-OBJ-structural-response](#epi-obj-structural-response) | no content change | Structural claim/citation/usage associations | see route | see route | see route | Structural veto | Identity/coverage consistency only; usage support need only be nonempty, not shown entailed | see route | Validator into returned-byte selection, enforcing gate, current call | SRC-1 `crates/bran-core/src/adapters/connected.rs` | none | Different validator from fresh-byte CLI path | Concrete packet/response required to classify generated content |
| [RT-RTE-structural-connected](runtime.md#rt-rte-structural-connected) | disposition/acceptance | implemented | [EPI-OBJ-structural-response](#epi-obj-structural-response) | no content change | Canonical response bytes | see route | see route | see route | Rejection returns no accepted bytes, but raw response remains in outcome | Structural acceptance for return, not proven semantic acceptance | see route | Outcome consumer, accepted bytes versus separately exposed response/original bytes, current call | SRC-1 `crates/bran-core/src/adapters/connected.rs` | none | Suppression is not destruction of raw candidate | Caller must respect channels |
| [EPI-RTE-sqz-check](#epi-rte-sqz-check) | check/evidence production | implemented | [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet) | no content change | Compressed candidate | see route | see route | see route | Anchor/DLP/bound veto | Specified substrings retained; not general semantic equivalence | see route | Adapter to parent coordinator, receipt gate, current compression | SRC-1 `crates/bran-core/src/adapters/sqz.rs` | none | “Fidelity” checks anchors | Unanchored prose remains semantically unverified |
| [EPI-RTE-sqz-check](#epi-rte-sqz-check) | operational admission/selection/consumption | implemented | [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet) | truth-apt transformation: indeterminate | Smaller validated candidate versus original | see route | see route | see route | Byte-size selection; parent-specific failure handling | Unknown preservation beyond anchors; compression is not acceptance of source claims | see route | Packet/connected caller, replacement payload, enforcing byte selection, current invocation | SRC-1 `crates/bran-core/src/adapters/sqz.rs` | none | NotBeneficial means bytes, not task utility | Grounded output additionally forbids any answer change |
| [EPI-RTE-profile-check](#epi-rte-profile-check) | check/evidence production | implemented | Diagnostic result; see record | truth-apt transformation: entailed derivation | Profile conformance over scanned bundle | see route | see route | see route | Diagnostic and exit signal | Local syntax/shape/policy result, conditional on parser/encoding; no source truth license | see route | CLI automation, JSON/exit, enforcing command status; repair has separate gate | SRC-1 `crates/bran-core/src/profile.rs` | none | Verified metadata is shape-checked | Optional trust family may be absent |
| [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply) | disposition/acceptance | implemented | Replacement file bytes; see record | truth-apt transformation: indeterminate | File mutation | see route | see route | see route | Authorization/staleness/strict-validator veto and rollback | Strict-valid replacement for fixture scope, not proof of improved knowledge | see route | Repair coordinator to disk and later scans, enforcing mutation gate, persists until replaced | SRC-1 `crates/bran-core/src/repair/mod.rs` | none | Authority token is assertion | No automatic semantic criticism or production self-repair inferred |
| [EPI-RTE-evidence-summary](#epi-rte-evidence-summary) | check/evidence production | implemented | [EPI-OBJ-evidence-gaps](#epi-obj-evidence-gaps) | truth-apt transformation: entailed derivation | Recorded terms/rankings versus inspected inventory | see route | see route | see route | Diagnostic only | Bounded retrieval-history and metadata gaps, not truth error diagnoses | see route | CLI caller, JSON candidates with null replacement/authority, advisory, next manual/caller action | SRC-1 `crates/bran-cli/src/main.rs` | none | Proposal is not an admitted update | No automatic repair consumer in this function |
| [EPI-RTE-evidence-replay](#epi-rte-evidence-replay) | check/evidence production | implemented | [EPI-OBJ-evidence-gaps](#epi-obj-evidence-gaps) | truth-apt transformation: entailed derivation | Recorded versus current rankings/outcome | see route | see route | see route | Difference report only | Change detection; no reference answer or improvement ranking | see route | CLI caller, JSON differences, advisory, current replay | SRC-1 `crates/bran-cli/src/main.rs` | none | Changed need not mean better | It does not overwrite recorded baseline |
| [EPI-RTE-body-preserved](#epi-rte-body-preserved) | check/evidence production | implemented | Stripped-body comparison report; see record | truth-apt transformation: entailed derivation | Original/migrated stripped bytes | see route | see route | see route | Pass/fail command status | Equality within manifest/stripper domain only | see route | CLI automation, report/exit, enforcing command status, current check | SRC-1 `crates/bran-core/src/migration.rs` | none | Preservation is not correctness | Original bytes are not a truth oracle |
| [EPI-RTE-doctor-readiness](#epi-rte-doctor-readiness) | check/evidence production | implemented | Readiness report; see record | truth-apt transformation: entailed derivation | Local configured capability surfaces | see route | see route | see route | Readiness/warning status | Local setup evidence, explicitly not connected-execution attestation | see route | Operator, JSON/exit, advisory readiness, until configuration changes | SRC-1 `crates/bran-cli/src/main.rs` | none | Ready-to-attempt is not executed | External host not tested |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-authoritative-files](#epi-clm-authoritative-files) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) | None registered | No relevance intervention or task comparison | Deterministic ranking exposes reasons and selected evidence | “Authoritative” cannot be read as independently verified truth or guaranteed right files |
| [EPI-CLM-declared-authority](#epi-clm-declared-authority) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [EPI-RTE-profile-check](#epi-rte-profile-check) | None registered | Metadata selection/conformance is not validation of declaring source | Declared authority is used, alongside text/path matching | Imported declarations may carry unknown warrant |
| [RT-CLM-evidence-location](runtime.md#rt-clm-evidence-location) | see record | SRC-1 `skill/use-bran/SKILL.md`, doctrine/design | see record | [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) | None registered | Outer agent decisions excluded | Evidence-returning purpose fits inspected default routes | Outer agent's reasoning/changes not established |
| [RT-CLM-session-retention](runtime.md#rt-clm-session-retention) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) | None registered | Host echo not independent retention audit | Host session request is distinct from unconditional BRAN-local result publication | Broad no-retention reading contradicted by local store path |

## Bounded conclusion

**Repository evidence is acquired and ranked, not made true by ranking.** [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) establishes bounded source selection and delivery; [RT-BAP-evidence-supply](runtime.md#rt-bap-evidence-supply) names the advisory consumer path. Attribution and digests preserve inspectable lineage, but the source's warrant remains unknown. File authority declarations and matching scores supply selection priorities, not an independent evaluation of the assertions. The public claims therefore support evidence location, not assured semantic authority.

There is a concrete limit to deterministic reshaping. From the inspected `public_safe_excerpt` implementation, take a source whose metadata declares `public_boundary: safe` and whose body after the header is exactly “Access is allowed only for admins.” With an excerpt limit of 17 bytes, the source slice returned is “Access is allowed”. All characters are ASCII, so the UTF-8 adjustment does nothing. This is a source-code deduction, not an executed fixture. The prefix preserves bytes but removes the necessary restriction; semantic equivalence of the displayed proposition does not follow. [EPI-OBJ-provider-claims](#epi-obj-provider-claims) also records why matching arbitrary source substrings does not necessarily preserve complete claims. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/delegate.rs`.

> while !source.is_char_boundary(end) {
>     end -= 1;
> }
> Some(source[..end].to_owned())
> --- `crates/bran-cli/src/main.rs`

**Grounded completion has a real, narrow veto.** [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) and [EPI-OBJ-provider-claims](#epi-obj-provider-claims) establish acceptance for evidence return: nonempty admitted citations, exact answer reconstruction, material flags, claim/support equality, current file digest and support occurrence, protocol/surface checks, accepted compression and successful storage. This licenses the statement that the text is supported by current admitted file bytes. It does not license source truth, completeness, a checked explanation or an accepted ampliative inference. Arbitrary provider generation is an indeterminate transformation before that gate; accepted grounded text is constrained to source quotations. A new semantic synthesis cannot simply pass as paraphrase under exact text/support equality. The generic no-contract API and structural-citation API are source-supported counterexamples to generalizing this fresh-byte guarantee across BRAN.

**Other checks have different domains and forces.** Document admission licenses eligible projections for delivery, retains fidelity/derivation distinctions and refuses unusable text; it is not semantic endorsement. SQZ verifies required substrings, DLP and output bounds, and selects fewer bytes; unanchored semantic fidelity remains unknown. Profile checks derive conformance results, body-preserved derives stripped-byte equality, doctor derives local readiness, and replay derives differences. Their output is truth-apt within those local domains given correct parsing and premises; none supplies an expected correct outer-task answer. [EPI-RTE-document-admit](#epi-rte-document-admit), [EPI-RTE-sqz-check](#epi-rte-sqz-check), [EPI-RTE-profile-check](#epi-rte-profile-check), [EPI-RTE-body-preserved](#epi-rte-body-preserved), [EPI-RTE-doctor-readiness](#epi-rte-doctor-readiness), [EPI-RTE-evidence-replay](#epi-rte-evidence-replay).

**Retention and change are not automatically acceptance or integration.** Connected results can be stored and explicitly retrieved even with no-session requested. Recorded queries feed gap summaries and replay; proposals explicitly leave replacement and authority null. These findings establish diagnostic feedback, not a closed automatic correction loop or evidence-consuming acceptance of new knowledge. Settings and explicit-authority repair can alter later invocation policy or repository bytes, with software vetoes and bounded recovery as runtime describes. They do not thereby establish improved capacity, autonomous theory criticism or successful self-improvement. No lifecycle integration of accepted ampliative claims was established in these inspected routes; unassessed evaluator/export/derived-state paths prevent a whole-system absence claim. Learning, reflection, autonomy and self-improvement remain independent questions, not a bundled negative. No observed run licenses claims of exercised reliance or benefit. See [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply), [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply), [EPI-RTE-evidence-summary](#epi-rte-evidence-summary).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-provider-claims
Label: Provider claim parts

Source-native identity: `ProviderOutput` claim text/support/locator/digest. Form: natural-language text with symbolic associations, held in Rust structs and optionally stored as inline bytes. This output is distinct from the model and input packet: closest supplied records are [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) and [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port). The generic path can omit the production grounding contract, as the ledger distinguishes. No supplied operative object names these output parts.

Production grounded output requires exact claim/support equality and answer reconstruction; supplied [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) retains that passage. Additional implementation evidence, SRC-1 `crates/bran-core/src/agent/delegate.rs`, shows support occurrence is a substring test, not parsing of a whole proposition:

> if !bytes
>     .windows(support.len())
>     .any(|candidate| candidate == support.as_bytes())
> {
>     return false;
> }
> --- `crates/bran-core/src/agent/delegate.rs`

#### EPI-OBJ-structural-response
Label: Structural response claims

Part of: [RT-RTE-structural-connected](runtime.md#rt-rte-structural-connected)

Source-native identity: `ConnectedResponse` claim, citation and usage parts; natural-language assertions/support with symbolic IDs and locators, held in memory and canonical returned bytes. The parent is a route: this is its proposed response object, not the complete invocation. Distinct from [EPI-OBJ-provider-claims](#epi-obj-provider-claims), this has a structural-packet evaluator, a different response type and no built-in result-store consumer.

Structural usage validation requires nonempty bounded support plus packet identity matching. It does not compare usage support to excerpt bytes or relate its meaning to a claim. SRC-1 `crates/bran-core/src/adapters/connected.rs`:

> || usage.support.trim().is_empty()
> || usage.support.len() > MAX_TEXT
> --- `crates/bran-core/src/adapters/connected.rs`

#### EPI-OBJ-document-anchors
Label: Admitted document anchors

Source-native identity: `Admitted`, `EvidenceAnchor` and envelope; natural-language parsed text plus symbolic locators, digests, derivation and fidelity. Storage is in-memory projection/envelope and emitted JSON, not a retained document database in the inspected path. Distinct from [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet): enterprise evidence is appended separately and has its own parser/admission/anchor-ranking consumers. SRC-1 `crates/bran-document/src/admit.rs`, `crates/bran-cli/src/document_evidence.rs`.

> pub struct Admitted {
>     pub envelope: Json,
>     pub anchors: Vec<EvidenceAnchor>,
>     pub fidelity: Json,
> }
> --- `crates/bran-document/src/admit.rs`

DOCX envelope fidelity deliberately marks some features unsupported; labels do not imply unqualified preservation:

> ("macros".to_owned(), Json::Str("unsupported".to_owned())),
> ("paragraphs".to_owned(), Json::Str("normalized".to_owned())),
> ("tables".to_owned(), Json::Str("normalized".to_owned())),
> ("text".to_owned(), Json::Str("normalized".to_owned())),
> --- `crates/bran-document/src/admit.rs`

#### EPI-OBJ-evidence-gaps
Label: Evidence gap and replay diagnostics

Source-native identity: `EvidenceGapSummary`, proposal candidates and replay JSON. Symbolic sets/maps/arrays express truth-apt claims about retrieval history, inventory and differences. Storage: current invocation Rust values and JSON output; inputs reload query records from disk. Distinct from [RT-OBJ-packet-receipt](runtime.md#rt-obj-packet-receipt): this concerns accumulated queries and present repository coverage, not one packet's accounting. Closest supplied route [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) records the persistence precursor.

SRC-1 `crates/bran-cli/src/main.rs`; gap categorization does not establish why a document was never retrieved:

> if !retrieved.contains(&identity) {
>     never_retrieved.insert(identity);
> }
> --- `crates/bran-cli/src/main.rs`

### Routes

#### EPI-RTE-document-admit
Label: Document projection admission

Compared with [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), this isolates native-document admission rather than Markdown ranking. It also serves the separate document-inspect entry point, so its complete referent is not contained in that supplied route.

CLI document inspect or document discovery to adapter import, projection decoding, budgets, envelope validation and query/packet eligibility. Software owns rejection and anchor selection; caller supplies source, not mandatory human semantic approval. Natural-language source text is imported, not conjectured by the admission layer. SRC-1 `crates/bran-document/src/admit.rs`, `crates/bran-cli/src/document_evidence.rs`, `crates/bran-cli/src/main.rs`.

- Immediate return: Envelope with anchors/fidelity, or typed refusal; inspect emits refused status with successful command exit.
- Later read-back: inapplicable — admission itself persists no accumulated content; a later query reimports current documents.
- Delegated visibility: Outer agent receives separately appended admitted evidence; no model called by admission.
- Selection predicate: Registered format adapter; import succeeds without DLP/public-boundary refusal; recognized projection and nonempty budgeted anchors; emitted locator/text validation and built-envelope validation. Embedded matches rank by term score; OCR-derived matches are labelled and unranked.
- Invalidation or expiry: inapplicable — no retained admission artifact; current file import replaces the current invocation's view.
- Activation or effect: Eligibility for transport and bounded query/packet evidence delivery; no source-truth decision.
- Evidence limits: Parser internals not comprehensively audited; fidelity and truncation are explicit rather than full semantic preservation. Operation unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let (anchors, fidelity, processor) =
>     read_projection(format, &projection).ok_or(Refusal::UnsupportedContainer)?;
> let (anchors, omitted_anchors, mut omitted_bytes) = apply_anchor_budgets(anchors);
> if anchors.is_empty() {
>     return Err(Refusal::NoAdmissibleText);
> }
> --- `crates/bran-document/src/admit.rs`

#### EPI-RTE-sqz-check
Label: SQZ fidelity and byte selection

Distinct identity across [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) and [RT-RTE-structural-connected](runtime.md#rt-rte-structural-connected): this is their shared compression predicate/selection mechanism, not any complete invocation.

Packet and preservation anchors to configured compressor candidate, output checks and original-or-candidate selection. Code judges bounded output, required substring anchors and DLP; then smaller byte count, not semantic utility. Representation is prose payload plus symbolic receipt in memory. No expected-answer oracle. SRC-1 `crates/bran-core/src/adapters/sqz.rs`.

- Immediate return: Evaluation packet and receipt, or error. Candidate no smaller than original returns original with NotBeneficial; missing anchors/DLP fail; parent path determines incomplete versus fallback.
- Later read-back: inapplicable — adapter itself retains no history; a parent may store accepted output.
- Delegated visibility: Compressor receives selected payload; later model/outer caller receives parent-selected packet.
- Selection predicate: Enabled adapter and approved configured compressor, nonconflicting/present anchors, bounded DLP-safe candidate and every required anchor substring. Byte reduction selects candidate.
- Invalidation or expiry: inapplicable — candidate and receipt belong to this call, not an expiring store.
- Activation or effect: May replace delivered context; grounded runtime output has an additional exact-answer equality gate. Structural parent instead falls back to original on SQZ failure.
- Evidence limits: Anchor occurrence does not prove equivalent meaning, retention of unanchored clauses or improved task outcome; actual compressor implementation and operation uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if anchors.is_empty() {
>     return (FidelityStatus::RequiredButUnavailable, Vec::new());
> }
> let missing = anchors
>     .iter()
>     .filter(|anchor| !output.contains(anchor.value()))
>     .map(|anchor| anchor.id().to_owned())
>     .collect::<Vec<_>>();
> --- `crates/bran-core/src/adapters/sqz.rs`

> if candidate_bytes >= raw_bytes {
> --- `crates/bran-core/src/adapters/sqz.rs`

#### EPI-RTE-profile-check
Label: Profile conformance check

No supplied route declares the ordinary check evaluator. Closest [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply) consumes strict revalidation, but ordinary check also returns directly without mutation.

Requested profile and scan-derived Bundle to ProfileValidator outcomes, public-boundary diagnostics, selected result and command status. Code evaluates syntax/metadata and policy, not domain truth. Outcomes are symbolic in-memory structs/JSON; conformance propositions are entailed under the implemented parser/rules. SRC-1 `crates/bran-core/src/profile.rs`, `crates/bran-cli/src/main.rs`.

- Immediate return: Profile diagnostics, selected_passed, status and exit code.
- Later read-back: inapplicable — ordinary check retains no accumulated result in the inspected function.
- Delegated visibility: inapplicable — no model delegation by this evaluator.
- Selection predicate: Caller selects profile; policy and scanned bundle supply constraints. v0.2 optional families are checked only when present; strict has additional repository rules. Code can fail command, not automatically withdraw arbitrary existing knowledge.
- Invalidation or expiry: inapplicable — no retained acceptance certificate; recheck rescans current repository.
- Activation or effect: CLI exit/status changes on selected pass, failure or unknown profile; fixture repair separately consumes strict pass under its own authorization/rollback mechanism.
- Evidence limits: Not every strict rule audited; a verified metadata mapping is shape information, not independent verification of its claimed verifier. No observed conformance result.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> /// - Optional families are shape-validated only when present: `sources` /
> ///   `usage_window` (provenance), `generated` / `verified` (trust),
> --- `crates/bran-core/src/profile.rs`

> let status = if vres.selected_profile_error.is_some() {
>     "error"
> } else if vres.selected_passed() {
>     "ok"
> } else {
>     "failed"
> };
> --- `crates/bran-cli/src/main.rs`

#### EPI-RTE-evidence-summary
Label: Evidence gap summary and proposals

No counterpart among supplied declarations: [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) supplies recorded inputs but does not declare this diagnostic consumer.

Persisted QueryEvidenceRecord values plus live bundle inventory to gap summary or diagnostic candidates. Code unions unanswered terms, identifies path-only and never-retrieved documents, missing locators/unavailable roots, stale metadata and unclassified documents. It returns suggestions without authored replacement. SRC-1 `crates/bran-cli/src/main.rs`.

- Immediate return: Read-only summary or candidates, each with null replacement and authority.
- Later read-back: Loads accumulated query records; results themselves are not persisted or automatically applied by these functions.
- Delegated visibility: CLI caller receives JSON; no model or maintainer called automatically.
- Selection predicate: Explicit evidence summarize/propose; recorded request/rank inputs and current inspected bundle views define diagnostic categories.
- Invalidation or expiry: Clear explicitly removes the evidence store; missing locator/unavailable root/stale metadata are diagnostic, not automatic withdrawal of file claims.
- Activation or effect: Advisory gap reporting. Caller must decide what to propose, write and authorize; maintain apply is a separate gate.
- Evidence limits: No independent reference answers or evidence of semantic error, useful revision, automatic adaptation or improved retrieval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "{{\"kind\":\"unanswered_term\",\"target\":null,\"term\":\"{}\",\"replacement\":null,\"authority\":null}}",
> --- `crates/bran-cli/src/main.rs`

#### EPI-RTE-evidence-replay
Label: Recorded query replay comparison

No counterpart among supplied declarations: [RT-RTE-query-packet](runtime.md#rt-rte-query-packet) records original query evidence, not this replay comparator.

Recorded queries to current evaluation, then outcome/ranking diff and difference_count; code owns evaluation and comparison. Results are symbolic JSON. The old result is a baseline, not a correct-answer oracle. SRC-1 `crates/bran-cli/src/main.rs`.

- Immediate return: Per-request changed/added/removed rankings, changed outcomes and count. Re-evaluation failure becomes unavailable current outcome.
- Later read-back: Reads recorded requests/rankings for replay; does not rewrite baseline or ranking policy in this function.
- Delegated visibility: Caller receives diffs, not an automatic delegated critic.
- Selection predicate: Explicit evidence replay, each stored request and requested roots; comparator tests identity/payload and outcome equality.
- Invalidation or expiry: inapplicable — replay result not persisted here; evidence clear can remove its input store.
- Activation or effect: Only diagnostic return; difference_count records change, not acceptance/rejection of a successor.
- Evidence limits: No task quality metric, semantic correctness oracle or component-varying experiment; no operation observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let diffs = ranking_differences(&record.rankings, &current.rankings);
> let outcome_changed = record.outcome != current.outcome;
> if outcome_changed || !diffs.is_empty() {
>     difference_count += 1;
> }
> --- `crates/bran-cli/src/main.rs`

#### EPI-RTE-body-preserved
Label: Manifest body preservation check

No supplied record counterpart. Unlike [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply), this reports a read-only comparison, not an authorized file transaction.

Manifest pairs to safe reads, UTF-8 check, frontmatter stripping, body hashes, equality and findings, then CLI status/exit. Code evaluates the proposition that stripped bodies are byte-equal and optional original digest matches. Symbolic report in memory/JSON. SRC-1 `crates/bran-core/src/migration.rs`, `crates/bran-cli/src/main.rs`.

- Immediate return: BodyPreservedReport with files/findings/passed, or bounded read/manifest error; CLI pass/fail exit.
- Later read-back: inapplicable — this check retains no result or modified document.
- Delegated visibility: inapplicable — no model delegation.
- Selection predicate: Explicit body-preserved command and manifest; safe paths, size limits, valid optional hash, UTF-8 and exact compared-body equality.
- Invalidation or expiry: inapplicable — report describes current read, with no persisted endorsement or expiry.
- Activation or effect: Command fails on findings; no automatic rollback/admission consumer found in this CLI function.
- Evidence limits: Only manifest pairs and stripped-body domain; equal false assertions remain false. Stripper internals and downstream CI use not fully audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let preserved = orig_body == mig_body;
> if !preserved {
> --- `crates/bran-core/src/migration.rs`

> passed: findings.is_empty(),
> --- `crates/bran-core/src/migration.rs`

#### EPI-RTE-doctor-readiness
Label: Local readiness diagnosis

No supplied declaration names this evaluator. Closest [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply) supplies retained configuration, not readiness or execution attestation.

Settings/skill/packet and capability checks to local readiness report. Code is evaluator, domain is local setup, not actual provider operation. Symbolic booleans/status/JSON in memory. SRC-1 `crates/bran-cli/src/main.rs`.

- Immediate return: Local readiness/ready-to-attempt and warnings; connected_execution_ready remains false, host_attestation unavailable.
- Later read-back: Loads retained settings for diagnosis, but retains no new result; configuration consumer is already [RT-BAP-settings-consumption](runtime.md#rt-bap-settings-consumption).
- Delegated visibility: inapplicable — diagnosis initializes no provider call in the inspected function.
- Selection predicate: Explicit doctor mode; local setup predicates and capability probe. Onboarding and agent modes use different readiness definitions.
- Invalidation or expiry: inapplicable — no durable readiness decision; later invocation checks current setup.
- Activation or effect: Operator guidance and command warning/exit; does not certify provider execution or admit a learned policy.
- Evidence limits: Packet-round-trip internals not audited here; readiness capacity does not show exercised or beneficial operation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let ready_to_attempt = local_setup_ready && connected_agent_runtime;
> let connected_execution_ready = false;
> --- `crates/bran-cli/src/main.rs`

### Claims

#### EPI-CLM-authoritative-files
Label: Authoritative files for a question

Claimed operation: BRAN identifies which files are authoritative for a question. SRC-1 `README.md`, doctrine/design, not a retrieval-quality experiment. Distinct from [RT-CLM-evidence-location](runtime.md#rt-clm-evidence-location): this is the stronger authority assertion rather than division of task ownership.

> BRAN answers "which files are authoritative for this question,"
> ranked, with the reason attached.
> --- `README.md`

#### EPI-CLM-declared-authority
Label: Ranking on declared authority

Claimed operation: declarations rather than guesses ground ranking. SRC-1 `README.md`, doctrine/design. Distinct from [RT-CLM-evidence-location](runtime.md#rt-clm-evidence-location) and [EPI-CLM-authoritative-files](#epi-clm-authoritative-files): names the purported ranking basis, not task ownership or relevance outcome.

> BRAN ranks on declared authority, not guesswork.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; paths for new diagnostics are carried by their route records and the ledger, while supplied evidence/settings consumers remain [RT-BAP-evidence-supply](runtime.md#rt-bap-evidence-supply) and [RT-BAP-settings-consumption](runtime.md#rt-bap-settings-consumption).
