---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Amanuensis epistemic routes: source-backed claims, adversarial challenge, explanations, repair verification and bounded evaluation at the frozen revision."
run-id: AAS-2026-11-08-amanuensis-b3a8e3e53488-01
reviewed-boundary: a98093dc7aad3c0e64d42132ece305fc5ea7f3f9
---

# Amanuensis epistemic report

## Source-and-claim boundary

This report asks how Amanuensis turns code readings and external research into retained accounts, how it checks or withdraws them, and what later consumers may rely on. Scope, exclusions and source identity are as declared in [boundary](boundary.md#boundary-and-evidence); evidence identities resolve only through its [Source register](boundary.md#source-register). SRC-1 supplies inspected implementation and attributed doctrine/design, not an observed deployment. HEAD was checked against the registered pin. No target, test, example, model or provider was executed.

The material distinction is between **record authority** (which row may be returned, classified, or count toward a gate) and **source correctness** (whether its statement is true of the code). The server implements substantial controls over the former. Some checks consume evidence IDs, kinds and revisions without verifying the semantic relation. This is not an absence of criticism: phase 4 explicitly requests disproof, and repair/review handlers have different, concrete constraints. See [EPI-RTE-claim-challenge](#epi-rte-claim-challenge), [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) and [EPI-RTE-review-aggregation](#epi-rte-review-aggregation). It is also not a universal verdict on all shipped evaluators.

Consequential warrant claims are [EPI-CLM-earned-reliance](#epi-clm-earned-reliance), [EPI-CLM-explanation-limits](#epi-clm-explanation-limits), [EPI-CLM-repair-proof](#epi-clm-repair-proof) and the supplied [RT-CLM-autonomous-survey](runtime.md#rt-clm-autonomous-survey). The README itself excludes an established longitudinal usefulness claim. Excluded host/provider internals prevent assessing reliable model compliance, actual context isolation and parameter updates; see [RT-CMP-host-model](runtime.md#rt-cmp-host-model). Missing execution traces tied to these routes prevent observed acceptance, benefit and causal component attribution. Available repository receipts and generated conspectus files were not used as operation evidence; their existence is not evidence that a particular route generated or accepted their content.

### Coverage

“Direct” below means source text read in this job at SRC-1; “supplied” means reliance on the runtime record and its passages. File ranges were bounded. A declaration catalog was checked against runtime coverage rather than assuming only its selected routes exist.

| Entry point or operation | SRC-1 source path | Coverage / records or remaining limit |
|---|---|---|
| npm executables, installer dispatch | `mcp-server/package.json`, `mcp-server/src/cli.ts` | Direct bin mapping and main dispatch: init/install/upgrade/doctor/uninstall. Supplied [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill) covers instruction installation. Doctor/repair internals not independently assessed as knowledge evaluators; prevents installation-complete correctness claim. |
| MCP initialization, tool catalog and call dispatch | `mcp-server/src/index.ts` | Direct allTools composition and request handler; supplied [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch). Registered review, research, diagnosticity, learning, evaluation and maintenance tools are not invisible merely because runtime did not trace them fully. No separate epistemic hook is installed in the inspected dispatch; host hooks remain outside this conclusion. |
| Source survey and adversarial/packaging prompts | `.claude/skills/amanuensis/references/phase-2-structural.md`, `.claude/skills/amanuensis/references/phase-3-concerns.md`, `.claude/skills/amanuensis/references/phase-4-adversarial.md`, `.claude/skills/amanuensis/references/phase-5-packaging.md` | Direct phase procedures; supplied [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle). Model interpretation is requested, not observed. |
| Evidence, claims, intervals and challenge outcomes | `mcp-server/src/tools/evidence.ts`, `mcp-server/src/tools/claims.ts`, `mcp-server/src/helpers.ts`, `mcp-server/src/invariants.ts` | Direct writer/check/reader paths: [EPI-RTE-evidence-record](#epi-rte-evidence-record), [EPI-RTE-claim-admission](#epi-rte-claim-admission), [EPI-RTE-claim-challenge](#epi-rte-claim-challenge), [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal). |
| Concern classification, finding repair and contradiction resolution | `mcp-server/src/tools/dispositions.ts`, `mcp-server/src/tools/findings.ts`, `mcp-server/src/tools/contradictions.ts` | Direct operative handlers: [EPI-RTE-concern-disposition](#epi-rte-concern-disposition), [EPI-RTE-finding-resolution](#epi-rte-finding-resolution), [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution). |
| Explanations and slot discharge | `mcp-server/src/tools/explanations.ts`, `mcp-server/src/invariants.ts` | Direct admission and selectExplanation/readExplanation: [EPI-RTE-explanation-record](#epi-rte-explanation-record), [EPI-RTE-explanation-selection](#epi-rte-explanation-selection). |
| Reader standing, structure and defects | `mcp-server/src/tools/locus.ts` | Direct contentAuthorization, buildStructure and defect partition/replay excerpts; supplied [RT-RTE-locus-read](runtime.md#rt-rte-locus-read). Not a full independent audit of attention/history budgeting. |
| Competing-hypothesis matrix | `mcp-server/src/tools/diagnosticity.ts` | Direct open/cell/resolve handlers: [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution). |
| Sealed review analysis, expected-key scoring | `mcp-server/src/tools/review-analysis.ts` | Direct runtimeInput, land, aggregate, reveal and scoreEvaluation: [EPI-RTE-review-aggregation](#epi-rte-review-aggregation), [EPI-RTE-review-scoring](#epi-rte-review-scoring). Plan/freeze/dispatch helpers and all evidence-validation internals not fully traced; prevents complete isolation/custody guarantee. |
| External research import/use | `mcp-server/src/tools/research.ts` | Direct degradation, destination matcher, land and consume; [EPI-RTE-research-landing](#epi-rte-research-landing), [EPI-RTE-research-consumption](#epi-rte-research-consumption). Proposal admission, dispatch artifact custody and expiry are exposed but not fully assessed. |
| Stale backlog/clear/retire | `mcp-server/src/tools/stale.ts` | Direct handlers: [EPI-RTE-staleness-clear](#epi-rte-staleness-clear). Full git drift, impact, refresh and revalidation scoring chains remain unassessed; no freshness-complete conclusion. |
| Decision and learning/method admission | `mcp-server/src/tools/decisions.ts`, `mcp-server/src/tools/learning.ts`, `mcp-server/src/tools/crosswalk.ts`, `mcp-server/src/schema.sql` | Supplied [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) and [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission), including activation/readback and limits. No independent full crosswalk or future-run consumer trace in this report. |
| MCP and standalone publication, clean/readback alternatives | `mcp-server/src/tools/materialize.ts`, `materializer/materialize.py`, `materializer/amanuensis_materializer/core.py` | Supplied [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication); readback checks correspondence to durable state, not source correctness. Renderer/verifier internals not directly audited here. |
| Direct handler adapter and direct prose writes | `mcp-server/src/tools/chorusmith-adapter.ts`, `.claude/skills/amanuensis/SKILL.md` | Supplied [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) and runtime alternate-executor account. Outer Ajv is not a universal admission boundary. |
| Other registered analysis/program surfaces | `mcp-server/src/tools/evaluation.ts`, `mcp-server/src/tools/review.ts`, `mcp-server/src/tools/review-session.ts`, `mcp-server/src/tools/design-session.ts`, `mcp-server/src/tools/codebase-brief.ts`, `mcp-server/src/tools/composition.ts`, `mcp-server/src/tools/compare.ts` | Catalog checked; selected evaluation declarations/function locations searched. Full program operating-envelope derivation, review/design session admission and composition/compare consumers remain uninspected. These are relevant included paths; they prevent any system-complete negative about acceptance, integration, evaluation or theory building. |
| Carry/rebuild, historical evaluator, local receipts/CI | `dev/rebuild-self-conspectus-store.mjs`, `mcp-server/scripts/historical-evaluation.mjs`, `.github/workflows/test.yml` | Supplied boundary/runtime coverage only; no independent import lineage or historical trial assessment. Other dev/design/scholiast artifacts and receipts remain available but unassessed. No generalized effectiveness or causal conclusion. |

## Epistemic-object inventory

The IDs below identify operative parts, not observed candidate instances. A record's form, role, source and limit are owned by its declaration.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-evidence](#epi-obj-evidence) | see [EPI-OBJ-evidence](#epi-obj-evidence) | Structured evidence | SRC-1: `mcp-server/src/tools/evidence.ts` | see [EPI-OBJ-evidence](#epi-obj-evidence) |
| [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-OBJ-claims](#epi-obj-claims) | Typed claims | SRC-1: `mcp-server/src/tools/claims.ts` | see [EPI-OBJ-claims](#epi-obj-claims) |
| [EPI-OBJ-dispositions](#epi-obj-dispositions) | see [EPI-OBJ-dispositions](#epi-obj-dispositions) | Concern dispositions | SRC-1: `mcp-server/src/tools/dispositions.ts` | see [EPI-OBJ-dispositions](#epi-obj-dispositions) |
| [EPI-OBJ-findings](#epi-obj-findings) | see [EPI-OBJ-findings](#epi-obj-findings) | Findings and resolution events | SRC-1: `mcp-server/src/tools/findings.ts` | see [EPI-OBJ-findings](#epi-obj-findings) |
| [EPI-OBJ-contradictions](#epi-obj-contradictions) | see [EPI-OBJ-contradictions](#epi-obj-contradictions) | Contradictions | SRC-1: `mcp-server/src/tools/contradictions.ts` | see [EPI-OBJ-contradictions](#epi-obj-contradictions) |
| [EPI-OBJ-explanations](#epi-obj-explanations) | see [EPI-OBJ-explanations](#epi-obj-explanations) | Purpose and account | SRC-1: `mcp-server/src/tools/explanations.ts` | see [EPI-OBJ-explanations](#epi-obj-explanations) |
| [EPI-OBJ-diagnosticity](#epi-obj-diagnosticity) | see [EPI-OBJ-diagnosticity](#epi-obj-diagnosticity) | Diagnosticity matrix | SRC-1: `mcp-server/src/tools/diagnosticity.ts` | see [EPI-OBJ-diagnosticity](#epi-obj-diagnosticity) |
| [EPI-OBJ-review-analysis](#epi-obj-review-analysis) | see [EPI-OBJ-review-analysis](#epi-obj-review-analysis) | Review judgments and aggregation | SRC-1: `mcp-server/src/tools/review-analysis.ts` | see [EPI-OBJ-review-analysis](#epi-obj-review-analysis) |
| [EPI-OBJ-blind-truth](#epi-obj-blind-truth) | see [EPI-OBJ-blind-truth](#epi-obj-blind-truth) | Blind truth and scores | SRC-1: `mcp-server/src/tools/review-analysis.ts` | see [EPI-OBJ-blind-truth](#epi-obj-blind-truth) |
| [EPI-OBJ-research-results](#epi-obj-research-results) | see [EPI-OBJ-research-results](#epi-obj-research-results) | External research results | SRC-1: `mcp-server/src/tools/research.ts` | see [EPI-OBJ-research-results](#epi-obj-research-results) |
| [EPI-OBJ-stale-ledger](#epi-obj-stale-ledger) | see [EPI-OBJ-stale-ledger](#epi-obj-stale-ledger) | Stale file ledger | SRC-1: `mcp-server/src/tools/stale.ts` | see [EPI-OBJ-stale-ledger](#epi-obj-stale-ledger) |
| [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill) | Instruction content, not an observed truth judgment | see [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill) | SRC-1: `.claude/skills/amanuensis/SKILL.md` | Static method; host compliance unobserved |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Internal candidate content not determinable from weights | see [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | SRC-1: `.claude/skills/amanuensis/SKILL.md` | Provider internals outside boundary |
| [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | Decision revision/premise content: see record | Recorded decision authority | SRC-1: `mcp-server/src/tools/decisions.ts` | Supplied route, no individual populated revision assessed |
| [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | Lesson/policy content: see record | Proposed and active policy representation | SRC-1: `mcp-server/src/tools/learning.ts` | Supplied route; exact proposal semantics and later activation unobserved |

## Authority-route ledger

Architectural status is assessed here. Other fields marked “see” are owned by the cited record, including the specific target/domain, result, force and horizon. Repeated citations indicate different consequential functions of one implementation; checking is not disposition, and retention is not lifecycle integration. None of these implementations establishes an observed operation merely by existing.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-evidence-record](#epi-rte-evidence-record) | check/evidence production | implemented | [EPI-OBJ-evidence](#epi-obj-evidence) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | SRC-1: `mcp-server/src/tools/evidence.ts` | none | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) |
| [EPI-RTE-evidence-record](#epi-rte-evidence-record) | retention | implemented | [EPI-OBJ-evidence](#epi-obj-evidence) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | SRC-1: `mcp-server/src/tools/evidence.ts` | none | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) | see [EPI-RTE-evidence-record](#epi-rte-evidence-record) |
| [EPI-RTE-claim-admission](#epi-rte-claim-admission) | check/evidence production | implemented | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | SRC-1: `mcp-server/src/tools/claims.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) |
| [EPI-RTE-claim-admission](#epi-rte-claim-admission) | disposition/acceptance | implemented | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | SRC-1: `mcp-server/src/tools/claims.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) |
| [EPI-RTE-claim-admission](#epi-rte-claim-admission) | retention | implemented | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | SRC-1: `mcp-server/src/tools/claims.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) | see [EPI-RTE-claim-admission](#epi-rte-claim-admission) |
| [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | check/evidence production | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | SRC-1: `mcp-server/src/invariants.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) |
| [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | retention | implemented | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | SRC-1: `mcp-server/src/invariants.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) |
| [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | operational admission/selection/consumption | implemented | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | SRC-1: `mcp-server/src/invariants.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) | see [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) |
| [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | SRC-1: `mcp-server/src/tools/claims.ts` | none | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) |
| [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | lineage/freshness/recovery | implemented | [EPI-OBJ-claims](#epi-obj-claims) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | SRC-1: `mcp-server/src/tools/claims.ts` | none | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) | see [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) |
| [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | check/evidence production | implemented | [EPI-OBJ-dispositions](#epi-obj-dispositions) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | SRC-1: `mcp-server/src/tools/dispositions.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) |
| [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | disposition/acceptance | implemented | [EPI-OBJ-dispositions](#epi-obj-dispositions) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | SRC-1: `mcp-server/src/tools/dispositions.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) |
| [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | retention | implemented | [EPI-OBJ-dispositions](#epi-obj-dispositions) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | SRC-1: `mcp-server/src/tools/dispositions.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) | see [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) |
| [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | check/evidence production | implemented | [EPI-OBJ-findings](#epi-obj-findings) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | SRC-1: `mcp-server/src/tools/findings.ts` | [EPI-CLM-repair-proof](#epi-clm-repair-proof) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) |
| [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | disposition/acceptance | implemented | [EPI-OBJ-findings](#epi-obj-findings) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | SRC-1: `mcp-server/src/tools/findings.ts` | [EPI-CLM-repair-proof](#epi-clm-repair-proof) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) |
| [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | retention | implemented | [EPI-OBJ-findings](#epi-obj-findings) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | SRC-1: `mcp-server/src/tools/findings.ts` | [EPI-CLM-repair-proof](#epi-clm-repair-proof) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | see [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) |
| [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | disposition/acceptance | implemented | [EPI-OBJ-contradictions](#epi-obj-contradictions) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | SRC-1: `mcp-server/src/tools/contradictions.ts` | none | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) |
| [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | retention | implemented | [EPI-OBJ-contradictions](#epi-obj-contradictions) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | SRC-1: `mcp-server/src/tools/contradictions.ts` | none | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | see [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) |
| [EPI-RTE-explanation-record](#epi-rte-explanation-record) | check/evidence production | implemented | [EPI-OBJ-explanations](#epi-obj-explanations) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | SRC-1: `mcp-server/src/tools/explanations.ts` | [EPI-CLM-explanation-limits](#epi-clm-explanation-limits) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) |
| [EPI-RTE-explanation-record](#epi-rte-explanation-record) | retention | implemented | [EPI-OBJ-explanations](#epi-obj-explanations) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | SRC-1: `mcp-server/src/tools/explanations.ts` | [EPI-CLM-explanation-limits](#epi-clm-explanation-limits) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) | see [EPI-RTE-explanation-record](#epi-rte-explanation-record) |
| [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-explanations](#epi-obj-explanations) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | SRC-1: `mcp-server/src/invariants.ts` | [EPI-CLM-explanation-limits](#epi-clm-explanation-limits) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | see [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) |
| [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | check/evidence production | implemented | [EPI-OBJ-diagnosticity](#epi-obj-diagnosticity) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | SRC-1: `mcp-server/src/tools/diagnosticity.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) |
| [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | disposition/acceptance | implemented | [EPI-OBJ-diagnosticity](#epi-obj-diagnosticity) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | SRC-1: `mcp-server/src/tools/diagnosticity.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) |
| [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | retention | implemented | [EPI-OBJ-diagnosticity](#epi-obj-diagnosticity) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | SRC-1: `mcp-server/src/tools/diagnosticity.ts` | [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) | see [EPI-RTE-diagnosticity-resolution](#epi-rte-diagnosticity-resolution) |
| [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | check/evidence production | implemented | [EPI-OBJ-review-analysis](#epi-obj-review-analysis) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | SRC-1: `mcp-server/src/tools/review-analysis.ts` | none | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) |
| [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | disposition/acceptance | implemented | [EPI-OBJ-review-analysis](#epi-obj-review-analysis) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | SRC-1: `mcp-server/src/tools/review-analysis.ts` | none | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) |
| [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | retention | implemented | [EPI-OBJ-review-analysis](#epi-obj-review-analysis) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | SRC-1: `mcp-server/src/tools/review-analysis.ts` | none | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | see [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) |
| [EPI-RTE-review-scoring](#epi-rte-review-scoring) | check/evidence production | implemented | [EPI-OBJ-blind-truth](#epi-obj-blind-truth) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | SRC-1: `mcp-server/src/tools/review-analysis.ts` | none | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) |
| [EPI-RTE-review-scoring](#epi-rte-review-scoring) | retention | implemented | [EPI-OBJ-blind-truth](#epi-obj-blind-truth) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | SRC-1: `mcp-server/src/tools/review-analysis.ts` | none | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) | see [EPI-RTE-review-scoring](#epi-rte-review-scoring) |
| [EPI-RTE-research-landing](#epi-rte-research-landing) | content transformation | implemented | [EPI-OBJ-research-results](#epi-obj-research-results) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | SRC-1: `mcp-server/src/tools/research.ts` | none | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) |
| [EPI-RTE-research-landing](#epi-rte-research-landing) | check/evidence production | implemented | [EPI-OBJ-research-results](#epi-obj-research-results) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | SRC-1: `mcp-server/src/tools/research.ts` | none | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) |
| [EPI-RTE-research-landing](#epi-rte-research-landing) | retention | implemented | [EPI-OBJ-research-results](#epi-obj-research-results) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) | SRC-1: `mcp-server/src/tools/research.ts` | none | see [EPI-RTE-research-landing](#epi-rte-research-landing) | see [EPI-RTE-research-landing](#epi-rte-research-landing) |
| [EPI-RTE-research-consumption](#epi-rte-research-consumption) | operational admission/selection/consumption | implemented | [EPI-OBJ-research-results](#epi-obj-research-results) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | SRC-1: `mcp-server/src/tools/research.ts` | none | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) |
| [EPI-RTE-research-consumption](#epi-rte-research-consumption) | retention | implemented | [EPI-OBJ-research-results](#epi-obj-research-results) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | SRC-1: `mcp-server/src/tools/research.ts` | none | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) | see [EPI-RTE-research-consumption](#epi-rte-research-consumption) |
| [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | lineage/freshness/recovery | implemented | [EPI-OBJ-stale-ledger](#epi-obj-stale-ledger) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | SRC-1: `mcp-server/src/tools/stale.ts` | none | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) | see [EPI-RTE-staleness-clear](#epi-rte-staleness-clear) |
| [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | content transformation | doctrine only | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | truth-apt transformation: indeterminate | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | SRC-1: `.claude/skills/amanuensis/SKILL.md` | none | see [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) | No populated output and checked premises identify acquisition, reshaping, entailment or non-entailment; cannot label all model prose conjecture. |
| [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | operational admission/selection/consumption | implemented | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | truth-apt transformation: non-ampliative reshaping | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | SRC-1: `mcp-server/src/tools/locus.ts` | none | see [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) | Delivery is not compliance or evidence of correctness. |
| [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | check/evidence production | implemented | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | no content change | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | SRC-1: `mcp-server/src/tools/materialize.ts` | none | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | Optional readback; projection fidelity is not source truth. |
| [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | operational admission/selection/consumption | implemented | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | truth-apt transformation: non-ampliative reshaping | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | SRC-1: `materializer/materialize.py` | none | see [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) | Clean promotion can occur with verification disabled; see supplied record. |
| [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | disposition/acceptance | implemented | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | no content change | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | SRC-1: `mcp-server/src/tools/decisions.ts` | none | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | Recorded decision authority is not independently authenticated correctness or deployment. |
| [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | retention | implemented | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | no content change | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | SRC-1: `mcp-server/src/tools/decisions.ts` | none | see [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) | History/pointer retention differs from accepted-claim lifecycle integration. |
| [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | check/evidence production | implemented | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | truth-apt transformation: entailed derivation | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | SRC-1: `mcp-server/src/tools/learning.ts` | none | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | Directional difference/minimum effect is conditional on supplied measurements. |
| [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | disposition/acceptance | implemented | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | no content change | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | SRC-1: `mcp-server/src/tools/learning.ts` | none | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | Qualification/staging/readback validates supplied policy representation, not independent outcome truth. |
| [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | behavior/policy adaptation | implemented | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | non-truth-apt policy/content update: active policy representation | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | SRC-1: `mcp-server/src/tools/learning.ts` | none | see [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) | Database activation/readback is wired; actual future behavioral dependency is unobserved. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-earned-reliance](#epi-clm-earned-reliance) | see record | SRC-1: `README.md`; doctrine/design | Phased disproof and evidence discipline; see record | [EPI-RTE-evidence-record](#epi-rte-evidence-record), [EPI-RTE-claim-admission](#epi-rte-claim-admission), [EPI-RTE-claim-challenge](#epi-rte-claim-challenge), [EPI-RTE-concern-disposition](#epi-rte-concern-disposition), [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) | None used | No actual accuracy comparison; caller controls semantic assertions and kind labels | Real provenance/admission/status gates and requested disproof, not automatic proof every admitted claim fits its evidence | Literal universal reading is too strong: metadata admission, deferred bypass and separate adapter/direct-write paths bound it |
| [EPI-CLM-explanation-limits](#epi-clm-explanation-limits) | see record | SRC-1: `README.md`; doctrine/design | Phase-4 sentence criticism and phase-5 revision/decline | [EPI-RTE-explanation-record](#epi-rte-explanation-record), [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) | None used | No body-specific source comparison observed | Explanations are retained model accounts with explicit abstention and selection, not mechanically checked truth | Dedicated reader inspected; full ageing display chain not independently audited |
| [EPI-CLM-repair-proof](#epi-clm-repair-proof) | see record | SRC-1: `README.md`; doctrine/design | Repairs remain unverified pending new evidence | [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) | None used | No test execution or repair outcome evidence | Fixed and verified-fixed cannot silently collapse through the inspected fixed writer; explicit verification/custody is required | “Proves” is stronger than role/session/ancestry checks; new same-session evidence can still be misinterpreted |
| [RT-CLM-autonomous-survey](runtime.md#rt-clm-autonomous-survey) | see record | SRC-1: `.claude/skills/amanuensis/SKILL.md`; doctrine/design | see record | [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle), [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) | None used | Host scheduling/compliance unobserved | Autonomous continuation is requested without per-phase human gates; code provides state/tool scaffolding | This does not establish reliable criticism, truthful acceptance or autonomous theory building |

## Bounded conclusion

**What is acquired and retained.** [EPI-RTE-evidence-record](#epi-rte-evidence-record) and [EPI-RTE-research-landing](#epi-rte-research-landing) import caller-supplied source descriptions, excerpts and external statements. They preserve declared locators, revisions and access limitations; actual source warrant is unknown without verifying the reading and interpretation. Research confidence is constrained by declared access and source counts, not established independence. [EPI-RTE-claim-admission](#epi-rte-claim-admission), [EPI-RTE-concern-disposition](#epi-rte-concern-disposition), [EPI-RTE-explanation-record](#epi-rte-explanation-record) and [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) retain different objects with different authority rules. Initial current-claim authority can precede challenge. Explanation retention can explicitly say “declined”; its body need not be a newly derived or accepted claim.

**What checks change.** There is no single evaluator. Git resolution/ancestry checks target revision custody; enums, evidence-kind ranking and attachment predicates target record eligibility; caller models judge semantic support, concern fit and disproof; review aggregation deterministically combines those judgments; sealed scoring compares resulting keys to caller-supplied reference keys. Their licenses do not transfer between domains. [EPI-RTE-claim-withdrawal](#epi-rte-claim-withdrawal) changes later current selection, [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) changes unresolved selection, and [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) changes pending/verified defect partitions. These are consequential consumers, not inert review labels. [EPI-RTE-claim-challenge](#epi-rte-claim-challenge) enables ordinary mapped progression but retains the supplied deferred-path exception. Its requested semantic review is doctrine; recorded outcome and continuation checks are implemented.

**What is reshaped or derived.** [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) returns selected retained accounts, subject to standing and omission controls; it does not generate an explanation. The inspected structure builder withholds content for unauthorized file/symbol standing, but both examined and examined-stale are content-authorizing, so drift does not mean blanket withdrawal. [EPI-RTE-explanation-selection](#epi-rte-explanation-selection) deterministically selects a whole stored body or abstention without changing its meaning. [EPI-RTE-review-aggregation](#epi-rte-review-aggregation) derives status and retained keys from recorded judgments; [EPI-RTE-review-scoring](#epi-rte-review-scoring) derives agreement/stability against a supplied oracle. These derivations are warranted as implementation deductions about their inputs, not as proofs that the input judgments or reference answers describe the code correctly. Projection/readback in [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) checks derived views against durable state, with the supplied optional-verification limits.

**What is not established.** Model-authored statements can be truth-apt, but no supplied candidate instance and source comparison establishes a particular novel non-entailed proposition or accepted ampliative claim here. The ordinary skill requests criticism and revision, not just fluent summaries; semantic acceptance for correctness requires that examination to operate. No report-wide absence of acceptance or lifecycle integration follows: decision authority admission is separately wired, and other relevant shipped analysis/design/evaluation surfaces remain unassessed. [EPI-RTE-research-consumption](#epi-rte-research-consumption) records claimed use or no-change; its changed flag alone proves neither a changed destination nor acceptance followed by lifecycle integration.

**Policy and future behavior.** [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) separately supports direct update of an active policy representation and successful reader comparison inside a transaction. It does not establish improved capacity, model-weight learning, or later behavior causally depending on the changed policy. Distributed-parametric internals remain as bounded in [RT-CMP-host-model](runtime.md#rt-cmp-host-model). Reflection, learning, autonomy and self-improvement are not inferred from each other. For the inspected explanation route, localized whole-body revision is afforded; consumption/revision are requested in phase 4/5; content-directed criticism naming a contradicted sentence is prescribed. No inspected candidate/trace establishes all theory-builder conditions 1–4 as exercised or successful. Unassessed review/design/program surfaces prevent a system-complete negative about those properties. The independent route conclusions above stand without such a verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-evidence
Label: Structured evidence

Candidate content: Caller-authored excerpts, notes and assertions about code at a revision; source truth is not independently established.

Representational form and storage substrate: Natural-language excerpt/note plus symbolic path, kind, revision and session fields in SQLite evidence and attachment tables.

Identity comparison: No supplied counterpart: unlike [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill), this is accumulated survey content.

Evidence: SRC-1: `mcp-server/src/tools/evidence.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-claims
Label: Typed claims

Candidate content: Statements about types, state, flows and invariants over named code/revision scopes.

Representational form and storage substrate: Natural-language statement with symbolic epistemic kind, subject, claim key, Git validity interval and evidence links in SQLite claims, claim_evidence and event tables.

Identity comparison: No supplied object counterpart; these are products of [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle), not the static skill.

Evidence: SRC-1: `mcp-server/src/tools/claims.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-dispositions
Label: Concern dispositions

Candidate content: Whether a named concern obtains in a subsystem, with evidence quality and rationale.

Representational form and storage substrate: Natural-language rationale and symbolic classification/quality/linchpin fields in SQLite dispositions and disposition_evidence.

Identity comparison: Distinct from claims: mutable subsystem/concern classification, not immutable claim-key interval.

Evidence: SRC-1: `mcp-server/src/tools/dispositions.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-findings
Label: Findings and resolution events

Candidate content: Symptom, root-cause and business-context claims; whether a recorded repair was verified at a revision.

Representational form and storage substrate: Natural-language finding and verification rationale plus symbolic status, fix revision and evidence links in SQLite findings and finding_resolution_events.

Identity comparison: Distinct from dispositions: finding-specific repair lifecycle and later defect partitions.

Evidence: SRC-1: `mcp-server/src/tools/findings.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-contradictions
Label: Contradictions

Candidate content: Caller-identified incompatible finding classifications or scopes, and proposed resolution.

Representational form and storage substrate: Natural-language conflict/scope/rationale plus symbolic resolution and finding/evidence IDs in SQLite contradictions and contradiction_resolution_events.

Identity comparison: Distinct from findings: relation between two findings with its own resolution history.

Evidence: SRC-1: `mcp-server/src/tools/contradictions.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-explanations
Label: Purpose and account

Candidate content: Model-authored purpose/how-it-works prose about a subsystem or project; a declined slot instead records a reason, not a positive explanation.

Representational form and storage substrate: Natural-language body plus symbolic subject, slot, disposition, revision and evidence links in SQLite explanations and explanation_evidence.

Identity comparison: Distinct from claims: append-only whole-body correction and newest-effective selection rather than individual claim interval.

Evidence: SRC-1: `mcp-server/src/tools/explanations.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-diagnosticity
Label: Diagnosticity matrix

Candidate content: Caller judgments of consistency/contradiction between each evidence item and competing concern; designated leading concern.

Representational form and storage substrate: Natural-language symptom/notes with symbolic concern-by-evidence verdict cells and session outcome in SQLite diagnosticity tables.

Identity comparison: Distinct from dispositions: comparison matrix, not the resulting concern classification.

Evidence: SRC-1: `mcp-server/src/tools/diagnosticity.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-review-analysis
Label: Review judgments and aggregation

Candidate content: Candidate defect claims and role judgments; derived survived, defeated or contested finding keys.

Representational form and storage substrate: Natural-language claims/rationales plus symbolic role/verdict/evidence-origin and JSON aggregate in SQLite review_judgments, review_hypotheses and review_aggregations.

Identity comparison: No supplied counterpart: separate sealed review-analysis machinery, not the ordinary phase-4 survey record.

Evidence: SRC-1: `mcp-server/src/tools/review-analysis.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-blind-truth
Label: Blind truth and scores

Candidate content: Caller-supplied expected finding keys for assigned blind arms; exact agreement and stability against those expectations.

Representational form and storage substrate: Symbolic expected keys, assignment/pair/replicate IDs, salted hash, contamination flags and numerical report in SQLite review_blind_reveals and review_evaluations.

Identity comparison: Distinct from review judgments: reference outcome and scoring consumer, not reviewer-produced content.

Evidence: SRC-1: `mcp-server/src/tools/review-analysis.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-research-results
Label: External research results

Candidate content: Imported external statements with source access limitations, confidence and destination; separately recorded consumption effect.

Representational form and storage substrate: Natural-language excerpts, claims and effect statements plus symbolic provenance, degradation and destination fields in SQLite research_results, research_sources, research_external_claims and research_consumptions.

Identity comparison: No supplied counterpart: imported decision-related content, not [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) itself.

Evidence: SRC-1: `mcp-server/src/tools/research.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

#### EPI-OBJ-stale-ledger
Label: Stale file ledger

Candidate content: Per-file assertion of examination at a revision and stale/absent bookkeeping; freshness is not endorsement.

Representational form and storage substrate: Symbolic paths, revisions, stale flag/reason in SQLite file_ledger and scope_gaps.

Identity comparison: No supplied counterpart: per-file freshness state, not [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) selection implementation.

Evidence: SRC-1: `mcp-server/src/tools/stale.ts`; operative support and limits are retained in the corresponding route declarations below. No populated candidate is asserted to have been produced or checked in this analysis.

### Routes

#### EPI-RTE-evidence-record
Label: Evidence recording

Object: [EPI-OBJ-evidence](#epi-obj-evidence).

Content/update relation: truth-apt transformation: acquisition/import.

Endpoints: caller citation/excerpt → add_evidence → evidence row/ID. Owner: handler code; the caller, ordinarily a host model, selects the source and authors the evidence kind, excerpt and note. Check target/domain: relative non-traversing source-path syntax, enum kind and resolvable workspace commit. These are provenance-shape checks, not comparison of an excerpt or interpretation with the Git blob. Source warrant: unknown; recorded locator and revision preserve claimed lineage, not authenticated source reading. A counterexample to semantic certification is an inaccurate excerpt with otherwise valid fields: this handler stores the supplied excerpt without fetching its lines. SRC-1: `mcp-server/src/tools/evidence.ts`, `mcp-server/src/helpers.ts`. Distinct from [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch): domain-level evidence admission and retention, not request transport. Caller proposes; code can veto malformed fields, not false prose. Open survey mode; no answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Inserted evidence ID or refusal.
- Later read-back: Evidence IDs and rows reach claim, disposition, finding, explanation and review writers and get_evidence across sessions.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Active session, valid path syntax, evidence-kind enum and resolvable revision.
- Invalidation or expiry: No expiry in add_evidence; later authority changes occur in consuming records, not by this writer.
- Activation or effect: Stores caller evidence and returns ID; its kind can license stronger downstream classifications, without proving the observation.
- Evidence limits: No observed execution; file existence, excerpt accuracy and semantic support are not established by the inspected writer.

> const excerpt = optString(args, "excerpt");
> --- `mcp-server/src/tools/evidence.ts`

> .run(filePath, symbol, lineRange, refSha, kind, excerpt, note, sessionId);
> --- `mcp-server/src/tools/evidence.ts`

#### EPI-RTE-claim-admission
Label: Claim checks and current authority

Object: [EPI-OBJ-claims](#epi-obj-claims).

Content/update relation: no content change.

Endpoints: caller statement and evidence IDs → add_claim/insertClaim → current claims row, supports links and asserted event. Owner: handler and Git/SQLite. Check target/domain: session, subject/kind enums, unique current key, resolvable commits, ancestry of valid_from and evidence, plus file/kind conjunction for key-type/state-container/flow keys. Proposed text remains caller-authored; code does not derive it. Result and force: refusal or transactional admission as current authority. Epistemic license: declared revision and qualifying support metadata; neither truth nor entailment is checked. Operational authority: get_claims selects current versions, and the locus structure builder may expose them. Consumer/channel/horizon: later agents via JSON, advisory for reasoning across sessions; uniqueness and attachment requirements enforce record admission now. SRC-1: `mcp-server/src/tools/claims.ts`, `mcp-server/src/tools/locus.ts`. Distinct from [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) and [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch): domain admission rather than orchestration/transport. Open requests; caller proposes, code vetoes structural defects; no independent expected-answer oracle. Rejected writes roll back; successors use a separate route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: get_claims and describe_locus later select retained statements with evidence metadata.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Current unique key and valid support; file-anchored key categories require a code-verified or contract-stated row on the subject path.
- Invalidation or expiry: Validity intervals close only through explicit invalidation/supersession in this handler family; query_sha uses ancestry.
- Activation or effect: Grants recorded current authority before a later adversarial challenge; admission alone is not evidence-consuming semantic acceptance for correctness.
- Evidence limits: The statement is requireString input; metadata membership does not establish that evidence entails it.

> if (rows.some((row) => FILE_ANCHORED_EVIDENCE.includes(row.kind) && row.file_path === path)) {
>   return;
> }
> --- `mcp-server/src/tools/claims.ts`

> statement,
>             epistemicKind,
>             assertedAtSha,
>             validFromSha,
>             sessionId,
>             evidenceRows,
>             reason: "initial assertion",
> --- `mcp-server/src/tools/claims.ts`

#### EPI-RTE-claim-challenge
Label: Adversarial challenge outcome

Object: [EPI-OBJ-claims](#epi-obj-claims).

Content/update relation: no content change.

Endpoints: phase-4 disproof search → caller challenge/outcome → record_claim_challenge → outcome row consumed by mapped prerequisites. The model is the intended evaluator of each current claim against source code; criterion is an actual overturning mechanism, scoped to the subsystem/revision, not a quota of defeats. Implementation checks the reported outcome: challenge length at least 24 after trimming; survived must reference a current claim and no closing event; overturned/superseded must cite that claim's matching closing event and boundary. Code licenses a recorded challenge, not reliable model search. Normal mapped advance checks for an outcome row per current key-prefix claim; it is enforcing continuation bookkeeping, not a semantic oracle. SRC-1: `.claude/skills/amanuensis/references/phase-4-adversarial.md`, `mcp-server/src/tools/claims.ts`, `mcp-server/src/invariants.ts`. Distinct part of the survey from [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle), which describes host phase orchestration. Countercase: a sufficiently long but uninformative survived string passes the inspected length check; deferred status also bypasses the ordinary forward walk, as supplied runtime establishes. A field note alone is not the structured outcome row the SQL prerequisite queries. The phase-4 text's survived-note recipe therefore needs record_claim_challenge as well before an ordinary mapped advance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: get_claim_challenges returns chronological outcomes; mapped prerequisite reads claim_challenge_outcomes.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Current claim for survived; matching closure event for defeat/replacement; active session and resolvable challenge SHA.
- Invalidation or expiry: Append-only reported outcomes; later passes add rows; validity changes are separate.
- Activation or effect: Permits normal mapped progression when all current claims have an outcome; semantic review remains model-mediated.
- Evidence limits: Doctrinal evidence-consuming challenge is specified; its actual operation, quality and independence are unobserved. Deferred bypass prevents a universal completion guarantee.

> AND NOT EXISTS (
>                 SELECT 1 FROM claim_challenge_outcomes o WHERE o.claim_id = c.claim_id
>               )
> --- `mcp-server/src/invariants.ts`


#### EPI-RTE-claim-withdrawal
Label: Claim invalidation and supersession

Object: [EPI-OBJ-claims](#epi-obj-claims).

Content/update relation: no content change.

Endpoints: caller contradictory evidence/reason → invalidate_claim or supersede_claim → closed exclusive interval, validity event and optional successor on the same key. Code checks current predecessor, strict-descendant boundary and at least one new attached evidence ID; successor gets only newly supplied support and reuses insertClaim checks. The caller judges contradiction and proposes successor text; code checks lineage/admission, not semantic defeat. Operational force: get_claims omits historical rows by default; describe_locus structure filters interval applicability and preserves history routes. This changes reliance selection across sessions, not just a review label. SRC-1: `mcp-server/src/tools/claims.ts`, `mcp-server/src/tools/locus.ts`. Distinct from [RT-RTE-locus-read](runtime.md#rt-rte-locus-read): authority mutation upstream of that consumer. Rejection/rollback: transactional closure-plus-successor avoids losing current authority on a failed successor. No human approval or answer oracle is required in this open request mode.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: Closed claims, contradictory support and supersession rationale remain available in history and ancestry-filtered reads.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Current predecessor, new evidence and a strict descendant of valid_from; unused successor ID for replacement.
- Invalidation or expiry: Exclusive boundary removes the predecessor at and after that commit; historical query remains possible.
- Activation or effect: Withdraws current authority or atomically replaces it, enforcing downstream current selection.
- Evidence limits: A same-valid_from revision correction is refused by strict-descendant logic; this is narrower than unrestricted in-place correction. New evidence ID does not prove semantic contradiction.

> if (!evidenceIds.some((id) => !existing.has(id))) {
>   throw new ToolError("invalidation requires new evidence not already attached to the claim");
> }
> --- `mcp-server/src/tools/claims.ts`

> if (boundary === validFrom || !isAncestor(ctx, validFrom, boundary)) {
> --- `mcp-server/src/tools/claims.ts`

#### EPI-RTE-concern-disposition
Label: Concern evidence quality and disposition

Object: [EPI-OBJ-dispositions](#epi-obj-dispositions).

Content/update relation: no content change.

Endpoints: caller concern classification/rationale/evidence → set_disposition → mutable subsystem-concern row with support attachments. Code checks phase depth, concern existence, resolvable revisions and evidence IDs; evidence_quality cannot outrank the strongest attached kind. The caller/model assesses whether the concern obtains, following phase-3 source-reading criteria. No program checks that classification follows from attached evidence or that the evidence kind was earned. Operational force: the retained row is the concern account; forward phase prerequisites inspect attachments, per supplied runtime. Consumer/channel/horizon: later survey/adversarial agents through query results and published accounts; classification is advisory for interpretation, while metadata checks enforce admission. SRC-1: `mcp-server/src/tools/dispositions.ts`, `.claude/skills/amanuensis/references/phase-3-concerns.md`. Distinct from [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle): concrete disposition writer rather than phase coordinator. Open survey; caller proposes/decides semantic verdict, code vetoes invalid metadata; no reference-answer oracle. Rejected transaction admits neither row nor new attachments. Existing evidence roles are not overwritten by default support attachments.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: get_dispositions and get_disposition_evidence expose retained classifications/evidence to later passes.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: At least one existing resolvable evidence row, valid concern/classification and adequate recorded status.
- Invalidation or expiry: Upsert replaces the current classification/rationale; support links can accumulate and explicit roles remain.
- Activation or effect: Admits concern verdicts and checks claimed evidence quality against supplied kind labels.
- Evidence limits: This is a genuine structured gate but not a verifier of source truth; evidence kind itself is caller supplied.

> if (claimedRank >= 0 && claimedRank < strongestRank) {
> --- `mcp-server/src/tools/dispositions.ts`

> ON CONFLICT(subsystem_id, concern_code) DO UPDATE SET
>              classification = excluded.classification,
> --- `mcp-server/src/tools/dispositions.ts`

#### EPI-RTE-finding-resolution
Label: Repair verification and finding overturn

Object: [EPI-OBJ-findings](#epi-obj-findings).

Content/update relation: no content change.

Endpoints: caller finding/repair/verification → finding and append-only resolution events → later reader defect partitions. add_finding rejects initially fixed or ruled-out status but can create confirmed-bug or confirmed-acceptable at concerns depth without requiring evidence_ids in this writer. update_finding_status fixed requires repair location/SHA and records fixed-pending-verification; verify_finding_fix requires that state, active-session attached fix-verification evidence and repair ancestry. Its Git --is-ancestor accepts the repair commit itself as well as descendants; the nearby strict-descendant comment is stronger than the check. Overturn to ruled-out requires current-session evidence attached to the finding, but requireOverturnEvidence counts any role, not specifically compensating. Caller supplies the verification_note and judges repair correctness; no test runner is invoked here. Result force: verify appends verified-fixed, and locus partitions distinguish awaiting-verification from verified-fixed. Epistemic license is recorded evidence/revision custody for a caller verification assertion, not independent proof the repair works. SRC-1: `mcp-server/src/tools/findings.ts`, `mcp-server/src/invariants.ts`, `mcp-server/src/tools/locus.ts`. Distinct from [RT-RTE-locus-read](runtime.md#rt-rte-locus-read): mutation and verification feeding the reader. Open repair requests; caller proposes and code vetoes custody/state defects; no expected-answer oracle. Rollback is transactional for coarse update/event; history records subsequent reconsideration rather than deleting the previous event.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: Finding resolution history and reader partitions retain pending versus verified repair states for later agents.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Concerns depth, pending repair, matching finding attachment, same active session, fix-verification role and repair lineage.
- Invalidation or expiry: Further status/resolution events change current state while preserving history.
- Activation or effect: Blocks silent fixed-to-verified promotion; delivers verified-fixed only after explicit verification call and metadata checks.
- Evidence limits: No execution, independent repair test, semantic evidence validation or causal repair success established.

> if (evidence.role !== "fix-verification") {
>   throw new ToolError("verification evidence must be attached with role fix-verification");
> }
> --- `mcp-server/src/tools/findings.ts`

> requireAncestor(ctx, fixSha, evidenceSha);
> --- `mcp-server/src/tools/findings.ts`

#### EPI-RTE-contradiction-resolution
Label: Contradiction disposition

Object: [EPI-OBJ-contradictions](#epi-obj-contradictions).

Content/update relation: no content change.

Endpoints: caller incompatible findings → unresolved contradiction → resolve_contradiction → current resolution plus proof-history row. The caller identifies incompatibility and judges resolution; code does not discover logical contradiction. Non-unresolved resolution requires active-session evidence attached to one party, rationale and additionally scope_note for scope-distinction. It records the relational resolution, not automatically rewriting either finding's status. get_contradictions defaults to unresolved, so the resolution removes it from that default attention channel without deleting history. Epistemic license: caller evidence-backed resolution assertion; no proof of logical consistency. SRC-1: `mcp-server/src/tools/contradictions.ts`. No supplied counterpart; distinct from [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission), which concerns decision revisions. Open requests; caller proposes/decides, code vetoes missing custody; no oracle. Failed checks leave the relation unchanged; setting unresolved reopens it.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: get_contradictions(all) and resolution history retain evidence pointer, scope and rationale across sessions.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Existing findings/relation and current-session evidence attached to one conflicting finding for resolution.
- Invalidation or expiry: Can return to unresolved; history appends rather than silently deleting the conflict.
- Activation or effect: Changes default unresolved selection; does not itself fix code or settle the parties' truth.
- Evidence limits: Evidence attachment does not establish that the asserted conflict or scope distinction is logically correct.

> if (!evidence.attached_to_party) {
>   return {
>     ok: false,
>     error: "contradiction resolution evidence must be attached to one of its findings",
>   };
> }
> --- `mcp-server/src/tools/contradictions.ts`


#### EPI-RTE-explanation-record
Label: Explanation recording or decline

Object: [EPI-OBJ-explanations](#epi-obj-explanations).

Content/update relation: no content change.

Endpoints: model/caller whole-body explanation or decline → record_explanation/decline_explanation → append-only slot row. Check target/domain: eligible subject/status, size/prose shape, evidence existence/count, at least one non-name/non-pattern kind and at least one cited subsystem-ledger file, plus resolvable record revision. No minimum length or truth check. Decline instead requires a bounded paragraph reason, not evidence, and can supersede a recorded body. This is retention of a model interpretation or explicit abstention, not acceptance of a produced claim against a correctness criterion. The phase-4 instruction calls for sentence-specific contradictory notes, and phase 5 requests revision or confirmation against those notes; the model's actual criticism and compliance remain unobserved. SRC-1: `mcp-server/src/tools/explanations.ts`, `.claude/skills/amanuensis/references/phase-4-adversarial.md`, `.claude/skills/amanuensis/references/phase-5-packaging.md`. Distinct from [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle): persisted explanation-slot writer. Open surveys; caller proposes whole-body replacement or abstention, code vetoes formatting/metadata defects, no human per-body approval or expected-answer oracle. Failure leaves previous rows intact.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Receipt identifying slot/disposition/revision, not body.
- Later read-back: get_explanations and the mapped explanation-discharge gate select these rows; materializer consumes explanations through its own implementation.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Eligible subject, nonempty bounded body/reason, resolvable revision; recorded bodies additionally need qualifying evidence.
- Invalidation or expiry: A newer recorded/declined/withdrawn row changes effective content without deleting older rows.
- Activation or effect: Makes model-authored explanatory content available and discharges slot obligations, not source correctness.
- Evidence limits: Body semantic preservation/entailment is indeterminate without an actual body and checked source reading. No candidate instance or successful theory revision is established here.

> if (cited.every((row) => NAME_AND_PATTERN_KINDS.includes(row.kind))) {
>   throw new ToolError(RECORD_REFUSALS.namesAndPatterns());
> }
> --- `mcp-server/src/tools/explanations.ts`

> if (inLedger.n === 0) throw new ToolError(RECORD_REFUSALS.notInLedger(subject.id));
> --- `mcp-server/src/tools/explanations.ts`

#### EPI-RTE-explanation-selection
Label: Effective explanation selection

Object: [EPI-OBJ-explanations](#epi-obj-explanations).

Content/update relation: truth-apt transformation: non-ampliative reshaping.

Endpoints: stored slot rows → readExplanation/selectExplanation → get_explanations response and mapped discharge check. Owner: code. It selects greatest row ID with a resolvable ref_sha when workspace binding permits checking; eligibility and recorded/declined/withdrawn disposition determine visible state. It does not run a model or check source entailment, and resolvability here is not the stronger claim-interval ancestry test. Consumer/channel/horizon: tool caller receives whole effective body plus provenance; mapped admission consumes slot state, enforcing recorded-or-declined obligation. Its epistemic license is only a retained revision-bound model account or explicit abstention. SRC-1: `mcp-server/src/invariants.ts`, `mcp-server/src/tools/explanations.ts`. Distinct from [RT-RTE-locus-read](runtime.md#rt-rte-locus-read): dedicated explanation reader and slot gate, not structure-section selection. Concrete implementation-layer deduction without target execution: for an eligible subject and two resolvable rows id=1 recorded and id=2 declined, iteration chooses id=2 and returns declined, not the older explanation. If id=2 is withdrawn, state is not-recorded and no body is returned; it does not fall back to id=1. This bounds claims that retaining prose implies present endorsement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Effective body or explicit declined/not-recorded state with provenance.
- Later read-back: Each later invocation reselects retained rows; current body and earlier-row count are returned.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Eligibility, greatest ID among resolvable revisions; without bound workspace newest row is unchecked.
- Invalidation or expiry: Newer decline/withdrawal can remove a positive account; status ineligibility yields not-recorded.
- Activation or effect: Selects or withholds an account and discharges or blocks mapped slot obligations; no semantic acceptance is implied.
- Evidence limits: Dedicated reader inspected; full materializer rendering and actual downstream reasoning from the body are not established by this deduction.

> if (effective === null || row.id > effective.id) effective = row;
> --- `mcp-server/src/invariants.ts`

> return { state, row: state === "not-recorded" ? null : effective, checked, earlierRows };
> --- `mcp-server/src/invariants.ts`

#### EPI-RTE-diagnosticity-resolution
Label: Competing concern matrix

Object: [EPI-OBJ-diagnosticity](#epi-obj-diagnosticity).

Content/update relation: no content change.

Endpoints: caller competing concerns/evidence → matrix and caller cell verdicts → caller leading_concern/outcome → get_diagnosticity_matrix. The description prescribes inconsistency ranking; inspected resolve_diagnosticity_matrix only checks that resolved has a leader and that any leader belongs to the matrix, then writes it. It neither computes inconsistency ranking nor requires every cell. Thus the model/caller is the evaluator of concern fit and selector; code enforces membership, not comparative validity. Epistemic license: recorded comparison judgments, not a proven winning explanation. Operational force is advisory through later caller reads; phase 3 instructs resolution before dispositions but the inspected resolver does not itself call set_disposition. SRC-1: `mcp-server/src/tools/diagnosticity.ts`, `.claude/skills/amanuensis/references/phase-3-concerns.md`. No supplied counterpart; different from [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission)'s numerical qualification. Open diagnostic request; caller can choose unresolved-competition, no independent answer oracle, no demonstrated downstream selection. Revisions upsert cell verdicts and update outcome rather than proving a criticism loop occurred.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: Matrix reader exposes cells and named outcome to later survey reasoning.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: At least two existing concern codes on opening; cell concern/evidence membership; leader membership on resolution.
- Invalidation or expiry: Cell verdicts and outcome can be overwritten through the tools; no expiry shown in resolver.
- Activation or effect: Records comparison outcome; no autonomous rejection or numerical ranking of hypotheses in the inspected resolver.
- Evidence limits: Doctrinal ordering is not host-enforced reasoning, exhaustive evidence coverage or observed correct diagnosis.

> if (outcome === "resolved" && !leadingConcern) {
>   return { ok: false, error: "resolved outcome requires leading_concern" };
> }
> --- `mcp-server/src/tools/diagnosticity.ts`

> UPDATE diagnosticity_sessions
>              SET outcome = ?, leading_concern = ?, linchpin_note = ?, resolved_at = datetime('now')
>            WHERE id = ?
> --- `mcp-server/src/tools/diagnosticity.ts`

#### EPI-RTE-review-aggregation
Label: Independent-role review aggregation

Object: [EPI-OBJ-review-analysis](#epi-obj-review-analysis).

Content/update relation: truth-apt transformation: entailed derivation.

Endpoints: dispatched role packets → caller judgments/new evidence → land_review_pass → aggregate_review_analysis → retained keys and survived/defeated/contested report. Owner: code for custody/fan-in/status; caller models for judgments. Check domain: exact frozen hypotheses reconciled by non-generators, permitted packet evidence, newly discovered evidence for refuter overturn, budget and complete role fan-in. Generators receive published briefs/catalog; refuters hypotheses; verifiers verification packets. Those packet distinctions are implemented context selection, not proof hosts have fresh isolated contexts. Aggregation derives status from stored judgments: verified defeat requires intersection between discovered refuter-overturn evidence and verifier-overturn evidence; otherwise unanimous upheld survives, all else contests. Intended use/scope: observe-only review analysis at reviewed_sha; allowed_actions inspect/report, not code acceptance/merge/deployment. Epistemic license: a checked derivation about recorded judgments, conditional on their accuracy and packet custody. Operational force: report's retained_finding_keys feeds review scoring; no automatic promotion into ordinary claims/findings is shown in this aggregate handler. SRC-1: `mcp-server/src/tools/review-analysis.ts`. No supplied counterpart; distinct from ordinary [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle). Caller proposes/semantically judges, code vetoes deficient custody/fan-in and computes final selection. No answer oracle until separate blind reveal/scoring. Failed budget can mark run failed; contaminated/failed runs reject landing.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: readAnalysis returns persisted judgments/aggregation; score_review_evaluation consumes retained keys.
- Delegated visibility: Role-specific packets select published brief/catalog, hypotheses or verification packets; host context isolation is not established.
- Selection predicate: Dispatched valid pass, exact hypothesis coverage, budget, evidence scope/packet membership, then complete role fan-in.
- Invalidation or expiry: Contamination/failure block landing; aggregate status preserves disagreements and defeated hypotheses.
- Activation or effect: Computes retained review keys, not product deployment permission. Packet authority is observe-only policy, not an OS sandbox.
- Evidence limits: No execution or independence/benefit observation; a formal status from model judgments cannot authenticate source truth.

> const finalStatus = verifiedDefeat ? "defeated" : unanimousUphold ? "survived" : "contested";
> --- `mcp-server/src/tools/review-analysis.ts`

> .filter((result) => result.final_status === "survived")
>       .map((result) => result.finding_key)
>       .sort(),
> --- `mcp-server/src/tools/review-analysis.ts`

#### EPI-RTE-review-scoring
Label: Blind review reference scoring

Object: [EPI-OBJ-blind-truth](#epi-obj-blind-truth).

Content/update relation: truth-apt transformation: entailed derivation.

Endpoints: terminal aggregate + caller salted sealed truth → reveal_review_analysis_truth → score_review_evaluation → report. Program checks assignment/replicate and seal, records canary contamination and excludes contaminated runs; derives predicted/expected exact equality, Jaccard retest stability and red/valid status under per-condition/arm coverage and surface-shape checks. Target/domain: agreement of retained finding keys with caller-provided expected keys in blind review arms, not general architectural truth. Expected-answer oracle: revealed truth keys, supplied by caller and committed via hash; hash equality protects continuity, not correctness or independence of the supplied reference. Force: returns and retains an evaluation report, without a downstream activation consumer established in this trace. SRC-1: `mcp-server/src/tools/review-analysis.ts`. Distinct from [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission): this is review evaluation, not learning-policy activation. Bounded comparison mode; computation derives scores, caller supplies reference/outcomes and can select run IDs; no authenticated human review inferred. Refusal for seal mismatch or repeat evaluation; red is a retained result, not an exception proving no state was written. A concrete implementation deduction: predicted keys [a] and expected [a,b] make exact false and append differs-from-sealed-truth to red reasons; this is reference mismatch, not a causal explanation of why a reviewer missed b.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: Review evaluation row/report is durable and returned; later activation use is uninspected.
- Delegated visibility: Blind reference is revealed only after terminal aggregate/contaminated status; arbitrary external host visibility is not controlled by this function.
- Selection predicate: Revealed reference per run; uncontaminated aggregated rows included, others excluded; required arms and replicates checked.
- Invalidation or expiry: Contamination excludes a run; evaluation IDs cannot be overwritten by this writer.
- Activation or effect: Produces valid/red measured-agreement report; no code-change authority follows from this check alone.
- Evidence limits: No supplied trial was inspected. Conditions/arms support comparison design, not observed success or independent component causal effects.

> exact: stableJson(predicted) === stableJson(expected),
> --- `mcp-server/src/tools/review-analysis.ts`

> if (!report.exact)
>           redReasons.push(`${condition}/${arm}/${report.run_id} differs from sealed truth`);
> --- `mcp-server/src/tools/review-analysis.ts`

#### EPI-RTE-research-landing
Label: External result provenance admission

Object: [EPI-OBJ-research-results](#epi-obj-research-results).

Content/update relation: truth-apt transformation: acquisition/import.

Endpoints: caller external source records/claims/artifacts → land_research_result for dispatched request → durable result, sources, claims and code-contradiction links. Owner: code checks; external reading and claim authorship are caller supplied. Domain: valid source IDs, held excerpts for directly-read/snippet status, confidence/source-count/access constraints and destination matching. chain_degradation records worst declared access status; verified needs at least two directly-read sources, corroborated needs two accessible sources. These are warranted metadata constraints, not tests that two sources are independent or that excerpts imply the statement. Source warrant: unknown; the route retains excerpts and declared degradation but does not authenticate source contents. Contradicting code observations remain separate linked records; the landing function does not invalidate them. SRC-1: `mcp-server/src/tools/research.ts`. Distinct from [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission): imported evidence can inform a decision but landing does not accept a decision. Trigger: dispatched bounded external question; caller proposes, code vetoes shape/custody. No expected-answer oracle. Transaction stores result and transition atomically; rejection preserves dispatched state.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: get_research_request exposes landed sources/claims for later decision-related consumption.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Dispatched request with durable artifacts, source references, confidence/access thresholds and matching destination.
- Invalidation or expiry: Expiry has a separate exposed operation; full queue admission/expiry caller chain is not assessed here.
- Activation or effect: Admits imported statements with explicit provenance/degradation and contradiction links; not automatic source-truth acceptance.
- Evidence limits: External contents beyond the frozen repository are not additional evidence in this analysis. Reported directly-read status is caller assertion.

> if (confidence === "verified" && (citedSources.length < 2 || chainDegradation !== 0)) {
>   throw new ToolError("verified external claims require at least two directly-read sources");
> }
> --- `mcp-server/src/tools/research.ts`

> if (status === "snippet" || status === "via-agent") return 1;
> --- `mcp-server/src/tools/research.ts`

#### EPI-RTE-research-consumption
Label: Declared research use

Object: [EPI-OBJ-research-results](#epi-obj-research-results).

Content/update relation: no content change.

Endpoints: landed research result → consume_research_result → consumption/effect record and consumed request. It requires no-change reason or a changed-effect statement and destination matching an external claim from this result. Consumer/channel/force/horizon: caller records intended decision-premise/option/hypothesis/confidence effect in SQLite; later queue readers can see consumption. The handler does not mutate the target decision revision or verify its semantic change. Thus it is use accounting, not evidence of acceptance followed by lifecycle integration at the named destination. Caller proposes and declares effect, code can veto destination mismatch; no independent answer oracle. SRC-1: `mcp-server/src/tools/research.ts`. Distinct from [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission), which separately changes decision authority. Rejection leaves result landed; transaction binds consumption to request transition. A possible no-change result is explicit and retained.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: Consumption rows and consumed queue state reach later get/list research queries.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Landed result; changed effect must cite a matching external claim target, or no-change supplies only a reason.
- Invalidation or expiry: Consumed state is terminal under the advertised expiry contract; destination rollback is outside this handler.
- Activation or effect: Records reconciled use or no-change and reports changed boolean; does not itself update target content.
- Evidence limits: No target decision mutation or later behavior is demonstrated by effect_statement or changed=true.

> if (externalClaim.target_kind !== effectKind || externalClaim.target_ref !== targetRef) {
>   throw new ToolError("consumption effect must match the cited external claim destination");
> }
> --- `mcp-server/src/tools/research.ts`

> changed: effectKind !== "no-change",
> --- `mcp-server/src/tools/research.ts`

#### EPI-RTE-staleness-clear
Label: Freshness assertion

Object: [EPI-OBJ-stale-ledger](#epi-obj-stale-ledger).

Content/update relation: no content change.

Endpoints: caller file/revision → clear_staleness → ledger stale=0/new ref_sha. Code refuses absent rows, but the inspected handler uses requireString for ref_sha without resolving it or verifying re-examination. The caller/model is responsible for the refresh instruction's claim that it re-examined this file at this commit. This is a freshness assertion, not acceptance or repair verification. get_stale_backlog consumes the stale flag; clearing removes the row from that backlog and deletes its absent scope-gap row. Operational force: deterministic backlog selection now; future model work selection is advisory via returned backlog. SRC-1: `mcp-server/src/tools/stale.ts`; doctrine is in [boundary](boundary.md#boundary-and-evidence). Distinct from [RT-RTE-locus-read](runtime.md#rt-rte-locus-read): freshness mutation, not account delivery. No active-session check appears in this handler, unlike add_evidence; no universal session-bound writer guarantee follows from this source. Caller initiates/claims examination, code vetoes missing/absent row; no oracle or semantic test.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler result or refusal as described above; no observed execution is asserted.
- Later read-back: Later backlog reads select stale=1, so a cleared row no longer appears there.
- Delegated visibility: No separate delegated context is created by this handler; any permitted caller can receive its response. Actual host grants and cross-agent exposure are uninspected.
- Selection predicate: Existing scoped file not recorded absent; string revision supplied.
- Invalidation or expiry: Later change detection can mark stale again; clear itself does not re-examine source.
- Activation or effect: Clears stale markers and changes the recorded examination revision; no new warrant is established.
- Evidence limits: Full detect_changes/refresh/revalidation chain remains partially inspected; no system-wide claim of freshness accuracy.

> const refSha = requireString(args, "ref_sha");
> --- `mcp-server/src/tools/stale.ts`

> SET stale = 0, stale_since = NULL, stale_reason = NULL, ref_sha = ?
> --- `mcp-server/src/tools/stale.ts`

### Claims

#### EPI-CLM-earned-reliance
Label: Earned codebase reliance

Claimed operation: agents can rely on an evidence-backed living map; write gates prevent claims outrunning evidence and partial work masquerading as completion. SRC-1: `README.md`, doctrine/design. Distinct from [RT-CLM-autonomous-survey](runtime.md#rt-clm-autonomous-survey), which claims autonomous scope/phase continuation rather than content warrant. The same README explicitly leaves longitudinal utility unestablished; this limits a broad product reading without nullifying implemented gates. See [EPI-RTE-claim-admission](#epi-rte-claim-admission), [EPI-RTE-claim-challenge](#epi-rte-claim-challenge), [EPI-RTE-concern-disposition](#epi-rte-concern-disposition) and [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) for narrower enforcement domains.

> Those rules are enforced when records are written. A claim cannot outrun its evidence,
> partial work cannot masquerade as completion, and “fixed” cannot silently become
> “verified-fixed.”
> --- `README.md`

> What has not been established yet is the longitudinal product claim: how useful the
> conspectus remains as a real project changes, how much repeated explanation and
> verification it saves, and where the workflow creates friction.
> --- `README.md`


#### EPI-CLM-explanation-limits
Label: Explanation warrant limit

Claimed operation: model-authored, revision/evidence-bound explanation orients readers but has no truth gate. SRC-1: `README.md`, doctrine/design. No supplied counterpart: a distinct explicit limitation on the explanation object, not a contrary reading of the autonomous survey claim.

> No gate checks that an explanation is
> true: it orients a reader, while claims remain the home of individually checkable rules.
> --- `README.md`


#### EPI-CLM-repair-proof
Label: Evidence-proven repair

Claimed operation: independently challenged concerns can be acted on without redoing review, and repairs stay unverified until new evidence proves them at the repair revision. SRC-1: `README.md`, doctrine/design. This is a distinct consequential repair-use claim within the broader earned-reliance claim, not identical to [RT-CLM-autonomous-survey](runtime.md#rt-clm-autonomous-survey). [EPI-RTE-finding-resolution](#epi-rte-finding-resolution) supports explicit pending/verified separation while bounding “proof” to caller verification plus custody checks.

> - **Act on findings without redoing the review.** Concerns are independently challenged;
>   repairs remain unverified until new evidence proves them at the repaired revision.
> --- `README.md`


### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; concrete consumer/channel/force/horizon fields are owned by the route declarations and supplied runtime records.
