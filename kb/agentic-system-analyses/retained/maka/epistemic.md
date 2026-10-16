---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Apache Maka epistemic routes: user-evidence memory acceptance, goal judging, context authority and benchmark verification at the frozen commit."
run-id: AAS-2026-10-15-maka-4a8b73e41579-01
reviewed-boundary: "1751c399239b0f6b717e98e2a5e2b875c3dd11ce"
---

# Apache Maka epistemic report

## Source-and-claim boundary

The analysis asks how Maka turns incoming assertions, conversation history and task evidence into later reliance or control. Scope and exclusions are those of the [boundary and Source register](boundary.md#source-register), SRC-1. All new reads below are implementation or doctrine/design at that same commit. There are no observed runs or causal experiments. Accessible source does not make provider parameters, human approval behavior or external verifier truth accessible.

The consequential public claim is [RT-CLM-task-runtime](runtime.md#rt-clm-task-runtime); an additional evaluator-design claim is [EPI-CLM-goal-judge](#epi-clm-goal-judge). Neither is an observed result. The runtime account is provisional, not an inspection ceiling: goal evaluation and canonical memory acceptance supply important countercases to a blanket “no evaluator” conclusion.

| Entry point / operation | Source path | Coverage and prevented conclusion |
|---|---|---|
| CLI dispatch: run, eval, ACP, TUI, session import/export, plugin and Host administration | SRC-1 `packages/cli/src/cli-core.ts` dispatch search | Direct search establishes alternate surfaces; CLI run detailed account supplied by [RT-RTE-cli-turn](runtime.md#rt-rte-cli-turn). Import/export, ACP and update bodies uninspected: no complete semantic-lineage or change-admission negative. |
| Main model/tool execution, Code Mode, child/Graph, plugin executor/LLM, scheduled/recovered work | SRC-1 runtime paths named in supplied records | Supplied [RT-RTE-tool-settlement](runtime.md#rt-rte-tool-settlement), [RT-RTE-child-graph](runtime.md#rt-rte-child-graph), [RT-RTE-executor-plugin](runtime.md#rt-rte-executor-plugin), [RT-RTE-durable-wake](runtime.md#rt-rte-durable-wake). Not independently reread here; answer truth and opaque executor effects unresolved. |
| Compaction, source coverage and history replacement | SRC-1 `packages/runtime/src/ai-sdk-compaction.ts` | Supplied [RT-RTE-context-projection](runtime.md#rt-rte-context-projection); structural coverage is not semantic preservation. Native provider state and archive reload remain unresolved. |
| memory_remember, memory_extract and incidental/compaction extraction | SRC-1 `packages/runtime/src/memory-extraction.ts`, `packages/runtime/src/memory-extraction-proposal.ts` | Direct proposal/prompt/admission reads and extraction canonicalization-to-commit reads; [EPI-RTE-memory-evidence](#epi-rte-memory-evidence) through [EPI-RTE-memory-commit](#epi-rte-memory-commit). Trigger discovery by search, not exhaustive trigger/lane inspection. |
| Extraction storage and fact recall; recall material/open/widen tools and recall.query | SRC-1 `packages/storage/src/sqlite-long-term-memory-store.ts`, `packages/runtime-host/src/server/execution-composition.ts`, `packages/runtime/src/recall-tools.ts` | Storage commit/lifecycle searches, direct searchFacts wiring and recall result projection. [EPI-RTE-memory-commit](#epi-rte-memory-commit). Full ranking, lifecycle filtering, material fetching/import and external-session synchronization uninspected: no retrieval completeness, deletion propagation or source-warrant preservation guarantee. |
| memory.query/mutate: propose, remember, approve, reject, set_status, reset, restore, replacement upload | SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts`, `packages/core/src/local-memory.ts` | Direct semantic mutation and read-projection reads; replacement upload dispatch inspected, full replacement validation not traced. [EPI-RTE-local-memory-use](#epi-rte-local-memory-use). No universal human-review or semantic-acceptance conclusion. |
| Goal completion hook, evaluator and next-turn selection | SRC-1 `packages/runtime/src/goal-evaluator.ts`, `packages/runtime/src/goal-continuation.ts`, `packages/runtime-host/src/server/goal-coordinator.ts` | Direct evaluator, completion consumer and recent-context projection reads. [EPI-RTE-goal-judge](#epi-rte-goal-judge), [EPI-RTE-goal-selection](#epi-rte-goal-selection). Exact provider wiring and complete recovery uninspected. |
| Eval verification and result consumer | SRC-1 `packages/eval/src/harness-executor.ts`, `packages/eval/src/runner.ts` | Direct reward import/status and result merge reads. [EPI-RTE-eval-verification](#epi-rte-eval-verification). External verifier bodies, task oracles and experiments uninspected: no comparative benchmark or causal conclusion. |
| Daily review, assistant memory-network indexes and proactive Matters | SRC-1 `packages/runtime-host/src/server/daily-review-coordinator.ts`, `packages/runtime-host/src/assistant/` | Located but uninspected, not excluded. Cannot settle their semantic evaluation, revision, lifecycle integration or behavior-adaptation routes. |
| Native/client capabilities, MCP, computer use, Feishu source plugin, workspace/skill guidance and plugin installation | SRC-1 `apps/`, `native/`, `scripts/plugins/`, `packages/mcp/`, `skills/` and runtime prompt/plugin paths | Supplied runtime covers composition/admission seams, not all bodies. [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission), [RT-BAP-composed-prompt](runtime.md#rt-bap-composed-prompt). Prevents exhaustive system-wide evaluator, provenance, adaptation or acceptance negatives. |

No new repository identity is introduced. Available unread files are inspection limits, not access gaps. Missing execution evidence prevents assertions that any judged candidate was actually accepted, any prompt changed behavior, any goal was achieved, or any benchmark improved. Distributed-parametric limits remain those of [RT-CMP-ai-model](runtime.md#rt-cmp-ai-model): inference wiring does not pin exact weights or expose training, and an endpoint alias may change resolution.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-item](#epi-obj-memory-item) | see record | see record | SRC-1 `packages/runtime/src/memory-extraction-proposal.ts` | see record |
| [EPI-OBJ-goal-evaluation](#epi-obj-goal-evaluation) | see record | see record | SRC-1 `packages/runtime/src/goal-evaluator.ts` | see record |
| [EPI-OBJ-local-memory](#epi-obj-local-memory) | see record | see record | SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts` | see record |
| [EPI-OBJ-verifier-result](#epi-obj-verifier-result) | see record | see record | SRC-1 `packages/eval/src/harness-executor.ts` | see record |
| [RT-OBJ-run-composition](runtime.md#rt-obj-run-composition) | see record | see record | SRC-1 `packages/runtime-host/src/server/execution-model-composition.ts` | see record |
| [RT-CMP-ai-model](runtime.md#rt-cmp-ai-model) | not determinable at parameter-content level; see record | see record | SRC-1 `packages/runtime-host/src/server/execution-model-composition.ts` | see record |

Tool results, imported conversation and generated answers may contain truth-apt assertions, but their actual propositions and warrant cannot be individuated without a concrete input/output instance. General inference capability is not a particular accepted ampliative claim. Compaction summaries and opaque executor/native-provider state remain separate from extracted memory; see [RT-RTE-context-projection](runtime.md#rt-rte-context-projection) and [RT-RTE-executor-plugin](runtime.md#rt-rte-executor-plugin).

## Authority-route ledger

Route ID: [EPI-RTE-memory-evidence](#epi-rte-memory-evidence)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-item](#epi-obj-memory-item)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Evaluator/condition and domain: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Activation and timing: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Possible or observed result: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Implemented force: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Epistemic authority and scope: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Operational authority: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Behavioral-authority path: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Evidence source ID and local anchor: SRC-1 `packages/runtime/src/memory-extraction-proposal.ts`.
Claim IDs: none.
Mismatch marker: none; limits see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).
Gap/limit: see [EPI-RTE-memory-evidence](#epi-rte-memory-evidence).

Route ID: [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-item](#epi-obj-memory-item)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Evaluator/condition and domain: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Activation and timing: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Possible or observed result: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Implemented force: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Epistemic authority and scope: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Operational authority: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Behavioral-authority path: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Evidence source ID and local anchor: SRC-1 `packages/runtime/src/memory-extraction.ts`.
Claim IDs: none.
Mismatch marker: none; limits see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).
Gap/limit: see [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize).

Route ID: [EPI-RTE-memory-disposition](#epi-rte-memory-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-item](#epi-obj-memory-item)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Evaluator/condition and domain: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Activation and timing: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Possible or observed result: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Implemented force: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Epistemic authority and scope: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Operational authority: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Behavioral-authority path: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Evidence source ID and local anchor: SRC-1 `packages/runtime/src/memory-extraction.ts`.
Claim IDs: none.
Mismatch marker: none; limits see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).
Gap/limit: see [EPI-RTE-memory-disposition](#epi-rte-memory-disposition).

Route ID: [EPI-RTE-memory-commit](#epi-rte-memory-commit)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-item](#epi-obj-memory-item)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Evaluator/condition and domain: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Activation and timing: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Possible or observed result: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Implemented force: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Epistemic authority and scope: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Operational authority: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Behavioral-authority path: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Evidence source ID and local anchor: SRC-1 `packages/runtime/src/memory-extraction.ts`.
Claim IDs: none.
Mismatch marker: none; limits see [EPI-RTE-memory-commit](#epi-rte-memory-commit).
Gap/limit: see [EPI-RTE-memory-commit](#epi-rte-memory-commit).

Route ID: [EPI-RTE-goal-judge](#epi-rte-goal-judge)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-goal-evaluation](#epi-obj-goal-evaluation)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Evaluator/condition and domain: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Activation and timing: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Possible or observed result: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Implemented force: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Epistemic authority and scope: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Operational authority: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Behavioral-authority path: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Evidence source ID and local anchor: SRC-1 `packages/runtime/src/goal-evaluator.ts`.
Claim IDs: [EPI-CLM-goal-judge](#epi-clm-goal-judge).
Mismatch marker: none; limits see [EPI-RTE-goal-judge](#epi-rte-goal-judge).
Gap/limit: see [EPI-RTE-goal-judge](#epi-rte-goal-judge).

Route ID: [EPI-RTE-goal-selection](#epi-rte-goal-selection)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-goal-evaluation](#epi-obj-goal-evaluation)
Content/update relation: non-truth-apt policy/content update: goal control state and next-turn steering
Transition or check target: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Evaluator/condition and domain: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Activation and timing: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Possible or observed result: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Implemented force: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Epistemic authority and scope: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Operational authority: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Behavioral-authority path: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Evidence source ID and local anchor: SRC-1 `packages/runtime/src/goal-continuation.ts`.
Claim IDs: [EPI-CLM-goal-judge](#epi-clm-goal-judge).
Mismatch marker: none; limits see [EPI-RTE-goal-selection](#epi-rte-goal-selection).
Gap/limit: see [EPI-RTE-goal-selection](#epi-rte-goal-selection).

Route ID: [EPI-RTE-local-memory-use](#epi-rte-local-memory-use)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-local-memory](#epi-obj-local-memory)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Evaluator/condition and domain: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Activation and timing: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Possible or observed result: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Implemented force: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Epistemic authority and scope: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Operational authority: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Behavioral-authority path: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Evidence source ID and local anchor: SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts`.
Claim IDs: none.
Mismatch marker: none; limits see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).
Gap/limit: see [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).

Route ID: [EPI-RTE-eval-verification](#epi-rte-eval-verification)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-verifier-result](#epi-obj-verifier-result)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Evaluator/condition and domain: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Activation and timing: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Possible or observed result: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Implemented force: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Epistemic authority and scope: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Operational authority: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Behavioral-authority path: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Evidence source ID and local anchor: SRC-1 `packages/eval/src/harness-executor.ts`.
Claim IDs: [RT-CLM-task-runtime](runtime.md#rt-clm-task-runtime).
Mismatch marker: none; limits see [EPI-RTE-eval-verification](#epi-rte-eval-verification).
Gap/limit: see [EPI-RTE-eval-verification](#epi-rte-eval-verification).

The supplied routes remain material without duplicate declarations. [RT-RTE-tool-settlement](runtime.md#rt-rte-tool-settlement) supplies operational admission (implemented; no content change in the dispatch check), not task-truth acceptance. [RT-RTE-context-projection](runtime.md#rt-rte-context-projection) supplies implemented retention and content transformation: semantic preservation of model summaries is indeterminate, while coverage checks concern identity. [RT-BAP-composed-prompt](runtime.md#rt-bap-composed-prompt) supplies advisory content consumption; [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) supplies operational configuration admission. Those records own their fields. No independent lifecycle-integration route beyond retention/use was established in the new reads: the uninspected assistant and review operations prevent a system-complete negative.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-task-runtime](runtime.md#rt-clm-task-runtime) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-tool-settlement](runtime.md#rt-rte-tool-settlement), [RT-RTE-context-projection](runtime.md#rt-rte-context-projection), [RT-RTE-durable-wake](runtime.md#rt-rte-durable-wake), [EPI-RTE-eval-verification](#epi-rte-eval-verification) | none supplied | No experiments inspected; external task verifiers and remote execution prevent independent validity/attribution | Ledger-backed execution and score import implemented in bounded paths | No measured comparative advantage or universal ledger completeness established |
| [EPI-CLM-goal-judge](#epi-clm-goal-judge) | see record | SRC-1 `packages/runtime/src/goal-evaluator.ts`; doctrine/design | see record | [EPI-RTE-goal-judge](#epi-rte-goal-judge), [EPI-RTE-goal-selection](#epi-rte-goal-selection) | none supplied | Separate call is not independent evidence; no intervention/comparison | Separate tool-free judging call and consequential control are implemented | Claimed prevention of premature completion is not established |

## Bounded conclusion

Maka has more than a terminal-answer label. Its extraction path performs a fallible evidence-consuming acceptance decision: a model is asked whether quoted user evidence fully supports a durable assertion, software rejects malformed/unsupported-reference outputs, and surviving canonical items become commit candidates. Intended use is later global/workspace memory recall, not certification of external fact truth. This is independent of the Local Memory approval queue: caller-supplied approval metadata authorizes prompt use but does not demonstrate semantic review. See [EPI-RTE-memory-canonicalize](#epi-rte-memory-canonicalize), [EPI-RTE-memory-disposition](#epi-rte-memory-disposition), [EPI-RTE-local-memory-use](#epi-rte-local-memory-use).

User assertions are acquired, and their source links can survive extraction persistence. But the recall fact projection supplies content/kind/time without full citation or canonicalization rationale. Source warrant is therefore not completely delivered at that consumer. Model extraction may reshape or introduce unsupported meaning; implementation alone cannot decide entailment for every output. No warranted novel derivation or accepted ampliative proposition is established. Retention, indexing and recall are not additional truth acceptance or lifecycle integration. See [EPI-RTE-memory-commit](#epi-rte-memory-commit).

Goal evaluation has operational force beyond advice. Parsed met/impossible flags can stop the goal loop, waiting changes continuation, and the reason steers a later turn. That judge sees a lossy text projection, not independently re-executed tools. Timeout/error permits continuation but does not count as real progress or stall evidence. These distinctions defeat both “no evaluator” and “goal achieved means verified task success.” See [EPI-RTE-goal-judge](#epi-rte-goal-judge) and [EPI-RTE-goal-selection](#epi-rte-goal-selection).

A separate benchmark route imports external verifier scores and reports infrastructure/subject classification. A completed verification is not necessarily a positive reward. It cannot establish model reasoning correctness, mechanism transfer or causal component benefit. See [EPI-RTE-eval-verification](#epi-rte-eval-verification).

Local Memory archive/status and policy changes can withdraw content from later prompt projections; extraction rejection prevents selected writes; stale goal checkpoints discard judgments. These are different withdrawal domains, not a universal belief-retraction mechanism. Provider-internal state, full recall lifecycle propagation, assistant indexes/Matters and daily-review routes remain unresolved. Learning benefit, formulated-theory criticism/iteration, reflection and exercised self-improvement are not inferred from memory retention, model judging or plugin installability. The goal path establishes evidence-responsive continuation control, not an evaluated improvement to the runtime's own organization. No single epistemic verdict follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-memory-item
Label: Memory Item

Source-native MemoryProposalItem and canonical Memory Item payloads contain durable user facts/preferences/identity/project knowledge, or plans/predictions, in natural-language content. Kind, temporal/scope tags, keys and evidence references are symbolic indexing/admission fields. Proposal/canonicalization objects reside transiently in extraction state; admitted MemoryItemWrite values enter the long-term SQLite store. SRC-1 `packages/runtime/src/memory-extraction-proposal.ts`, `packages/runtime/src/memory-extraction.ts`, `packages/storage/src/sqlite-long-term-memory-store.ts`. No counterpart after comparison with runtime objects: RunComposition is composition metadata, not this item. Actual proposition truth and semantic preservation are not determinable without an output instance.

> content: z.string().min(1).max(2_000),
> --- `packages/runtime/src/memory-extraction-proposal.ts`

> keys: z.array(memoryKeySchema).min(1).max(16),
> evidence: z.array(memoryEvidenceCitationSchema).min(1).max(8),
> --- `packages/runtime/src/memory-extraction-proposal.ts`

#### EPI-OBJ-goal-evaluation
Label: GoalEvaluation

Symbolic met/impossible/progress/waiting/evaluatorFailed flags and natural-language reason assert goal satisfaction or progress over a condition and recent text. Transient model response is parsed into coordinator state; a pending continuation can retain reason-derived steering and checkpoint/control identity through durability callbacks. SRC-1 `packages/runtime/src/goal-evaluator.ts`, `packages/runtime/src/goal-continuation.ts`. Distinct from all supplied runtime objects: this judges outcome/control rather than composition identity. It does not contain direct environment measurements.

> met: parsed.met === true,
> impossible: parsed.impossible === true,
> progress: parsed.progress === true,
> waiting: parsed.waiting === true,
> evaluatorFailed: false,
> --- `packages/runtime/src/goal-evaluator.ts`

#### EPI-OBJ-local-memory
Label: Local Memory bundle entries

Durable bundle Markdown contains natural-language title/content and symbolic status/scope/lifecycle metadata. Pending proposals and active entries differ in admission and consumers. Only selected active promptContent reaches the model projection. Store abstraction is InteractiveMemoryBundleStoreWriter; physical bundle layout was not traced here. SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts`, `packages/core/src/local-memory.ts`. This is a source part feeding the supplied prompt-authority path, not a duplicate of RunComposition or extracted Memory Item.

> const visibleEntries = parsed.activeEntries.filter(
>   (entry) => entry.scope !== 'session' || (sessionId.length > 0 && entry.sessionId === sessionId),
> );
> --- `packages/core/src/local-memory.ts`

#### EPI-OBJ-verifier-result
Label: ExecutorVerification

Symbolic score/status plus artifact references and failure text are acquired from external trial result.json and audit evidence, then assembled in runner result state. Trial JSON is a file substrate; later report persistence is uninspected. A configured reward key defines the imported outcome variable, not universal task truth. SRC-1 `packages/eval/src/harness-executor.ts`, `packages/eval/src/runner.ts`. No counterpart after comparison with supplied runtime objects or claims; a public benchmark claim is not a verifier result.

> const score = result.verifier_result?.rewards?.[rewardKey(cell)] ?? null;
> --- `packages/eval/src/harness-executor.ts`

### Routes

#### EPI-RTE-memory-evidence
Label: Memory evidence admission

Unlike the broader tool-settlement route, this checks long-term-memory evidence; no counterpart after comparison with supplied runtime records.

Endpoints and progression: Candidate citations, schema, secret policy, keys and temporal bounds; target domain is extraction input, not external fact truth. Before canonicalization and again before writes, for requested or incidental extraction. Owner/evaluator: Software checks sourceRef membership, normalized quote substring, nonempty cited events and valid bounds. No reference-answer oracle. Model proposes; code can veto requested work or drop incidental items.
Result: Eligible candidate, evidence/admission failure, secret-policy no-op or omitted incidental item.
Implemented force: Enforcing admission to the canonicalization/write path.
Epistemic authority and scope: Citation occurrence and admissibility only; occurrence does not entail the proposed assertion.
Operational authority: Blocks invalid candidates before persistence; does not authorize tools or establish real-world truth.
Behavioral-authority path: Extraction pipeline; admission result; enforcing; this extraction operation.
Evidence: SRC-1 `packages/runtime/src/memory-extraction-proposal.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: Validated candidate fields or rejection reason.
- Later read-back: inapplicable — this check itself retains no content; the separate commit route retains admitted outputs.
- Delegated visibility: Canonicalizer receives validated user quotes, not tool/assistant evidence; interpretation context may be supplied separately.
- Selection predicate: Exact evidence references, normalized quote membership, valid item fields and policy.
- Invalidation or expiry: Failed admission discards incidental items or fails requested extraction; sensitive requested content clears writes.
- Activation or effect: Implemented filtering; operation unobserved.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete implementation deduction, without execution: a citation quote `  Alice   ` normalizes to `Alice`; a source providerVisibleTexts value `Alice` passes substring membership and the four-character minimum, while `Alicia` fails it. This proves only lexical presence, not entailment of arbitrary item content. This countercase blocks attributing a semantic entailment oracle to deterministic admission. NFC/trim and minute flooring reshape text/time non-ampliatively in their limited domains; e.g. minuteTimestamp(123456) yields 120000, not a finer event-time claim.

> const quote = normalizeEvidenceText(citation.quote);
> --- `packages/runtime/src/memory-extraction-proposal.ts`

> Array.from(quote).length < 4 ||
> !evidenceContainsQuote(source, quote)
> --- `packages/runtime/src/memory-extraction-proposal.ts`

> return (source.providerVisibleTexts ?? [source.text]).some((text) => text.includes(quote));
> --- `packages/runtime/src/memory-extraction-proposal.ts`

> return value.normalize('NFC').replace(/\s+/g, ' ').trim();
> --- `packages/runtime/src/memory-extraction-proposal.ts`

> return Math.floor(value / 60_000) * 60_000;
> --- `packages/runtime/src/memory-extraction-proposal.ts`

#### EPI-RTE-memory-canonicalize
Label: Memory canonicalization

No counterpart in runtime: this is an evidence-consuming memory evaluator, not ordinary main-loop generation or compaction.

Endpoints and progression: Whether user evidence fully supports a durable self-contained assertion for later memory reuse. After deterministic admission, within bounded model-call budget. Owner/evaluator: Isolated model judge using user-authored quoted evidence and optional interpretation context. No tools or expected-answer oracle; model may accept/rewrite or reject. Software validates result identities and schema.
Result: Accepted canonical item or rejection; missing/duplicate/extra candidate IDs prevent successful result processing.
Implemented force: Model recommendation becomes write eligibility only through the separate disposition route.
Epistemic authority and scope: Fallible evidence-consuming semantic support assessment over supplied user excerpts; not independent validation of the user's statements.
Operational authority: Provides a disposition input, not direct execution authority.
Behavioral-authority path: Extraction disposition code; structured results; permissive pending revalidation; current operation.
Evidence: SRC-1 `packages/runtime/src/memory-extraction.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: Per-candidate accepted item or rejected status.
- Later read-back: inapplicable — evaluation returns to the current extraction operation; commit owns later retention.
- Delegated visibility: Only selected user evidence and bounded interpretation context enter the isolated judge.
- Selection predicate: Candidates surviving deterministic policy/evidence admission.
- Invalidation or expiry: Call budget exhaustion, blocked policy or invalid result set can stop extraction.
- Activation or effect: Wired model evaluation; no observed judgments or accuracy comparison.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The prompted transformation aims at non-ampliative canonicalization; there is no concrete model output to check whether that aim is met. Thus relation is indeterminate rather than conjecture merely because entailment is unproven. The model sees quoted evidence, not the candidate's original proposed wording in the constructed candidate payload, so this is evidence-based reconstruction as well as judging.

> 'Accept only when the evidence itself fully supports one durable, self-contained assertion. Otherwise return status=rejected.',
> --- `packages/runtime/src/memory-extraction-proposal.ts`

> 'For accepted results, rewrite concisely without adding facts, values, names, dates, or relationships absent from the evidence.',
> --- `packages/runtime/src/memory-extraction-proposal.ts`

> if (!results || results.length !== candidates.length) {
>   canonicalFailureClass = 'schema';
>   continue;
> }
> --- `packages/runtime/src/memory-extraction.ts`

#### EPI-RTE-memory-disposition
Label: Memory item disposition

Distinct disposition following the memory canonicalizer, not the evaluator itself or the retained item.

Endpoints and progression: Canonical candidate acceptance for long-term-memory persistence and later recall, scoped global or workspace as assigned. After canonicalizer returns one result per candidate, before atomic commit. Owner/evaluator: Model supplies accepted/rejected result against evidence-support criterion; software reattaches original citations, rechecks policy and evidence, then selects writes. No per-item human approval is required by this branch; a remember request is not approval of generated wording.
Result: Write selected; incidental rejection omitted; requested rejection fails operation; sensitive no-op clears all writes.
Implemented force: Enforcing write-list selection.
Epistemic authority and scope: Implemented acceptance decision consumes user evidence through a fallible model criterion. It licenses reuse as a supported user assertion, not independently established fact; accepted ampliative production is not demonstrated.
Operational authority: Permits selected content to enter memory commit; rejects other candidates.
Behavioral-authority path: Commit builder; selected writes array; enforcing; operation and later recall if commit succeeds.
Evidence: SRC-1 `packages/runtime/src/memory-extraction.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: Writes array and requested-item indexes or counted failure/no-op.
- Later read-back: inapplicable — selection itself has no later read-back; selected writes feed the retention route.
- Delegated visibility: Only surviving canonical items cross into persistence.
- Selection predicate: Canonical acceptance plus repeated deterministic admission.
- Invalidation or expiry: Policy recheck before commit can block; a rejected explicit item fails rather than silently producing success.
- Activation or effect: Write eligibility is implemented, not evidence that accepted items are true.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (result.status === 'rejected') {
>   if (candidate.requested) {
>     return { kind: 'counted_failure', failureClass: 'requested_admission' };
>   }
>   continue;
> }
> --- `packages/runtime/src/memory-extraction.ts`

> const canonicalProposal: MemoryProposalItem = {
>   ...result.item,
>   evidence: candidate.proposal.evidence,
> };
> --- `packages/runtime/src/memory-extraction.ts`

> writes.push(memoryItemWrite(snapshot, admission.fields, candidate.requested));
> --- `packages/runtime/src/memory-extraction.ts`

#### EPI-RTE-memory-commit
Label: Memory extraction commit

No runtime counterpart: its context-projection record is a different retained representation and admission path.

Endpoints and progression: Admitted writes, original cited-event lineage, coverage cursor and extraction receipt. After item disposition, including intentionally empty no-op operations. Owner/evaluator: Allowed-session recheck and commit port; SQLite extraction uses operation/request/cursor consistency. Software owns commit; semantic decision occurred upstream. No new answer oracle.
Result: Committed receipt and advanced cursor, or blocked/failed persistence.
Implemented force: Enforcing storage handoff; commit success is not a new semantic acceptance.
Epistemic authority and scope: Retains upstream support judgment and lineage rather than adding truth warrant.
Operational authority: Makes stored items available to subsequent memory search.
Behavioral-authority path: Long-term-memory store then recall dependencies; durable rows; permissive later retrieval; across invocations.
Evidence: SRC-1 `packages/runtime/src/memory-extraction.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: Commit receipt and processed cursor.
- Later read-back: Recall searchFacts later reads long-term-memory content, kind and observedAt using prefix keys and optional workspace key.
- Delegated visibility: Foreground recall gets projected facts, not all extraction citations or canonicalizer rationale.
- Selection predicate: Allowed snapshot and surviving write list; operation and cursor guards in storage.
- Invalidation or expiry: Commit failure prevents successful receipt; full lifecycle-mutation and archive search behavior are uninspected.
- Activation or effect: Persistence and read wiring inspected; no observed stored extraction instance.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Retention is distinct from lifecycle integration: this write alone does not demonstrate new evidence connections or changed organization after acceptance. Recall's projection can lose explicit warrant details even when storage retains them.

> if (!(await this.allowed(snapshot.sessionId))) return { kind: 'blocked' };
> const committed = await this.ports.commit({
> --- `packages/runtime/src/memory-extraction.ts`

> facts: result.facts.map((fact) => ({
>   content: fact.content,
>   kind: fact.kind,
>   observed_at: fact.observedAt,
> })),
> --- `packages/runtime/src/recall-tools.ts`

> const records = await longTermMemoryStore.searchByKeys({
>   terms,
>   match: 'prefix',
>   ...(workspaceKey ? { workspaceKey } : {}),
>   limit,
> });
> --- `packages/runtime-host/src/server/execution-composition.ts`

#### EPI-RTE-goal-judge
Label: Goal evaluation

Runtime omitted this material evaluator. It is distinct from RT-RTE-durable-wake: it judges goal continuation, not scheduled-fire identity.

Endpoints and progression: Whether a configured goal condition is met, impossible, progressing or waiting, judged from recent conversation text. After a completed turn for an active/current goal; bounded timeout and cancellation. Owner/evaluator: Tool-free session-model call with a conservative evidence/scope prompt; parser checks booleans, not actual goal achievement. No reference answer oracle. User/model goal authorship is not determined here.
Result: Four flags and reason, or evaluatorFailed neutral fallback on timeout/error/invalid output.
Implemented force: Flags are inputs to the separate continuation selector, not proof of outcome.
Epistemic authority and scope: Fallible text-only judgment; receives last six nonempty user/assistant messages with long-message opening/end excerpts, not direct file checks or full tool results.
Operational authority: No direct permission change; supplies goal-control evidence.
Behavioral-authority path: Goal continuation coordinator; parsed flags/reason; permissive input to selector; next goal transition.
Evidence: SRC-1 `packages/runtime/src/goal-evaluator.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: Parsed GoalEvaluation.
- Later read-back: inapplicable — judgment returns to current completion; selector retains pending continuation when needed.
- Delegated visibility: Isolated model receives condition and projected recent conversation, not tool execution capability.
- Selection predicate: Active goal, completion event and current checkpoint.
- Invalidation or expiry: Abort/timeout returns evaluatorFailed; stale checkpoint discards returned judgment.
- Activation or effect: Implemented judge; reliability and successful goal recognition unobserved.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The input projection is a consequential qualification: recentContext filters to user/assistant rows, skips empty assistant text, keeps six and excerpts long messages. A goal judgment can therefore rest on assistant reports rather than independently checked tool evidence. Distinct model calls do not provide independent evidence sources.

> .slice(-6)
> .map(({ type, text }) => `[${type}]: ${evaluatorExcerpt(text)}`)
> .join('\n');
> --- `packages/runtime-host/src/server/goal-coordinator.ts`

> - met: true ONLY if there is clear, concrete evidence the condition is fully satisfied. Match verification scope to the requirement scope — do not accept a narrower substitute.
> --- `packages/runtime/src/goal-evaluator.ts`

> reason: 'Evaluator timed out (continuing)',
> --- `packages/runtime/src/goal-evaluator.ts`

#### EPI-RTE-goal-selection
Label: Goal continuation selection

No counterpart: not the scheduler admission in RT-RTE-durable-wake nor generic main-loop termination.

Endpoints and progression: Goal terminal status, wait/continue choice, progress accounting and pending continuation. After goal evaluation, before admission of another goal turn. Owner/evaluator: Coordinator interprets model flags after currency checks; GoalManager settles state. Model judges, software decides operative state. No independent answer oracle. Failures do not count as real no-progress judgments.
Result: achieved/impossible stops; waiting records wait; otherwise continuation with progress only if evaluation did not fail.
Implemented force: Enforcing state transition plus advisory reason in later model prompt.
Epistemic authority and scope: Operational achieved label does not independently warrant goal truth or mechanism correctness.
Operational authority: Stops goal loop, waits or prepares another turn; goal/task gates still govern admission.
Behavioral-authority path: GoalManager and continuation admission; flags and durable pending prompt; enforcing control/advisory steering; successive goal turns.
Evidence: SRC-1 `packages/runtime/src/goal-continuation.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: Settled GoalState and possibly lane intent/pending prompt.
- Later read-back: Pending continuation is recorded durably with checkpoint/control lease and consumed by later admission machinery; full recovery rehydration is uninspected.
- Delegated visibility: Next turn receives built continuation prompt, not a grant of new tool capability.
- Selection predicate: Current lane/checkpoint, active/waiting state and later task-gate admission.
- Invalidation or expiry: Stale goal/lane rejects; terminal/other stopped states clear intent; cancelled evaluation cannot settle a replaced checkpoint.
- Activation or effect: Wired evidence-responsive control, not evidence of improved future capacity.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operational terminal classification is not epistemic acceptance of an external fact against independently checked evidence. Goal state and steering are policy updates, separately from the judge's truth-apt flags. No theory formulation/criticism loop is established by this state machine.

> verdict: evaluation.met ? 'achieved' : 'impossible',
> --- `packages/runtime/src/goal-continuation.ts`

> ...(!evaluation.evaluatorFailed ? { madeProgress: evaluation.progress } : {}),
> --- `packages/runtime/src/goal-continuation.ts`

> await this.deps.durability.recordPendingContinuation({
>   checkpoint: lane.intent.checkpoint,
>   controlLease,
>   prompt: pendingPrompt,
>   triggeringTurnId: turnId,
> });
> --- `packages/runtime/src/goal-continuation.ts`

#### EPI-RTE-local-memory-use
Label: Local Memory mutation and use

Distinct retained source feeding RT-BAP-composed-prompt, rather than a duplicate of that overall prompt-authority path.

Endpoints and progression: Active Local Memory entries admitted to a session prompt; pending, archived or incompatible-session entries do not enter this projection. Prompt composition after durable bundle mutations; separately from extracted long-term-memory recall. Owner/evaluator: Software parses active entries, checks privacy/memory/agent-read policy and session scope, redacts and caps prompt body. Named approve/manual-save surfaces record user approval metadata, but caller identity and actual human evidence review are uninspected.
Result: Body or no body; archived entries remain outside active projection. Restore/reset/reject are exposed mutation branches.
Implemented force: Enforcing prompt selection; selected text remains advisory to model.
Epistemic authority and scope: Approval metadata authorizes use, not evidence-consuming semantic acceptance under a named truth criterion.
Operational authority: Changes model-visible context; no safety/permission override authorized by composer wording.
Behavioral-authority path: Interactive composer and selected model; untrusted Local Memory prompt section; advisory; session/turn composition and later rereads.
Evidence: SRC-1 `packages/runtime-host/src/server/memory-coordinator.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: Policy-filtered body with bundle/memory revisions.
- Later read-back: Later prompt composition reads durable bundle; status changes, reset or replacement can withdraw prior entries from prompt delivery.
- Delegated visibility: Child sessions do not implicitly inherit this material, per runtime record.
- Selection predicate: Enabled policy, document state, active status and matching session scope; bounded content length.
- Invalidation or expiry: Incognito, disabled read, safe mode, missing body, archive and session mismatch withhold projection; backups can restore content.
- Activation or effect: Visible withdrawal from projection is implemented; model obedience and factual validation are not established.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mutation is caller-proposed, revision guarded and software committed: propose writes pending; approve moves a named proposal; remember appends an entry; reject removes pending eligibility; set_status changes lifecycle; reset and restore supply recovery. These are separate from the prompt-consumption function in this row, described here to bound what its source's approval metadata means. The full caller UI/authentication is not inspected. There is no evidence-consuming truth criterion in the inspected mutation branch. Storage failure/unknown commit can poison activation and request drain rather than silently reporting success.

> case 'approve': {
>   const proposal = findLocalMemoryEntryDraft(pending, input.proposalId);
>   if (!proposal) return rejected('not_found');
> --- `packages/runtime-host/src/server/memory-coordinator.ts`

> if (parsed.safeMode || parsed.activeEntries.length === 0) return undefined;
> --- `packages/core/src/local-memory.ts`

> if (body.length <= LOCAL_MEMORY_PROMPT_MAX_CHARS) return body;
> const boundarySafe = truncateUtf16Safe(body, LOCAL_MEMORY_PROMPT_MAX_CHARS);
> --- `packages/core/src/local-memory.ts`

#### EPI-RTE-eval-verification
Label: Eval verification results

Countercase to treating CLI terminal output as the only task evaluator; distinct from all supplied runtime routes.

Endpoints and progression: Benchmark task outcome under the configured external verifier/reward key, separately from process completion. After subject execution unless cancelled or already uncertain/infra-failed. Owner/evaluator: External verifier supplies rewards; Maka reads result.json, classifies subject exception and egress-audit failure. Verifier implementation and task-specific oracle are uninspected; source warrant unknown, not inherited from a successful process.
Result: Score (possibly zero), completed/subject_failed/infra_failed; missing reward or audit failure is infra_failed.
Implemented force: Enforcing result classification and report input, not foreground model admission.
Epistemic authority and scope: Supports an imported benchmark score only under external verifier domain/validity; no causal component effect or general task-success guarantee.
Operational authority: Runner merges verified score/status with usage, cost, duration and artifacts; does not automatically revise agent machinery.
Behavioral-authority path: Eval runner; verification object; enforcing reporting classification; this trial/result.
Evidence: SRC-1 `packages/eval/src/harness-executor.ts`; implementation unless a prompt/comment is identified as doctrine/design. Architectural wiring is not observed operation.

- Immediate return: ExecutorVerification score, status, failureReason and artifacts.
- Later read-back: uninspected — runner result assembly is inspected, later durable aggregation and benchmark publication are not.
- Delegated visibility: inapplicable — this verifier-result path does not delegate work to an agent.
- Selection predicate: Configured reward key, trial result path and audit evidence; runner avoids verifying uncertain subject states.
- Invalidation or expiry: Infrastructure/audit failures block valid completed classification; no score threshold is enforced by verificationStatus.
- Activation or effect: No supplied run or controlled experiment; completed can coexist with score zero.
- Evidence limits: No target execution or model outcomes supplied; source establishes route logic only. Relevant coverage limits remain in the boundary table.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The reward is imported, not produced by Maka's local status classifier. Zero is present and hence can yield completed: process/verification completion and task score remain separate. An official-verifier label does not inspect the verifier's oracle validity. Runner consumes the result but no automatic agent-policy update follows in the inspected result merge.

> if (auditFailure !== null || score === null) return 'infra_failed';
> return subjectException ? 'subject_failed' : 'completed';
> --- `packages/eval/src/harness-executor.ts`

> const verified = decodeVerification(await verify());
> return {
>   score: verified.score,
> --- `packages/eval/src/runner.ts`

### Claims

#### EPI-CLM-goal-judge
Label: External goal judge

SRC-1 `packages/runtime/src/goal-evaluator.ts`, doctrine/design comment, claims a separate judge prevents rationalized premature completion. This is narrower than the public task-runtime claim but consequential because a met flag stops goal continuation. No counterpart after comparison with [RT-CLM-task-runtime](runtime.md#rt-clm-task-runtime): the latter claims product task measures and event authority, not evaluator independence. Separate call wiring supports a bounded architectural reading; correctness and comparative prevention remain unobserved.

> The working model never judges its own completion (unlike Codex): keeping the
> --- `packages/runtime/src/goal-evaluator.ts`

> judge external prevents the agent from rationalizing itself into a premature
> --- `packages/runtime/src/goal-evaluator.ts`

> "done", which is Codex's documented failure mode.
> --- `packages/runtime/src/goal-evaluator.ts`

Claim conclusion status: claimed

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
