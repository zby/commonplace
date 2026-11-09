---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MGI-Mind's candidate transformations, validity policies, outcome authority and evaluator limits at the frozen revision."
run-id: AAS-2026-11-08-mgi-mind-e0f02081480f-01
reviewed-boundary: a8defc36f7d0bcd5108714763a12625a0eda0868
---

# MGI-Mind epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on MGI-Mind's retained assertions and procedures, rather than merely making them available. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register). All new inspection below is SRC-1 at that register's frozen commit, implementation unless marked doctrine/design. No target, tests, examples or providers were executed.

The supplied runtime orders inspection but is not treated as complete. In particular, fact conflict resolution, explicit withdrawal, typed outcomes, skill outcomes, transcript filtering, provenance admission and retrieval advice require separate assessment. No defective supplied runtime fact requires supersession. A newly identified public-tool-description mismatch is local to [EPI-CLM-outcome-duel](#epi-clm-outcome-duel), not a reason to discard the working procedure-outcome route.

| Entry point / operation | Source path in SRC-1 | Coverage and conclusion limit |
|---|---|---|
| CLI dispatch; MCP operations and startup | `src/cli.rs`, `src/mcp.rs` | Direct dispatch searches and bounded reads, including outcome, provenance, skill and advice branches. Shared add, service and context findings are see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing), [RT-RTE-scoped-http](runtime.md#rt-rte-scoped-http). |
| Direct add, ingest and quarantine | `src/ingest.rs`, `src/storage.rs` | Direct heuristic and relevant storage reads; admission policy is see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission). Direct add is a counterexample to universal relevance gating. Explicit quarantine promotion/expiry bodies not independently retraced; no system-complete admission guarantee. |
| Agent extraction and optional local extractor | `src/extractor.rs`, `src/mcp.rs` | Direct prompt/parser/repair reads supplement [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction). Actual generated triples and semantic fidelity remain unobserved. |
| Fact add, query, invalidate/restore, cardinality | `src/knowledge.rs`, `src/duel.rs` | Direct core, visibility and withdrawal reads; history/as-of helpers enumerated but not fully retraced. No guarantee of historical-query fidelity across all callers. |
| Drift and background re-test | `src/doubt.rs`, `src/confidence.rs` | Direct scoring, transition and retrieval-consumer reads. Background lifecycle ownership is supplied by runtime; no observed scheduled pass. |
| Procedure learn/recall/outcome; skill outcome/match | `src/procedure.rs`, `src/skill.rs`, `src/storage.rs`, `src/mcp.rs` | Direct admission, counters, verification flags, return and ranking reads. [EPI-RTE-outcome-trust](#epi-rte-outcome-trust) separates caller reports from independently measured success. |
| Typed outcome log | `src/outcome.rs`, `src/storage.rs`, `src/mcp.rs` | Direct write/read namespace and bridge inspection; facts and memories are not interchangeable IDs. |
| Provenance import | `src/provenance.rs`, `src/mcp.rs` | Direct validator, formatter and storage handoff reads. Checks citation shape, not source occurrence or truth. |
| Transcript ingestion | `src/session_ingest.rs` | Direct producer/filter/handoff reads. Text survives with role tags; session-ID lineage does not reach stored source metadata in this implementation. |
| Should-search advisory operation | `src/retrieval_policy.rs`, `src/mcp.rs` | Direct classifier and dispatch reads. Advice does not enforce host search. |
| Markdown reconciliation; consolidation; sessions and context | `src/md_reconcile.rs`, `src/consolidate.rs`, `src/session.rs`, `src/cli.rs` | Supplied findings only: [RT-RTE-markdown-reconcile](runtime.md#rt-rte-markdown-reconcile), [RT-RTE-store-consolidation](runtime.md#rt-rte-store-consolidation), [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing). No independent complete maintenance audit. |
| Evaluators | `src/bench.rs`, `src/bench_procedural.rs`, `src/bench_policy.rs`, `src/bench_stale.rs`, `src/calibration.rs` | Direct scoring/aggregation/scaffold reads; raw result files, test suites and CI not inspected here. No observed efficacy or causal benefit claim. |
| Host prompts, Python drivers and HTTP routes | `AI_INSTRUCTIONS.md`, `docs/integrations/openai_agents.py`, `src/http_api.rs` | Supplied boundary/runtime findings except targeted manual search; no external SDK inspection. Tool-result delivery is not demonstrated belief or compliance. |
| Remaining included administrative/maintenance paths | `src/cli.rs` | Import/export, backup/recovery, migrations, blocks, web capture, install-mode auto-detection and full consolidation branches remain unassessed beyond supplied findings/dispatch enumeration. No system-complete negative about evaluation, derivation or adaptation follows. |

Consequential claims are [RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit), [EPI-CLM-validity-model](#epi-clm-validity-model), [EPI-CLM-outcome-duel](#epi-clm-outcome-duel) and [EPI-CLM-procedure-signal](#epi-clm-procedure-signal). No supplied execution evidence individuates a generated accepted ampliative proposition. This prevents a conclusion about exercised knowledge production, not inspection of the implemented selection architecture. External inference internals remain opaque; fixity and version limits are see [RT-CMP-embedder](runtime.md#rt-cmp-embedder), [RT-CMP-reranker](runtime.md#rt-cmp-reranker), [RT-CMP-extractor](runtime.md#rt-cmp-extractor), [RT-CMP-host-model](runtime.md#rt-cmp-host-model).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memories](#epi-obj-memories) | Caller notes and transcript assertions; rules may instead be non-truth-apt prescriptions | see record | SRC-1 `src/ingest.rs` | No item-level source warrant established |
| [EPI-OBJ-provenance](#epi-obj-provenance) | Imported snippet, citation metadata and optional note | see record | SRC-1 `src/provenance.rs` | Citation formatting is not authentication |
| [EPI-OBJ-facts](#epi-obj-facts) | Subject-predicate-object assertions | see record | SRC-1 `src/knowledge.rs` | Declared cardinality defines conflict domain; “valid” is storage standing |
| [EPI-OBJ-procedures](#epi-obj-procedures) | Proposed error-to-fix relations; fix text can be imperative | see record | SRC-1 `src/procedure.rs` | Success on a task would not prove explanation or transfer |
| [EPI-OBJ-skills](#epi-obj-skills) | Caller playbooks; truth-apt theory content not determinable without actual bodies | see record | SRC-1 `src/skill.rs` | Mutable text alone is not content-directed criticism |
| [EPI-OBJ-procstats](#epi-obj-procstats) | Counts/verified standing about procedures and skills | see record | SRC-1 `src/storage.rs` | Derived authority, not independently authenticated outcomes |
| [EPI-OBJ-external-signals](#epi-obj-external-signals) | Caller claims of test/compile/user/citation outcomes | see record | SRC-1 `src/outcome.rs` | Report type does not establish the reported event occurred |
| [EPI-OBJ-session-summary](#epi-obj-session-summary) | Caller summary of prior work | see record | SRC-1 `src/session.rs` | Supplied runtime establishes retention/delivery, not factual accuracy |

## Authority-route ledger

The ledger separates checks, disposition, retention and consumption even when one function implements several. Record-owned details are “see” citations; architectural status is assessed here. No row claims observed operation. “None” under epistemic authority means no truth license established by that route, not that the stored content is false.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | content transformation | implemented | [EPI-OBJ-memories](#epi-obj-memories) | truth-apt transformation: acquisition/import | Caller note enters memory | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | Stored or error | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | Source warrant unknown | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | see [RT-BAP-host-recall](runtime.md#rt-bap-host-recall) | SRC-1 `src/storage.rs` | [RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit) | none | Source only; activation unobserved |
| [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | check/evidence production | implemented | [EPI-OBJ-memories](#epi-obj-memories) | no content change | Relevance, novelty and duplicate suitability, not proposition truth | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | Ingest, not direct add | Verdict and placement counters | Policy check | None beyond gate criterion | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | SRC-1 `src/ingest.rs` | none | none | Source only; activation unobserved |
| [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | disposition/acceptance | implemented | [EPI-OBJ-memories](#epi-obj-memories) | no content change | Admission to live or quarantined retrieval state | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | After gate | Store/quarantine/reassert/skip | Enforcing placement | Operational admission, not evidence-consuming truth acceptance | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | SRC-1 `src/ingest.rs` | none | none | Source only; activation unobserved |
| [EPI-RTE-text-selection](#epi-rte-text-selection) | content transformation | implemented | [EPI-OBJ-memories](#epi-obj-memories) | truth-apt transformation: non-ampliative reshaping | Marker removal / transcript text selection | Deterministic code on specified text domain | Raw ingest or transcript ingest | Selected text, role prefix; omitted non-text blocks | Enforcing producer filter | No new source warrant; transcript-session lineage degraded | Candidates reach ingest | Ingest -> stored notes -> later search; permissive retention, advisory host use | SRC-1 `src/ingest.rs`, `src/session_ingest.rs` | none | none | Concrete deduction in record; not a fidelity guarantee for arbitrary Unicode or omitted context |
| [EPI-RTE-provenance-import](#epi-rte-provenance-import) | check/evidence production | implemented | [EPI-OBJ-provenance](#epi-obj-provenance) | no content change | Snippet/citation shape | Code: nonempty, HTTPS/host, path and range syntax | Before storage | Pass or tool error | Enforcing request rejection | Syntax only; no fetched source comparison | Bad shape blocks import | Validator -> MCP branch; enforcing this request | SRC-1 `src/provenance.rs`, `src/mcp.rs` | none | none | Source only; activation unobserved |
| [EPI-RTE-provenance-import](#epi-rte-provenance-import) | content transformation | implemented | [EPI-OBJ-provenance](#epi-obj-provenance) | truth-apt transformation: acquisition/import | External snippet plus citation envelope | Caller supplies snippet and metadata; code formats | After validation | Citation-wrapped note | Admission through ordinary storage | Citation association retained; source warrant unknown | Can later be searched | MCP -> storage -> search -> host; contextual, cross-session | SRC-1 `src/provenance.rs`, `src/mcp.rs` | none | none | Source only; activation unobserved |
| [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) | content transformation | implemented | [EPI-OBJ-facts](#epi-obj-facts) | truth-apt transformation: indeterminate | Memory text -> proposed triples | see [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) | Feature/install/ingest dependent | Model-proposed structured assertions | see [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) | Neither entailment nor non-entailment established for actual output | see [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) | see [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) | SRC-1 `src/extractor.rs` | none | none | May reshape, derive or conjecture; need input/output propositions and checked interpretation to decide |
| [EPI-RTE-extraction-parser](#epi-rte-extraction-parser) | check/evidence production | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Model response's JSON structure | Serde parser; array-of-arrays fallback, not semantic verifier | After completion, one wording repair if malformed | Parsed triples or error/drop | Enforcing structural gate | No entailment, source-truth or completeness license | Parsed response permits fact API calls | Parser -> background worker -> fact writer; permissive immediate | SRC-1 `src/extractor.rs` | none | none | Source only; activation unobserved |
| [EPI-RTE-fact-comparison](#epi-rte-fact-comparison) | check/evidence production | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Same-axis distinct-object conflict on Single/TemporalSingle | Cardinality/strings then weighted entrenchment vs challenger | Fact add under locks; first or Multi bypasses duel | Flip, contested or quarantine recommendation | Policy result | No world-truth comparison; counters, age, dependencies and inheritance proxy standing | Disposition consumes recommendation | Duel -> fact add branch; policy decision this write | SRC-1 `src/knowledge.rs`, `src/duel.rs` | [EPI-CLM-validity-model](#epi-clm-validity-model) | none | Unregistered Multi axes do not resolve contradictions; repetitions need not be independent observations |
| [EPI-RTE-fact-disposition](#epi-rte-fact-disposition) | disposition/acceptance | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Standing of proposed and displaced triple | Fact code consumes duel/tombstone/flip-back conditions | After comparison, before/after upsert respectively | Active, contested, quarantine; stale/superseded predecessor; invalidated refusal | Enforcing store status | Operational standing under declared axis, not truth acceptance | Default query membership changes | Fact writer -> payload status -> query filters; enforcing later reads | SRC-1 `src/knowledge.rs`, `src/duel.rs` | [EPI-CLM-validity-model](#epi-clm-validity-model) | none | Source only; activation unobserved |
| [EPI-RTE-fact-disposition](#epi-rte-fact-disposition) | retention | implemented | [EPI-OBJ-facts](#epi-obj-facts) | truth-apt transformation: acquisition/import | Retain caller or extractor assertion and status | see [EPI-RTE-fact-disposition](#epi-rte-fact-disposition) | Fact upsert | Payload-only fact; retired losers retained | Durable write | Input warrant unknown; rejection status not deletion | History/contest/default readers differ | Qdrant -> fact consumers; retained across invocations | SRC-1 `src/knowledge.rs` | [EPI-CLM-validity-model](#epi-clm-validity-model) | none | Source only; activation unobserved |
| [EPI-RTE-fact-withdrawal](#epi-rte-fact-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Explicit withdrawal/restoration of named fact | Caller decision; code changes valid flag and temporal bound | On invalidate/restore request | Invalidated; same/case-whitespace re-add refused; explicit restore possible | Enforcing visibility/tombstone | Caller withdrawal respected; no independent falsification judgment | Blocks default reads/reassertion until restore, status retained | Caller -> fact payload -> query/add consumers; enforcing across later calls | SRC-1 `src/knowledge.rs` | [EPI-CLM-validity-model](#epi-clm-validity-model) | none | Source only; activation unobserved |
| [EPI-RTE-fact-consumption](#epi-rte-fact-consumption) | operational admission/selection/consumption | implemented | [EPI-OBJ-facts](#epi-obj-facts) | truth-apt transformation: non-ampliative reshaping | Returned query facts | Valid/status filters, lexical query, optional drift order | On query; context route separately supplied | Visible selected assertions, possibly doubt flag | Enforcing membership, ranking order | Returned does not mean accepted true; contested/unknown remain visible | Fact material reaches caller; excluded standing withheld | Query -> caller text/structured results -> possible host; contextual this request | SRC-1 `src/knowledge.rs` | [EPI-CLM-validity-model](#epi-clm-validity-model) | none | Source only; activation unobserved |
| [EPI-RTE-outcome-recording](#epi-rte-outcome-recording) | content transformation | implemented | [EPI-OBJ-external-signals](#epi-obj-external-signals) | truth-apt transformation: acquisition/import | Caller report -> typed signal | Type parser plus source-key deduplication | mind_outcome | Persisted latest type/source report; possible doubt flag | Enforcing log update | Report warrant unknown; no test execution or proof check here | New test/compile signal on procedure enables outcome bridge | MCP -> memory payload -> bridge/guardrail; permissive immediate and later | SRC-1 `src/outcome.rs`, `src/mcp.rs` | [EPI-CLM-outcome-duel](#epi-clm-outcome-duel) | memory/fact namespace gap | Report authentication and connection to exact tested content remain unestablished |
| [EPI-RTE-outcome-trust](#epi-rte-outcome-trust) | behavior/policy adaptation | implemented | [EPI-OBJ-procstats](#epi-obj-procstats) | non-truth-apt policy/content update: outcome-derived ranking state | Procedure/skill trust counters and verified flag | Caller worked/verify or new typed procedure signal; arithmetic rule | Outcome request; later recall/match | Counts changed, verified latches, trust shifts order | Ranking, not execution mandate | Success metadata licenses boost under local policy; no general correctness or transfer license | Later candidates may rank higher/lower, failure does not clear verified | Side collection -> recall/match -> rank -> host tool text; ranking then advisory across tasks | SRC-1 `src/storage.rs`, `src/procedure.rs`, `src/skill.rs`, `src/mcp.rs` | [EPI-CLM-procedure-signal](#epi-clm-procedure-signal) | caller flags are not independent measurement | Source only; activation unobserved |
| [EPI-RTE-drift-evaluation](#epi-rte-drift-evaluation) | check/evidence production | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Fact-origin versus recent-query embedding context | Centered cosine with available origin/current/mean; configured threshold | Query; off/shadow/enforce modes | Measurement; enforcing mode updates consecutive-drift counter | Measurement in shadow; counter/ranking when enforce | Context distance, not evidence that assertion is false | In enforce, doubt result reaches query's in_doubt sorting | Activity/origin -> drift -> fact query; ranking this request; counters later | SRC-1 `src/doubt.rs`, `src/knowledge.rs` | [EPI-CLM-validity-model](#epi-clm-validity-model) | none | Missing context means no penalty; in-context retrieval resets count |
| [EPI-RTE-confidence-retest](#epi-rte-confidence-retest) | check/evidence production | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Cached confidence vs recomputed proxy score | Formula from fact metadata; typed signal lookup uses memories namespace | Scheduled re-test path supplied by runtime | Promote/recover/no change plus score cache | Counter disposition, not world test | No direct re-observation of proposition; formula threshold only | Can change future doubt state; query application remains mode/context dependent | Re-test -> fact score/count -> retrieval drift consumer; conditional ranking later | SRC-1 `src/doubt.rs`, `src/confidence.rs`, `src/storage.rs` | [EPI-CLM-validity-model](#epi-clm-validity-model) | typed signal namespace gap | Not a guarantee every low score is demoted in every reader |
| [EPI-RTE-search-advice](#epi-rte-search-advice) | operational admission/selection/consumption | implemented | [EPI-OBJ-memories](#epi-obj-memories) | no content change | Need to consult memory | Query cues and known-library word match | Explicit should-search call | P1/P2/P0 advice with reasons | Advisory | No warrant that no relevant memory exists on P0 | Host may choose search, server cannot require it | MCP advice text -> host; advisory immediate answer | SRC-1 `src/retrieval_policy.rs`, `src/mcp.rs` | [RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit) | none | Source only; activation unobserved |
| [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) | operational admission/selection/consumption | implemented | [EPI-OBJ-session-summary](#epi-obj-session-summary) | truth-apt transformation: non-ampliative reshaping | Briefing content selection | see [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) | see [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) | see [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) | Contextual | No accuracy endorsement from freshness or selection | see [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) | see [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) | SRC-1 `src/cli.rs` | none | none | Source only; activation unobserved |
| [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | retention | implemented | [EPI-OBJ-skills](#epi-obj-skills) | non-truth-apt policy/content update: caller playbook replacement | Named instruction body | see [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | see [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | see [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | Durable content replacement | No truth acceptance established | see [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | see [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | SRC-1 `src/skill.rs` | none | none | Source only; activation unobserved |
| [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | check/evidence production | implemented | Evaluation outputs; see record | no content change | Retrieval identifiers/fix strings, policy accounting, synthetic duel outcomes | Dataset oracle or authored expected outcome; not unrestricted truth oracle | Explicit benchmark/calibrate request | Reports/counts; STALE dispatch returns empty report | Reporting only in inspected entry paths | Only named metric/domain; no demonstrated end-to-end warrant | No inspected automatic deployment or semantic acceptance consumer | Evaluator -> CLI/optional result file -> operator; advisory experiment report | SRC-1 `src/bench.rs`, `src/bench_procedural.rs`, `src/bench_policy.rs`, `src/bench_stale.rs`, `src/calibration.rs` | none | none | No runs claimed; procedural benchmark directly recalls storage before trust ranking; policy baseline is constructed |
| [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | retention | implemented | [EPI-OBJ-memories](#epi-obj-memories) | no content change | Retain admitted note | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | Durable storage | No new epistemic license | see [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) | see [RT-BAP-host-recall](runtime.md#rt-bap-host-recall) | SRC-1 `src/storage.rs` | none | none | Source only; observed activation unestablished |
| [EPI-RTE-text-selection](#epi-rte-text-selection) | content transformation | implemented | [EPI-OBJ-facts](#epi-obj-facts) | truth-apt transformation: indeterminate | My … is … interpreted as user triple | see [EPI-RTE-text-selection](#epi-rte-text-selection) | Raw ingest | Subject user, sliced predicate/object | Candidate generation | Speaker resolution unchecked | Fact candidate may enter fact admission | Heuristic -> ingest -> fact store; permissive this input | SRC-1 `src/ingest.rs` | none | none | Source only; observed activation unestablished |
| [EPI-RTE-drift-evaluation](#epi-rte-drift-evaluation) | disposition/acceptance | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Doubt state after numerical check | see [EPI-RTE-drift-evaluation](#epi-rte-drift-evaluation) | Enforce only, required context present | Counter changed, in_doubt sorting | Ranking | Operational de-emphasis, not truth rejection | see [EPI-RTE-drift-evaluation](#epi-rte-drift-evaluation) | see [EPI-RTE-drift-evaluation](#epi-rte-drift-evaluation) | SRC-1 `src/doubt.rs`, `src/knowledge.rs` | none | none | Source only; observed activation unestablished |
| [EPI-RTE-confidence-retest](#epi-rte-confidence-retest) | disposition/acceptance | implemented | [EPI-OBJ-facts](#epi-obj-facts) | no content change | Promote/recover doubt after score check | see [EPI-RTE-confidence-retest](#epi-rte-confidence-retest) | After recomputation | Count and score stored | Enforcing metadata update | No truth acceptance | see [EPI-RTE-confidence-retest](#epi-rte-confidence-retest) | see [EPI-RTE-confidence-retest](#epi-rte-confidence-retest) | SRC-1 `src/doubt.rs` | none | none | Source only; observed activation unestablished |
| [EPI-RTE-outcome-recording](#epi-rte-outcome-recording) | retention | implemented | [EPI-OBJ-external-signals](#epi-obj-external-signals) | no content change | Retain deduplicated reported signals | see [EPI-RTE-outcome-recording](#epi-rte-outcome-recording) | After parse/dedup | Log written | Durable report retention | Report retained, not acceptance of claim | see [EPI-RTE-outcome-recording](#epi-rte-outcome-recording) | see [EPI-RTE-outcome-recording](#epi-rte-outcome-recording) | SRC-1 `src/outcome.rs`, `src/storage.rs` | none | none | Source only; observed activation unestablished |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source / evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit) | see record | see record | see record | [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), [EPI-RTE-search-advice](#epi-rte-search-advice) | Uninspected | None; external host choice is not an intervention comparison | Tools and guidance afford recall before answering | Habit/compliance unobserved |
| [EPI-CLM-validity-model](#epi-clm-validity-model) | see record | see record | see record | [EPI-RTE-fact-comparison](#epi-rte-fact-comparison), [EPI-RTE-fact-disposition](#epi-rte-fact-disposition), [EPI-RTE-fact-withdrawal](#epi-rte-fact-withdrawal), [EPI-RTE-drift-evaluation](#epi-rte-drift-evaluation), [EPI-RTE-confidence-retest](#epi-rte-confidence-retest) | Uninspected | No demonstrated improvement; formula criteria differ from proposition testing | Implemented standing, withdrawal and conditional ranking controls | “Re-justifying” is context/proxy scoring, not a fresh truth test; default shadow differs from enforcement |
| [EPI-CLM-outcome-duel](#epi-clm-outcome-duel) | see record | see record | see record | [EPI-RTE-outcome-recording](#epi-rte-outcome-recording), [EPI-RTE-fact-comparison](#epi-rte-fact-comparison), [EPI-RTE-confidence-retest](#epi-rte-confidence-retest) | Uninspected | No live comparison; new challenger uses zero external count and no typed score | Procedure bridge works structurally; generic fact-duel feed not established | Typed reports stored on memories, not facts; no automatic ID correspondence in inspected path |
| [EPI-CLM-procedure-signal](#epi-clm-procedure-signal) | see record | see record | see record | [EPI-RTE-outcome-trust](#epi-rte-outcome-trust), [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | Uninspected | Returned success reports do not isolate fix efficacy; retrieval benchmark measures matching strings | Outcome-responsive ranking is implemented | Verification can be supplied by caller; no mandatory harness proof |

## Bounded conclusion

**Acquisition and reshaping.** Ordinary notes, provenance snippets, asserted facts, error/fix pairs and summaries enter from callers. Their source warrant is unknown. Provenance import retains a citation envelope without fetching or checking it. Transcript import preserves user/assistant text and role but discards service/tool/thinking blocks and does not retain its calculated transcript source tag. Marker extraction can faithfully remove an instruction wrapper on the demonstrated ASCII input, but its “my … is …” conversion requires interpreting speaker as “user”; this interpretation is not a checked source-truth premise. These findings are see [EPI-RTE-text-selection](#epi-rte-text-selection), [EPI-RTE-provenance-import](#epi-rte-provenance-import), [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory).

**Generation and checks.** Optional extraction requests triples, then tests response shape and retries malformed JSON. It does not compare each triple to the input's semantic content. Without actual paired inputs and outputs, the edge remains indeterminate between reshaping, entailed derivation and ampliative conjecture. No produced accepted ampliative claim is established. This is not a claim that no model can conjecture. Evidence-consuming acceptance with a criterion, intended use and scope is not supplied by a successful parse, gate verdict, persistence, freshness or top retrieval rank ([RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction), [EPI-RTE-extraction-parser](#epi-rte-extraction-parser)).

**Standing and withdrawal.** Fact conflict checks target distinct objects on declared single-valued axes. Weighted history selects operational standing; first writes and Multi predicates do not duel. Active/contested status is not a source-truth license. Disposition retains candidates and losers but changes default visibility; explicit invalidation blocks reassertion until explicit restore. Drift compares contexts, while re-test recalculates metadata confidence. Neither evaluator directly tests the proposition against the world. Their criteria, consumers and conditional ranking force are separately retained in [EPI-RTE-fact-comparison](#epi-rte-fact-comparison), [EPI-RTE-fact-disposition](#epi-rte-fact-disposition), [EPI-RTE-fact-withdrawal](#epi-rte-fact-withdrawal), [EPI-RTE-drift-evaluation](#epi-rte-drift-evaluation), [EPI-RTE-confidence-retest](#epi-rte-confidence-retest). Retaining status-bearing assertions is not established lifecycle integration after epistemic acceptance.

**Adaptation without a truth acceptance route.** Procedure and skill outcomes durably change ranking state consumed by future recall/match. This implemented path exists independently of the typed-signal/fact-ID gap. The named outcome types and caller verification flags do not authenticate tests. A verified flag latches even after failures, although failures reduce ranking. The path changes retrieval policy over candidates rather than editing their explanations. No improved future capacity, content-directed theory criticism, or exercised self-improvement follows from counters alone ([EPI-RTE-outcome-trust](#epi-rte-outcome-trust)). The shipped playbook body replacement path separately affords durable instruction changes ([RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)). Actual theory-builder properties remain unestablished without actual content and criticism/consumption evidence; model opacity is not evidence of their absence.

**Evaluation and downstream reliance.** Benchmark answer oracles are dataset session IDs, exact fix text, or authored synthetic outcome expectations. They are not unrestricted semantic judges. Policy comparison constructs its no-search baseline; STALE's frozen dispatch returns an empty aggregation. No causal experiment here licenses attributing better assistant answers or safer belief revision. Search, fact query, briefings and skills can reach an assistant through returned material; the host's interpretation remains advisory/contextual, not mandatory acceptance. Retrieval advice can request a search, not enforce one ([EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation), [EPI-RTE-search-advice](#epi-rte-search-advice), [RT-BAP-host-recall](runtime.md#rt-bap-host-recall)). Unassessed maintenance/evaluation paths and absent execution evidence prevent a whole-system negative or efficacy verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-memories
Label: Memory text

Source-native memory chunks contain natural-language caller text; Qdrant stores payload and dense/sparse indexes. Numerical embeddings select text, not establish its truth. Closest supplied record is [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), a write/read route rather than this object; no object counterpart is declared there. Provenance-wrapped notes are separately assessed below. SRC-1, `src/storage.rs`, `src/ingest.rs`.

> content,
>                 source: None,
> --- `src/ingest.rs`

#### EPI-OBJ-provenance
Label: Provenance content

Material part of the memory-text class with different admission checks: natural-language snippet and note plus symbolic citation-field envelope, stored through ordinary memory storage. Distinct from [EPI-OBJ-memories](#epi-obj-memories) as the citation-bearing part; no supplied object counterpart. SRC-1, `src/provenance.rs`, `src/mcp.rs`.

> out.push_str("[external] ");
>     out.push_str(input.origin_url);
> --- `src/provenance.rs`

#### EPI-OBJ-facts
Label: Fact triples

Natural-language subject/predicate/object labels are encoded as symbolic fields consumed by exact/lexical fixed rules. Vectorless Qdrant facts also carry status, temporal bounds and counts. No supplied object counterpart; closest [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) produces some, but explicit callers produce others. SRC-1, `src/knowledge.rs`.

> payload.insert("subject".into(), subject.into());
>     payload.insert("predicate".into(), predicate.into());
>     payload.insert("object".into(), object.into());
> --- `src/knowledge.rs`

#### EPI-OBJ-procedures
Label: Error fix playbooks

Natural-language fix/context plus symbolic normalized error signature, vectors for retrieval and identity metadata live in memories collection under procedure type. No supplied object counterpart; distinct from ordinary notes by matching/ranking consumers. SRC-1, `src/storage.rs`, `src/procedure.rs`.

> payload.insert("trigger_error".into(), norm_error.into());
>     payload.insert("trigger_context".into(), context.into());
>     payload.insert("fix".into(), fix.into());
> --- `src/storage.rs`

#### EPI-OBJ-skills
Label: Skill playbooks

Named caller text has natural-language body/trigger and symbolic stable identity; stored in Qdrant and selected through match/show/catalogue. Body content cannot be individuated as a truth-apt theory from the API alone. Closest supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) is this object's admission route, not an object counterpart. SRC-1, `src/skill.rs`; retention/consumer evidence is supplied by that runtime record.

> let existed = storage::get_skill(config, &name).await?.is_some();
>     let id = storage::add_skill(config, &name, when, body).await?;
> --- `src/skill.rs`

#### EPI-OBJ-procstats
Label: Procedure statistics

Symbolic integer counters, last_used timestamp and string boolean verified in Qdrant's separate derived stats collection. Consumers merge these with procedure/skill hits. Distinct from their core instruction text; dropping statistics need not delete it. No supplied object counterpart; [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) mentions separate outcome history without declaring this object. SRC-1, `src/storage.rs`.

> let verified = cur.verified || (worked && verify);
> --- `src/storage.rs`

#### EPI-OBJ-external-signals
Label: Typed external signals

Symbolic type/success/source/timestamp reports serialized as JSON in the memories collection's external_signals_v15 field. Natural-language source strings are caller identities/labels, not authenticated evidence. Distinct from [EPI-OBJ-procstats](#epi-obj-procstats): log deduplication and counter updates differ. No supplied object counterpart. SRC-1, `src/outcome.rs`, `src/storage.rs`.

> set_memory_payload_field(config, memory_id, "external_signals_v15", serialised).await
> --- `src/storage.rs`

#### EPI-OBJ-session-summary
Label: Session summary

Natural-language caller summary on local session files. Closest supplied record [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) supplies persistence and later read-back passages; this object is distinct from that route and no supplied object counterpart exists. Evidence and exact consumer are see that record, SRC-1 `src/session.rs`, `src/cli.rs`. No endorsement or semantic validation follows from atomic file write.

### Routes

#### EPI-RTE-text-selection
Label: Text candidate selection

Code owns raw-marker selection and transcript filtering before ingest. This producer is upstream of, not identical to, [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission). No supplied counterpart after comparison. SRC-1, `src/ingest.rs`, `src/session_ingest.rs`. Concrete implementation deduction: ASCII input `Remember that the staging DB is Postgres 16.` has its prefix removed, yielding `the staging DB is Postgres 16.` as a Memory candidate. This is non-ampliative reshaping of the assertion, not a newly evidenced database claim. In contrast `My editor is Helix.` becomes subject `user`, predicate `editor`, object `Helix`; speaker resolution to user is an unchecked interpretation, so this fact edge is truth-apt transformation: indeterminate. These deductions trace code only, not target execution. Transcript producer retains only user/assistant text, prefixes role, and calls ingest on all candidates. It computes but discards transcript source_tag, degrading session-specific lineage. The caller selects input; code proposes candidates, ingest decides later admission; no per-candidate human veto or answer oracle. Open-input mode, no autonomous criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate list internally; transcript report on completion.
- Later read-back: Selected stored text can reach later search through ingest.
- Delegated visibility: inapplicable — no isolated model worker; transcript filters producer-visible material.
- Selection predicate: Markers for raw text; transcript row role and text-block type.
- Invalidation or expiry: inapplicable — this producer has no retained queue; ordinary memory maintenance acts later.
- Activation or effect: Implemented filtering/reshaping, not observed improved relevance.
- Evidence limits: Full semantic fidelity of omitted context and arbitrary Unicode byte slicing not established.

> if let Some(r) = lower.strip_prefix("remember that ") {
>             Some(line[line.len() - r.len()..].trim().to_string())
> --- `src/ingest.rs`

> let _ = source_tag; // reserved for a future per-candidate source plumbing.
> 
>     report.ingested = ingest::run_ingest(config, None, candidates, library).await?;
> --- `src/session_ingest.rs`

#### EPI-RTE-provenance-import
Label: Provenance admission

Caller proposes snippet, URL and metadata; MCP validation decides syntactic admission, then formatter passes content to ordinary storage. Distinct from [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory) by mandatory citation checks, not by a stronger fact oracle. SRC-1, `src/mcp.rs`, `src/provenance.rs`. Validation checks nonempty snippet/tool, obvious markup, URL host/scheme and optional repository/path/range syntax; it does not fetch source or compare snippet occurrence. Caller can edit/retry, no per-item human approval or reference-answer oracle. Open-request mode; normal memory delete/rewrite is separate recovery. Citation fields persist with snippet, but source truth/authenticity remains unknown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Error or saved chunk count plus provenance identifier.
- Later read-back: Formatted note can reach later search.
- Delegated visibility: inapplicable — no delegated inference.
- Selection predicate: Provenance validator then ordinary storage admission.
- Invalidation or expiry: Normal memory deletion/replacement; no citation freshness check here.
- Activation or effect: Wired syntax rejection and cited-content retention.
- Evidence limits: Source occurrence, URL mutability and relevance of the optional note remain unverified.

> if let Err(e) = crate::provenance::validate(&input) {
>                 anyhow::bail!("{e}");
>             }
> --- `src/mcp.rs`

> let n = crate::storage::add_memory(cfg, input.library, &content, Some(&source)).await?;
> --- `src/mcp.rs`

#### EPI-RTE-extraction-parser
Label: Extraction structure check

Part of: [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction)

Material parser/check part of the supplied optional extraction route, with distinct target from the model's semantic extraction request. SRC-1, `src/extractor.rs`. It strips fences, locates array bounds and tries typed objects, then three-string arrays; one stricter wording retry handles parse failure. The prompt's instruction to use nonempty subject/object is a request, not an independently implemented truth/entailment test in parse_response. This route can reject malformed content without evaluating whether a well-formed proposition follows from the input. Owner is extractor code; Qwen supplies proposal, code can veto structure; no human gate or answer oracle; open input.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed triples or error after repair attempt.
- Later read-back: inapplicable — parser conversation is transient; successful triples persist through separate fact admission.
- Delegated visibility: Worker sees selected memory content; no parent transcript guaranteed.
- Selection predicate: Successful JSON object-array parse or nonempty fallback list of length-three arrays.
- Invalidation or expiry: inapplicable — no retained parser result cache or durable retry queue.
- Activation or effect: Parsed results permit worker fact writes; semantics unobserved.
- Evidence limits: JSON success establishes structure only; no actual input/output fidelity trace supplied.

> if let Ok(triples) = serde_json::from_str::<Vec<Triple>>(body) {
>         return Some(triples);
>     }
> --- `src/extractor.rs`

> parse_response(&second)
>         .ok_or_else(|| anyhow::anyhow!("extractor returned non-JSON twice; dropping chunk"))
> --- `src/extractor.rs`

#### EPI-RTE-fact-comparison
Label: Fact conflict comparison

Fact add consults cardinality, same-axis existing valid facts and distinct-object conflict; deterministic duel compares strongest incumbent entrenchment to challenger weight. SRC-1, `src/knowledge.rs`, `src/duel.rs`. New identity relative to supplied ingest/extraction routes: those deliver assertions; this route judges conflicting fact standing from metadata. Multi and first writes skip conflict comparison. Caller supplies content and may register cardinality; code proposes verdict and can veto live visibility later. No mandatory human approval or answer oracle; open-request mode. Challenger inputs use confirmation history and process-local inherited flag, but external_signals=0 and external_signal_score=None in this add path. Counterexample to interpreting confirmations as independent observations: exact reassertion increments the triple's count without a world-observation check. Formula success does not establish proposition truth or causal mechanism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Duel recommendation and optional loser ID to writer.
- Later read-back: Fact payload history can affect later duels.
- Delegated visibility: inapplicable — no model delegation.
- Selection predicate: Conflict on Single/TemporalSingle; most-entrenched existing opponent.
- Invalidation or expiry: Later reassertion changes counts; flip-back window affects subsequent disposition.
- Activation or effect: Implemented policy comparison; no exercised correction benefit shown.
- Evidence limits: Cardinality schema and metadata are premises, not verified world facts; generic typed outcome-to-fact feed not established.

> external_signals: 0,
> --- `src/knowledge.rs`

> external_signal_score: None,
> --- `src/knowledge.rs`

> let w_new = weight_new_for_mode(new_inputs, config.install_mode);
>     let outcome = resolve_duel(ent_score, w_new);
> --- `src/duel.rs`

#### EPI-RTE-fact-disposition
Label: Fact standing and retention

Fact writer consumes comparison, tombstone and flip-back results; upserts proposed triple/status before retiring a loser as stale or superseded by cardinality. SRC-1, `src/knowledge.rs`, `src/duel.rs`. Distinct from [EPI-RTE-fact-comparison](#epi-rte-fact-comparison): this is the consequential store mutation, not its evaluator. No supplied counterpart after comparison with [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), which admits upstream memory candidates. Caller proposes assertion; code owns status decision; no answer oracle or mandatory per-content human veto. Active is operational admission, not evidence-consuming acceptance against a source-truth criterion. Separate locks serialize fact writers, but upsert/retire are separate operations, not demonstrated all-or-nothing rollback. Reassertion and explicit restore supply bounded recovery. Guidance is cardinality/weight/flip-back policy; stored text/status/counts, not a justification proof.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ID/verdict such as recorded, won, contested, quarantined or invalidated.
- Later read-back: Default queries exclude hidden statuses; contest/history paths can access other standing.
- Delegated visibility: inapplicable — no isolated inference.
- Selection predicate: Tombstone and duel verdict; recent flip-back converts winning reassertion to contested.
- Invalidation or expiry: Explicit invalidate/restore, further assertions or maintenance; loser retained.
- Activation or effect: Wired status and query-membership changes; observed truth correction unestablished.
- Evidence limits: Retaining losers preserves trace, not an audit that proves the winner; no lifecycle integration after truth acceptance established.

> crate::duel::DuelOutcome::Flip if flip_back => (EntryStatus::Contested, None),
>                 crate::duel::DuelOutcome::Flip => (EntryStatus::Active, loser),
>                 crate::duel::DuelOutcome::Contested => (EntryStatus::Contested, None),
> --- `src/knowledge.rs`

> crate::duel::DuelOutcome::Quarantine => (EntryStatus::QuarantineCandidate, None),
> --- `src/knowledge.rs`

#### EPI-RTE-fact-withdrawal
Label: Fact invalidate restore

Caller explicitly withdraws a named fact; code sets valid=false and valid_until. Reasserting same triple or case/whitespace variant is refused by add; restore alone flips valid back and removes bound, leaving lifecycle status untouched. SRC-1, `src/knowledge.rs`. Distinct from [EPI-RTE-fact-disposition](#epi-rte-fact-disposition) automatic duel retirement: withdrawal marks a retracted mistake rather than temporal successor history. No supplied counterpart. Caller chooses/vetoes operation, code enforces; human versus model authorship unresolved. No truth oracle or independent falsification check; open-request mode. Reversible explicit restore, not automatic regeneration, is recovery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Invalidate timestamp, restore boolean or refused re-add verdict.
- Later read-back: Default query/add predicates honor withdrawal; restoring stale status does not automatically make it visible.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Named ID and current valid flag; variant tombstone normalized by case/whitespace.
- Invalidation or expiry: Explicit restore is the withdrawal reversal; original status retained.
- Activation or effect: Enforcing later visibility and reassertion guard.
- Evidence limits: Full historical-query behavior not retraced; caller withdrawal reason need not be evidenced.

> payload.insert("valid".into(), "false".into());
>     payload.insert("valid_until".into(), now.clone().into());
> --- `src/knowledge.rs`

> if existing_valid.as_deref() == Some("false") {
> --- `src/knowledge.rs`

> if valid.as_deref() != Some("false") {
>         return Ok(false);
>     }
> --- `src/knowledge.rs`

#### EPI-RTE-fact-consumption
Label: Fact query visibility

Query code filters valid=true and hidden statuses, collects lexical matches, applies optional drift evaluation and orders in_doubt last. SRC-1, `src/knowledge.rs`. Distinct from supplied [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing): direct fact-query consumer and its sorting, not the briefing's selected rendering. Contested and Unknown are default-visible too, so visible is not synonymous with uncontested or established true. This is selection/delivery, not epistemic acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected facts, possibly in_doubt; empty list if facts collection unavailable.
- Later read-back: Reads persisted assertions and statuses accumulated through prior writes.
- Delegated visibility: inapplicable — caller receives results, no isolated agent frame.
- Selection predicate: Valid flag, status exclusions and text match; drift only if configured context exists.
- Invalidation or expiry: Future status/validity changes alter membership; retrieval context can reset doubt.
- Activation or effect: Enforcing membership and conditional ranking, advisory host meaning.
- Evidence limits: Host belief/use, temporal-reader completeness and query success unobserved.

> must: vec![Condition::matches("valid", "true".to_string())],
>         must_not: hidden_status_must_not(),
> --- `src/knowledge.rs:890-891`

> facts.sort_by_key(|f| f.in_doubt);
> --- `src/knowledge.rs`

#### EPI-RTE-outcome-recording
Label: Typed outcome reports

Caller supplies memory ID, signal type, success and source; server timestamps, deduplicates by (type,source), writes log, flags repeated recent test failures and bridges new test/compile signals to procedure counters. SRC-1, `src/mcp.rs`, `src/outcome.rs`, `src/storage.rs`. No supplied route counterpart: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) does not record outcome signals. Code validates the enum, not test execution or evidence linking a specific content version to a measured result. Caller is proposer and reporter, code admits; no mandatory human approval, independent expected-answer oracle or bounded experiment. Reposting updates the signal log but novelty gating prevents a repeated key bumping procedure counters again; a changed success value under the same key is therefore not a fresh counter event. Guidance is type/source policy; persisted result is reports, not executable test proof. Later correction of report does not undo prior counter effects.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Report count, optional guardrail and procedure outcome confirmation.
- Later read-back: Stored log can reach scoring helper; procedure counters reach recall; namespace limits below.
- Delegated visibility: inapplicable — no delegated evaluator.
- Selection predicate: Known signal type; latest timestamp per type/source; new key plus procedure type for bridge.
- Invalidation or expiry: Same-key log replacement; not atomic counter rollback or truth withdrawal.
- Activation or effect: Log update and procedure bridge wired; guardrail schedules attention rather than independently validating claim.
- Evidence limits: Storage helpers read/write MEMORIES_COLLECTION. Fact re-test passes a fact ID to that helper, while fact payloads reside in FACTS_COLLECTION. Without a same-ID memory point/bridge, this does not deliver fact-local typed evidence; no such bridge established in these paths.

> let (mut out, signal_was_new) =
>                 crate::outcome::record_with_novelty(cfg, memory_id, signal).await?;
> --- `src/mcp.rs`

> MEMORIES_COLLECTION,
>         memory_id,
>         "external_signals_v15",
> --- `src/storage.rs`

> if signal_was_new
>                 && is_proc_signal
>                 && crate::storage::is_procedure(cfg, memory_id).await?
> --- `src/mcp.rs`

#### EPI-RTE-outcome-trust
Label: Outcome trust ranking

Outcome code records worked/failure and latching verified state in derived statistics; procedure recall and skill match fetch statistics and rank candidates. SRC-1, `src/storage.rs`, `src/procedure.rs`, `src/skill.rs`, `src/mcp.rs`. Distinct material outcome consumer from supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), which replaces bodies. Human/model contribution depends on caller. Code accepts caller flags: mind_learn accepts verified (default false), manual procedure_outcome forces verify=false, skill outcome accepts verify directly, and typed new test/compile procedure signal bridges with verify=success. No harness result is required by these inspected branches. No mandatory human veto or answer oracle; open requests. No text repair/criticism follows failure; counters persist and tilt future selection. Derived stats can be discarded independently, but the verified flag is not automatically withdrawn on failure. Evidence-responsive ranking capacity exists; improvement needs outcomes and a defensible comparison.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Confirmation of changed counts/verified state.
- Later read-back: Recall/match overlays statistics then rank_score changes future ordering.
- Delegated visibility: inapplicable — no separate inference frame.
- Selection predicate: Procedure/skill ID; verified boost +0.25; outcome ratio contribution capped at 0.20 in magnitude.
- Invalidation or expiry: Counts accumulate; verified latches; dropping derived statistics is recovery separate from core text.
- Activation or effect: Implemented durable behavior-shaping selection state; downstream model use and improved capacity unobserved.
- Evidence limits: Caller verification is not independent measurement; retrieval-pool selection bounds which boosted candidate can appear.

> let verified = cur.verified || (worked && verify);
> --- `src/storage.rs`

> if h.verified {
>         s += 0.25; // a deterministic-signal-verified fix is trustworthy
>     }
> --- `src/procedure.rs`

> s += 0.20 * ratio * confidence;
> --- `src/procedure.rs`

> let verify = arg_bool(args, "verify", false);
>                     crate::skill::outcome(cfg, name, worked, verify, Some(agent.unwrap_or("mcp")))
> --- `src/mcp.rs`

#### EPI-RTE-drift-evaluation
Label: Context drift standing

Code compares centered context vectors for a surfaced fact, not its proposition to observations. SRC-1, `src/doubt.rs`, `src/knowledge.rs`. Distinct from supplied context assembly: this is query-time standing evaluation. Required origin/current/corpus mean may be missing; off returns no check, shadow records measurement without modifying ranking, enforce compares configured threshold and updates consecutive counter; query marks in_doubt then sorts it after other facts. Enforcing mode can change reliance ranking without accepting/rejecting truth. No human judgment or model answer oracle in comparison; config owner chooses threshold/mode. This check is content-insensitive numerical context similarity, not formulated theory criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Optional doubt state to query plus drift observation.
- Later read-back: Persisted counter used on later checks; origin context was retained at write.
- Delegated visibility: inapplicable — no model delegate.
- Selection predicate: Existing contextual vectors, mode and drift threshold; repeated drift counter.
- Invalidation or expiry: An in-context retrieval resets consecutive drift count; no deletion.
- Activation or effect: Conditional ranking and observation wired, not calibrated semantic validity.
- Evidence limits: Context similarity cannot license source truth; missing vectors or shadow mode do not enforce a penalty.

> let origin = crate::activity::load_origin_context(config, origin_context_id?)?;
>     let drift = context_drift(&origin, current, mean)?;
>     crate::activity::observe_drift(config, drift);
> --- `src/doubt.rs`

> DriftMode::Enforce(threshold) => {
>             apply_doubt_check_to_fact(config, fact_id, drift > threshold)
>                 .await
>                 .ok()
>         }
>         _ => None,
> --- `src/doubt.rs`

#### EPI-RTE-confidence-retest
Label: Metadata confidence re-test

Background re-test reads fact counters and cached score, computes weighted proxy confidence, chooses transition and writes score/count. SRC-1, `src/doubt.rs`, `src/confidence.rs`. Closest supplied [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) does not perform this re-test; runtime account separately identifies background maintenance without a record for these formulas. No counterpart. It is not a fresh empirical test: the criterion is score delta and threshold; code can promote/recover doubt state, without deleting. Typed signal lookup is shared with memory reports; [EPI-RTE-outcome-recording](#epi-rte-outcome-recording) states the fact/memory namespace gap. Caller/config/model facts supply premises; code decides standing. No expected-answer oracle or human per-transition approval. Scores and doubt counts persist, audit records label transitions; no autonomous revision of weights/theory is shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: PromoteToDoubt, RecoverFromDoubt or NoChange to scheduler.
- Later read-back: Fresh confidence score becomes next comparison baseline; count reaches subsequent drift checks.
- Delegated visibility: inapplicable — no model delegate.
- Selection predicate: Downward delta greater than 0.2 and score below 0.3; recovery requires in-doubt and upward delta greater than 0.2.
- Invalidation or expiry: Later recalculation can recover; ordinary query can reset count in enforcing context.
- Activation or effect: Stored metadata change wired; actual query ranking still depends on its mode/context and check.
- Evidence limits: No actual scheduled pass; storage lookup errors/defaults may replace unavailable inputs; no universal demotion guarantee.

> let typed_signals = crate::storage::read_external_signals(config, fact_id)
>         .await
>         .unwrap_or_default();
> --- `src/doubt.rs`

> let transition = decide_retest_transition(cached_score, new_score, currently_in_doubt);
> --- `src/doubt.rs`

> if delta < -RETEST_DOWN_SHIFT_DELTA && new_score < RETEST_PROMOTE_THRESHOLD {
> --- `src/confidence.rs`

#### EPI-RTE-search-advice
Label: Search before answer advice

MCP retrieves known library names and classifies query with deterministic cues; result is search priority/reason, not an enforced search. SRC-1, `src/mcp.rs`, `src/retrieval_policy.rs`. Distinct from [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), which actually performs recall, and complements [RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit). Query names a known library -> P1; meta/cross-session/negation cues also select P1, personal/project cues P2, otherwise P0. Code proposes advice; host chooses and can ignore it; no answer oracle. Open-request operation. No persisted changed host policy or mandatory gate is shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rendered priority and reason, suggested libraries.
- Later read-back: inapplicable — this operation does not accumulate advice for a future invocation.
- Delegated visibility: inapplicable — no delegated context.
- Selection predicate: Cue matching plus library word boundaries.
- Invalidation or expiry: inapplicable — request-local advisory result.
- Activation or effect: Advisory behavior choice, no guaranteed memory consultation.
- Evidence limits: P0 is absence of detected trigger, not proof of absent useful memory or answer correctness.

> // Live, query-aware search-before-answer advice (the runtime half of
>             // the policy that AI_INSTRUCTIONS documents and bench_policy scores
>             // offline). Advisory only — MCP cannot force a search.
> --- `src/mcp.rs`

#### EPI-RTE-benchmark-evaluation
Label: Benchmark evaluator scope

Distinct from supplied runtime invocation routes: these explicit evaluator drivers own experiment/report computation, not production truth admission. SRC-1, `src/bench.rs`, `src/bench_procedural.rs`, `src/bench_policy.rs`, `src/bench_stale.rs`, `src/calibration.rs`. LongMemEval batches supplied sessions into an isolated library, retrieves and scores distinct session IDs against dataset answer_session_ids. This measures any gold session in top-k, not final answer truth or complete evidence sufficiency. Procedural benchmark learns dataset pairs then directly calls storage::recall_procedures and compares exact trimmed fix strings; it does not exercise procedure::rank's trust adjustment in that query. Policy benchmark credits recorded hit_at and constructs all-false without-policy rows: no agent policy intervention is observed. Calibration compares formulas on authored scenarios with source-native expected outcomes; fit to intent is not world-correctness. Frozen STALE run logs scaffold notice and returns aggregate of no scenarios, even though another branch is mentioned. No external branch or raw-result efficacy is imported. Operator chooses dataset/command; code scores against named oracle; outputs are reports, not automatically admitted policy revisions. No implemented successor-selection consumer established in these inspected entry paths.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Metric reports/counters and optional result file; STALE empty aggregation.
- Later read-back: uninspected — raw result files and any later operator use not inspected.
- Delegated visibility: inapplicable — inspected retrieval/calibration paths use dataset/score functions; STALE judge parameter is not exercised by frozen run.
- Selection predicate: Dataset gold IDs/fix equality or authored expected duel outcome; policy question-type buckets.
- Invalidation or expiry: inapplicable — evaluator reports do not themselves withdraw production content.
- Activation or effect: Wired metric production, no observed run or automatic improvement from it.
- Evidence limits: No component effect, replay safety, answer quality or transfer inference. Tests/CI/raw results not independently inspected here.

> ranked_sessions.iter().take(k).any(|s| gold.contains(s))
> --- `src/bench.rs`

> let gold_position = hits.iter().position(|h| h.fix.trim() == item.fix.trim());
> --- `src/bench_procedural.rs`

> ("R@1".to_string(), false),
>                 ("R@5".to_string(), false),
>                 ("R@10".to_string(), false),
> --- `src/bench_policy.rs`

> if actual == s.expected {
>             matched += 1;
> --- `src/calibration.rs`

> Ok(aggregate(&[], _judge_model))
> --- `src/bench_stale.rs`

### Claims

#### EPI-CLM-validity-model
Label: Validity model

Claimed operation: duel, doubt window, inheritance discount, temporal standing and withdrawal keep old or self-reinforcing assertions from ossifying; facts re-justify themselves and quiet ones are re-tested. SRC-1, `README.md`, doctrine/design. Distinct from supplied [RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit), which asks the host to recall. The source qualifies default shadow mode and incomplete live dependency/diversity producers. Implemented standing controls are real; source-truth checking and improved validity are separate unsupported conclusions.

> The part that is harder to find is what keeps the store from ossifying as it
> fills with old, contradictory, or self-reinforcing beliefs.
> --- `README.md`

> An entrenched fact has to keep re-justifying itself.
> --- `README.md`

> This ships in
> shadow: drift is measured and recorded, and no fact changes, until you set
> `doubt_drift_threshold` from your own store's numbers and switch
> `doubt_drift_mode` to `"enforce"`.
> --- `README.md`

#### EPI-CLM-outcome-duel
Label: Outcome fact feed

Claimed operation: registered mind_outcome tool description says typed signals feed the fact duel rule's external_signal_score. SRC-1, `src/mcp.rs`, doctrine/design embedded in executable tool registration. No supplied claim counterpart after comparison with [RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit). This narrower claim is not supported as a generic live fact-add route: challenger external count is zero and typed score None; incumbent reads entrenchment inputs, not typed signal score. Separately re-test calls memory-namespace signal reader using fact ID. A coincidental same-ID memory row is not a fact-local signal producer/bridge. This limits the claim without denying the implemented procedure bridge.

> Feeds the fact duel rule's external_signal_score.
> --- `src/mcp.rs`

#### EPI-CLM-procedure-signal
Label: Procedure verification bar

Claimed operation: reliable verified state should require deterministic success rather than an impression; failures should demote bad playbooks. SRC-1, `src/procedure.rs`, doctrine/design. Distinct from supplied recall-habit claim and from outcome-to-fact feed. The implementation requests this provenance but accepts flags/types from callers, while ranking does consume the resulting state. No automatic source-authentication guarantee follows.

> A reliable `verified = true` needs a
> //! deterministic signal (test green / exit 0) from the harness, not from mgimind.
> --- `src/procedure.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
