---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LLM Project Wiki's source acquisition, compiled-page reliance and maintenance checks: what licenses later answers at the frozen prompt boundary."
run-id: AAS-2026-10-14-llm-project-wiki-c6c664168f3e-01
reviewed-boundary: "1fdfba9129a46afd18aa68a83f12d6716ab694c6"
---

# LLM Project Wiki epistemic report

## Source-and-claim boundary

The question is whether compiled project pages acquire a checked warrant for later answers, or principally receive operational priority. The target is the complete two-file prompt package, not an installed vault or Claude Code. Scope, exclusions and evidence identity are in [the boundary](boundary.md#boundary-and-evidence); sources are in its [Source register](boundary.md#source-register). SRC-1 supplies doctrine/design and attributed example operation, not an inspected deployment, execution trace or causal experiment.

Both tracked files were read directly and completely at the frozen revision, independently of the supplied runtime account. No executable CLI dispatch, hook registration, tool registry or provider call is shipped. The material exposed operations are the pasted setup and the commands it asks a host model to generate. Embedded shell examples have inspectable text semantics, but do not establish installed implementation or observed operation. The runtime's bootstrap, lookup, sync, ingest and audit containers remain valid; this report separates their epistemic functions rather than superseding them.

| Entry point or operation | Directly read source path | Record coverage | Limit and conclusion prevented |
|---|---|---|---|
| New-project setup, audit questions, page construction, self-audit | SRC-1, `SETUP_PROMPT.md`, Phases 0–3 and 6 | [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | No generated pages or results; actual derivations and semantic correctness unassessed. |
| Copying, authority header, source timestamp reconciliation | SRC-1, `SETUP_PROMPT.md`, Phase 2, G1–G2 | [RT-RTE-source-sync](runtime.md#rt-rte-source-sync), [EPI-OBJ-sources](#epi-obj-sources) | No installation or source provenance; preservation/completeness in use unknown. |
| Diff ingest, dry-run, gap resolution, new pages | SRC-1, `SETUP_PROMPT.md`, Phase 2 | [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), [EPI-OBJ-log](#epi-obj-log) | No revisions or trace; admission cannot be equated with acceptance. |
| Wiki-first questions/edits, optional status and phase-completion callers | SRC-1, `SETUP_PROMPT.md`, Phase 4 | [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup), [RT-BAP-project-rules](runtime.md#rt-bap-project-rules), [EPI-OBJ-index](#epi-obj-index) | Host loading/compliance and answer correctness unknown. |
| Templates, schema, health dashboard, lint/query conventions | SRC-1, `SETUP_PROMPT.md`, Phase 1 | [RT-OBJ-schema](runtime.md#rt-obj-schema), [EPI-RTE-schema-check](#epi-rte-schema-check) | No generated queries or plugin implementation; dashboard execution unassessed. |
| Existing-vault audit, source/entity coverage, graph/schema repair, protocol changes and audit log | SRC-1, `SETUP_PROMPT.md`, G0–G7 | [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit), [EPI-RTE-link-check](#epi-rte-link-check), [EPI-RTE-schema-check](#epi-rte-schema-check) | Prescribed repair is not evidence of repaired installation or better future capacity. |
| Persistence housekeeping/manuals and public capability claims | SRC-1, `SETUP_PROMPT.md`, Phase 5 and Quality Bar; `README.md` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge), [EPI-CLM-answer-coverage](#epi-clm-answer-coverage), [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness) | Tracking instructions do not show persistence/reload; README counts do not show correctness or causal benefit. |

All shipped material paths are assessed at the design layer. Missing project sources prevent individuating actual truth-apt premises. Missing vault pages prevent classifying particular summaries, explanations and decision rationales. Missing host/run evidence prevents establishing activation, acceptance or withdrawal in use. Missing comparisons prevent attributing improved answers or efficiency to wiki-first selection. Provider state is opaque as bounded by [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code); no conclusion about parameter learning follows.

Consequential claims are [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge), [EPI-CLM-answer-coverage](#epi-clm-answer-coverage), [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first), [RT-CLM-sources-immutability](runtime.md#rt-clm-sources-immutability) and [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness).

## Epistemic-object inventory

Each row refers to a specified artifact, not an available generated instance. Owned identity, form and consumer fields are in the cited records.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-sources](#epi-obj-sources) | Acquired project memories, docs, rules and code references; individual propositions not determinable | see record | SRC-1, `SETUP_PROMPT.md`, Phase 2 | Original authorship, accuracy and copy outcomes unknown. |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Signatures/schemas, implementation constraints, cross-entity explanations, decisions/rejected alternatives and current project state | see record | SRC-1, `SETUP_PROMPT.md`, Phase 3 | Exact content, entailment and initial lineage unavailable. |
| [EPI-OBJ-index](#epi-obj-index) | Intent-to-page mappings and coverage associations; dashboard metadata predicates | see record | SRC-1, `SETUP_PROMPT.md`, Phase 1 | Selection relevance is model-authored; plugin execution uninspected. |
| [EPI-OBJ-log](#epi-obj-log) | Statements of missing/wrong content, ingest history, audit outcomes | see record | SRC-1, `SETUP_PROMPT.md`, Phases 4, 6, G7 | Logged result is not independent evidence of its own truth. |
| [RT-OBJ-schema](runtime.md#rt-obj-schema) | Primarily maintenance policy, not a factual project answer | see record | SRC-1, `SETUP_PROMPT.md`, Phase 1 | Required keys and conventions guide writes; enforcement unknown. |
| [RT-OBJ-wiki-ingest](runtime.md#rt-obj-wiki-ingest) | Primarily selection/revision policy | see record | SRC-1, `SETUP_PROMPT.md`, Phase 2 | Generated command and activation unavailable. |
| [RT-OBJ-setup-prompt](runtime.md#rt-obj-setup-prompt) | Current-run guidance, including proposed maintenance machinery | see record | SRC-1, `SETUP_PROMPT.md` | Not accumulated memory; instructions are not outcome evidence. |
| [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) | Distributed-parametric model content not determinable from these sources | see record | SRC-1, `README.md` | Version, changing weights and endpoint routing uninspected. |

## Authority-route ledger

These are sparse function-level overlays. Fields owned by canonical records use `see`; function classification and architectural status are local. All routes below are **doctrine only**: their installed behavior was not inspected. Neither a requested check nor a metadata update constitutes an evidence-consuming acceptance decision.

Route ID: [RT-RTE-source-sync](runtime.md#rt-rte-source-sync)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-sources](#epi-obj-sources).
Content/update relation: truth-apt transformation: acquisition/import. Source warrant is unknown; copying imports content, not confirmation of its claims. The specified header adds policy without validating the copied propositions.
Transition or check target: project material into Sources copies.
Evaluator/condition and domain: see route; shell path/existence/update conditions, not a truth evaluator.
Activation and timing; possible or observed result; implemented force: see route. Described copying and header insertion, no observed result.
Epistemic authority and scope: source-reference status, not certification.
Operational authority and behavioral-authority path: see route; future ingest model receives copied files as references, advisory force over later maintenance invocations.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, Phase 2.
Claim IDs: [RT-CLM-sources-immutability](runtime.md#rt-clm-sources-immutability). Mismatch marker: literal immutability/read-only is qualified by sync and manual copy; header is interpretation policy.
Gap/limit: copied facts and provenance unavailable; suppressed errors and timestamp replacement do not license a complete/fresh-source claim.

Route ID: [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap), [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: truth-apt transformation: indeterminate. Literal excerpts could be non-ampliative reshaping; explanations could be entailed derivations or ampliative conjectures. Neither non-entailment nor semantic preservation is established for absent pages. Original source and generated page pairs would decide the edge, not the word “compiled.”
Transition or check target: sources/current pages into candidate project descriptions, explanations and rationales.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see cited routes; instructed host model writes domain pages, section updates or source-based repairs.
Epistemic authority and scope: candidate descriptions only; no checked derivation or accepted ampliative claim established.
Operational authority and behavioral-authority path: written Wiki pages are intended references for later lookup; see [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup). Advisory content receives primary-reference ranking through project rules over later sessions.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, Phases 2–3, G3.
Claim IDs: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge). Mismatch marker: semantic compilation and accumulation do not confer warrant.
Gap/limit: source inspection is prescribed and can correct a page; this is stronger than unconstrained generation, but no actual semantic comparison result is supplied.

Route ID: [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap), [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index).
Content/update relation: no content change.
Transition or check target: project/entity coverage and the ability to answer the Quality Bar's project questions from wiki pages.
Evaluator/condition and domain: host model compares entity inventory/pages and judges sufficiency. No expected correct answer or independently executed semantic test is supplied.
Activation and timing; possible or observed result; implemented force: see routes; bootstrap self-audit, ongoing insufficiency, and G3 scans produce requested gap/stale findings, not observed scores.
Epistemic authority and scope: at most assessed coverage or task sufficiency; answering without source access alone does not certify the answer.
Operational authority and behavioral-authority path: gap findings guide source fallback, new pages and repairs through log/maintenance channels; see [EPI-OBJ-log](#epi-obj-log) and [RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules). Advisory guidance across subsequent maintenance rounds.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, Phase 6, Quality Bar, G3.
Claim IDs: [EPI-CLM-answer-coverage](#epi-clm-answer-coverage), [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness). Mismatch marker: sufficiency is not semantic correctness.
Gap/limit: no run/result/consumer trace; source reconciliation is a possible contrary witness to a claim that the design never checks content.

Route ID: [EPI-RTE-schema-check](#epi-rte-schema-check)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: key-string presence only, not valid frontmatter, source truth or semantic fidelity.
Operational authority and behavioral-authority path: see record; diagnostics feed requested repairs, advisory within an audit invocation.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, G5.
Claim IDs: [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness). Mismatch marker: no `sources` check; body strings can pass.
Gap/limit: model review could exceed the example, but such review is unobserved.

Route ID: [EPI-RTE-link-check](#epi-rte-link-check)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: limited syntactic navigation evidence; no support for the truth of linked assertions or relevance of a link.
Operational authority and behavioral-authority path: see record; model repairs links/index/pages from diagnostics, advisory within audit.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, G4.
Claim IDs: [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness). Mismatch marker: prefix/substring matches are weaker than exact target/index membership.
Gap/limit: supplied examples need interpretation; diagnostics are not correctness oracles.

Route ID: [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap), [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [RT-OBJ-schema](runtime.md#rt-obj-schema).
Content/update relation: no content change.
Transition or check target: admission of model-authored pages, revisions and maintenance instructions into the installation, not established epistemic acceptance.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see routes. Model proposes, judges and writes; user starts and later commits; no required independent veto, post-preview approval or atomic rollback.
Epistemic authority and scope: no recorded evidence-consuming acceptance naming criterion, intended use and scope found in the two shipped files. Quality and source-reference criteria guide work but are not a retained acceptance decision.
Operational authority and behavioral-authority path: direct requested writes permit later use/maintenance; see [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) and [RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules).
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, Phases 2–4, G1–G6.
Claim IDs: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge). Mismatch marker: operational admission differs from epistemic acceptance.
Gap/limit: host veto possibilities uninspected; audit is recovery rather than demonstrated rejection/withdrawal of a bad claim.

Route ID: [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap), [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index), [EPI-OBJ-log](#epi-obj-log).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see routes; filesystem artifacts and logs requested, with tracking conventions.
Epistemic authority and scope: availability for reliance, not corroboration or accepted status.
Operational authority and behavioral-authority path: see routes; later model reads page/index/log through lookup or maintenance, advisory/ranking over future sessions.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, Phases 1, 5–6, G7.
Claim IDs: [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge). Mismatch marker: retained/cross-linked candidates are not lifecycle integration after acceptance.
Gap/limit: no accepted claim or corresponding post-acceptance lifecycle route established; linking and indexing themselves are prescribed organization of retained candidates.

Route ID: [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-index](#epi-obj-index), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: no content change.
Transition or check target: page selection and source/memory fallback, not answer validation.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route; intent mapping and model sufficiency select requested context, while `/status` explicitly falls back if stale.
Epistemic authority and scope: primary-reference priority for project answers; no checked truth license.
Operational authority and behavioral-authority path: see [RT-BAP-project-rules](runtime.md#rt-bap-project-rules); future model, live instruction files, policy/ranking force across sessions. No access-control prohibition on source reading established.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, Phase 4.
Claim IDs: [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first), [EPI-CLM-answer-coverage](#epi-clm-answer-coverage). Mismatch marker: continuation without source read is not epistemic warrant.
Gap/limit: general lookup has no explicit stale-page rejection gate; special status fallback is a contrary witness to a universal claim that staleness never changes consumption.

Route ID: [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup), [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)
Route function: lineage/freshness/recovery
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-sources](#epi-obj-sources), [EPI-OBJ-log](#epi-obj-log).
Content/update relation: no content change for status/date bookkeeping; source/page content changes belong to the transformation rows.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see routes. Code-edit path grep requests stale marking; one-comparison Git selection plus source/page reads request refresh; broader audit compares inventories/timestamps and updates stale pages.
Epistemic authority and scope: dependencies and possible obsolescence, not endorsement. Date bump does not prove correction; no retained evidence-version pin is specified.
Operational authority and behavioral-authority path: see routes; stale flags/log gaps reach maintenance, status fallback and health queries; advisory selection over later invocations.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, Phases 2, 4, G2–G3.
Claim IDs: [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness). Mismatch marker: diff selection and documented grep do not enforce universal refresh.
Gap/limit: no automatic withdrawal of all stale claims, transactional rollback or verified propagation established. Source fallback and later repair remain meaningful prescribed recovery paths.

Route ID: [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)
Route function: behavior/policy adaptation
Architectural status: doctrine only
Object/candidate ID: [RT-OBJ-schema](runtime.md#rt-obj-schema), [RT-OBJ-wiki-ingest](runtime.md#rt-obj-wiki-ingest).
Content/update relation: non-truth-apt policy/content update: repair script coverage, command procedures and wiki-first/stale/ingest wiring.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route; checklist diagnosis leads to requested direct patches, without testing the wiki-first premise itself.
Epistemic authority and scope: policy repair does not prove the policy superior or project facts true.
Operational authority and behavioral-authority path: see [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) and [RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules); intended live future-session instructions, contingent on host loading/compliance.
Evidence source ID and local anchor: SRC-1, `SETUP_PROMPT.md`, G1, G2, G6.
Claim IDs: [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness). Mismatch marker: none beyond unobserved activation.
Gap/limit: the runtime's separate reflection/self-improvement assessments remain bounded by its route evidence; no exercised causal chain or improved capacity is supplied.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | see record | SRC-1, `README.md`; doctrine/design | see record and [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap) | None inspected as installed routes | README reports page counts; no reproducible trace or semantic check | No comparison; accumulating pages does not show compounding warranted knowledge | Persistent compilation is specified | Production/acceptance of new warranted claims unestablished |
| [EPI-CLM-answer-coverage](#epi-clm-answer-coverage) | see record | SRC-1, `SETUP_PROMPT.md`; doctrine/design | Quality questions and gap logging | None inspected | None supplied | Wiki-only answers need not be correct; source checks and fallback are permitted | A task-relative sufficiency target is specified | Correct answer coverage and transfer unknown |
| [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first) | see record | SRC-1, `SETUP_PROMPT.md`; doctrine/design | see [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup) | None inspected | None supplied | Host compliance uninspected; edit/audit/fallback paths qualify universality | Operational ranking policy | Not a truth gate or demonstrated source-read reduction |
| [RT-CLM-sources-immutability](runtime.md#rt-clm-sources-immutability) | see record | SRC-1, `README.md`, `SETUP_PROMPT.md`; doctrine/design | see [RT-RTE-source-sync](runtime.md#rt-rte-source-sync) | None inspected | None supplied | Imports/header do not check truth; copy/manual repair changes files | Reference versus compiled-layer distinction | Literal immutability and instruction isolation not enforced |
| [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness) | see record | SRC-1, `SETUP_PROMPT.md`; doctrine/design | see [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit), [EPI-RTE-schema-check](#epi-rte-schema-check), [EPI-RTE-link-check](#epi-rte-link-check) | None inspected | None supplied | Partial text predicates, generated implementation unavailable; no causal experiment | Multi-category inspection and repair specified | No system-complete correctness, fresh coverage or automatic enforcement |

## Bounded conclusion

The design imports project material whose source warrant is unknown, and asks a model to produce persistent, linked project pages. The content spans literal excerpts, descriptive summaries, explanations and decision rationales. No actual source/page pair supports a checked derivation or a positively classified ampliative conjecture. Retention and operational use are prescribed, not observed. See [EPI-OBJ-sources](#epi-obj-sources) and [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).

The design does contain checks: source/entity reconciliation, task-sufficiency judgments, graph diagnostics, metadata checks and stale/timestamp repair. These have separate licenses. G5's key-presence checks do not validate frontmatter or truth; G4's navigation checks do not establish relevance or semantic correctness. The model is instructed to consume findings to repair pages or methods, but no evaluated result and consequential deployed consumer is supplied. See [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit), [EPI-RTE-schema-check](#epi-rte-schema-check) and [EPI-RTE-link-check](#epi-rte-link-check).

No recorded epistemic acceptance decision against a named criterion, intended use and scope was found in either shipped file. There are quality criteria and direct model admission instead. This bounded finding is about the package, not opaque model reasoning or all possible installations. Linking admitted candidates to pages, index and sources is not demonstrated lifecycle integration after acceptance.

The strongest specified authority is operational: wiki pages rank first for project answers, maintenance schema/commands guide revisions, and gap/stale records guide later repair. A special status consumer uses stale fallback; ordinary lookup lacks an explicit general stale-rejection gate. The source-edit and audit paths can bypass wiki-only reading. All force remains host/model-mediated policy, not inspected enforcement. See [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup), [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) and [RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules).

Audit can directly revise future behavior-guiding machinery without producing or accepting a truth-apt project claim. That prescribed pathway does not establish improved capacity, exercised self-improvement, theory criticism/iteration, or parameter learning. Those properties are independent; the runtime's bounded findings remain unchanged. Public “compiled knowledge” and wiki-only answer coverage are supported as intended organization and use, not demonstrated knowledge warrant or benefit.

## Shared records

### Operative objects

#### EPI-OBJ-sources
Label: Sources reference layer

Source-native identity: `Sources/Memory/`, `Sources/Rules/`, `Sources/Docs/`. Specified filesystem snapshots, not shipped generated artifacts. Natural-language project assertions and archived policies coexist with symbolic code/config excerpts. Imported text is later interpreted by the ingest/audit model; symbolic excerpts may describe code but no shipped evaluator runs them. Original human/model authorship and warrant are unknown.

Distinct from [RT-OBJ-setup-prompt](runtime.md#rt-obj-setup-prompt), which is current invocation guidance. [RT-RTE-source-sync](runtime.md#rt-rte-source-sync) describes its acquisition, not the stored referent. No supplied object counterpart after comparison. SRC-1, `SETUP_PROMPT.md`, Phases 1–2. The warning header is selected interpretive policy, not validation; the supplied source-sync record retains that passage.

> A bash script that copies project memory/docs into `Sources/`. Adapt paths for this project's structure. Standard pattern:
> --- `SETUP_PROMPT.md`

#### EPI-OBJ-wiki-pages
Label: Wiki compiled pages

Source-native identity: `Wiki/` pages, specified generated Markdown stored in the vault filesystem and requested to remain Git-tracked. Distinct operative parts: natural-language descriptions, constraints, explanations and decision rationales consumed by the model; symbolic verbatim signatures/schemas/code excerpts used as project references; frontmatter keys/status/path/date metadata used by shell/query selectors. These paths differ in epistemic function; none has an available instance here. Natural-language facts guide answers by interpretation, while selectors give metadata fixed matching semantics. Source paths supply intended lineage but not immutable evidence versions.

Distinct from [RT-OBJ-schema](runtime.md#rt-obj-schema), which governs maintenance. [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap) and [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest) produce/revise this object rather than duplicate its identity. No supplied object counterpart after comparison. SRC-1, `SETUP_PROMPT.md`, Phase 3.

> **Entity pages MUST include:**
> - `source_file:` frontmatter pointing to the exact file
> - Full function/class signatures with TypeScript types
> - Full schema definitions (Zod, Prisma, SQL DDL — whatever is used)
> --- `SETUP_PROMPT.md`

> **Decision pages MUST include:**
> - The decision made
> - Why (the forces, constraints, and context that drove it)
> - What was rejected and why
> - Consequences
> --- `SETUP_PROMPT.md`

These fields request content, not an acceptance record. Particular explanations could be copied, derived or conjectured; absent source/page pairs prevent deciding.

#### EPI-OBJ-index
Label: Semantic Lookup and health navigation

Source-native identity: generated `index.md` and `Wiki/_Health.md`, stored as Markdown in the vault. Semantic Lookup and TOC mappings are model-authored natural-language navigation aids with symbolic wikilink targets. Health-query code is symbolic text intended for Dataview; concrete queries and plugin behavior are unavailable. Intent mapping selects facts to read; metadata predicates flag stale/old/orphan/key-missing candidates, not false claims. These are distinct from the maintenance conventions in [RT-OBJ-schema](runtime.md#rt-obj-schema) and from the consumer [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup); no supplied object counterpart after comparison. SRC-1, `SETUP_PROMPT.md`, Phase 1.

> 2. A **Semantic Lookup** table: "question / intent → wiki page" (15–20 entries covering the most common LLM questions about this project)
> 3. A full TOC grouped by domain, with `[[wikilinks]]` to every wiki page
> 4. A Dataview block for stale pages (requires Dataview plugin)
> --- `SETUP_PROMPT.md`

> - Schema violations (pages missing `type` or `updated`)
> --- `SETUP_PROMPT.md`

#### EPI-OBJ-log
Label: Gap and activity log

Source-native identity: generated `log.md`, append-only Markdown on the vault filesystem. Natural-language missing/wrong-content statements and operation/outcome summaries are read by the maintenance model. Date/operation headings are conventions, not a shipped independently validating consumer. The log can preserve a reported criticism of a page and guide later repair; it is not a semantic test oracle or a verified acceptance history. Distinct from [RT-OBJ-wiki-ingest](runtime.md#rt-obj-wiki-ingest), the command consuming it; [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit) describes read/repair rather than its storage identity. No supplied object counterpart after comparison. SRC-1, `SETUP_PROMPT.md`, Phase 4, G0, G7.

> <One sentence describing what's missing or wrong in the wiki>
> --- `SETUP_PROMPT.md`

> This tells you: when the wiki was last updated, what was intentionally deferred, and what the maintainer already flagged as missing. Do not re-discover things that are already logged.
> --- `SETUP_PROMPT.md`

### Routes

#### EPI-RTE-schema-check
Label: Frontmatter diagnostic check
Part of: [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)

A material check subroute of G5, distinct from the audit container's disposition/repair. Endpoints: selected Wiki page text → grep key-presence predicates → missing-field messages → requested model repair. Owner: instructed audit model; the embedded shell evaluates line prefixes. Context/state: selected page bytes; no page changes by the diagnostic itself. SRC-1, `SETUP_PROMPT.md`, G5; doctrine/design layer of an embedded example, not an installed validator.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Missing type/updated/status messages when corresponding grep fails; silence otherwise in the example.
- Later read-back: inapplicable — diagnostic itself retains nothing; audit summary retention is in the parent route.
- Delegated visibility: inapplicable — no delegated evaluator is specified.
- Selection predicate: Wiki/**/*.md loop and beginning-of-line key strings, contingent on the host shell's glob behavior.
- Invalidation or expiry: inapplicable — predicates inspect current selected bytes; no durable checked state is issued.
- Activation or effect: Model is asked to fix violations; no consumed diagnostic or repair trace supplied.
- Evidence limits: No full YAML parsing, allowed-value check or sources predicate; concrete generated implementation and operation unavailable.

Target/domain: presence of three key strings anywhere in selected page text. Deterministic text deduction: a page whose entire body is `type: nonsense`, `updated: nonsense`, `status: nonsense` on separate lines passes all three greps despite lacking frontmatter delimiters and `sources`. This is a deduction from inspected snippet text, not target execution. The contrary case is the broader natural-language instruction: a compliant model could notice invalid frontmatter beyond grep, so the deduction bounds the example rather than proves every installation defective.

> for page in Wiki/**/*.md; do
>   grep -q "^type:" "$page" || echo "MISSING type: $page"
>   grep -q "^updated:" "$page" || echo "MISSING updated: $page"
>   grep -q "^status:" "$page" || echo "MISSING status: $page"
> done
> --- `SETUP_PROMPT.md`

The model proposes/decides missing-field additions; no required human per-field veto. Mode: open audit, triggered by existing vault/schema gaps, without an expected-answer oracle. Guidance is required frontmatter and appropriate values. No rejection gate or rollback supplied; parent audit is recovery. Diagnostics have advisory force for current model repair, not an epistemic license for page facts.

#### EPI-RTE-link-check
Label: Link and index diagnostics
Part of: [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)

Material G4 check subroute, distinct from requested subsequent additions/corrections. Endpoints: Wiki paths/content and index bytes → grep/find/count checks → orphan/broken/index-missing diagnostics → model repair. Owner: instructed audit model, assisted by symbolic shell examples. Checks do not modify state themselves. SRC-1, `SETUP_PROMPT.md`, G4, doctrine/design.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: ORPHAN, BROKEN LINK and MISSING FROM INDEX messages under the examples' predicates.
- Later read-back: inapplicable — diagnostic text itself has no specified persistence; parent audit log summarizes repairs.
- Delegated visibility: inapplicable — no separate delegated link evaluator is defined.
- Selection predicate: Page glob; wikilink regex; target basename find; name-string grep in index.
- Invalidation or expiry: inapplicable — current-byte diagnostics, no persistent validation certificate.
- Activation or effect: Requested link/page/index repair by audit model; no supplied exercised consumer.
- Evidence limits: Matching heuristics are not complete graph parsing or semantic evaluation; generated execution and shell/plugin compatibility unknown.

Target/domain: syntactic reachability and index mention. The orphan example searches a prefix: for page `Foo.md`, another page containing a wikilink to Foobar matches the searched opening brackets followed by Foo, so the count can be nonzero without any actual link to Foo. Likewise `grep -q "$name" index.md` can find Foo as prose or a substring without a Wiki target. These are concrete input deductions from snippet text, not executions. The broken-link example strips display text and searches for a basename; it can guide repairs but does not check the claim at the target. The broader request for connected coverage could prompt model inspection beyond these examples.

>   name=$(basename "$page" .md)
>   count=$(grep -rl "\[\[$name" Wiki/ | grep -v "$page" | wc -l)
>   [ "$count" -eq 0 ] && echo "ORPHAN: $page"
> --- `SETUP_PROMPT.md`

>   grep -q "$name" index.md || echo "MISSING FROM INDEX: $name"
> --- `SETUP_PROMPT.md`

> Fix each orphan by adding a wikilink to it from the most relevant existing page. Fix each broken link by either creating the missing page or correcting the link text.
> --- `SETUP_PROMPT.md`

Model proposes/decides repairs with no mandatory human veto or independent expected-answer oracle. Mode: open existing-vault audit; trigger: navigation gaps. Guidance: relevance and matching target existence. Changed links/pages persist under parent audit; no rollback specified. Diagnostic consumer is the current audit model through shell output, advisory force over repair within the invocation; later navigation consumers receive repaired pages/index, not a truth certificate.

### Claims

#### EPI-CLM-compiled-knowledge
Label: Compounding compiled knowledge

Claimed operation: source material becomes compiled, persistent knowledge that grows through sync and questions. This is distinct from [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first), which concerns selection priority, and [RT-CLM-sources-immutability](runtime.md#rt-clm-sources-immutability), which concerns layer authority. SRC-1, `README.md`, doctrine/design; attributed example counts elsewhere in README do not establish semantic warrant.

> The key principle from Karpathy's gist: **Sources are raw input. Wiki is compiled knowledge.** The wiki is a persistent, compounding artifact — it gets richer with every source sync and every question asked.
> --- `README.md`

The source-sync and gap/ingest design can grow an artifact, but sync alone does not update Wiki pages and candidate accumulation does not establish accepted knowledge.

#### EPI-CLM-answer-coverage
Label: Wiki-only answer coverage

Claimed criterion: project questions across purpose, schemas, behavior, rationale, state, constraints and deployment should be answerable without source reads. Distinct from [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness), which claims repair breadth, and [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first), which gives priority rather than a sufficiency criterion. SRC-1, `SETUP_PROMPT.md`, Quality Bar, doctrine/design.

> The wiki is complete when a future LLM session can answer any of these questions using only wiki pages (no source reads):
> --- `SETUP_PROMPT.md`

> If any question requires opening a source file to answer, that's a gap. File it in `log.md`.
> --- `SETUP_PROMPT.md`

The criterion records a coverage failure, not an independently checked correct answer. It does not supply an observed acceptance decision or warrant for every answer.
