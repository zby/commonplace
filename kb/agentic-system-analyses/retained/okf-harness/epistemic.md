---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OKF Harness epistemic routes: source acquisition, agent synthesis, structural checks, evidence withholding and retained-answer authority."
run-id: AAS-2026-10-15-okf-harness-6bf5507fbdbf-01
reviewed-boundary: "0dd4f806c454a68088c5a3e64b4cbebbe2c216be"
---

# OKF Harness epistemic report

## Source-and-claim boundary

The question is what licenses later reliance on this agent-maintained wiki. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers: see its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. The external agent owns semantic synthesis and judgment; its provider state remains uninspected, as recorded in [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent).

Assessed families are source import, requested semantic edits, structural/integrity evaluation, reconciliation acknowledgment, bounded evidence selection, direct retrieval, conversation write-back and Git recovery. The extra graph and doctor surfaces are assessed below rather than silently subsumed under retrieval. No actual claim-producing session, adjudication trace, provider internals or controlled comparison was supplied. These missing items prevent findings of exercised semantic acceptance, warrant-preserving synthesis, parameter learning or causal improvement. They do not prevent assessment of executable selectors and delivered instructions. Uninspected available branches are not access gaps or evidenced absences.

Consequential claims: see [RT-CLM-evidence-boundary](runtime.md#rt-clm-evidence-boundary), [RT-CLM-delivery-ceiling](runtime.md#rt-clm-delivery-ceiling), and [EPI-CLM-provenance-origin](#epi-clm-provenance-origin).

| Entry point or operation | Source path, SRC-1 | Coverage and inspection basis |
|---|---|---|
| CLI dispatch | `packages/cli/src/index.ts` | Dispatch search confirms init, workspace, query, recovery, doctor, source, agent and bootstrap registrations; supplied runtime traces these families. |
| init; agent; bootstrap; adopt-runtime; launch; OpenCode synchronization | `packages/agent-pack/src/index.ts`; `packages/setup/src/index.ts`; `packages/native-integration/src/opencode.ts` | Supplied [RT-RTE-guidance-install](runtime.md#rt-rte-guidance-install), [RT-RTE-runtime-launch](runtime.md#rt-rte-runtime-launch): static instruction/configuration admission, not semantic acceptance. No target-owned model hook or evaluator inferred. Other host integrations are not independently audited; parity and complete hook coverage are unestablished. |
| source add/list; ingest plan | `packages/core/src/source/index.ts`; `packages/core/src/source/ingest.ts`; `packages/agent-pack/templates/okf-harness/references/ingest.md` | Supplied registration/planner findings in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); direct full ingest-reference read. URL body acquisition is explicitly not established. |
| check/status | `packages/core/src/check/index.ts`; `packages/core/src/lint/index.ts` | Direct complete check read and lint integrity branch; [EPI-RTE-workspace-check](#epi-rte-workspace-check). Remaining lint details not exhaustively audited; no complete semantic-evaluator negative follows. |
| source reconcile | `packages/core/src/source/reconciliation.ts`; `packages/agent-pack/templates/okf-harness/references/reconcile.md` | Direct acknowledgment/filter branch and complete reference; [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile). |
| evidence | `packages/core/src/evidence/index.ts`; `packages/core/src/search/index.ts` | Direct plan, provenance, risk/seal and search selection branches; [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer). Excerpt section-scoring details remain supplied runtime coverage, not independently audited. |
| search/read | `packages/cli/src/commands/query.ts`; `packages/core/src/search/index.ts`; `packages/core/src/read/index.ts` | Full query handler, search exclusion branch and read data types; supplied [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval) supplies downstream read behavior. |
| answer; optional write-back | `packages/agent-pack/templates/okf-harness/references/answer.md` | Direct complete instruction read; [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer), [EPI-CLM-provenance-origin](#epi-clm-provenance-origin). |
| graph | `packages/core/src/graph/index.ts`; `packages/cli/src/commands/query.ts` | Direct graph construction/report writes and CLI consumer; [EPI-RTE-graph-report](#epi-rte-graph-report). HTML rendering not audited for browser security or semantic interpretation. |
| doctor | `packages/cli/src/commands/doctor.ts`; `packages/cli/src/doctor/index.ts` | Direct complete handler and orchestration/aggregation branch; [EPI-RTE-doctor-check](#epi-rte-doctor-check). Individual probes remain selectively uninspected; broad host-health verification is not established. |
| checkpoint/history/restore | `packages/core/src/recovery/index.ts` | Supplied [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery); no independent Git implementation audit. |
| tests/example workspace | `packages/cli/test/maintenance-loop.test.ts`; `examples/ai-research-workspace/README.md` | Supplied boundary inspection only: executable expectations and synthetic content, not observed semantic success or causal support. |

This coverage is selective within the whole-system boundary. It supports route-specific conclusions, not a system-complete negative about every possible evaluator.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-registered-source](#epi-obj-registered-source) | See record | See record | SRC-1 `packages/core/src/source/index.ts` | See record |
| [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | See record | See record | SRC-1 `packages/agent-pack/templates/okf-harness/references/ingest.md` | See record |
| [EPI-OBJ-reconciliation-ledger](#epi-obj-reconciliation-ledger) | See record | See record | SRC-1 `packages/core/src/source/reconciliation.ts` | See record |
| [EPI-OBJ-evidence-brief](#epi-obj-evidence-brief) | See record | See record | SRC-1 `packages/core/src/evidence/index.ts` | See record |
| [EPI-OBJ-check-result](#epi-obj-check-result) | See record | See record | SRC-1 `packages/core/src/check/index.ts` | See record |
| [RT-OBJ-workflow-guidance](runtime.md#rt-obj-workflow-guidance) | Prescriptive content; not itself evidence of wiki truth | See record | SRC-1 `packages/agent-pack/templates/okf-harness/SKILL.md` | See record |
| [RT-OBJ-runtime-pin](runtime.md#rt-obj-runtime-pin) | Version selector, not factual knowledge acceptance | See record | SRC-1 `packages/core/src/config/index.ts` | See record |

## Authority-route ledger

Rows split functions even when they share a supplied route container. Values owned by canonical records are referenced rather than redeclared.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-registered-source](#epi-obj-registered-source) | truth-apt transformation: acquisition/import | File/URL registration | See route; input validation, not source truth | See route | See route | See route | Byte identity preserved for file copy; source truth unknown. URL metadata is not imported page content | See route | See route | SRC-1 `packages/core/src/source/index.ts` | none | none | See route |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | doctrine only | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Source reading to wiki synthesis | External agent; semantic fidelity domain | See route | Requested source-based prose | Requested workflow, not compelled semantic behavior | Not determinable: no produced claim with derivation supplied | See route | See [RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance) | SRC-1 `packages/agent-pack/templates/okf-harness/references/ingest.md` | none | none | Summary versus entailed derivation versus non-entailed conjecture needs actual input/output claims |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | retention | implemented | [EPI-OBJ-registered-source](#epi-obj-registered-source) | no content change | Raw copy and manifest persistence | See route | See route | See route | See route | Retention does not accept source propositions | See route | See route | SRC-1 `packages/core/src/source/index.ts` | none | none | Wiki writes use external agent I/O; post-edit check is not transactional acceptance |
| [EPI-RTE-workspace-check](#epi-rte-workspace-check) | check/evidence production | implemented | [EPI-OBJ-check-result](#epi-obj-check-result) | truth-apt transformation: entailed derivation | Workspace conformance, recorded bytes and revision bookkeeping | See record | See record | See record | Diagnostic | License limited to implemented predicates over snapshot facts | See record | See record | SRC-1 `packages/core/src/check/index.ts` | none | none | Neither ready nor sealed validates semantic truth |
| [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) | operational admission/selection/consumption | implemented | [EPI-OBJ-evidence-brief](#epi-obj-evidence-brief) | no content change | Eligibility for evidence return | Check blocked status, source-risk seals, lexical selection | See route | See route | Enforcing within planner; agent withholding is requested | Exclusion diagnoses provenance risk, not falsity; rank is not confidence | See route | See [RT-BAP-evidence-context](runtime.md#rt-bap-evidence-context) | SRC-1 `packages/core/src/evidence/index.ts` | [RT-CLM-evidence-boundary](runtime.md#rt-clm-evidence-boundary) | none | Direct search/read remain counterpaths |
| [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) | content transformation | implemented | [EPI-OBJ-evidence-brief](#epi-obj-evidence-brief) | truth-apt transformation: non-ampliative reshaping | Selected wiki excerpts and provenance pointers | Deterministic selection/packaging; text-scope domain | See route | See route | Ranking and bounded delivery | Excerpt text retained; omitted context may change interpretation. Source warrant through prior synthesis is unknown | See route | See [RT-BAP-evidence-context](runtime.md#rt-bap-evidence-context) | SRC-1 `packages/core/src/evidence/index.ts` | none | none | No summary generation in inspected excerpt assignment; semantic completeness unestablished |
| [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) | check/evidence production | doctrine only | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Answer sufficiency and conflicts | External agent; question-specific adequacy | See route | Requested judgment and disclosure | Advisory instruction | No recorded evidence-consuming acceptance available | See route | See [RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance) | SRC-1 `packages/agent-pack/templates/okf-harness/references/answer.md` | [RT-CLM-delivery-ceiling](runtime.md#rt-clm-delivery-ceiling) | none | Delivery is not compliance |
| [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) | disposition/acceptance | doctrine only | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Proposed conversation answer worth keeping | Explicit user yes; retention-worthiness criterion | See route | See route | Requested permission before write | User yes is expressly not factual certification; not epistemic acceptance | See route | See route | SRC-1 `packages/agent-pack/templates/okf-harness/references/answer.md` | [EPI-CLM-provenance-origin](#epi-clm-provenance-origin) | none | No-match alone is permission to offer, not permission to persist |
| [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) | retention | doctrine only | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Conversation answer to one concept and index | See route | See route | See route | Requested agent edit | Content relation and source warrant unknown; citation-empty pages legitimate | See route | See [RT-BAP-evidence-context](runtime.md#rt-bap-evidence-context) | SRC-1 `packages/agent-pack/templates/okf-harness/references/answer.md` | [EPI-CLM-provenance-origin](#epi-clm-provenance-origin) | none | Persistence and walkable prose links do not establish post-acceptance lifecycle integration |
| [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile) | content transformation | doctrine only | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Changed source claims and affected wiki claims | Agent compares both revisions; positive signal for removal | See route | Requested direct prose revision or withdrawal | Workflow policy | Source comparison is requested; no actual accepted revision supplied | See route | See [RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance) | SRC-1 `packages/agent-pack/templates/okf-harness/references/reconcile.md` | none | none | Omission alone explicitly does not warrant removal |
| [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile) | disposition/acceptance | implemented | [EPI-OBJ-reconciliation-ledger](#epi-obj-reconciliation-ledger) | no content change | Exact edge and nonempty judgment note | See route | See route | See route | Enforces ledger admission, not semantic adjudication | Registered edge acknowledgment only | See route | See route | SRC-1 `packages/core/src/source/reconciliation.ts` | none | none | No affected-prose inspection in command |
| [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile) | lineage/freshness/recovery | implemented | [EPI-OBJ-reconciliation-ledger](#epi-obj-reconciliation-ledger) | truth-apt transformation: entailed derivation | Acknowledged pair removed from pending edges | Exact-pair filtering; ledger domain | See route | See route | Changes derived dangling facts | Acknowledged is not proven reconciled | See route | See route | SRC-1 `packages/core/src/source/reconciliation.ts` | none | none | Future check can clear currency debt without proving semantic update |
| [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Caller-selected wiki content | See route | See route | See route | See route | Retrieval grants visibility, not endorsement | See route | See route | SRC-1 `packages/core/src/search/index.ts` | [RT-CLM-evidence-boundary](runtime.md#rt-clm-evidence-boundary) | none | Empty exclusion set defeats universal-denial reading |
| [EPI-RTE-graph-report](#epi-rte-graph-report) | content transformation | implemented | Wiki links and graph assertions: see record | truth-apt transformation: entailed derivation | Graph connectivity under parsed-link rules | See record | See record | See record | See record | Existence/connectivity only, not support of linked assertions | See record | See record | SRC-1 `packages/core/src/graph/index.ts` | none | none | No post-acceptance lifecycle integration inferred from a citation edge |
| [EPI-RTE-doctor-check](#epi-rte-doctor-check) | check/evidence production | implemented | Runtime/workspace diagnostic assertions: see record | truth-apt transformation: entailed derivation | Dependency and installation probe results | See record | See record | See record | See record | Probe/aggregation domain, not semantic knowledge | See record | See record | SRC-1 `packages/cli/src/doctor/index.ts` | none | none | Individual probe validity selectively uninspected |
| [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery) | lineage/freshness/recovery | implemented | Workspace files and judgment commits | no content change | Selected prior completion | See route | See route | See route | See route | Restored history is not reaccepted truth; may restore superseded content | See route | See route | SRC-1 `packages/core/src/recovery/index.ts` | none | none | See route |

No accepted semantic candidate is evidenced, so post-acceptance lifecycle integration is not determinable from these sources. This is not a claim that ordinary wiki organization or revision is absent.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-evidence-boundary](runtime.md#rt-clm-evidence-boundary) | See record | SRC-1 `packages/agent-pack/templates/okf-harness/references/answer.md`, doctrine/design | See record | See [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) and [RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval) | None supplied | No causal comparison; graph bounds do not establish semantic closure | Local planner withholding is implemented | Agent widening and host adherence unobserved; no universal read gate |
| [RT-CLM-delivery-ceiling](runtime.md#rt-clm-delivery-ceiling) | See record | SRC-1 `packages/agent-pack/templates/okf-harness/references/answer.md`, doctrine/design | See record | See [RT-RTE-guidance-install](runtime.md#rt-rte-guidance-install) | None supplied | Delivered obligations do not identify component benefit | The claimed ceiling is appropriately scoped | Native payload differs; actual loading unobserved |
| [EPI-CLM-provenance-origin](#epi-clm-provenance-origin) | See record | SRC-1 `packages/agent-pack/templates/okf-harness/references/answer.md`, doctrine/design | See record | See [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) | None supplied | No authorship discriminator or paired history supplied | Empty payload supports missing parsed provenance | It cannot uniquely establish conversation origin; same weight is a declared policy, not measured warrant |

## Bounded conclusion

Source registration preserves local-file bytes and records identities; it does not validate their propositions, and URL registration does not capture page bodies. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Wiki content can subsequently shape answers through the implemented context-selection path [RT-BAP-evidence-context](runtime.md#rt-bap-evidence-context). Source warrant across agent synthesis is unknown. Actual synthesis could preserve claims, derive claims or conjecture them; source instructions alone do not decide which occurred.

The implemented evaluators have local domains: [EPI-RTE-workspace-check](#epi-rte-workspace-check) checks structure, byte integrity and ledger facts; [EPI-RTE-graph-report](#epi-rte-graph-report) derives connectivity; [EPI-RTE-doctor-check](#epi-rte-doctor-check) reports probe results. Their rule-bound deductions have inspectable premises, not established external source truth. Planner admission blocks malformed conformance and withholds certain risky concepts, but direct retrieval is a counterpath. Source-risk exclusion is not rejection of false propositions.

Semantic adequacy and conflict evaluation are delivered obligations. Explicit write-back yes admits retention for future use, not truth certification. Reconciliation acknowledgment admits a pair/note and removes bookkeeping debt, without consuming evidence that affected prose was corrected. Git restoration can withdraw later states operationally without evaluating either state's truth. See the separate rows above and their declaring records.

The provenance-origin disclosure has a specific evidential limit: an empty parsed trail is not an authorship record. See [EPI-CLM-provenance-origin](#epi-clm-provenance-origin). No trace supports produced accepted ampliative knowledge or post-acceptance integration. This does not erase implemented acquisition, retention, selection or the requested semantic evaluation routes. Exact external model version, parameter changes and endpoint substitution remain uninspected independently of these symbolic routes. No single epistemic score, learning verdict or exercised self-improvement conclusion follows.

## Shared records

### Operative objects

#### EPI-OBJ-registered-source
Label: Registered source

Distinct retained input object, not the supplied route [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Local source body is natural-language or opaque supplied bytes on disk; URL registration instead retains symbolic metadata. Manifest fields are symbolic identities/path/hash, not the body's assertions. Candidate propositions can be acquired from readable bodies; their truth and initial source warrant are unknown. Immutable API copy means byte preservation, not endorsement. SRC-1 `packages/core/src/source/index.ts`; minimum implementation passage is supplied in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Later consumers are agent source reading and checks; URL contents still require acquisition elsewhere.

#### EPI-OBJ-wiki-page
Label: Wiki page

Distinct output/input object of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile), [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer). Natural-language assertions persist as Markdown files; symbolic paths/frontmatter/citations drive selection and lineage, not proof. Source-based pages and citation-empty conversation write-backs share storage but differ in lineage. Actual source-to-claim relation is not determinable. Agent semantic authorship and physical edits are external; later planner and answering agent consume the files. SRC-1 `packages/agent-pack/templates/okf-harness/references/ingest.md`, `packages/agent-pack/templates/okf-harness/references/answer.md`.

> An answer worked out from the conversation has no registered source behind it, so the written-back page carries no citations. That is a legitimate state and the post-edit check reports nothing for it.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

#### EPI-OBJ-reconciliation-ledger
Label: Reconciliation ledger

Distinct persisted object, not the supplied [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile) route. JSONL exact-pair fields are symbolic on local disk; the note is natural language whose substance is not checked by admission. Ledger represents recorded acknowledgments, not verified corrected wiki claims. Later filtering consumes IDs, not the semantic adequacy of notes. SRC-1 `packages/core/src/source/reconciliation.ts`; minimum append passage is in the supplied route.

#### EPI-OBJ-evidence-brief
Label: Evidence Brief

Distinct mixed returned object of [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer), not another route. Natural-language excerpt text is combined with symbolic ranges, paths, source pointers, seals and budgets in transient CLI JSON. Later host interpretation can treat excerpt assertions as evidence; metadata alone licenses only identities, selection and lineage facts. This return is not itself persistent memory. The selected excerpt is assigned from returned read text, not generated by a target-owned model. SRC-1 `packages/core/src/evidence/index.ts`.

> excerpt: selected.read.content.text,
> --- `packages/core/src/evidence/index.ts`

#### EPI-OBJ-check-result
Label: Check result

Distinct diagnostic object consumed inside [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) and by status/check handlers. Symbolic transient object with ready/needs_attention/blocked, currency and findings. Truth-apt assertions concern snapshot rule results, not semantic correctness of wiki prose. See [EPI-RTE-workspace-check](#epi-rte-workspace-check) for computation and limits. SRC-1 `packages/core/src/check/index.ts`.

### Routes

#### EPI-RTE-workspace-check
Label: Workspace check

Distinct evaluator spanning standalone check/status and a material stage of [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer); not contained in exactly one supplied route. Endpoints: workspace snapshot → lint plus currency → structured check result. Core owns evaluation; no human veto or answer oracle for semantic correctness is furnished. Open operational diagnostic, not an improvement experiment. Check reference claims readiness within readability/conformance; it separates high-priority risk from universal answer blocking. SRC-1 `packages/core/src/check/index.ts`, `packages/core/src/lint/index.ts`, `packages/agent-pack/templates/okf-harness/references/check.md`.

- Immediate return: Structured status, conformance, grouped findings and currency.
- Later read-back: inapplicable — check is computed anew; it does not persist a decision or modify prose.
- Delegated visibility: CLI caller gets diagnostics; evidence planner receives the same snapshot-derived result.
- Selection predicate: Four conformance codes determine blocked; other findings determine needs_attention; currency uses error diagnostics and promoted pending edges.
- Invalidation or expiry: Snapshot changes require a new check; no enduring semantic endorsement is issued.
- Activation or effect: Planner throws on blocked; selected risk findings become seals/warnings. Standalone reporting does not automatically repair or roll back files.
- Evidence limits: Predicates establish rule outcomes, not truth, evidence sufficiency, source fidelity or successful agent maintenance. No execution evidence supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete implementation deduction, not target execution: if lint issues are empty and no promoted source has a dangling revision edge, currency is sealed and status is ready. This includes a workspace with zero promoted sources. If a matching edge is acknowledged, pair filtering can remove its pending status without reading wiki prose. Thus neither sealed nor ready entails accepted knowledge. A contrary case to blanket passivity is the planner's blocked branch, which actually throws; its enforcement domain is conformance, not truth.

> status: okfFindings.length > 0 ? "blocked" : harnessOk ? "ready" : "needs_attention",
> --- `packages/core/src/check/index.ts`

> return { sealed: dangling.length === 0, promotedSources, dangling, diagnostics };
> --- `packages/core/src/check/index.ts`

> if (actual === entry.sha256) {
>         return [];
>       }
> --- `packages/core/src/lint/index.ts`

#### EPI-RTE-graph-report
Label: Graph report

Distinct route, no counterpart after comparison with supplied retrieval routes. The evidence route uses graph data internally; this exposed operation additionally writes JSON and HTML reports. Endpoints: current wiki files → parsed nodes/edges/backlinks → report files and returned paths/stats. Core deterministic rules own transformation; caller chooses invocation, browser opening is optional. Natural-language titles are copied; graph assertions are symbolic. SRC-1 `packages/core/src/graph/index.ts`, `packages/cli/src/commands/query.ts`.

- Immediate return: Report paths, counts, missing targets and issues.
- Later read-back: Persisted reports can be opened later; no inspected automatic acceptance/update consumer reads these reports to revise wiki knowledge.
- Delegated visibility: CLI caller receives stats/paths; browser may receive graph visualization on explicit open.
- Selection predicate: Non-reserved files; parse Markdown/bare references, resolve targets, exclude self-edges, deduplicate and sort; target references/ or bare reference syntax yields citation kind.
- Invalidation or expiry: A later generation overwrites report files; report timestamp is not semantic freshness of claims.
- Activation or effect: Writes connectivity reports and optional browser display, not claim admission or prose repair.
- Evidence limits: Edges describe parsed linkage, not evidence entailment or accepted claim integration. Browser rendering and actual use unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete text-transform deduction: for a parsed link target resolving from concept A to existing concept `references/r`, the kind is citation and backlinks for that target include A. This follows from target naming and parsing, irrespective of whether A's assertion is supported by r. The semantic support claim therefore cannot inherit the graph rule's warrant.

> target.kind === "citation" || conceptId.startsWith("references/") ? "citation" : "link",
> --- `packages/core/src/graph/index.ts`

> backlinks[edge.to] = [...(backlinks[edge.to] ?? []), edge.from].sort();
> --- `packages/core/src/graph/index.ts`

#### EPI-RTE-doctor-check
Label: Doctor check

Distinct diagnostic route, no counterpart after comparison with supplied runtime routes. Endpoints: dependency/integration/workspace probes → grouped status summary → CLI envelope/exit code and next-step advice. Deterministic orchestration owns aggregation; caller initiates an open operational check, not a knowledge or improvement experiment. Probe reports contain symbolic status and natural-language explanations. No answer oracle for wiki truth is supplied. SRC-1 `packages/cli/src/doctor/index.ts`, `packages/cli/src/commands/doctor.ts`.

- Immediate return: Checks, groups, pass/warn/fail/skip summary and envelope with ok determined by zero failures.
- Later read-back: inapplicable — inspected orchestration returns diagnostics without retaining a knowledge decision.
- Delegated visibility: Caller receives diagnostic envelope; invoked probes receive executable arguments/environment, not a semantic wiki-claim evaluation request.
- Selection predicate: Runtime probes, supported host integrations and fallback checks; workspace checks run only when a workspace resolves; development dependency check is opt-in.
- Invalidation or expiry: New environment or workspace state needs a new invocation.
- Activation or effect: Handler sets failure exit status and repair advice; no automatic wiki semantic acceptance or repair is implemented by this orchestration.
- Evidence limits: Individual probe implementations are selectively uninspected; successful aggregation establishes only zero reported failures, not effective host instruction adherence or truthful wiki content. No probe execution supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> ok: summary.fail === 0,
>     workspace: workspaceRoot,
> --- `packages/cli/src/doctor/index.ts`

> setExitCode(result.ok ? 0 : 1);
> --- `packages/cli/src/commands/doctor.ts`

### Behavioral-authority paths

none declared in this member

### Claims

#### EPI-CLM-provenance-origin
Label: Empty provenance disclosure

Distinct consequential design claim from the supplied withholding/delivery claims. Answer instruction directs the agent to label empty-provenance supporting pages as conversation-derived and says a user's recorded decision carries the same weight as other evidence. This is a disclosure/weight policy, not an implemented origin classifier. SRC-1 `packages/agent-pack/templates/okf-harness/references/answer.md`; implementation of provenance fields in `packages/core/src/evidence/index.ts` collects parsed citations, reference sources and source pointers, with no authorship channel.

> When a load-bearing claim rests on pages whose provenance payload is empty — no citations and no source pointers — name in the answer that the knowledge came from conversation rather than an ingested source. Weight is not discounted: the user's own recorded decision carries the same weight as any other evidence. The obligation is retraceability, not caveating; the answer always shows where the provenance trail ends.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

> return {
>     citations: read.citations,
>     citationIssues: read.citationIssues,
>     references,
>     sourceIds,
>     sources,
>   };
> --- `packages/core/src/evidence/index.ts`

Countercase: a citation-empty page introduced by direct/manual authorship has the same parsed empty fields as a compliant conversation write-back. The implemented payload cannot distinguish them. Workflow-conforming write-back does support the claimed origin in that restricted case; absence of an origin trace prevents extending it to arbitrary stored pages. No observed misdisclosure is claimed.

### Components

none declared in this member

### Evidenced absences

none declared in this member
