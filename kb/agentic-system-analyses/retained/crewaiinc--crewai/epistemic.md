---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "CrewAI truth-apt content, memory curation, output gates and feedback authority at the frozen revision."
run-id: AAS-2026-10-15-crewai-62e53db969a7-01
reviewed-boundary: "3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8"
---

# CrewAI epistemic report

## Source-and-claim boundary

The question is what licenses later reliance on CrewAI's generated outputs and retained context. The [boundary and Source register](boundary.md#source-register) fix SRC-1 and the whole open-source framework, excluding hosted implementations and external model/storage internals. This member uses implementation and attributed design evidence, not execution evidence. No observed run, verified candidate instance or causal comparison was supplied. Successful checks, extraction fidelity, exercised adaptation and improved performance therefore remain unobserved. Exact provider weights and provider-side learning remain uninspected; see [RT-CMP-agent-llm](runtime.md#rt-cmp-agent-llm), [RT-CMP-memory-llm](runtime.md#rt-cmp-memory-llm) and [RT-CMP-memory-embedder](runtime.md#rt-cmp-memory-embedder).

The supplied runtime is provisional. Direct reads below extend it to consolidation, explicit mutation, feedback lessons, score reporting and the CLI's remote evaluation gate. These are additional material operations, not a supersession of its valid containers. Uninspected adapters, source-specific parsing and provider executors prevent a system-complete negative about truth testing or knowledge production. A custom callable guardrail or tool could supply an evidence-based evaluator; the default model judgment does not establish one.

| Entry point or operation | SRC-1 source path | Coverage and records / prevented conclusion |
|---|---|---|
| Crew/Agent output, tools, hooks and Task gates | `lib/crewai/src/crewai/task.py`; `lib/crewai/src/crewai/agents/crew_agent_executor.py`; `lib/crewai/src/crewai/hooks/tool_hooks.py` | Supplied runtime findings, not new direct reads: [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff), [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff), [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch), [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail). Async and provider parity limits remain. |
| CLI run/test/eval | `lib/cli/src/crewai_cli/cli.py`; `lib/cli/src/crewai_cli/experimental/eval_crew.py` | Direct dispatch and gate reads; [EPI-RTE-eval-gate](#epi-rte-eval-gate). Model-comparison internals uninspected; remote evaluator unavailable. |
| Memory extraction and consolidation | `lib/crewai/src/crewai/memory/analyze.py`; `lib/crewai/src/crewai/memory/encoding_flow.py` | Direct helper and analysis/apply reads; [EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-consolidation-check](#epi-rte-consolidation-check), [EPI-RTE-plan-application](#epi-rte-plan-application). Earlier embedding/dedup implementation not fully inspected here. |
| Recall and explicit memory tools | `lib/crewai/src/crewai/memory/recall_flow.py`; `lib/crewai/src/crewai/tools/memory_tools.py`; `lib/crewai/src/crewai/memory/types.py` | Direct router, exploration, synthesis, formatting, score and tool reads; [EPI-RTE-memory-selection](#epi-rte-memory-selection). Shallow recall and view enforcement not fully inspected here. |
| Update/forget/reset | `lib/crewai/src/crewai/memory/unified_memory.py`; `lib/crewai/src/crewai/utilities/reset_memories.py` | Direct update/forget and CLI utility reads; [EPI-RTE-memory-mutation](#epi-rte-memory-mutation). Physical deletion/backend recovery not independently audited. |
| Knowledge ingestion/query | `lib/crewai/src/crewai/knowledge/knowledge.py`; `lib/crewai/src/crewai/knowledge/source/base_knowledge_source.py` | Direct API, chunking and save reads; [EPI-RTE-knowledge-import](#epi-rte-knowledge-import). Individual parsers and storage backends uninspected: no universal fidelity claim. Agent context delivery supplied by [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff). |
| Flow feedback learning | `lib/crewai/src/crewai/flow/human_feedback.py` | Direct distillation and pre-review reads, plus default-depth/source forwarding in `lib/crewai/src/crewai/memory/unified_memory.py` and privacy predicates there and in `lib/crewai/src/crewai/memory/recall_flow.py`; [EPI-RTE-feedback-lessons](#epi-rte-feedback-lessons). Public records need not match learn_source. Full decorator/resume admission uninspected: no universal human approval claim. |
| Crew train/test | `lib/crewai/src/crewai/utilities/evaluators/crew_evaluator_handler.py`; `lib/crewai/src/crewai/utilities/evaluators/task_evaluator.py` | Test evaluator directly read; training supplied by [RT-RTE-crew-training](runtime.md#rt-rte-crew-training). [EPI-RTE-test-scoring](#epi-rte-test-scoring) adds reporting, not training admission. |
| Skills, working summaries, delegation, Flow persistence | `lib/crewai/src/crewai/skills/tool.py`; `lib/crewai/src/crewai/utilities/agent_utils.py`; `lib/crewai/src/crewai/flow/runtime/__init__.py` | Supplied [RT-RTE-skill-disclosure](runtime.md#rt-rte-skill-disclosure), [RT-RTE-context-summary](runtime.md#rt-rte-context-summary), [RT-RTE-agent-delegation](runtime.md#rt-rte-agent-delegation), [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution). Delivery/restore is not truth acceptance. |
| Memory doctrine and prompts | `docs/edge/en/concepts/memory.mdx`; `lib/crewai/src/crewai/translations/en.json` | Direct overview and extraction/consolidation prompt inspection; [EPI-CLM-memory-facts](#epi-clm-memory-facts). Examples are not run artifacts. |
| Retrieval adapters, file inputs, MCP/remote services, remaining hooks | `lib/crewai-tools/src/crewai_tools/__init__.py`; `lib/crewai-files/src/crewai_files/__init__.py` | Boundary includes local implementations, but individual epistemic routes uninspected here. No complete enumeration or system-wide absence is inferred. Hosted service quality is outside the frozen implementation. |

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-record](#epi-obj-memory-record) | Stored assertions, decisions or observations; truth scope depends on the statement | see record | see record | Arbitrary strings need not be truth-apt; no instances supplied |
| [EPI-OBJ-consolidation-plan](#epi-obj-consolidation-plan) | Update text may assert facts; action/reason fields mix policy and content | see record | see record | Model comparison receives truncated old content |
| [EPI-OBJ-memory-match](#epi-obj-memory-match) | Record text plus relevance scores and model-reported gaps, not confidence in truth | see record | see record | Formatting omits explicit gap and lineage fields |
| [EPI-OBJ-feedback-lessons](#epi-obj-feedback-lessons) | Generalized lessons may assert reusable conditions; instructions may be non-truth-apt | see record | see record | No lesson instances or warranted generalizations supplied |
| [RT-OBJ-trained-agents](runtime.md#rt-obj-trained-agents) | see record | see record | see record | Retained suggestions are not necessarily explanatory claims |
| [RT-OBJ-skill](runtime.md#rt-obj-skill) | see record | see record | see record | Static instruction disclosure is not a use-derived finding |

## Authority-route ledger

Each route below is implementation-supported but unobserved. Fields owned by supplied records are cited rather than copied. For model-generated transformations, semantic preservation, entailment and non-entailment cannot be determined without input/output instances: the classification is indeterminate, not automatically conjecture. Imported statements have unknown external warrant. No inspected retention path by itself supplies an evidence-consuming acceptance decision with a truth criterion, intended use and scope.

Route ID: [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff), [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: task and standalone outputs, see records.
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: generated response to selected task/messages.
Evaluator/condition and domain: configured agent model; response generation is not independent verification.
Activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see cited records. Candidate generation is wired; truth and exercised compliance remain unestablished.
Claim IDs: none. Mismatch marker: none. Gap/limit: no candidate instances.

Route ID: [EPI-RTE-memory-extraction](#epi-rte-memory-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-record](#epi-obj-memory-record).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: raw task/conversation content to discrete statements.
Evaluator/condition and domain: memory LLM and output schema; schema checks strings, not source truth.
Activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: candidate statements only; preservation of names/numbers is requested, not demonstrated.
Operational authority: caller can submit returned statements for saving; fallback submits full content.
Behavioral-authority path: extraction caller → remember → later recall, advisory task context across runs if persisted.
Claim IDs: [EPI-CLM-memory-facts](#epi-clm-memory-facts). Mismatch marker: fact terminology exceeds demonstrated warrant. Gap/limit: transformation relation requires concrete input/output evidence.

Route ID: [EPI-RTE-consolidation-check](#epi-rte-consolidation-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-consolidation-plan](#epi-obj-consolidation-plan).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: accuracy/redundancy/supersession of retrieved old memories relative to new text.
Evaluator/condition and domain: LLM comparing new content with summaries containing at most 200 old-content characters; not a source-authentication procedure.
Activation and timing; possible or observed result; evidence source ID and local anchor: see record.
Implemented force: plan proposal; application is separately listed below.
Epistemic authority and scope: proposed relative-content judgment only; contradictory new content is not independently established as true.
Operational authority: no database effect until plan application.
Behavioral-authority path: structured plan → encoding pipeline; proposed update/delete/insert for this save.
Claim IDs: [EPI-CLM-memory-facts](#epi-clm-memory-facts). Mismatch marker: unknown warrant. Gap/limit: no full-context guarantee or observed comparison.

Route ID: [EPI-RTE-plan-application](#epi-rte-plan-application)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-consolidation-plan](#epi-obj-consolidation-plan).
Content/update relation: no content change.
Transition or check target: apply model actions or fast-path/default insert.
Evaluator/condition and domain: pipeline predicates, action type, new-content presence and first-action conflict resolution; structural admission, not truth acceptance.
Activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: no added factual license from admission.
Operational authority: permits destructive deletion, content replacement and insertion without a separately shown human per-plan veto.
Behavioral-authority path: plan → storage mutation → future recall availability, enforcing for stored state until later change.
Claim IDs: none. Mismatch marker: none. Gap/limit: check failure defaults to retention rather than withholding uncertain content.

Route ID: [EPI-RTE-plan-application](#epi-rte-plan-application)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-record](#epi-obj-memory-record).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: text and resolved fields to stored record; model replacement may change meaning.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: retained candidate, not accepted claim.
Operational authority: makes retained text available to later query consumers.
Behavioral-authority path: storage → recall → formatted model context; advisory after enforcing storage selection, potentially across runs.
Claim IDs: none. Mismatch marker: lineage loss on replacement. Gap/limit: update reconstructs record with old metadata but does not carry source/private fields explicitly; no evidential-history acceptance link is established.

Route ID: [EPI-RTE-memory-selection](#epi-rte-memory-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-match](#epi-obj-memory-match).
Content/update relation: no content change.
Transition or check target: retrieved records' relevance and exploration depth, not factual correctness.
Evaluator/condition and domain: weighted semantic similarity, recency, importance, thresholds, query complexity and exploration budget.
Activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: ranked relevance only; score is not calibrated truth probability.
Operational authority: selects records and continuation depth before agent consumption.
Behavioral-authority path: recall router/ranker → top limited matches → agent prompt/tool result; ranking then advisory, current and later invocations.
Claim IDs: [EPI-CLM-memory-facts](#epi-clm-memory-facts). Mismatch marker: confidence label is relevance-derived. Gap/limit: exploration can append missing-information reports but final results remain retrieved records.

Route ID: [EPI-RTE-memory-selection](#epi-rte-memory-selection)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-match](#epi-obj-memory-match).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target: match object to display text.
Evaluator/condition and domain: deterministic format implementation, not a semantic judge.
Activation and timing; possible or observed result; evidence source ID and local anchor: see record.
Implemented force: content, rounded score and nonempty categories/metadata enter the tool observation; explicit evidence_gaps, source and match reasons are omitted.
Epistemic authority and scope: no new warrant; reduced caveat/lineage visibility.
Operational authority: changes what the downstream model can see without an extra check.
Behavioral-authority path: MemoryMatch.format → Search memory tool → foreground LLM, advisory for current execution.
Claim IDs: none. Mismatch marker: evidence gaps are not delivered by this formatter. Gap/limit: metadata can independently contain caveats; other callers may inspect full objects.

Route ID: [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: TaskOutput, see record.
Content/update relation: no content change.
Transition or check target: task output against caller-configured callable or language criterion.
Evaluator/condition and domain; activation and timing; possible or observed result; evidence source ID and local anchor: see record.
Implemented force: reported check result; disposition is separate below.
Epistemic authority and scope: only what the configured evaluator can warrant; no supplied independent oracle.
Operational authority; behavioral-authority path: see record.
Claim IDs: [RT-CLM-output-validation](runtime.md#rt-clm-output-validation). Mismatch marker: none. Gap/limit: output validation is not universal effect validation.

Route ID: [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail), [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: task/standalone candidate, see records.
Content/update relation: no content change.
Transition or check target: success flag and retry budget for progression/return.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor: see records.
Claim IDs: [RT-CLM-output-validation](runtime.md#rt-clm-output-validation). Mismatch marker: none. Gap/limit: Task memory save precedes rejection; standalone save follows its gate. Neither revokes prior tool effects.

Route ID: [EPI-RTE-memory-mutation](#epi-rte-memory-mutation)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-record](#epi-obj-memory-record).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: caller replacement text or deletion/reset criteria.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: replacement warrant unknown; deletion is withdrawal of availability, not criticism proving falsity.
Operational authority: update changes future retrieved text; forget/reset removes stored availability.
Behavioral-authority path: caller/API or reset utility → storage → later recall, enforcing stored availability until subsequent writes.
Claim IDs: none. Mismatch marker: none. Gap/limit: no automatic propagation into already delivered prompts or downstream copies established.

Route ID: [EPI-RTE-knowledge-import](#epi-rte-knowledge-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: source text and chunks, see record.
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: configured sources to chunk store and query results.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: source warrant unknown; storage/search does not authenticate assertions. Base chunking itself is non-ampliative slicing.
Operational authority: query relevance filtering selects context available to agent callers.
Behavioral-authority path: source.add → storage.save → query → agent context, ranking then advisory while stored.
Claim IDs: none. Mismatch marker: none. Gap/limit: source-specific conversions and complete returned-context fidelity uninspected.

Route ID: [EPI-RTE-feedback-lessons](#epi-rte-feedback-lessons)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-feedback-lessons](#epi-obj-feedback-lessons).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: method output plus human feedback to lessons; later output plus lessons to pre-review revision.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: human feedback is input evidence, not guaranteed endorsement of each distilled lesson or its transfer.
Operational authority: automatic memory retention and later eligible-output rewriting; no per-lesson approval is shown in these helpers.
Behavioral-authority path: retained memory → relevance recall with learn_source controlling private-record visibility, not excluding other public records → reviewing LLM → replacement method output; recalled content is advisory, replacement permissive, across calls while retained. Public non-lesson content can enter the same review channel.
Claim IDs: none. Mismatch marker: none. Gap/limit: lessons and revisions may be truth-apt or purely behavioral; absent instances prevent individuating propositions.

Route ID: [RT-RTE-crew-training](runtime.md#rt-rte-crew-training)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-trained-agents](runtime.md#rt-obj-trained-agents).
Content/update relation: non-truth-apt policy/content update: persisted behavioral suggestions, potentially mixed with uninspected factual claims.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; evidence source ID and local anchor: see record.
Behavioral-authority path: see [RT-BAP-training-instructions](runtime.md#rt-bap-training-instructions).
Claim IDs: none. Mismatch marker: none. Gap/limit: same-agent model scoring is not causal improvement evidence or a weight update.

Route ID: [EPI-RTE-test-scoring](#epi-rte-test-scoring)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: task output and numeric quality score, see record.
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: task completion/quality/performance against task description and expected-output specification.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: model opinion about fit to specification, not a supplied expected-answer comparison.
Operational authority: reporting only in inspected callback; no score-driven mutation/admission shown there.
Behavioral-authority path: evaluator Task → numeric score → event and report table, advisory for human consumers of the test run.
Claim IDs: none. Mismatch marker: none. Gap/limit: reported success cannot identify producer mechanism or component effects.

Route ID: [EPI-RTE-eval-gate](#epi-rte-eval-gate)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: remotely returned run verdict, see record.
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: remote evaluation status and gate string for selected traced execution.
Evaluator/condition and domain: local done/passed predicate; remote goal evaluator implementation outside boundary.
Activation and timing; possible or observed result; implemented force; evidence source ID and local anchor: see record.
Epistemic authority and scope: unknown remote warrant; local code establishes status interpretation only.
Operational authority: non-passed result exits nonzero; passed result allows normal CLI return, usable by a cooperating CI process.
Behavioral-authority path: remote verdict → CLI exit code → optional external pipeline, enforcing process status for this evaluation, not universal deployment prevention.
Claim IDs: [EPI-CLM-eval-exit](#epi-clm-eval-exit). Mismatch marker: none. Gap/limit: no actual CI consumer or remote evaluation evidence supplied.

Lifecycle integration: no route found within boundary for the narrower searched extraction, consolidation, test-score and feedback helper paths that first accepts a truth claim against evidence and then links that accepted claim into an evidential organization. This is not a framework-wide absence: configured guardrails, arbitrary tools and Flow bodies remain open. Storage updates, trained instructions and operational reuse above are retained candidates or policy updates unless an independently evidenced acceptance decision supplies more.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-memory-facts](#epi-clm-memory-facts) | see record | see record | see record | [EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-consolidation-check](#epi-rte-consolidation-check), [EPI-RTE-plan-application](#epi-rte-plan-application), [EPI-RTE-memory-selection](#epi-rte-memory-selection) | none supplied | No experimental outcomes; full-content fallback and truncated comparisons limit fact/fidelity interpretation | LLM extraction, retention and relevance routing are wired | Fact labels and importance/relevance do not establish truth |
| [RT-CLM-output-validation](runtime.md#rt-clm-output-validation) | see record | see record | see record | [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail) | none supplied | see record | Configured Task progression check | Prior writes/effects not revoked; oracle depends on caller |
| [RT-CLM-tool-veto](runtime.md#rt-clm-tool-veto) | see record | see record | see record | [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) | none supplied | see record | Conditional pre-call policy enforcement | Neither content truth check nor universal mediation |
| [EPI-CLM-eval-exit](#epi-clm-eval-exit) | see record | see record | see record | [EPI-RTE-eval-gate](#epi-rte-eval-gate) | none supplied | Hosted goal judgment inaccessible; external CI behavior unsupplied | Local exit status reflects remote done/passed predicate | Does not establish correct remote verdict or prevented deployment |

## Bounded conclusion

CrewAI wires several independent authority paths. Memory extraction produces candidate statements; consolidation compares them with old text, then separate application logic can delete, update or insert. That check can be skipped on a fast path and failures default to insertion. Thus storage and later prompt use are not evidence of accepted factual knowledge. Consolidation sees shortened old text and update construction can lose lineage fields; claims of complete provenance or truth-preserving merging are unsupported. See [EPI-RTE-consolidation-check](#epi-rte-consolidation-check) and [EPI-RTE-plan-application](#epi-rte-plan-application).

Recall ranks by relevance, age and importance, not truth. Model-reported gaps can exist on the full match object while Search memory's formatted delivery omits that field. Acquired knowledge-source text and caller-written replacements retain unknown source warrant; deterministic chunking and formatting add none. No warranted-premise derivation or produced accepted ampliative claim is established by these inspected paths. Their generated semantic relations remain indeterminate without instances, not classified as conjectures just because entailment is unknown. See [EPI-RTE-memory-selection](#epi-rte-memory-selection), [EPI-RTE-knowledge-import](#epi-rte-knowledge-import) and [EPI-RTE-memory-mutation](#epi-rte-memory-mutation).

Task guardrails can enforce configured acceptance for progression and may contain evidence-based checks supplied by an application. Their license is exactly the configured criterion's domain; no such truth oracle or successful check was supplied. Rejection does not retract Crew executor memory already saved or earlier tool effects. Standalone finalization instead checks before its output save. Hooks enforce local tool policy, not universal epistemic warrant. See [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail), [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff) and [RT-CLM-tool-veto](runtime.md#rt-clm-tool-veto).

Feedback lessons and training suggestions can reshape later outputs or instructions without a demonstrated truth-apt theory route. Feedback pre-review passes learn_source to default-deep recall, but its privacy predicate also admits public records from other sources. The reviewer receives matched content under a lesson label without source fields; this is not an exclusively feedback-derived review context. See [EPI-RTE-feedback-lessons](#epi-rte-feedback-lessons). This is implemented retained-text adaptation, not provider-weight training. Human feedback contributes evidence but does not establish human approval of each inferred rule. Later consumption is wired; exercised causal dependence and objective improvement are unsupplied, independently limiting learning and exercised self-improvement claims. No inference of reflection, autonomy or theory-builder conditions follows merely from these labels. Test scoring reports model opinions; the separate CLI eval gate consumes an opaque hosted verdict and sets exit status. Neither route supplies a causal experiment. These conclusions remain local to their routes, not one system-wide epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-memory-record
Label: MemoryRecord content

Source-native identity: `MemoryRecord.content` and caller/extractor-produced statements. Natural-language text is interpreted by later models; substrate is a MemoryRecord passed to storage. Categories/metadata and embeddings are separate selection aids, not the assertion's warrant. SRC-1, `lib/crewai/src/crewai/memory/encoding_flow.py`. No supplied record declares this object; [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff) describes the enclosing task caller rather than the retained object.

> content=item.content,
> scope=item.resolved_scope,
> categories=item.resolved_categories,
> metadata=item.resolved_metadata,
> --- `lib/crewai/src/crewai/memory/encoding_flow.py`

#### EPI-OBJ-consolidation-plan
Label: ConsolidationPlan

Source-native identity: structured plan with actions, insertion flag and reasons, plus optional replacement content. Symbolic action fields have fixed code consumers; natural-language reasons/content require interpretation. Substrate: Pydantic objects in encoding state. SRC-1, `lib/crewai/src/crewai/memory/analyze.py`. Distinct from the model binding in [RT-CMP-memory-llm](runtime.md#rt-cmp-memory-llm); no supplied plan counterpart.

> class ConsolidationPlan(BaseModel):
>     """LLM output for consolidating new content with existing memories."""
> --- `lib/crewai/src/crewai/memory/analyze.py`

#### EPI-OBJ-memory-match
Label: MemoryMatch

Source-native identity: MemoryRecord plus symbolic numeric relevance score, reasons and natural-language evidence gaps. In-process Pydantic result, optionally rendered to strings. This is distinct from stored content and from [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff)'s enclosing retrieval caller; no supplied match counterpart. SRC-1, `lib/crewai/src/crewai/memory/types.py`.

> score: float = Field(
>     description="Combined relevance score (semantic, recency, importance).",
> )
> --- `lib/crewai/src/crewai/memory/types.py`

#### EPI-OBJ-feedback-lessons
Label: DistilledLessons

Source-native identity: lessons distilled from Flow output and raw human feedback. Natural-language statements/instructions stored through memory with learn_source; eligible for later consumption by the reviewing LLM alongside other public memories. The review-context collection is not lineage-restricted to this object. Distinct from role-keyed pickle suggestions in [RT-OBJ-trained-agents](runtime.md#rt-obj-trained-agents); the shared feedback theme does not identify their artifacts or consumers. SRC-1, `lib/crewai/src/crewai/flow/human_feedback.py`.

> if lessons:
>     mem.remember_many(lessons, source=learn_source)  # type: ignore[union-attr]
> --- `lib/crewai/src/crewai/flow/human_feedback.py`

### Routes

#### EPI-RTE-memory-extraction
Label: Memory statement extraction

The caller supplies raw text; memory LLM proposes discrete statements using shipped extraction guidance. JSON/Pydantic validation admits a list, not independently verified facts. This helper is distinct from [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff)'s task scheduling and from [RT-CMP-memory-llm](runtime.md#rt-cmp-memory-llm)'s model identity. SRC-1 implementation, `lib/crewai/src/crewai/memory/analyze.py`. Failure can retain raw content instead of refusing a candidate. Open input transformation; no expected-answer oracle or human per-statement approval in the helper.

- Immediate return: list of statements, empty list for empty text, or full-content fallback; HookAborted propagates.
- Later read-back: inapplicable — helper itself does not persist; callers can submit its return to remember for later recall.
- Delegated visibility: LLM receives raw content with system extraction instructions.
- Selection predicate: nonempty input and response-model/JSON parsing.
- Invalidation or expiry: inapplicable — returned list has no lifecycle policy here.
- Activation or effect: produces candidate text for caller-directed retention, not a truth decision.
- Evidence limits: implementation only; extraction fidelity and generated statement instances unsupplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _logger.warning(
>     "Memory extraction failed, storing full content as single memory: %s",
>     e,
>     exc_info=False,
> )
> return [content]
> --- `lib/crewai/src/crewai/memory/analyze.py`

#### EPI-RTE-consolidation-check
Label: Memory consolidation check

A new save above the similarity threshold sends new content plus similar-record summaries to the memory LLM, requesting keep/update/delete and insertion judgment. The prompt asks conservative treatment of contradiction, supersession and redundancy, but supplies no independent source verification. This is a distinct evaluator call from [RT-RTE-crew-training](runtime.md#rt-rte-crew-training), not its score/suggestion producer. SRC-1 implementation, `lib/crewai/src/crewai/memory/analyze.py` and `lib/crewai/src/crewai/memory/encoding_flow.py`; guidance in `lib/crewai/src/crewai/translations/en.json`. The LLM proposes; schema parsing admits a plan; caller/framework hooks can abort, but no human per-action review is shown. Mode: open saves, triggered by similar records, not controlled experiments. No answer oracle. Failure defaults to insert, not withholding reliance.

- Immediate return: ConsolidationPlan or default insert plan; HookAborted propagates.
- Later read-back: inapplicable — plan itself is transient; application persists its effects, separately recorded.
- Delegated visibility: new text and old-record IDs, scope, importance, creation time, and first 200 content characters.
- Selection predicate: similar records and pipeline similarity threshold; supplied fields can skip separate metadata analysis.
- Invalidation or expiry: per-save plan superseded by completion; no plan history demonstrated.
- Activation or effect: proposes content replacement, deletion and insertion instructions.
- Evidence limits: relative comparison of partial texts is not truth testing against the world; no run supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> f"  content: {r.content[:200]}{'...' if len(r.content) > 200 else ''}"
> --- `lib/crewai/src/crewai/memory/analyze.py`

> _CONSOLIDATION_DEFAULT = ConsolidationPlan(actions=[], insert_new=True)
> --- `lib/crewai/src/crewai/memory/analyze.py`

#### EPI-RTE-plan-application
Label: Consolidation plan application

Encoding code consumes plan actions, keeps the first effective action per record, embeds replacement content, applies deletes/updates and saves insertions. Fast paths with no sufficiently similar record insert without consolidation; metadata analysis is not acceptance. Software admits these changes without a separate evidenced truth criterion or human plan approval. Guidance derives from the check above; recovery/rollback history is not established. This route is distinct from [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail): output rejection does not undo these writes. SRC-1 implementation, `lib/crewai/src/crewai/memory/encoding_flow.py`.

Updated records retain existing ID, scope, categories, metadata, importance and creation time, but the inspected constructor does not explicitly propagate source/private fields. Retained old metadata is not a proof that it supports the revised statement. The route provides organization and future availability, not lifecycle integration of an already accepted truth claim.

- Immediate return: state counters and item result_record, with inserts/updates/deletes applied.
- Later read-back: future recall can select inserted/replaced records; deleted candidates cease to be available through the store.
- Delegated visibility: embedder receives replacement strings; storage receives records and IDs.
- Selection predicate: dropped items and missing plans skipped; delete/update actions deduplicated; update requires new_content; insert_new controls insertion.
- Invalidation or expiry: deletes remove availability; subsequent writes can replace records; no versioned rollback shown here.
- Activation or effect: storage mutation before future recall; semantic behavioral effects remain unobserved.
- Evidence limits: storage backend guarantees not audited; insertion and mutation are not factual acceptance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if fields_provided and not has_similar:
>     self._apply_defaults(item)
>     item.plan = ConsolidationPlan(actions=[], insert_new=True)
> --- `lib/crewai/src/crewai/memory/encoding_flow.py`

> if dedup_deletes:
>     self._storage.delete(record_ids=list(dedup_deletes))
>     self.state.records_deleted += len(dedup_deletes)
> --- `lib/crewai/src/crewai/memory/encoding_flow.py`

> scope=existing.scope,
> categories=existing.categories,
> metadata=existing.metadata,
> importance=existing.importance,
> created_at=existing.created_at,
> last_accessed=now,
> embedding=new_emb if new_emb else existing.embedding,
> --- `lib/crewai/src/crewai/memory/encoding_flow.py`

#### EPI-RTE-memory-selection
Label: Recall relevance selection

RecallFlow routes on relevance-derived confidence, query complexity and budget. Exploration asks an LLM for relevant information and missing information; final synthesis deduplicates original records, recomputes relevance and limits the list. It does not accept a newly synthesized factual answer. Search memory uses m.format rather than delivering every result field. Distinct from [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff)'s scheduling and enclosing prompt preparation: this record establishes selector and formatting semantics. SRC-1 implementation, `lib/crewai/src/crewai/memory/recall_flow.py`, `lib/crewai/src/crewai/memory/types.py`, `lib/crewai/src/crewai/tools/memory_tools.py`. The model may propose query analysis/exploration; code controls ranking and depth; no human admission or expected-answer oracle in these paths. Mode: open retrieval.

Concrete deterministic deduction: a match with score 0.8, content `The API limit is 1000.`, empty categories/metadata and evidence_gaps containing `Date missing` formats as `- (score=0.80) The API limit is 1000.`. The gap is absent from that string because the formatter reads only score, content, categories and metadata. This is implementation-layer reasoning, not target execution. A false assertion with the same score/metadata would be formatted identically apart from its content; the score cannot certify truth. Full-object callers can still read evidence_gaps.

- Immediate return: ranked MemoryMatch list; Search memory returns deduplicated formatted strings or no-results text.
- Later read-back: existing retained records reach later model calls through prompt preparation or explicit tools; selection creates no separate durable knowledge artifact.
- Delegated visibility: exploration LLM sees query and top five result contents per finding; foreground tool consumer sees formatted fields, not explicit evidence_gaps or source fields.
- Selection predicate: relevance score, thresholds, query complexity, remaining budget, deduplicated IDs and result limit.
- Invalidation or expiry: query results are current-call values; retained records remain subject to future store changes.
- Activation or effect: ranks model-visible context and changes exploration continuation; no demonstrated semantic compliance.
- Evidence limits: shallow recall and every view/backend not independently inspected; gaps are model reports, not a verified completeness measurement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> composite = (
>     config.semantic_weight * semantic_score
>     + config.recency_weight * decay
>     + config.importance_weight * record.importance
> )
> --- `lib/crewai/src/crewai/memory/types.py`

> self.state.confidence = max((f["top_score"] for f in findings), default=0.0)
> --- `lib/crewai/src/crewai/memory/recall_flow.py`

> lines = [f"- (score={self.score:.2f}) {self.record.content}"]
> if self.record.categories:
>     lines.append(f"  categories: {', '.join(self.record.categories)}")
> if self.record.metadata:
>     for key, value in self.record.metadata.items():
>         if value is not None:
>             lines.append(f"  {key}: {value}")
> return "\n".join(lines)
> --- `lib/crewai/src/crewai/memory/types.py`

> all_lines.append(m.format())
> --- `lib/crewai/src/crewai/tools/memory_tools.py`

#### EPI-RTE-memory-mutation
Label: Explicit memory mutation

Memory.update accepts caller replacement fields, re-embeds changed content and calls storage.update; read_only returns the existing record. Memory.forget forwards deletion criteria to storage; unlike update, the inspected forget body has no read_only branch. This observation does not assert bypass of every scoped wrapper. Reset utility routes Crew and Flow reset commands to their stores. Distinct from [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail)'s output gate and [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution)'s state hydration. SRC-1 implementation, `lib/crewai/src/crewai/memory/unified_memory.py` and `lib/crewai/src/crewai/utilities/reset_memories.py`. Caller proposes/decides replacement or deletion; caller identity does not establish human approval. No factual oracle, evidence check or automatic dependency invalidation appears in these inspected API bodies. Mode: explicit maintenance; no model critique required.

- Immediate return: updated/unchanged record, deleted count, or reset command completion/error.
- Later read-back: future store queries see changed availability/content; no automatic retraction of already delivered messages established.
- Delegated visibility: storage receives IDs/filters/updated records; embedder sees replacement content.
- Selection predicate: record ID or scope/category/time/metadata filters; missing update ID raises; read_only prevents update.
- Invalidation or expiry: explicit mutation/delete/reset; history restoration and cross-artifact rollback uninspected.
- Activation or effect: changes retained availability and content for later consumers.
- Evidence limits: no executed cleanup, backend deletion proof or universal wrapper equivalence supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.read_only:
>     return existing
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

> updated = existing.model_copy(update=updates)
> self._storage.update(updated)
> return updated
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

> if isinstance(mem, Memory):
>     mem.reset_all()
> --- `lib/crewai/src/crewai/utilities/reset_memories.py`

#### EPI-RTE-knowledge-import
Label: Knowledge source import

Knowledge assigns storage to sources and calls add. BaseKnowledgeSource chunks text by fixed character windows and saves those strings; query delegates to storage search with result count and threshold. This route describes imported context, not produced accepted findings. Source-authentication and parser fidelity are not established by the inspected base layer. It is distinct from [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff)'s enclosing task and knowledge consumer. SRC-1 implementation, `lib/crewai/src/crewai/knowledge/knowledge.py` and `lib/crewai/src/crewai/knowledge/source/base_knowledge_source.py`. Caller supplies source objects; source-type/schema validation checks configuration, not assertions. No human per-chunk approval or truth oracle in these bodies. Mode: open ingestion/query; recovery is raised storage/source errors, not an evidential revision loop.

Concrete base-chunking deduction: with chunk_size=4 and chunk_overlap=1, `abcdef` yields `abcd`, `def`, because the range advances by three and slices four characters. Slicing creates no new proposition and can cut a sentence. This is code deduction, not target execution; it makes no claim about every parser's settings or output.

- Immediate return: add_sources finishes or raises; query returns backend SearchResults.
- Later read-back: saved chunks can be selected by later queries and supplied to agent context.
- Delegated visibility: source receives storage; base save passes chunks; search receives query, limit and threshold.
- Selection predicate: caller-configured source list and backend relevance threshold/limit.
- Invalidation or expiry: uninspected — base ingestion/query bodies do not establish per-claim withdrawal or backend expiry.
- Activation or effect: makes imported text retrievable; actual answer influence unobserved.
- Evidence limits: specific sources, provenance and backend transformations uninspected; no factual warrant follows from the Knowledge name.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for source in self.sources:
>     source.storage = self.storage
>     source.add()
> --- `lib/crewai/src/crewai/knowledge/knowledge.py`

> return [
>     text[i : i + self.chunk_size]
>     for i in range(0, len(text), self.chunk_size - self.chunk_overlap)
> ]
> --- `lib/crewai/src/crewai/knowledge/source/base_knowledge_source.py`

#### EPI-RTE-feedback-lessons
Label: Feedback lesson reuse

Distillation helper gives method output and raw feedback to the configured LLM, parses lessons, and submits them to memory with learn_source. Pre-review passes learn_source to default-deep recall and asks the LLM to improve eligible string/Pydantic output before review. This argument is not an exclusive source filter: deep and shallow recall both admit public records regardless of source and private records matching the supplied source. Thus public non-lesson content can be presented as lessons; the reviewer receives matched content strings, not source/private fields. Hidden-valued models and other types bypass rewriting. LLM proposes lesson/revision; software admits parsed text/type-compatible output. Human feedback is not necessarily per-lesson approval; no independent oracle appears. Strict mode raises on failure; otherwise helper keeps raw output or stores nothing. No versioned lesson rollback shown. Distinct from role-keyed Crew suggestions in [RT-RTE-crew-training](runtime.md#rt-rte-crew-training); overlaps [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution) only as one Flow feedback feature, not a universal execution rule. SRC-1 implementation, `lib/crewai/src/crewai/flow/human_feedback.py`.

- Immediate return: distillation saves lessons or returns without saving; pre-review returns revised eligible output or original output.
- Later read-back: default-deep recall can supply retained lessons and other public memory content on later method pre-review calls; learn_source does not restrict public-record lineage.
- Delegated visibility: distiller sees method name/output/feedback; reviewer sees rendered output and matched record content presented as lessons, not source/private fields or necessarily the feedback trace.
- Selection predicate: memory exists, nonempty lessons/matches, eligible output type and absence of hidden model fields; recall uses relevance selection and permits public records regardless of source plus private records matching learn_source.
- Invalidation or expiry: memory mutation/reset can change retained lessons; no helper-local version history or per-lesson approval rollback shown.
- Activation or effect: retained feedback-derived text is wired to possible output rewriting before a later review.
- Evidence limits: decorator/resume routing and actual learned rules uninspected; no causal dependence or improved outcome supplied. The source argument cannot license a lineage-restricted review-context comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> query = f"human feedback lessons for {method_name}: {rendered}"
> matches = mem.recall(query, source=learn_source)
> --- `lib/crewai/src/crewai/flow/human_feedback.py`

> lessons = "\n".join(f"- {m.record.content}" for m in matches)
> --- `lib/crewai/src/crewai/flow/human_feedback.py`

SRC-1 implementation: `lib/crewai/src/crewai/memory/unified_memory.py` defaults recall to deep and passes source/include_private to RecallFlow. Its shallow predicate has the same public-or-matching-private rule. Independent deep-path evidence in `lib/crewai/src/crewai/memory/recall_flow.py` confirms the correction; it agrees with supplied [MEM-RTE-feedback-lessons](memory.md#mem-rte-feedback-lessons), [MEM-RTE-memory-recall](memory.md#mem-rte-memory-recall) and [MEM-OBJ-memory-metadata](memory.md#mem-obj-memory-metadata), rather than treating source as authenticated authorship.

> if not self.state.include_private and raw:
>     raw = [
>         (r, s)
>         for r, s in raw
>         if not r.private or r.source == self.state.source
>     ]
> --- `lib/crewai/src/crewai/memory/recall_flow.py`

> return _as_structured(response, PreReviewResult).improved_output
> --- `lib/crewai/src/crewai/flow/human_feedback.py`

#### EPI-RTE-test-scoring
Label: Crew test scoring

CrewEvaluator installs itself as task callback, constructs an evaluator agent/task from task specification and actual output, obtains a numeric quality field, emits a result event and appends the score for reports. Different referent from training admission [RT-RTE-crew-training](runtime.md#rt-rte-crew-training): this callback reports scores rather than saving role-keyed suggestions. SRC-1 implementation, `lib/crewai/src/crewai/utilities/evaluators/crew_evaluator_handler.py`. Target: task completion, quality and performance over given task description/expected-output specification. Judge: selected LLM via evaluator agent; expected_output is specification text, not necessarily a correct reference answer. Human contribution is caller configuration, not per-score approval. Bounded test iterations do not by themselves supply a causal comparison or component intervention.

- Immediate return: callback records score/event or raises on missing task/quality.
- Later read-back: score arrays feed current test reporting; inapplicable to durable learned artifacts — none written by this inspected callback.
- Delegated visibility: evaluator receives task description, expected output, agent role/goal and raw task output.
- Selection predicate: matching task description and Pydantic numeric quality result.
- Invalidation or expiry: per-evaluator run arrays; no semantic claim withdrawal/history mechanism shown.
- Activation or effect: score event, printed task/crew averages and duration reporting; not an output acceptance gate in this callback.
- Evidence limits: source examples of score tables are not observed results; provider quality and actual comparisons unsupplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for task in self.crew.tasks:
>     task.callback = self.evaluate
> --- `lib/crewai/src/crewai/utilities/evaluators/crew_evaluator_handler.py`

> self.tasks_scores[self.iteration].append(quality_score)
> --- `lib/crewai/src/crewai/utilities/evaluators/crew_evaluator_handler.py`

#### EPI-RTE-eval-gate
Label: Remote evaluation gate

CLI eval is an additional material route omitted from the supplied runtime's selected cases. It requests a hosted evaluation of a traced execution, waits for a verdict, prints it and a possible brief, writes returned evaluation configuration and maps done/passed to normal return; otherwise it exits nonzero. Remote evaluator quality and criteria generation are not frozen implementation. The gate is distinct from [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail): it grades a run after it happened, not a TaskOutput before progression. SRC-1 implementation, `lib/cli/src/crewai_cli/cli.py` and `lib/cli/src/crewai_cli/experimental/eval_crew.py`. Caller selects run; service proposes verdict; local code decides status. No local human approval required for status consumption. Mode: post-run grading; the separate --models route dispatches deployment comparisons whose internals remain uninspected. No reference answer is supplied in this evidence.

- Immediate return: displayed verdict/brief and normal return on done/passed, nonzero exit otherwise; interruption has separate exit handling.
- Later read-back: returned evaluation configuration is passed to write_eval_config; full criteria reuse semantics uninspected.
- Delegated visibility: service receives selected execution request; local code consumes hosted verdict, not evaluator internals.
- Selection predicate: requested or recorded execution and local done/passed predicate.
- Invalidation or expiry: rerun/re-evaluate is the documented change cycle; rollback of already executed effects is not provided by this gate.
- Activation or effect: changes process exit status, permitting external CI gating; actual CI consumer not supplied.
- Evidence limits: no successful remote call, verdict instance, CI behavior or causal experiment; external hosted implementation excluded.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not _gate_passed(finished):
>     raise SystemExit(1)
> --- `lib/cli/src/crewai_cli/experimental/eval_crew.py`

> verdict = finished.get("verdict") if finished.get("status") == "done" else None
> return isinstance(verdict, dict) and str(verdict.get("gate")).lower() == "passed"
> --- `lib/cli/src/crewai_cli/experimental/eval_crew.py`

### Claims

#### EPI-CLM-memory-facts
Label: Discrete facts and adaptive recall

SRC-1 doctrine/design, `docs/edge/en/concepts/memory.mdx`, presents extraction as discrete facts and recall as relevant context injection. The overview also describes inference of scope/categories/importance and adaptive-depth composite scoring. This is a retention/context claim, not an explicit claim of infallible factual verification. No supplied counterpart: [RT-CLM-output-validation](runtime.md#rt-clm-output-validation) is a separate output-progression contract. Fact terminology must not be promoted to demonstrated truth or acceptance. Implementation is established by the extraction, consolidation and selection records; observed fidelity and causal benefit are unsupplied.

> After each task, the crew automatically extracts discrete facts from the task output and stores them. Before each task, the agent recalls relevant context from memory and injects it into the task prompt.
> --- `docs/edge/en/concepts/memory.mdx`

#### EPI-CLM-eval-exit
Label: Evaluation exit contract

SRC-1 doctrine/design in CLI eval documentation states the process status can gate CI. This is distinct from [RT-CLM-output-validation](runtime.md#rt-clm-output-validation)'s intra-task progression contract. The local predicate is inspected implementation; no CI consumer, hosted judge correctness or prevented shipment is observed.

> A run's evaluation exits 0 only when the goal gate PASSED, and 1 otherwise — a
> failed gate, no verdict, or an evaluation that could not run — so a CI job can
> gate on it. A comparison exits 0 when it finished, 1 when it failed or could
> not start.
> --- `lib/cli/src/crewai_cli/cli.py`
