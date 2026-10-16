---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Spacebot epistemic routes: extraction, operational admission, consolidation, withdrawal and later reliance, distinguished from truth acceptance."
run-id: AAS-2026-10-14-spacebot-6a954b400f95-01
reviewed-boundary: "5c2ee47b397e09c956dc15000ea576ecd28e92bb"
---

# Spacebot epistemic report

## Source-and-claim boundary

The question is how Spacebot turns conversations, files and work into content on which later processes can rely, and what its checks license. The whole-system functional scope and exclusions remain those of the [boundary](boundary.md#boundary-and-evidence); the [Source register](boundary.md#source-register) supplies SRC-1. This report does not create another source. Every new finding below is implementation or doctrine/design at that frozen commit. No run, persisted candidate instance, experiment or user database was supplied. Accordingly, architectural capacity can be assessed, but exercise, semantic compliance, benefit and causal attribution cannot.

The source supports heterogeneous routes, not one truth oracle. Memory extraction and procedure reflection ask models to judge what is worth retaining. Programs check shape, identifiers and completion. Search, ranking and rendering make retained material usable. These are different operations. A saved `fact`, an `updates` edge, a successful terminal signal and a versioned wiki edit are not themselves evidence-consuming truth acceptance decisions.

Public/design claims assessed here are [EPI-CLM-memory-context](#epi-clm-memory-context), [EPI-CLM-write-consolidation](#epi-clm-write-consolidation), [EPI-CLM-better-use](#epi-clm-better-use), and [EPI-CLM-wiki-verification](#epi-clm-wiki-verification). Instruction delivery and role-grant qualifications remain in [RT-CLM-required-skills](runtime.md#rt-clm-required-skills) and [RT-CLM-role-grants](runtime.md#rt-clm-role-grants).

### Coverage

Direct inspection means selected executable bodies, prompt passages or dispatch definitions, not every line of the named file. Supplied findings are explicitly distinguished.

| Entry point or operation | SRC-1 path | Coverage / records or limit |
|---|---|---|
| CLI resource dispatch | `src/cli/mod.rs`; bounded searches of `src/cli/memory.rs`, `src/cli/wiki.rs`, `src/cli/ingest.rs` | Direct enum/dispatch inspection: Memory, Wiki and Ingest are shipped alternate surfaces, not external hosts. Searches identify memory inspection and wiki create/edit/archive/restore API calls; all CLI/API mutation handlers not audited. |
| Main conversational, delegated, cron, autonomy and OpenCode entry | `src/main.rs`, `src/agent/channel.rs`, `src/opencode/worker.rs` | Supplied [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn), [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work), [RT-RTE-autonomy-epoch](runtime.md#rt-rte-autonomy-epoch), [RT-RTE-opencode-work](runtime.md#rt-rte-opencode-work). No fresh audit of their complete tool-result semantics. |
| Persistence and ingestion | `prompts/en/memory_persistence.md.j2`, `prompts/en/ingestion.md.j2`, `src/agent/ingestion.rs`, `src/tools.rs` | Direct selected prompt, chunk construction, completion classification and branch tool registration: [EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-completion-contract](#epi-rte-completion-contract). |
| Memory writes, consolidation and withdrawal | `src/tools/memory_save.rs`, `src/tools/memory_delete.rs`, `src/memory/consolidation.rs`, `src/memory/maintenance.rs` | Direct validation/save, batch merge, soft forgetting, decay/prune/merge bodies: [EPI-RTE-memory-save](#epi-rte-memory-save), [EPI-RTE-batch-consolidation](#epi-rte-batch-consolidation), [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal). Store call sites/searches do not constitute a full SQL audit. |
| Recall and standing context | `src/memory/search.rs`, `src/memory/render.rs`, `src/memory/store.rs` | Direct graph expansion and complete production renderer; store forgotten predicates searched: [EPI-RTE-memory-selection](#epi-rte-memory-selection), [EPI-RTE-memory-render](#epi-rte-memory-render). Hybrid retrieval fusion, participant rendering and every temporal/chronicle retrieval path remain unassessed here. |
| Hook completion, leak cleanup and result broadcast | `src/hooks/spacebot.rs` | Direct contract/nudge predicates and result event/termination bodies: [EPI-RTE-completion-contract](#epi-rte-completion-contract), [EPI-RTE-result-filtering](#epi-rte-result-filtering). Pattern detector implementation and full loop-guard/retry behavior not audited. |
| Wiki model write/read plus alternate API/CLI mutation | `src/tools/wiki_create.rs`, `src/tools/wiki_edit.rs`, `src/tools/wiki_read.rs`, `src/wiki/store.rs`, `skills/builtin/wiki-writing/SKILL.md` | Direct tool calls, create/edit, tolerant replacement and selected procedure passages: [EPI-RTE-wiki-mutation](#epi-rte-wiki-mutation). Store history/restore/archive signatures searched, not all bodies assessed. API callers remain separately uninspected. |
| Procedure and machinery changes | `src/tools/skill_manage.rs`, `src/skills.rs`, `src/api/config.rs` | Supplied [RT-RTE-skill-change](runtime.md#rt-rte-skill-change), [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction), [RT-BAP-runtime-config](runtime.md#rt-bap-runtime-config). No new claim of semantic acceptance. |
| Behavioral evaluators | `tests/behavioral_fixtures.rs` | Direct fixture definition, first-event capture and threshold: [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures). Other source tests are not comprehensively assessed; no results supplied. |
| Numerical inference state | `src/memory/embedding.rs`, `src/llm/model.rs` | Direct embedding wrapper; supplied [RT-CMP-spacebot-model](runtime.md#rt-cmp-spacebot-model). Provider/fastembed internals and exact downloaded model identity unavailable within SRC-1. |
| Other exposed effects and evaluators | `src/tools.rs`, `src/api/server.rs`, `src/tools/web_search.rs`, `src/tools/browser.rs`, `src/mcp.rs`, `src/agent/cortex.rs` | Tool registration/search inventory plus supplied runtime coverage only. Search/browser/MCP source warrant, all API edits, cortex diagnostics, identity/factory writes, goals/tasks outcome interpretation and full update CLI are not independently traced. Available uninspected code, not absence. |

These remaining operations prevent a system-complete negative about truth checks or acceptance. Missing run evidence prevents concluding that a particular proposition was extracted, conjectured, tested, accepted or used. Missing source-content comparisons prevent classifying actual model outputs as non-ampliative or ampliative. Missing controlled comparisons prevent improvement or component-effect attribution. External inference, OpenCode and remote service internals retain the boundary's exclusions; no claims about their internal evaluators follow.

## Epistemic-object inventory

Fields owned by a record are given there; the table is an overlay, not a second declaration.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-content](#epi-obj-memory-content) | Statements about users, projects, decisions, observations; actual statements not supplied | see record | SRC-1 `src/tools/memory_save.rs` | Type labels do not certify propositions. |
| [EPI-OBJ-memory-metadata](#epi-obj-memory-metadata) | None for selectors themselves; relational labels can assert content relationships | see record | SRC-1 `src/memory/search.rs` | `contradicts` is not adjudication. |
| [EPI-OBJ-completion-state](#epi-obj-completion-state) | Whether specific successful save IDs were recorded in the current process | see record | SRC-1 `src/tools/memory_persistence_complete.rs` | Does not individuate truth of saved text. |
| [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | Versioned article assertions, potentially procedures | see record | SRC-1 `src/wiki/store.rs` | No actual article or verified correction supplied. |
| [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history) | Utterances and tool-result assertions | see record | SRC-1 `src/agent/channel.rs` | Speaker/source warrant varies; summary fidelity unobserved. |
| [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set) | Procedures may contain assertions; imperatives themselves are not truth-apt | see record | SRC-1 `src/skills.rs` | Particular formulated theory not determinable. |
| [EPI-OBJ-fixture-sample](#epi-obj-fixture-sample) | Assertions about first visible tool/arguments, reply or timeout | see record | SRC-1 `tests/behavioral_fixtures.rs` | Test definitions only, not sampled results. |
| [EPI-CMP-embedding-model](#epi-cmp-embedding-model) | Dense vectors do not expose individuated propositions here | see record | SRC-1 `src/memory/embedding.rs` | Truth-apt internal content not determinable. |
| [RT-CMP-spacebot-model](runtime.md#rt-cmp-spacebot-model) | Generated statements possible; parametric propositions not individuated | see record | SRC-1 `src/llm/model.rs` | Opaque provider weights are not evidence of acceptance or absent learning. |

## Authority-route ledger

All listed implemented routes have unobserved operation. `see` fields point to the declaring record rather than repeating its owned details. An indeterminate transformation requires actual inputs/outputs and a scoped semantic comparison; lack of an entailment proof alone is not evidence of ampliation.

Route ID: [EPI-RTE-memory-extraction](#epi-rte-memory-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: conversation/file statements to selected distilled statements; acquisition precedes the model transformation. External source warrant is unknown, not upgraded by extraction.
Evaluator/condition and domain: model selection under relevance, durability and stale-conflict instructions; no fixed answer oracle.
Activation and timing: see [EPI-RTE-memory-extraction](#epi-rte-memory-extraction).
Possible or observed result: see [EPI-RTE-memory-extraction](#epi-rte-memory-extraction).
Implemented force: candidate generation and tool requests, not enforced semantic verification.
Epistemic authority and scope: source testimony and model interpretation only; no particular produced accepted ampliative claim established.
Operational authority: behavior permitted, blocked, or changed: model can request writes and associations.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/agent/ingestion.rs`, `prompts/en/memory_persistence.md.j2`.
Claim IDs or none: [EPI-CLM-better-use](#epi-clm-better-use).
Mismatch marker or none: none.
Gap/limit: no actual proposition/output pair; preservation, entailment and novel conjecture remain distinguishable but unresolved.

Route ID: [EPI-RTE-memory-save](#epi-rte-memory-save)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content), [EPI-OBJ-memory-metadata](#epi-obj-memory-metadata)
Content/update relation: no content change
Transition or check target: empty/oversized text, out-of-range importance, known type, required human key, association target existence and embedding success.
Evaluator/condition and domain: Rust validation and backing-store/index outcomes; see record.
Activation and timing: see [EPI-RTE-memory-save](#epi-rte-memory-save).
Possible or observed result: see [EPI-RTE-memory-save](#epi-rte-memory-save).
Implemented force: enforcing within this tool; invalid association targets are skipped rather than invalidating the content.
Epistemic authority and scope: bounded evidence about shape, referential integrity and recorded pipeline success, not factual truth or entailment of relations.
Operational authority: behavior permitted, blocked, or changed: permits or refuses this write pipeline; embedding failure invokes compensation.
Behavioral-authority path: tool caller via result/error, enforcing for that call; future consumers via [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/tools/memory_save.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: not a universal admission gate over generic files, API changes or other retained artifacts.

Route ID: [EPI-RTE-memory-save](#epi-rte-memory-save)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: submitted bytes persist; human anchors append prior content plus the submitted observation.
Evaluator/condition and domain: see [EPI-RTE-memory-save](#epi-rte-memory-save).
Activation and timing: see [EPI-RTE-memory-save](#epi-rte-memory-save).
Possible or observed result: see [EPI-RTE-memory-save](#epi-rte-memory-save).
Implemented force: durable availability, not lifecycle integration after truth acceptance.
Epistemic authority and scope: no additional source warrant established by persistence or a `fact` type.
Operational authority: behavior permitted, blocked, or changed: retained content can enter recall and later prompts before any semantic acceptance.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/tools/memory_save.rs`.
Claim IDs or none: [EPI-CLM-memory-context](#epi-clm-memory-context).
Mismatch marker or none: none.
Gap/limit: source field is caller-supplied; it is not an authenticated citation chain.

Route ID: [EPI-RTE-completion-contract](#epi-rte-completion-contract)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-completion-state](#epi-obj-completion-state)
Content/update relation: no content change
Transition or check target: submitted terminal outcome against successful save IDs recorded in this run.
Evaluator/condition and domain: set comparison, duplicate/empty checks and minimum reason length; see record.
Activation and timing: see [EPI-RTE-completion-contract](#epi-rte-completion-contract).
Possible or observed result: see [EPI-RTE-completion-contract](#epi-rte-completion-contract).
Implemented force: enforces reporting consistency, not completeness of extracted knowledge.
Epistemic authority and scope: a bounded implementation-derived claim about recorded saves. `no_memories` establishes a permitted terminal declaration, not that nothing true or useful existed.
Operational authority: behavior permitted, blocked, or changed: errors refuse an inconsistent completion.
Behavioral-authority path: tool result to hook and ingestion caller; see record.
Evidence source ID and local anchor: SRC-1 `src/tools/memory_persistence_complete.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: truth, coverage and adequacy of reason are not the check target.

Route ID: [EPI-RTE-completion-contract](#epi-rte-completion-contract)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-completion-state](#epi-obj-completion-state)
Content/update relation: no content change
Transition or check target: eligibility to terminate persistence/mark ingestion chunk processed.
Evaluator/condition and domain: hook and caller consume successful terminal evidence; see record.
Activation and timing: see [EPI-RTE-completion-contract](#epi-rte-completion-contract).
Possible or observed result: see [EPI-RTE-completion-contract](#epi-rte-completion-contract).
Implemented force: enforcing continuation/termination protocol.
Epistemic authority and scope: acceptance of the completion report for process control only, not acceptance of memory propositions for truth.
Operational authority: behavior permitted, blocked, or changed: terminate successfully after terminal tool; reject bare text or missing signal.
Behavioral-authority path: see [EPI-RTE-completion-contract](#epi-rte-completion-contract).
Evidence source ID and local anchor: SRC-1 `src/hooks/spacebot.rs`, `src/agent/ingestion.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: completing the process does not establish successful epistemic coverage.

Route ID: [EPI-RTE-batch-consolidation](#epi-rte-batch-consolidation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: model-supplied merged text replacing survivor and absorbing another memory.
Evaluator/condition and domain: see [EPI-RTE-batch-consolidation](#epi-rte-batch-consolidation).
Activation and timing: see [EPI-RTE-batch-consolidation](#epi-rte-batch-consolidation).
Possible or observed result: see [EPI-RTE-batch-consolidation](#epi-rte-batch-consolidation).
Implemented force: durable replacement and forgotten provenance targets; advice itself is advisory.
Epistemic authority and scope: transaction/type/identifier checks do not verify that merged text preserves, corrects or follows from its sources.
Operational authority: behavior permitted, blocked, or changed: survivor changes future recall/render; absorbed content leaves ordinary retrieval.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/memory/consolidation.rs`.
Claim IDs or none: [EPI-CLM-write-consolidation](#epi-clm-write-consolidation).
Mismatch marker or none: write-time advice is not a blocking merge invariant.
Gap/limit: retention/lineage is implemented; acceptance-then-integration is not established by an Updates edge.

Route ID: [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-metadata](#epi-obj-memory-metadata)
Content/update relation: non-truth-apt policy/content update: importance decay, deletion and survivor selection
Transition or check target: age/access/importance and vector-near candidates, not proposition truth.
Evaluator/condition and domain: see [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance).
Activation and timing: see [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance).
Possible or observed result: see [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance).
Implemented force: enforcing store mutation and later ranking/availability changes.
Epistemic authority and scope: neither recency nor similarity licenses truth or semantic equivalence.
Operational authority: behavior permitted, blocked, or changed: decay changes salience; pruning removes rows; merge retains a selected survivor.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/memory/maintenance.rs`.
Claim IDs or none: [EPI-CLM-write-consolidation](#epi-clm-write-consolidation).
Mismatch marker or none: separate background merge route exists.
Gap/limit: source wiring is not evidence of an active janitor in a deployment.

Route ID: [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: deterministic trim/substring suppression/concatenation/byte clipping.
Evaluator/condition and domain: see [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance).
Activation and timing: see [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance).
Possible or observed result: see [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance).
Implemented force: replacement survivor content, retained for later use.
Epistemic authority and scope: no general semantic-preservation guarantee; the concrete substring counterexample is in the record.
Operational authority: behavior permitted, blocked, or changed: suppresses text before future consumers receive it.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/memory/maintenance.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: some inputs are mere non-ampliative grouping; arbitrary inputs can lose necessary qualifications. No particular deployed outcome inferred.

Route ID: [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: no content change
Transition or check target: selected memory's availability through ordinary search/render.
Evaluator/condition and domain: model/tool caller chooses ID; program checks existence/forgotten state, not falsity.
Activation and timing: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal).
Possible or observed result: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal).
Implemented force: enforcing soft withdrawal for consumers honoring forgotten status.
Epistemic authority and scope: availability withdrawal, not a demonstrated refutation.
Operational authority: behavior permitted, blocked, or changed: exclude selected item from subsequent ordinary recall/render.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/tools/memory_delete.rs`, `src/memory/search.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: already delivered prompts, copied text and derived skills are not automatically retracted by this operation.

Route ID: [EPI-RTE-memory-selection](#epi-rte-memory-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-metadata](#epi-obj-memory-metadata)
Content/update relation: no content change
Transition or check target: candidate salience in graph expansion.
Evaluator/condition and domain: fixed type multipliers, edge weight, importance and forgotten filter; see record.
Activation and timing: see [EPI-RTE-memory-selection](#epi-rte-memory-selection).
Possible or observed result: see [EPI-RTE-memory-selection](#epi-rte-memory-selection).
Implemented force: ranking, not rejection of one side of a contradiction.
Epistemic authority and scope: retrieval relevance only; edge direction/truth not adjudicated here.
Operational authority: behavior permitted, blocked, or changed: conflicting items can remain eligible with reduced scores.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/memory/search.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: graph expansion part only, not full hybrid search assessment.

Route ID: [EPI-RTE-memory-render](#epi-rte-memory-render)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: stored text to first-line bullets, bounded by type caps and word budget.
Evaluator/condition and domain: deterministic formatting and truncation rules, not a truth evaluator.
Activation and timing: see [EPI-RTE-memory-render](#epi-rte-memory-render).
Possible or observed result: see [EPI-RTE-memory-render](#epi-rte-memory-render).
Implemented force: selection and prompt supply.
Epistemic authority and scope: no added warrant; hidden lines may contain conditions necessary to interpret the visible line.
Operational authority: behavior permitted, blocked, or changed: later channel receives selected first lines, not full memory content/provenance.
Behavioral-authority path: see [EPI-BAP-memory-context](#epi-bap-memory-context).
Evidence source ID and local anchor: SRC-1 `src/memory/render.rs`.
Claim IDs or none: [EPI-CLM-memory-context](#epi-clm-memory-context).
Mismatch marker or none: current store bytes do not establish current truth.
Gap/limit: concrete code deduction in record; not an observed incident.

Route ID: [EPI-RTE-wiki-mutation](#epi-rte-wiki-mutation)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-content](#epi-obj-wiki-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: caller-provided article/edit to current version plus history.
Evaluator/condition and domain: type parsing, slug resolution and tolerant old-string match; see record.
Activation and timing: see [EPI-RTE-wiki-mutation](#epi-rte-wiki-mutation).
Possible or observed result: see [EPI-RTE-wiki-mutation](#epi-rte-wiki-mutation).
Implemented force: content persistence and read-back; verification remains procedural guidance.
Epistemic authority and scope: version/authorship identifies an edit, not authoritative evidence for its assertions.
Operational authority: behavior permitted, blocked, or changed: wiki readers can consume updated content; historical reads remain possible.
Behavioral-authority path: see [EPI-BAP-wiki-readers](#epi-bap-wiki-readers).
Evidence source ID and local anchor: SRC-1 `src/wiki/store.rs`, `src/tools/wiki_edit.rs`.
Claim IDs or none: [EPI-CLM-wiki-verification](#epi-clm-wiki-verification).
Mismatch marker or none: verification requested, not enforced by inspected create/edit path.
Gap/limit: model edits may preserve, import or conjecture; actual content and evidence comparison missing.

Route ID: [EPI-RTE-result-filtering](#epi-rte-result-filtering)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: possible secret-pattern leaks and broadcast payload size, not proposition correctness.
Evaluator/condition and domain: hook scan/termination or scrub/cap; see record.
Activation and timing: see [EPI-RTE-result-filtering](#epi-rte-result-filtering).
Possible or observed result: see [EPI-RTE-result-filtering](#epi-rte-result-filtering).
Implemented force: enforcing channel termination or event transformation, depending on consumer.
Epistemic authority and scope: no truth license; event viewers may receive a partial/redacted trace.
Operational authority: behavior permitted, blocked, or changed: can stop continuation and withhold event bytes.
Behavioral-authority path: channel hook enforces current turn; worker/branch event payload reaches subscribers with scrubbed/capped content.
Evidence source ID and local anchor: SRC-1 `src/hooks/spacebot.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: event cleanup is not proof that model-internal tool results were identically cleaned, nor comprehensive secret detection.

Route ID: [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixture-sample](#epi-obj-fixture-sample)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: captured first-event sample against fixture predicate and pass count against threshold.
Evaluator/condition and domain: fixture closure and integer comparison; input sampling limitations in record.
Activation and timing: see [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures).
Possible or observed result: see [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures).
Implemented force: evidence production for developer assertion, not live model admission.
Epistemic authority and scope: conditional on correct capture/predicate, pass count entails threshold result. No warranted observed premises were supplied.
Operational authority: behavior permitted, blocked, or changed: supplies test result; does not automatically accept changed memory or skill content.
Behavioral-authority path: test process/output to developer; no inspected automatic successor-selection consumer.
Evidence source ID and local anchor: SRC-1 `tests/behavioral_fixtures.rs`.
Claim IDs or none: [EPI-CLM-better-use](#epi-clm-better-use).
Mismatch marker or none: first-tool contract is not end-to-end answer correctness.
Gap/limit: no test execution; no causal effect of a particular prompt component established.

Route ID: [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixture-sample](#epi-obj-fixture-sample)
Content/update relation: no content change
Transition or check target: fixture test completion.
Evaluator/condition and domain: assertion consumes threshold result; see record.
Activation and timing: see [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures).
Possible or observed result: see [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures).
Implemented force: enforcing test failure within that test process.
Epistemic authority and scope: a bounded routing-contract result, not knowledge acceptance or transfer safety.
Operational authority: behavior permitted, blocked, or changed: failing assertion fails the test; repository-wide deployment veto not traced.
Behavioral-authority path: see [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures).
Evidence source ID and local anchor: SRC-1 `tests/behavioral_fixtures.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no executed outcome or downstream release decision supplied.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-memory-context](#epi-clm-memory-context) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-memory-render](#epi-rte-memory-render), [EPI-RTE-memory-save](#epi-rte-memory-save) | none supplied | No freshness/truth experiment | Current store selection can be delivered without a synthesis-model call | “No staleness” licenses at most store-view freshness, not truth or complete content. |
| [EPI-CLM-write-consolidation](#epi-clm-write-consolidation) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-batch-consolidation](#epi-rte-batch-consolidation), [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance) | none supplied | No demonstrated duplicate resolution rate | Advisory write-time checks plus explicit model batch exist | Save lands first; background similarity merge also exists. Not an unconditional merge-on-save invariant. |
| [EPI-CLM-better-use](#epi-clm-better-use) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-skill-change](runtime.md#rt-rte-skill-change), [EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures) | none supplied | No before/after intervention or live trace; fixtures target first tools | Improvement-directed retained instruction change and later delivery are wired | Improvement, automatic semantic correction and beneficial accumulation unestablished. |
| [EPI-CLM-wiki-verification](#epi-clm-wiki-verification) | see record | SRC-1 `skills/builtin/wiki-writing/SKILL.md`, doctrine/design | see record | [EPI-RTE-wiki-mutation](#epi-rte-wiki-mutation) | none supplied | No inspected verification result consumed by create/edit handler | Agents are instructed to verify factual corrections and summarize their basis | Tool/store checks match/type and persists text; compliance and evidence quality unknown. |

## Bounded conclusion

Spacebot can acquire external testimony through messages and files, ask models to select/distill it, retain typed text and relationships, and expose it to later models. Its source warrant is unknown unless separately established; type, importance and association labels do not upgrade it. The automatic retention route allows reliance before demonstrated truth acceptance ([EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-memory-save](#epi-rte-memory-save), [EPI-BAP-memory-context](#epi-bap-memory-context)). No actual produced accepted ampliative claim was supplied. Model outputs cannot be classified as entailed or ampliative merely because the prompt says “extract” or “reflect.”

Checks have real but bounded force. Save checks enforce shape and pipeline success; completion checks enforce agreement with this run's saved-ID set and decide process termination. Similarity, access, age and importance alter availability and salience without judging truth. `contradicts` lowers graph weight but does not choose the true side. Forgetting excludes future ordinary retrieval, not already delivered copies or downstream derivatives ([EPI-RTE-completion-contract](#epi-rte-completion-contract), [EPI-RTE-memory-selection](#epi-rte-memory-selection), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal), [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance)). This is operational disposition, not a blanket absence of evaluation.

Two deterministic text paths need special caution. The renderer omits all but a memory's first nonempty line; maintenance can suppress a substring or clip bytes. Concrete code deductions below show why neither supports a universal meaning-preservation claim. Byte-current rendering is not truth-current rendering, and a provenance edge is not acceptance followed by lifecycle integration ([EPI-RTE-memory-render](#epi-rte-memory-render), [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance), [EPI-RTE-batch-consolidation](#epi-rte-batch-consolidation)).

Wiki verification is requested by procedure, while inspected write handlers admit caller text after structural/matching operations. Version history and read-back preserve inspectability, not warrant ([EPI-RTE-wiki-mutation](#epi-rte-wiki-mutation), [EPI-BAP-wiki-readers](#epi-bap-wiki-readers)). Behavioral fixtures do consume a named criterion for a narrow intended use: checking first-action routing under specified conversations, with a four-of-five threshold. They neither accept arbitrary generated propositions nor supply evidence that the tested behavior succeeded here ([EPI-RTE-behavioral-fixtures](#epi-rte-behavioral-fixtures)).

Procedure reflection remains an independently supported instruction-change capacity: trace inspection can lead to skill writes and later instructional delivery. The supplied [RT-RTE-skill-change](runtime.md#rt-rte-skill-change) independently bounds learning, reflection, self-improvement and theory-builder conditions 1–4. This report finds no new run evidence closing those limits. Autonomy admission does not establish epistemic autonomy or reliable criticism; parameter opacity does not negate non-parametric adaptation. Model-driven instruction updates and code-driven decay/selection are behavior-shaping routes even when no accepted truth-apt claim is established. These conclusions do not yield a single epistemic status or a system-wide negative: the coverage table names still-unassessed relevant operations.

## Shared records

### Components

#### EPI-CMP-embedding-model
Label: EmbeddingModel numerical encoder

Source-native identity: `EmbeddingModel` wraps `fastembed::TextEmbedding` in an Arc. Numerical parameters are distributed-parametric state in downloaded/cache-backed model files and memory; output vectors are dense numerical representations used for similarity, not localized natural-language claims. Distinct from [RT-CMP-spacebot-model](runtime.md#rt-cmp-spacebot-model), which wraps generative provider inference. SRC-1 `src/memory/embedding.rs` supplies implementation.

Parameters change during operation: no parameter-update API appears in this inspected wrapper; library internals uninspected. Exact version pinned: not established by this wrapper, which uses `InitOptions::default()` and a cache directory; the exact downloaded artifact/default model resolution is uninspected. Mutable endpoint can resolve to another model: no per-call endpoint switching appears here; initialization/download resolution and cache replacement remain uninspected. Input/output embeddings change with content; that is not evidence of parameter training or internal truth acceptance.

> let options = fastembed::InitOptions::default()
>             .with_cache_dir(cache_dir.to_path_buf())
>             .with_show_download_progress(true);
> --- `src/memory/embedding.rs`

### Operative objects

#### EPI-OBJ-memory-content
Label: Memory content statements

Source-native identity: `Memory.content`, natural-language text retained in per-agent SQLite, with text/embedding indexing in LanceDB. Distinct from the live-history container [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history) and procedures [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set). It can encode factual assertions, reported decisions or preferences; no instance was supplied. SRC-1 `src/tools/memory_save.rs` shows caller-content construction and human-anchor append. Re-encoding it numerically does not make the natural-language content itself parametric.

> let mut memory = Memory::new(&args.content, memory_type);
> --- `src/tools/memory_save.rs`

#### EPI-OBJ-memory-metadata
Label: Memory selectors and associations

Source-native identity: memory type, importance, forgotten state, source/channel fields and `Association` relation/weight. Symbolic selectors and graph labels reside in SQLite; importance is a scalar consumed by fixed scoring rules, not distributed-parametric state. The labels may assert `updates` or `contradicts`, but program consumers use fixed rules rather than prove those relations. Distinct from [EPI-OBJ-memory-content](#epi-obj-memory-content); neither is the live-history object [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history). SRC-1 `src/tools/memory_save.rs`, `src/memory/search.rs`. The minimum passages are in the save and selection records below.

#### EPI-OBJ-completion-state
Label: MemoryPersistenceContractState saved IDs

Source-native identity: `MemoryPersistenceContractState`, in-process mutex-protected saved-ID set and terminal outcome. Symbolic IDs, enum variants and result JSON receive exact code interpretation. Optional event summaries remain natural-language content, not proof obligations checked by the ID contract. Distinct from durable [EPI-OBJ-memory-content](#epi-obj-memory-content); no counterpart in supplied runtime records, whose [RT-RTE-context-control](runtime.md#rt-rte-context-control) concerns history pressure rather than terminal consistency. SRC-1 `src/tools/memory_persistence_complete.rs`.

> pub struct MemoryPersistenceContractState {
>     saved_memory_ids: Mutex<BTreeSet<String>>,
>     terminal_outcome: Mutex<Option<MemoryPersistenceTerminalOutcome>>,
> }
> --- `src/tools/memory_persistence_complete.rs`

#### EPI-OBJ-wiki-content
Label: WikiPage current and historical content

Source-native identity: `WikiPage.content` and `WikiPageVersion.content`, natural-language Markdown in instance SQLite; version, slug, page type and authorship are symbolic metadata. Distinct from per-agent memory statements and [RT-OBJ-skill-set](runtime.md#rt-obj-skill-set). No counterpart in supplied runtime object records; wiki grants in [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work) are execution affordances, not this content store. SRC-1 `src/wiki/store.rs`; mutation passages below supply evidence.

#### EPI-OBJ-fixture-sample
Label: Behavioral fixture sample

Source-native identity: fixture `Sample` fields for first tool, arguments, reply and timeout. In-process symbolic capture and program predicates; text fields represent observed event bytes if run. Not a retained production-memory artifact and not [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history). Source declarations are not observed samples. SRC-1 `tests/behavioral_fixtures.rs`.

> sample.first_tool = Some(tool_name);
>                         sample.tool_args = Some(args);
>                         break;
> --- `tests/behavioral_fixtures.rs`

### Routes

#### EPI-RTE-memory-extraction
Label: Conversation and ingest extraction

Endpoints/progression: conversation persistence trigger or per-file chunk → model prompt with memory tools → model-selected recall/save/association/event requests. Owner: runtime sets context/grants and model selects semantic content. Distinct from the skill-mutation referent of [RT-RTE-skill-change](runtime.md#rt-rte-skill-change); they share the persistence branch but produce different objects. [RT-RTE-context-control](runtime.md#rt-rte-context-control) explicitly separates summarization from extraction. SRC-1 `src/agent/ingestion.rs`, `prompts/en/ingestion.md.j2`, `prompts/en/memory_persistence.md.j2`, `src/tools.rs`; implementation and doctrine/design.

The model proposes and decides what is worth saving; code may refuse tool arguments. No per-content human approval or fixed answer oracle is enforced in the inspected automatic path. Mode: open extraction, not controlled curriculum. Guidance calls for selective durable information, recall before save, and treating conflicting old material as stale. The instruction is not evidence that verification occurred. Proposed changes persist as memory/event text; completion failure need not undo prior saves. Recovery is retry/progress tracking plus tool-local compensation, not demonstrated semantic rollback.

- Immediate return: tool results followed by terminal branch/chunk outcome.
- Later read-back: saved text can reach later recall, rendering and participant context; optional events feed working memory.
- Delegated visibility: ingestion creates a fresh agent/history per chunk; persistence branches receive channel context and profile grants, not an assumed full external source corpus.
- Selection predicate: configured persistence triggers or queued files/chunks, then model relevance/durability selection.
- Invalidation or expiry: later deletion, consolidation and maintenance can alter memories; source truth expiry is not automatically adjudicated by extraction.
- Activation or effect: memory mutation is wired through tools; actual model-selected content and later content-dependent behavior unobserved.
- Evidence limits: no candidate transcript/input-output comparison; neither faithful reshaping nor ampliative invention follows from the route name.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> You are a memory ingestion process. You are given a chunk of text from a file that a user has placed in the ingestion directory. Your job is to extract useful information and persist it as structured memories.
> --- `prompts/en/ingestion.md.j2`

> 2. Do not save the raw text verbatim. Distill information into clean, structured memory content.
> --- `prompts/en/ingestion.md.j2`

> 8. Verify stale memory before relying on it. If a recalled memory conflicts with
> the newer conversation context, treat the older item as stale, avoid propagating
> it as truth, and capture the latest truth via `updates` or `contradicts`.
> --- `prompts/en/memory_persistence.md.j2`

> /// Creates a fresh LLM agent with memory tools for each chunk. No history
> /// carries over between chunks — each chunk is independent.
> --- `src/agent/ingestion.rs`

#### EPI-RTE-memory-save
Label: Memory save validation and persistence

Endpoints/progression: model/caller arguments → Rust structural and target checks → SQLite content/associations → embedding storage → recorded save ID → advisory consolidation. Owner: `MemorySaveTool`. The model proposes semantic text/type/relations; program decides tool-local admission; there is no truth oracle or human per-content approval here. Guidance: type/tool schema and persistence prompt, with optional caller source/channel fields. Recovery: embedding failure invokes compensation; association failures can be skipped/logged and FTS failures warn. Human anchors append observations rather than verify them. Distinct from [RT-RTE-skill-change](runtime.md#rt-rte-skill-change), which admits procedure files. SRC-1 `src/tools/memory_save.rs`, implementation.

- Immediate return: saved memory metadata/advisory or error; known missing association target is skipped.
- Later read-back: SQLite text and indexed content become eligible for later recall/render; recorded successful IDs serve current-run completion checks.
- Delegated visibility: tool callers receive result, not a semantic-proof artifact; eligible branches have save/recall/delete/consolidate grants.
- Selection predicate: valid content/type/importance and human key where required, target existence for graph edges, successful embedding path.
- Invalidation or expiry: explicit forget, consolidation or maintenance; failed embeddings invoke compensating delete or anchor restoration.
- Activation or effect: save and append are implemented; downstream use and embedding recovery success unobserved.
- Evidence limits: no content truth check in inspected body; not a universal guarantee over every API/storage mutation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if let Some(importance) = args.importance
>             && !(0.0..=1.0).contains(&importance)
> --- `src/tools/memory_save.rs`

> // Verify the target memory exists before creating a graph edge
>             // to prevent dangling associations from LLM hallucinated IDs.
> --- `src/tools/memory_save.rs`

> merged.content = format!("{}\n{}", existing.content.trim_end(), args.content);
> --- `src/tools/memory_save.rs`

> self.compensate_embedding_failure(&memory, replaced_anchor.as_ref())
>                     .await;
>                 return Err(MemorySaveError(format!(
>                     "Failed to generate embedding: {embed_err}"
>                 )));
> --- `src/tools/memory_save.rs`

#### EPI-RTE-completion-contract
Label: Persistence completion consistency

Endpoints/progression: tool-provided terminal outcome/ID list → set equality or no-save/reason checks → success JSON → hook terminal state/termination → ingestion requires signal. Owner: tool state, hook and ingestion caller. No counterpart in supplied runtime route records: [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work) is a container-level delegation account, not this ID evaluator. Model proposes saved/no_memories; program can veto inconsistent reports. Mode is current-run protocol, with recorded save IDs as reference evidence, not expected true memory content. Guidance: terminal tool schema. Rejected completion can be retried; already saved memories are not rolled back by this contract. SRC-1 `src/tools/memory_persistence_complete.rs`, `src/hooks/spacebot.rs`, `src/agent/ingestion.rs`, implementation.

- Immediate return: success outcome or validation error; successful terminal tool causes hook termination without trailing model call.
- Later read-back: inapplicable — this evaluator's state is current-run bookkeeping, not a retained lesson; separately persisted memory/events have their own consumers.
- Delegated visibility: hook shares contract state with persistence branch/ingestion tool server; child sees tool success/error.
- Selection predicate: saved requires nonempty exact recorded set without duplicates; no_memories requires no IDs or prior saves and a short reason.
- Invalidation or expiry: state scoped to the branch/chunk; late content truth changes are not reevaluated by this set comparison.
- Activation or effect: bare-text completion is rejected without terminal state; successful parsed terminal result stops the loop and lets ingestion recognize completion.
- Evidence limits: successful-ID consistency does not establish complete extraction, true statements, source support or ongoing index freshness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if provided_set != recorded_set {
>                     return Err(MemoryPersistenceCompleteError(format!(
>                         "saved_memory_ids mismatch: expected {:?}, got {:?}",
>                         recorded_ids, provided_ids
>                     )));
>                 }
> --- `src/tools/memory_persistence_complete.rs`

> contract_state.set_terminal_outcome(outcome);
>             return HookAction::Terminate {
>                 reason: Self::MEMORY_PERSISTENCE_COMPLETE_REASON.into(),
>             };
> --- `src/hooks/spacebot.rs`

> if !contract_state.has_terminal_outcome() {
>         return Err(anyhow::anyhow!(
>             "ingestion chunk {chunk_number}/{total_chunks} for {filename} completed without memory_persistence_complete signal"
>         ));
>     }
> --- `src/agent/ingestion.rs`

#### EPI-RTE-batch-consolidation
Label: Advisory consolidation and atomic batch

Endpoints/progression: completed save → optional near-duplicate/cap advice → model's merge batch → partition/type/existence/nonempty checks → SQLite transaction → survivor text/provenance and forgotten absorbed rows → post-commit embeddings. Owner: model chooses semantic merge; code applies/refuses batch. No fixed truth oracle or required human approval. Open maintenance request. Guidance asks combined deduplicated statement superseding outdated wording, but type/ID checks cannot validate that instruction. Recovery: SQLite failure rolls back batch; embedding errors after commit warn only. Compared with [RT-RTE-context-control](runtime.md#rt-rte-context-control), this changes durable memories, not history summary. SRC-1 `src/tools/memory_save.rs`, `src/memory/consolidation.rs`, `prompts/en/memory_persistence.md.j2`; implementation and doctrine/design.

- Immediate return: save advice or batch report/error.
- Later read-back: survivor replacement reaches ordinary recall/render; forgotten absorbed rows and Updates provenance can remain inspectable in SQLite.
- Delegated visibility: branch receives advisory and supplies merged_content; this is not automatic acceptance by a separate semantic evaluator.
- Selection predicate: optional runtime-configured similarity/cap advice; model chooses ops; batch requires known partition and matching memory types and nonempty merged text.
- Invalidation or expiry: absorbed memories leave ordinary retrieval; batch failure rolls back SQLite changes, while post-commit embedding upkeep is warn-only.
- Activation or effect: transaction mutates content/availability and provenance; no observed consolidation or verified semantic preservation.
- Evidence limits: advice cannot enforce merging before write; no proposition-level truth or contradiction decision is recorded by structural validation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Write-time consolidation check. Advisory: the save has already
>         // landed; the advice tells the branch about near-duplicates and
>         // per-partition over-cap debt so it can run one atomic batch.
> --- `src/tools/memory_save.rs`

> updated_survivor.content = op.merged_content.clone();
>         updated_survivor.importance = survivor.importance.max(absorbed.importance);
> --- `src/memory/consolidation.rs`

> // The merges are durable. Embedding upkeep is warn-only from here: a
>     // stale or orphaned embedding row is invisible to recall (joins resolve
>     // through SQLite) and self-heals on the next content change. The
>     // absorbed rows stay in SQLite as forgotten memories — each one is the
>     // provenance target of its survivor's Updates edge — only their
>     // embedding rows are removed.
> --- `src/memory/consolidation.rs`

The quoted comment describes intended recovery/invisibility; this inspection does not independently prove every join or self-heal path.

#### EPI-RTE-memory-maintenance
Label: Decay pruning and similarity merge

Endpoints/progression: maintenance invocation → decay by update/access age → low-importance/old/non-identity deletion → similarity candidates → importance/ID survivor → deterministic content merge → atomic store merge → embedding updates. Owner: Rust maintenance policy and numerical similarity lookup, no semantic judge. Distinct from history [RT-RTE-context-control](runtime.md#rt-rte-context-control) and skill reflection [RT-RTE-skill-change](runtime.md#rt-rte-skill-change). SRC-1 `src/memory/maintenance.rs`; implementation. Background wiring is supplied by boundary, not execution evidence.

Admission/selection: program chooses survivor by importance then ID, can stop on limits/cancellation/errors; no human per-content approval or expected-answer oracle. Guidance: configured age, decay, prune and similarity thresholds. Persists changed importance, merged text and deletion/forgotten outcomes. Store mutation can precede embedding errors; no semantic rollback/equivalence experiment inspected.

Concrete implementation deduction, not execution: `merged_memory_content("Do not deploy.".to_string(), "deploy.")` returns `Do not deploy.` because the winner contains the loser substring. The imperative/assertion contrast is lost as a distinct input, despite literal byte containment. With arbitrary truth-apt text, `merged_memory_content("It is not true that P.".to_string(), "P.")` likewise returns the winner alone: character substring containment is not proposition equivalence or reconciliation. For two unrelated short strings it appends blank-line-separated text; over the byte cap it clips at a UTF-8 boundary. Therefore this route is not generally warranted non-ampliative semantic deduplication. No actual deployed pair is claimed.

- Immediate return: maintenance report or cancellation/error.
- Later read-back: changed importance/content and surviving rows alter later recall/render; deleted rows are unavailable through ordinary loads.
- Delegated visibility: inapplicable — this inspected function is programmatic, not a delegated model loop.
- Selection predicate: non-identity decay, age/importance pruning, bounded similarity candidate scan; higher importance then lexical ID wins a pair.
- Invalidation or expiry: deletion/forgetting and replacement; cancellation checks bound work, but no demonstrated atomic rollback of the entire pass.
- Activation or effect: policy directly changes later availability and salience, independent of truth judgments.
- Evidence limits: semantic similarity does not establish equivalence; no run, duplicate quality result or benefit comparison supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> report.pruned = prune_memories(memory_store, config, &mut maintenance_cancel_rx).await?;
>         report.merged = merge_similar_memories(
> --- `src/memory/maintenance.rs`

> let first_wins = first.importance > second.importance
>         || (first.importance == second.importance && first.id < second.id);
> --- `src/memory/maintenance.rs`

> if winner_trimmed.contains(loser_trimmed) {
>         return winner_trimmed.to_string();
>     }
> --- `src/memory/maintenance.rs`

> let boundary = merged.floor_char_boundary(MAX_MERGED_MEMORY_CONTENT_BYTES);
>     merged[..boundary].to_string()
> --- `src/memory/maintenance.rs`

#### EPI-RTE-memory-withdrawal
Label: Memory soft withdrawal

Endpoints/progression: caller selects ID/reason → load/existence/already-forgotten checks → store forget → ordinary search/render filters. Owner: caller/model selects withdrawal; program applies flag. Distinct from [RT-RTE-context-control](runtime.md#rt-rte-context-control), which removes live history, not this durable candidate. SRC-1 `src/tools/memory_delete.rs`, `src/memory/search.rs`, `src/memory/store.rs`; implementation. No expected truth oracle, semantic falsity criterion or required human confirmation; open request. Optional reason is logged, not judged as a refutation. No restore step was traced for this tool.

- Immediate return: forgotten flag/message or lookup/error result.
- Later read-back: subsequent ordinary search/render excludes forgotten items; retained database rows can remain provenance targets.
- Delegated visibility: tool caller gets status; already copied content and private contexts are not globally recalled.
- Selection predicate: supplied ID exists and is not already forgotten.
- Invalidation or expiry: flag excludes that row until changed by another path; no automatic downstream derivative invalidation traced.
- Activation or effect: enforcing ordinary retrieval exclusion, not necessarily removal from every API/history surface.
- Evidence limits: no evidence that this selection was a true correction rather than housekeeping or error.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let was_forgotten = store
>             .forget(&args.memory_id)
>             .await
>             .map_err(|e| MemoryDeleteError(format!("Failed to forget memory: {e}")))?;
> --- `src/tools/memory_delete.rs`

> "UPDATE memories SET forgotten = 1, updated_at = ? WHERE id = ? AND forgotten = 0",
> --- `src/memory/store.rs`

#### EPI-RTE-memory-selection
Label: Graph relation ranking

Endpoints/progression: graph expansion start → load edges and related memory → forgotten filter → type/weight/importance score → results; RelatedTo/PartOf continue traversal. Owner: code. Distinct from [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn), which consumes the resulting context rather than defines this ranker. SRC-1 `src/memory/search.rs`, implementation. This is a material part of retrieval, not an inventory of all hybrid selection. No truth oracle or acceptance decision is implemented by the inspected multiplier.

- Immediate return: scored related memories added to results.
- Later read-back: stored relationships and importance affect later retrieval calls; this routine does not itself write a new lesson.
- Delegated visibility: eligible memory-recall callers can receive selected items; full private context is outside this ranker.
- Selection predicate: visited/depth controls, available non-forgotten related rows, edge type/weight and importance.
- Invalidation or expiry: forgotten filter excludes rows; later relationship/content changes affect future calls, not prior deliveries.
- Activation or effect: ranking force in retrieval; actual model reliance unobserved.
- Evidence limits: contradictions receive nonzero score, not truth adjudication; full hybrid fusion remains unassessed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let type_multiplier = match assoc.relation_type {
>                         RelationType::Updates => 1.5,
>                         RelationType::CausedBy | RelationType::ResultOf => 1.3,
>                         RelationType::RelatedTo => 1.0,
>                         RelationType::Contradicts => 0.5,
>                         RelationType::PartOf => 0.8,
>                     };
> --- `src/memory/search.rs`

> let score = memory.importance as f64 * assoc.weight as f64 * type_multiplier;
> --- `src/memory/search.rs`

#### EPI-RTE-memory-render
Label: First-line memory context render

Endpoints/progression: store/task query → fixed type sections/caps → sorted entries → first nonempty trimmed content line/date → word-budgeted bullets and counts → channel preamble. Owner: code; no model synthesis or truth evaluator. Distinct from live-history reduction [RT-RTE-context-control](runtime.md#rt-rte-context-control); both affect model-visible context, but this renderer selects durable memory statements. SRC-1 `src/memory/render.rs`, implementation; channel consumption supplied by boundary and [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn).

Concrete deduction from inspected code, without execution: one Fact content `Deployment is safe.\nOnly if the migration has completed.` with sufficient budget becomes bullet `- Deployment is safe. (YYYY-MM-DD)` using that row's update date. `first_line` drops the second-line condition; no retained source field is printed in this bullet. Conversely a single-line qualified fact keeps its qualification. The scope is arbitrary memory text, not a claim that the extraction prompt produced the adversarial example. This counterexample defeats a general semantic-preservation guarantee, not the implementation's deterministic formatting claim. Non-ampliative formatting is established for restricted inputs whose first line is self-contained; actual deployed preservation is indeterminate without content.

- Immediate return: Memory Store text and Active Tasks section.
- Later read-back: later model invocations receive selected retained memory first lines, including shown-of-total counts; tasks always render separately from memory word budget.
- Delegated visibility: channel receives the rendered view; branch recall can access deeper material through another path, not an automatically dereferenced pointer.
- Selection predicate: fixed selected types, scaled per-type caps, importance/update/ID sorting, first nonempty line and remaining word budget; human anchors excluded from global block.
- Invalidation or expiry: store changes affect future renders; omitted items can remain in store; no truth-expiry check.
- Activation or effect: bytes supplied to future channel context; model obedience and content-dependent decisions unobserved.
- Evidence limits: limited view is not full content/provenance, and deterministic current state can still be false or omit necessary conditions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let line = format!(
>                 "- {} ({})\n",
>                 first_line(&memory.content),
>                 memory.updated_at.format("%Y-%m-%d")
>             );
> --- `src/memory/render.rs`

> fn first_line(content: &str) -> &str {
>     content
>         .lines()
>         .map(str::trim)
>         .find(|line| !line.is_empty())
>         .unwrap_or("")
> }
> --- `src/memory/render.rs`

#### EPI-RTE-wiki-mutation
Label: Wiki versioned mutation and read-back

Endpoints/progression: granted wiki tool or alternate administrative caller → typed create or old/new-string edit → store current content/version/history → requested page/version read. Owner: caller selects content, code parses type and resolves matching/replacement. Distinct from [RT-RTE-skill-change](runtime.md#rt-rte-skill-change): instance-wide article storage is not SkillSet instruction admission. SRC-1 `src/tools/wiki_create.rs`, `src/tools/wiki_edit.rs`, `src/tools/wiki_read.rs`, `src/wiki/store.rs`; implementation. `skills/builtin/wiki-writing/SKILL.md` provides doctrine/design, requesting verification against authoritative sources before correcting facts. No proof/evidence object is required by inspected handlers. Model or caller proposes and decides content; software vetoes invalid type/match/store failure, not unsupported factual claims; no per-content human approval is enforced here. Mode: open writing/editing. No expected-answer oracle. History/restore operations exist, but all restore/archive bodies and API paths are not audited as a universal rollback guarantee.

- Immediate return: slug/version or error; reads return content and linked-page titles/broken markers.
- Later read-back: later requested current/historical version reads expose stored article text; links resolve titles only, not linked article evidence.
- Delegated visibility: granted branches/workers can receive wiki tool outputs; source verification is a model instruction, not a separate service automatically run.
- Selection predicate: title/type for create, slug and tolerant old-string match for edit, optional version for read.
- Invalidation or expiry: new version replaces current content; archive/restore surfaces exist; already delivered text is not automatically withdrawn.
- Activation or effect: persistent text/version changes and later reads wired; article correctness and reader reliance unobserved.
- Evidence limits: tolerant replacement locates text, not truth; versioning alone does not establish evidence-consuming acceptance or lifecycle integration.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let page_type = WikiPageType::parse(&args.page_type)
>             .ok_or_else(|| WikiCreateError(format!("invalid page_type: {}", args.page_type)))?;
> --- `src/tools/wiki_create.rs`

> let new_content = tolerant_replace(
>             &page.content,
>             &input.old_string,
>             &input.new_string,
>             input.replace_all,
>         )
>         .map_err(|e| WikiError::EditFailed(e.to_string()))?;
> --- `src/wiki/store.rs`

> // Resolve inline wiki: links (titles only, no content fetch)
> --- `src/tools/wiki_read.rs`

#### EPI-RTE-result-filtering
Label: Tool-result leak and display filtering

Endpoints/progression: tool result → hook leak scan/guard → channel termination on detected leak, or worker/branch event scrub and byte cap → event subscribers. Owner: hook policy. Distinct from [RT-RTE-delegated-work](runtime.md#rt-rte-delegated-work), a broader execution route: this is the cross-process-result consumer transformation. It overlaps live-history content [RT-OBJ-channel-history](runtime.md#rt-obj-channel-history) but also broadcasts to non-history consumers, so it is not a part of exactly that container. SRC-1 `src/hooks/spacebot.rs`, implementation. Safety predicate, not truth acceptance. No human/content oracle is implied; scan internals were not audited.

- Immediate return: HookAction continuation/termination plus tool-completed event.
- Later read-back: uninspected — transcript/event persistence and later reflection may consume transformed events, but every subscription/persistence path was not traced here.
- Delegated visibility: branch/worker events are scrubbed and capped for subscribers including SSE; this does not imply identical rewriting of each model's private tool message.
- Selection predicate: process type, leak scan result, reply special case and output cap.
- Invalidation or expiry: current turn may terminate; scrubbed/omitted bytes do not automatically become recoverable evidence in event consumers.
- Activation or effect: code enforces detected-leak termination and event payload transformation; no runtime incident observed.
- Evidence limits: no complete detector audit or claim of comprehensive leak prevention; formatting/omission can alter downstream evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let scrubbed = crate::secrets::scrub::scrub_leaks(result);
>             let capped =
>                 crate::tools::truncate_output(&scrubbed, crate::tools::MAX_TOOL_OUTPUT_BYTES);
>             self.emit_tool_completed_event_from_capped(tool_name, call_id, capped)
>                 .await;
> --- `src/hooks/spacebot.rs`

> reason: "Reply contained a secret. Channel turn terminated.".into(),
> --- `src/hooks/spacebot.rs`

#### EPI-RTE-behavioral-fixtures
Label: First-action behavioral fixture evaluation

Endpoints/progression: canned conversation/pinned config template → real channel/provider call if explicitly run → first observed ToolStarted or response/timeout → per-fixture predicate → pass count → threshold assertion. Owner: developer-authored harness/predicates; model supplies responses, not its own acceptance criterion. Distinct from production [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn): this is an external-to-that-turn test consumer, shipped within SRC-1. Source is `tests/behavioral_fixtures.rs`, implementation and test-design doctrine. Mode: bounded fixture suite; reference outcome is each fixture's predicate over tool name/arguments or reply. Objective is current prompt routing contract, not factual answer truth or improved skill capacity. Programmer can change predicate; test assertion vetoes a test pass, not all deployment/admission paths. No successor installation/rollback consumer traced.

The fixture begins capture by subscribing after sending the inbound message. Therefore observed first event means first event captured by this subscriber, not proof of complete event delivery under every scheduling interleaving. The loop stops on first captured ToolStarted or text response, not on completed effects. Five samples use shared bootstrapped deps with per-sample channel creation; no independent treatment/control comparison is encoded by the four-of-five threshold alone.

- Immediate return: sample report and successful assertion or failed test.
- Later read-back: inapplicable — source test definitions do not establish retained production knowledge or an automatic trace-fed instruction change.
- Delegated visibility: first event can identify delegation, but worker completion/outcome is not the acceptance target.
- Selection predicate: explicitly invoked ignored live tests with API key; configured model override/default, fixture conversation/settings and predicate; five samples, threshold four.
- Invalidation or expiry: fixture result applies to those samples/configuration; changed model/prompt/conditions require renewed evidence.
- Activation or effect: threshold assertion consumes sample counts and can fail test process; no executed result or release veto shown here.
- Evidence limits: first action is not final correctness, reliability bound, replay guarantee or causal component effect; model version/config template is not an immutable deployed model snapshot.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const SAMPLES: usize = 5;
> const THRESHOLD: usize = 4;
> --- `tests/behavioral_fixtures.rs`

> assert!(
>         passes >= THRESHOLD,
>         "{name}: {passes}/{SAMPLES} passed, below threshold {THRESHOLD}/{SAMPLES}"
>     );
> --- `tests/behavioral_fixtures.rs`

### Claims

#### EPI-CLM-memory-context
Label: Deterministic current memory context

Claimed operation: conversations open on deterministic top-per-type memory context without LLM synthesis or staleness. SRC-1 `README.md`, doctrine/design. Distinct from [RT-CLM-required-skills](runtime.md#rt-clm-required-skills), which promises required procedure bodies, not memory view content. Freshness must be scoped to queried store state; first-line/cap selection is not a truth guarantee.

> - **Memory-first knowledge context** — every conversation opens with a deterministic render of the memory store: top memories per type with shown-of-total counts, straight from SQLite. No LLM synthesis pass, no staleness, no idle token spend
> --- `README.md`

#### EPI-CLM-write-consolidation
Label: Write-time duplicate consolidation

Claimed operation: duplicate merge on save rather than later background cleanup. SRC-1 `README.md`, doctrine/design. No counterpart in supplied runtime claims; [RT-RTE-skill-change](runtime.md#rt-rte-skill-change) concerns procedure changes rather than duplicate memory storage. The inspected save advice and independently implemented background merge qualify the categorical wording.

> - **Write-time consolidation** — duplicates get merged when memories are saved, not cleaned up later by a background loop
> --- `README.md`

#### EPI-CLM-better-use
Label: Improvement with accumulated use

Claimed operation: work becomes skills and sessions build on prior sessions without user action, with improvement from use. SRC-1 `README.md`, doctrine/design. Closest supplied record [RT-RTE-skill-change](runtime.md#rt-rte-skill-change) assesses the self-change path; this distinct claim record records the broader public benefit assertion rather than redeclaring the route.

> **And it gets better the more you use it.** Work becomes skills, conversations become memory, and goals pull it forward between them. Every session builds on the last, without any user action.
> --- `README.md`

#### EPI-CLM-wiki-verification
Label: Verified wiki factual corrections

Claimed operation: factual corrections should be checked against authoritative sources and their basis included in edit summary. SRC-1 `skills/builtin/wiki-writing/SKILL.md`, doctrine/design; not a claim that the tool enforces a verification oracle. Distinct from [RT-CLM-required-skills](runtime.md#rt-clm-required-skills): particular procedure content, not delivery guarantee.

> When correcting factual content, verify the correction against authoritative sources before applying it. Include the basis for the correction in the edit summary.
> --- `skills/builtin/wiki-writing/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### EPI-BAP-memory-context
Label: Retained memory to later model context

Consumer: later channel and eligible recall-calling branch/worker models. Channel: selected global first-line render, requested recall, separately scoped participant/temporal paths whose complete transformations remain unassessed. Force: code enforces selection/exclusion/ranking; delivered text gives natural-language advisory context, not enforced truth or obedience. Horizon: later invocations and sessions while rows remain available; copied material can outlive source withdrawal. Distinct from [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction), which conveys procedures, and [RT-BAP-runtime-config](runtime.md#rt-bap-runtime-config), which gives symbolic machinery controls. SRC-1 `src/memory/render.rs`, `src/memory/search.rs`, `src/tools.rs`; minimum passages and channel consumption are in [EPI-RTE-memory-render](#epi-rte-memory-render), [EPI-RTE-memory-selection](#epi-rte-memory-selection) and supplied [RT-RTE-channel-turn](runtime.md#rt-rte-channel-turn). Actual semantic reliance unobserved.

#### EPI-BAP-wiki-readers
Label: Wiki version to later readers

Consumer: models calling wiki_read and human/API/CLI readers. Channel: current or requested historical content plus metadata and resolved link titles, not automatic linked-content verification. Force: informational/advisory natural-language content; symbolic version/slug selects bytes, not epistemic endorsement. Horizon: later reads across sessions until edits/archive/other mutation changes discoverability; historical access can remain. Distinct from [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction), because this is article retrieval rather than required instruction injection. SRC-1 `src/tools/wiki_read.rs`, `src/wiki/store.rs`; load-bearing read/mutation passages in [EPI-RTE-wiki-mutation](#epi-rte-wiki-mutation). Reader trust/compliance and every archive path unobserved.
