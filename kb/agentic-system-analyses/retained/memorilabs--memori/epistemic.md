---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Memori epistemic routes: service-derived candidates, client admission, contextual reliance and bounded benchmark judgments."
run-id: AAS-2026-10-17-memori-fd4a0418c09b-01
reviewed-boundary: 574b1ea3e876f100ef82c37817d603eb7e258e59
---

# Memori epistemic report

## Source-and-claim boundary

Question: what truth-apt content does Memori acquire or generate, what checks license reliance, and which consumers give the results consequential force? Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register), SRC-1. This is a complete artifact, partial service-dependent loop, not a whole-system knowledge-production audit.

Direct reads below add client parsing, SQLite lineage/withdrawal, query selection, OpenClaw cleanup, feedback and notebook evaluators to the supplied runtime account. All implementation deductions concern the frozen source; none required target execution. Source-native documentation supplies design or reported results, not independently observed runs. No provider/service was called. No frozen execution trace, causal intervention, extraction input/output instance or independently authenticated benchmark result was supplied.

| Entry point/operation | Source path | Coverage basis and records / prevented conclusion |
|---|---|---|
| Python registered calls, streaming and explicit capture | `memori/llm/invoke/invoke.py` | Supplied runtime findings: [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation), [RT-RTE-stream-exhaustion](runtime.md#rt-rte-stream-exhaustion); direct reads of recall/injection below. Not all framework stream wrappers inspected; no all-provider negative. |
| Python augmentation and local write consumers | `memori/memory/augmentation/augmentations/memori/_augmentation.py` | Direct process/response/scheduling reads plus `_struct.py`, `_db_writer.py`, SQLite driver selected fact/summary/graph branches; service-import through local-retention records below. Other database drivers and transaction behavior remain uninspected. |
| Manual recall and deletion | `memori/__init__.py` | Direct API dispatch and `memori/memory/recall.py`, `memori/search/_core.py`, `memori/llm/pipelines/recall_injection.py`: recall-selection, entity-withdrawal below. Native search internals not exhaustively traced. |
| TypeScript hooks and native worker/service routes | `memori-ts/src/memori.ts` | Supplied findings [RT-RTE-typescript-hooks](runtime.md#rt-rte-typescript-hooks), [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission). Native local checks do not establish hosted extraction correctness. |
| OpenClaw registered tools/hooks | `integrations/openclaw/src/tools/index.ts` | Direct registration, feedback, sanitizer and augmentation submission reads; [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), capture-cleanup, feedback-delivery below. Compaction consumer guidance see [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance). |
| Claude CLI and skill | `integrations/claude-code/index.ts` | Direct terminal dispatch and feedback branch; supplied [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill), [RT-CLM-ambient-lifecycle](runtime.md#rt-clm-ambient-lifecycle). Recall/summary/augmentation/compaction covered by supplied account; quota/signup are administrative, not truth acceptance. |
| Hermes tools and turn capture | `integrations/hermes/src/memori_hermes/__init__.py` | Dispatch search cross-checked against [RT-RTE-hermes-provider](runtime.md#rt-rte-hermes-provider); feedback included, no local memory-repair consumer established. Host implementation remains excluded. |
| Python management CLI | `memori/__main__.py` | Direct complete dispatch read: cluster, quota, provision, setup, sign-up. Administrative operation bodies not evaluated for epistemic content; no system-complete absence of other checks follows. |
| Hosted MCP and durable-only prompt | `docs/memori-cloud/mcp/skills/memori-mcp/SKILL.md` | Supplied design evidence [RT-RTE-mcp-guidance](runtime.md#rt-rte-mcp-guidance); server/tool internals inaccessible, preventing enforcement and truth-check conclusions. |
| Lab evaluator and imported augmented data | `benchmarks/02_run_benchmark.ipynb` | Direct complete decoded source reads of both notebooks and benchmark README; benchmark-answer/judging/metrics/retention below. External datasets/weights not acquired; notebook cells have no supplied execution outputs. |
| Public warrant/result claims | `README.md` | Direct README, augmentation concept and benchmark-results documentation reads; claim records below. Tests/evaluators outside these notebooks remain available but uninspected: prevents a repository-complete negative about evaluation. |

Missing server derivation/admission/compaction implementation prevents deciding semantic fidelity, novelty, contradictions, evidence-consuming acceptance and post-acceptance integration there. Missing concrete extraction candidates prevents distinguishing reshaping, entailed inference and ampliative conjecture per service output. Missing run evidence prevents activation/benefit conclusions; missing independently varied component comparisons prevents attributing benchmark outcomes to structured extraction, summary use or any particular check. Opaque inference parameters are see runtime component records, not inferred from memory updates.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-conversation-messages](#epi-obj-conversation-messages) | see [EPI-OBJ-conversation-messages](#epi-obj-conversation-messages) | Conversation messages | SRC-1 `memori/memory/_writer.py` | see [EPI-OBJ-conversation-messages](#epi-obj-conversation-messages) |
| [EPI-OBJ-entity-facts](#epi-obj-entity-facts) | see [EPI-OBJ-entity-facts](#epi-obj-entity-facts) | Entity facts | SRC-1 `memori/memory/_struct.py` | see [EPI-OBJ-entity-facts](#epi-obj-entity-facts) |
| [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples) | see [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples) | Semantic triples | SRC-1 `memori/memory/_struct.py` | see [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples) |
| [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary) | see [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary) | Conversation summary | SRC-1 `memori/memory/augmentation/augmentations/memori/_augmentation.py` | see [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary) |
| [EPI-OBJ-process-attributes](#epi-obj-process-attributes) | see [EPI-OBJ-process-attributes](#epi-obj-process-attributes) | Process attributes | SRC-1 `memori/memory/_struct.py` | see [EPI-OBJ-process-attributes](#epi-obj-process-attributes) |
| [EPI-OBJ-fact-embeddings](#epi-obj-fact-embeddings) | see [EPI-OBJ-fact-embeddings](#epi-obj-fact-embeddings) | Fact embeddings | SRC-1 `memori/search/_core.py` | see [EPI-OBJ-fact-embeddings](#epi-obj-fact-embeddings) |
| [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context) | see [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context) | Recall context | SRC-1 `memori/llm/pipelines/recall_injection.py` | see [RT-BAP-recalled-context](runtime.md#rt-bap-recalled-context) |
| [EPI-OBJ-benchmark-answer](#epi-obj-benchmark-answer) | see [EPI-OBJ-benchmark-answer](#epi-obj-benchmark-answer) | Lab answer | SRC-1 `benchmarks/02_run_benchmark.ipynb` | see [EPI-OBJ-benchmark-answer](#epi-obj-benchmark-answer) |
| [EPI-OBJ-benchmark-verdict](#epi-obj-benchmark-verdict) | see [EPI-OBJ-benchmark-verdict](#epi-obj-benchmark-verdict) | Lab verdict | SRC-1 `benchmarks/02_run_benchmark.ipynb` | see [EPI-OBJ-benchmark-verdict](#epi-obj-benchmark-verdict) |
| [EPI-OBJ-feedback-content](#epi-obj-feedback-content) | see [EPI-OBJ-feedback-content](#epi-obj-feedback-content) | Feedback content | SRC-1 `integrations/claude-code/index.ts` | see [EPI-OBJ-feedback-content](#epi-obj-feedback-content) |

## Authority-route ledger

Each row is a sparse function-level overlay; record-owned fields are `see` the cited declaration. Operational admission is not epistemic acceptance. Hosted extraction is declared by the public augmentation claim below, but its implementation and semantic update relation are not determinable; that limit does not erase the implemented import route.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-service-import](#epi-rte-service-import) | content transformation | implemented | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) | SRC-1 `memori/memory/augmentation/augmentations/memori/_augmentation.py` | [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-RTE-service-import](#epi-rte-service-import) | see [EPI-RTE-service-import](#epi-rte-service-import) |
| [EPI-RTE-triple-shape](#epi-rte-triple-shape) | check/evidence production | implemented | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | SRC-1 `memori/memory/_struct.py` | [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) | see [EPI-RTE-triple-shape](#epi-rte-triple-shape) |
| [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | content transformation | implemented | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | SRC-1 `memori/memory/_struct.py` | [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) | see [EPI-RTE-triple-rendering](#epi-rte-triple-rendering) |
| [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | disposition/acceptance | implemented | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | SRC-1 `memori/memory/augmentation/augmentations/memori/_augmentation.py` | [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) | see [EPI-RTE-memory-scheduling](#epi-rte-memory-scheduling) |
| [EPI-RTE-local-retention](#epi-rte-local-retention) | retention | implemented | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | SRC-1 `memori/storage/drivers/sqlite/_driver.py` | [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-RTE-local-retention](#epi-rte-local-retention) | see [EPI-RTE-local-retention](#epi-rte-local-retention) |
| [EPI-RTE-recall-selection](#epi-rte-recall-selection) | operational admission/selection/consumption | implemented | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | SRC-1 `memori/llm/pipelines/recall_injection.py` | [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) | see [EPI-RTE-recall-selection](#epi-rte-recall-selection) |
| [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | content transformation | implemented | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | SRC-1 `integrations/openclaw/src/sanitizer.ts` | [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) | see [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) |
| [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | operational admission/selection/consumption | implemented | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | SRC-1 `memori/memory/recall.py` | none | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) | see [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal) |
| [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | other — feedback transport | implemented | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | SRC-1 `integrations/claude-code/index.ts` | none | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) | see [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery) |
| [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | content transformation | implemented | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | SRC-1 `benchmarks/02_run_benchmark.ipynb` | [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) | see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) |
| [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | check/evidence production | implemented | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | SRC-1 `benchmarks/02_run_benchmark.ipynb` | [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) | see [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) |
| [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | disposition/acceptance | implemented | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | SRC-1 `benchmarks/02_run_benchmark.ipynb` | [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | see [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) |
| [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | retention | implemented | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | SRC-1 `benchmarks/02_run_benchmark.ipynb` | [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) | see [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention) |

No route found within the inspected Python parser/scheduler/writer/recall branches for evidence-consuming truth acceptance or lifecycle integration after such acceptance. This is a bounded client finding, not an invented evaluator or system-wide absence. The countercase search found an actual lab answer evaluator, explicit deletion, and feedback transmission; these are separately assessed rather than collapsed into “no checks.” Native/TypeScript client routes and service internals retain their separate coverage limits.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-structured-memory](#epi-clm-structured-memory) | see [EPI-CLM-structured-memory](#epi-clm-structured-memory) | SRC-1 `docs/memori-cloud/concepts/advanced-augmentation.mdx`; doctrine/design | see claim | [EPI-RTE-service-import](#epi-rte-service-import), [EPI-RTE-local-retention](#epi-rte-local-retention), [EPI-RTE-recall-selection](#epi-rte-recall-selection) | none supplied | see claim | Candidate acquisition, storage and context delivery wired | [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) qualifies full-conversation/lossless reading; “facts” is not a truth certificate. |
| [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | see [EPI-CLM-benchmark-warrant](#epi-clm-benchmark-warrant) | SRC-1 `docs/memori-cloud/benchmark/results.mdx`; reported operation and design interpretation | see claim | [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer), [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging), [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics) | none supplied | see claim | Reference-based lab evaluator implemented | Reported scores do not establish extraction truth, mechanism or transfer. |
| [RT-CLM-ambient-lifecycle](runtime.md#rt-clm-ambient-lifecycle) | see [RT-CLM-ambient-lifecycle](runtime.md#rt-clm-ambient-lifecycle) | SRC-1 `integrations/claude-code/SKILL.md`; doctrine/design | see claim | [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill) | none supplied | see route | Requested conduct, invokable CLI | Instruction delivery and compliance are distinct; hosted MCP durable-only policy is not this ambient policy. |
| [EPI-CLM-agent-learning](#epi-clm-agent-learning) | see [EPI-CLM-agent-learning](#epi-clm-agent-learning) | SRC-1 `README.md`; design and reported operation | see claim | [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [RT-RTE-mcp-guidance](runtime.md#rt-rte-mcp-guidance) | none supplied | see claim | Retained content can shape future context | Improved capacity and enterprise causal attribution remain unestablished. |

## Bounded conclusion

- Memori implements acquisition and later delivery of truth-apt user/entity assertions, structured relationships and summaries. Imported source warrant is unknown; fact and summary storage plus mention linkage is not a recorded truth acceptance. See [EPI-RTE-service-import](#epi-rte-service-import), [EPI-RTE-local-retention](#epi-rte-local-retention). Process descriptions persist too, but their subsequent reader is uninspected. No observed candidate-to-check-to-accepted-ampliative-claim chain is supplied.
- Deterministic triple rendering reshapes a positive relation without adding warrant. Service-side derivation remains indeterminate: lack of entailment proof does not establish conjecture. There is no checked derivation from warranted premises demonstrated here. Structural validity, repeat counts, timestamps, embeddings and relevance rank license software handling or context selection, not truth. See [EPI-RTE-triple-shape](#epi-rte-triple-shape), [EPI-RTE-triple-rendering](#epi-rte-triple-rendering), [EPI-RTE-recall-selection](#epi-rte-recall-selection).
- Operational authority is concrete: software can schedule and retain service candidates, filter context, replay history and deliver recalled text to a provider or host agent. Its force is ranking/advisory at inference, not enforced truth-based action. Scope/horizon differ between automatic SDK injection and intentional host tools; see [RT-BAP-recalled-context](runtime.md#rt-bap-recalled-context) and [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance). OpenClaw cleanup can discard consequential qualifiers before service input; [EPI-RTE-capture-cleanup](#epi-rte-capture-cleanup) supplies a code deduction, not an observed failure.
- Entity deletion withdraws local fact/graph sources, not historical utterances or already consumed context. Feedback sends reports but no inspected local adaptation follows. See [EPI-RTE-entity-withdrawal](#epi-rte-entity-withdrawal), [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery). No direct behavior/policy update from evaluation is demonstrated in these inspected clients; server handling remains unknown.
- The lab evaluator is an important positive countercase to a blanket “no evaluation” account. It compares generated answers to dataset references and accepts parsed CORRECT labels for aggregate reporting over labelled cases. That criterion, intended use and scope are limited to benchmark scoring; raw transcript truth and memory extraction are not its check target. Labels and errors are retained, not integrated as production knowledge. See [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging), [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics), [EPI-RTE-benchmark-retention](#epi-rte-benchmark-retention).
- Model parameter fixity remains component-specific: see [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model), [RT-CMP-sentence-transformers-embedder](runtime.md#rt-cmp-sentence-transformers-embedder), [RT-CMP-tei-embeddings](runtime.md#rt-cmp-tei-embeddings), [RT-CMP-augmentation-service](runtime.md#rt-cmp-augmentation-service), and benchmark model details below. Context updates do not establish weight updates. Trace-fed retention can afford recurrent behavioral influence without proving improved capacity. Learning, reflection, autonomous theory building and self-improvement are not inferred from one another. For the README's improvement claims, later exercised causal dependence and objective-responsive update determination remain unestablished; benchmark reports do not close those links. See [EPI-CLM-agent-learning](#epi-clm-agent-learning).

## Shared records

### Components

#### EPI-CMP-benchmark-embedder
Label: Benchmark embedding model

Source-native identity: `SentenceTransformer(google/embeddinggemma-300m)`. Distinct from [RT-CMP-sentence-transformers-embedder](runtime.md#rt-cmp-sentence-transformers-embedder): lab-only embedding configuration, not the Rust production embedder. Representational form: distributed-parametric. Storage substrate: downloaded weights/cache and loaded model. Parameters changing during operation: no training operation in inspected indexing or query encoding code. Exact version pinned: no immutable weights/digest or model repository revision. Mutable endpoint resolving to another model: no remote inference endpoint here; name-based download and mutable upstream artifacts can change loaded weights. Evidence: SRC-1 `benchmarks/01_load_indexes.ipynb`, `benchmarks/02_run_benchmark.ipynb` (implementation); passage below.

#### EPI-CMP-benchmark-inference
Label: Benchmark answering and judging model

Source-native identity: configurable `OPENAI_MODEL`, default `gpt-4.1-mini`, used by `call_llm` for answering and judging in separate calls. Distinct from [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model): lab configuration/call sites, not the SQLite example's deployed invocation. Representational form: distributed-parametric. Storage substrate: external provider service. Parameters changing during operation: provider internals uninspected; notebook requests inference, not training. Exact version pinned: no immutable provider weights/version. Mutable endpoint resolving to another model: yes, alias and environment configuration can change resolution. Evidence: SRC-1 `benchmarks/02_run_benchmark.ipynb` (implementation).

>     "    model=OPENAI_MODEL,\n",
> --- `benchmarks/02_run_benchmark.ipynb`

>     "EMBED_MODEL_NAME = \"google/embeddinggemma-300m\"\n",
> --- `benchmarks/02_run_benchmark.ipynb`

### Operative objects

#### EPI-OBJ-conversation-messages
Label: Conversation messages

Source-native identity: `ConversationMessage role/content and completed-turn trace`. Representational form: Natural-language utterances and tool-result text; symbolic roles, tool IDs and arguments are separate transport/lineage fields. Storage substrate: Configured database rows or hosted conversation service; host trace transmission varies. Candidate/role: Utterances can report preferences, events and tool outcomes; storing assistant speech does not make it evidence of the reported world. Distinct from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context): captured input/history, not the formatted recall envelope. Overlaps producer/consumer routes [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation) and [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks); not a part of exactly one route. Evidence: SRC-1 `memori/memory/_writer.py` (implementation); supporting route passages below or supplied runtime passages.

#### EPI-OBJ-entity-facts
Label: Entity facts

Source-native identity: `Memories.entity.facts / memori_entity_fact.content`. Representational form: Natural-language propositions. Storage substrate: Local fact rows, with optional embedding and mention links; hosted alternative opaque. Candidate/role: Candidate user/entity assertions; source truth and extraction fidelity are unknown. Distinct from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context): retained proposition versus transient delivery envelope. Evidence: SRC-1 `memori/memory/_struct.py` (implementation); supporting route passages below or supplied runtime passages.

#### EPI-OBJ-semantic-triples
Label: Semantic triples

Source-native identity: `SemanticTriple / memori_knowledge_graph`. Representational form: Symbolic subject/predicate/object and type fields; names and predicates require semantic interpretation. Storage substrate: Local graph rows; hosted alternative opaque. Candidate/role: Relational assertions; shape validation cannot warrant the asserted relation. Distinct from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context): structured retained assertions, some also rendered as fact text. Evidence: SRC-1 `memori/memory/_struct.py` (implementation); supporting route passages below or supplied runtime passages.

#### EPI-OBJ-conversation-summary
Label: Conversation summary

Source-native identity: `Memories.conversation.summary / memori_conversation.summary`. Representational form: Natural-language summary. Storage substrate: Conversation row, overwritten by summary update; hosted alternative opaque. Candidate/role: Condensed assertions; used in subsequent service input and alongside recalled facts. Compression fidelity unestablished. Distinct from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context): stored summary supplied to extraction and recall, not its context envelope. Evidence: SRC-1 `memori/memory/augmentation/augmentations/memori/_augmentation.py` (implementation); supporting route passages below or supplied runtime passages.

#### EPI-OBJ-process-attributes
Label: Process attributes

Source-native identity: `Memories.process.attributes`. Representational form: Natural-language strings describing process/agent responsibilities. Storage substrate: Process attribute rows or opaque hosted state. Candidate/role: May contain truth-apt process descriptions or policy; individual instances unavailable, so truth-aptness is not determinable per item. Closest [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission); distinct retained part, not the route or recall envelope. Later process-attribute consumption is uninspected. Evidence: SRC-1 `memori/memory/_struct.py` (implementation); supporting route passages below or supplied runtime passages.

#### EPI-OBJ-fact-embeddings
Label: Fact embeddings

Source-native identity: `entity.fact_embeddings / content_embedding`. Representational form: Distributed-parametric dense numerical representation; fixed numerical ranking consumers. Storage substrate: Vector-valued local fact columns; lab FAISS indexes have separate input provenance described in [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer). Candidate/role: Ranking representation, not an individuated proposition or a correctness certificate. Distinct from [RT-CMP-sentence-transformers-embedder](runtime.md#rt-cmp-sentence-transformers-embedder): produced vectors, not producing weights. Native embedder and optional TEI fixity are see [RT-CMP-sentence-transformers-embedder](runtime.md#rt-cmp-sentence-transformers-embedder) and [RT-CMP-tei-embeddings](runtime.md#rt-cmp-tei-embeddings). Evidence: SRC-1 `memori/search/_core.py` (implementation); supporting route passages below or supplied runtime passages.

>         self.attributes.extend(process.get("attributes", []))
> --- `memori/memory/_struct.py`

>                 SELECT role,
>                        content
>                   FROM memori_conversation_message
>                  WHERE conversation_id = ?
>                  ORDER BY id
> --- `memori/storage/drivers/sqlite/_driver.py`

>         self.facts.extend(entity.get("facts", []))
>         self.fact_embeddings.extend(entity.get("fact_embeddings", []))
> --- `memori/memory/_struct.py`

>         self.summary = conversation.get("summary", None)
> --- `memori/memory/_struct.py`

#### EPI-OBJ-benchmark-answer
Label: Benchmark generated answer

Source-native identity: `generated_answer` with `question`, `gold_answer`, retrieved context and conversation ID. Representational form: natural-language candidate answer, with symbolic dictionary fields/identifiers. Storage substrate: transient result dictionaries and timestamped result JSON. Producer: lab answer model; consumers: judge prompt, metrics inspection and report serialization. Truth-apt content: candidate answers about past conversations, or an error string on failed generation; no actual answer instance is supplied. Distinct from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context): generated lab answer, not deployed input context. Evidence: SRC-1 `benchmarks/02_run_benchmark.ipynb` (implementation); see [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) for production passage.

#### EPI-OBJ-benchmark-verdict
Label: Benchmark verdict

Source-native identity: raw `judge_response` and parsed `label`. Representational form: natural-language judgment response and symbolic CORRECT/WRONG/None label with fixed metric-consumer rules. Storage substrate: evaluation dictionaries and saved JSON. Truth-apt content: a bounded judgment about reference-answer agreement, not a world-truth certificate. Producer: judge call/parser; consumers: metric denominator/count logic, wrong-answer inspection and report writer. These parts have separate checks and force, detailed in [EPI-RTE-benchmark-judging](#epi-rte-benchmark-judging) and [EPI-RTE-benchmark-metrics](#epi-rte-benchmark-metrics); no raw verdict instance is supplied. No counterpart in supplied runtime objects. Evidence: SRC-1 `benchmarks/02_run_benchmark.ipynb` (implementation).

>     "    return {**result, \"judge_response\": response, \"label\": label}\n",
> --- `benchmarks/02_run_benchmark.ipynb`

#### EPI-OBJ-feedback-content
Label: Feedback content

Source-native identity: CLI `flags.content` / OpenClaw tool `params.content`. Representational form: natural-language report or request, symbolic HTTP envelope. Storage substrate: transient request; remote retention unavailable. Producer: foreground agent/user; consumer: feedback service/team, not an inspected local adaptation consumer. Content may report truth-apt defects or request features; truth-aptness and warrant of each instance are not determinable without instances. Distinct from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context) and [EPI-OBJ-conversation-messages](#epi-obj-conversation-messages): explicit feedback input, not captured conversational history. Evidence: SRC-1 `integrations/claude-code/index.ts`, `integrations/openclaw/src/tools/memori-feedback.ts` (implementation); passage in [EPI-RTE-feedback-delivery](#epi-rte-feedback-delivery).

### Routes

#### EPI-RTE-service-import
Label: Service import

Part of: [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: content transformation. Content/update relation: truth-apt transformation: acquisition/import. Objects/candidates: [EPI-OBJ-entity-facts](#epi-obj-entity-facts), [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples), [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary), [EPI-OBJ-process-attributes](#epi-obj-process-attributes)

Client consumes the returned service object; external source warrant is unknown. This is acquisition at the SDK boundary, not proof that Memori produced a warranted proposition. The inaccessible extraction step may reshape, derive or conjecture; its semantic relation is indeterminate without input/output instances and server policy. The service proposes; software dispatch decides local continuation; caller may withhold capture, but no per-item human approval is established. Open application traffic, no answer oracle.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Memories object placed in augmentation context.
- Later read-back: Imported candidates can reach local writes and later recall; see local-retention and recall-selection below.
- Delegated visibility: Only the selected content and identifiers, not arbitrary host state.
- Selection predicate: Entity/config/conversation prerequisites and nonempty service response; service errors return unchanged context except quota escalation.
- Invalidation or expiry: uninspected — no universal expiry or retraction contract is established.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: No target execution; hosted internals and arbitrary configurations remain uninspected.

Evidence: SRC-1 `memori/memory/augmentation/augmentations/memori/_augmentation.py` (implementation).

>         memories = await self._process_api_response(api_response)
>
>         ctx.data["memories"] = memories
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

#### EPI-RTE-triple-shape
Label: Triple shape

Part of: [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: check/evidence production. Content/update relation: no content change. Objects/candidates: [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples)

Check target: returned triple record in the Python augmentation protocol. Evaluator: deterministic field-presence rules, not a world-truth evaluator. The program tests subject, predicate, object, names and types. Passing licenses parsing in this schema only; no evidence of entailment, sincerity or empirical corroboration. Result is consumed by the conversion/admission branches.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: None for invalid record, or constructed SemanticTriple for valid record.
- Later read-back: Valid triples may be retained and later rendered into fact context; invalid triples do not enter this parsed list.
- Delegated visibility: Only the selected content and identifiers, not arbitrary host state.
- Selection predicate: Each semantic_triples/triples entry passed to _parse_semantic_triple.
- Invalidation or expiry: inapplicable — instantaneous structural test, not a retained decision record.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: No target execution; hosted internals and arbitrary configurations remain uninspected.

Evidence: SRC-1 `memori/memory/_struct.py` (implementation).

>         if not all([subject_name, subject_type, object_name, object_type]):
>             return None
> --- `memori/memory/_struct.py`

#### EPI-RTE-triple-rendering
Label: Triple rendering

Part of: [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: content transformation. Content/update relation: truth-apt transformation: non-ampliative reshaping. Objects/candidates: [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples), [EPI-OBJ-entity-facts](#epi-obj-entity-facts)

Within the simple positive triple encoding, rendering re-expresses fields; it does not independently infer a new relationship. Concrete deduction from source, not execution: {subject:{name:"Ada"}, predicate:"uses", object:{name:"SQLite"}} yields "Ada uses SQLite" in build_fact_text_from_triple_entry. Nonempty content overrides field rendering. Names containing negation, qualifiers or incompatible schema conventions do not gain a checked formal interpretation from concatenation. No warranted premises or checked inference domain establishes an entailed new claim here.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Existing nonempty content, rendered fact string, or None.
- Later read-back: Rendered text is appended to entity facts and can reach subsequent recall.
- Delegated visibility: Only the selected content and identifiers, not arbitrary host state.
- Selection predicate: Content takes priority; otherwise subject name, predicate and object name must exist.
- Invalidation or expiry: inapplicable — transient conversion; resulting fact retention has separate lifecycle.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: No target execution; hosted internals and arbitrary configurations remain uninspected.

Evidence: SRC-1 `memori/memory/_struct.py` (implementation).

>     return f"{subject_name} {predicate} {object_name}"
> --- `memori/memory/_struct.py`

#### EPI-RTE-memory-scheduling
Label: Memory scheduling

Part of: [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: disposition/acceptance. Content/update relation: no content change. Objects/candidates: [EPI-OBJ-entity-facts](#epi-obj-entity-facts), [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples), [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary), [EPI-OBJ-process-attributes](#epi-obj-process-attributes)

Disposition target: parsed service candidates for local write scheduling, not truth acceptance. Software schedules nonempty lists/summary and valid identifiers; service proposal policy is opaque. No named evidence-consuming truth criterion, intended epistemic use/scope or item-level human approval appears in this inspected scheduling code. Content can be operationally admitted before acceptance. Guidance consists of returned service fields; rollback is operational error handling, not a semantic withdrawal decision. Open traffic; no answer oracle.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Queued method-path write operations.
- Later read-back: Scheduled candidates may persist through writer/driver and be used without a subsequent epistemic check.
- Delegated visibility: Only the selected content and identifiers, not arbitrary host state.
- Selection predicate: Entity/process/conversation IDs and nonempty parsed content; missing embeddings can trigger additional triple-derived fact rendering.
- Invalidation or expiry: Failures may skip writes; no semantic rollback contract in these schedulers.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: The service may perform additional checks; absence of a client truth gate is not an end-to-end absence.

Evidence: SRC-1 `memori/memory/augmentation/augmentations/memori/_augmentation.py` (implementation).

>         if memories.conversation.summary:
>             ctx.add_write(
>                 "conversation.update",
>                 ctx.payload.conversation_id,
>                 memories.conversation.summary,
>             )
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

#### EPI-RTE-local-retention
Label: Local retention

Part of: [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: retention. Content/update relation: no content change. Objects/candidates: [EPI-OBJ-entity-facts](#epi-obj-entity-facts), [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples), [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary), [EPI-OBJ-process-attributes](#epi-obj-process-attributes)

Python write tasks resolve driver methods; SQLite stores facts and triples, increments duplicate occurrence counts, overwrites summary and links fact mentions to conversations. Counts and timestamps track recurrence/freshness, not corroboration. SQLite get_facts_by_ids joins summaries through mention links, providing a lineage association but not provenance to a checked original claim. This is retention and organization before established acceptance, not lifecycle integration as defined by this analysis. Software admits writes; caller supplies attribution/configuration; no per-item human review. Driver commits inside methods limit the meaning of outer batch rollback.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Driver completion/commit, not an epistemic decision. DbWriterRuntime attempts adapter rollback on batch exception.
- Later read-back: Facts and joined summaries reach retrieval; summary also becomes next augmentation input. Process-attribute later reader is uninspected.
- Delegated visibility: Writer receives selected content and database identifiers. get_facts_by_ids returns fact content, dates and linked summaries, not source message quotations.
- Selection predicate: WriteTask method-path dispatch and per-driver nonempty/identifier conditions.
- Invalidation or expiry: Repeated fact text increments count; summary replacement updates a row. No inspected semantic contradiction retraction. Explicit entity withdrawal is separate.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: SRC-1 also memori/memory/augmentation/_db_writer.py and augmentation handler; detailed retention conclusion is SQLite/Python-specific, not all drivers or cloud.

Evidence: SRC-1 `memori/storage/drivers/sqlite/_driver.py`, `memori/memory/augmentation/_db_writer.py` (implementation).

>                 SELECT m.fact_id,
>                        c.summary AS content,
>                        COALESCE(c.date_updated, c.date_created) AS date_created
>                   FROM memori_entity_fact_mention m
>                   JOIN memori_conversation c
>                     ON c.id = m.conversation_id
> --- `memori/storage/drivers/sqlite/_driver.py`

>                         for task in tasks:
>                             task.execute(driver)
>
>                         if adapter:
>                             adapter.flush()
>                             adapter.commit()
> --- `memori/memory/augmentation/_db_writer.py`

>                 ON CONFLICT(entity_id, uniq) DO UPDATE SET
>                     num_times = num_times + 1,
>                     date_last_time = datetime('now')
> --- `memori/storage/drivers/sqlite/_driver.py`

#### EPI-RTE-recall-selection
Label: Recall selection

Part of: [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation)

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: operational admission/selection/consumption. Content/update relation: no content change. Objects/candidates: [EPI-OBJ-entity-facts](#epi-obj-entity-facts), [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary), [EPI-OBJ-fact-embeddings](#epi-obj-fact-embeddings)

Target: relevance of retained facts to a query in Python search/injection. Evaluator: dense similarities plus lexical weighting, top-limit and configured threshold; plain string cloud facts score 1.0. Selection grants context access, not epistemic endorsement. Summaries are scoped to selected facts and duplicate summary text is removed. Facts become natural-language provider input under relevance guidance; the model receives strings, not a proof or a forced action. Owner is deterministic SDK code; provider interprets. Immediate-inference advisory/ranking force; recurrent horizon depends on later retrieval.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Provider request kwargs containing selected facts and summaries, or unchanged request.
- Later read-back: Retained candidates enter later registered invocations; delivery is wired, changed provider behavior is not observed.
- Delegated visibility: Provider receives formatted selected fact/summary text and date labels; no automatic full evidential lineage.
- Selection predicate: Query/entity/storage gates, selected recall backend, ranking/limit/threshold.
- Invalidation or expiry: Changing session affects history; dropping a below-threshold fact withholds this delivery, not durable rejection.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: SRC-1 memori/search/_core.py and memori/memory/recall.py also inspected. Native ranking internals, cloud scoring and all framework consumers are not exhaustively inspected.

Evidence: SRC-1 `memori/llm/pipelines/recall_injection.py` (implementation).

>     relevant_facts = [
>         f
>         for f in facts
>         if _score_for_recall_threshold(f) >= invoke.config.recall_relevance_threshold
>     ]
> --- `memori/llm/pipelines/recall_injection.py`

>         rank_score_map = {
>             fid: (w_cos * float(similarities_map.get(fid, 0.0)))
>             + (w_lex * float(lex_scores.get(fid, 0.0)))
>             for fid in candidate_ids
>         }
> --- `memori/search/_core.py`

> def _score_for_recall_threshold(fact: RecallFact) -> float:
>     if isinstance(fact, str):
>         return 1.0
> --- `memori/memory/recall.py`

#### EPI-RTE-capture-cleanup
Label: Capture cleanup

Part of: [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks)

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: content transformation. Content/update relation: truth-apt transformation: indeterminate. Objects/candidates: [EPI-OBJ-conversation-messages](#epi-obj-conversation-messages)

OpenClaw cleaning is not guaranteed to preserve assertion meaning. Concrete deduction: user string "Do not run this:
```sh
rm -rf data
```
Run only in a disposable sandbox." becomes "Run only in a disposable sandbox." because the last fence truncates everything before it. The client loses prohibition and command context before parseUserMessage/buildAugmentationPayload forwards the text. For a message ending at the closing fence, cleaned text is empty and capture may be skipped. This falsifies universal lossless-capture interpretation; it does not establish any particular false memory or ampliative inference. Possible relations include lossy compression, altered assertion and no truth-apt content; supplied run instances are missing.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Cleaned text; turn parser can skip missing text or substitute synthetic assistant response for tool-only turns.
- Later read-back: Transformed user/assistant text and cleaned tool-result text are sent to service; later derived memory is service-dependent.
- Delegated visibility: Only the selected content and identifiers, not arbitrary host state.
- Selection predicate: Successful host event, bounded recent-message slice and complete non-system turn; cleanText also used on tool results.
- Invalidation or expiry: inapplicable — source omission occurs before submission; no inverse/reconstruction branch inspected.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: SRC-1 integrations/openclaw/src/handlers/augmentation.ts inspected through payload submission. Deduction uses implementation only; no execution or universal host-format assumption.

Evidence: SRC-1 `integrations/openclaw/src/sanitizer.ts` (implementation).

>   if (message.includes('```')) {
>     const lastFenceIndex = message.lastIndexOf('```');
>     if (lastFenceIndex !== -1) {
>       message = message.substring(lastFenceIndex + 3).trim();
>     }
>   }
> --- `integrations/openclaw/src/sanitizer.ts`

> function parseUserMessage(msg: OpenClawMessage): IntegrationMessage | null {
>   const cleanedContent = cleanText(msg.content);
>   return cleanedContent
>     ? { role: msg.role as Role, content: cleanedContent, type: extractContentType(msg.content) }
>     : null;
> }
> --- `integrations/openclaw/src/handlers/augmentation.ts`

#### EPI-RTE-entity-withdrawal
Label: Entity withdrawal

Distinct from [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation): explicit removal operation, not model-call capture/context delivery.

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: operational admission/selection/consumption. Content/update relation: no content change. Objects/candidates: [EPI-OBJ-entity-facts](#epi-obj-entity-facts), [EPI-OBJ-semantic-triples](#epi-obj-semantic-triples)

Caller-requested BYODB withdrawal, not truth-directed rejection. API validates mode/identifier then Recall invokes graph deletion and fact deletion. SQLite deletes graph edges and orphan nodes, then fact rows; it preserves conversation records and summaries. Consequently it can remove a later fact-retrieval source but cannot revoke already delivered model context, erase the conversation, or prevent later service re-derivation. Human versus computational caller is unknown; no answer oracle, experiment or truth criterion. Separate commits do not establish atomic global deletion.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: None from public delete_entity_memories; mode errors otherwise.
- Later read-back: Affected fact/graph rows are removed from subsequent local reads; preserved conversation history may still be replayed.
- Delegated visibility: Configured entity identity resolved into local storage identifier.
- Selection predicate: Public API requires BYODB; storage and resolved entity must exist.
- Invalidation or expiry: Deletion takes effect at database operation boundary; no cloud/global purge or already-injected-context rollback.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: SRC-1 memori/__init__.py and SQLite driver deletion branches inspected; other drivers, caches and concurrent augmentation races not fully traced.

Evidence: SRC-1 `memori/memory/recall.py` (implementation).

>         self.config.storage.driver.knowledge_graph.delete_by_entity(entity_id)
>         self.config.storage.driver.entity_fact.delete_by_entity(entity_id)
> --- `memori/memory/recall.py`

#### EPI-RTE-feedback-delivery
Label: Feedback delivery

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: other — feedback transport. Content/update relation: truth-apt transformation: acquisition/import for factual reports; non-truth-apt requests are transported without semantic judgment. Objects/candidates: [EPI-OBJ-feedback-content](#epi-obj-feedback-content)

Feedback may report a bug, missing memory or useful recall. Claude CLI posts content to /agent/feedback; OpenClaw tool sends agentFeedback and returns success/error. This acquires reports for the team/service with unknown source warrant. No inspected local consumer revises a memory, prompt, ranker or model from the report. Do not equate transmission with content-directed criticism or operative self-improvement. Foreground agent/user proposes content; transport checks are not truth checks; service disposition opaque.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Success after awaited POST, or CLI failure/tool error.
- Later read-back: uninspected — no returned retained feedback reader or local adaptation loop established.
- Delegated visibility: Feedback text and authenticated service namespace.
- Selection predicate: CLI content/API-key requirements or registered authenticated host tool.
- Invalidation or expiry: uninspected — remote feedback retention and handling unavailable.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: Distinct from [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill) and [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks): omitted feedback operation spanning multiple exposed surfaces, not another declaration of their lifecycle containers. SRC-1 integrations/openclaw/src/tools/memori-feedback.ts inspected.

Evidence: SRC-1 `integrations/claude-code/index.ts` (implementation).

>   await post(`${BASE_URL}/agent/feedback`, { content: flags.content });
>   return { success: true };
> --- `integrations/claude-code/index.ts`

#### EPI-RTE-benchmark-answer
Label: Benchmark answer

No counterpart after comparison with supplied runtime routes: these are lab evaluator operations, not deployed memory admission or invocation.

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: content transformation. Content/update relation: truth-apt transformation: indeterminate. Inputs: [EPI-OBJ-entity-facts](#epi-obj-entity-facts), [EPI-OBJ-conversation-summary](#epi-obj-conversation-summary). Candidate: [EPI-OBJ-benchmark-answer](#epi-obj-benchmark-answer).

A separate lab pipeline imports pre-augmented memory JSON, concatenates content/context for embedding, builds per-conversation indexes, retrieves via FAISS/BM25 RRF, and asks an LLM for answers using selected memories/summaries. Truth-apt answer candidates are generated, but no frozen candidate instances establish entailment or non-entailment; do not classify all answers as ampliative. Temporal calculation is requested by prompt, not a checked derivation proof. Answer and judge use the same configurable OPENAI_MODEL, by default gpt-4.1-mini, in separate calls.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Answer result dict with candidate text, retrieved content/count and question/gold metadata; errors produce ERROR text.
- Later read-back: Candidate results feed judging and saved evaluation payload, not a local product-memory update.
- Delegated visibility: Answer model receives formatted retrieved memories/summaries and question, not raw transcript or gold answer in its answer prompt.
- Selection predicate: Available per-conversation index; question categories 1–4; top-K hybrid retrieval.
- Invalidation or expiry: inapplicable — candidate lab result, not an automatically admitted production memory.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: SRC-1 benchmarks/01_load_indexes.ipynb and 02_run_benchmark.ipynb read as JSON source. Remote memory data, QA data and weight artifacts are not frozen; no stored execution output found in these notebook cells.

Evidence: SRC-1 `benchmarks/02_run_benchmark.ipynb` (implementation).

>     "        answer = await call_llm(prompt)\n",
> --- `benchmarks/02_run_benchmark.ipynb`

#### EPI-RTE-benchmark-judging
Label: Benchmark judging

No counterpart after comparison with supplied runtime routes: these are lab evaluator operations, not deployed memory admission or invocation.

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: check/evidence production. Content/update relation: no content change. Objects/candidates: lab generated_answer/label records produced by [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) (natural-language answer/judge response plus symbolic parsed label, transient dicts and saved JSON).

Check target: candidate QA answer against supplied gold answer, LoCoMo categories 1–4. Evaluator: LLM call instructed to be generous about matching topic/date, then JSON/fallback substring label parser. The expected answer is the dataset answer (adversarial_answer branch exists but category 5 is excluded by default). The model sees question, gold and generated text, not original transcript or extraction lineage. This is a lab answer oracle with limited reference scope, not an extraction-acceptance gate. Example source deduction: non-JSON "INCORRECT" contains CORRECT and no WRONG, so fallback returns CORRECT; ambiguous both-token replies return None. This parser countercase bounds grading reliability without demonstrating its occurrence.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: CORRECT, WRONG or None retained with judge_response.
- Later read-back: Labels are consumed by metrics/report retention, not inspected live-memory admission.
- Delegated visibility: Judge receives QA triple; source evidence and retrieved context are not passed to this prompt.
- Selection predicate: Every generated answer result gets a judge call; parser accepts exact JSON labels or exclusive substring matches.
- Invalidation or expiry: inapplicable — no durable verdict revision procedure implemented in notebook.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: Model judgment and lenient gold matching do not certify world truth, extraction fidelity, transfer or production-loop mechanism. Same-model answering/judging and unpinned external data limit independence/reproducibility.

Evidence: SRC-1 `benchmarks/02_run_benchmark.ipynb` (implementation).

>     "    has_correct = \"CORRECT\" in upper\n",
>     "    has_wrong = \"WRONG\" in upper\n",
>     "    if has_correct and not has_wrong:\n",
>     "        return \"CORRECT\"\n",
> --- `benchmarks/02_run_benchmark.ipynb`

#### EPI-RTE-benchmark-metrics
Label: Benchmark metrics

No counterpart after comparison with supplied runtime routes: these are lab evaluator operations, not deployed memory admission or invocation.

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: disposition/acceptance. Content/update relation: no content change. Objects/candidates: lab generated_answer/label records produced by [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) (natural-language answer/judge response plus symbolic parsed label, transient dicts and saved JSON).

Software accepts parsed CORRECT labels as success for reporting accuracy over successfully labelled QA results, not for general epistemic reliance or product-memory integration. Criterion: lenient reference-answer match as interpreted by judge; intended use: lab aggregate/category/conversation scoring; scope: available-index category 1–4 questions. Missing indexes omit questions before generation; None verdicts are excluded from accuracy denominator and separately reported as failures. No human per-answer approval. This does not establish produced accepted ampliative knowledge because candidate novelty, reliable source warrant and that intended use are not established.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: Accuracy and failure-rate aggregates and printed tables.
- Later read-back: Metrics enter saved report payload, not SDK ranking or model training.
- Delegated visibility: Aggregate code receives parsed labels, generated-answer records and errors.
- Selection predicate: Only non-null labels enter accuracy; category and conversation groupings inherit generation coverage.
- Invalidation or expiry: inapplicable — no automatic threshold-triggered revision or deployment gate.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: A reporting disposition is operative at the measurement consumer only. No implemented component intervention or equivalent baseline answer-evaluation branch establishes causal extraction benefit.

Evidence: SRC-1 `benchmarks/02_run_benchmark.ipynb` (implementation).

>     "accuracy = n_correct / n_evaluated if n_evaluated > 0 else 0\n",
> --- `benchmarks/02_run_benchmark.ipynb`

#### EPI-RTE-benchmark-retention
Label: Benchmark retention

No counterpart after comparison with supplied runtime routes: these are lab evaluator operations, not deployed memory admission or invocation.

- implementation conclusion status: wired
- operation conclusion status: uninspected

Function: retention. Content/update relation: no content change. Objects/candidates: lab generated_answer/label records produced by [EPI-RTE-benchmark-answer](#epi-rte-benchmark-answer) (natural-language answer/judge response plus symbolic parsed label, transient dicts and saved JSON).

Notebook saves configuration, aggregate summary, details, labels, raw judge responses and error list to timestamped JSON. This preserves evaluable lab records; it is not lifecycle integration of accepted production knowledge. Wrong-answer inspection prints examples for a possible human reader; it does not implement criticism-driven memory/policy replacement.

Endpoints/progression, owner, context/state/action effects, check/disposition domain, operational versus epistemic authority and behavioral-authority path are established above for this function; the concrete return, later consumer, channel, gating and horizon are:

- Immediate return: results_gemma/eval_<timestamp>.json and printed location.
- Later read-back: uninspected — notebook provides output for later human comparison but no automatic reload/update consumer of prior result files.
- Delegated visibility: Local filesystem gets details, summary and errors.
- Selection predicate: Running metrics/save cell after evaluation.
- Invalidation or expiry: uninspected — timestamped output has no implemented semantic expiry/rollback policy.
- Activation or effect: Implementation is wired; actual invocation, behavioral dependence and benefit are unobserved.
- Evidence limits: Retained-file writing is implementation evidence only; no such run artifact is supplied here.

Evidence: SRC-1 `benchmarks/02_run_benchmark.ipynb` (implementation).

>     "    json.dump(save_payload, f, indent=2, ensure_ascii=False)\n",
> --- `benchmarks/02_run_benchmark.ipynb`

### Claims

#### EPI-CLM-structured-memory
Label: Structured memory and automatic recall

Claimed operation: full conversation/trace becomes facts, preferences, skills, triples and searchable memory, later automatically injected into context. Source: SRC-1 `docs/memori-cloud/concepts/advanced-augmentation.mdx` (doctrine/design). Closest supplied [RT-CLM-ambient-lifecycle](runtime.md#rt-clm-ambient-lifecycle) governs Claude foreground conduct, not this SDK/service derivation claim; distinct identity. Client import/storage/recall implementations support transport and operational use, not “objective information” as checked truth. The Python summary-conditioned selection and generic stream exception in [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission), [RT-RTE-stream-exhaustion](runtime.md#rt-rte-stream-exhaustion), plus OpenClaw cleanup, defeat an unconditional full-content/all-path interpretation. No observed-run or causal support is supplied. Hosted acceptance remains unknown; not a system-wide absence.

> 1. Reads the full conversation (user messages and AI responses)
> 2. Identifies facts, preferences, skills, and attributes
> 3. Extracts semantic triples (subject-predicate-object relationships)
> 4. Generates vector embeddings for semantic search
> 5. Stores everything in your managed memory space
> --- `docs/memori-cloud/concepts/advanced-augmentation.mdx`

#### EPI-CLM-benchmark-warrant
Label: Benchmark accuracy and structure warrant

Claimed operation: reported 87.0% accuracy supports isolating high-signal knowledge via triples/summaries, with reduced context cost. Source: SRC-1 `docs/memori-cloud/benchmark/results.mdx`, `README.md` (reported operation plus design interpretation). No counterpart among supplied runtime claims. Actual notebook implementation supports lab answering, judging, reporting and retention. The notebook consumes pre-augmented external data rather than reconstructing extraction, does not independently vary structure/summary components, and token baseline is a length comparison rather than a full-context answer experiment. Reported cross-system results are not a supplied causal experiment; frozen raw run details/references and dataset identities are missing. Thus even successful QA would not establish the producing extraction mechanism, replay safety, transfer or component effect. README says roughly 67% reduction versus Zep; result table 721 versus 3,911 implies roughly 82%, also stated in results prose. This public reporting inconsistency does not alter client routes and prevents treating both reduction figures as the same measurement.

> Among retrieval-based systems, Memori achieved a leading overall score of 87.0%, successfully outperforming Zep (79.09%), LangMem (78.05%), and Mem0 (62.47%). This validates the assumption that by structuring unstructured chat logs into semantic triples and summaries, Memori effectively isolates high-signal knowledge. This structured memory design significantly narrows the gap to the Full-Context ceiling while keeping context windows highly manageable and operational token costs low.
> --- `docs/memori-cloud/benchmark/results.mdx`

> Compared with other retrieval-based memory systems, Memori outperformed Zep, LangMem, and Mem0 while reducing prompt size by roughly **67% vs. Zep** and lowering context cost by more than **36x vs. full-context prompting**.
> --- `README.md`

#### EPI-CLM-agent-learning
Label: Agent learning and run-over-run improvement

Claimed operation: agents learn coding patterns/preferences/conventions through memory; enterprise traces stop redundant discoveries and improve run over run. Source: SRC-1 `README.md` (design and reported operation). Distinct from supplied ambient-lifecycle policy claim. Bounded target: Memori-mediated retention/context organization across later sessions; objective: reduced redundant discovery/cost or improved later task capacity, independently specifiable from storing a record. SDK/host wiring affords state-fed future context, not exercised improvement. Learning improved-capacity evidence is uninspected; reflection's self-representation and two causal directions are unestablished here; autonomy of internal theory criticism is unestablished independently. No theory-builder status follows merely from stored rules/skills or feedback reports: no concrete formulated theory/criticism/revision iteration is supplied. For self-improvement attribution, objective-bearing evidence shaping update determination is opaque; storage can change retained organization and delivery is wired, but later exercised behavioral dependence and causal attribution are missing. This neither proves nor disproves an opaque service learning mechanism. No observed-run or causal experiment is supplied for the enterprise anecdote.

> Works for solo developers and teams. Your agent learns coding patterns, reviewer preferences, and project conventions over time. For teams, that means shared context that new engineers pick up on day one instead of absorbing tribal knowledge over months.
> --- `README.md`

> By integrating Memori's agent-native memory layer in a secure private VPC, the platform captured execution traces to stop redundant discoveries and improve run over run.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; use [RT-BAP-recalled-context](runtime.md#rt-bap-recalled-context) and [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance). Distinct lab consumers and withdrawal/feedback force are specified in their route records; they do not inherit model-context authority.
