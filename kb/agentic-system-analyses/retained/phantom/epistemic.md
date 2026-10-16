---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Phantom epistemic routes: imported assertions, heuristic fact authority, reflection admission and later reliance."
run-id: AAS-2026-10-15-phantom-cc566f03ac40-01
reviewed-boundary: "f8c7ab42d885936ee54abc785528000260f4acc5"
---

# Phantom epistemic report

## Source-and-claim boundary

The question is how Phantom turns conversations and task results into content available for later reliance, and what its checks license. The functional scope and exclusions are those of the [boundary and Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design only. No supplied trace establishes exercised acceptance, a particular learned output, successful recall, or improvement. External model parameters, SDK internals and deployed storage remain outside inspection; these gaps prevent weight-learning, dependency-enforcement and durability conclusions, respectively.

The runtime is a provisional route account, not the inspection limit. Its foreground, alternate ingress, instruction and executable-extension routes are retained. Added direct reads at the same pin establish vector-memory generation, similarity checking, validity withdrawal, prompt delivery and deletion. Direct correction reads of SRC-1 `src/evolution/reflection-subprocess.ts`, `src/evolution/engine.ts` and `src/evolution/versioning.ts` confirm that compact is a per-file change type, not an admitted top-level status: committed compactions return changed ok and take the ordinary live-config refresh. The corrected supplied [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) retains the supporting passages and downstream loader/formatter limits. The reflection teaching text is a model instruction, not evidence that a model complied. Claims are [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker) and [EPI-CLM-session-learning](#epi-clm-session-learning).

| Entry point or operation | Source path, SRC-1 | Coverage and basis | Remaining limit |
|---|---|---|---|
| CLI dispatch/start | `src/cli/index.ts` | Direct dispatch read; startup supplied by [RT-RTE-channel-work](runtime.md#rt-rte-channel-work) and boundary | Doctor/init/token/status implementations not assessed for health/provisioning truth claims; no CLI-complete epistemic negative |
| Channel response and post-response learning | `src/index.ts`, `src/memory/consolidation.ts` | Supplied [RT-RTE-channel-work](runtime.md#rt-rte-channel-work); direct consolidation read and caller outcome search; [EPI-RTE-fact-extraction](#epi-rte-fact-extraction) | Outcome label is not verified task success |
| Browser chat/continuity | `src/chat/writer.ts`, `src/chat/continuity-context.ts`, `src/agent/murph-context.ts` | Supplied [RT-RTE-durable-chat](runtime.md#rt-rte-durable-chat), [RT-RTE-chat-context](runtime.md#rt-rte-chat-context) | Transcript-search redaction/ranking implementation uninspected; no full recovery-fidelity claim |
| Scheduled/HTTP/MCP direct work | `src/scheduler/executor.ts`, `src/core/server.ts`, `src/mcp/tools-swe.ts` | Supplied [RT-RTE-direct-work](runtime.md#rt-rte-direct-work); direct review/PR/CI handler reads; [EPI-RTE-review-request](#epi-rte-review-request) | Arbitrary tool-mediated checking remains task-dependent |
| Gate, queue, reflection | `src/evolution/gate.ts`, `src/evolution/gate-prompt.ts`, `src/evolution/subprocess-prompt.ts`, `src/evolution/invariant-check.ts` | Direct gate/prompt/full invariant reads; supplied [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) for snapshot, branches and live consumer | No generated reflection artifacts or observed comparison; no established semantic acceptance from version commits |
| Vector store admission/withdrawal | `src/memory/consolidation.ts`, `src/shared/patterns.ts`, `src/memory/semantic.ts` | Direct full reads; [EPI-RTE-fact-extraction](#epi-rte-fact-extraction), [EPI-RTE-fact-retention](#epi-rte-fact-retention), [EPI-RTE-similarity-check](#epi-rte-similarity-check), [EPI-RTE-validity-change](#epi-rte-validity-change) | Embeddings and remote search results unobserved |
| Prompt and tool retrieval | `src/memory/context-builder.ts`, `src/memory/ranking.ts`, `src/memory/procedural.ts`, `src/agent/in-process-reflective-tools.ts`, `src/mcp/tools-universal.ts` | Direct builder/ranking/procedure/reflective-tool reads; external-tool search, supplemented by runtime prompt findings; [EPI-RTE-memory-delivery](#epi-rte-memory-delivery) | Full external search-core body and episodic retrieval body uninspected; no exhaustive selection-equivalence claim |
| Dashboard deletion | `src/ui/api/memory.ts`, `src/memory/system.ts`, `src/memory/semantic.ts`, `src/memory/procedural.ts` | Direct API deletion and store reads; [EPI-RTE-memory-delete](#epi-rte-memory-delete) | No erasure propagation into already delivered context or derived files established |
| Foreground edits, registered tools, hooks and operator configuration | `src/agent/hooks.ts`, `src/mcp/dynamic-handlers.ts`, `src/ui/api/phantom-config.ts` | Supplied [RT-RTE-dynamic-tools](runtime.md#rt-rte-dynamic-tools), [RT-RTE-operator-config](runtime.md#rt-rte-operator-config), [RT-BAP-handler-execution](runtime.md#rt-bap-handler-execution) | Shape/permission checks do not establish content truth; no system-wide common admission gate |
| SDK/model internals and other shipped skills/evaluators | `skills-builtin/`, `e2e/`, `src/agent/agent-sdk.ts` | SDK gap in boundary; available skill/evaluation bodies largely uninspected in this member | Prevents system-complete negative about all checking or theory production; test existence is not a passing run |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-semantic-facts](#epi-obj-semantic-facts) | see record | see record | SRC-1 `src/memory/semantic.ts` | see record |
| [EPI-OBJ-episodes](#epi-obj-episodes) | see record | see record | SRC-1 `src/memory/consolidation.ts` | see record |
| [EPI-OBJ-procedures](#epi-obj-procedures) | see record | see record | SRC-1 `src/memory/procedural.ts` | see record |
| [RT-OBJ-chat-context](runtime.md#rt-obj-chat-context) | see record | see record | SRC-1 `src/chat/continuity-context.ts` | see record |
| [RT-OBJ-session-store](runtime.md#rt-obj-session-store) | see record | see record | SRC-1 `src/agent/session-store.ts` | see record |
| [RT-OBJ-dynamic-tools](runtime.md#rt-obj-dynamic-tools) | see record | see record | SRC-1 `src/mcp/dynamic-tools.ts` | see record |
| [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) | see record | see record | SRC-1 `src/evolution/subprocess-prompt.ts` | Retained file content is heterogeneous; no observed candidate instance supplied |
| [RT-CMP-main-model](runtime.md#rt-cmp-main-model), [RT-CMP-judge-model](runtime.md#rt-cmp-judge-model), [RT-CMP-reflection-model](runtime.md#rt-cmp-reflection-model), [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client) | see records | see records | SRC-1 `src/config/providers.ts` | Opaque parameters and unpinned endpoints; no inspected weight-update route |

## Authority-route ledger

All statuses below describe architecture, not observed activation. Each cited record owns the detailed target, evaluator, result, force, authority path and limits. Split rows distinguish checking from disposition and retention from acceptance. A row's relation is an assessment of that function only, not of every output of the containing route.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-channel-work](runtime.md#rt-rte-channel-work) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/agent/runtime.ts` | [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker) | none | No candidate output to classify as entailed or ampliative |
| [RT-RTE-durable-chat](runtime.md#rt-rte-durable-chat) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/chat/writer.ts` | none | none | Persistence is not acceptance |
| [RT-RTE-chat-context](runtime.md#rt-rte-chat-context) | operational admission/selection/consumption | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/chat/continuity-context.ts` | none | none | Bounded artifact selection, not comprehensive recall |
| [EPI-RTE-fact-extraction](#epi-rte-fact-extraction) | content transformation | implemented | [EPI-OBJ-semantic-facts](#epi-obj-semantic-facts), [EPI-OBJ-episodes](#epi-obj-episodes) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/memory/consolidation.ts` | [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker) | Predicate assignment can exceed quotation | see record |
| [EPI-RTE-fact-retention](#epi-rte-fact-retention) | retention | implemented | [EPI-OBJ-semantic-facts](#epi-obj-semantic-facts) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/memory/semantic.ts` | none | none | Upsert does not record truth acceptance |
| [EPI-RTE-similarity-check](#epi-rte-similarity-check) | check/evidence production | implemented | [EPI-OBJ-semantic-facts](#epi-obj-semantic-facts) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/memory/semantic.ts` | none | Similarity is not logical inconsistency | see record |
| [EPI-RTE-validity-change](#epi-rte-validity-change) | disposition/acceptance | implemented | [EPI-OBJ-semantic-facts](#epi-obj-semantic-facts) | non-truth-apt policy/content update: recall eligibility metadata | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/memory/semantic.ts` | none | Withdrawal, not evidence-consuming acceptance | see record |
| [EPI-RTE-memory-delivery](#epi-rte-memory-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-semantic-facts](#epi-obj-semantic-facts), [EPI-OBJ-episodes](#epi-obj-episodes), [EPI-OBJ-procedures](#epi-obj-procedures) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/memory/context-builder.ts` | [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker) | Known Facts label exceeds independently checked warrant | see record |
| [EPI-RTE-memory-delete](#epi-rte-memory-delete) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/ui/api/memory.ts` | none | none | Deletion is not revision of downstream copies |
| [RT-RTE-judge-call](runtime.md#rt-rte-judge-call) | check/evidence production | implemented | see record | non-truth-apt policy/content update: learning-worthiness vote | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/evolution/gate-prompt.ts` | [EPI-CLM-session-learning](#epi-clm-session-learning) | Vote does not verify retained propositions | Gate receives sampled/truncated messages and unavailable reaction/block signals |
| [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) | operational admission/selection/consumption | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/evolution/gate.ts` | [EPI-CLM-session-learning](#epi-clm-session-learning) | Failsafe enqueues without a favorable judgment | Gate selection only |
| [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/evolution/subprocess-prompt.ts` | [EPI-CLM-session-learning](#epi-clm-session-learning) | none | Compaction, inferred preferences and direct imports require output-level classification |
| [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/evolution/invariant-check.ts` | [EPI-CLM-session-learning](#epi-clm-session-learning) | Byte/pattern domain, not truth or value alignment | Snapshot and skip limits in record |
| [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/evolution/reflection-subprocess.ts` | [EPI-CLM-session-learning](#epi-clm-session-learning) | Operational file admission is not proposition acceptance | Soft warnings do not veto |
| [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/evolution/engine.ts` | [EPI-CLM-session-learning](#epi-clm-session-learning) | none | Changed ok compactions commit and take the ordinary live-config refresh; downstream delivery remains loader/formatter-dependent |
| [EPI-RTE-review-request](#epi-rte-review-request) | check/evidence production | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/mcp/tools-swe.ts` | none | none | Advisory review, no merge/admission consumer established |
| [RT-RTE-dynamic-tools](runtime.md#rt-rte-dynamic-tools) | operational admission/selection/consumption | implemented | see record | non-truth-apt policy/content update: executable capability registration | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/mcp/dynamic-tools.ts` | [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker) | Shape admission is not semantic verification | Separate Bash-hook bypass path |
| [RT-RTE-operator-config](runtime.md#rt-rte-operator-config) | behavior/policy adaptation | implemented | see record | non-truth-apt policy/content update: caller-supplied instructions and configuration | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `src/ui/api/phantom-config.ts` | none | none | Instruction bodies can also contain claims; their truth is unassessed |

There is no separately established lifecycle-integration route in this assessment: edits, versioning, file promotion and prompt use do not alone demonstrate a prior evidence-consuming acceptance decision. This is a limit on interpreting those inspected functions, not a system-complete absence claim. Reflection's instruction to read the constitution and drop conflicting bullets is an implemented request for a model check; its execution and judgments are unobserved. The software check's actual domain is bytes, file names, line counts, fences, patterns and declared-versus-actual changes, not constitutional semantic consistency. [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission); SRC-1 `src/evolution/invariant-check.ts`, `src/evolution/subprocess-prompt.ts`.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker) | see record | SRC-1 `src/agent/prompt-assembler.ts`; doctrine/design | see record | [RT-RTE-channel-work](runtime.md#rt-rte-channel-work), [EPI-RTE-memory-delivery](#epi-rte-memory-delivery), [RT-RTE-dynamic-tools](runtime.md#rt-rte-dynamic-tools) | None supplied | No comparison or demonstrated accumulation benefit | Persistence and later behavior-shaping delivery are wired | Compounding knowledge/capability and growth with every conversation exceed demonstrated warrant; ingress routes differ |
| [EPI-CLM-session-learning](#epi-clm-session-learning) | see record | SRC-1 `docs/self-evolution.md`; doctrine/design | see record | [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission), [RT-RTE-judge-call](runtime.md#rt-rte-judge-call) | None supplied | No outcome/comparison evidence; gate can skip, reflection can skip, direct ingress bypasses channel post-processing | Improvement-directed instruction maintenance exists | Every-session rewriting and doing better are not established; snapshot exclusions/skip branch limit universal byte-validation reading |

## Bounded conclusion

Phantom can acquire user assertions and retain task metadata, episodic summaries, fact-like text and instruction files for later use. Source warrant is **unknown**, not upgraded by storage. For short direct quotations the original wording can survive, but truncation, predicate reassignment and prompt rendering can remove scope and source context. The semantic fact object preserves episode IDs; the automatic prompt shows natural language and confidence rather than those IDs. This is operational reliance on retained material, not a checked transfer of warrant. [EPI-RTE-fact-extraction](#epi-rte-fact-extraction), [EPI-RTE-fact-retention](#epi-rte-fact-retention), [EPI-RTE-memory-delivery](#epi-rte-memory-delivery).

Two implemented evaluators have sharply different targets. The gate model judges a sampled session's worthiness for maintenance, not the truth of a future memory bullet. Its failure admits work. Deterministic invariants assess covered post-state structure and narrow credential/duplicate patterns; hard failures can restore snapshots, soft warnings do not reject, and skip does not receive the same post-check. Neither licenses truth of a new domain claim. Reflection is asked to infer preferences, compact and move content, and to check constitution consistency. No observed output lets this analysis distinguish particular imports, entailed derivations, semantic-preserving compactions and ampliative conjectures. No produced accepted ampliative claim is established. [RT-RTE-judge-call](runtime.md#rt-rte-judge-call), [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission).

The semantic store's candidate-conflict selector and confidence comparison have enforcing recall consequences but do not establish logical contradiction or correctness. A higher/equal-confidence candidate can expire an old item, while lower-confidence candidates still persist. Default recall excludes expired items; temporal recall does not enforce that same exclusion. Dashboard deletion offers a separate withdrawal mechanism, without demonstrated removal from existing prompts, transcripts or evolved notes. [EPI-RTE-similarity-check](#epi-rte-similarity-check), [EPI-RTE-validity-change](#epi-rte-validity-change), [EPI-RTE-memory-delete](#epi-rte-memory-delete).

Later authority is heterogeneous: natural-language prompt/tool evidence guides the main model over current and subsequent invocations; registered handler definitions execute under process rights; shape-checked operator configuration can change future instructions or settings. There is no common truth gate on these planes. Review requests add model feedback, not an enforced correctness acceptance step; the named CI/PR status handlers inspected here return placeholders. [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance), [RT-BAP-handler-execution](runtime.md#rt-bap-handler-execution), [RT-RTE-operator-config](runtime.md#rt-rte-operator-config), [EPI-RTE-review-request](#epi-rte-review-request).

The reflection path supports a bounded dispositional improvement-directed self-change account, not exercised or beneficial self-improvement: the later-operation dependence link and outcome comparison remain unestablished. Its theory-builder conditions, learning, reflection and autonomy retain the separate statuses in [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission); file addressability and iterative queue wiring do not supply missing content-directed criticism or demonstrated learning. Distributed-parametric inference is present, but inspected wrappers do not train the models, and provider-side mutation is uninspected. Missing traces and the explicitly unassessed operations above prevent a global negative about truth production, and they also prevent an unqualified positive epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-semantic-facts
Label: Semantic fact payloads

Source-native identity: `SemanticFact`, Qdrant semantic collection payload. Distinct from the runtime's session rows, dynamic definitions and chat supplement; no supplied record declares this vector-store object. Natural-language assertion text is interpreted by the model; subject/predicate/object, confidence, validity and source episode IDs are symbolic fields used by store code. Dense retrieval vectors are distributed numerical representations, not assertions with separately individuated truth conditions. Substrate: external Qdrant; embedding component is [RT-CMP-embedding-client](runtime.md#rt-cmp-embedding-client). Candidate content includes corrections and preferences, but a confidence number is assigned by extractor branch, not a calibrated warrant. SRC-1 `src/memory/consolidation.ts`, `src/memory/semantic.ts`.

> source_episode_ids: fact.source_episode_ids,
> confidence: fact.confidence,
> valid_from: new Date(fact.valid_from).getTime(),
> valid_until: fact.valid_until ? new Date(fact.valid_until).getTime() : null,
> --- `src/memory/semantic.ts`

#### EPI-OBJ-episodes
Label: Heuristic session episodes

Source-native identity: `Episode` created by `createEpisodeFromSession`, retained through `MemorySystem.storeEpisode`. Natural-language summary/detail carries assertions about a request and its outcome; symbolic metadata carries IDs, timestamps, outcome and importance. Qdrant-backed episodic store is distinct from [RT-OBJ-session-store](runtime.md#rt-obj-session-store), which coordinates SDK sessions. The summary copies/truncates the first user message; it is not a checked account of the whole task. Caller search in SRC-1 `src/index.ts` shows success/failure assigned from an `Error:` response prefix, so the imported outcome label supplies no independent task oracle. SRC-1 `src/memory/consolidation.ts`, `src/memory/system.ts`.

> const firstMessage = data.userMessages[0] ?? "No user message";
> const summary = firstMessage.length > 200 ? `${firstMessage.slice(0, 197)}...` : firstMessage;
> --- `src/memory/consolidation.ts`

#### EPI-OBJ-procedures
Label: Procedural memory payloads

Source-native identity: `Procedure`, Qdrant procedures collection. Natural-language description, trigger and ordered actions coexist with symbolic counters, confidence, IDs and dense/sparse retrieval representations. Distinct from runtime's executable dynamic tools: this store supplies suggested steps to a model, not registered subprocess code. SRC-1 `src/memory/procedural.ts`, `src/memory/context-builder.ts`. Procedure extraction is not supplied by the inspected consolidation route, which returns `proceduresDetected: 0`. Repository-wide non-test caller search found `storeProcedure` and `updateProcedureOutcome` only in the system wrapper; this limits inference of an active producer/outcome-feedback loop, not API capacity.

> const embeddingText = `${procedure.description} ${procedure.trigger}`;
> --- `src/memory/procedural.ts`

> const steps = procedure.steps.map((s) => `  ${s.order}. ${s.action}`).join("\n");
> --- `src/memory/context-builder.ts`

### Routes

#### EPI-RTE-fact-extraction
Label: Heuristic fact extraction

Distinct downstream transformation from [RT-RTE-channel-work](runtime.md#rt-rte-channel-work), not another declaration of foreground execution. Service callback supplies session data; consolidation code owns episode construction and pattern-based fact extraction, then calls store methods. No per-fact human approval or independent truth evaluator. Operating mode: open conversation traces. Trigger: post-response channel callback when memory is ready. Proposed change: append episode and correction/preference candidates. Pattern tests can omit a message, but do not reject an untrue matching sentence. Later storage/deletion is covered separately. Guidance is literal regexes, not model criticism. SRC-1 `src/memory/consolidation.ts`, `src/shared/patterns.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: episode/fact counts, zero detected procedures, duration after store calls.
- Later read-back: stored candidates can reach later retrieval; source episode IDs link facts to the constructed episode.
- Delegated visibility: store receives full payload; context builder later renders only selected fields.
- Selection predicate: every session gets an episode; correction/preference regex matches over lowercased user messages independently create facts.
- Invalidation or expiry: no extraction-time truth rejection or old-fact update; store validity and dashboard deletion are separate.
- Activation or effect: wired candidate construction and retention calls; no observed useful learning.
- Evidence limits: source-only deduction; pattern match is not semantic entailment or factual verification.

Concrete static trace, not execution: `I prefer tea` matches the preference pattern, producing object `I prefer tea`, identical natural-language text and confidence 0.9. `I do not agree that I prefer tea` also contains the matching substring and receives subject `user`, predicate `prefers`, and confidence 0.9, despite denying the embedded preference. The retained natural-language sentence still includes the denial: this is a mismatch between fields, not proof that every downstream model reads it as an affirmative preference. A message longer than 300 characters loses the tail in `natural_language`; a trailing restriction can therefore disappear. These counterexamples defeat a universal semantic-preservation claim. Acquisition of the user sentence is established; the overall field assignment/truncation relation is indeterminate across arbitrary input. No particular novel accepted proposition is observed.

> /i\s+prefer\s/,
> --- `src/shared/patterns.ts`

> subject: "user",
> predicate: "prefers",
> object: message.slice(0, 200),
> natural_language: message.slice(0, 300),
> source_episode_ids: [episodeId],
> confidence: 0.9,
> --- `src/memory/consolidation.ts`

#### EPI-RTE-fact-retention
Label: Semantic fact retention

New store-write referent, distinct from the extraction and supplied foreground routes. `MemorySystem.storeFact` delegates to `SemanticStore.store`; store software first invokes the separate conflict routes, embeds the natural-language text, then upserts the supplied candidate regardless of whether its confidence displaced an older one. Qdrant/embedding success is required for completion. Software proposes no independent content; supplied user wording and extractor metadata persist. No semantic rollback is established if a later upsert fails after an old item was expired. Operating mode: automatic writes from open traces; answer oracle: none. SRC-1 `src/memory/system.ts`, `src/memory/semantic.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: fact ID after embedding and upsert, or propagated error.
- Later read-back: payload and retrieval vectors enter later fact search and dashboard reads.
- Delegated visibility: remote embedder sees assertion text; Qdrant receives text, metadata and vectors.
- Selection predicate: initialized memory plus explicit store call; no truth-admission criterion.
- Invalidation or expiry: replacement by same ID, validity updates or explicit deletion; no automatic truth correction established.
- Activation or effect: retained availability is wired, not evidence-consuming acceptance or model compliance.
- Evidence limits: no observed store operation; external persistence and partial-write recovery unverified.

> const contradictions = await this.findContradictions(fact);
>
> for (const existing of contradictions) {
> await this.resolveContradiction(fact, existing);
> }
>
> const factVec = await this.embedder.embed(fact.natural_language);
> --- `src/memory/semantic.ts`

#### EPI-RTE-similarity-check
Label: Fact conflict selection

Distinct evaluator stage before disposition; no supplied counterpart after comparison with [RT-RTE-judge-call](runtime.md#rt-rte-judge-call), which is a model call for different targets. Target/domain: active fact payloads sharing a subject, retrieved by embedding the new subject/predicate, at most ten, with score at least 0.85, different ID and unequal object text. Embedding/search and code predicates are the evaluator. The code does not require equal predicate despite its comment. Its result is a candidate conflict list, not proof of logical contradiction: two different preference objects can both be true. No answer oracle or human decision is supplied. SRC-1 `src/memory/semantic.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: filtered fact payload list.
- Later read-back: inapplicable — transient list is consumed in the same store call, not retained itself.
- Delegated visibility: remote search receives subject/predicate embedding and active-subject filter.
- Selection predicate: matching subject, null valid_until, top-ten retrieval, score threshold, other ID, unequal object.
- Invalidation or expiry: recomputed per incoming fact; validity affects future candidate retrieval.
- Activation or effect: list feeds confidence-based withdrawal; no rejection of new candidate here.
- Evidence limits: score behavior unobserved; unequal strings and high similarity do not establish inconsistency or source truth.

> must: [{ key: "subject", match: { value: newFact.subject } }, { is_null: { key: "valid_until" } }],
> --- `src/memory/semantic.ts`

> if (r.id === newFact.id) return false;
> if (r.score < SIMILARITY_THRESHOLD) return false;
> const existingObject = r.payload.object as string;
> return existingObject !== newFact.object;
> --- `src/memory/semantic.ts`

#### EPI-RTE-validity-change
Label: Fact validity withdrawal

Distinct disposition from conflict checking and fact retention. Store software consumes candidate conflicts and compares metadata confidence; equal or higher incoming confidence expires the older fact at incoming valid_from. The incoming candidate is still stored if lower-confidence. Trigger: automatic store call; proposer: extractor/caller; decider/veto: numeric rule, not a second model or human. The criterion grants default-recall priority, not epistemic acceptance of a proposition for a named use. Rollback of old validity on later write failure is not shown. SRC-1 `src/memory/semantic.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: completion of optional existing-payload update.
- Later read-back: ordinary recall filters null valid_until; temporal recall instead restricts valid_from without the null-validity condition.
- Delegated visibility: Qdrant receives old ID and expiration timestamp, not a rationale or checked contradiction.
- Selection predicate: candidate list from conflict selection and incoming confidence greater than or equal to existing confidence.
- Invalidation or expiry: old fact is marked expired, not deleted; historical paths can still expose it.
- Activation or effect: enforcing default-recall eligibility change, with no demonstrated correctness gain.
- Evidence limits: hard-coded extractor confidence can decide withdrawal; no observed conflict or independent truth evidence.

> if (newFact.confidence >= existingFact.confidence) {
> await this.qdrant.updatePayload(this.collectionName, existingFact.id, {
> valid_until: new Date(newFact.valid_from).getTime(),
> });
> }
> --- `src/memory/semantic.ts`

#### EPI-RTE-memory-delivery
Label: Memory reliance delivery

Distinct vector-memory delivery from [RT-RTE-chat-context](runtime.md#rt-rte-chat-context), which reconstructs host chat artifacts. `MemoryContextBuilder` recalls episodes/facts/procedure in parallel; code prioritizes facts, budget-filters sections and uses episode durability rules. [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) supplies the subsequent prompt consumer. Separate in-process reflective tools allow requested fact/episode retrieval with temporal windows; model chooses whether to request or rely on these results. These are selection and supply, not truth acceptance. SRC-1 `src/memory/context-builder.ts`, `src/memory/ranking.ts`, `src/agent/in-process-reflective-tools.ts`, `src/memory/semantic.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: bounded natural-language prompt sections, or JSON memory-tool results; unavailable stores can yield empty results.
- Later read-back: subsequent invocations can receive previously retained facts, episodes and procedures.
- Delegated visibility: automatic fact section contains natural_language and confidence, not source_episode_ids or validity metadata; procedures expose steps, trigger and counters; tool results can expose fuller payloads.
- Selection predicate: query retrieval, readiness, section budget, episode score/access/importance and procedure similarity threshold; requested temporal tools additionally supply a time range.
- Invalidation or expiry: default semantic recall excludes expired items; supplying timeRange removes that default condition. Already injected copies are not retracted by store changes.
- Activation or effect: model receives advisory content and suggested steps; changed decisions, successful recall and benefit are unobserved.
- Evidence limits: Known Facts and confidence formatting do not calibrate source reliability. Existing procedure origin and outcome-counter update callers remain unestablished.

Behavioral-authority path: main model consumer, appended prompt or tool-result channel, advisory/ranking force, current invocation plus later rebuilds. Automatic source links are omitted in the rendered fact section. The temporal exception is consequential: reflective search sets `opts.timeRange`, so an expired fact whose valid_from lies in the window can be returned; withdrawal is not global. This qualifies any claim that newer facts universally replace older beliefs. The retrieval code imposes no evidence-consuming criterion for intended truth reliance.

> const lines = facts.map((f) => `- ${f.natural_language} [confidence: ${f.confidence.toFixed(1)}]`);
> return `## Known Facts\n${lines.join("\n")}`;
> --- `src/memory/context-builder.ts`

> if (!options?.timeRange) {
> must.push({ is_null: { key: "valid_until" } });
> }
> --- `src/memory/semantic.ts`

> if (input.days_back !== undefined) {
> opts.timeRange = { from: daysAgo(input.days_back), to: new Date() };
> opts.strategy = "temporal";
> }
> --- `src/agent/in-process-reflective-tools.ts`

#### EPI-RTE-memory-delete
Label: Dashboard memory withdrawal

Distinct deletion operation; not [RT-RTE-operator-config](runtime.md#rt-rte-operator-config)'s instruction/configuration writes. Dashboard API accepts type/ID, verifies existence, calls episode/fact/procedure deletion and returns deleted status. Caller proposes and decides removal; server validates shape and existence, not falsity. Cookie-auth context is documented in the API; exact caller humanity and reason are not established. Intended use: remove a stored item, not accept a replacement claim. Recovery is not provided by this API. SRC-1 `src/ui/api/memory.ts`, `src/memory/system.ts`, `src/memory/semantic.ts`, `src/memory/procedural.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: deleted flag and ID, or validation/not-found/I/O failure.
- Later read-back: future store searches no longer have the deleted point, conditional on external deletion semantics.
- Delegated visibility: selected item ID reaches type-specific store/deletePoint; no rationale or content criticism is retained here.
- Selection predicate: DELETE detail route, valid ID and existing selected item.
- Invalidation or expiry: explicit point deletion; no derived-content or in-flight-prompt cascade shown.
- Activation or effect: enforcing source-store removal rather than advisory flagging.
- Evidence limits: no supplied deletion run, causal improvement or global erasure guarantee.

> const existing = await getItemById(deps, type, idParsed.data);
> if (!existing) return json({ error: "Memory not found" }, { status: 404 });
> await deleteItemById(deps, type, idParsed.data);
> return json({ deleted: true, id: idParsed.data });
> --- `src/ui/api/memory.ts`

#### EPI-RTE-review-request
Label: MCP review feedback
Part of: [RT-RTE-direct-work](runtime.md#rt-rte-direct-work)

Material subroute for code/PR evaluation; parent remains a valid container for several direct callers, not superseded. MCP caller supplies target/focus, handler constructs review request, main runtime/model performs open-ended review and returns feedback JSON to caller. Target is supplied code/PR content over requested general/security/performance/style/tests domain; no frozen expected answer/reference outcome is supplied. Model proposes feedback; caller can use or ignore it. No inspected handler enforces merge, revision or rejection from the result. PR/CI status handlers in the same module return `not_connected`, so their tool names do not establish environment measurement. SRC-1 `src/mcp/tools-swe.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: review text, focus, cost and duration through MCP, or error response.
- Later read-back: runtime session retention may apply; no dedicated review-acceptance artifact is written by this handler.
- Delegated visibility: target and focus reach foreground runtime; exact retrieved target content depends on model/tool behavior.
- Selection predicate: explicit phantom_review_request tool invocation and validated target/focus.
- Invalidation or expiry: no semantic withdrawal or expiry for feedback in the handler.
- Activation or effect: advisory feedback returned to requesting client; downstream enforcement not established.
- Evidence limits: no observed review, correctness score or accepted change; generic tool effects are still possible during runtime execution.

> const response = await deps.runtime.handleMessage("mcp", `review-${Date.now()}`, prompt);
> --- `src/mcp/tools-swe.ts`

> status: "not_connected",
> message:
> "CI/CD integration not yet configured. " +
> "Pipeline monitoring will be available once CI access is set up during onboarding.",
> --- `src/mcp/tools-swe.ts`

### Claims

#### EPI-CLM-session-learning
Label: Every-session learning claim

Claimed operation: every session causes reflection and configuration rewriting to improve the next session. Distinct from [RT-CLM-autonomous-worker](runtime.md#rt-clm-autonomous-worker)'s identity/persistence claim; this is an operator-facing pipeline and benefit claim. SRC-1 `docs/self-evolution.md`, doctrine/design. Gate/reflection skipping and direct-ingress differences in [RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) and [RT-RTE-direct-work](runtime.md#rt-rte-direct-work) qualify universal activation. Structural file admission is supported, but semantic correctness and better future action are not demonstrated by source configuration.

> After every session, Phantom reflects on what happened and rewrites its own configuration to do better next time.
> --- `docs/self-evolution.md`

The same document declares post-write validation. The skip branch and snapshot exclusions in the supplied runtime prevent reading this as universal complete post-state coverage. The direct invariant read confirms that warnings do not independently veto and that the checker delegates I9 cleanup to the runner.

> After the subprocess exits, a deterministic sweep validates the outcome. Nine invariants, all pure functions:
> --- `docs/self-evolution.md`

> passed: hardFailures.length === 0,
> --- `src/evolution/invariant-check.ts`
