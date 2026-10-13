---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Atomic's candidate generation, citation checks, publication authority and retrieval evaluation at its frozen source revision."
run-id: AAS-2026-10-12-atomic-f98683232831-01
reviewed-boundary: "983bea6baf449d060514c94b3b15b5f85f77ba9b"
---

# Atomic epistemic report

## Source-and-claim boundary

The question is how Atomic acquires or generates truth-apt content, checks it, grants reliance and makes it consequential. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. External provider weights and host internals remain excluded. Their absence prevents assessments of model-internal learning, provider reliability and external-agent behavior, not inspection of Atomic's admission routes.

The report directly inspects citation resolution and generated-content delivery as potential counterexamples to a simple claim that inline citations guarantee grounding. The checks establish identities and numbering, not support for each proposition. Wiki human review is available but bypassable by immediate acceptance or direct generation. Report prose can be automatically retained after a nonempty check. These distinctions are supported by [EPI-RTE-citation-resolution](#epi-rte-citation-resolution), [EPI-RTE-generated-delivery](#epi-rte-generated-delivery), [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission) and [RT-RTE-report-finding](runtime.md#rt-rte-report-finding).

Consequential knowledge-product claims are see [EPI-CLM-cited-products](#epi-clm-cited-products). The explicit-mutation constraint is see [RT-CLM-explicit-mutation](runtime.md#rt-clm-explicit-mutation). No claim of universally verified truth is attributed to the target.

| Entry point or operation | SRC-1 path | Coverage and prevented conclusion |
| --- | --- | --- |
| Chat, tool dispatch, reader and mutation grants | `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-core/src/agent_runtime/run.rs` | Supplied [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-atom-mutation](runtime.md#rt-rte-atom-mutation); direct marker cleanup and generated reader inspection in [EPI-RTE-generated-delivery](#epi-rte-generated-delivery). |
| Shared citation ledger and report final pass | `crates/atomic-core/src/agent_runtime/citations.rs`, `crates/atomic-core/src/reports/agentic.rs` | Direct implementation reads in [EPI-RTE-citation-resolution](#epi-rte-citation-resolution). |
| Wiki synthesis, proposal acceptance, dismissal and direct publication | `crates/atomic-core/src/lib.rs`, `crates/atomic-server/src/routes/wiki.rs`, `crates/atomic-core/src/wiki/mod.rs` | Supplied [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission); direct section-operation citation mapping inspection in [EPI-RTE-wiki-citations](#epi-rte-wiki-citations). Section-operation application and archive restoration internals remain unassessed. |
| Report manual/scheduled runs, provenance and finding write | `crates/atomic-core/src/reports/runner.rs` | Supplied [RT-RTE-report-finding](runtime.md#rt-rte-report-finding). Storage helper internals and deletion propagation unassessed; no universal atomicity or withdrawal guarantee. |
| MCP registered operations | `crates/atomic-server/src/mcp/server.rs` | Direct search of registered tool declarations and reader/write names corroborates supplied routes; includes generated findings, wiki readers, URL ingestion and search aliases. Individual MCP excerpt/alias transformations unassessed; prevents complete cross-channel lineage assessment. |
| HTTP exposed operations | `crates/atomic-server/src/routes/mod.rs` | Direct dispatch search includes proposal accept/dismiss, wiki deletion/versions, report definitions/findings, URL ingestion and compact-tags. Handler internals beyond supplied routes unassessed. No system-complete negative about checking or withdrawal. |
| Core capture, direct SQLite import, saved chat answers, browser/mobile and plugins | `crates/atomic-core/src/lib.rs`, `scripts/import/shared/index.js`, `src/components/chat/saveAnswerAsAtom.ts` | Supplied [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) and boundary coverage; ingestion/extraction and client confirmation paths not directly traced here. Source fidelity and all human admission variants unresolved. |
| Standalone/cloud maintenance, tagging, graph and settings | `crates/atomic-server/src/main.rs`, `crates/atomic-cloud/src/dispatcher.rs`, `crates/atomic-core/src/extraction.rs`, `crates/atomic-core/src/graph_maintenance.rs`, `crates/atomic-core/src/compaction.rs` | Supplied [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change); direct check-keyword search of extraction and compaction, not a full semantic trace. Tag compaction, graph mathematics and reset propagation remain unassessed. |
| CLI and utility dispatch | `package.json`, `Cargo.toml`, `scripts/reset-tags.js`, `scripts/reset-chunks.js` | Direct manifest search confirms imports/resets/benchmark commands; supplied boundary names direct database changes. Utility bodies not inspected here; prevents universal admission/freshness guarantees. No omitted route is treated as absent. |
| Retrieval evaluator | `crates/atomic-bench/src/suites/memory_longitudinal.rs` | Direct scoring implementation read in [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring); broader suite keyword search is not complete evaluator inspection. Other benchmark suites and fixture truth remain unassessed. |
| Public knowledge-product claims | `README.md` | Direct feature passage in [EPI-CLM-cited-products](#epi-clm-cited-products). Other manuals and historical claims unassessed; no exhaustive public-claim inventory asserted. |

No live provider response, persisted candidate with route provenance, human decision trace or benchmark result was supplied. Consequently generation semantics, exercised checking, accepted claims, actual later reliance and causal benefit remain unobserved. Available but uninspected paths above prevent a system-complete negative about evidence-consuming acceptance, theory criticism or learning.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-atom-content](#epi-obj-atom-content) | Note propositions, if present | Captured knowledge | see record | Arbitrary markdown need not be truth-apt; source warrant unknown. |
| [EPI-OBJ-generated-prose](#epi-obj-generated-prose) | Answers, wiki assertions and report findings, if present | Synthesized/cited products | see record | No individuated generated candidate or verified semantic transformation supplied. |
| [EPI-OBJ-citation-ledger](#epi-obj-citation-ledger) | Source identities/excerpts and marker associations | Citable evidence | see record | Association does not establish entailment or external source truth. |
| [RT-CMP-tagging-model](runtime.md#rt-cmp-tagging-model) | Tag assignments may express classification propositions | Utility model | see record | Specific classification target, truth and evaluator not individuated here. |
| [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) | Not determinable from a vector alone | Numerical retrieval representation | see record | Semantic similarity is not proposition validity. |
| [RT-CMP-agentic-model](runtime.md#rt-cmp-agentic-model) | Internal content not determinable | Candidate generation and tool choice | see record | Weights/version and provider parameter updates inaccessible; inference requests do not establish weight learning. |

## Authority-route ledger

Fields owned by shared records are given by `see`; the architectural classification and bounded epistemic interpretation below are this report's overlay. Container routes are split by function rather than interpreted as single checks.

Route ID: [RT-RTE-capture-write](runtime.md#rt-rte-capture-write)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-atom-content](#epi-obj-atom-content).
Content/update relation: truth-apt transformation: acquisition/import, when submitted content contains propositions; source warrant unknown.
Transition or check target: admission of request content; see record.
Evaluator/condition and domain: software storage/optional duplicate-source handling, not truth judgment; see record.
Activation and timing: see record.
Possible or observed result: see record; no observed run.
Implemented force: see record.
Epistemic authority and scope: no independent truth license from capture.
Operational authority: inserted content becomes readable before enrichment completion; see record.
Behavioral-authority path: storage readers and later selected search/model context, permissive availability until mutation/deletion; see record.
Evidence source ID and local anchor: SRC-1 `crates/atomic-core/src/lib.rs`; see record.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: none.
Gap/limit: import fidelity and provenance beyond the supplied capture path unassessed.

Route ID: [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission), [RT-RTE-report-finding](runtime.md#rt-rte-report-finding)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-prose](#epi-obj-generated-prose).
Content/update relation: truth-apt transformation: indeterminate. Reshaping, entailed derivation and ampliative conjecture remain possible; no generated proposition and its complete premises supplied.
Transition or check target: model requests to answer/synthesize/write; separate progressions are see records.
Evaluator/condition and domain: provider generation is not an independent truth evaluator; see records.
Activation and timing: see records.
Possible or observed result: proposed text; see records; operation unobserved.
Implemented force: generation request, not reliable compliance.
Epistemic authority and scope: candidate production only; no accepted ampliative claim established.
Operational authority: next-stage structural admission or answer persistence; see records.
Behavioral-authority path: respective chat, wiki and report consumers/channels/horizons are see records; no common grant beyond candidate availability.
Evidence source ID and local anchor: SRC-1 `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/wiki/agentic.rs`, `crates/atomic-core/src/reports/agentic.rs`; see records.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: none; semantic entailment unresolved rather than assumed novel.
Gap/limit: no concrete provider output or evidence-consuming acceptance trace.

Route ID: [EPI-RTE-citation-resolution](#epi-rte-citation-resolution)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-citation-ledger](#epi-obj-citation-ledger).
Content/update relation: no content change to prose; symbolic citation selection only.
Transition or check target: marker identity in the current run ledger, not factual claim support.
Evaluator/condition and domain: deterministic register/lookup/dedup, with Open or SeededOnly admission; see record.
Activation and timing: see record.
Possible or observed result: resolvable citation subset; see record.
Implemented force: enforces eligible identity lookup; unknown citation rows omitted.
Epistemic authority and scope: licenses association to registered identity and first excerpt only.
Operational authority: determines citation rows accompanying saved final prose, not whether every assertion may be published.
Behavioral-authority path: report mapper/storage and chat persistence/readers, enforcing citation identity selection for that result; see record.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: citations are weaker than verified grounding; target does not claim otherwise in inspected feature text.
Gap/limit: unknown markers can remain in prose; no semantic evaluator in this function.

Route ID: [EPI-RTE-wiki-citations](#epi-rte-wiki-citations)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-prose](#epi-obj-generated-prose).
Content/update relation: no content change to merged prose.
Transition or check target: citation indices of merged section-operation output.
Evaluator/condition and domain: explicit old/new index maps, not factual support; see record.
Activation and timing: see record.
Possible or observed result: retained old lineage or newly mapped excerpts; unknown citation omitted.
Implemented force: enforcing metadata construction, not article rejection.
Epistemic authority and scope: identity preservation of known references, not endorsement.
Operational authority: supplies proposal citations consumed by publication; see record.
Behavioral-authority path: draft/proposal saver then live article reader after acceptance; structural lineage force, persistent until replacement.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: none.
Gap/limit: full-rewrite mapping and storage version restoration not independently assessed.

Route ID: [RT-RTE-atom-mutation](runtime.md#rt-rte-atom-mutation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-atom-content](#epi-obj-atom-content).
Content/update relation: truth-apt transformation: indeterminate for edited propositions; edit correctness does not determine semantic preservation.
Transition or check target: edit shape, nonempty/change and timestamp concurrency, not truth; see record.
Evaluator/condition and domain: deterministic handler/storage check; see record.
Activation and timing: see record.
Possible or observed result: write or structural/concurrency rejection; see record.
Implemented force: enforcing update admissibility, not epistemic acceptance.
Epistemic authority and scope: no evidence-consuming truth decision established.
Operational authority: automatically changes atom after checks; see record.
Behavioral-authority path: model tool call to storage, enforcing write then later atom/search consumption; see record.
Evidence source ID and local anchor: SRC-1 `crates/atomic-core/src/chat_tools.rs`; see record.
Claim IDs: [RT-CLM-explicit-mutation](runtime.md#rt-clm-explicit-mutation).
Mismatch marker: explicit-request guidance is not independently enforced consent.
Gap/limit: ScopeGuard on readers does not establish scope enforcement on mutation.

Route ID: [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-prose](#epi-obj-generated-prose).
Content/update relation: no content change by acceptance itself.
Transition or check target: proposal base article identity/timestamp; see record.
Evaluator/condition and domain: software stale-base gate; caller accept/dismiss in review mode, automatic acceptance/direct save in alternate modes; see record.
Activation and timing: see record.
Possible or observed result: publication, dismissal, stale rejection or replacement; see record.
Implemented force: operational publication admission.
Epistemic authority and scope: caller acceptance has no named evidence-consuming truth criterion in this supplied route. Not acceptance in the technical epistemic sense merely because the method is named accept.
Operational authority: replaces live wiki and links; see record.
Behavioral-authority path: proposal/API to live wiki store then wiki/model readers, enforcing publication, persistent until replacement/deletion.
Evidence source ID and local anchor: SRC-1 `crates/atomic-core/src/lib.rs`; see record.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: human review not invariant.
Gap/limit: human actual criteria and exercised review not supplied.

Route ID: [RT-RTE-report-finding](runtime.md#rt-rte-report-finding)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-prose](#epi-obj-generated-prose).
Content/update relation: no content change by nonempty gate.
Transition or check target: final prose emptiness; see record.
Evaluator/condition and domain: deterministic trim/nonempty test; see record.
Activation and timing: after final pass, before finding write; see record.
Possible or observed result: EmptyScope or finding write; see record.
Implemented force: enforcing existence of content, not proposition correctness.
Epistemic authority and scope: provenance identifies report origin; no factual acceptance criterion established.
Operational authority: generated finding admitted automatically; see record.
Behavioral-authority path: runner/storage to finding readers and opted-in search, permissive reuse until later deletion/mutation; see record.
Evidence source ID and local anchor: SRC-1 `crates/atomic-core/src/reports/runner.rs`; see record.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: operational success does not imply supported research finding.
Gap/limit: transactional helper internals and withdrawal propagation unassessed.

Route ID: [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission), [RT-RTE-report-finding](runtime.md#rt-rte-report-finding)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-prose](#epi-obj-generated-prose).
Content/update relation: no content change from saving.
Transition or check target: respective persistence calls; see records.
Evaluator/condition and domain: storage success, not truth; see records.
Activation and timing: distinct save paths and ordering are see records.
Possible or observed result: durable message, article or finding; see records.
Implemented force: durable availability.
Epistemic authority and scope: persistence alone does not establish acceptance or lifecycle integration.
Operational authority: later reload/read possible; see records.
Behavioral-authority path: separate historical-message, wiki and finding consumers/channels/horizons are see records.
Evidence source ID and local anchor: SRC-1 `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/lib.rs`, `crates/atomic-core/src/reports/runner.rs`; see records.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: none.
Gap/limit: no observed retention or trace of later changed behavior.

Route ID: [EPI-RTE-generated-delivery](#epi-rte-generated-delivery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-prose](#epi-obj-generated-prose).
Content/update relation: truth-apt transformation: indeterminate. The reader unconditionally deletes matching bracketed numbers before line-window selection; these can carry proposition content, not just citation metadata. Non-ampliative reshaping is supported for the genuine-marker example in the record, not for the actual reader transformation across arbitrary prose. Entailed derivation or ampliative conjecture would require a concrete delivered proposition and its inputs; semantic preservation requires establishing the role of each removed expression in the selected content.
Transition or check target: scoped generated-content retrieval and current-run numbering.
Evaluator/condition and domain: reader code and line-window selection, not independent epistemic evaluation; see record.
Activation and timing: see record.
Possible or observed result: paged prose with new wiki/finding citation identity.
Implemented force: delivered model context, not enforced endorsement.
Epistemic authority and scope: current citation points to generated product, not automatically to its original evidence.
Operational authority: model may use retained generated prose in later answers.
Behavioral-authority path: tool result to provider, advisory/informational current-turn force; see record.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-cited-products](#epi-clm-cited-products).
Mismatch marker: downstream product citation is not transitive proof of original claims.
Gap/limit: actual reliance is unobserved; implementation alone establishes possible loss of proposition content. No semantic-preservation license applies to arbitrary delivered prose.

Route ID: [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: no new truth-apt object; metric propositions concern retrieval against fixture labels.
Content/update relation: truth-apt transformation: entailed derivation within the score function's finite input domain, conditional on supplied labels/ranks.
Transition or check target: evidence-session recovery at cutoff.
Evaluator/condition and domain: deterministic set membership and arithmetic; see record.
Activation and timing: benchmark scoring; see record.
Possible or observed result: recall/hit/MRR metrics; no observed score.
Implemented force: diagnostic reporting, not live KB acceptance or policy adaptation.
Epistemic authority and scope: licenses fixture-relative retrieval measurement only, not answer truth or explanation quality.
Operational authority: benchmark metrics emitted; no inspected live admission consumer.
Behavioral-authority path: metric reporter to experiment operator, advisory benchmark horizon; see record.
Evidence source ID and local anchor: see record.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: fixture evidence validity and comparative/causal attribution unestablished.

Route ID: [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: model components/settings and derived state; see records.
Content/update relation: non-truth-apt policy/content update: caller settings and operational derived-state refresh; specific tag propositions unassessed separately.
Transition or check target: jobs/settings admission, not evidence-consuming capacity comparison; see records.
Evaluator/condition and domain: configuration routing, task predicates and provider extraction; see records.
Activation and timing: see records.
Possible or observed result: changed settings/derived indexes; see records.
Implemented force: configuration selection and ranking availability, not demonstrated improvement.
Epistemic authority and scope: graph similarity, tags and completion status do not license truth judgments.
Operational authority: later model/prompt selection and retrieval can change; see records.
Behavioral-authority path: settings/provider resolution and search/graph consumers, permissive or ranking force on later operations; see records and [RT-BAP-chat-prompt](runtime.md#rt-bap-chat-prompt).
Evidence source ID and local anchor: SRC-1 `crates/atomic-core/src/graph_maintenance.rs`, `crates/atomic-core/src/lib.rs`; see records.
Claim IDs: none.
Mismatch marker: graph task completion can follow caught computation error.
Gap/limit: no observed evaluation-responsive improvement or provider weight update.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-cited-products](#epi-clm-cited-products) | Wiki articles with inline citations; recurring cited report findings, including contradiction scans | see record | Feature declaration and model citation instructions; see record | [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission), [RT-RTE-report-finding](runtime.md#rt-rte-report-finding), [EPI-RTE-citation-resolution](#epi-rte-citation-resolution), [EPI-RTE-wiki-citations](#epi-rte-wiki-citations) | Not supplied | No experiment; citation mapping checks identity, not truth or contradiction validity | Implemented generation/publication and citation metadata routes | Groundedness, contradiction detection accuracy and every-factual-claim compliance unknown. Feature text is not a universal correctness guarantee. |
| [RT-CLM-explicit-mutation](runtime.md#rt-clm-explicit-mutation) | Only explicitly requested writes | see record | Tool-description instruction | [RT-RTE-atom-mutation](runtime.md#rt-rte-atom-mutation) | Not supplied | No consent comparison; handler structural checks do not establish explicit user intent | Model guidance plus automatic write capacity | Not enforced as an independent per-content consent gate. |

## Bounded conclusion

Atomic wires acquisition of note content, model-generated answers/wiki/report candidates, structural publication gates and later consumption. Imported note warrant is unknown; capture and enrichment do not independently endorse propositions. The generation edges are semantically indeterminate without individuated outputs and premises. Novelty is not inferred merely from use of an LLM. See [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) and [EPI-OBJ-generated-prose](#epi-obj-generated-prose).

The implemented checks have narrower domains than truth assessment. Citation resolution checks eligible identity and deduplicates markers; wiki section updates preserve known citation associations. These are useful lineage controls, not evidence-consuming acceptance of claims. Atom mutation checks structural/concurrency admissibility; wiki acceptance checks base freshness and permits caller review, while alternate routes directly publish. Reports reject empty prose and otherwise automatically admit findings. Each grant is operational, with the specific consumers/horizons above; none of these checks alone establishes accepted ampliative knowledge. See [EPI-RTE-citation-resolution](#epi-rte-citation-resolution), [EPI-RTE-wiki-citations](#epi-rte-wiki-citations), [RT-RTE-atom-mutation](runtime.md#rt-rte-atom-mutation), [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission) and [RT-RTE-report-finding](runtime.md#rt-rte-report-finding).

Generated products are retained and can become later model input. The inspected chat readers delete matching bracketed numbers before paging and cite the product under a current-turn identity. Removing genuine evidence markers prevents their collision with current-turn numbering but does not preserve the full original source graph in the displayed tool payload. The deletion also matches ordinary numeric assertion content, so semantic preservation of delivered prose is indeterminate, not established by calling it marker cleanup. No observed downstream reliance or benefit is established. Persistence, links and operational use are not reclassified as lifecycle integration after epistemic acceptance. See [EPI-RTE-generated-delivery](#epi-rte-generated-delivery).

The retrieval evaluator derives fixture-relative metrics through fixed arithmetic. Conditional example: two reference evidence sessions and one recovered within cutoff yield recall 0.5. This is entailed by the inspected function conditional on those premises; it does not establish that the reference labels are true or that an answer is correct. See [EPI-RTE-retrieval-scoring](#epi-rte-retrieval-scoring).

Settings and derived state can change future behavior without a demonstrated truth-apt acceptance loop. Provider state is opaque and mutable endpoints are not immutable parameter identities. No supplied operation closes an improvement attribution or establishes model weight learning. Automated generation and admission are implemented independently of those unknowns. Learning benefit, content-directed criticism, theory iteration and reflective/autonomous theory-building are not system-wide negatives here: unresolved compaction, other evaluators, instructions and client paths prevent such completeness. The absence of observed runs additionally prevents claims of exercised behavior or causal benefit. See [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), [RT-CMP-agentic-model](runtime.md#rt-cmp-agentic-model), [RT-CMP-tagging-model](runtime.md#rt-cmp-tagging-model) and [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model).

## Shared records

### Operative objects

#### EPI-OBJ-atom-content
Label: Atom content

Source-native identity: markdown content of atoms. Representational form: natural-language propositions where present; markdown structure is symbolic rendering metadata. Storage substrate: Atomic database. Distinct from [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), which grants operations rather than retaining note prose. Closest supplied route [RT-RTE-capture-write](runtime.md#rt-rte-capture-write) describes its insertion, not an object declaration. SRC-1 doctrine/design `README.md`; implementation evidence and passage are see that route. The README names content as knowledge but does not establish source truth.

> Atomic stores knowledge as **atoms** — markdown notes that are automatically chunked, embedded, tagged, and linked by semantic similarity. Your atoms can be synthesized into wiki articles, explored on a spatial canvas, and queried through an agentic chat interface.
> --- `README.md`

#### EPI-OBJ-generated-prose
Label: Generated prose

Source-native identity: assistant message content, wiki article content and report finding markdown. Representational form: natural-language products, with symbolic inline markers assessed separately in [EPI-OBJ-citation-ledger](#epi-obj-citation-ledger). Storage substrate: database messages/articles/finding atoms. This is an inventory container, not an assertion that all three share admission or consumers. Distinct from supplied model components and ToolRegistry; closest supplied [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission), [RT-RTE-report-finding](runtime.md#rt-rte-report-finding) are production/retention routes, not object declarations. SRC-1 implementation evidence and load-bearing passages are see those records and [EPI-RTE-generated-delivery](#epi-rte-generated-delivery). No actual generated proposition is supplied; truth aptitude and semantic transformation must be determined per candidate.

#### EPI-OBJ-citation-ledger
Label: CitationLedger

Source-native identity: CitationLedger map and Citable entries. Representational form: symbolic identities, indices and chunk positions; natural-language excerpt content is a separate payload interpreted by readers. Storage substrate: current-run Mutex-protected memory; selected entries become citation metadata via separate persistence routes. Distinct from [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), which maps tool names to executors. Closest supplied routes [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) and [RT-RTE-report-finding](runtime.md#rt-rte-report-finding) use this object but do not declare it. SRC-1 implementation `crates/atomic-core/src/agent_runtime/citations.rs`.

> struct LedgerInner {
>     by_key: HashMap<(CitationSource, String), Citable>,
>     next_number: i32,
> }
> --- `crates/atomic-core/src/agent_runtime/citations.rs`

### Routes

#### EPI-RTE-citation-resolution
Label: Citation resolution

Part of: [RT-RTE-report-finding](runtime.md#rt-rte-report-finding)

This record individuates the report's final citation-selection function, not its whole admission route. Shared ledger implementation also supports chat, but the declaring referent here is report final-pass resolution. Endpoints: final markdown → ledger.cited_in → ResolvedCitation mapper → report runner persistence. Owner: deterministic code. Context/state: seeded and tool-registered identities, with policy Open or SeededOnly. Effects: selected citation metadata, unchanged final prose. The model proposes markers; code decides identity eligibility. No human veto, expected-answer oracle or truth criterion here. Operating mode: open report generation, not an improvement experiment. Unknown markers lose citation rows rather than rejecting final content. Guidance is the final-pass request; output retained is prose plus selected citation metadata.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RunOutput containing original content and resolved citations.
- Later read-back: report citation metadata becomes available through finding readers; specific storage reader internals uninspected.
- Delegated visibility: final provider gets research messages plus tool-free markdown instruction; it does not receive a later semantic verification result.
- Selection predicate: final text numeric markers, first occurrence, eligible registered number; registration retains first excerpt for a source identity.
- Invalidation or expiry: ledger ends with run; persistence is separate; no automatic prose correction on unknown number.
- Activation or effect: citation subset wired into RunOutput and supplied report persistence route; operation unobserved.
- Evidence limits: eligible identity is not support for a statement; initial source truth and later claim interpretation remain unchecked by this function.

SRC-1 implementation `crates/atomic-core/src/agent_runtime/citations.rs`, `crates/atomic-core/src/reports/agentic.rs`. Concrete implementation deduction: with ledger numbers 1 and 3 registered, final text `Claim [3]. Claim [99]. Again [3]. Then [1].` returns entries 3 then 1, leaving the original text unchanged. The unmatched 99 and repeated 3 produce no extra citation rows. No target execution was needed.

> let key = (source, source_id.to_string());
> --- `crates/atomic-core/src/agent_runtime/citations.rs`

> if let Some(existing) = inner.by_key.get(&key) {
>     return Some(existing.number);
> }
> --- `crates/atomic-core/src/agent_runtime/citations.rs`

> if !seen.insert(number) {
>     continue;
> }
> match by_number.get(&number) {
>     Some(citable) => cited.push(citable.clone()),
>     None => tracing::warn!(
>         citation_number = number,
>         "[agent_runtime] agent cited an unknown number; dropping"
>     ),
> }
> --- `crates/atomic-core/src/agent_runtime/citations.rs`

> let content = final_pass(&provider_config, &model, &messages).await?;
> let citations = ledger
>     .cited_in(&content)
> --- `crates/atomic-core/src/reports/agentic.rs`

> Ok(RunOutput { content, citations })
> --- `crates/atomic-core/src/reports/agentic.rs`

#### EPI-RTE-generated-delivery
Label: Generated delivery

Part of: [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn)

This is the chat turn's generated wiki/finding read function, not its overall model loop. Endpoints: scoped get_wiki/get_finding storage read → strip markers → line window → current-run citation register → tool result to model. Owner: Rust reader and ledger. State: retained generated content, paging and current ledger. Effects: current model context and citable product identity. No candidate truth decision or answer oracle: code decides selection and formatting, model may interpret the result. Operating mode is open chat. Numeric marker deletion protects local numbering but also removes original source associations from this payload.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: paged generated prose, descriptive product header and possible current-ledger marker.
- Later read-back: retained articles/findings are requested from storage on later chat invocations; cleanup output is current-run state, not separately persisted by these readers.
- Delegated visibility: provider gets selected prose and product identity; original inline marker identities are removed before paging.
- Selection predicate: requested tag/finding ID through scoped reader, then offset/limit; excerpt is registered against wiki tag ID or finding atom ID.
- Invalidation or expiry: current ledger expires after run; product replacement/deletion changes subsequent retrieval; reader does not withdraw historical answers.
- Activation or effect: selected retained generated prose is wired into tool output; changed behavior unobserved.
- Evidence limits: semantic preservation of arbitrary numeric bracket text is not universal; regex also removes noncitation numeric expressions matching its syntax. Product identity does not establish original evidence support.

SRC-1 implementation `crates/atomic-core/src/chat_tools.rs`. Concrete deduction: `Paris is in France [7].` becomes `Paris is in France.` before windowing. When `[7]` is a genuine evidence marker, this preserves that sentence's proposition while changing its reference metadata. Registration creates/reuses a new citation to the wiki/finding product, not to whatever original source 7 denoted. Counterexample: `The recorded value is [7].` becomes `The recorded value is.` under the same regex. Here the removed number supplies the asserted value; deleting it loses proposition content. Both wiki and finding readers apply deletion before selecting the line window and registering the resulting excerpt. Thus genuine-marker removal and product citation are implemented, but semantic preservation of arbitrary delivered prose is not established. Its content/update relation remains indeterminate without the original content, the roles of the deleted expressions and the selected output; this implementation deduction needs no runtime trace.

> .get_or_init(|| Regex::new(r" ?\[\d+\]").ok())
> .as_ref()
> {
>     Some(marker) => marker.replace_all(text, "").into_owned(),
>     None => text.to_string(),
> }
> --- `crates/atomic-core/src/chat_tools.rs`

> let window = line_window(
>     &strip_citation_markers(&wiki.article.content),
>     offset,
>     limit,
>     "get_wiki",
> );
> let number = ctx.citations.register(
>     CitationSource::Wiki,
>     &tag.tag.id,
>     None,
>     excerpt(&window.body),
> );
> --- `crates/atomic-core/src/chat_tools.rs`

> let window = line_window(
>     &strip_citation_markers(&finding.atom.content),
>     offset,
>     limit,
>     "get_finding",
> );
> let number = ctx.citations.register(
>     CitationSource::Finding,
>     atom_id,
>     None,
>     excerpt(&window.body),
> );
> --- `crates/atomic-core/src/chat_tools.rs`

#### EPI-RTE-wiki-citations
Label: Wiki citations

Part of: [RT-RTE-wiki-admission](runtime.md#rt-rte-wiki-admission)

This part owns section-operation citation reconstruction, not wiki candidate synthesis or acceptance. Endpoints: merged_content with existing/new source maps → known citation rows → WikiProposalDraft. Owner: deterministic code. Context/state: old indices, old excerpts and new source chunks. Effects: proposal metadata preserving old source identity or mapping new chunks. No human truth judgment, expected-answer oracle or live acceptance within this function. Operating mode: wiki update preparation. Unknown numbers are omitted from citation list, not rejected prose. Distinct checks/consumers from report citation resolution.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: optional WikiProposalDraft with merged_content and citations.
- Later read-back: proposal and, after separate publication, article citation readers can consume constructed metadata; see supplied parent route.
- Delegated visibility: synthesis source numbering is represented by old/new maps; reconstruction itself does not call the model.
- Selection predicate: numeric markers in merged content, deduplicated and resolved against explicit existing/new index maps.
- Invalidation or expiry: proposal supersession/stale rejection owned by parent route, not this metadata function.
- Activation or effect: reconstructed citations attached to draft; no observed publication.
- Evidence limits: index preservation does not check source truth or claim support; excerpt truncation can omit context.

SRC-1 implementation `crates/atomic-core/src/wiki/mod.rs`. A known old marker preserves its original atom/chunk/excerpt even with sparse numbering; this is a counterexample to assuming every wiki update remaps indices positionally. No supersession of the valid runtime container is needed.

> atom_id: existing_citation.atom_id.clone(),
> chunk_index: existing_citation.chunk_index,
> excerpt: existing_citation.excerpt.clone(),
> source_url: existing_citation.source_url.clone(),
> --- `crates/atomic-core/src/wiki/mod.rs`

> "[wiki] Merged article references citation with no known source — dropping from citation list"
> --- `crates/atomic-core/src/wiki/mod.rs`

#### EPI-RTE-retrieval-scoring
Label: Retrieval scoring

No counterpart after comparison with supplied runtime records: [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) changes live derived state, while this evaluator emits benchmark metrics. Endpoints: retrieved session IDs/ranks and reference evidence set → score_retrieval → metric reporting. Owner: benchmark code. State: fixed cutoff and fixture evidence IDs. Effects: recall, hit and reciprocal-rank values. Fixture labels serve as reference outcome; their provider is the dataset, not the model. No human/model semantic judge in this scoring function. Operating mode: bounded benchmark cases, not live-content admission. Code decides comparison; operator can interpret metrics. No implemented automatic successor selection or live veto follows from the score.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RetrievalScore with retrieved_evidence, recall, hit, mrr and first_rank.
- Later read-back: uninspected — benchmark reporting consumption after emission not traced here; no live KB update consumer established.
- Delegated visibility: inapplicable — score function invokes no provider or delegated worker.
- Selection predicate: session.rank at or below cutoff and evidence-set membership.
- Invalidation or expiry: inapplicable — pure scoring result; caller's report retention lifecycle not inspected.
- Activation or effect: function computes metrics that the suite reports; no supplied executed evaluation.
- Evidence limits: label validity, retrieval correctness beyond evidence IDs, answer truth and component causal benefit not established.

SRC-1 implementation `crates/atomic-bench/src/suites/memory_longitudinal.rs`. The scoring domain is finite session-label recovery, not substantive truth of retrieved prose. Implementation deduction: one recovered evidence session out of two yields 0.5 recall; rank 2 as first match yields 0.5 MRR. Warrant is conditional on the input labels/ranks, not a claim about an actual target run.

> let recall = if evidence.is_empty() {
>     0.0
> } else {
>     retrieved_evidence as f64 / evidence.len() as f64
> };
> --- `crates/atomic-bench/src/suites/memory_longitudinal.rs`

> let mrr = first_rank.map(|rank| 1.0 / rank as f64).unwrap_or(0.0);
> --- `crates/atomic-bench/src/suites/memory_longitudinal.rs`

### Claims

#### EPI-CLM-cited-products
Label: Cited products

Claimed operation: wiki synthesis with inline citations built from notes, and scheduled research tasks yielding recurring cited findings including contradiction scans/open-question tracking. SRC-1 doctrine/design `README.md`. Distinct from [RT-CLM-explicit-mutation](runtime.md#rt-clm-explicit-mutation), which constrains agent writes, not research-product warrant. The declaration does not promise that every factual claim is independently verified; its implemented support and limits are compared above.

> - **Wiki Synthesis** — LLM-generated articles with inline citations, built from your notes
> - **Reports** — Scheduled research tasks that turn your atoms into recurring cited findings (daily briefings, contradiction scans, open-question tracking)
> --- `README.md`
