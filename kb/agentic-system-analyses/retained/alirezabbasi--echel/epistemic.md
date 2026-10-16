---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Echel epistemic routes: imported product assertions, review metadata, structural gates, verification and bounded downstream reliance."
run-id: AAS-2026-10-15-echel-08d27848b99a-01
reviewed-boundary: aee36de4d2d1c404fb36e9ad68cc0a920784ee61
---

# Echel epistemic report

## Source-and-claim boundary

The question is how Echel obtains product assertions, checks them, grants reliance, and changes subsequent work. The frozen repository and exclusions are those in the [boundary Source register](boundary.md#source-register), SRC-1. This is source analysis, not target execution. The runtime is a provisional starting point. This member directly inspected CLI dispatch, context rendering, clarification, authority, canonical store write/load, findings, lifecycle, profiles, relationships, queries, index construction/search/freshness, import/export, migration transformation/recovery, integrity diagnostics, kernel gate, README, two maintenance skills and the evaluation metric specification. These are added SRC-1 implementation or doctrine/design coverage, not additional sources.

External Hermes/model processing, authenticated reviewer identity, actual proposal/evidence/decision instances, and product-scenario execution are unavailable within the supplied evidence. Respectively these prevent conclusions about hidden inference or parameter updates, genuine human approval, evidence-consuming semantic acceptance, and exercised benefit. Canonical artifact/work/task/release payloads and optional extension semantics are not individually assessed as truth-apt producers here: no instance or dedicated authoring path beyond generic storage/transfer was inspected. This prevents a complete semantic-object inventory or negative about every canonical record type. Available but unread benchmark scenario/metric catalogs and detailed test assertions are not access gaps. Their omission prevents an exhaustive evaluator audit. No system-complete negative about all possible checking or learning follows.

Public warrant claims are declared below; the runtime responsibility claim remains in its supplied record. Coverage distinguishes direct inspection (D) from supplied runtime evidence (R).

| Entry point or operation | SRC-1 path | Coverage and records / limit |
|---|---|---|
| CLI registration and dispatch | `pyproject.toml`, `src/echel/cli/main.py` | D dispatch; R entry-point registration. All eleven subcommands accounted for below; search of `src/echel` for hook/register/tool wiring found the Hermes toolset request, not an additional Echel tool registry. External Hermes hooks remain uninspected. |
| init | `src/echel/initialization.py` | R: [RT-RTE-idea-init](runtime.md#rt-rte-idea-init); initial content acquisition, not synthesis of a product theory. |
| clarify | `src/echel/methodology/clarification.py` | D: [EPI-RTE-clarification-select](#epi-rte-clarification-select). |
| status, lifecycle, add, advance, work | `src/echel/cli/main.py`, `src/echel/workflow.py` | D dispatch and correction reads of workflow/model/store/compiler; R baseline: [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow). Legacy accepted-status writes and force bypass remain material alternatives. |
| context, run; direct adapter API | `src/echel/context/compiler.py`, `src/echel/runtimes/hermes.py` | D compiler/CLI; R adapter: [RT-RTE-compile-run](runtime.md#rt-rte-compile-run). No Echel parsing of agent discoveries into canonical proposals. |
| verify | `src/echel/verification/runner.py` | R: [RT-RTE-verify-work](runtime.md#rt-rte-verify-work); D CLI consumer. Return status is not a product answer oracle. |
| canonical acceptance/rejection and direct writes | `src/echel/authority.py`, `src/echel/storage/records.py`, `src/echel/schemas/v1/record.schema.json` | D service/store and targeted schema clauses; [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide). Full schema audit not performed. |
| findings create/decide/assess | `src/echel/findings.py` | D: [EPI-RTE-finding-review](#epi-rte-finding-review). |
| canonical maturity assessment, advance, stale propagation | `src/echel/lifecycle.py` | D: [EPI-RTE-maturity-check](#epi-rte-maturity-check), [EPI-RTE-maturity-advance](#epi-rte-maturity-advance), [EPI-RTE-stale-propagation](#epi-rte-stale-propagation). Not the CLI's legacy advance. |
| profile inspection/change | `src/echel/profiles.py` | D: [EPI-RTE-profile-selection](#epi-rte-profile-selection). |
| explicit relationships | `src/echel/relationships.py` | D: [EPI-RTE-relationship-write](#epi-rte-relationship-write). |
| search, reverse links, impact; index rebuild/discard | `src/echel/queries.py`, `src/echel/storage/index.py` | D: [EPI-RTE-canonical-query](#epi-rte-canonical-query). Rehydrated provenance, not independent confirmation. |
| portable export/import | `src/echel/portability.py` | D service: [EPI-RTE-portable-import](#epi-rte-portable-import); bundle source authenticity unestablished. |
| migration preview/apply/recover/rollback | `src/echel/migrations.py` | D transformation and main control/recovery paths: [EPI-RTE-schema-migration](#epi-rte-schema-migration); low-level manifest/path helpers not exhaustively audited. |
| journal commit/recover/rollback | `src/echel/storage/transactions.py` | D selected commit/recovery/apply paths: [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) and import record; prepare/locking internals not exhaustively audited, preventing a universal concurrency guarantee. |
| integrity inspect | `src/echel/integrity.py` | D: [EPI-RTE-integrity-check](#epi-rte-integrity-check). |
| contributor checks and maintainer admission | `CONTRIBUTING.md`, `.github/workflows/quality.yml` | D and R: [RT-RTE-source-admission](runtime.md#rt-rte-source-admission), [EPI-OBJ-contribution](#epi-obj-contribution). Implemented check jobs are separate from doctrine-only human admission; no merge, release or deployed check evidence. |
| validation/operations instructions | `skills/validation/SKILL.md`, `skills/operations/SKILL.md` | D doctrine: [EPI-CLM-approved-discoveries](#epi-clm-approved-discoveries); other nine skills covered by boundary/runtime only. Delivery/compliance unknown. |
| kernel evaluator and stored local result | `benchmarks/kernel/gate.py`, `benchmarks/kernel/evidence/2026-07-15-local.json` | D gate, R attributed artifact: [EPI-RTE-kernel-gate](#epi-rte-kernel-gate). No independent observed or causal run. |
| product-scenario evaluation | `docs/product/evaluation-metrics.md` | D doctrine: [EPI-CLM-evaluation-contract](#epi-clm-evaluation-contract). Catalogs, scenario fixtures and downstream harness not inspected; no achieved scenario claims licensed. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | See record | See record | SRC-1, `src/echel/workflow.py` | See record |
| [EPI-OBJ-work-item](#epi-obj-work-item) | See record | See record | SRC-1, `src/echel/model/records.py` | See record |
| [EPI-OBJ-legacy-project](#epi-obj-legacy-project) | See record | See record | SRC-1, `src/echel/storage/files.py` | See record |
| [EPI-OBJ-kernel-report](#epi-obj-kernel-report) | See record | See record | SRC-1, `benchmarks/kernel/gate.py` | See record |
| [EPI-OBJ-contribution](#epi-obj-contribution) | See record | See record | SRC-1, `CONTRIBUTING.md` | See record |
| [EPI-OBJ-claim](#epi-obj-claim) | See record | See record | SRC-1, `src/echel/authority.py` | See record |
| [EPI-OBJ-decision](#epi-obj-decision) | See record | See record | SRC-1, `src/echel/authority.py` | See record |
| [EPI-OBJ-learning](#epi-obj-learning) | See record | See record | SRC-1, `src/echel/authority.py` | See record |
| [EPI-OBJ-run](#epi-obj-run) | See record | See record | SRC-1, `src/echel/cli/main.py` | See record |
| [EPI-OBJ-finding](#epi-obj-finding) | See record | See record | SRC-1, `src/echel/findings.py` | See record |
| [EPI-OBJ-relationship](#epi-obj-relationship) | See record | See record | SRC-1, `src/echel/relationships.py` | See record |
| [EPI-OBJ-project](#epi-obj-project) | See record | See record | SRC-1, `src/echel/lifecycle.py` | See record |
| [EPI-OBJ-evidence](#epi-obj-evidence) | See record | See record | SRC-1, `src/echel/verification/runner.py` | See record |
| [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context) | See record | See record | SRC-1, `src/echel/context/compiler.py` | Sources omitted from text; see rendering deduction below |
| [RT-CMP-runtime-model](runtime.md#rt-cmp-runtime-model) | Not determinable inside opaque distributed parameters | See record | SRC-1, `src/echel/runtimes/hermes.py` | Version, mutation and hidden inference remain uninspected |

## Authority-route ledger

Architectural status is assessed here; shared records own the remaining details. Repeated references split functions of one implementation rather than assert additional independent mechanisms. All implemented rows are implementation evidence, not observed activation. `See record` carries the exact field ownership rather than copying the runtime.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | content transformation | implemented | [EPI-OBJ-claim](#epi-obj-claim) | truth-apt transformation: acquisition/import | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | See record; source warrant unknown | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | none | none | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) |
| [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | retention | implemented | [EPI-OBJ-claim](#epi-obj-claim) | no content change | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | See record; proposed raw idea only | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) | none | none | see [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) |
| [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | content transformation | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) | truth-apt transformation: acquisition/import | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | See record; caller assertions and labels, warrant unknown | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | none | none | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) |
| [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | retention | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record), [EPI-OBJ-work-item](#epi-obj-work-item), [EPI-OBJ-legacy-project](#epi-obj-legacy-project) | no content change | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | See record; retained before independent acceptance | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | none | none | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) |
| [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | operational admission/selection/consumption | implemented | [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record), [EPI-OBJ-legacy-project](#epi-obj-legacy-project) | no content change | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | See record; kind/status gate, force bypass | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) | none | none | see [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) |
| [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | content transformation | implemented | [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context) | truth-apt transformation: non-ampliative reshaping | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | See record and concrete rendering deduction | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | [EPI-CLM-trustworthy-context](#epi-clm-trustworthy-context) | provenance loss; not accepted-only | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) |
| [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | operational admission/selection/consumption | implemented | [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context) | no content change | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | See record; advisory prompt, explicit execution option | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | [EPI-CLM-trustworthy-context](#epi-clm-trustworthy-context) | none | see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) |
| [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | check/evidence production | implemented | [EPI-OBJ-evidence](#epi-obj-evidence) | truth-apt transformation: entailed derivation | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | See record; process-result domain, not semantic product correctness | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | [EPI-CLM-approved-discoveries](#epi-clm-approved-discoveries) | none | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) |
| [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | retention | implemented | [EPI-OBJ-evidence](#epi-obj-evidence) | no content change | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | See record; summary/hash persistence, not knowledge promotion | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) | none | none | see [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) |
| [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | check/evidence production | implemented | [EPI-OBJ-claim](#epi-obj-claim) | no content change | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | See record; eligibility and identity labels, not rationale truth | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | none | none | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) |
| [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | disposition/acceptance | implemented | [EPI-OBJ-claim](#epi-obj-claim) | non-truth-apt policy/content update: accepted/rejected authority metadata | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | See record; human-labelled decision, no enforced evidence criterion | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) | [EPI-CLM-approved-discoveries](#epi-clm-approved-discoveries) | record status is not evidence-consuming semantic acceptance | see [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) |
| [EPI-RTE-clarification-select](#epi-rte-clarification-select) | check/evidence production | implemented | [EPI-OBJ-claim](#epi-obj-claim) | truth-apt transformation: entailed derivation | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | Kind absence under active-status predicate | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | none | none | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) |
| [EPI-RTE-clarification-select](#epi-rte-clarification-select) | operational admission/selection/consumption | implemented | [EPI-OBJ-claim](#epi-obj-claim) | non-truth-apt policy/content update: next question selection | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | First unfilled non-excluded kind; advisory CLI next action | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) | none | none | see [EPI-RTE-clarification-select](#epi-rte-clarification-select) |
| [EPI-RTE-maturity-check](#epi-rte-maturity-check) | check/evidence production | implemented | [EPI-OBJ-project](#epi-obj-project) | truth-apt transformation: entailed derivation | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | Accepted-kind presence and linked active severity | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) | none | none | see [EPI-RTE-maturity-check](#epi-rte-maturity-check) |
| [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | disposition/acceptance | implemented | [EPI-OBJ-project](#epi-obj-project) | non-truth-apt policy/content update: maturity advance | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | Preview gate plus labelled human authorization; apply does not reassess all evidence | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) | none | none | see [EPI-RTE-maturity-advance](#epi-rte-maturity-advance) |
| [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | disposition/acceptance | implemented | [EPI-OBJ-claim](#epi-obj-claim) | non-truth-apt policy/content update: accepted knowledge marked stale | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | Human-labelled backward revision, not falsity inference | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | none | none | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) |
| [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | retention | implemented | [EPI-OBJ-claim](#epi-obj-claim) | no content change | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | Journal installs stale statuses and reasons | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) | none | none | see [EPI-RTE-stale-propagation](#epi-rte-stale-propagation) |
| [EPI-RTE-finding-review](#epi-rte-finding-review) | content transformation | implemented | [EPI-OBJ-finding](#epi-obj-finding) | truth-apt transformation: acquisition/import | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | Caller statement, severity and affected links; source warrant unknown | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | none | none | see [EPI-RTE-finding-review](#epi-rte-finding-review) |
| [EPI-RTE-finding-review](#epi-rte-finding-review) | check/evidence production | implemented | [EPI-OBJ-finding](#epi-obj-finding) | truth-apt transformation: entailed derivation | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | Active/severity impact mapping | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | none | none | see [EPI-RTE-finding-review](#epi-rte-finding-review) |
| [EPI-RTE-finding-review](#epi-rte-finding-review) | disposition/acceptance | implemented | [EPI-OBJ-finding](#epi-obj-finding) | non-truth-apt policy/content update: finding accepted/resolved/dismissed | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | Human-labelled rationale changes impact, without automatic claim rewrite | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | see [EPI-RTE-finding-review](#epi-rte-finding-review) | none | none | see [EPI-RTE-finding-review](#epi-rte-finding-review) |
| [EPI-RTE-profile-selection](#epi-rte-profile-selection) | behavior/policy adaptation | implemented | [EPI-OBJ-project](#epi-obj-project) | non-truth-apt policy/content update: lifecycle profile selection | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | Explicit human-labelled selection among static policies | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) | none | none | see [EPI-RTE-profile-selection](#epi-rte-profile-selection) |
| [EPI-RTE-relationship-write](#epi-rte-relationship-write) | check/evidence production | implemented | [EPI-OBJ-relationship](#epi-obj-relationship) | no content change | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | Typed endpoints, allowed predicate, nonempty reason; not semantic support | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | none | none | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) |
| [EPI-RTE-relationship-write](#epi-rte-relationship-write) | retention | implemented | [EPI-OBJ-relationship](#epi-obj-relationship) | truth-apt transformation: acquisition/import | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | Caller rationale persisted; source warrant unknown | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | none | none | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) |
| [EPI-RTE-relationship-write](#epi-rte-relationship-write) | lifecycle integration | implemented | [EPI-OBJ-relationship](#epi-obj-relationship) | no content change | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | Conditional on prior acceptance: link accepted content to evidence; API does not verify that precondition | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) | none | none | see [EPI-RTE-relationship-write](#epi-rte-relationship-write) |
| [EPI-RTE-canonical-query](#epi-rte-canonical-query) | content transformation | implemented | [EPI-OBJ-relationship](#epi-obj-relationship) | truth-apt transformation: non-ampliative reshaping | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | Rebuild/index/search/path organization, not additional product warrant | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | none | none | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) |
| [EPI-RTE-canonical-query](#epi-rte-canonical-query) | lineage/freshness/recovery | implemented | [EPI-OBJ-relationship](#epi-obj-relationship) | no content change | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | Fingerprint veto and canonical provenance reload | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | none | none | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) |
| [EPI-RTE-canonical-query](#epi-rte-canonical-query) | operational admission/selection/consumption | implemented | [EPI-OBJ-claim](#epi-obj-claim) | no content change | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | FTS ranking/path traversal to API caller, not Hermes compiler | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) | none | none | see [EPI-RTE-canonical-query](#epi-rte-canonical-query) |
| [EPI-RTE-portable-import](#epi-rte-portable-import) | check/evidence production | implemented | [EPI-OBJ-claim](#epi-obj-claim) | no content change | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | Schema, identity/order/endpoint and fingerprint checks | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | none | none | see [EPI-RTE-portable-import](#epi-rte-portable-import) |
| [EPI-RTE-portable-import](#epi-rte-portable-import) | retention | implemented | [EPI-OBJ-claim](#epi-obj-claim) | truth-apt transformation: acquisition/import | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | Transferred records and authority metadata; origin warrant unknown | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | see [EPI-RTE-portable-import](#epi-rte-portable-import) | none | none | see [EPI-RTE-portable-import](#epi-rte-portable-import) |
| [EPI-RTE-schema-migration](#epi-rte-schema-migration) | content transformation | implemented | [EPI-OBJ-claim](#epi-obj-claim) | truth-apt transformation: indeterminate | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | Caller set/remove fields may change semantic assertions; see counterexample | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | none | none | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) |
| [EPI-RTE-schema-migration](#epi-rte-schema-migration) | lineage/freshness/recovery | implemented | [EPI-OBJ-claim](#epi-obj-claim) | no content change | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | Backups, source/target digests and guarded rollback | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) | none | none | see [EPI-RTE-schema-migration](#epi-rte-schema-migration) |
| [EPI-RTE-integrity-check](#epi-rte-integrity-check) | check/evidence production | implemented | [EPI-OBJ-claim](#epi-obj-claim) | truth-apt transformation: entailed derivation | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | Healthy means no inspected structural error, not true product content | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) | none | none | see [EPI-RTE-integrity-check](#epi-rte-integrity-check) |
| [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | check/evidence production | implemented | [EPI-OBJ-kernel-report](#epi-obj-kernel-report) | truth-apt transformation: entailed derivation | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | Measured counts/timings to threshold Boolean; synthetic SQL domain | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | none | none | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) |
| [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | operational admission/selection/consumption | implemented | [EPI-OBJ-kernel-report](#epi-obj-kernel-report) | no content change | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | Gate Boolean to CLI exit code, not release authority | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) | none | none | see [EPI-RTE-kernel-gate](#epi-rte-kernel-gate) |
| [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | disposition/acceptance | doctrine only | [EPI-OBJ-contribution](#epi-obj-contribution) | non-truth-apt policy/content update: source change admission | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | See record; declared maintainer decision, not an implemented automatic acceptance gate | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | none | none | see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) |
| [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | check/evidence production | implemented | [EPI-OBJ-contribution](#epi-obj-contribution) | truth-apt transformation: entailed derivation | Configured core-job outcomes for the proposed checkout | CI jobs and baseline aggregator; domain is tool/assertion predicates and job success, not product truth | Push, PR or manual dispatch; baseline after core jobs | Job outcomes and success/failure of baseline | Baseline fails if any required core job is not successful | Only configured checks; no maintainer acceptance or release license | Changes baseline outcome, not canonical project state or automatic merge | CI baseline, needs JSON, enforcing exit status, current workflow | SRC-1, `.github/workflows/quality.yml`; see [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) | none | Passing checks are not source-change acceptance | Branch protection, actual check runs and maintainer decisions uninspected |

**Concrete rendering deduction (implementation, not execution).** For a legacy work item related to `KNO-0001`, a matching knowledge record with statement `Exports require consent.`, status `stale`, confidence `high`, and sources `audit-A` is selected without a status veto. With kind `constraint`, its text line is `- [KNO-0001] (constraint, stale, confidence=high): Exports require consent.` The source reference is not rendered. This preserves the assertion text but degrades delivered warrant/lineage; it does not newly verify the assertion. A rejected or proposed record satisfies the same membership predicate. JSON context preserves dictionaries, so the loss is specific to text and `run`, not every context surface. SRC-1, `src/echel/context/compiler.py`; see [RT-RTE-compile-run](runtime.md#rt-rte-compile-run).

> f"- [{record['id']}] ({record['kind']}, {record.get('status', 'unknown')}, "
> f"confidence={record.get('confidence', 'unknown')}): {record['statement']}"
> --- `src/echel/context/compiler.py`

**No automatic promotion inferred.** Verification's outcome summary is a process-status derivation. A caller-supplied executable could implement a strong domain oracle, or merely return success without checking the intended condition. The runner alone licenses neither alternative. The CLI dispatch consumes Evidence only for output and does not call canonical knowledge acceptance. Likewise stdout truncation in `run` can retain arbitrary model claims, but their truth-apt content and relation to inputs are not determinable without an instance. Non-entailment is not inferred from opacity. SRC-1, `src/echel/cli/main.py`; [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) and [RT-RTE-compile-run](runtime.md#rt-rte-compile-run).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-trustworthy-context](#epi-clm-trustworthy-context) | see record | see record | see record | [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | None supplied | No comparative context-quality evidence | Explicit related-ID selection and text reshaping | Smallest/trustworthy not guaranteed by membership; status and lineage counterexamples |
| [EPI-CLM-approved-discoveries](#epi-clm-approved-discoveries) | see record | see record | see record | [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide), [RT-RTE-verify-work](runtime.md#rt-rte-verify-work), [EPI-RTE-stale-propagation](#epi-rte-stale-propagation), [EPI-RTE-relationship-write](#epi-rte-relationship-write) | None supplied | No traced discovery → evidence-consuming decision → later reliance | Separate proposed-content review and correction facilities | No automatic verified-discovery promotion in CLI; alternate writes bypass service |
| [RT-CLM-runtime-boundary](runtime.md#rt-clm-runtime-boundary) | see record | see record | see record | [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) | None supplied | External runtime opaque | Execution delegated; product context supplied | Ownership statement is not an isolation invariant |
| [EPI-CLM-evaluation-contract](#epi-clm-evaluation-contract) | see record | see record | see record | [EPI-RTE-kernel-gate](#epi-rte-kernel-gate), [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) are narrower, not implementations of the entire scenario protocol | Local kernel result is reported operation only | Synthetic SQL timing is not a component-isolated comparison or product scenario | Explicit criteria exist as doctrine | Achieved context/task/learning metrics and release acceptance unestablished |

## Bounded conclusion

Echel acquires caller-authored ideas, assertions, findings and relations. The canonical services preserve provenance fields and attributable decision metadata, while portable import preserves supplied metadata without authenticating its origin. None of these surfaces supplies source truth by virtue of retention. Legacy context reshapes statements into selected prompt text; it loses source references and does not exclude unaccepted or stale knowledge. Those contents can advise a model in the current request, but delivery does not establish compliance or repeated beneficial reliance. See [RT-RTE-idea-init](runtime.md#rt-rte-idea-init), [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow), [RT-RTE-compile-run](runtime.md#rt-rte-compile-run), [EPI-RTE-portable-import](#epi-rte-portable-import).

Legacy workflow retains [EPI-OBJ-knowledge-record](#epi-obj-knowledge-record) and [EPI-OBJ-work-item](#epi-obj-work-item), and updates [EPI-OBJ-legacy-project](#epi-obj-legacy-project). Its stage gate consumes stored knowledge labels and project stage, not the later compiled prompt. Kernel counts/timings belong to [EPI-OBJ-kernel-report](#epi-obj-kernel-report), returned and printed by the benchmark, not the legacy work-verification Evidence retention chain. Contributor checks concern [EPI-OBJ-contribution](#epi-obj-contribution); wired CI outcomes do not implement the separately declared human maintainer acceptance, nor mutate canonical project maturity. SRC-1, `src/echel/workflow.py`, `benchmarks/kernel/gate.py`, `.github/workflows/quality.yml`, `CONTRIBUTING.md`.

The checked derivations are narrower than product truth: clarification gaps from record-kind predicates; maturity usability from accepted-kind presence and active linked severity; finding impact from status/severity; query paths from declared edges; process summaries from exit codes; integrity reports from structural diagnostics; and kernel pass/fail from counts and timing thresholds. Their premises are file contents or measured process outputs, not independently warranted product facts. No transfer from those domains to correctness of product statements is licensed. See the corresponding ledger records.

Canonical acceptance records a caller-supplied human-labelled decision and nonempty rationale for a proposed claim, decision or learning. It does not require an inspected evidence reference, semantic criterion, intended use or scope. Therefore an `accepted` state can change the maturity gate without establishing a produced accepted ampliative claim in this analysis's sense. Human evidence review is possible and prescribed; its occurrence and quality are unobserved. There is no concrete generated conjecture instance here from which entailment/non-entailment or evidence-consuming acceptance can be determined. See [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide), [EPI-RTE-maturity-check](#epi-rte-maturity-check).

Correction is not merely aspirational: findings can block canonical maturity and reviewed stale propagation can withdraw accepted status from explicit downstream protected knowledge. Accepted content can be linked to evidence by the relationship API, but that API does not require prior acceptance; a relationship's existence is neither evidence that acceptance happened nor proof that its rationale is true. These facilities support possible post-acceptance integration, not a demonstrated integrated discovery cycle. Resolved/dismissed findings release their severity effect; previously delivered prompts are not recalled. See [EPI-RTE-finding-review](#epi-rte-finding-review), [EPI-RTE-stale-propagation](#epi-rte-stale-propagation), [EPI-RTE-relationship-write](#epi-rte-relationship-write).

Direct policy adaptation exists through profile selection; it changes required-kind policy without deriving new product truth. Retained findings/statuses can shape later canonical assessments, independently of whether they reach Hermes. Parameter learning remains uninspected at the external model; retained-record use is a separate implemented capacity, not demonstrated improved future action. Reflection, autonomous content criticism, iterative theory revision and self-improvement are not established by these source-only facilities or by raw run/evidence retention. This is not evidence of their universal absence. No observed update-to-later-behavior chain or causal improvement comparison is supplied. The static methodology and contributor procedure must not be mistaken for an exercised theory-building process. See [EPI-RTE-profile-selection](#epi-rte-profile-selection), [RT-CMP-runtime-model](runtime.md#rt-cmp-runtime-model), [RT-RTE-source-admission](runtime.md#rt-rte-source-admission).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-knowledge-record
Label: KnowledgeRecord

Part of: [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow)

This object is a retained output/input of the parent route, not a subroute. Source-native identity: legacy `KnowledgeRecord`, with caller-supplied natural-language statement and symbolic kind/stage/status/confidence/source references. Storage substrate: `.echel/knowledge/<id>.json` through FileStore. It is acquired from the caller and retained before independent acceptance; source warrant is unknown. Workflow status consumes kind/stage/accepted-or-validated labels; ContextCompiler separately selects related IDs and renders statements. Neither consumer receives an already compiled prompt from WorkflowService. Distinct from [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context), the later in-process rendering, and from canonical [EPI-OBJ-claim](#epi-obj-claim). SRC-1 implementation: `src/echel/workflow.py`, `src/echel/model/records.py`, `src/echel/storage/files.py`, `src/echel/context/compiler.py`.

> self.store.put("knowledge", record.to_dict())
> --- `src/echel/workflow.py`

> and record.get("stage") == current.id
> and record.get("status") in {"accepted", "validated"}
> --- `src/echel/workflow.py`

#### EPI-OBJ-work-item
Label: WorkItem

Part of: [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow)

Retained output of the parent route: legacy `WorkItem`, not a route. Natural-language title/objective/acceptance and executable verification strings coexist with symbolic ID/status/stage and `relates_to` references. Storage: `.echel/work/<id>.json`. WorkflowService verifies referenced IDs exist, then retains caller-authored work. ContextCompiler reads it to select and render context; verification reads its commands. Objectives and acceptance conditions need not be truth-apt; no concrete warranted proposition is supplied. Distinct from the compiled text in [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context) and canonical project state. SRC-1 implementation: `src/echel/model/records.py`, `src/echel/workflow.py`, `src/echel/storage/files.py`; verification consumer supplied by [RT-RTE-verify-work](runtime.md#rt-rte-verify-work).

> self.store.put("work", record.to_dict())
> --- `src/echel/workflow.py`

#### EPI-OBJ-legacy-project
Label: Legacy Project

Part of: [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow)

State input/output of the parent route, not a route: legacy `Project` dataclass persisted as JSON `.echel/project.json`. Name/idea are natural-language caller content; `current_stage` is symbolic workflow policy state. Workflow status loads it to choose stage requirements; advance replaces its stage and saves it. No new product assertion or semantic acceptance follows. Distinct from canonical [EPI-OBJ-project](#epi-obj-project), despite the shared relative filename: envelopes and consuming services differ. Also distinct from [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context), which is not a lifecycle-gate input. SRC-1 implementation: `src/echel/workflow.py`, `src/echel/model/records.py`, `src/echel/storage/files.py`.

> project = replace(project, current_stage=target.id, updated_at=utc_now())
> self.store.save_project(project)
> --- `src/echel/workflow.py`

#### EPI-OBJ-kernel-report
Label: KernelGateReport

Part of: [EPI-RTE-kernel-gate](#epi-rte-kernel-gate)

Result object of the parent route, not a route. Source-native identity: `KernelGateReport` and nested Timing values. Symbolic counts, dataset digest, database size, measured timings and threshold Booleans state truth-apt results only over the generated SQLite kernel workload. Storage substrate: in-process dataclass, serialized JSON on stdout; generated database is separate. The report is not written to legacy evidence JSON or read by the work verifier. `main` consumes `report.passed` for exit status. Distinct from [EPI-OBJ-evidence](#epi-obj-evidence) and the peer [MEM-OBJ-evidence](memory.md#mem-obj-evidence), both legacy verification results; no supplied kernel-object counterpart. SRC-1 implementation: `benchmarks/kernel/gate.py`; producer/consumer passage in [EPI-RTE-kernel-gate](#epi-rte-kernel-gate).

> "timings": [timing.to_dict() for timing in self.timings],
> "passed": self.passed,
> --- `benchmarks/kernel/gate.py`

#### EPI-OBJ-contribution
Label: Contribution patch

Part of: [RT-RTE-source-admission](runtime.md#rt-rte-source-admission)

Proposed artifact of the parent route, not a route. Source-native identity: contributor patch/PR containing code, contracts, acceptance mapping and verification evidence. Representational form: symbolic source/configuration changes plus natural-language rationale and review. Storage substrate: repository patch/history and external collaboration channel by doctrine; no concrete patch, review event or adopted update is supplied. CI checks the checkout through configured jobs; maintainer acceptance is declared separately, not implemented by the success aggregator. Distinct from canonical [EPI-OBJ-project](#epi-obj-project), which is neither the contribution nor the maintainer's review artifact. SRC-1 doctrine/design: `CONTRIBUTING.md`; implementation: `.github/workflows/quality.yml`; closest supplied route supplies maintainer quotation and limits.

> A passing command is evidence, not automatic acceptance.
> --- `CONTRIBUTING.md`

> failed = {name: result for name, result in results.items() if result != "success"}
> --- `.github/workflows/quality.yml`

> if failed:
>     raise SystemExit(f"required jobs did not succeed: {failed}")
> --- `.github/workflows/quality.yml`

#### EPI-OBJ-claim
Label: Claim

Canonical `claim.statement`: caller-supplied natural-language candidate; scope/truth cannot be established from field names. Symbolic status/authority/provenance fields control service eligibility and maturity consumption; JSON under `.echel/records` is the substrate. These protected families share the authority service, but only claim kinds feed the inspected maturity gate. Evidence: SRC-1, `src/echel/authority.py`, `src/echel/lifecycle.py`, `src/echel/schemas/v1/record.schema.json`. Closest supplied record is [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) (route, not object); no supplied object counterpart. Distinct from legacy [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context) and its selected knowledge. Candidate text is acquired, not shown generated. No accepted instance, semantic acceptance criterion or source verification is supplied.

#### EPI-OBJ-finding
Label: Finding

Canonical `finding.statement` is natural-language criticism, risk, gap, defect or question; not every instance is truth-apt. Status/severity and `affects` endpoints are symbolic JSON consumed by impact/maturity. Storage: `.echel/records/findings` plus separate relationship files. Evidence: SRC-1, `src/echel/findings.py`, `src/echel/lifecycle.py`. Closest supplied [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) includes legacy findings, not this canonical family or API consumer. No supplied canonical finding-object counterpart. A contradiction label alone does not individuate a challenged theory or establish its falsity.

#### EPI-OBJ-relationship
Label: Relationship

Canonical `source`, `predicate`, `target`, `policy`, provenance and natural-language `reason`. JSON record plus disposable SQLite projection. Endpoint/predicate fields have symbolic query and stale-propagation consumers; reason is human-readable rationale that may assert support/contradiction. Evidence: SRC-1, `src/echel/relationships.py`, `src/echel/queries.py`. No supplied counterpart after comparison with [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context) (legacy `relates_to` membership is a different encoding/consumer). The service validates type eligibility, not whether support or contradiction is sound.

#### EPI-OBJ-project
Label: Project

Canonical `project.maturity`/`profile` and transition metadata: symbolic policy/organization state, not a product truth claim. The derived `MaturityAssessment` reports truth-apt facts about stored state under a fixed rule. JSON `.echel/project.json`; assessments are in-process return values. Evidence: SRC-1, `src/echel/lifecycle.py`, `src/echel/profiles.py`. Closest [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) is a producer route; [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) uses a different project model. No supplied object counterpart. A maturity label is not certification or semantic correctness.

#### EPI-OBJ-evidence
Label: Evidence

Legacy `Evidence` command/subject/exit status/summary/checksum are JSON records in the legacy evidence collection. Command and exit fields are symbolic; the natural-language summary is a deterministic passed/failed label, not an assessment of product intent. Canonical Evidence is a different schema family, not implicitly populated by verification. Evidence: SRC-1, `src/echel/cli/main.py`, `src/echel/verification/runner.py`, `src/echel/schemas/v1/record.schema.json`; producer/retention passages supplied by [RT-RTE-verify-work](runtime.md#rt-rte-verify-work) and [RT-RTE-compile-run](runtime.md#rt-rte-compile-run). Distinct object identity; no supplied Evidence/Run object declaration. Output hash is an identity check, not evidence sufficiency; summary content absent prevents candidate-level inference.

#### EPI-OBJ-decision
Label: Decision

Canonical `decision.outcome` and `alternatives` contain natural-language choices and possibly truth-apt reasons, but a decision is not necessarily a factual assertion. Symbolic accepted/rejected/stale authority metadata is governed by the same protected service as [EPI-OBJ-claim](#epi-obj-claim). JSON `.echel/records/decisions` is read by canonical queries and stale propagation; decision kinds do not satisfy the claim-kind maturity gate. SRC-1, `src/echel/authority.py`, `src/echel/lifecycle.py`, `src/echel/schemas/v1/record.schema.json`. No supplied object counterpart; closest [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) is the route. No decision instance with an evidentially accepted proposition is supplied.

#### EPI-OBJ-learning
Label: Learning

Canonical `learning.observation`, `implication`, and evidence-ID list: natural-language candidate observation/consequence plus symbolic references and authority state. JSON `.echel/records/learnings`; canonical authority, query and stale consumers, not legacy context compiler. Evidence: SRC-1, `src/echel/authority.py`, `src/echel/schemas/v1/record.schema.json`, `src/echel/lifecycle.py`. Distinct object from [EPI-OBJ-claim](#epi-obj-claim) and [EPI-OBJ-decision](#epi-obj-decision) despite shared admission. Closest supplied [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) covers the route, not an object. Retaining a learning-labelled record or evidence IDs does not establish improved capacity or consumption of the evidence in acceptance.

#### EPI-OBJ-run
Label: Run

Legacy `Run` context digest/command/status/exit code are symbolic; bounded stdout summary is opaque text that may contain truth-apt claims. JSON `.echel/runs` is the substrate. Evidence: SRC-1, `src/echel/cli/main.py`; supplied producer [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) has no Run object counterpart. Summary retains at most the last 4000 stdout characters; no statement instance or provenance-to-acceptance chain is supplied. No inspected compiler read-back consumes Run summaries. Distinct from process-verification [EPI-OBJ-evidence](#epi-obj-evidence) and external [RT-CMP-runtime-model](runtime.md#rt-cmp-runtime-model).

### Routes

#### EPI-RTE-clarification-select
Label: Clarification selection

CLI/root/excluded IDs → canonical scan → active kinds and ordered gaps → one question. Code owns deterministic selection; caller answers/defers outside this method. No supplied counterpart: [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) supplies the raw idea but does not select questions. Target: presence of four problem kinds, not truth or evidence quality of statements. Proposed claims count active. The fixed gap prompts/reasons are guidance, not generated explanatory claims. For a repository with only one raw idea, the next question concerns the affected actor; adding even a proposed affected-actor claim moves selection to the problem question. This is a deduction from implementation, not execution. Operating mode: open user clarification, with no expected semantic answer oracle; caller exclusions can defer, code vetoes unknown IDs. No answers or knowledge updates persist here.

Evidence: SRC-1, `src/echel/methodology/clarification.py` (implementation).

- Immediate return: ClarificationResult/question/unresolved kinds or structured error.
- Later read-back: inapplicable — the result does not write accumulated content; subsequent calls rescan caller-maintained claims.
- Delegated visibility: CLI user receives prompt/reason/basis; no model invocation.
- Selection predicate: Exactly one project/raw idea; claim kinds except rejected/superseded/stale; first missing non-excluded gap.
- Invalidation or expiry: Rescan each call; exclusions are request scoped.
- Activation or effect: Advisory next question in current call; no acceptance or stage mutation.
- Evidence limits: Only kind presence is assessed; no actual answer or warranted problem statement supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if item.record["status"] not in {"rejected", "superseded", "stale"}
> --- `src/echel/methodology/clarification.py`

#### EPI-RTE-maturity-check
Label: Maturity assessment

Canonical project ID → selected profile/base stage requirements → accepted claims at current stage → linked active finding severities → MaturityAssessment. Code computes the target: usability under policy, not adequacy of claim content. Closest [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) has a different legacy gate; runtime mentions canonical services without declaring this referent. Required-kind dictionary retains one ID per kind, so duplicate accepted claims of a kind do not cause every such claim's finding to block. No inference of exhaustive contradiction coverage follows. Policy/schema/status values supply predicates, not product answer oracles. Caller provides accepted claims/findings; program can veto advance through its result.

Evidence: SRC-1, `src/echel/lifecycle.py` (implementation).

- Immediate return: Usable Boolean, missing kinds, blockers/cautions and next stage.
- Later read-back: inapplicable — assessment itself is not retained; later assessments load changed canonical records.
- Delegated visibility: API caller only; legacy compiler is not this consumer.
- Selection predicate: Accepted claim at current stage; active finding explicitly affects a selected required claim ID.
- Invalidation or expiry: Recomputed on assess; no expiry mechanism or certification.
- Activation or effect: Preview advance consumes unusable result as enforcing block; status explanation is advisory otherwise.
- Evidence limits: Structural usability only; duplicate-kind and explicit-link limits; no observed maturity success.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> usable=not missing and not blocking,
> --- `src/echel/lifecycle.py`

#### EPI-RTE-maturity-advance
Label: Maturity advance

Caller asks to advance → labelled human lifecycle capability/rationale/time → assessment → project revision → apply/store. Part of the canonical service family mentioned in runtime, but no supplied dedicated route counterpart. Distinct from [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) and its force option. Caller proposes/decides the stage change; code can reject unauthorized labels, unusable current stage, no next stage or inconsistent metadata/write conflict. Criterion: current policy usable and next exists; intended use: stage advance, not claim truth acceptance. Apply validates transition metadata and project revision, but does not rerun assessment or bind every supporting claim/finding revision. Evidence changes after preview can therefore escape that gate if project preconditions remain satisfied. Operating mode: open explicit review; oracle is the fixed structural assessment, not expected product behavior. Guidance: rationale and human-labelled advance. What persists is maturity/actor/reason, not new product evidence. Recovery: reload/review on conflict; no automatic compensation.

Evidence: SRC-1, `src/echel/lifecycle.py` (implementation).

- Immediate return: Preview transition or applied RecordWritePlan/error.
- Later read-back: Project maturity and rationale are read by later assessments/profile inspection.
- Delegated visibility: inapplicable — no agent delegation.
- Selection predicate: Authorized-labelled caller; usable assessment and a next stage.
- Invalidation or expiry: Project revision/digest conflict; evidence set is not atomically frozen by apply.
- Activation or effect: Permits next canonical stage; project-state update consumed on later API calls.
- Evidence limits: Identity is caller supplied; no actual human review or product correctness evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not assessment.usable or assessment.next is None:
> --- `src/echel/lifecycle.py`

#### EPI-RTE-stale-propagation
Label: Backward stale propagation

Caller finding/root/principal/reason → open/accepted finding and explicit affects check → traverse informs/supports through protected types → accepted records become stale → transaction execute. No dedicated supplied counterpart; related [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) decides proposed records instead of withdrawing accepted status. Target: reviewed reliance withdrawal, not a determination of falsity. Human-labelled knowledge:decide caller initiates and can withhold request; code vetoes inactive/unrelated finding, unaccepted root or malformed staged metadata. Operating mode: open backward review, no independent semantic oracle. Rationale/finding/root guide the change and persist in staleness metadata. Protected paths stop at nonprotected nodes; no universal dependency propagation. Journal commit recovery rolls forward durable commit intent and prepared rollback discards intent; this is storage recovery, not semantic reversal. Transactions obtain expectations during preparation, not from all original preview reads, so do not infer a frozen multi-record evidential snapshot.

Evidence: SRC-1, `src/echel/lifecycle.py`, `src/echel/storage/transactions.py` (implementation).

- Immediate return: BackwardRevision preview, applied transaction or error.
- Later read-back: Canonical load/scan and later maturity checks see stale statuses and reasons.
- Delegated visibility: inapplicable — no delegated runtime or recall channel.
- Selection predicate: Accepted protected root and accepted protected downstream nodes along informs/supports; explicit active finding affects root.
- Invalidation or expiry: Changes status to stale; no time expiry and no retraction of already delivered model context.
- Activation or effect: Withdraws accepted-kind eligibility at canonical consumers after installation; does not rewrite claim text or legacy knowledge.
- Evidence limits: No observed correction cycle; relationship truth unverified; concurrent/recovery guarantees not exhaustively audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> updated["status"] = "stale"
> --- `src/echel/lifecycle.py`

#### EPI-RTE-finding-review
Label: Finding review and impact

Caller supplies finding statement/kind/severity/affected records → service creates open finding plus affects relationships → journal retention; later human-labelled finding:decide request accepts/resolves/dismisses with rationale → impact recalculated. Closest supplied [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) reads legacy findings; this is canonical creation/review feeding maturity. Targets are structural admissibility, active severity impact, and a caller judgement of disposition, separately—not automatic semantic diagnosis. No model critic is invoked. Caller proposes content and decision; code vetoes invalid/duplicate affected IDs, forbidden links, unauthorized labels, empty rationale or invalid states. Open and accepted error/critical findings block when relevant; resolved/dismissed remove that effect without rewriting affected content. Operating mode: open human-labelled review; fixed severity mapping is an impact rule, not truth oracle. Guidance/retained result: statement/provenance/reason and decision metadata. No generic reopen/undo in inspected decision path; conflicts require explicit reconciliation.

Evidence: SRC-1, `src/echel/findings.py` (implementation).

- Immediate return: FindingCreation/FindingDecision/impact or error; apply creates records or revises finding.
- Later read-back: Finding and links read by assess and canonical maturity; decision rationale retained.
- Delegated visibility: inapplicable — no runtime invocation; canonical findings are not automatically converted into legacy compiler findings.
- Selection predicate: Known kind/severity, unique existing affected targets; decision from open/accepted state; accepted→accepted rejected.
- Invalidation or expiry: Resolved/dismissed are inactive; no timer; current findings/links read on later assessment.
- Activation or effect: Severity is enforcing via maturity preview, advisory via impact result; disposition changes later gate eligibility.
- Evidence limits: No evidence-consuming criterion requires proving the finding true or resolution sufficient; no observed criticism instance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> active = finding["status"] in ACTIVE_FINDING_STATES
> --- `src/echel/findings.py`

#### EPI-RTE-profile-selection
Label: Profile selection

Project/target/principal/rationale → inspect registered policy → revised profile metadata → apply/store. No supplied dedicated counterpart; [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) initially sets a profile but does not change one. Target is policy selection, not product truth. Caller chooses prototype/product/production/regulated; human-labelled profile:change authorization and program consistency/write checks can veto. Both upgrades and downgrades among registered profiles are possible; there is no implemented evidence-responsive autonomous policy tuner. New required-kind lists are a deduplication of base and additions. Operating mode: explicit open policy choice; no correctness oracle or certification. Rationale/actor/old/new persist. Recovery is conflict/review rather than automatic rollback.

Evidence: SRC-1, `src/echel/profiles.py` (implementation).

- Immediate return: Inspection/transition or write/error.
- Later read-back: Later LifecycleService.assess reads selected profile and changed required kinds.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Known different target plus human-labelled capability, rationale and time.
- Invalidation or expiry: Project revision/digest guards; no expiry.
- Activation or effect: Enforcing policy input for subsequent maturity assessment; no agent tool restriction or model parameter change.
- Evidence limits: Choice may change the floor without new evidence; actual activation/improvement unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> policy.required_for(stage.id, stage.required_kinds)
> --- `src/echel/profiles.py`

#### EPI-RTE-relationship-write
Label: Explicit relationship write

Caller source/predicate/target/reason/provenance → existing endpoint and allowed type-pair checks → schema preview → apply revalidates → canonical write. No supplied counterpart; differs from legacy work relations in [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow). Target: syntactic/type-policy eligibility; nonempty rationale is not evaluation of semantic support. Caller proposes link and decides to apply; code can veto missing/self/disallowed endpoints and malformed/conflicting writes. Operating mode: open link authoring, no model or expected truth oracle. Guidance is core/v1 relation policy; retained result includes reason/provenance. Query and stale propagation consume edges symbolically. Link creation can integrate an already accepted claim with evidence, but also permits proposed knowledge: no acceptance precondition. Thus post-acceptance integration is conditional, not demonstrated. No automatic semantic rollback; canonical revision workflow needed to change content.

Evidence: SRC-1, `src/echel/relationships.py` (implementation).

- Immediate return: RelationshipTransition or write/error.
- Later read-back: Canonical query/impact and backward revision load these relationships.
- Delegated visibility: API returns full link/reason/provenance; no automatic agent delivery.
- Selection predicate: Typed existing distinct endpoints, allowed core/v1 predicate, nonempty reason; pending endpoints allowed for staged creation.
- Invalidation or expiry: Revalidation on apply; no automatic expiry or proof of semantic consistency.
- Activation or effect: Permits link storage; query path selection and stale reachability depend on accepted edge metadata.
- Evidence limits: Edge semantics remain caller assertions, not checked entailment or acceptance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not self.policy.allows(predicate, source_type, target_type):
> --- `src/echel/relationships.py`

#### EPI-RTE-canonical-query
Label: Canonical query and projection

Canonical files → disposable SQLite/FTS rebuild → query hits → canonical rehydration and current-index assertion → provenance/path result. No supplied counterpart; [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) uses legacy explicit relations rather than this query API. Target of freshness: current canonical bytes and matching identities/relations; evaluator is digest and field equality. Target of selection: lexical query and explicit edge direction/depth, not verified relevance or causal impact. Index text recursively gathers strings except extensions; original content is still reloaded. BM25 orders search hits with record-ID tie-break and limit. This is reshaping/ranking; relationship-derived impact is a path under explicit policy, not a claim that all real impacts have been found. Caller chooses query/depth; fixed code vetoes bad query/limit/stale state. No reference semantic answer oracle. Rebuild/discard modifies cache only. No epistemic endorsement from freshness.

Evidence: SRC-1, `src/echel/queries.py`, `src/echel/storage/index.py` (implementation).

- Immediate return: Canonical ProvenancedRecord tuples, reverse-link explanations or bounded ImpactResult; stale/invalid errors.
- Later read-back: Cache can serve later calls but each guarded read compares canonical snapshot; records/provenance reloaded.
- Delegated visibility: API caller receives full canonical record and provenance; no direct Hermes/legacy compiler wiring.
- Selection predicate: FTS match/BM25/limit or explicit graph traversal (depth 1–10); no accepted-only filter.
- Invalidation or expiry: Discard/rebuild; fingerprint mismatch blocks use; post-query freshness asserted.
- Activation or effect: Enforcing freshness veto on query, ranking force to caller; advisory impact paths; no automatic knowledge revision.
- Evidence limits: No semantic relevance/edge-truth test; concurrent snapshot isolation and adversarial cache modification not proved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> records = tuple(self._from_search_hit(hit) for hit in hits)
> self.index.assert_current()
> return records
> --- `src/echel/queries.py`

#### EPI-RTE-portable-import
Label: Portable import and export

Canonical scans → deterministic ordered export bundle; external bundle → preview schema/path/order/ID/relationship endpoint/fingerprint checks → empty-target apply → transaction write. No supplied counterpart; [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) reviews proposals while import transfers existing supplied authority metadata. Target: bundle internal coherence and unchanged digest, not source trust or substantive correctness. Caller supplies bundle and requests apply; code can veto invalid/oversized/version-mismatched/orphan/modified/nonempty target. Operating mode: explicit repository transfer, no truth oracle or authenticated reviewer. Guidance is format/schema; proposed and accepted statuses/provenance persist as supplied, without a second knowledge decision. Recovery uses transaction machinery, not a semantic rejection/review. Export itself is non-ampliative serialization; import is acquisition, not new knowledge production.

Evidence: SRC-1, `src/echel/portability.py` (implementation).

- Immediate return: ExportBundle, ImportPlan or ImportResult/error.
- Later read-back: Canonical services/query/maturity can load transferred records after installation.
- Delegated visibility: inapplicable — no runtime delegation.
- Selection predicate: Canonical record families only; empty target; deterministic order, valid IDs/versions/endpoints and matching fingerprint.
- Invalidation or expiry: Apply checks empty target and plan fingerprint; transaction recovery for install; origin signatures not checked.
- Activation or effect: Permits imported supplied accepted statuses to become canonical gate inputs; metadata preservation is not authenticated acceptance.
- Evidence limits: Source warrant unknown; full transactional atomicity/concurrency not audited; no transfer instance supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> raise self._invalid("/records", "records must use deterministic canonical path order")
> --- `src/echel/portability.py`

#### EPI-RTE-schema-migration
Label: Schema migration and recovery

Caller target/version/time/resolutions → v0 record clone → remove_fields/set_fields → version/revision/migration extension → schema validation → staged bytes/backups → commit/recover or guarded rollback. No supplied counterpart; ordinary [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) is not required to supply arbitrary migration resolutions. Target: version/schema and source/staged digests, not preservation of statement meaning or genuine authority. A concrete implementation deduction: input statement `Exports require consent.` plus resolution set_fields statement `Exports never require consent.` replaces that field before validation. If the remaining envelope validates, no semantic comparator vetoes the reversal. With empty resolution, statement text is preserved while envelope metadata changes. Hence the unrestricted route is indeterminate between reshaping, imported edits, and new claims; cannot classify every migration as lossless or ampliative. Caller proposes resolutions/applies; software vetoes bad versions, invalid target records, source/staged conflicts. Operating mode: explicit maintenance, schema oracle only. Backups retain exact sources and recovery rolls forward committing intent; rollback refuses postmigration changes. Guidance is schema plus caller resolution, not evidence review; what persists includes changed fields and migration metadata.

Evidence: SRC-1, `src/echel/migrations.py` (implementation).

- Immediate return: MigrationPlan or result/error; already-current returns no change.
- Later read-back: Canonical consumers load migrated records; backups allow guarded byte restoration.
- Delegated visibility: inapplicable — no agent invocation.
- Selection predicate: Uniform supported source versions 0/1 to target 1; explicit resolutions only for known IDs.
- Invalidation or expiry: Source/target/staged digests; post-change rollback conflict; no semantic expiry.
- Activation or effect: Changes canonical content/metadata and thus future consumers; no authority-service or truth-preservation guarantee established.
- Evidence limits: Implementation paths inspected, not helper/security audit or fault-injection evidence; caller edits require independent warrant.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> migrated.update(set_fields)
> --- `src/echel/migrations.py`

#### EPI-RTE-integrity-check
Label: Integrity diagnostics

Canonical paths → decode/version/schema/path/duplicate/endpoint checks → optional index freshness diagnostic → sorted issues and healthy Boolean. No supplied dedicated counterpart; canonical authority route checks admission rather than repository-wide diagnostics. Target: stored structural integrity, explicitly not truth of statements, soundness of reasons or authenticated approval. Program maps errors to unhealthy and cache problems to warnings; no automatic repair/disposition consumer is wired here. Caller may act on repair guidance but that is not observed or enforced. Operating mode: on-demand inspection; reference predicates are schema/identity/fingerprint, not product answer oracle.

Evidence: SRC-1, `src/echel/integrity.py` (implementation).

- Immediate return: IntegrityReport(healthy, checked count, issues/remedies).
- Later read-back: inapplicable — inspection does not retain or repair content; callers may save returned report externally.
- Delegated visibility: inapplicable — no delegated consumer.
- Selection predicate: Canonical project and record JSON paths plus disposable index when present.
- Invalidation or expiry: Point-in-time inspect; cache missing/stale can be warning rather than unhealthy.
- Activation or effect: Advisory report to caller in current invocation; no implemented automatic admission veto or repair.
- Evidence limits: Healthy does not entail product truth, complete relationships or correctly accepted evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> healthy = not any(issue.severity == "error" for issue in ordered)
> --- `src/echel/integrity.py`

#### EPI-RTE-kernel-gate
Label: Synthetic kernel gate

Caller dataset sizes/samples → synthetic SQLite population → direct SQL timings/counts → report.passed → main exit 0/1 and JSON. No supplied route counterpart; [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) is broader contributor admission. Target: generated SQL kernel counts and sampled p90 query latency under QUERY_TARGET_MS; oracle is threshold arithmetic, not context correctness, learning or product success. Observations are perf_counter intervals when run; supplied local artifact is only attributed reported operation (boundary). Timing Boolean is operative at CLI exit. The gate queries its own connection directly, bypassing the full QueryService canonical rehydration/fingerprint path, so it cannot warrant its end-to-end latency. Caller chooses sample configuration; software rejects under-minimum sizes/samples and Boolean vetoes success status. Operating mode: bounded synthetic benchmark, no independent component variation or product scenario baseline. No automatic method revision or release approval.

Evidence: SRC-1, `benchmarks/kernel/gate.py` (implementation).

- Immediate return: KernelGateReport JSON; exit code from passed.
- Later read-back: inapplicable — gate prints report and leaves generated database; no retained result is read by product runtime here.
- Delegated visibility: inapplicable — no model/runtime delegation.
- Selection predicate: Synthetic generator and three SQL operations, minimum counts and samples; fixed timing threshold.
- Invalidation or expiry: Database replaced per run; no automatic invalidation/reproduction of stored local result.
- Activation or effect: Enforcing process exit gate only, immediate run horizon; downstream CI/release adoption unobserved.
- Evidence limits: No executed target command; reported artifact not independently reproduced; hardware, full API and scenario effects excluded.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return 0 if report.passed else 1
> --- `benchmarks/kernel/gate.py`

The migration and query classifications use these additional implementation passages (SRC-1):

> for field in remove_fields:
>     migrated.pop(field, None)
> migrated.update(set_fields)
> --- `src/echel/migrations.py`

> if metadata.get("fingerprint") != current:
>     connection.close()
>     raise IndexError(
>         "ECHEL-INDEX-STALE", self.path, "canonical records changed; rebuild the index"
>     )
> --- `src/echel/storage/index.py`

> if key != "extensions":
>     collect(value[key])
> --- `src/echel/storage/index.py`

> ORDER BY bm25(records_fts), r.record_id LIMIT ?""",  # nosec B608
> --- `src/echel/storage/index.py`

> return self.store.write(transition.record, transition.expectation)
> --- `src/echel/lifecycle.py`

> self.transactions.execute(revision.transaction_id, list(revision.records))
> --- `src/echel/lifecycle.py`

The authority service records a rationale but no required evidence-consuming semantic test (SRC-1); the supplied runtime record supplies authorization/eligibility evidence:

> updated["authority"] = {
>     "action": action,
>     "actor": principal.id,
>     "actor_kind": "human",
>     "capability": AUTHORITY_CAPABILITY,
>     "rationale": rationale.strip(),
>     "decided_at": decided_at,
>     "proposal_revision": loaded.record["revision"],
> }
> --- `src/echel/authority.py`

### Claims

#### EPI-CLM-trustworthy-context
Label: Smallest trustworthy context

Claimed operation: the agent receives the smallest trustworthy work context. Source: SRC-1, `README.md` (doctrine/design). Closest supplied [RT-CLM-runtime-boundary](runtime.md#rt-clm-runtime-boundary) claims responsibility separation, not context minimality/warrant; this is a distinct claim. Mechanism comparison: [RT-RTE-compile-run](runtime.md#rt-rte-compile-run). Exact native statement is shared with the next claim:

> It starts with one raw idea, asks only the questions required by the current stage, and lets product knowledge mature alongside implementation. Echel supplies an AI agent with the smallest trustworthy context needed for a work item and promotes verified discoveries back into durable project memory only after approval.
> --- `README.md`

#### EPI-CLM-approved-discoveries
Label: Approved verified discoveries

Claimed operation: verified discoveries return to durable project memory only after approval. Source: SRC-1, `README.md`, quotation above (doctrine/design). Distinct from [RT-CLM-runtime-boundary](runtime.md#rt-clm-runtime-boundary) and context selection claim: this asserts promotion and approval, not ownership or selection. Validation/operations instructions support the intended evidence-and-review procedure, not an implemented automatic bridge. Canonical human-labelled review supports a narrow approval protocol; legacy accepted writes, direct schema-valid writes and imported metadata limit the system-wide reading. Concrete acquired content and a reviewed decision can be retained without establishing a newly produced accepted ampliative claim.

> Evaluate acceptance conditions, regressions, security, operability, and product intent. Prefer executable checks. Tie evidence to the work item and exact source revision. Record failures as findings rather than editing requirements to match the implementation.
> --- `skills/validation/SKILL.md`

> Collect user feedback, incidents, metrics, costs, and operational friction. Relate findings to existing knowledge and work. Propose corrections, new assumptions, or work items with provenance. Do not let runtime memory silently alter product truth.
> --- `skills/operations/SKILL.md`

#### EPI-CLM-evaluation-contract
Label: Evaluation evidence contract

Claimed warrant: outcome acceptance requires condition-specific evidence and recorded review; provisional thresholds do not prove achieved quality. Source: SRC-1, `docs/product/evaluation-metrics.md` (doctrine/design). No supplied counterpart after comparison with [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) (contributor workflow, not the scenario measurement claim). Defines immutable conditions, review and disclosure intended for product scenarios; does not claim present execution. Kernel gate is narrower and not counterevidence to this explicit future-work qualification.

> A task is accepted only when its immutable acceptance conditions have sufficient evidence and the required reviewer records a decision. Runtime completion, a patch, a commit, or green tests alone are not acceptance.
> --- `docs/product/evaluation-metrics.md`

> E2-063 implements the context benchmark harness and E2-105 runs the release comparison. Until those tasks produce evidence, this document defines how success will be measured, not proof of success.
> --- `docs/product/evaluation-metrics.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
